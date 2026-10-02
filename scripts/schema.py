"""schema.py — write each page's structured data (schema.org JSON-LD) from the page's own words.

Usage: python scripts/schema.py             write the blocks into public/
       python scripts/schema.py --check     exit 1 if any page isn't what this would write now
       python scripts/schema.py --controls  three broken copies, each of which --check must catch

Which pages (copy-review-009 SD1 and SD2, ruled 2026-10-01 "sd1 ok, sd2 ok, all A"):
  - index.html: a ProfilePage whose mainEntity is the Person (SD1). Its name is the page's <title>.
  - every case study, public/work/*.html with a claim under its H1 (not _template.html): a CreativeWork
    and a BreadcrumbList (SD2), filled from the page's own H1, claim and canonical URL.
  - every other page: no block.
The block sits at the end of <head>, between <!-- schema:begin ... --> and <!-- schema:end -->. Never
hand-edit it: edit the page's words or SD1's constants below, and re-run this.

--check fails when:
  - a page's block isn't what this would write now (or is missing, or a page that shouldn't have one does)
  - a string in a block isn't on the page: text must be in its visible text or <title>, a URL must be one of
    its links (resolved against its canonical URL) or the canonical itself
  - a page has any inline <script> other than a JSON-LD block (Q-P4-4 A), or a block that isn't valid JSON
site_check.py runs the same checks on every served page. Written 2026-10-01 for Phase 4 (P4-C).
"""
import html, json, os, re, sys, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(HERE, "..", "public")
SITE = "https://tc-ventures.ca/"
BEGIN = ("<!-- schema:begin: written by scripts/schema.py from this page's own words (copy-review-009 SD1, "
         "SD2). Re-run it; don't edit this block. -->")
BEGIN_RE = re.compile(r"<!-- schema:begin\b.*?-->")
END = "<!-- schema:end -->"
BLOCK_RE = re.compile(r"<!-- schema:begin\b.*?<!-- schema:end -->(\r?\n)?", re.S)   # with its own line end

# SD1, ruled. Each string must also be on the home page (--check).
PERSON = {
    "@type": "Person",
    "@id": SITE + "#person",
    "name": "Thomas Cheesman",
    "url": SITE,
    "email": "mailto:thomas@tc-ventures.ca",
    "address": {"@type": "PostalAddress", "addressLocality": "Grande Prairie", "addressRegion": "Alberta"},
    "sameAs": ["https://www.linkedin.com/in/thomas-cheesman-20234285/", "https://github.com/DriftingSplash9",
               "https://thomascheesman.ca"],
}
AUTHOR = {k: PERSON[k] for k in ("@type", "@id", "name", "url")}


def text_of(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", fragment))).strip()


def found(pattern, page):
    m = re.search(pattern, page, re.S)
    return text_of(m.group(1)) if m else None


def canonical(page):
    m = re.search(r'<link rel="canonical" href="([^"]+)"', page)
    return m.group(1) if m else None


def data_for(page):
    """The structured data this page should carry, or None."""
    canon = canonical(page)
    if canon == SITE:
        return {"@context": "https://schema.org", "@type": "ProfilePage", "@id": SITE + "#profile", "url": SITE,
                "name": found(r"<title>(.*?)</title>", page), "mainEntity": PERSON}
    claim = found(r'<p class="cs-head__claim">(.*?)</p>', page)
    if canon and "/work/" in canon and claim:
        h1 = found(r"<h1>(.*?)</h1>", page)
        return {"@context": "https://schema.org", "@graph": [
            {"@type": "CreativeWork", "@id": canon + "#case-study", "url": canon, "name": h1,
             "description": claim, "author": AUTHOR},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Thomas Cheesman", "item": SITE},
                {"@type": "ListItem", "position": 2, "name": "Projects", "item": SITE + "projects"},
                {"@type": "ListItem", "position": 3, "name": h1}]}]}
    return None


def render(page):
    """The block this page should carry (LF line endings), or None."""
    data = data_for(page)
    if data is None:
        return None
    body = json.dumps(data, ensure_ascii=False, indent=2).replace("</", "<\\/")
    return f'{BEGIN}\n<script type="application/ld+json">\n{body}\n</script>\n{END}'


def current(page):
    m = BLOCK_RE.search(page)
    return m.group(0).rstrip("\r\n").replace("\r\n", "\n") if m else None


def problems(page):
    """Everything --check would fail on this page's HTML."""
    out = []
    want, have = render(page), current(page)
    if want != have:
        out.append("no block, but it should have one" if have is None and want else
                   "a block, but it shouldn't have one" if want is None else
                   "the block isn't what schema.py writes now")
    for m in re.finditer(r"<script\b([^>]*)>(.*?)</script>", page, re.S):
        attrs, inner = m.group(1), m.group(2)
        if "src=" in attrs:
            continue
        if 'type="application/ld+json"' not in attrs:
            out.append("an inline <script> that isn't JSON-LD")
            continue
        try:
            data = json.loads(inner)
        except ValueError as e:
            out.append(f"a JSON-LD block that isn't valid JSON ({e})")
            continue
        out += [f"not on the page: {s!r}" for s in strings_not_on_page(data, page)]
    return out


def strings_not_on_page(data, page):
    canon = canonical(page) or SITE
    body = re.sub(r"<head\b.*?</head>|<script\b.*?</script>|<style\b.*?</style>", " ", page, flags=re.S)
    visible = text_of(body)
    title = found(r"<title>(.*?)</title>", page) or ""
    links = {urllib.parse.urljoin(canon, html.unescape(h)) for h in re.findall(r'href="([^"]+)"', page)}
    links.add(canon)
    missing = []
    def walk(x, key=""):
        if isinstance(x, dict):
            for k, v in x.items():
                walk(v, k)
        elif isinstance(x, list):
            for v in x:
                walk(v, key)
        elif isinstance(x, str) and not key.startswith("@"):
            if re.match(r"(https?:|mailto:)", x):
                if x not in links:
                    missing.append(x)
            elif x not in visible and x != title:
                missing.append(x)
    walk(data)
    return missing


def pages():
    out = [os.path.join(PUBLIC, f) for f in sorted(os.listdir(PUBLIC)) if f.endswith(".html")]
    work = os.path.join(PUBLIC, "work")
    out += [os.path.join(work, f) for f in sorted(os.listdir(work)) if f.endswith(".html") and not f.startswith("_")]
    return out


def write(path):
    raw = open(path, encoding="utf-8", newline="").read()
    nl = "\r\n" if "\r\n" in raw else "\n"
    page = BLOCK_RE.sub("", raw)
    block = render(page)
    if block:
        page = page.replace("</head>", block.replace("\n", nl) + nl + "</head>", 1)
    if page != raw:
        open(path, "w", encoding="utf-8", newline="").write(page)
        return True
    return False


def controls():
    """Three broken pages; each must be caught. Returns True if all are."""
    home = open(os.path.join(PUBLIC, "index.html"), encoding="utf-8").read()
    case = open(os.path.join(PUBLIC, "work", "gprs.html"), encoding="utf-8").read()
    bent = home.replace('"addressLocality": "Grande Prairie"', '"addressLocality": "Grand Prairie"', 1)
    cases = [   # (name, broken page, original, the problem it must raise)
        ("a string changed in the home block", bent, home, "not on the page: 'Grand Prairie'"),
        ("a case study's block removed", BLOCK_RE.sub("", case), case, "no block, but it should have one"),
        ("a bare inline <script> added", case.replace("</head>", "<script>1</script></head>", 1), case,
         "an inline <script> that isn't JSON-LD"),
    ]
    ok = True
    for name, broken, original, expect in cases:
        changed = broken != original
        caught = expect in problems(broken)
        print(("PASS " if changed and caught else "FAIL ") + f"control: {name} is caught" +
              ("" if changed else "  [the fault couldn't be planted: the page changed; fix controls()]"))
        ok &= changed and caught
    return ok


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the Windows console is cp1252
    args = sys.argv[1:]
    if "--controls" in args:
        sys.exit(0 if controls() else 1)
    if "--check" in args:
        bad = 0
        for p in pages():
            for prob in problems(open(p, encoding="utf-8").read()):
                print(f"FAIL {os.path.relpath(p, PUBLIC)}: {prob}")
                bad += 1
        print("ok: every page's structured data is what schema.py writes, and on the page" if not bad else
              f"{bad} problem(s)")
        sys.exit(1 if bad else 0)
    changed = [os.path.relpath(p, PUBLIC) for p in pages() if write(p)]
    print("wrote: " + (", ".join(changed) if changed else "nothing changed"))


if __name__ == "__main__":
    main()
