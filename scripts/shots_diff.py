"""shots_diff.py — prove a change is invisible: every page, pixel for pixel, before and after.

Usage: python scripts/shots_diff.py BEFORE [AFTER] [--out DIR] [--inject CSS] [--self]

BEFORE and AFTER are copies of public/ (AFTER defaults to this repo's public/).
For the tree on main:  git archive origin/main public | tar -x -C DIR   (then pass DIR/public)

Pages come from BEFORE's sitemap, plus /404. Each page is shot whole, light and
dark, 1280 and 375px wide, from both trees, and each pair is compared pixel for
pixel. "Same" means identical images, not similar ones. So that two shots of an
unchanged page come out identical:
  - the clock is fixed (the contact page shows the local time)
  - CSS animations are held at their start (the 404's drift), and no caret shows
  - motion is reduced, so the home page's 3D ledger is drawn whole and still, and the shot waits
    for it to draw and fade in
  - lazy images are made eager and decoded before the shot (a lazy, async
    image can otherwise paint as an empty box in a full-page shot), and the
    fonts are waited for

Controls, run both before trusting a pass (CLAUDE.md rule 3):
  --self          compares BEFORE with itself: every pair must be the same, or
                  the shots aren't stable enough to prove anything
  --inject CSS    adds CSS to the AFTER pages only: a one-pixel change must be
                  found on every page it touches

A pass says the pages render identically at those four settings, in this
Chromium. It says nothing about other browsers, other settings, or how a page
looks. Exit 1 if any pair differs; --out DIR keeps each differing pair and a
picture of where they differ. Written 2026-09-29 for Phase 3 step 2
(copy-review-007 P3-0 section 6).
"""
import io, os, re, socketserver, sys, threading
from functools import partial
from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from site_check import CleanURLHandler, CHROMIUM

WIDTHS, SCHEMES = (1280, 375), ("light", "dark")
CLOCK = "2026-09-29T12:00:00"
SETTLE = """async () => {
  const imgs = [...document.images];
  imgs.forEach(i => { i.loading = 'eager'; i.decoding = 'sync'; });
  await Promise.all(imgs.map(i => i.complete && i.naturalWidth ? 0 :
    new Promise(r => { i.addEventListener('load', r, {once: true}); i.addEventListener('error', r, {once: true}); })));
  await Promise.all(imgs.map(i => i.decode().catch(() => 0)));
  await document.fonts.ready;
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
}"""


def serve(root):
    srv = socketserver.TCPServer(("127.0.0.1", 0), partial(CleanURLHandler, directory=os.path.abspath(root)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"


# The home page's 3D ledger (copy-review-010) is drawn by script; under Full its opening runs on real time, so
# two shots never matched. Shots are taken with reduced motion (the scene drawn whole and still) once it has
# drawn and faded in. Added 2026-10-02, after --self found home at 1280 differing from itself.
SCENE_SETTLE = """async () => {
  const r = document.documentElement;
  for (let i = 0; i < 100 && r.hasAttribute('data-lg-scene') && r.getAttribute('data-lg-scene') !== 'on'; i++)
    await new Promise(f => setTimeout(f, 50));
  if (r.getAttribute('data-lg-scene') === 'on') await new Promise(f => setTimeout(f, 1500));
}"""


def shot(browser, url, width, scheme, inject=None):
    ctx = browser.new_context(viewport={"width": width, "height": 900}, color_scheme=scheme, reduced_motion="reduce")
    page = ctx.new_page()
    page.clock.set_fixed_time(CLOCK)
    page.goto(url, wait_until="networkidle")
    if inject:
        page.add_style_tag(content=inject)
    page.evaluate(SETTLE)
    page.evaluate(SCENE_SETTLE)
    png = page.screenshot(full_page=True, animations="disabled", caret="hide")
    ctx.close()
    return png


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the Windows console is cp1252
    args = sys.argv[1:]
    opt = lambda k: args[args.index(k) + 1] if k in args else None
    out, inject = opt("--out"), opt("--inject")
    pos = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] not in ("--out", "--inject"))]
    if not pos:
        sys.exit(__doc__)
    before = pos[0]
    after = before if "--self" in args else (pos[1] if len(pos) > 1 else os.path.join(HERE, "..", "public"))
    sitemap = open(os.path.join(before, "sitemap.xml"), encoding="utf-8").read()
    paths = [re.sub(r"^https://tc-ventures\.ca", "", u) or "/" for u in re.findall(r"<loc>([^<]+)</loc>", sitemap)] + ["/404"]
    (sb, ub), (sa, ua) = serve(before), serve(after)
    same, diff = 0, []
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROMIUM if os.path.exists(CHROMIUM) else None)
        for path in paths:
            for width in WIDTHS:
                for scheme in SCHEMES:
                    a = shot(browser, ub + path, width, scheme)
                    b = shot(browser, ua + path, width, scheme, inject)
                    name = f"{path.strip('/').replace('/', '_') or 'home'}-{width}-{scheme}"
                    if a == b:
                        same += 1
                        continue
                    if out:
                        os.makedirs(out, exist_ok=True)
                    ia, ib = Image.open(io.BytesIO(a)).convert("RGB"), Image.open(io.BytesIO(b)).convert("RGB")
                    if ia.size != ib.size:
                        why = f"size {ia.size} -> {ib.size}"
                    else:
                        d = ImageChops.difference(ia, ib)
                        box = d.getbbox()
                        if box is None:      # same pixels, different PNG bytes
                            same += 1
                            continue
                        r, g, bl = d.split()
                        mask = ImageChops.lighter(ImageChops.lighter(r, g), bl).point(lambda v: 255 if v else 0)
                        why = f"{mask.histogram()[255]} pixels differ, within {box}"
                        if out:
                            mask.save(os.path.join(out, name + "-where.png"))
                    diff.append(f"{name}: {why}")
                    if out:
                        ia.save(os.path.join(out, name + "-before.png"))
                        ib.save(os.path.join(out, name + "-after.png"))
        browser.close()
    sb.shutdown(); sa.shutdown()
    for d in diff:
        print("DIFFERS " + d)
    total = same + len(diff)
    print(f"{len(paths)} pages x {len(WIDTHS)} widths x {len(SCHEMES)} schemes: {same} of {total} pairs identical"
          + (" (BEFORE against itself)" if "--self" in args else "") + (f" (injected into AFTER: {inject})" if inject else ""))
    sys.exit(0 if not diff and total else 1)


if __name__ == "__main__":
    main()
