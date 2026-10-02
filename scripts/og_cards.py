"""og_cards.py — a link-preview card for each case study and /method (copy-review-009 P4-D, Q-P4-5 A).

Usage: python scripts/og_cards.py              render every card into public/assets/img/og/, and point each
                                               page's og:image and og:image:alt at its card
       python scripts/og_cards.py --out DIR    render every card into DIR, to look at; touches nothing else
       python scripts/og_cards.py --check      exit 1 if any page's preview tags or card aren't right
       python scripts/og_cards.py --controls   the H1 fitter and --check, each against a planted fault

Each card is 1200x630, drawn from the page itself: the wordmark ("Thomas Cheesman"), the page's H1 unchanged,
its address, and a picture already on the page, shown whole (object-fit: contain, nothing cropped):
  - the image named in CARDS (each is the page's first image), or
  - for a page with no image, a figure on it as drawn, screenshotted from the page (the loop diagram on
    /method, the structured-data excerpt on Bare Your Rare).
The frame is og-src/og.html's: light paper, the site's type, a dark panel with the teal rule. The H1 is sized
down from 64px until it fits, and the run stops if it can't fit at 36px. Each card is rendered from the
site's own origin (a card with a blank origin loses its fonts silently), and the run stops if either face
isn't loaded. The card PNG carries the page's path and H1 as text chunks, so --check can tell a card made
for an older H1 without rendering it again. Home, Projects, Background, Contact and 404 keep the site card.
The cards are fetched only by link previews, never with the page, so they add nothing to page weight.

--check, on every page: a card page's og:image is its card, its og:image:alt is the ruled text (ALT), its
card exists, is 1200x630, and was made for this page and its current H1; every other page keeps the site
card. site_check.py runs the same check on every served page. Written 2026-10-02 for Phase 4.
"""
import base64, html, io, os, re, socketserver, sys, threading
from functools import partial
from PIL import Image, PngImagePlugin
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from site_check import CleanURLHandler, CHROMIUM

PUBLIC = os.path.abspath(os.path.join(HERE, "..", "public"))
OUT = os.path.join(PUBLIC, "assets", "img", "og")
SITE = "https://tc-ventures.ca"
SITE_CARD = SITE + "/assets/img/og-card.png"
# page (clean path) -> the picture: an image already on the page, or a CSS selector for a figure to draw
CARDS = {
    "/work/influence-graph": {"img": "/assets/img/graph-gp-budget.webp"},
    "/work/back-quarter": {"img": "/assets/img/back-quarter-3d.webp"},
    "/work/desk-and-drawer": {"img": "/assets/img/desk-hotspots.webp"},
    "/work/bare-your-rare": {"figure": "figure.excerpt"},
    "/work/gprs": {"img": "/assets/img/gprs-home.webp"},
    "/work/this-site": {"img": "/assets/img/this-site-home.webp"},
    "/method": {"figure": "figure.loop"},
}
# OG1 to OG7, ruled 2026-10-02 ("cards ok, og1-7 ok, q-og1 a"). Never edit without a copy review.
ALT = {
    "/work/influence-graph": "Thomas Cheesman: The Economic Report Influence Graph. Beside the title, a three-dimensional web of coloured spheres joined by fine lines, on a dark ground.",
    "/work/back-quarter": "Thomas Cheesman: A homepage you drive around. Beside the title, a low-polygon farmyard with an orange buggy, a white camper trailer, twin grain bins and a red barn.",
    "/work/desk-and-drawer": "Thomas Cheesman: A menu that is a photograph of my desk. Beside the title, the photograph: a curved monitor, a lit keyboard, a mug, a rubber duck and a stack of books.",
    "/work/bare-your-rare": "Thomas Cheesman: A rare-disease site, written by a patient. Beside the title, an excerpt of the site's structured data, marking a guide as a medical web page for patients.",
    "/work/gprs": "Thomas Cheesman: A housing society’s website. Beside the title, the society's home page, under the heading Accessible and Affordable Housing in Grande Prairie.",
    "/work/this-site": "Thomas Cheesman: This site. Beside the title, its home page, under the heading I run a nonprofit's website, and I hold it to a written standard.",
    "/method": "Thomas Cheesman: How AI is a tool I work with and an accessibility feature itself. Beside the title, the working loop: six steps from the brief to the next session, and the file each step writes.",
}

CARD = """<!doctype html><html><head><meta charset="utf-8"><base href="{base}/"><style>
@font-face{{font-family:'Familjen Grotesk';src:url(assets/fonts/familjen-grotesk-latin.woff2) format('woff2');font-weight:400 700}}
@font-face{{font-family:'IBM Plex Mono';src:url(assets/fonts/ibm-plex-mono-500-latin.woff2) format('woff2');font-weight:500}}
html,body{{margin:0;width:1200px;height:630px;overflow:hidden;background:#FCFCFD;color:#14181F}}
.c{{display:grid;grid-template-columns:540px 1fr;height:630px}}
.t{{padding:64px 48px 56px 72px;display:flex;flex-direction:column;min-width:0}}
.l{{font:500 17px/1 'IBM Plex Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:#5F6A79;margin:0}}
h1{{font:600 64px/1.04 'Familjen Grotesk',sans-serif;letter-spacing:-.02em;margin:28px 0 0;overflow-wrap:break-word}}
.u{{margin-top:auto;font:500 20px/1.2 'IBM Plex Mono',monospace;color:#0F5F6B}}
.f{{background:#060914;display:flex;align-items:center;justify-content:center;border-left:6px solid #0F5F6B;padding:32px}}
.f img{{max-width:100%;max-height:100%;object-fit:contain;display:block}}
</style></head><body><div class="c"><div class="t">
<p class="l">Thomas Cheesman</p>
<h1>{h1}</h1>
<p class="u">tc-ventures.ca{path}</p>
</div><div class="f"><img src="{src}" alt=""></div></div></body></html>"""

ROOM = 630 - 64 - 56 - 17 - 28 - 24 - 40   # the H1's height budget: card less padding, label, address, gap
FIT_H1 = """(room) => {
  const h = document.querySelector('h1');
  let size = 64;
  while (h.getBoundingClientRect().height > room && size > 36) { size -= 2; h.style.fontSize = size + 'px'; }
  return [size, h.getBoundingClientRect().height <= room];
}"""


def serve(root):
    srv = socketserver.TCPServer(("127.0.0.1", 0), partial(CleanURLHandler, directory=root))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"


def serve_card(card):
    """A one-argument route handler: Playwright fills a second parameter with the request, so a default
    argument there would be overwritten."""
    def handle(route):
        route.fulfill(status=200, body=card, headers={"Content-Type": "text/html; charset=utf-8"})
    return handle


def text_of(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def page_file(path):
    return os.path.join(PUBLIC, path.strip("/") + ".html")


def slug(path):
    return path.strip("/").replace("/", "-")


def card_url(path):
    return f"{SITE}/assets/img/og/{slug(path)}.png"


def h1_html(page):
    return re.search(r"<h1[^>]*>(.*?)</h1>", page, re.S).group(1).strip()


def draw(browser, base, path, pic, h1):
    """(PNG bytes, H1 size, fits) for one card; h1 is the H1's HTML."""
    if "img" in pic:
        if pic["img"] not in open(page_file(path), encoding="utf-8").read():
            sys.exit(f"{path}: {pic['img']} isn't on the page; CARDS is out of date")
        src = pic["img"].lstrip("/")
    else:   # the figure as the page draws it: light theme, motion off
        ctx = browser.new_context(viewport={"width": 1280, "height": 900}, device_scale_factor=2,
                                  color_scheme="light", reduced_motion="reduce")
        pg = ctx.new_page()
        pg.goto(base + path, wait_until="networkidle")
        pg.evaluate("document.fonts.ready.then(() => 0)")
        png = pg.locator(pic["figure"]).first.screenshot(animations="disabled")
        ctx.close()
        src = "data:image/png;base64," + base64.b64encode(png).decode()
    ctx = browser.new_context(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
    pg = ctx.new_page()
    pg.route(base + "/__og-card", serve_card(CARD.format(base=base, h1=h1, path=path, src=src)))
    pg.goto(base + "/__og-card", wait_until="networkidle")
    pg.evaluate("document.fonts.ready.then(() => 0)")
    fams = pg.evaluate("[...document.fonts].filter(f => f.status === 'loaded').map(f => f.family)")
    if not any("Familjen" in f for f in fams) or not any("Plex" in f for f in fams):
        sys.exit(f"{path}: the card's fonts didn't load ({fams})")
    size, fits = pg.evaluate(FIT_H1, ROOM)
    png = pg.screenshot()
    ctx.close()
    return png, size, fits


def with_chunks(png, path, h1):
    """The PNG re-saved with the page's path and plain-text H1 in it."""
    info = PngImagePlugin.PngInfo()
    info.add_text("Page", path)
    info.add_text("Title", text_of(h1))
    out = io.BytesIO()
    Image.open(io.BytesIO(png)).save(out, "PNG", pnginfo=info, optimize=True)
    return out.getvalue()


def render(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    srv, base = serve(PUBLIC)
    sizes = {}
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch(executable_path=CHROMIUM if os.path.exists(CHROMIUM) else None)
            for path, pic in CARDS.items():
                h1 = h1_html(open(page_file(path), encoding="utf-8").read())
                png, size, fits = draw(b, base, path, pic, h1)
                if not fits:
                    sys.exit(f"{path}: the H1 doesn't fit the card even at 36px")
                sizes[path] = size
                with open(os.path.join(out_dir, slug(path) + ".png"), "wb") as f:
                    f.write(with_chunks(png, path, h1))
            b.close()
    finally:
        srv.shutdown()
    return sizes


def attr(s):
    return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def set_meta(page, prop, value):
    new, n = re.subn(rf'(<meta property="{re.escape(prop)}" content=")[^"]*(")',
                     lambda m: m.group(1) + attr(value) + m.group(2), page, count=1)
    if n != 1:
        sys.exit(f"no {prop} tag to set")
    return new


def write_tags():
    changed = []
    for path in CARDS:
        f = page_file(path)
        raw = open(f, encoding="utf-8", newline="").read()
        page = set_meta(set_meta(raw, "og:image", card_url(path)), "og:image:alt", ALT[path])
        if page != raw:
            open(f, "w", encoding="utf-8", newline="").write(page)
            changed.append(path)
    return changed


def meta(page, prop):
    m = re.search(rf'<meta property="{re.escape(prop)}" content="([^"]*)"', page)
    return html.unescape(m.group(1)) if m else None


def problems(path, page, image_bytes):
    """What --check fails on for one page; image_bytes(url) returns the card's bytes, or None."""
    out = []
    if path not in CARDS:
        if meta(page, "og:image") not in (SITE_CARD, None):
            out.append(f"og:image is {meta(page, 'og:image')}, not the site card")
        return out
    if meta(page, "og:image") != card_url(path):
        out.append(f"og:image is {meta(page, 'og:image')}, not its card")
    if meta(page, "og:image:alt") != ALT[path]:
        out.append("og:image:alt isn't the ruled text")
    if (meta(page, "og:image:width"), meta(page, "og:image:height")) != ("1200", "630"):
        out.append("og:image width and height aren't 1200 and 630")
    data = image_bytes(card_url(path))   # bytes; None for a 404; or another HTTP status, as a number
    if data is None:
        return out + ["the card isn't there (404)"]
    if isinstance(data, int):
        return out + [f"the card answered {data}"]
    im = Image.open(io.BytesIO(data))
    if im.size != (1200, 630):
        out.append(f"the card is {im.size}, not 1200x630")
    chunks = getattr(im, "text", {}) or {}
    if chunks.get("Page") != path or chunks.get("Title") != text_of(h1_html(page)):
        out.append(f"the card was made for {chunks.get('Page')!r}, {chunks.get('Title')!r}: re-run og_cards.py")
    return out


def local_image(url):
    f = os.path.join(PUBLIC, url[len(SITE) + 1:].replace("/", os.sep))
    return open(f, "rb").read() if os.path.exists(f) else None



def pages():
    out = {"/" if f == "index.html" else "/" + f[:-5]: os.path.join(PUBLIC, f)
           for f in sorted(os.listdir(PUBLIC)) if f.endswith(".html")}
    work = os.path.join(PUBLIC, "work")
    out.update({"/work/" + f[:-5]: os.path.join(work, f) for f in sorted(os.listdir(work))
                if f.endswith(".html") and not f.startswith("_")})
    return out


def controls():
    ok = True
    def say(name, good):
        nonlocal ok
        ok &= good
        print(("PASS " if good else "FAIL ") + "control: " + name)
    # The fitter, never needed by the seven H1s: a long one must shrink and fit; a far longer one mustn't fit
    # Measured 2026-10-02: /method's H1 twice shrinks to 50px and fits; eight times doesn't fit at 36px.
    # (Four times still fits at 36px.)
    long_h1 = "How AI is a tool I work with and an accessibility feature itself; " * 2
    srv, base = serve(PUBLIC)
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch(executable_path=CHROMIUM if os.path.exists(CHROMIUM) else None)
            _, size, fits = draw(b, base, "/method", CARDS["/method"], long_h1)
            say(f"a long H1 shrinks to fit (at {size}px)", size < 64 and fits)
            _, size, fits = draw(b, base, "/method", CARDS["/method"], long_h1 * 4)
            say("a far longer H1 is reported as not fitting", not fits)
            b.close()
    finally:
        srv.shutdown()
    # --check against planted faults, on /work/gprs
    path = "/work/gprs"
    page = open(page_file(path), encoding="utf-8").read()
    say("the page passes as it is", problems(path, page, local_image) == [])
    bent = set_meta(page, "og:image:alt", ALT[path] + " x")
    say("a changed og:image:alt is caught", "og:image:alt isn't the ruled text" in problems(path, bent, local_image))
    # in the <h1> itself: the same words come first in <title>, so a plain replace would miss the H1
    renamed = re.sub(r"(<h1[^>]*>).*?(</h1>)", r"\1A housing society’s web site\2", page, count=1, flags=re.S)
    say("a card made for an older H1 is caught", any("made for" in p for p in problems(path, renamed, local_image)))
    say("a missing card is caught", "the card isn't there (404)" in problems(path, page, lambda u: None))
    say("a card refused (403) is reported as 403", "the card answered 403" in problems(path, page, lambda u: 403))
    return ok


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the Windows console is cp1252
    args = sys.argv[1:]
    if "--controls" in args:
        sys.exit(0 if controls() else 1)
    if "--check" in args:
        bad = 0
        for path, f in pages().items():
            for prob in problems(path, open(f, encoding="utf-8").read(), local_image):
                print(f"FAIL {path}: {prob}")
                bad += 1
        print("ok: every page's link preview is right" if not bad else f"{bad} problem(s)")
        sys.exit(1 if bad else 0)
    out = args[args.index("--out") + 1] if "--out" in args else OUT
    for path, size in render(out).items():
        print(f"{path}: H1 at {size}px")
    print(f"wrote {len(CARDS)} cards to {out}")
    if "--out" not in args:
        changed = write_tags()
        print("tags: " + (", ".join(changed) if changed else "nothing changed"))


if __name__ == "__main__":
    main()
