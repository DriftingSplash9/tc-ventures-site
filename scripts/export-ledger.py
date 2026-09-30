#!/usr/bin/env python3
"""
export-ledger.py  —  write the build ledger into the home page, from the handoffs

What it draws
-------------
One column per handoff (handoff-001.md onward), in order. One thread per open
item: from the handoff whose section 4 first lists it to the handoff where it
is gone, or where its own row says CLOSED or KILLED. Threads are grouped into
bands by the workstream heading the row sits under (### PLAN, ### COPY ...).
A thread still open at the last column runs to the edge: solid, or dotted if
ledger/curation.json marks the item parked.

Two pictures of the same data: landscape, and portrait for phones (CSS shows
one). In each, the threads sit in one <g class="lg__threads">, so
assets/ledger.js can clip them to a handoff (Phase 3 step 5). Under them, the
scrubber (copy-review-007 step 5): a slider, and every handoff's line stacked
in one place, one shown at a time. Then the caption. CSS shows it only when scripts run, and the
script leaves it out until its label is ruled (curation copy.scrub). Then an
ordered list, the text equivalent: one line per handoff, with its date,
linking the file on GitHub.

Curated by construction
-----------------------
No prose from a handoff reaches the page. The page carries only handoff
numbers, dates, workstream names, and the strings in ledger/curation.json,
which are ruled in a copy review before they ship (copy-review-006). Item IDs
are used for layout and never printed. Excluded before anything is drawn: rows
under the headings in curation "exclude", and IDs with the prefixes there (the
private project; other sites' items). As a last guard the script refuses to
write a block that mentions the private project by name.

The ledger stops at the last handoff whose line is ruled. A new handoff shows
up only after its line is ruled, so the ledger can lag the repo but is never
wrong about it.

How to run
----------
    python scripts/export-ledger.py             write into public/index.html
    python scripts/export-ledger.py --check     exit 1 if the page's block is not
                                                what this would write now
    python scripts/export-ledger.py --report    threads, doubts and flags; writes nothing
    python scripts/export-ledger.py --draft --html PATH
                                                preview: include unruled lines, write
                                                PATH (never public/index.html)

The page must already carry <!-- ledger:begin ... --> and <!-- ledger:end -->.
Written 2026-09-29 for Phase 2 (plan-001 §4c; copy-review-006 LG0, ruled).
"""
import datetime, html, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CURATION = ROOT / "ledger" / "curation.json"
PAGE = ROOT / "public" / "index.html"
REPO = "https://github.com/DriftingSplash9/tc-ventures-site/blob/main/"
BEGIN = ("<!-- ledger:begin: written by scripts/export-ledger.py from the handoffs and "
         "ledger/curation.json. Edit those and re-run it; do not edit this block. -->")
BEGIN_RE = re.compile(r"<!-- ledger:begin\b.*?-->", re.S)
END = "<!-- ledger:end -->"
DENY = re.compile(r"lander|rocket", re.I)
INF = 10 ** 9
ROW_ID = re.compile(r"^\|\s*\**([A-Z][A-Z0-9]*-\d+[a-z]?)\**\s*\|\s*(.*?)\s*\|")
ENDS_HERE = re.compile(r"\b(CLOSED|KILLED)\b")


def esc(s):
    return html.escape(s, quote=False)


# ---------------------------------------------------------------- reading --

def section(text, num):
    m = re.search(rf"^## {num}\..*?$(.*?)(?=^## \d+\.|\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def read_handoffs():
    out = []
    for p in sorted(ROOT.glob("handoff-[0-9][0-9][0-9].md")):
        t = p.read_text(encoding="utf-8")
        m = re.search(r"\*\*Written:\*\*\s*(\d{4}-\d{2}-\d{2})", t)
        rows, head = {}, None
        for line in section(t, 4).splitlines():
            h = re.match(r"^###\s+(.+?)\s*$", line)
            if h:
                head = h.group(1)
                continue
            r = ROW_ID.match(line)
            if r and head:
                rows[r.group(1)] = (head, r.group(2))
        out.append({"num": p.stem.split("-")[1], "file": p.name,
                    "written": m.group(1) if m else None, "rows": rows})
    nums = [int(h["num"]) for h in out]
    if nums != list(range(1, len(nums) + 1)):
        sys.exit(f"handoff numbers are not 1..N without gaps: {nums}")
    return out


def excluded(cur, item, head):
    ex = cur["exclude"]
    return head in ex["headings"] or item.split("-")[0] in ex["id_prefixes"]


def band_of(cur, head):
    b = cur["fold"].get(head, head)
    if b not in cur["bands"]:
        sys.exit(f"unknown workstream heading {head!r}: add it to curation bands, fold or exclude")
    return b


def build(cur, draft):
    """The handoffs the ledger shows, their dates and lines, and the threads."""
    hs = read_handoffs()
    shown = []
    for h in hs:
        c = cur["handoffs"].get(h["num"])
        if not c or not c.get("line") or not (c.get("ruled") or draft):
            break                                    # stop at the first unruled line
        date = cur["dates"].get(h["num"], {}).get("date") or h["written"]
        if not date:
            sys.exit(f"{h['file']}: no Written: date and no curation date")
        shown.append({**h, "date": date, "line": c["line"], "ruled": c.get("ruled")})
    if not shown:
        sys.exit("no handoff has a ruled line yet")
    n = len(shown)
    splits = cur.get("split", {})
    threads, doubts = [], []
    for item in sorted({i for h in shown for i in h["rows"]}):
        k = 0
        while k < n:
            if item not in shown[k]["rows"]:
                k += 1
                continue
            s = k
            while k + 1 < n and item in shown[k + 1]["rows"] and shown[k + 1]["num"] not in splits.get(item, []):
                k += 1
            run = [shown[j]["rows"][item] for j in range(s, k + 1)]
            ex = {excluded(cur, item, head) for head, _ in run}
            if ex == {True}:
                k += 1
                continue
            if ex == {True, False}:
                sys.exit(f"{item} moves between an excluded and a kept heading: decide it in curation")
            end, state, why = None, None, ""
            for j, (head, title) in enumerate(run):
                if ENDS_HERE.search(title):
                    end, state, why = s + j, "closed", f"row says {ENDS_HERE.search(title).group(1)}"
                    break
            if state is None:
                if k == n - 1:
                    end, state = n - 1, "open"
                else:
                    end, state, why = k + 1, "closed", "row gone"
            if state == "open" and item in cur["parked"]:
                state = "parked"
            first, last = run[0][1].lower(), run[-1][1].lower()
            wa, wb = set(re.findall(r"[a-z]{4,}", first)), set(re.findall(r"[a-z]{4,}", last))
            if wa and wb and not (wa & wb) and item not in cur["reviewed_ids"]:
                doubts.append(f"{item}: wording changed ({shown[s]['num']} vs {shown[k]['num']}); "
                              "same item or two? record it in curation reviewed_ids or split")
            threads.append({"id": item, "band": band_of(cur, run[-1][0]), "s": s, "e": end,
                            "state": state, "why": why})
            k += 1
    for item in cur["parked"]:
        if not any(t["id"] == item and t["state"] == "parked" for t in threads):
            doubts.append(f"{item}: marked parked in curation but not open at the last column")
    return shown, threads, doubts


# -------------------------------------------------------------- rendering --

def pack(ts):
    lanes = []
    for t in sorted(ts, key=lambda t: (t["s"], t["e"], t["id"])):
        stop = t["e"] if t["state"] == "closed" else INF
        for li, le in enumerate(lanes):
            if le < t["s"]:
                lanes[li], t["lane"] = stop, li
                break
        else:
            lanes.append(stop)
            t["lane"] = len(lanes) - 1
    return len(lanes)


def f(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


def day_labels(shown):
    """Label a column only where the date changes: '11 Sep', then '12', '16'..."""
    out, prev = {}, None
    for j, h in enumerate(shown):
        d = datetime.date.fromisoformat(h["date"])
        if prev is None or d.month != prev.month:
            out[j] = f"{d.day} {d.strftime('%b')}"
        elif d != prev:
            out[j] = str(d.day)
        prev = d
    return out


def thread_marks(t, a1, a2, fixed1, fixed2, horizontal):
    """a = position along time; fixed = position across. Returns SVG strings."""
    def pt(a, c):
        return (a, c) if horizontal else (c, a)
    (x1, y1), (x2, y2) = pt(a1, fixed1), pt(a2, fixed2)
    cls = {"closed": "lg__t", "open": "lg__t lg__t--open", "parked": "lg__t lg__t--parked"}[t["state"]]
    dot = {"closed": "lg__dot", "open": "lg__dot lg__dot--open", "parked": "lg__dot lg__dot--open"}[t["state"]]
    s = [f'<line class="{cls}" x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}"/>',
         f'<circle class="{dot}" cx="{f(x1)}" cy="{f(y1)}" r="1.8"/>']
    if t["state"] == "closed":
        if horizontal:
            s.append(f'<line class="lg__end" x1="{f(x2)}" y1="{f(y2 - 2.5)}" x2="{f(x2)}" y2="{f(y2 + 2.5)}"/>')
        else:
            s.append(f'<line class="lg__end" x1="{f(x2 - 2.5)}" y1="{f(y2)}" x2="{f(x2 + 2.5)}" y2="{f(y2)}"/>')
    return s


def threads_g(marks):
    """Every thread in one group, which assets/ledger.js clips to a handoff."""
    return '<g class="lg__threads">' + "".join(marks) + "</g>"


def scrubber(cur, shown):
    """The slider and every line stacked in one place (copy-review-007 step 5).

    Left out until its label is ruled. The last line is the one shown before
    the script runs; CSS hides the whole thing when scripts don't run."""
    s = cur["copy"].get("scrub") or {}
    if not s.get("ruled"):
        return []
    n = len(shown)
    # Where the first and last columns sit in the landscape picture (svg_land's
    # LEFT, RIGHT and W), so CSS can put the slider's ends under them.
    out = ['<div class="ledger__scrub" style="--lg-from: 9.746%; --lg-to: 3.814%">',
           f'<label for="ledger-scrub">{esc(s["label"])}</label>',
           f'<input type="range" id="ledger-scrub" min="1" max="{n}" step="1" value="{n}">',
           '<div class="ledger__read">']
    for j, h in enumerate(shown):
        on = " is-on" if j == n - 1 else ""
        out.append(f'<p class="ledger__at{on}"><b>{h["num"]}</b> <time datetime="{h["date"]}">{h["date"]}</time> '
                   f'<span>{esc(h["line"])}</span></p>')
    return out + ['</div>', '</div>']


def svg_land(cur, shown, threads):
    n = len(shown)
    W, LEFT, RIGHT, TOP, ROW, PAD = 944, 92, 908, 28, 5, 7   # scrubber() mirrors LEFT, RIGHT and W
    col = [LEFT + (j * (RIGHT - LEFT) / (n - 1) if n > 1 else 0) for j in range(n)]
    spacing = (RIGHT - LEFT) / (n - 1) if n > 1 else 99
    step = next(s for s in (1, 2, 5, 10, 20, 50) if s * spacing >= 26)
    body, marks, y = [], [], TOP
    for b in cur["bands"]:
        ts = [t for t in threads if t["band"] == b]
        if not ts:
            continue
        lanes = pack(ts)
        h = PAD * 2 + (lanes - 1) * ROW
        body.append(f'<line class="lg__sep" x1="0" y1="{f(y - 3)}" x2="{W}" y2="{f(y - 3)}"/>')
        body.append(f'<text class="lg__band" x="0" y="{f(y + h / 2 + 3.5)}">{esc(b)}</text>')
        for t in sorted(ts, key=lambda t: (t["lane"], t["s"])):
            c = y + PAD + t["lane"] * ROW
            a2 = col[t["e"]] if t["state"] == "closed" else W - 4
            marks += thread_marks(t, col[t["s"]], a2, c, c, True)
        y += h + 6
    grid = []
    for j, x in enumerate(col):
        grid.append(f'<line class="lg__col" x1="{f(x)}" y1="{TOP - 6}" x2="{f(x)}" y2="{f(y - 4)}"/>')
        if j % step == 0 or j == n - 1:
            grid.append(f'<text class="lg__num" x="{f(x)}" y="{TOP - 11}" text-anchor="middle">{shown[j]["num"]}</text>')
    last_right = -INF
    for j, lab in day_labels(shown).items():
        half = len(lab) * 3.1
        if col[j] - half > last_right + 4:
            grid.append(f'<text class="lg__date" x="{f(col[j])}" y="{f(y + 12)}" text-anchor="middle">{esc(lab)}</text>')
            last_right = col[j] + half
    H = y + 18
    c = cur["copy"]
    return (f'<svg class="ledger__pic ledger__pic--land" viewBox="0 0 {W} {f(H)}" role="img" '
            f'aria-labelledby="ledger-land-t ledger-land-d">'
            f'<title id="ledger-land-t">{esc(c["title"])}</title>'
            f'<desc id="ledger-land-d">{esc(c["desc_land"])}</desc>'
            + "".join(grid) + "".join(body) + threads_g(marks) + "</svg>")


def svg_port(cur, shown, threads):
    n = len(shown)
    TOP, RS, X0, LANE, PAD, GAP = 74, 16, 70, 6, 6, 5
    row = [TOP + j * RS for j in range(n)]
    bottom = row[-1] + 12
    body, marks, x = [], [], X0
    for b in cur["bands"]:
        ts = [t for t in threads if t["band"] == b]
        if not ts:
            continue
        lanes = pack(ts)
        w = PAD * 2 + (lanes - 1) * LANE
        body.append(f'<line class="lg__sep" x1="{f(x - 2.5)}" y1="{TOP - 8}" x2="{f(x - 2.5)}" y2="{f(bottom)}"/>')
        body.append(f'<text class="lg__band" transform="translate({f(x + w / 2 + 3.5)} {TOP - 12}) rotate(-90)">'
                    f'{esc(b)}</text>')
        for t in sorted(ts, key=lambda t: (t["lane"], t["s"])):
            c = x + PAD + t["lane"] * LANE
            a2 = row[t["e"]] if t["state"] == "closed" else bottom
            marks += thread_marks(t, row[t["s"]], a2, c, c, False)
        x += w + GAP
    W = x + 2
    grid = []
    for j, yy in enumerate(row):
        grid.append(f'<line class="lg__col" x1="{X0 - 4}" y1="{f(yy)}" x2="{f(W)}" y2="{f(yy)}"/>')
        grid.append(f'<text class="lg__num" x="0" y="{f(yy + 3.5)}">{shown[j]["num"]}</text>')
    for j, lab in day_labels(shown).items():
        grid.append(f'<text class="lg__date" x="26" y="{f(row[j] + 3.5)}">{esc(lab)}</text>')
    H = bottom + 4
    c = cur["copy"]
    return (f'<svg class="ledger__pic ledger__pic--port" viewBox="0 0 {f(W)} {f(H)}" role="img" '
            f'aria-labelledby="ledger-port-t ledger-port-d">'
            f'<title id="ledger-port-t">{esc(c["title"])}</title>'
            f'<desc id="ledger-port-d">{esc(c["desc_port"])}</desc>'
            + "".join(grid) + "".join(body) + threads_g(marks) + "</svg>")


def render(cur, draft=False):
    shown, threads, doubts = build(cur, draft)
    c = cur["copy"]
    if not (c.get("ruled") or draft):
        sys.exit("the ledger's own copy (curation copy) is not ruled yet; use --draft for a preview")
    if draft and c.get("scrub") and not c["scrub"].get("ruled"):
        c = dict(c, scrub=dict(c["scrub"], ruled="draft"))
        cur = dict(cur, copy=c)
    items = []
    for h in shown:
        items.append(f'<li><a href="{REPO}{h["file"]}">{h["file"][:-3]}</a> '
                     f'<time datetime="{h["date"]}">{h["date"]}</time> '
                     f'<span>{esc(h["line"])}</span></li>')
    block = "\n".join([
        BEGIN,
        '<figure class="ledger">',
        svg_land(cur, shown, threads),
        svg_port(cur, shown, threads),
        *scrubber(cur, shown),
        f'<figcaption>{c["caption_html"]}</figcaption>',
        "</figure>",
        '<details class="ledger__list">',
        f'<summary>{esc(c["summary"])}</summary>',
        '<ol>', *items, '</ol>',
        "</details>",
        END,
    ])
    if DENY.search(block):
        sys.exit("refusing to write: the block mentions the private project")
    return block, shown, threads, doubts


def splice(page_text, block):
    m1 = BEGIN_RE.search(page_text)
    i2 = page_text.find(END)
    if not m1 or i2 < m1.start():
        sys.exit("the page has no <!-- ledger:begin --> ... <!-- ledger:end --> markers")
    return page_text[:m1.start()] + block + page_text[i2 + len(END):]


def current_block(page_text):
    m1 = BEGIN_RE.search(page_text)
    i2 = page_text.find(END)
    return page_text[m1.start():i2 + len(END)] if m1 and i2 > m1.start() else None


def main():
    args = sys.argv[1:]
    cur = json.loads(CURATION.read_text(encoding="utf-8"))
    draft = "--draft" in args
    target = pathlib.Path(args[args.index("--html") + 1]).resolve() if "--html" in args else PAGE.resolve()
    block, shown, threads, doubts = render(cur, draft)

    if "--report" in args:
        print(f"columns: {shown[0]['num']}..{shown[-1]['num']}"
              + ("  (draft: unruled lines included)" if draft else ""))
        for state in ("closed", "open", "parked"):
            print(f"  {state}: {sum(t['state'] == state for t in threads)}")
        for t in threads:
            if t["why"].startswith("row says"):
                print(f"  ends on its own row: {t['id']} at {shown[t['e']]['num']} ({t['why']})")
        for d in doubts:
            print("  DOUBT", d)
        return

    raw = target.read_bytes().decode("utf-8")
    crlf = "\r\n" in raw
    text = raw.replace("\r\n", "\n")
    if "--check" in args:
        now = current_block(text)
        if now != block:
            print("FAIL: the page's ledger is not what export-ledger.py would write now"
                  + ("" if now else " (no ledger block found)"))
            sys.exit(1)
        print(f"ok: the page's ledger matches (columns {shown[0]['num']}..{shown[-1]['num']})")
        return
    if draft and target == PAGE.resolve():
        sys.exit("--draft never writes public/index.html; pass --html PATH for a preview")
    out = splice(text, block)
    if crlf:
        out = out.replace("\n", "\r\n")
    target.write_bytes(out.encode("utf-8"))
    print(f"wrote the ledger into {target} (columns {shown[0]['num']}..{shown[-1]['num']})")
    for d in doubts:
        print("DOUBT", d)


if __name__ == "__main__":
    main()
