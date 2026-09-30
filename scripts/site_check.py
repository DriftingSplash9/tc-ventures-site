"""site_check.py — check every page of tc-ventures.ca in a real browser.

Usage: python scripts/site_check.py            (serves ./public locally)
       python scripts/site_check.py --live     (checks https://tc-ventures.ca)
       python scripts/site_check.py --root DIR (serves another copy of public/,
                                                e.g. an older commit, as a
                                                negative control)
       add --draft-ledger for a preview whose ledger carries unruled lines

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
    only, with nothing moving; under Off, no transition. Live, Chrome aborts
    about half of these transitions (cause not yet found), so each case gets
    up to M1_TRIES changes of page; Off must show none on every one
  - M2, the draw-in: under Full the threads are clipped to 001 before the first
    paint, and run to the newest once the ledger is in view; under Reduced,
    Off and the OS's "reduce motion" the ledger is whole from the start
  - the scrubber: the arrow keys move it, and the column, the clip, the line
    and the slider's spoken value follow; at that earlier handoff a thread
    that closed later is drawn open, and one closed by then is not; its box keeps one height at every
    handoff, so nothing below it moves; with JavaScript off it doesn't show.
    It is written only once its label is ruled, so until then these fail.

Exit code 1 if any check fails. Written 2026-09-26 (INFRA-13): the nav is
copied into every page by hand, so this is what catches a page left behind.

A known fault is a check that fails today for a reason logged in the handoff's
open items. It isn't counted and doesn't fail the run: the summary names it,
and -v prints each one as KNOWN. The day it passes, it fails the run until its
mark comes off the check, so a fixed fault can't go on being excused. Now:
none. DESIGN-1 and DESIGN-3 were marked from 2026-09-29 until Phase 3 step 4
fixed them (2026-09-30).
"""
import http.server, importlib.util, json, os, re, socketserver, sys, threading, urllib.request
from functools import partial
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
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
# Changes of page per M1 case, since Chrome aborts some live transitions (handoff-027)
M1_TRIES = 3
# Screen widths checked with the browser's text at 200% (DESIGN-3 at 375, DESIGN-4 at 480 and 760)
BIG_TEXT_WIDTHS = (375, 480, 760, 1280)


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


def ledger_expected(draft):
    """What scripts/export-ledger.py would write now, or the reason it can't."""
    spec = importlib.util.spec_from_file_location("export_ledger", os.path.join(HERE, "export-ledger.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    cur = json.loads(mod.CURATION.read_text(encoding="utf-8"))
    try:
        return mod, mod.render(cur, draft)[0], ""
    except SystemExit as e:
        return mod, None, str(e)


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


def main():
    args = sys.argv[1:]
    root = args[args.index("--root") + 1] if "--root" in args else os.path.join(HERE, "..", "public")
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

    results, known = [], []
    def check(name, ok, detail="", fault=None):
        if fault and not ok:
            known.append(fault)
            if "-v" in args:
                print(f"KNOWN {name}  [{detail}] ({fault})", flush=True)
            return
        if fault:
            ok, detail = False, f"passes now: take the {fault} mark off this check"
        results.append(ok)
        if not ok or "-v" in args:
            print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""), flush=True)

    nc = status(base + "/no-such-page-site-check")
    check("negative control: unknown URL 404", nc == 404, str(nc))

    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=CHROMIUM if os.path.exists(CHROMIUM) else None)
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

        mod, want, why = ledger_expected("--draft-ledger" in args)
        served = mod.current_block(raw_page(base + "/"))
        check("ledger: served block matches export-ledger.py now", want is not None and served == want,
              why or ("no ledger block served" if served is None else "differs: re-run export-ledger.py"))
        for width, shows, hides in ((1280, "land", "port"), (375, "port", "land")):
            ctx = browser.new_context(color_scheme="light", viewport={"width": width, "height": 900})
            page = ctx.new_page(); page.goto(base + "/", wait_until="networkidle")
            vis = [page.locator(f".ledger__pic--{k}").is_visible() if page.locator(f".ledger__pic--{k}").count() == 1 else None
                   for k in (shows, hides)]
            check(f"ledger: {shows} picture shows at {width}px, {hides} does not", vis == [True, False], str(vis))
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
        m1_want = {
            "full": {"::view-transition-group(cs-title)": 500, "::view-transition-new(cs-title)": 500,
                     "::view-transition-old(cs-title)": 500, "::view-transition-group(tb-name)": 350,
                     "::view-transition-old(root)": 250, "::view-transition-new(root)": 250},
            "reduced": {"::view-transition-group(cs-title)": None, "::view-transition-group(tb-name)": 0,
                        "::view-transition-old(root)": 250, "::view-transition-new(root)": 250},
        }
        # Live, Chrome aborts about half of these transitions for a reason not yet found (handoff-027;
        # locally it never does). So each case gets up to M1_TRIES changes of page: it passes on the first
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

        scrub = """() => { const i = document.getElementById('ledger-scrub'); if (!i) return null;
            const r = document.querySelector('#lg-clip-0 rect');
            return {v: +i.value, max: +i.max, w: r ? +r.getAttribute('width') : null,
                    at: window.__clipAt === undefined ? null : window.__clipAt,
                    paint: (performance.getEntriesByName('first-paint')[0] || {}).startTime || null}; }"""
        clip_at = """new MutationObserver(() => {
            const g = document.querySelector('.lg__threads');
            if (window.__clipAt === undefined && g && g.hasAttribute('clip-path')) window.__clipAt = performance.now();
          }).observe(document, {attributes: true, childList: true, subtree: true});"""
        bad = []
        for level, os_reduce in ((None, False), ("full", False), (None, True), ("reduced", False), ("off", False)):
            ctx = browser.new_context(viewport={"width": 1280, "height": 900},
                                      reduced_motion="reduce" if os_reduce else "no-preference")
            ctx.add_init_script(clip_at)
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
                ok = s0["v"] == 1 and s0["w"] < 150 and s0["at"] is not None and s0["paint"] is not None \
                    and s0["at"] < s0["paint"] and s1["v"] == s1["max"] and s1["w"] == 944
            else:
                ok = s0["v"] == s0["max"] and s0["w"] == 944 and s1["v"] == s1["max"]
            if not ok:
                bad.append(f"{name}: at load {s0}, in view {s1}")
            ctx.close()
        check("motion M2: the draw-in under Full (clipped before first paint), whole under Reduced, Off and the OS's",
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
                        line: document.querySelectorAll('.ledger__list li span')[v - 1].textContent,
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
    print(f"{sum(results)} of {len(results)} checks passed" + (f"; known faults, not counted: {faults}" if known else ""))
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
