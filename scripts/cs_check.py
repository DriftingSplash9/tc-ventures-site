"""cs_check.py — check one case-study page in a real browser, served locally.

Usage: python scripts/cs_check.py work/bare-your-rare [--preview] [--shots DIR]

Serves ./public on a local port from inside this process (a separate
http.server can outlive its shell), with the site's clean URLs (/x -> x.html),
then drives headless Chromium through Playwright. Checks:

  1. the page answers 200, and a made-up URL answers 404 (negative control)
  2. title and H1 match; noindex and the draft banner are present with
     --preview and absent without it
  3. the six case-study sections, in the fixed order
  4. the Projects sub-menu: its order, aria-current on this page and on
     Projects; by keyboard, Tab reaches the toggle, Enter opens it, Esc closes
     it and returns focus
  5. no console errors, in light and in dark
  6. no sideways scroll at 375px
  7. with JavaScript off, the words and links are all there
  8. every link: local ones against the local server, others fetched live.
     LinkedIn answers 999 to scripts (expected). A GitHub blob link to a file
     that is only on an unmerged branch answers 404 until it merges.

--shots DIR writes one screenshot per section, light and dark at 1280px (each
after scrollIntoView and a pause, since full-page shots of a tall page tile
and lazy images render black), and the header at 375px. Look at them: a
script cannot judge how a page looks.

Exit code 1 if any check fails. Written 2026-09-26 (INFRA-13).
"""
import http.server, json, os, re, socketserver, sys, threading, time, urllib.request
from functools import partial
from playwright.sync_api import sync_playwright

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public")
SECTIONS = ["ask", "standard", "wrong", "caught", "shipped", "receipts"]
SUBMENU = ["/work/influence-graph", "/work/bare-your-rare", "/work/gprs", "/work/this-site"]
CHROMIUM = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"


class CleanURLHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def translate_path(self, path):
        p = super().translate_path(path.split("?")[0].split("#")[0])
        if not os.path.exists(p) and os.path.exists(p + ".html"):
            return p + ".html"
        return p


def serve():
    handler = partial(CleanURLHandler, directory=os.path.abspath(ROOT))
    srv = socketserver.TCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f"http://127.0.0.1:{srv.server_address[1]}"


def status(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (cs_check.py; link check)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return f"ERR {type(e).__name__}"


def main():
    args = sys.argv[1:]
    page_path = "/" + args[0].strip("/")
    preview = "--preview" in args
    shots = args[args.index("--shots") + 1] if "--shots" in args else None
    results = []

    def check(name, ok, detail=""):
        results.append((ok, name, detail))
        print(("PASS " if ok else "FAIL ") + name + (f"  [{detail}]" if detail else ""), flush=True)

    srv, base = serve()
    url = base + page_path
    check("page 200", status(url) == 200, str(status(url)))
    nc = status(base + "/work/no-such-page-cs-check")
    check("negative control: unknown URL 404", nc == 404, str(nc))

    exe = CHROMIUM if os.path.exists(CHROMIUM) else None
    with sync_playwright() as pw:
        browser = pw.chromium.launch(executable_path=exe)

        for scheme in ["light", "dark"]:
            ctx = browser.new_context(color_scheme=scheme, viewport={"width": 1280, "height": 900})
            page = ctx.new_page()
            errors = []
            page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            page.on("pageerror", lambda e: errors.append(str(e)))
            page.goto(url, wait_until="networkidle")
            check(f"no console errors ({scheme})", not errors, "; ".join(errors)[:300])

            if scheme == "light":
                title = page.title()
                h1 = page.locator("h1").inner_text().strip()
                check("title is the H1", title == f"{h1} - Thomas Cheesman", title)
                robots = page.locator('meta[name="robots"]').count()
                banner = page.locator(".draft").count()
                if preview:
                    check("preview: noindex present", robots == 1)
                    check("preview: draft banner present", banner == 1)
                else:
                    check("live: no noindex", robots == 0)
                    check("live: no draft banner", banner == 0)
                ids = page.eval_on_selector_all(".cs-section", "els => els.map(e => e.id)")
                check("six sections in order", ids == SECTIONS, ",".join(ids))
                hrefs = page.eval_on_selector_all("#navsub-work a", "els => els.map(e => e.getAttribute('href'))")
                check("sub-menu order", hrefs == SUBMENU, ",".join(hrefs))
                cur = page.eval_on_selector_all("#navsub-work a[aria-current='page']", "els => els.map(e => e.getAttribute('href'))")
                check("sub-menu aria-current=page on this page", cur == [page_path], ",".join(cur))
                proj = page.locator(".navsub > a[href='/projects']").get_attribute("aria-current")
                check("Projects aria-current=true", proj == "true", str(proj))

                # keyboard: Tab until the toggle has focus (never a fixed count)
                page.keyboard.press("Tab")
                for _ in range(30):
                    if page.evaluate("document.activeElement.classList.contains('navsub__toggle')"):
                        break
                    page.keyboard.press("Tab")
                on_toggle = page.evaluate("document.activeElement.classList.contains('navsub__toggle')")
                check("Tab reaches the sub-menu toggle", on_toggle)
                page.keyboard.press("Enter")
                page.wait_for_timeout(400)
                opened = page.locator(".navsub__toggle").get_attribute("aria-expanded")
                check("Enter opens the sub-menu", opened == "true", str(opened))
                page.keyboard.press("Escape")
                page.wait_for_timeout(400)
                closed = page.locator(".navsub__toggle").get_attribute("aria-expanded")
                back = page.evaluate("document.activeElement.classList.contains('navsub__toggle')")
                check("Esc closes it and returns focus", closed == "false" and back, f"{closed}, focus back {back}")

                links = page.eval_on_selector_all("a[href]", "els => els.map(e => e.href)")

            if shots:
                os.makedirs(shots, exist_ok=True)
                page.evaluate("window.scrollTo(0, 0)")
                page.wait_for_timeout(700)
                page.screenshot(path=f"{shots}/{scheme}-00-head.png")
                for i, sid in enumerate(SECTIONS, 1):
                    page.locator(f"#{sid}").scroll_into_view_if_needed()
                    page.evaluate(f"document.getElementById('{sid}').scrollIntoView({{block: 'start'}})")
                    page.wait_for_timeout(700)
                    page.screenshot(path=f"{shots}/{scheme}-{i:02d}-{sid}.png")
            ctx.close()

        ctx = browser.new_context(viewport={"width": 375, "height": 800}, color_scheme="light")
        page = ctx.new_page()
        page.goto(url, wait_until="networkidle")
        sw = page.evaluate("[document.documentElement.scrollWidth, document.documentElement.clientWidth]")
        check("no sideways scroll at 375px", sw[0] <= sw[1], f"{sw[0]} vs {sw[1]}")
        if shots:
            page.wait_for_timeout(700)
            page.screenshot(path=f"{shots}/light-375-head.png")
        ctx.close()

        ctx = browser.new_context(java_script_enabled=False, viewport={"width": 1280, "height": 900})
        page = ctx.new_page()
        page.goto(url)
        nojs_sections = page.eval_on_selector_all(".cs-section", "els => els.map(e => e.id)")
        nojs_links = page.eval_on_selector_all("a[href]", "els => els.length")
        nojs_words = len(page.locator("main").inner_text().split())
        check("JS off: sections, links and words present",
              nojs_sections == SECTIONS and nojs_links == len(links) and nojs_words > 300,
              f"{len(nojs_sections)} sections, {nojs_links} links, {nojs_words} words")
        ctx.close()
        browser.close()

    seen = {}
    for href in links:
        u = href.split("#")[0]
        if u.startswith("mailto:") or u in seen:
            continue
        if u.startswith(base):
            code = status(u)
        else:
            code = status(u)
            if code != 200:
                time.sleep(8)
                code = status(u)
        seen[u] = code
    bad = {u: c for u, c in seen.items() if c != 200 and not (c == 999 and "linkedin.com" in u)}
    for u, c in bad.items():
        print(f"      link {c}: {u.replace(base, '')}")
    check(f"links answer 200 ({len(seen)} unique)", not bad, f"{len(bad)} not 200")

    srv.shutdown()
    failed = [r for r in results if not r[0]]
    print(f"\n{len(results) - len(failed)} of {len(results)} checks passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
