"""site_check.py — check every page of tc-ventures.ca in a real browser.

Usage: python scripts/site_check.py            (serves ./public locally)
       python scripts/site_check.py --live     (checks https://tc-ventures.ca)
       python scripts/site_check.py --root DIR (serves another copy of public/,
                                                e.g. an older commit, as a
                                                negative control)

Pages come from public/sitemap.xml, plus /404. For each page:
  - status 200, and a made-up URL gives 404 (negative control)
  - the Projects sub-menu lists exactly SUBMENU, in order, with its labels
  - aria-current: "page" on the sub-menu link of the page you're on (case
    studies only); on Projects, "page" for /projects and "true" for every
    /work/ page
  - no noindex (except /404, which carries it on purpose) and no draft banner
  - no console errors, and no sideways scroll at 375px
And once, on the home page: Tab reaches the sub-menu toggle, Enter opens it,
Esc closes it and returns focus.

Exit code 1 if any check fails. Written 2026-09-26 (INFRA-13): the nav is
copied into every page by hand, so this is what catches a page left behind.
"""
import http.server, os, re, socketserver, sys, threading, urllib.request
from functools import partial
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
SUBMENU = [
    ("/work/influence-graph", "The Economic Report Influence Graph"),
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

    results = []
    def check(name, ok, detail=""):
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
            ctx.close()
            ctx = browser.new_context(viewport={"width": 375, "height": 800})
            page = ctx.new_page(); page.goto(base + path, wait_until="networkidle")
            sw = page.evaluate("[document.documentElement.scrollWidth, document.documentElement.clientWidth]")
            check(f"{path}: no sideways scroll at 375px", sw[0] <= sw[1], f"{sw}")
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
        ctx.close(); browser.close()
    if srv:
        srv.shutdown()
    print(f"{sum(results)} of {len(results)} checks passed")
    sys.exit(0 if all(results) else 1)


if __name__ == "__main__":
    main()
