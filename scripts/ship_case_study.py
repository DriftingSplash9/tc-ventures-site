"""ship_case_study.py — take case-study previews live: the sub-menu on every page, and the rest.

Usage: python scripts/ship_case_study.py work/<slug> [work/<slug> ...] [--dry-run] [--repo DIR]

A preview is a page in public/work/ that already carries the sub-menu it will
ship with (its own entry marked aria-current="page"), a noindex line and a
draft banner, and is listed in public/.assetsignore. The new entries' labels
and places are read from the preview itself, so a label and the order are
written once, in the page, and copied from there. Then this:

  1. adds each new entry to the sub-menu of every other page that has one
     (13 files today, _template.html included), after the entry before it,
     with the preview's label markup and the line's own indentation
  2. takes the noindex line and the draft banner off each page it ships
  3. takes each page out of public/.assetsignore, with any comment lines that
     headed only those pages
  4. adds each page to public/sitemap.xml after the entry before it, in the
     same shape
  5. sets SUBMENU in scripts/site_check.py and scripts/cs_check.py

Before anything is written, it checks all of this, and refuses on any failure:
  - each page is a preview: one noindex line and one banner, in .assetsignore,
    not in the sitemap
  - each preview's sub-menu is cs_check.py's PLANNED_SUBMENU, with the same
    labels on every preview, and its own entry is the only one marked current
  - PLANNED_SUBMENU without the pages being shipped is the sub-menu live now:
    SUBMENU in site_check.py and in cs_check.py, and on every other page
  - each new label is its page's H1 (a case study's sub-menu label is its H1)
Every edit goes through scripts/patch.py: all files or none, line endings kept.

It does not touch /projects or the home cards (that is copy, through a copy
review), and it proves nothing about the pages. After it, run
    python scripts/site_check.py
    python scripts/cs_check.py work/<slug>          (without --preview)
and look at the pages. Ship the page and its links in the same push.

--repo DIR runs it on another copy of the repo (a test), not this one.
Written 2026-09-29 (INFRA-13): the nav is copied into every page by hand.
"""
import ast, html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from patch import Patch, PatchError, key

SITE = "https://tc-ventures.ca"
MENU = re.compile(r'<ul class="navsub__list" id="navsub-work"[^>]*>\n(.*?)\n[ \t]*</ul>', re.S)
ITEM = re.compile(r'^[ \t]*<li><a href="([^"]+)"( aria-current="page")?>(.*?)</a></li>$', re.M)
NOINDEX = '<meta name="robots" content="noindex, nofollow">\n'
BANNER = re.compile(r'<div class="draft">\n.*?\n</div>\n\n', re.S)
WIDTH = 100


def menu(text):
    """[(href, current, label markup)] of the page's sub-menu, or None if it has none or it won't parse."""
    m = MENU.findall(text)
    if len(m) != 1:
        return None
    items = ITEM.findall(m[0])
    return [(h, bool(c), lab) for h, c, lab in items] if len(items) == m[0].count("<li>") else None


def h1(text):
    m = re.findall(r"<h1\b[^>]*>(.*?)</h1>", text, re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", m[0]))).strip() if len(m) == 1 else None


def py_list(text, name):
    """(the exact source of `NAME = [...]`, its value), or (None, None) unless it occurs once."""
    m = re.findall(rf"^{name} = \[.*?\]$", text, re.M | re.S)
    return (m[0], ast.literal_eval(m[0].split("=", 1)[1].strip())) if len(m) == 1 else (None, None)


def wrapped(name, items):
    """A flat list of strings, in cs_check.py's layout: wrapped under the bracket at WIDTH."""
    lines, cur = [], f"{name} = ["
    indent = " " * len(cur)
    for i, s in enumerate(items):
        tok = json.dumps(s) + ("]" if i == len(items) - 1 else ",")
        if cur.strip() not in (f"{name} = [",) and len(cur) + 1 + len(tok) > WIDTH:
            lines.append(cur)
            cur = indent + tok
        else:
            cur += tok if cur.endswith("[") else " " + tok
    return "\n".join(lines + [cur])


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the Windows console is cp1252
    args = sys.argv[1:]
    repo = os.path.abspath(args[args.index("--repo") + 1]) if "--repo" in args else os.path.join(HERE, "..")
    if "--repo" in args:
        del args[args.index("--repo"):args.index("--repo") + 2]
    dry = "--dry-run" in args
    slugs = [re.sub(r"\.html$", "", a.strip("/")) for a in args if not a.startswith("--")]
    if not slugs:
        sys.exit(__doc__)
    pub = os.path.join(repo, "public")
    new = ["/" + s for s in slugs]
    p, problems = Patch(), []

    def need(ok, msg):
        if not ok:
            problems.append(msg)
        return ok

    # --- what is live now, and what is planned
    site_py, cs_py = os.path.join(repo, "scripts", "site_check.py"), os.path.join(repo, "scripts", "cs_check.py")
    site_src, cs_src = Patch.read(site_py)[0], Patch.read(cs_py)[0]
    site_old, site_menu = py_list(site_src, "SUBMENU")
    cs_old, cs_menu = py_list(cs_src, "SUBMENU")
    _, planned = py_list(cs_src, "PLANNED_SUBMENU")
    if not (need(site_menu is not None, "site_check.py: no single SUBMENU = [...]")
            and need(cs_menu is not None, "cs_check.py: no single SUBMENU = [...]")
            and need(planned is not None, "cs_check.py: no single PLANNED_SUBMENU = [...]")):
        sys.exit("Refused, nothing written:\n  " + "\n  ".join(problems))
    live = [h for h, _ in site_menu]
    need(cs_menu == live, f"cs_check.py SUBMENU {cs_menu} is not site_check.py's {live}")
    need([h for h in planned if h not in new] == live,
         f"PLANNED_SUBMENU without {new} is {[h for h in planned if h not in new]}, not the live sub-menu {live}")
    for n in new:
        need(n in planned, f"{n} is not in PLANNED_SUBMENU")
        need(n not in live, f"{n} is already in the live sub-menu")

    # --- the previews
    labels, previews = {}, {}
    for s, n in zip(slugs, new):
        path = os.path.abspath(os.path.join(pub, s + ".html"))
        if not need(os.path.exists(path), f"{s}.html: no such page"):
            continue
        text = Patch.read(path)[0]
        previews[key(path)] = (path, text)
        items = menu(text)
        if not need(items is not None, f"{s}.html: no sub-menu that parses"):
            continue
        need([h for h, _, _ in items] == planned, f"{s}.html: sub-menu {[h for h, _, _ in items]} is not PLANNED_SUBMENU")
        need([h for h, c, _ in items if c] == [n], f"{s}.html: aria-current is on {[h for h, c, _ in items if c]}, not {n} alone")
        for h, _, lab in items:
            need(labels.setdefault(h, lab) == lab, f"{s}.html: label for {h} is {lab!r}, another preview has {labels[h]!r}")
        need(text.count(NOINDEX) == 1, f"{s}.html: {text.count(NOINDEX)} noindex lines, not 1")
        need(len(BANNER.findall(text)) == 1, f"{s}.html: {len(BANNER.findall(text))} draft banners, not 1")
        need(html.unescape(labels.get(n, "")) == h1(text), f"{s}.html: label {labels.get(n)!r} is not the H1 {h1(text)!r}")
    for h, lab in site_menu:
        need(h not in labels or html.unescape(labels[h]) == lab,
             f"label for {h}: previews have {labels.get(h)!r}, site_check.py has {lab!r}")
    if problems:
        sys.exit("Refused, nothing written:\n  " + "\n  ".join(problems))

    # 1. the sub-menu on every other page
    others = []
    for d, _, files in os.walk(pub):
        for f in sorted(files):
            path = os.path.abspath(os.path.join(d, f))
            if f.endswith(".html") and key(path) not in previews:
                text = Patch.read(path)[0]
                items = menu(text)
                if items is None:
                    need("navsub-work" not in text, f"{os.path.relpath(path, pub)}: a sub-menu that won't parse")
                    continue
                rel = os.path.relpath(path, pub)
                if need([h for h, _, _ in items] == live, f"{rel}: sub-menu {[h for h, _, _ in items]} is not the live one"):
                    others.append(path)
    for path in others:
        for n in [h for h in planned if h in new]:
            i = planned.index(n)
            li = f'<li><a href="{n}">{labels[n]}</a></li>'
            text = p.text(path)
            if i > 0:
                m = re.findall(rf'^[ \t]*<li><a href="{re.escape(planned[i - 1])}"(?: aria-current="page")?>.*?</a></li>\n', text, re.M)
                if need(len(m) == 1, f"{os.path.relpath(path, pub)}: {len(m)} entries for {planned[i - 1]}"):
                    indent = m[0][:len(m[0]) - len(m[0].lstrip())]
                    p.edit(path, m[0], m[0] + indent + li + "\n")
            else:
                m = re.findall(rf'^[ \t]*<li><a href="{re.escape(live[0])}"(?: aria-current="page")?>.*?</a></li>\n', text, re.M)
                if need(len(m) == 1, f"{os.path.relpath(path, pub)}: {len(m)} entries for {live[0]}"):
                    indent = m[0][:len(m[0]) - len(m[0].lstrip())]
                    p.edit(path, m[0], indent + li + "\n" + m[0])

    # 2. the previews: noindex and banner off
    for path, text in previews.values():
        p.edit(path, NOINDEX, "")
        p.edit(path, BANNER.findall(text)[0], "")

    # 3. .assetsignore
    ign = os.path.join(pub, ".assetsignore")
    text = Patch.read(ign)[0]
    lines = text.split("\n")
    drop = set()
    for s in slugs:
        at = [i for i, line in enumerate(lines) if line.strip() == s + ".html"]
        if need(len(at) == 1, f".assetsignore: {len(at)} lines for {s}.html, not 1"):
            drop.add(at[0])
    for i in sorted(drop):
        j = i - 1
        while j >= 0 and j in drop:
            j -= 1
        if j >= 0 and lines[j].startswith("#"):
            c0 = j
            while c0 > 0 and lines[c0 - 1].startswith("#"):
                c0 -= 1
            k, group = j + 1, []
            while k < len(lines) and lines[k].strip() and not lines[k].startswith("#"):
                group.append(k)
                k += 1
            if group and all(g in drop for g in group):
                drop |= set(range(c0, j + 1))
    if drop:
        p.edit(ign, text, "\n".join(l for i, l in enumerate(lines) if i not in drop))

    # 4. the sitemap
    sm = os.path.join(pub, "sitemap.xml")
    for n in [h for h in planned if h in new]:
        i = planned.index(n)
        text = p.text(sm)
        need(f"<loc>{SITE}{n}</loc>" not in text, f"sitemap.xml: already lists {n}")
        anchor = planned[i - 1] if i > 0 else live[0]
        m = re.findall(rf"^[ \t]*<url><loc>{re.escape(SITE + anchor)}</loc>.*?</url>\n", text, re.M)
        if need(len(m) == 1, f"sitemap.xml: {len(m)} entries for {anchor}"):
            line = m[0].replace(f"<loc>{SITE}{anchor}</loc>", f"<loc>{SITE}{n}</loc>")
            p.edit(sm, m[0], m[0] + line if i > 0 else line + m[0])

    # 5. the checkers
    menu_new = [(h, html.unescape(labels[h])) for h in planned]
    p.edit(site_py, site_old, "SUBMENU = [\n" + "".join(
        f"    ({json.dumps(h)}, {json.dumps(lab, ensure_ascii=False)}),\n" for h, lab in menu_new) + "]")
    p.edit(cs_py, cs_old, wrapped("SUBMENU", planned))

    if problems:
        sys.exit("Refused, nothing written:\n  " + "\n  ".join(problems))
    try:
        report = p.apply(dry=dry, base=repo)
    except PatchError as e:
        sys.exit(f"Refused: {e}")
    print(f"Shipping {', '.join(new)}: the sub-menu on {len(others)} other pages is now")
    for h, lab in menu_new:
        print(f"  {'+' if h in new else ' '} {h}  {lab}")
    print(report)
    if not dry:
        print("Next: python scripts/site_check.py, then python scripts/cs_check.py "
              + " / ".join(slugs) + " (without --preview), and look at the pages.")


if __name__ == "__main__":
    main()
