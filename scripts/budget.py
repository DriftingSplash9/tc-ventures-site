"""budget.py — page weight and automated accessibility rules for every page of tc-ventures.ca.

Usage: python scripts/budget.py              (serves ./public locally)
       python scripts/budget.py --live       (measures https://tc-ventures.ca as served)
       python scripts/budget.py --root DIR   (another copy of public/)
       python scripts/budget.py --controls   (plants two faults in a copy of public/; both must be caught)
       add -v to print every PASS; --no-a11y to skip the accessibility rules

Pages come from public/sitemap.xml, plus /404. For each page, at 1280 and 375px wide, in a fresh browser
with an empty cache:
  - "first load": what the page fetches before any click or scroll
  - "page": the same once scrolled to the end, so the lazy images are in. This is the page's weight, and
    the ceiling applies to it (the larger of the two widths).
Bytes are the site's own files (same origin), as decoded: the size of the files themselves, so the local
and live numbers match. Requests to other origins (Cloudflare's analytics beacon, live only) are counted
apart and never in the ceiling. --live also reports what crossed the wire (compressed), which is what a
reader downloads. 1 kB = 1000 bytes, as Chrome's DevTools counts.

The graph: on /work/influence-graph, a click on "Load the live graph" fetches the 3D library and the data.
Those bytes are reported on their own, not counted in the page (copy-review-009 P4-A).

Checks (exit 1 if any fails):
  - every page in the sitemap has a ceiling in CEILINGS, and its weight is at or under it
  - accessibility: axe-core's WCAG 2.0, 2.1 and 2.2 A and AA rules on every page, light and dark, with
    motion reduced so the page is whole; any violation fails. "Needs review" results are counted with -v,
    and don't fail. axe-core is the pinned copy in scripts/vendor/axe-core/, checked against AXE_SHA512
    first, so an edited or replaced copy fails the run. It's a tool for this check, never deployed.
  - known faults (KNOWN): a violation logged in an open item, by page and rule. It isn't counted and
    doesn't fail the run; the summary names it, and -v prints each as KNOWN. The day it stops showing, the
    run fails until its line comes off KNOWN, so a fixed fault can't go on being excused. Now: A-1's
    nested-interactive on the two loop diagrams (Q-P4-9 A).

Controls (CLAUDE.md rule 3), --controls: a copy of public/ with three faults planted, measured on the pages
they touch and /background, left alone:
  - a heavy image added to /contact: its ceiling must fail
  - the alt text taken off /work/gprs's first image: its accessibility rules must fail, light and dark
  - /method's loop diagram fixed (role="img" taken off): its known fault must fail as "passes now"
and nothing else may fail. Only those pages, so a fault elsewhere can't blur the result.

A ceiling is a ruled number (Q-P4-2 A, copy-review-009): raising one is a change Thomas rules, recorded
next to it. Written 2026-10-01 for Phase 4 (P4-A).
"""
import base64, hashlib, math, os, re, shutil, socketserver, sys, tempfile, threading
from functools import partial
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from site_check import CleanURLHandler, CHROMIUM

LIVE = "https://tc-ventures.ca"
WIDTHS = (1280, 375)
AXE = os.path.join(HERE, "vendor", "axe-core", "axe.min.js")
# axe-core 4.11.4 from cdnjs, the sha512 cdnjs publishes for it (fetched 2026-10-01)
AXE_SHA512 = "QfFHXx4S3wB2zSlH0uAam/F3gYphMSJBlGy9O9gfKSgRWlOBszxKkMh/78TrN/nZK534NoFtG2eCIUtdkMQUQw=="
AXE_TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"]
CONTROL_PAGES = ("/contact", "/work/gprs", "/background", "/method")
# Ceilings in kB, on the "page" weight: the weight measured locally at 91e2b71, plus 10%, rounded up to the
# next 10 kB. Ruled Q-P4-8 A, 2026-10-01. The home page grows a little with each ledger column.
# "/" raised from 390 to 1320 for the 3D ledger hero (Three.js, 808 kB decoded): measured locally at
# 1,199 kB on 2026-10-02, by the same rule. Ruled Q-S4-1 A, copy-review-010, 2026-10-02.
CEILINGS = {
    "/": 1320, "/projects": 720, "/work/influence-graph": 670, "/work/back-quarter": 360,
    "/work/desk-and-drawer": 480, "/work/bare-your-rare": 300, "/work/gprs": 530, "/work/this-site": 400,
    "/method": 310, "/background": 290, "/contact": 290, "/404": 280,
}
CEILINGS_RULED = "Q-P4-8 A, 2026-10-01; '/' Q-S4-1 A, 2026-10-02"
# Known faults: (page, axe rule) -> the open item that owns the fix. Ruled Q-P4-9 A, 2026-10-01. A known
# violation isn't counted; any other violation on the same page still fails. The day one stops showing,
# the run fails until its line comes off.
KNOWN = {
    ("/method", "nested-interactive"): "A-1",           # the loop diagram: links inside <svg role="img">
    ("/work/this-site", "nested-interactive"): "A-1",   # the same, on this site's loop
}

SCROLL_TO_END = """async () => {
  const step = Math.max(200, innerHeight - 100);
  for (let y = 0; y < document.documentElement.scrollHeight; y += step) {
    scrollTo(0, y);
    await new Promise(r => setTimeout(r, 120));
  }
  scrollTo(0, document.documentElement.scrollHeight);
  await new Promise(r => setTimeout(r, 300));
  const imgs = [...document.images];
  await Promise.all(imgs.map(i => i.complete ? 0 :
    new Promise(r => { i.addEventListener('load', r, {once: true}); i.addEventListener('error', r, {once: true}); })));
}"""

RUN_AXE = """async (tags) => {
  const r = await axe.run(document, {runOnly: {type: 'tag', values: tags}, resultTypes: ['violations', 'incomplete']});
  const pick = v => ({id: v.id, impact: v.impact, n: v.nodes.length,
                      at: v.nodes.slice(0, 3).map(n => n.target.join(' '))});
  return {violations: r.violations.map(pick), incomplete: r.incomplete.map(pick)};
}"""


def kb(n):
    return n / 1000


def serve(root):
    srv = socketserver.TCPServer(("127.0.0.1", 0), partial(CleanURLHandler, directory=os.path.abspath(root)))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"


def sitemap_paths(root):
    text = open(os.path.join(root, "sitemap.xml"), encoding="utf-8").read()
    return [re.sub(r"^https://tc-ventures\.ca", "", u) or "/" for u in re.findall(r"<loc>([^<]+)</loc>", text)]


def tally(reqs, origin):
    """The finished requests, split into the site's own and everyone else's."""
    t = {"own": 0, "wire": 0, "reqs": 0, "other": 0, "other_reqs": 0}
    for req in reqs:
        resp = req.response()
        if resp is None:
            continue
        try:
            body = len(resp.body())
        except Exception:
            body = 0
        if req.url.startswith(origin):
            t["own"] += body
            t["wire"] += req.sizes().get("responseBodySize", 0) or 0
            t["reqs"] += 1
        else:
            t["other"] += body
            t["other_reqs"] += 1
    return t


def measure(browser, base, path, width, graph=False):
    ctx = browser.new_context(viewport={"width": width, "height": 900})
    page = ctx.new_page()
    done = []   # summed after, outside the event handler
    page.on("requestfinished", lambda r: done.append(r))   # Playwright can't wrap a bound builtin
    page.goto(base + path, wait_until="networkidle")
    n_first = len(done)
    page.evaluate(SCROLL_TO_END)
    page.wait_for_timeout(500)
    n_full = len(done)
    if graph:
        btn = page.locator(".gd__load")
        btn.scroll_into_view_if_needed()
        btn.click()
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1500)
    first, full = tally(done[:n_first], base), tally(done[:n_full], base)
    extra = tally(done[n_full:], base) if graph else None
    ctx.close()
    return first, full, extra


def axe_run(browser, base, path, scheme):
    ctx = browser.new_context(viewport={"width": 1280, "height": 900}, color_scheme=scheme,
                              reduced_motion="reduce", bypass_csp=True)
    page = ctx.new_page()
    page.goto(base + path, wait_until="networkidle")
    page.evaluate("document.fonts.ready.then(() => 0)")
    page.add_script_tag(path=AXE)
    res = page.evaluate(RUN_AXE, AXE_TAGS)
    ctx.close()
    return res


def run(root, base, live, verbose, a11y, only=None):
    """Measure every page (or only those named); return (failures, passes, known faults seen)."""
    fails, passes, known = [], [], []
    def check(name, ok, detail=""):
        (passes if ok else fails).append(name)
        if not ok or verbose:
            print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""), flush=True)

    paths = sitemap_paths(root) + ["/404"]
    if only:
        paths = [p for p in paths if p in only]
    for p in paths:
        check(f"ceiling set: {p}", p in CEILINGS, "" if p in CEILINGS else "no ceiling in CEILINGS")

    rows, graph_extra = [], None
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROMIUM if os.path.exists(CHROMIUM) else None)
        for p in paths:
            per = {}
            for w in WIDTHS:
                first, full, extra = measure(browser, base, p, w, graph=(p == "/work/influence-graph" and w == 1280))
                per[w] = (first, full)
                if extra:
                    graph_extra = extra
            weight = max(per[w][1]["own"] for w in WIDTHS)
            rows.append((p, per, weight))
            if p in CEILINGS:   # a missing ceiling already failed above
                check(f"weight: {p}", kb(weight) <= CEILINGS[p],
                      f"{kb(weight):.0f} kB, ceiling {CEILINGS[p]} kB")
        if a11y:
            for p in paths:
                for scheme in ("light", "dark"):
                    r = axe_run(browser, base, p, scheme)
                    v = r["violations"]
                    mine = [x for x in v if (p, x["id"]) not in KNOWN]
                    detail = "; ".join(f"{x['id']} ({x['impact']}) x{x['n']}: {', '.join(x['at'])}" for x in mine)
                    check(f"accessibility: {p} {scheme}", not mine, detail)
                    for (kp, rule), item in KNOWN.items():
                        if kp != p:
                            continue
                        if any(x["id"] == rule for x in v):
                            known.append(f"{item} {rule} {p}")
                            if verbose:
                                print(f"KNOWN accessibility: {p} {scheme}  [{rule}] ({item})", flush=True)
                        else:
                            check(f"known fault fixed: {p} {scheme} {rule}", False,
                                  f"passes now: take its {item} line off KNOWN")
                    if verbose and r["incomplete"]:
                        print(f"  needs review, {p} {scheme}: " +
                              "; ".join(f"{x['id']} x{x['n']}" for x in r["incomplete"]))
        browser.close()

    print()
    hdr = f"{'page':24} {'first load 1280':>16} {'first 375':>10} {'page':>8} {'reqs':>5}"
    if live:
        hdr += f" {'on the wire':>12} {'other origins':>14}"
    hdr += f" {'ceiling':>8}"
    print(hdr)
    for p, per, weight in rows:
        line = (f"{p:24} {kb(per[1280][0]['own']):>13.0f} kB {kb(per[375][0]['own']):>7.0f} kB "
                f"{kb(weight):>5.0f} kB {per[1280][1]['reqs']:>5}")
        if live:
            line += f" {kb(per[1280][1]['wire']):>9.0f} kB {kb(per[1280][1]['other']):>8.0f} kB ({per[1280][1]['other_reqs']})"
        line += f" {str(CEILINGS.get(p, '-')):>5} kB" if p in CEILINGS else f" {'-':>8}"
        print(line)
    if graph_extra:
        print(f"\nthe graph, after its click (not in the page): {kb(graph_extra['own']):.0f} kB in "
              f"{graph_extra['reqs']} requests" + (f", {kb(graph_extra['wire']):.0f} kB on the wire" if live else ""))
    return fails, passes, known


def plant_controls(src):
    """A copy of public/ with three faults: a heavy image on /contact, an image without alt on /work/gprs,
    and /method's loop diagram fixed, so its known fault stops showing."""
    tmp = tempfile.mkdtemp(prefix="budget-controls-")
    dst = os.path.join(tmp, "public")
    shutil.copytree(src, dst)
    shutil.copy(os.path.join(dst, "assets", "img", "graph-app-ui.webp"),
                os.path.join(dst, "assets", "img", "control-heavy.webp"))
    c = os.path.join(dst, "contact.html")
    html = open(c, encoding="utf-8").read()
    html2 = html.replace("</main>", '<img src="/assets/img/control-heavy.webp" width="10" height="10" alt=""></main>', 1)
    g = os.path.join(dst, "work", "gprs.html")
    gh = open(g, encoding="utf-8").read()
    gh2 = re.sub(r'(<img src="/assets/img/gprs-home\.webp"[^>]*?)\s+alt="[^"]*"', r"\1", gh, count=1, flags=re.S)
    m = os.path.join(dst, "method.html")
    mh = open(m, encoding="utf-8").read()
    mh2 = mh.replace('<svg viewBox="0 0 880 284" role="img"', '<svg viewBox="0 0 880 284"', 1)
    if html2 == html or gh2 == gh or mh2 == mh:
        sys.exit("controls: could not plant a fault (the pages changed); fix plant_controls")
    open(c, "w", encoding="utf-8").write(html2)
    open(g, "w", encoding="utf-8").write(gh2)
    open(m, "w", encoding="utf-8").write(mh2)
    return tmp, dst


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the Windows console is cp1252
    args = sys.argv[1:]
    verbose, a11y, live = "-v" in args, "--no-a11y" not in args, "--live" in args
    root = args[args.index("--root") + 1] if "--root" in args else os.path.join(HERE, "..", "public")

    if a11y:
        got = base64.b64encode(hashlib.sha512(open(AXE, "rb").read()).digest()).decode()
        if got != AXE_SHA512:
            sys.exit(f"FAIL axe-core: {AXE} is not the pinned copy (sha512 {got[:16]}...)")
    if CEILINGS and not CEILINGS_RULED:
        print("note: the ceilings are proposed, not ruled (copy-review-009)\n")

    if "--controls" in args:
        tmp, dst = plant_controls(root)
        srv, base = serve(dst)
        try:   # the planted pages, and one left alone that must pass
            fails, _, _ = run(dst, base, False, verbose, a11y, only=CONTROL_PAGES)
        finally:
            srv.shutdown()
            shutil.rmtree(tmp, ignore_errors=True)
        want = {"weight: /contact"} | ({"accessibility: /work/gprs light", "accessibility: /work/gprs dark",
                                       "known fault fixed: /method light nested-interactive",
                                       "known fault fixed: /method dark nested-interactive"} if a11y else set())
        got = set(fails)
        print()
        if got == want:
            print(f"controls: OK, the {len(want)} planted faults failed and nothing else did")
            sys.exit(0)
        print(f"controls: FAILED. Missed: {sorted(want - got) or 'none'}. Unexpected: {sorted(got - want) or 'none'}")
        sys.exit(1)

    srv = None
    if live:
        base = LIVE
    else:
        srv, base = serve(root)
    try:
        fails, passes, known = run(root, base, live, verbose, a11y)
    finally:
        if srv:
            srv.shutdown()
    print(f"\n{len(passes)} of {len(passes) + len(fails)} checks passed")
    if known:
        print(f"known faults, not counted ({len(known)}): " + "; ".join(sorted(set(known))) + ", light and dark")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
