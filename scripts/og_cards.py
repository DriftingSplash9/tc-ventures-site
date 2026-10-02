"""og_cards.py — a link-preview card for each case study and /method (copy-review-009 P4-D, Q-P4-5 A).

Usage: python scripts/og_cards.py --out DIR   render every card into DIR, to look at; touches nothing else
       python scripts/og_cards.py             render into public/assets/img/og/ and point each page's
                                              og:image and og:image:alt at its card (refused until the alt
                                              text is ruled: ALT_RULED)
       python scripts/og_cards.py --check     exit 1 if a page's og tags or card aren't what this writes

Each card is 1200x630, drawn from the page itself: the wordmark ("Thomas Cheesman"), the page's H1 unchanged,
its address, and a picture already on the page, shown whole (object-fit: contain, nothing cropped):
  - the image named in CARDS (each is the page's first image), or
  - for a page with no image, a figure on it as drawn, screenshotted from the page (the loop diagram on
    /method, the structured-data excerpt on Bare Your Rare).
The card's frame is og-src/og.html's: light paper, the type, a dark panel with the teal rule for the
picture. The H1 is sized down until it fits. Home, Projects, Background, Contact and 404 keep the site card.
The cards are fetched only by link previews, never with the page, so they add nothing to page weight.
Written 2026-10-02 for Phase 4.
"""
import base64, html, os, re, socketserver, sys, threading
from functools import partial
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from site_check import CleanURLHandler, CHROMIUM

PUBLIC = os.path.abspath(os.path.join(HERE, "..", "public"))
OUT = os.path.join(PUBLIC, "assets", "img", "og")
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
ALT = {}            # OG1 to OG7, filled once ruled (copy-review-009)
ALT_RULED = None

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

FIT_H1 = """() => {
  const h = document.querySelector('h1'), room = 630 - 64 - 56 - 17 - 28 - 24 - 40;
  let size = 64;
  while (h.getBoundingClientRect().height > room && size > 36) { size -= 2; h.style.fontSize = size + 'px'; }
  return size;
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


def page_file(path):
    return os.path.join(PUBLIC, path.strip("/") + ".html")


def h1_of(path):
    t = open(page_file(path), encoding="utf-8").read()
    return re.search(r"<h1[^>]*>(.*?)</h1>", t, re.S).group(1).strip()


def render(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    srv, base = serve(PUBLIC)
    sizes = {}
    try:
        with sync_playwright() as pw:
            b = pw.chromium.launch(executable_path=CHROMIUM if os.path.exists(CHROMIUM) else None)
            for path, pic in CARDS.items():
                if "img" in pic:
                    if pic["img"] not in open(page_file(path), encoding="utf-8").read():
                        sys.exit(f"{path}: {pic['img']} isn't on the page; CARDS is out of date")
                    src = pic["img"].lstrip("/")
                else:   # draw the figure as the page shows it, light theme, motion off
                    ctx = b.new_context(viewport={"width": 1280, "height": 900}, device_scale_factor=2,
                                        color_scheme="light", reduced_motion="reduce")
                    pg = ctx.new_page()
                    pg.goto(base + path, wait_until="networkidle")
                    pg.evaluate("document.fonts.ready.then(() => 0)")
                    png = pg.locator(pic["figure"]).first.screenshot(animations="disabled")
                    ctx.close()
                    src = "data:image/png;base64," + base64.b64encode(png).decode()
                ctx = b.new_context(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
                pg = ctx.new_page()
                # Served from the site's own origin: a card set with set_content() has a blank origin, and the
                # fonts, fetched cross-origin, silently fall back (found 2026-10-02)
                card = CARD.format(base=base, h1=h1_of(path), path=path, src=src)
                pg.route(base + "/__og-card", serve_card(card))
                pg.goto(base + "/__og-card", wait_until="networkidle")
                pg.evaluate("document.fonts.ready.then(() => 0)")
                fams = pg.evaluate("[...document.fonts].filter(f => f.status === 'loaded').map(f => f.family)")
                if not any("Familjen" in f for f in fams) or not any("Plex" in f for f in fams):
                    sys.exit(f"{path}: the card's fonts didn't load ({fams})")
                sizes[path] = pg.evaluate(FIT_H1)
                pg.screenshot(path=os.path.join(out_dir, path.strip("/").replace("/", "-") + ".png"))
                ctx.close()
            b.close()
    finally:
        srv.shutdown()
    return sizes


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the Windows console is cp1252
    args = sys.argv[1:]
    if "--out" in args:
        out = args[args.index("--out") + 1]
        for path, size in render(out).items():
            print(f"{path}: H1 at {size}px")
        print(f"wrote {len(CARDS)} cards to {out}")
        return
    if not ALT_RULED:
        sys.exit("refused: the cards' alt text (OG1 onward, copy-review-009) isn't ruled; use --out DIR to preview")
    sys.exit("not built yet: writing the og tags comes after the alt text is ruled")


if __name__ == "__main__":
    main()
