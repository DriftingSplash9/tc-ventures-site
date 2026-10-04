"""site_check.py — check every page of tc-ventures.ca in a real browser.

Usage: python scripts/site_check.py            (serves ./public locally)
       python scripts/site_check.py --live     (checks https://tc-ventures.ca)
       python scripts/site_check.py --root DIR (serves another copy of public/,
                                                e.g. an older commit, as a
                                                negative control)
       add --draft-ledger for a preview whose ledger carries unruled lines
       add --chrome to run every check in the installed Google Chrome, Thomas's
                                                browser, instead of Playwright's
                                                Chromium (run it too after a
                                                Chrome update)

Pages come from public/sitemap.xml, plus /404. For each page:
  - status 200, and a made-up URL gives 404 (negative control)
  - the Projects sub-menu lists exactly SUBMENU, in order, with its labels
  - aria-current: "page" on the sub-menu link of the page you're on (case
    studies only); on Projects, "page" for /projects and "true" for every
    /work/ page
  - no noindex (except /404, which carries it on purpose) and no draft banner
  - no console errors, and no sideways scroll at 375px
  - text grows with the browser's text size: with the root size doubled, every
    element with text of its own, outside SVG, is larger than before (a size
    left in px stays put and fails). Screen-reader-only text (.sr-only) is
    left out: it is never seen, and the one in the sub-menu button takes the
    browser's fixed button size.
  - the Display button shows
  - no sideways scroll with Larger text at 1280 and 375px
  - no sideways scroll with the browser's text at 200%, at 375, 480, 760 and
    1280px, with the sub-menu shut and open (DESIGN-3 and DESIGN-4, fixed in
    Phase 3 step 4). The size is set as the browser's own text-size setting
    sets it (CDP Page.setFontSizes), so em breakpoints respond as they would
    for a reader; a :root font-size override doesn't reach media queries.
  - at 375px, a click on the sub-menu toggle opens it, and with it open the
    page still doesn't scroll sideways (DESIGN-1, fixed in Phase 3 step 4)
And once, on the home page: Tab reaches the sub-menu toggle, Enter opens it,
Esc closes it and returns focus. Then the build ledger (copy-review-006):
  - the served ledger block is exactly what scripts/export-ledger.py would
    write now, so a stale or unshipped ledger fails
  - the landscape picture shows at 1280px and the portrait one at 375px
  - with JavaScript off, the list opens and every line links a handoff file
    that exists in the repo, numbered from 001 without gaps
Then the theme, on the home page (copy-review-007, Phase 3):
  - data-theme="dark" on <html> gives exactly the colours the OS's dark mode
    gives, and data-theme="light" gives the light ones even on a dark OS
  - contrast, from the colours the browser resolves: every text colour token on
    both grounds, and the solid button's text, is 4.5:1 or more, light and dark
And the Display panel (copy-review-007, Phase 3):
  - by keyboard: Tab reaches the button, Enter opens the panel, Tab enters it,
    an arrow key picks Full, marks <html> and saves it, Esc closes and returns
    focus
  - a choice (Dark) applies at once, carries to the next page, and is on
    <html> before that page's first paint
  - motion: the caret, the button fades and the 404's drift take the ruled
    times at every level, chosen and under System with and without the OS's
    "reduce motion"; under Off nothing is animating, with the menu and the
    panel open (under Full the drift runs: the control)
  - contrast More, light and dark: the choice and the OS's "more contrast" give
    the same colours, Standard undoes it, and text reaches 7:1, rules 3:1
  - with JavaScript off: no button, and the OS's dark mode still applies
And the motion (copy-review-007, Phase 3 step 5):
  - M1, page to page, from /projects to /work/gprs by its sub-menu label, read
    from the new page's own view transition: under Full the label and the H1
    share one moving group (0.5 s), the bar's parts slide (0.35 s) and the rest
    cross-fades (0.25 s); under Reduced, chosen or the OS's, the cross-fade
    only, with nothing moving; under Off, no transition. One change of page per
    case (M1_TRIES): the retries that covered DESIGN-5 came out once it was
    fixed. And with style.css held back 300 ms, the transition still runs, every
    time (DESIGN-5's own check)
  - M2, the draw-in, in the SVG pictures (with WebGL off, SCENE_OFF): under
    Full the threads are clipped to 001 before the first paint, and run to the
    newest once the ledger is in view; under Reduced, Off and the OS's "reduce
    motion" the ledger is whole from the start
  - the 3D hero (copy-review-010, assets/ledger-scene.js): it draws at 1280
    (behind the hero) and 375 (in the figure), aria-hidden, with the SVG
    pictures hidden; the served ledger-data.json is what export-ledger.py
    writes now; under Full the opening runs from load and the picture moves,
    under Reduced, Off and the OS's the slider starts at the newest and the
    picture holds still; a drag on it moves the slider, its line and its
    spoken value. The fallback: with WebGL refused, Three.js blocked or the
    data missing, the SVG pictures are back within 1.5 s. Control: the same
    three with the scene's give-up broken must each fail. And the served
    Three.js files hash to cdnjs's sha512 (THREE_SHA512), with a one-byte control
  - M3, the method loop: on /method, nothing traces before the diagram is in
    view; then under Full its six steps and five arrows pulse once in the
    loop's order (0.5 s each, 0.22 s apart) and the return arrow runs last
    (1.2 s); under Reduced, Off and the OS's "reduce motion", nothing
  - the scrubber: the arrow keys move it, and the column, the clip, the line
    and the slider's spoken value follow; at that earlier handoff a thread
    that closed later is drawn open, and one closed by then is not; its box keeps one height at every
    handoff, so nothing below it moves; with JavaScript off it doesn't show.
    It is written only once its label is ruled, so until then these fail.
  - the journey (TP-A, copy-review-013): under Full at 1280, the home page's runway is there (aria-hidden);
    half-way down it the scene holds the screen (its top at 0), the slider stands part-way, and the card beside
    the gate carries the list's line for the slider's handoff; at its end, and back at the top, the slider is
    at the newest. Under the OS's reduce-motion, under Off, and at 375: no runway
  - the header (copy-review-012): folded on /work/influence-graph, the name is the TC monogram; the name
    itself paints nothing, the T and C each paint their own gradient, and every fallen letter is
    see-through with no width. And Menu has no animation (no wobble, Thomas, 2026-10-03)
  - paint (PAINT): the same states drawn by Playwright's Chromium and by the installed Google Chrome, at
    1280 with reduced motion: the header at rest and folded (light and dark), the pills, the Menu panel,
    a section head and the home hero; and under Full (which it needs) the journey's line card, half-way
    (the card alone: the eased camera can sit a hair apart in the two, and the scene is WebGL, which the home
    hero's state already compares). Each fails when more than PAINT_PIXELS pixels differ by more than
    PAINT_CUT of 255 in a channel, and both pictures are saved for a look. Thomas's Chrome 154 drew the
    folded name with its fallen letters piled on the C (2026-10-03) while Chromium 147 drew it clean, so no
    other check here could see it. Calibrated that day: no pixel over 80 in any state on 5bffd55; 42 to 53
    in each folded state on dea074c, the stacked C (the control). Where Chrome isn't installed (a cloud
    session) these don't run, and the summary says so.

And the structured data, every page as served (copy-review-009 P4-C, scripts/schema.py): the block is what
schema.py writes from the page's own words, every string in it is on the page, and there is no inline
<script> but JSON-LD. And the link preview (scripts/og_cards.py): each card page's og:image is its own card,
served at 1200x630 and made for its current H1, with the ruled alt text; every other page keeps the site card.
And with --live only (copy-review-009 P4-B; the local server applies neither file):
  - headers: every page, one file of each kind (HEADER_FILES) and an unknown URL's 404 are served with
    exactly the headers public/_headers gives that path. Control: a copy of the rules with one value
    changed must be caught on /
  - redirects: every line of public/_redirects answers its code with a Location of its destination, and
    the destination loads (200)
Before any of it, --live refuses to run unless every file of origin/main is, byte for byte, the same in
the copy this script is in (and in --root's copy of public/). The live run compares the site with what
that copy says it should be (the ledger block, _headers, _redirects, the sitemap), so a copy behind main,
or ahead of it, fails or passes for the wrong reason: a handoff trap, put into code 2026-10-03 as Thomas
ruled. It fetches origin first, and compares with line endings set aside (a Windows checkout holds a mix
of CRLF and LF, and git archive writes CRLF). Run it from `git archive origin/main` unpacked into the
scratchpad, or from a clean, up-to-date checkout of main.

Exit code 1 if any check fails. Every FAIL line is printed again at the end, on stderr (checklog.py). Written 2026-09-26 (INFRA-13): the nav is
copied into every page by hand, so this is what catches a page left behind.

A known fault is a check that fails today for a reason logged in the handoff's
open items. It isn't counted and doesn't fail the run: the summary names it,
and -v prints each one as KNOWN. The day it passes, it fails the run until its
mark comes off the check, so a fixed fault can't go on being excused. Now:
none. DESIGN-1 and DESIGN-3 were marked from 2026-09-29 until Phase 3 step 4
fixed them (2026-09-30).
"""
import base64, hashlib, http.server, importlib.util, io, json, os, re, socketserver, subprocess, sys, tarfile, tempfile, threading, time, urllib.error, urllib.parse, urllib.request
from functools import partial
from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import checklog, schema
TOKENS = ["paper", "paper-tint", "ink", "ink-soft", "muted", "rule", "accent", "accent-ink"]
TEXT_ON = [(f, g) for f in ("ink", "ink-soft", "muted", "accent", "accent-ink") for g in ("paper", "paper-tint")] \
    + [("paper", "accent")]       # the solid button
SUBMENU = [
    ("/work/influence-graph", "The Economic Report Influence Graph"),
    ("/work/back-quarter", "A homepage you drive around"),
    ("/work/desk-and-drawer", "A menu that is a photograph of my desk"),
    ("/work/bare-your-rare", "A rare-disease site, written by a patient"),
    ("/work/gprs", "A housing society’s website"),
    ("/work/this-site", "This site"),
]
CHROMIUM = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
# Paint (see the docstring): (name, path, colour scheme, scroll, what to shoot: a selector; MENU, the open
# Menu panel; or #id, that section's head). Drawn by Chromium and by the installed Chrome, and compared.
PAINT = [
    ("the header at rest, dark", "/work/influence-graph", "dark", 0, ".topbar__inner"),
    ("the folded header, dark", "/work/influence-graph", "dark", 1200, ".topbar__inner"),
    ("the folded header, light", "/work/influence-graph", "light", 1200, ".topbar__inner"),
    ("the pills, light", "/", "light", 0, ".topbar__inner"),
    ("the Menu panel, dark", "/work/gprs", "dark", 1200, "MENU"),
    ("a section head, dark", "/work/gprs", "dark", None, "#standard"),
    ("the home hero, dark", "/", "dark", 0, ".hero--home"),
    ("the journey's line card, dark", "/", "dark", 0.5, "JOURNEY"),
]
PAINT_CUT, PAINT_PIXELS = 80, 10
# The journey (TP-A): scroll the home page's runway to J (0 to 1), as ledger-scene.js measures it; and its state.
JOURNEY_AT = """j => { const b = document.querySelector('.lg-runway').getBoundingClientRect(), vh = innerHeight;
  scrollTo(0, b.top + scrollY - vh * 0.5 + j * (b.height - vh * 0.5)); }"""
# Under Playwright's software WebGL a frame can take a second (and holds up the polls), so the eased journey is
# waited for by what it shows: the slider unchanged for 3 s of the page's own time, and for JOURNEY_CARD the card on.
# Measured 2026-10-03: back at the top, the slider is at the newest within about 3 s; the camera eases on for ~30 s.
JOURNEY_STILL = """() => { const v = +document.getElementById('ledger-scrub').value, t = performance.now();
  if (window.__jv !== v) { window.__jv = v; window.__jt = t; return false; } return t - window.__jt >= 3000; }"""
JOURNEY_CARD = """() => { const v = +document.getElementById('ledger-scrub').value, t = performance.now();
  const on = !!document.querySelector('.lg-say[data-on]');
  if (!on || window.__jv !== v) { window.__jv = on ? v : undefined; window.__jt = t; return false; } return t - window.__jt >= 3000; }"""
JOURNEY_STATE = """() => { const c = document.querySelector('.hero--home > .lg-scene'), s = document.querySelector('.lg-say');
  const i = document.getElementById('ledger-scrub'), at = document.querySelectorAll('.ledger__at')[+i.value - 1];
  return {top: c ? Math.round(c.getBoundingClientRect().top) : null, v: +i.value,
          say: s && s.hasAttribute('data-on') ? s.textContent : '', line: at ? at.querySelector('span').textContent : '',
          hidden: document.querySelector('.lg-runway') ? document.querySelector('.lg-runway').getAttribute('aria-hidden') : null}; }"""
# Changes of page per M1 case. It was 3 while DESIGN-5 skipped live transitions; 1 since its fix
# (2026-10-01), so any skip fails again.
M1_TRIES = 1
# Screen widths checked with the browser's text at 200% (DESIGN-3 at 375, DESIGN-4 at 480 and 760)
BIG_TEXT_WIDTHS = (375, 480, 760, 1280)
# The 3D hero (copy-review-010) switched off before any script runs: prefs.js then never marks the page
# for it, and the SVG pictures and ledger.js behave as they did before it. For the SVG checks.
SCENE_OFF = "Object.defineProperty(window, 'WebGL2RenderingContext', {value: undefined, configurable: true});"
# WebGL refused, the way a browser without it answers: the scene loads, fails, and must give up.
NO_GL = """(() => { const g = HTMLCanvasElement.prototype.getContext;
  HTMLCanvasElement.prototype.getContext = function (k, ...a) { return /webgl/.test(k) ? null : g.call(this, k, ...a); }; })();"""
# Three.js 0.186.1, as cdnjs publishes it (copy-review-010 Q-H1 A): the served files must hash to these.
# three.core.js is cdnjs's three.core.min.js, under the name the module imports. See assets/vendor/three/SOURCE.md.
THREE_SHA512 = {
    "/assets/vendor/three/three.module.min.js": "5y1OuWCUVXtYlPOwdMCvNr/Scu/rs2aBbVxO5q1Du9DzLe7X0QpPf1yxAV839cwp7ZqIDv/UrCm0O2oXxM+rMA==",
    "/assets/vendor/three/three.core.js": "XHAcLGgLlaKvTJVfBh76iqQUVHJhHbsu+g/JhY0gQBrpYkg+L1MbYckDdUXkh4D/tsp/mVoPi+Art8oxizfddA==",
}
# One file of each kind, for the live header check (besides every page)
HEADER_FILES = ["/assets/style.css", "/assets/prefs.js", "/assets/img/og-card.png", "/assets/img/graph-gp-budget.webp",
                "/assets/fonts/source-serif-4-latin.woff2", "/favicon.svg", "/assets/gp-budget-graph.json",
                "/robots.txt", "/sitemap.xml"]


class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def translate_path(self, path):
        p = super().translate_path(path.split("?")[0].split("#")[0])
        if not os.path.exists(p) and os.path.exists(p + ".html"):
            return p + ".html"
        return p

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            body = open(os.path.join(self.directory, "404.html"), "rb").read()
            self.send_response(404); self.send_header("Content-Type", "text/html")
            self.end_headers(); self.wfile.write(body)
        else:
            super().send_error(code, message, explain)


def not_main(tree, public=None, ref="origin/main"):
    """For --live: each file of REF (after a fetch) that TREE, or PUBLIC for public/, doesn't hold byte for
    byte, line endings set aside; or why that can't be told. Files REF doesn't have are not compared (an untracked preview, say).
    The clone is TREE itself, or else the one the command was run from (TREE may be an unpacked archive)."""
    def git(cwd, *a):
        return subprocess.run(["git", "-C", cwd, *a], capture_output=True)
    repo = None
    for here in (tree, os.getcwd()):
        top = git(here, "rev-parse", "--show-toplevel")
        if top.returncode == 0:
            url = git(top.stdout.decode().strip(), "remote", "get-url", "origin").stdout.decode().strip()
            if re.search(r"tc-ventures-site(\.git)?/?$", url):
                repo = top.stdout.decode().strip()
                break
    if not repo:
        return ["no clone of tc-ventures-site in the script's folder or the current one, so origin/main can't be read"]
    if git(repo, "fetch", "--quiet", "origin", "main").returncode:
        return ["git fetch origin main failed"]
    tar = git(repo, "archive", "--format=tar", ref)
    if tar.returncode:
        return [f"git archive {ref} failed: {tar.stderr.decode().strip()}"]
    off = []
    with tarfile.open(fileobj=io.BytesIO(tar.stdout)) as t:
        for m in t.getmembers():
            if not m.isfile():
                continue
            want = t.extractfile(m).read().replace(b"\r\n", b"\n")
            copies = [(tree, m.name)]
            if public and m.name.startswith("public/"):
                copies.append((public, m.name[len("public/"):]))
            for base, rel in copies:
                p = os.path.join(base, rel)
                if not os.path.isfile(p):
                    off.append(f"missing: {p}")
                elif open(p, "rb").read().replace(b"\r\n", b"\n") != want:
                    off.append(f"not {ref}'s: {p}")
    return off


def paint_shot(browser, base, path, scheme, scroll, what):
    """One PAINT state as a PNG: 1280 wide, reduced motion (the journey: Full, which it needs), the fonts loaded,
    the home scene drawn."""
    journey = what == "JOURNEY"
    ctx = browser.new_context(viewport={"width": 1280, "height": 900}, color_scheme=scheme,
                              **({} if journey else {"reduced_motion": "reduce"}))
    try:
        page = ctx.new_page(); page.goto(base + path, wait_until="networkidle")
        page.evaluate("document.fonts.ready.then(() => true)")
        if path == "/":
            page.wait_for_function("document.documentElement.dataset.lgScene === 'on'", timeout=8000)
        if journey:
            page.wait_for_function("!!document.querySelector('.lg-runway')", timeout=8000)
            page.evaluate(JOURNEY_AT, scroll)
            page.wait_for_function(JOURNEY_CARD, polling=250, timeout=20000)
            return page.locator(".lg-say").screenshot()
        if scroll is not None:
            page.evaluate(f"window.scrollTo(0, {scroll})")
        page.wait_for_timeout(700)
        if what == "MENU":
            page.locator(".hc-menu").click(); page.wait_for_timeout(500)
            return page.screenshot(clip={"x": 0, "y": 0, "width": 1280, "height": 520})
        if what.startswith("#"):
            head = page.locator(f"{what} .cs-section__num")
            head.scroll_into_view_if_needed(); page.wait_for_timeout(500)
            return head.screenshot()
        return page.locator(what).first.screenshot()
    finally:
        ctx.close()


def paint_apart(a, b):
    """How many pixels of two PNGs differ by more than PAINT_CUT in a channel (all, if the sizes differ)."""
    A, B = Image.open(io.BytesIO(a)).convert("RGB"), Image.open(io.BytesIO(b)).convert("RGB")
    if A.size != B.size:
        return max(A.size[0] * A.size[1], B.size[0] * B.size[1])
    r, g, b2 = ImageChops.difference(A, B).split()
    return sum(ImageChops.lighter(ImageChops.lighter(r, g), b2).histogram()[PAINT_CUT + 1:])


def ledger_expected(draft):
    """What scripts/export-ledger.py would write now, or the reason it can't."""
    spec = importlib.util.spec_from_file_location("export_ledger", os.path.join(HERE, "export-ledger.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    cur = json.loads(mod.CURATION.read_text(encoding="utf-8"))
    try:
        out = mod.render(cur, draft)
        return mod, out[0], "", out[4]
    except SystemExit as e:
        return mod, None, str(e), None


def contrast(a, b):
    """WCAG contrast ratio of two #RRGGBB colours."""
    def lum(h):
        c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        c = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def raw_page(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (site_check.py)"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8").replace("\r\n", "\n")


def status(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (site_check.py)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code


class _NoFollow(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def fetch_headers(url):
    """(status, {header name in lower case: value}) for a GET, redirects not followed."""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (site_check.py)"})
    try:
        with urllib.request.build_opener(_NoFollow).open(req, timeout=20) as r:
            return r.status, {k.lower(): v for k, v in r.headers.items()}
    except urllib.error.HTTPError as e:
        return e.code, {k.lower(): v for k, v in e.headers.items()}


def headers_rules(text):
    """public/_headers as [(path pattern, {name: value})], in file order."""
    rules = []
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line[0].isspace():
            rules.append((line.strip(), {}))
        elif rules and ":" in line:
            name, value = line.strip().split(":", 1)
            rules[-1][1][name.strip().lower()] = value.strip()
    return rules


def headers_wanted(rules, path):
    """Every header the rules give this path; a later rule adds to an earlier one."""
    want = {}
    for pattern, hs in rules:
        if re.fullmatch(re.escape(pattern).replace(r"\*", ".*"), path):
            want.update(hs)
    return want


def headers_wrong(want, got):
    return [f"{k}: want {v!r}, got {got.get(k)!r}" for k, v in want.items() if got.get(k) != v]


def redirect_rules(text):
    """public/_redirects as [(source, destination, code)]."""
    out = []
    for line in text.splitlines():
        parts = line.split("#")[0].split()
        if len(parts) >= 2:
            out.append((parts[0], parts[1], int(parts[2]) if len(parts) > 2 else 302))
    return out


def main():
    args = sys.argv[1:]
    root = args[args.index("--root") + 1] if "--root" in args else os.path.join(HERE, "..", "public")
    if "--live" in args:
        off = not_main(os.path.abspath(os.path.join(HERE, "..")), os.path.abspath(root) if "--root" in args else None)
        if off:
            sys.exit("site_check.py --live: this copy isn't origin/main, so the live run would judge the site against "
                     "the wrong files. Run it from an up-to-date main: git archive origin/main, unpacked into the "
                     "scratchpad.\n  " + "\n  ".join(off[:15]) + (f"\n  and {len(off) - 15} more" if len(off) > 15 else ""))
    sitemap = open(os.path.join(root, "sitemap.xml"), encoding="utf-8").read()
    paths = [re.sub(r"^https://tc-ventures\.ca", "", u) or "/" for u in re.findall(r"<loc>([^<]+)</loc>", sitemap)]
    paths.append("/404")
    srv = None
    if "--live" in args:
        base = "https://tc-ventures.ca"
    else:
        srv = socketserver.TCPServer(("127.0.0.1", 0), partial(CleanURLHandler, directory=os.path.abspath(root)))
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        base = f"http://127.0.0.1:{srv.server_address[1]}"

    results, known, failed, skipped = [], [], checklog.failed(), []
    def check(name, ok, detail="", fault=None):
        if fault and not ok:
            known.append(fault)
            if "-v" in args:
                print(f"KNOWN {name}  [{detail}] ({fault})", flush=True)
            return
        if fault:
            ok, detail = False, f"passes now: take the {fault} mark off this check"
        results.append(ok)
        line = ("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else "")
        if not ok:
            failed.append(line)
        if not ok or "-v" in args:
            print(line, flush=True)

    nc = status(base + "/no-such-page-site-check")
    check("negative control: unknown URL 404", nc == 404, str(nc))

    if "--live" in args:
        # The headers Cloudflare serves are exactly what public/_headers says, on every page and one file of
        # each kind (copy-review-009 P4-B). The local server doesn't apply _headers, so this is live only.
        rules = headers_rules(open(os.path.join(root, "_headers"), encoding="utf-8").read())
        got_root = None
        for p in paths + HEADER_FILES + ["/no-such-page-site-check"]:
            st, got = fetch_headers(base + p)
            if p == "/":
                got_root = got
            want = headers_wanted(rules, p)
            check(f"headers as _headers says: {p}", bool(st in (200, 404) and want and not headers_wrong(want, got)),
                  f"status {st}; " + "; ".join(headers_wrong(want, got)) if headers_wrong(want, got) or st not in (200, 404) else "")
        # Control: one value changed in a copy of the rules must be caught on /
        bent = [(pat, {k: (v + " x" if i == 0 else v) for i, (k, v) in enumerate(hs.items())}) for pat, hs in rules]
        check("control: a changed _headers value is caught", bool(got_root) and
              bool(headers_wrong(headers_wanted(bent, "/"), got_root)))
        # Every public/_redirects rule answers its code and points at its destination, which itself loads
        rpath = os.path.join(root, "_redirects")
        for src, dst, code in redirect_rules(open(rpath, encoding="utf-8").read()) if os.path.exists(rpath) else []:
            st, got = fetch_headers(base + src)
            loc = urllib.parse.urljoin(base + src, got.get("location", ""))
            check(f"redirect: {src} -> {dst} {code}", st == code and loc == base + dst,
                  f"got {st} to {got.get('location')!r}")
            check(f"redirect target loads: {dst}", status(base + dst) == 200)

    # Structured data, every page as served (copy-review-009 P4-C): the block schema.py writes from the page's
    # own words, every string in it on the page, and no inline <script> but JSON-LD
    # And the link preview (copy-review-009 P4-D, scripts/og_cards.py): a card page's og:image is its card, with
    # the ruled alt text, served at 1200x630 and made for this page's H1; every other page keeps the site card
    import og_cards   # here, not at the top: og_cards imports this module
    def card_bytes(url):
        # With the same User-Agent as every other fetch here: Cloudflare answers Python's default one with 403
        # (found 2026-10-02, when every live card looked missing). Any status but 404 is reported as itself.
        req = urllib.request.Request(base + url[len("https://tc-ventures.ca"):],
                                     headers={"User-Agent": "Mozilla/5.0 (site_check.py)", "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            return None if e.code == 404 else e.code
    for p in paths:
        try:
            served_page = raw_page(base + p)
            probs, previews = schema.problems(served_page), og_cards.problems(p, served_page, card_bytes)
        except urllib.error.HTTPError as e:
            probs = previews = [f"status {e.code}"]
        check(f"structured data: {p}", not probs, "; ".join(probs))
        check(f"link preview: {p}", not previews, "; ".join(previews))

    with sync_playwright() as pw:
        if "--chrome" in args:
            browser = pw.chromium.launch(channel="chrome")
        else:
            browser = pw.chromium.launch(executable_path=CHROMIUM if os.path.exists(CHROMIUM) else None)
        print(f"browser: {'Chrome' if '--chrome' in args else 'Chromium'} {browser.version}", flush=True)
        for path in paths:
            ctx = browser.new_context(color_scheme="light", viewport={"width": 1280, "height": 900})
            page = ctx.new_page()
            errors = []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append(str(e)))
            resp = page.goto(base + path, wait_until="networkidle")
            code = resp.status if resp else 0
            check(f"{path}: 200", code == 200, str(code))
            links = page.eval_on_selector_all("#navsub-work a", "els => els.map(e => [e.getAttribute('href'), e.textContent.trim()])")
            check(f"{path}: sub-menu", [tuple(l) for l in links] == SUBMENU, str(links))
            cur = page.eval_on_selector_all("#navsub-work a[aria-current='page']", "els => els.map(e => e.getAttribute('href'))")
            want = [path] if path.startswith("/work/") else []
            check(f"{path}: sub-menu aria-current", cur == want, f"{cur} vs {want}")
            proj = page.locator(".navsub > a[href='/projects']").get_attribute("aria-current")
            want_p = "page" if path == "/projects" else ("true" if path.startswith("/work/") else None)
            check(f"{path}: Projects aria-current", proj == want_p, f"{proj} vs {want_p}")
            robots = page.locator('meta[name="robots"]').count()
            check(f"{path}: noindex only on /404", (robots == 1) == (path == "/404"), str(robots))
            check(f"{path}: no draft banner", page.locator(".draft").count() == 0)
            check(f"{path}: console clean", not errors, "; ".join(errors)[:200])
            display = page.locator(".display__toggle")
            check(f"{path}: Display button shows", display.count() == 1 and display.is_visible())
            sizes = """() => [...document.querySelectorAll('body *')]
                .filter(e => !e.closest('svg, .sr-only') && !['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE'].includes(e.tagName)
                        && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()))
                .map(e => [e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.split(' ')[0] : ''),
                           parseFloat(getComputedStyle(e).fontSize)])"""
            small = page.evaluate(sizes)
            doubled = page.add_style_tag(content=":root { font-size: 32px !important; }")
            big = page.evaluate(sizes)
            stuck = sorted({a[0] for a, b in zip(small, big) if b[1] <= a[1]})
            check(f"{path}: text grows with the browser's text size", bool(small) and len(small) == len(big) and not stuck,
                  f"{len(small)} text elements" + (f"; stay put: {', '.join(stuck)[:160]}" if stuck else ""))
            widths = "[document.documentElement.scrollWidth, document.documentElement.clientWidth]"
            wide = {}
            doubled.evaluate("e => e.remove()")
            page.evaluate("document.documentElement.setAttribute('data-text', 'larger')")
            wide["1280 Larger"] = page.evaluate(widths)
            ctx.close()
            ctx = browser.new_context(viewport={"width": 375, "height": 800})
            page = ctx.new_page(); page.goto(base + path, wait_until="networkidle")
            sw = page.evaluate("[document.documentElement.scrollWidth, document.documentElement.clientWidth]")
            check(f"{path}: no sideways scroll at 375px", sw[0] <= sw[1], f"{sw}")
            # Since the collapsing header (copy-review-012) a phone's nav sits behind Menu: open it first.
            if page.locator(".topbar[data-compact] .hc-menu").count():
                page.locator(".hc-menu").click(); page.wait_for_timeout(300)
            page.locator(".navsub__toggle").click(); page.wait_for_timeout(400)
            opened = page.locator(".navsub__toggle").get_attribute("aria-expanded") == "true"
            check(f"{path}: a click opens the sub-menu at 375px", opened)
            if opened:
                sw = page.evaluate("[document.documentElement.scrollWidth, document.documentElement.clientWidth]")
                check(f"{path}: no sideways scroll at 375px with the sub-menu open", sw[0] <= sw[1], f"{sw}")
                page.keyboard.press("Escape"); page.wait_for_timeout(300)
            page.evaluate("document.documentElement.setAttribute('data-text', 'larger')")
            wide["375 Larger"] = page.evaluate(widths)
            ctx.close()
            over = [f"{k}: {v[0]} wide at {v[1]}" for k, v in wide.items() if v[0] > v[1]]
            check(f"{path}: no sideways scroll with Larger text at 1280 and 375", not over,
                  "; ".join(over) or f"{len(wide)} cases")
            # The browser's own text size at 200%, set as the browser sets it, so em
            # breakpoints see it too (a :root override would not reach a media query).
            big = {}
            for w in BIG_TEXT_WIDTHS:
                ctx = browser.new_context(viewport={"width": w, "height": 800}); page = ctx.new_page()
                cdp = ctx.new_cdp_session(page); cdp.send("Page.enable")
                cdp.send("Page.setFontSizes", {"fontSizes": {"standard": 32, "fixed": 26}})
                page.goto(base + path, wait_until="networkidle")
                big[f"{w}"] = page.evaluate(widths)
                if page.locator(".topbar[data-compact] .hc-menu").count():   # 200% text: the compact bar
                    page.locator(".hc-menu").click(); page.wait_for_timeout(300)
                page.locator(".navsub__toggle").click(); page.wait_for_timeout(400)
                big[f"{w} menu open"] = page.evaluate(widths)
                ctx.close()
            over = [f"{k}: {v[0]} wide at {v[1]}" for k, v in big.items() if v[0] > v[1]]
            check(f"{path}: no sideways scroll with the browser's text at 200%, at "
                  + ", ".join(map(str, BIG_TEXT_WIDTHS)) + "px, sub-menu shut and open", not over,
                  "; ".join(over) or f"{len(big)} cases")

        ctx = browser.new_context(viewport={"width": 1280, "height": 900}); page = ctx.new_page()
        page.goto(base + "/", wait_until="networkidle")
        for _ in range(30):
            page.keyboard.press("Tab")
            if page.evaluate("document.activeElement.classList.contains('navsub__toggle')"):
                break
        check("home: Tab reaches the sub-menu toggle", page.evaluate("document.activeElement.classList.contains('navsub__toggle')"))
        page.keyboard.press("Enter"); page.wait_for_timeout(400)
        check("home: Enter opens it", page.locator(".navsub__toggle").get_attribute("aria-expanded") == "true")
        page.keyboard.press("Escape"); page.wait_for_timeout(400)
        check("home: Esc closes it and returns focus",
              page.locator(".navsub__toggle").get_attribute("aria-expanded") == "false"
              and page.evaluate("document.activeElement.classList.contains('navsub__toggle')"))
        ctx.close()

        mod, want, why, want_data = ledger_expected("--draft-ledger" in args)
        served = mod.current_block(raw_page(base + "/"))
        check("ledger: served block matches export-ledger.py now", want is not None and served == want,
              why or ("no ledger block served" if served is None else "differs: re-run export-ledger.py"))
        for width, shows, hides in ((1280, "land", "port"), (375, "port", "land")):
            ctx = browser.new_context(color_scheme="light", viewport={"width": width, "height": 900})
            ctx.add_init_script(SCENE_OFF)
            page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle")
            vis = [page.locator(f".ledger__pic--{k}").is_visible() if page.locator(f".ledger__pic--{k}").count() == 1 else None
                   for k in (shows, hides)]
            check(f"ledger, no WebGL: {shows} picture shows at {width}px, {hides} does not", vis == [True, False], str(vis))
            ctx.close()

        # The 3D hero (copy-review-010)
        scene_state = """() => { const c = document.querySelector('.lg-scene'), r = document.documentElement;
            const vis = k => { const e = document.querySelector('.ledger__pic--' + k); return !!e && e.getClientRects().length > 0; };
            const i = document.getElementById('ledger-scrub'), at = document.querySelector('.ledger__at.is-on span');
            return {mark: r.getAttribute('data-lg-scene'), canvas: !!c,
                    where: !c ? null : c.parentNode.classList.contains('ledger') ? 'figure' : c.parentNode.classList.contains('hero') ? 'hero' : '?',
                    hidden: c ? c.getAttribute('aria-hidden') : null, land: vis('land'), port: vis('port'),
                    v: i ? +i.value : null, max: i ? +i.max : null, said: i ? i.getAttribute('aria-valuetext') || '' : '',
                    line: at ? at.textContent : null}; }"""
        def colours(png):
            return len(set(Image.open(io.BytesIO(png)).convert("RGB").resize((160, 100)).get_flattened_data()))
        def scene_shot(page):
            """The part of the canvas in view. Under software WebGL a screenshot takes a second or more, so
            the checks below never depend on when within it the picture was taken."""
            b = page.locator(".lg-scene").bounding_box()
            if not b:
                return b""
            y0, y1 = max(b["y"], 0), min(b["y"] + b["height"], 900)
            return page.screenshot(clip={"x": b["x"] + b["width"] * 0.55, "y": y0, "width": b["width"] * 0.45, "height": y1 - y0})
        for width, where in ((1280, "hero"), (375, "figure")):
            ctx = browser.new_context(viewport={"width": width, "height": 900})
            page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle"); page.wait_for_timeout(1500)
            if page.locator(".lg-scene").count():
                page.locator(".lg-scene").scroll_into_view_if_needed(); page.wait_for_timeout(1000)
            s = page.evaluate(scene_state)
            n_col = colours(scene_shot(page)) if s["canvas"] else 0
            check(f"scene: draws at {width}px in the {where}, aria-hidden, the SVG pictures hidden",
                  s["mark"] == "on" and s["where"] == where and s["hidden"] == "true" and not s["land"] and not s["port"]
                  and n_col > 20, f"{s}; {n_col} colours")
            ctx.close()
        try:
            req = urllib.request.Request(base + "/assets/ledger-data.json", headers={"User-Agent": "Mozilla/5.0 (site_check.py)", "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=30) as r:
                served_data = r.read().decode("utf-8").replace("\r\n", "\n")
        except urllib.error.HTTPError:
            served_data = None
        def sha(b):
            return base64.b64encode(hashlib.sha512(b).digest()).decode()
        pins = {}
        for f, want_sha in THREE_SHA512.items():
            req = urllib.request.Request(base + f, headers={"User-Agent": "Mozilla/5.0 (site_check.py)", "Accept": "*/*"})
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    pins[f] = r.read()
            except urllib.error.HTTPError as e:
                pins[f] = None
        wrong = [f for f, b in pins.items() if b is None or sha(b) != THREE_SHA512[f]]
        check("scene: the served Three.js files are cdnjs's, by sha512", not wrong, "; ".join(wrong))
        # Control: one byte changed must not hash the same
        b0 = next(iter(pins.values())) or b"x"
        check("control: Three.js with one byte changed fails its sha512",
              sha(bytes([b0[0] ^ 1]) + b0[1:]) != THREE_SHA512["/assets/vendor/three/three.module.min.js"])
        ok = want_data is not None and served_data == want_data
        check("scene: served ledger-data.json matches export-ledger.py now", ok,
              "" if ok else why or ("not served" if served_data is None else "differs: re-run export-ledger.py"))

        scene_js = open(os.path.join(root, "assets", "ledger-scene.js"), encoding="utf-8").read()
        broken_js = scene_js.replace("root.removeAttribute('data-lg-scene');", "", 1)
        def fallback(case, broken):
            ctx = browser.new_context(viewport={"width": 1280, "height": 900})
            if case == "no WebGL":
                ctx.add_init_script(NO_GL)
            elif case == "Three.js blocked":
                ctx.route("**/assets/vendor/three/three.core.js*", lambda route: route.abort())
            else:
                ctx.route("**/assets/ledger-data.json*", lambda route: route.fulfill(status=404, body="no"))
            if broken:
                ctx.route("**/assets/ledger-scene.js*", lambda route: route.fulfill(
                    status=200, content_type="text/javascript", body=broken_js))
            page = ctx.new_page(); page.goto(base + "/", wait_until="load"); page.wait_for_timeout(1500)
            s = page.evaluate(scene_state); ctx.close()
            return s["mark"] is None and not s["canvas"] and s["land"], s
        cases = ("no WebGL", "Three.js blocked", "data missing")
        got = {c: fallback(c, False) for c in cases}
        check("scene: with WebGL refused, Three.js blocked or the data missing, the SVG pictures are back within 1.5 s",
              all(ok for ok, _ in got.values()), "; ".join(f"{c}: {s}" for c, (ok, s) in got.items() if not ok) or "3 cases")
        got = {c: fallback(c, True) for c in cases}
        check("control: with the scene's give-up broken, each of the three fails",
              broken_js != scene_js and not any(ok for ok, _ in got.values()),
              "give-up line not found in ledger-scene.js" if broken_js == scene_js else
              "; ".join(f"{c} passed anyway" for c, (ok, s) in got.items() if ok) or "3 cases")

        bad = []
        for level, os_reduce in ((None, False), ("full", False), (None, True), ("reduced", False), ("off", False)):
            ctx = browser.new_context(viewport={"width": 1280, "height": 900},
                                      reduced_motion="reduce" if os_reduce else "no-preference")
            if level:
                ctx.add_init_script(f"localStorage.setItem('tcv-display', JSON.stringify({{motion: '{level}'}}))")
            full = (level or ("reduced" if os_reduce else "full")) == "full"
            page = ctx.new_page(); page.goto(base + "/", wait_until="load"); page.wait_for_timeout(300)
            s0 = page.evaluate(scene_state)
            # Full: the first picture mid-opening (the opening takes over 3 s). Otherwise after the 0.9 s fade-in.
            page.wait_for_timeout(0 if full else 1500)
            a = scene_shot(page) if page.locator(".lg-scene").count() else b""
            page.wait_for_timeout(4500)
            s1 = page.evaluate(scene_state)
            b = scene_shot(page) if s1["canvas"] else b""
            ca, cb = (colours(a) if a else 0), (colours(b) if b else 0)
            name = f"{level or 'System'}{', OS reduce' if os_reduce else ''}"
            # Both pictures must have something in them, or "still" would pass on two blank ones.
            if full:
                ok = s0["v"] < s0["max"] and s1["v"] == s1["max"] and s1["mark"] == "on" and cb > 20 and a != b
            else:
                ok = s0["v"] == s0["max"] and s1["v"] == s1["max"] and s1["mark"] == "on" and ca > 20 and a == b
            if not ok:
                bad.append(f"{name}: slider {s0['v']} then {s1['v']} of {s1['max']}, mark {s1['mark']}, "
                           f"picture {'moved' if a != b else 'still'}, colours {ca} and {cb}")
            ctx.close()
        check("scene: the opening runs from load under Full and the picture moves; under Reduced, Off and the OS's it starts "
              "at the newest and holds still", not bad, "; ".join(bad) or "5 cases")

        ctx = browser.new_context(viewport={"width": 1280, "height": 900}, reduced_motion="reduce")
        page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle"); page.wait_for_timeout(1500)
        box = page.locator(".lg-scene").bounding_box() if page.locator(".lg-scene").count() else None
        if box:
            x, y = box["x"] + box["width"] * 0.8, box["y"] + min(box["height"], 900) * 0.5
            page.mouse.move(x, y); page.mouse.down()
            for k in range(1, 11):
                page.mouse.move(x - box["width"] * 0.035 * k, y)
            page.mouse.up(); page.wait_for_timeout(300)
        s = page.evaluate(scene_state)
        listed = page.evaluate("v => document.querySelectorAll('.ledger__list li')[v - 1].querySelector('span').textContent",
                               s["v"]) if s["v"] else None
        check("scene: a drag on it moves the slider back, and the line and spoken value follow",
              bool(box) and s["v"] < s["max"] and s["line"] == listed and s["said"].startswith(f"handoff-{s['v']:03d}, ")
              and s["said"].endswith(listed or "\0"), str(s)[:300])
        ctx.close()
        ctx = browser.new_context(java_script_enabled=False, viewport={"width": 1280, "height": 900})
        page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle")
        if page.locator("details.ledger__list > summary").count() == 1:
            page.locator("details.ledger__list > summary").click()
            opened = page.locator("details.ledger__list[open]").count() == 1
        else:
            opened = False
        check("ledger: list opens with JavaScript off", opened)
        hrefs = page.eval_on_selector_all("details.ledger__list li a", "els => els.map(e => e.getAttribute('href'))")
        nums = [re.fullmatch(re.escape(mod.REPO) + r"handoff-(\d{3})\.md", h or "") for h in hrefs]
        ok = bool(hrefs) and all(nums) and [int(m.group(1)) for m in nums] == list(range(1, len(hrefs) + 1)) \
            and all(os.path.exists(os.path.join(HERE, "..", f"handoff-{m.group(1)}.md")) for m in nums)
        check("ledger: every list line links a handoff file that exists, from 001 without gaps", ok,
              f"{len(hrefs)} links" + ("" if ok else f": {hrefs[:3]}"))
        ctx.close()

        tok = "names => names.map(n => getComputedStyle(document.documentElement).getPropertyValue('--' + n).trim().toUpperCase())"
        pal = {}
        for scheme in ("light", "dark"):
            ctx = browser.new_context(color_scheme=scheme, viewport={"width": 1280, "height": 900})
            page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle")
            pal[scheme] = page.evaluate(tok, TOKENS)
            for choice in ("light", "dark"):
                page.evaluate(f"document.documentElement.setAttribute('data-theme', '{choice}')")
                pal[scheme, choice] = page.evaluate(tok, TOKENS)
            ctx.close()
        check("theme: data-theme=dark gives the OS's dark colours, on a light OS and a dark one",
              pal["light", "dark"] == pal["dark", "dark"] == pal["dark"] != pal["light"],
              f"light OS {pal['light', 'dark']}, dark OS {pal['dark']}")
        check("theme: data-theme=light gives the light colours, on a dark OS and a light one",
              pal["dark", "light"] == pal["light", "light"] == pal["light"],
              f"dark OS {pal['dark', 'light']}, light OS {pal['light']}")
        for scheme in ("light", "dark"):
            t = dict(zip(TOKENS, pal[scheme]))
            ok = all(re.fullmatch(r"#[0-9A-F]{6}", v) for v in t.values())
            ratios = sorted((contrast(t[f], t[g]), f, g) for f, g in TEXT_ON) if ok else []
            low = [f"{f} on {g} {r:.2f}" for r, f, g in ratios if r < 4.5]
            check(f"contrast ({scheme}): every text colour on both grounds, and the solid button, 4.5:1 or more",
                  ok and not low, ("; ".join(low) if low else f"lowest {ratios[0][1]} on {ratios[0][2]} {ratios[0][0]:.2f}")
                  if ok else f"tokens not #RRGGBB: {t}")

        # ---- the Display panel (copy-review-007, Phase 3) ----
        dark_bg = "rgb(12, 15, 20)"                    # --dark-paper, as the browser reports it
        focused = "document.activeElement.classList.contains('display__toggle')"
        ctx = browser.new_context(color_scheme="light", viewport={"width": 1280, "height": 900})
        ctx.add_init_script("""new MutationObserver(() => {
            if (window.__themeAt === undefined && document.documentElement && document.documentElement.hasAttribute('data-theme'))
              window.__themeAt = performance.now();
          }).observe(document, {attributes: true, subtree: true, attributeFilter: ['data-theme']});""")
        page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle")
        for _ in range(40):
            page.keyboard.press("Tab")
            if page.evaluate(focused):
                break
        check("display: Tab reaches the Display button", page.evaluate(focused))
        page.keyboard.press("Enter"); page.wait_for_timeout(300)
        check("display: Enter opens the panel", page.locator(".display__toggle").get_attribute("aria-expanded") == "true"
              and page.locator(".display__panel").is_visible())
        page.keyboard.press("Tab")
        in_motion = page.evaluate("document.activeElement.name") == "display-motion"
        page.keyboard.press("ArrowRight"); page.wait_for_timeout(100)
        saved = page.evaluate("JSON.parse(localStorage.getItem('tcv-display') || '{}')")
        check("display: Tab enters the panel; an arrow key picks Full, marks <html> and saves it",
              in_motion and page.evaluate("document.documentElement.getAttribute('data-motion')") == "full"
              and saved.get("motion") == "full", f"in motion group: {in_motion}, saved {saved}")
        page.keyboard.press("Escape"); page.wait_for_timeout(300)
        check("display: Esc closes it and returns focus",
              page.locator(".display__toggle").get_attribute("aria-expanded") == "false" and page.evaluate(focused))
        page.locator(".display__toggle").click()
        if page.locator("label[for='display-theme-dark']").count():      # no panel: the check below fails, not the script
            page.locator("label[for='display-theme-dark']").click(); page.wait_for_timeout(100)
        bg_now = page.evaluate("getComputedStyle(document.body).backgroundColor")
        page.goto(base + "/method", wait_until="networkidle")
        state = page.evaluate("""() => ({theme: document.documentElement.getAttribute('data-theme'),
            motion: document.documentElement.getAttribute('data-motion'), bg: getComputedStyle(document.body).backgroundColor,
            at: window.__themeAt === undefined ? null : window.__themeAt,
            paint: (performance.getEntriesByName('first-paint')[0] || {}).startTime || null})""")
        check("display: a choice applies at once, carries to the next page, and is on <html> before its first paint",
              bg_now == dark_bg and state["theme"] == "dark" and state["motion"] == "full" and state["bg"] == dark_bg
              and state["at"] is not None and state["paint"] is not None and state["at"] < state["paint"],
              f"at once {bg_now}; next page {state}")
        ctx.close()

        ctx = browser.new_context(color_scheme="light", viewport={"width": 1280, "height": 900})
        page = ctx.new_page(); page.goto(base + "/404", wait_until="networkidle")
        times = """() => [getComputedStyle(document.querySelector('.navsub__toggle svg')).transitionDuration,
                           getComputedStyle(document.querySelector('.btn')).transitionDuration.split(',')[0].trim(),
                           getComputedStyle(document.querySelector('.drift')).animationName]"""
        ruled = {"full": ["0.15s", "0.2s", "drift"], "reduced": ["0s", "0.2s", "none"], "off": ["0s", "0s", "none"]}
        bad = []
        for level in (None, "full", "reduced", "off"):
            for os_reduce in (False, True):
                page.emulate_media(reduced_motion="reduce" if os_reduce else "no-preference")
                page.evaluate("l => l ? document.documentElement.setAttribute('data-motion', l)"
                              " : document.documentElement.removeAttribute('data-motion')", level)
                got, exp = page.evaluate(times), ruled[level or ("reduced" if os_reduce else "full")]
                if got != exp:
                    bad.append(f"{level or 'System'}{', OS reduce' if os_reduce else ''}: {got}, not {exp}")
        check("motion: caret, button fades and the 404's drift at each level, chosen and under System", not bad,
              "; ".join(bad) or "8 cases")
        page.emulate_media(reduced_motion="no-preference")
        page.evaluate("document.documentElement.removeAttribute('data-motion')")
        running_full = page.evaluate("document.getAnimations().length")
        page.evaluate("document.documentElement.setAttribute('data-motion', 'off')")
        page.locator(".navsub__toggle").click(); page.locator(".display__toggle").click()
        running_off = page.evaluate("document.getAnimations().length")
        check("motion Off: nothing is animating, with the menu and the panel open (under Full the drift runs)",
              running_full > 0 and running_off == 0, f"Full {running_full}, Off {running_off}")
        ctx.close()

        more = {}
        for scheme in ("light", "dark"):
            ctx = browser.new_context(color_scheme=scheme, viewport={"width": 1280, "height": 900})
            page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle")
            page.emulate_media(contrast="more")
            more[scheme, "os"] = page.evaluate(tok, TOKENS + ["focus-w"])
            page.evaluate("document.documentElement.setAttribute('data-contrast', 'standard')")
            more[scheme, "standard"] = page.evaluate(tok, TOKENS + ["focus-w"])
            page.emulate_media(contrast="no-preference")
            page.evaluate("document.documentElement.setAttribute('data-contrast', 'more')")
            more[scheme, "choice"] = page.evaluate(tok, TOKENS + ["focus-w"])
            ctx.close()
        for scheme in ("light", "dark"):
            std = pal[scheme] + ["2PX"]
            check(f"contrast More ({scheme}): the choice and the OS setting give the same colours, and Standard undoes it",
                  more[scheme, "choice"] == more[scheme, "os"] != std and more[scheme, "standard"] == std,
                  f"choice {more[scheme, 'choice']}, OS {more[scheme, 'os']}, standard {more[scheme, 'standard']}")
            t = dict(zip(TOKENS, more[scheme, "choice"]))
            if all(re.fullmatch(r"#[0-9A-F]{6}", v) for v in t.values()):
                low = [f"{f} on {g} {contrast(t[f], t[g]):.2f}" for f, g in TEXT_ON if contrast(t[f], t[g]) < 7] \
                    + [f"rule on {g} {contrast(t['rule'], t[g]):.2f}" for g in ("paper", "paper-tint") if contrast(t["rule"], t[g]) < 3]
                check(f"contrast More ({scheme}): text 7:1 or more, rules 3:1 or more", not low, "; ".join(low) or "all pass")
            else:
                check(f"contrast More ({scheme}): text 7:1 or more, rules 3:1 or more", False, f"tokens not #RRGGBB: {t}")

        # ---- the motion (copy-review-007, Phase 3 step 5) ----
        vt_log = """addEventListener('pagereveal', e => {
            const put = v => sessionStorage.setItem('vt', JSON.stringify(v));
            if (!e.viewTransition) { put('none'); return; }
            e.viewTransition.ready.then(() => put(Object.fromEntries(document.getAnimations()
                .filter(a => a.effect && a.effect.pseudoElement)
                .map(a => [a.effect.pseudoElement, a.effect.getComputedTiming().duration]))), () => put('skipped'));
          });"""
        # The ruled times. Made visible 2026-10-03 (copy-review-011, "Motion made visible", "1-4 yes"):
        # the title 500 -> 900 ms, the bar's parts 350 -> 600, the page 250 -> 700 (Reduced: the same
        # cross-fade time, with no move).
        m1_want = {
            "full": {"::view-transition-group(cs-title)": 900, "::view-transition-new(cs-title)": 900,
                     "::view-transition-old(cs-title)": 900, "::view-transition-group(tb-name)": 600,
                     "::view-transition-old(root)": 700, "::view-transition-new(root)": 700},
            "reduced": {"::view-transition-group(cs-title)": None, "::view-transition-group(tb-name)": 0,
                        "::view-transition-old(root)": 700, "::view-transition-new(root)": 700},
        }
        # Each case gets M1_TRIES changes of page (1 since DESIGN-5's fix): it passes on the first
        # transition that runs as ruled, and fails if one runs wrong or none runs at all. Off must show no
        # transition on every try.
        bad, tries_used = [], []
        for level, os_reduce in ((None, False), ("full", True), (None, True), ("reduced", False), ("off", False)):
            eff = level or ("reduced" if os_reduce else "full")
            name = f"{level or 'System'}{', OS reduce' if os_reduce else ''}"
            seen = []
            for _ in range(M1_TRIES):
                ctx = browser.new_context(viewport={"width": 1280, "height": 900},
                                          reduced_motion="reduce" if os_reduce else "no-preference")
                ctx.add_init_script(vt_log)
                if level:
                    ctx.add_init_script(f"localStorage.setItem('tcv-display', JSON.stringify({{motion: '{level}'}}))")
                page = ctx.new_page(); page.goto(base + "/projects", wait_until="networkidle")
                page.locator(".navsub__toggle").click(); page.wait_for_timeout(400)
                page.locator("#navsub-work a[href='/work/gprs']").click()
                page.wait_for_url("**/work/gprs"); page.wait_for_timeout(1000)
                got = page.evaluate("JSON.parse(sessionStorage.getItem('vt') || 'null')")
                ctx.close()
                seen.append(got)
                if eff != "off" and isinstance(got, dict):
                    break                      # a transition ran: judge it, no more tries
            tries_used.append(len(seen))
            if eff == "off":
                ran = [g for g in seen if g not in ("none", "skipped")]
                if ran:
                    bad.append(f"{name}: a transition ran {ran[0]}")
            elif not isinstance(seen[-1], dict):
                bad.append(f"{name}: no transition in {len(seen)} tries ({seen})")
            else:
                miss = [f"{k} {seen[-1].get(k)} not {v}" for k, v in m1_want[eff].items() if seen[-1].get(k) != v]
                if miss:
                    bad.append(f"{name}: " + ", ".join(miss))
        check("motion M1: /projects to /work/gprs by its label, at each level, chosen and under System", not bad,
              "; ".join(bad) or f"5 cases, tries used {tries_used}")

        # DESIGN-5: Chrome settles the new page's opt-in before a late style.css arrives, so the opt-in
        # must not live in style.css. Hold style.css back 300 ms on every change of page: the
        # transition must still run, every time (no retries).
        late = []
        for _ in range(3):
            ctx = browser.new_context(viewport={"width": 1280, "height": 900})
            ctx.add_init_script(vt_log)
            def slow(route):
                time.sleep(0.3); route.continue_()
            page = ctx.new_page(); page.goto(base + "/projects", wait_until="networkidle")
            ctx.route("**/assets/style.css*", slow)
            page.locator(".navsub__toggle").click(); page.wait_for_timeout(400)
            page.locator("#navsub-work a[href='/work/gprs']").click()
            page.wait_for_url("**/work/gprs"); page.wait_for_timeout(1500)
            got = page.evaluate("JSON.parse(sessionStorage.getItem('vt') || 'null')")
            late.append("ran" if isinstance(got, dict) and got.get("::view-transition-group(cs-title)") == m1_want["full"]["::view-transition-group(cs-title)"] else str(got))
            ctx.close()
        check("motion M1: still runs when style.css arrives 300 ms late (DESIGN-5), every time",
              late == ["ran"] * 3, str(late))

        scrub = """() => { const i = document.getElementById('ledger-scrub'); if (!i) return null;
            const r = document.querySelector('#lg-clip-0 rect');
            const g = document.querySelector('.ledger__pic--land .lg__threads');
            return {v: +i.value, max: +i.max, w: r ? +r.getAttribute('width') : null,
                    at: window.__clipAt === undefined ? null : window.__clipAt,
                    on: window.__waitOn === undefined ? null : window.__waitOn,
                    off: window.__waitOff === undefined ? null : window.__waitOff,
                    seen: g ? getComputedStyle(g).visibility : null,
                    paint: (performance.getEntriesByName('first-paint')[0] || {}).startTime || null}; }"""
        clip_at = """new MutationObserver(() => {
            const g = document.querySelector('.lg__threads'), r = document.documentElement, t = performance.now();
            if (window.__clipAt === undefined && g && g.hasAttribute('clip-path')) window.__clipAt = t;
            if (window.__waitOn === undefined && r.hasAttribute('data-lg-wait')) window.__waitOn = t;
            if (window.__waitOn !== undefined && window.__waitOff === undefined && !r.hasAttribute('data-lg-wait')) window.__waitOff = t;
          }).observe(document, {attributes: true, childList: true, subtree: true});"""

        def never_shown_whole(s):
            """Under Full the threads never paint unclipped before the draw-in (DESIGN-6): either the clip
            came before the first paint, or the wait mark was on before it and lifted no sooner than the clip."""
            if s["paint"] is None or s["at"] is None:
                return False
            return s["at"] < s["paint"] or (s["on"] is not None and s["on"] < s["paint"]
                                              and s["off"] is not None and s["at"] <= s["off"])
        bad = []
        for level, os_reduce in ((None, False), ("full", False), (None, True), ("reduced", False), ("off", False)):
            ctx = browser.new_context(viewport={"width": 1280, "height": 900},
                                      reduced_motion="reduce" if os_reduce else "no-preference")
            ctx.add_init_script(clip_at)
            ctx.add_init_script(SCENE_OFF)
            if level:
                ctx.add_init_script(f"localStorage.setItem('tcv-display', JSON.stringify({{motion: '{level}'}}))")
            page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle")
            s0 = page.evaluate(scrub)
            name = f"{level or 'System'}{', OS reduce' if os_reduce else ''}"
            if s0 is None:
                bad.append(f"{name}: no scrubber"); ctx.close(); continue
            page.locator(".ledger").scroll_into_view_if_needed()
            page.wait_for_timeout(4500)
            s1 = page.evaluate(scrub)
            if (level or ("reduced" if os_reduce else "full")) == "full":
                ok = s0["v"] == 1 and s0["w"] < 150 and never_shown_whole(s0) and s1["v"] == s1["max"] and s1["w"] == 944
            else:
                ok = s0["v"] == s0["max"] and s0["w"] == 944 and s1["v"] == s1["max"] and s0["on"] is None
            if not ok:
                bad.append(f"{name}: at load {s0}, in view {s1}")
            ctx.close()
        check("motion M2, no WebGL: the draw-in under Full (never shown whole first), whole under Reduced, Off and the OS's",
              not bad, "; ".join(bad) or "5 cases")

        # DESIGN-6: with ledger.js 1 s late the threads must still never paint whole before the draw-in, and
        # the draw-in still runs; with ledger.js blocked, prefs.js's 3 s fallback shows the ledger whole.
        bad = []
        for hold in ("late", "late", "blocked"):
            ctx = browser.new_context(viewport={"width": 1280, "height": 900})
            ctx.add_init_script(clip_at)
            ctx.add_init_script(SCENE_OFF)
            ctx.add_init_script("localStorage.setItem('tcv-display', JSON.stringify({motion: 'full'}))")
            if hold == "blocked":
                ctx.route("**/assets/ledger.js*", lambda route: route.abort())
            else:
                def late_js(route):
                    time.sleep(1.0); route.continue_()
                ctx.route("**/assets/ledger.js*", late_js)
            page = ctx.new_page(); page.goto(base + "/", wait_until="load")
            s0 = page.evaluate(scrub)
            if hold == "blocked":
                page.wait_for_timeout(3500)
                s1 = page.evaluate(scrub)
                ok = s1 is not None and s1["on"] is not None and s1["off"] is not None and s1["seen"] == "visible" and s1["at"] is None
            else:
                page.locator(".ledger").scroll_into_view_if_needed(); page.wait_for_timeout(4500)
                s1 = page.evaluate(scrub)
                ok = s0 is not None and never_shown_whole(s0) and s1["v"] == s1["max"]
            if not ok:
                bad.append(f"{hold}: at load {s0}, after {s1}")
            ctx.close()
        check("motion M2, no WebGL: ledger.js 1 s late, never shown whole first; blocked, shown whole after 3 s (DESIGN-6)",
              not bad, "; ".join(bad) or "3 cases")

        loop_anims = """() => document.getAnimations().filter(a => a.animationName && a.animationName.startsWith('loop-')).map(a => {
            const t = a.effect.target, c = a.effect.getComputedTiming();
            const key = t.closest('a') ? 'n' + [...t.closest('svg').querySelectorAll(':scope > a')].indexOf(t.closest('a'))
                      : t.classList.contains('loop__edge--back') ? 'back'
                      : 'e' + [...t.closest('svg').querySelectorAll(':scope > line.loop__edge')].indexOf(t);
            return [key, Math.round(c.delay), Math.round(c.duration)]; })"""
        order = ["n0", "e0", "n1", "e1", "n2", "e2", "n3", "e3", "n4", "e4", "n5", "back"]
        bad = []
        for level, os_reduce in ((None, False), ("full", False), (None, True), ("reduced", False), ("off", False)):
            ctx = browser.new_context(viewport={"width": 1280, "height": 900},
                                      reduced_motion="reduce" if os_reduce else "no-preference")
            if level:
                ctx.add_init_script(f"localStorage.setItem('tcv-display', JSON.stringify({{motion: '{level}'}}))")
            page = ctx.new_page(); page.goto(base + "/method", wait_until="networkidle")
            name = f"{level or 'System'}{', OS reduce' if os_reduce else ''}"
            early = page.evaluate(loop_anims)
            page.locator(".loop--files").scroll_into_view_if_needed(); page.wait_for_timeout(300)
            got = page.evaluate(loop_anims)
            ctx.close()
            if (level or ("reduced" if os_reduce else "full")) == "full":
                seq = [k for k, d, t in sorted(got, key=lambda r: r[1])]
                want_t = {k: (1200 if k == "back" else 500) for k in order}
                delays = [d for k, d, t in sorted(got, key=lambda r: r[1])]
                ok = not early and seq == order and all(t == want_t[k] for k, d, t in got) \
                    and delays == [round(i * 220) for i in range(12)]
                if not ok:
                    bad.append(f"{name}: before view {len(early)}, in view {sorted(got, key=lambda r: r[1])}")
            elif got or early:
                bad.append(f"{name}: {len(early) + len(got)} loop animations")
        check("motion M3: the method loop traces once in its order under Full, nothing under Reduced, Off and the OS's",
              not bad, "; ".join(bad) or "5 cases")

        ctx = browser.new_context(viewport={"width": 1280, "height": 900}, reduced_motion="reduce")
        page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle")
        if page.locator("#ledger-scrub").count():
            n = page.evaluate("+document.getElementById('ledger-scrub').max")
            heights = set()
            for v in range(1, n + 1):
                heights.add(page.evaluate("v => { const i = document.getElementById('ledger-scrub'); i.value = v;"
                                          " i.dispatchEvent(new Event('input'));"
                                          " return document.querySelector('.ledger__scrub').getBoundingClientRect().height; }", v))
            page.evaluate(f"(() => {{ const i = document.getElementById('ledger-scrub'); i.value = {n};"
                          " i.dispatchEvent(new Event('input')); })()")
            page.locator("#ledger-scrub").focus()
            for _ in range(9):
                page.keyboard.press("ArrowLeft")
            st = page.evaluate("""() => { const i = document.getElementById('ledger-scrub'), v = +i.value;
                const cols = [...document.querySelectorAll('.ledger__pic--land .lg__col')];
                return {v, on: cols.findIndex(c => c.classList.contains('lg__col--on')) + 1,
                        colx: +cols[v - 1].getAttribute('x1'), w: +document.querySelector('#lg-clip-0 rect').getAttribute('width'),
                        shown: [...document.querySelectorAll('.ledger__at')].filter(p => getComputedStyle(p).visibility === 'visible')
                               .map(p => p.querySelector('span').textContent),
                        line: document.querySelectorAll('.ledger__list li')[v - 1].querySelector('span').textContent,
                        said: i.getAttribute('aria-valuetext') || '',
                        then: (() => { const els = [...document.querySelectorAll('.ledger__pic--land line[data-e]')];
                          const teal = getComputedStyle(document.querySelector('.ledger__pic--land .lg__t--open')).stroke;
                          const later = els.filter(e => +e.dataset.e > v - 1), done = els.filter(e => +e.dataset.e <= v - 1);
                          return [later.length, later.filter(e => getComputedStyle(e).stroke !== teal).length,
                                  done.length, done.filter(e => getComputedStyle(e).stroke === teal).length]; })()}; }""")
            then = st.pop("then")
            check("scrubber: at an earlier handoff, threads that closed later are drawn open, those closed by then are not",
                  then[0] > 0 and then[2] > 0 and then[1] == 0 and then[3] == 0,
                  f"closed later: {then[0]}, not teal {then[1]}; closed by then: {then[2]}, teal {then[3]}")
            ok = st["v"] == n - 9 and st["on"] == st["v"] and abs(st["w"] - st["colx"] - 4) < 0.01 \
                and st["shown"] == [st["line"]] and st["said"].startswith(f"handoff-{st['v']:03d}, ") and st["said"].endswith(st["line"])
            check("scrubber: arrow keys move it; column, clip, line and spoken value follow", ok, str(st)[:300])
            check("scrubber: one height at every handoff, so nothing below it moves", len(heights) == 1,
                  f"{len(heights)} heights over {n} handoffs: {sorted(heights)[:4]}")
        else:
            check("scrubber: arrow keys move it; column, clip, line and spoken value follow", False,
                  "no scrubber: is its label ruled (curation copy.scrub)?")
            check("scrubber: one height at every handoff, so nothing below it moves", False, "no scrubber")
            check("scrubber: at an earlier handoff, threads that closed later are drawn open, those closed by then are not",
                  False, "no scrubber")
        ctx.close()

        # The journey (TP-A, copy-review-013; the docstring says what it holds)
        ctx = browser.new_context(viewport={"width": 1280, "height": 900})
        page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle")
        try:
            page.wait_for_function("document.documentElement.dataset.lgScene === 'on' && !!document.querySelector('.lg-runway')",
                                   timeout=15000)
            def settle(still):
                page.evaluate("window.__jv = undefined")    # a fresh count for each wait
                try:
                    page.wait_for_function(still, polling=250, timeout=20000)
                except Exception:
                    pass                                        # the state read next says what it got to
                return page.evaluate(JOURNEY_STATE)
            page.evaluate(JOURNEY_AT, 0.5); mid = settle(JOURNEY_CARD)
            page.evaluate(JOURNEY_AT, 1.0); end = settle(JOURNEY_STILL)
            page.evaluate("scrollTo(0, 0)"); back = settle(JOURNEY_STILL)
            n = page.evaluate("+document.getElementById('ledger-scrub').max")
            ok = bool(mid["top"] == 0 and 1 < mid["v"] < n and mid["line"] and mid["say"].endswith(mid["line"])
                      and mid["hidden"] == "true" and end["v"] == n and back["v"] == n)
            detail = f"half-way {mid}; at the end v {end['v']}; back at the top v {back['v']}; newest {n}"
        except Exception as e:
            ok, detail = False, f"{type(e).__name__}: {str(e).strip().splitlines()[0][:120]}"
        check("journey: under Full at 1280 the scene holds while the runway scrolls; the slider follows, each gate's line beside it",
              ok, detail)
        ctx.close()
        has = []
        for name, kw, level in [("the OS's reduce-motion", {"viewport": {"width": 1280, "height": 900}, "reduced_motion": "reduce"}, None),
                                ("Off", {"viewport": {"width": 1280, "height": 900}}, "off"),
                                ("375 wide", {"viewport": {"width": 375, "height": 800}}, None)]:
            ctx = browser.new_context(**kw)
            if level:
                ctx.add_init_script(f"localStorage.setItem('tcv-display', JSON.stringify({{motion: '{level}'}}))")
            page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle"); page.wait_for_timeout(2500)
            if page.evaluate("!!document.querySelector('.lg-runway') || document.documentElement.hasAttribute('data-lg-journey')"):
                has.append(name)
            ctx.close()
        check("journey: no runway under the OS's reduce-motion, under Off, or at 375", not has, "a runway under " + ", ".join(has))

        # The header's monogram (copy-review-012). The name's gradient is painted through its text; painted
        # through the whole name, it showed through the fallen letters too: Chrome 154 drew them piled on the C
        # (Thomas saw it, 2026-10-03), while this Chromium leaves a part-faded letter out, so no picture taken
        # here can show it. So: folded, the name paints nothing, the T and C each paint their own gradient, and
        # every fallen letter is see-through with no width. And Menu doesn't wobble (Thomas, 2026-10-03).
        ctx = browser.new_context(viewport={"width": 1280, "height": 900})
        page = ctx.new_page(); page.goto(base + "/work/influence-graph", wait_until="networkidle")
        page.evaluate("window.scrollTo(0, 1200)"); page.wait_for_timeout(1500)
        st = page.evaluate("""() => { const w = document.querySelector('.wordmark'), cs = e => getComputedStyle(e);
            const L = [...w.querySelectorAll('.hc-l')], keep = L.filter(s => s.classList.contains('hc-l--keep'));
            return {mono: w.hasAttribute('data-mono'), name: cs(w).backgroundImage,
                    keep: keep.map(s => cs(s).backgroundImage.startsWith('radial-gradient')),
                    fallen: L.filter(s => !keep.includes(s) && (cs(s).opacity !== '0' || s.getBoundingClientRect().width > 0)).length,
                    wobble: cs(document.querySelector('.hc-menu')).animationName}; }""")
        check("header: folded, the name is TC, each letter painting its own gradient, the fallen ones gone",
              st["mono"] and st["name"] == "none" and st["keep"] == [True, True] and st["fallen"] == 0, str(st))
        check("header: Menu doesn't wobble", st["wobble"] == "none", st["wobble"])
        ctx.close()

        # Paint: Chromium against the installed Chrome (PAINT; the docstring says why)
        pair = [pw.chromium.launch(executable_path=CHROMIUM if os.path.exists(CHROMIUM) else None)]
        try:
            pair.append(pw.chromium.launch(channel="chrome"))
        except Exception as e:
            skipped.append(f"{len(PAINT)} paint checks (no Google Chrome here: {str(e).strip().splitlines()[0][:80]})")
        if len(pair) == 2:
            keep = os.path.join(tempfile.gettempdir(), "site-check-paint")
            for name, path, scheme, scroll, what in PAINT:
                try:
                    a, b = (paint_shot(br, base, path, scheme, scroll, what) for br in pair)
                    n = paint_apart(a, b)
                    detail = f"{n} pixels over {PAINT_CUT} (Chromium {pair[0].version}, Chrome {pair[1].version})"
                    if n > PAINT_PIXELS:
                        os.makedirs(keep, exist_ok=True)
                        stem = os.path.join(keep, re.sub(r"\W+", "-", name).strip("-"))
                        open(stem + "-chromium.png", "wb").write(a); open(stem + "-chrome.png", "wb").write(b)
                        detail += f"; both pictures in {keep}: look at them"
                except Exception as e:
                    n, detail = None, f"{type(e).__name__}: {str(e).strip().splitlines()[0][:120]}"
                check(f"paint: {name}, drawn alike by Chromium and Chrome", n is not None and n <= PAINT_PIXELS, detail)
        for br in pair:
            br.close()

        ctx = browser.new_context(java_script_enabled=False, color_scheme="dark", viewport={"width": 1280, "height": 900})
        page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle")
        sc = page.locator(".ledger__scrub")
        check("scrubber: with JavaScript off, it's in the page but doesn't show", sc.count() == 1 and not sc.is_visible(),
              f"count {sc.count()}")
        shown = page.locator(".display__toggle").is_visible()
        bg = page.evaluate("getComputedStyle(document.body).backgroundColor")
        check("display: with JavaScript off, no Display button, and the OS's dark mode still applies",
              not shown and bg == dark_bg, f"button shown {shown}, background {bg}")
        ctx.close()
        browser.close()
    if srv:
        srv.shutdown()
    faults = ", ".join(f"{known.count(f)} {f}" for f in sorted(set(known)))
    print(f"{sum(results)} of {len(results)} checks passed" + (f"; known faults, not counted: {faults}" if known else "")
          + (f"; not run here: {'; '.join(skipped)}" if skipped else ""))
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
