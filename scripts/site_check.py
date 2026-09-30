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
  - at 375px, a click on the sub-menu toggle opens it, and with it open the
    page still doesn't scroll sideways (DESIGN-1, a known fault: see below)
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

Exit code 1 if any check fails. Written 2026-09-26 (INFRA-13): the nav is
copied into every page by hand, so this is what catches a page left behind.

A known fault is a check that fails today for a reason logged in the handoff's
open items. It isn't counted and doesn't fail the run: the summary names it,
and -v prints each one as KNOWN. The day it passes, it fails the run until its
mark comes off the check, so a fixed fault can't go on being excused. Now:
DESIGN-1, the open sub-menu at 375px (added 2026-09-29).
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
            sizes = """() => [...document.querySelectorAll('body *')]
                .filter(e => !e.closest('svg, .sr-only') && !['SCRIPT', 'STYLE', 'NOSCRIPT', 'TEMPLATE'].includes(e.tagName)
                        && [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()))
                .map(e => [e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.split(' ')[0] : ''),
                           parseFloat(getComputedStyle(e).fontSize)])"""
            small = page.evaluate(sizes)
            page.add_style_tag(content=":root { font-size: 32px !important; }")
            big = page.evaluate(sizes)
            stuck = sorted({a[0] for a, b in zip(small, big) if b[1] <= a[1]})
            check(f"{path}: text grows with the browser's text size", bool(small) and len(small) == len(big) and not stuck,
                  f"{len(small)} text elements" + (f"; stay put: {', '.join(stuck)[:160]}" if stuck else ""))
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
                check(f"{path}: no sideways scroll at 375px with the sub-menu open", sw[0] <= sw[1], f"{sw}",
                      fault="DESIGN-1")
            ctx.close()

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
        browser.close()
    if srv:
        srv.shutdown()
    faults = ", ".join(f"{known.count(f)} {f}" for f in sorted(set(known)))
    print(f"{sum(results)} of {len(results)} checks passed" + (f"; known faults, not counted: {faults}" if known else ""))
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
