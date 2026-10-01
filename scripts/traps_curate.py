"""Curation pass, draft: group every trap entry in handoffs 019..latest into traps, and list the doubts.

Each entry: handoff N, kind (New / Carried / Dropped), lead (the first bold run, or the quoted name on a
Dropped line), tally x.y. A trap's start is N - x. An entry joins the trap that was seen in the handoff
before, has the same start, and has the most similar lead. Anything that doesn't fit cleanly is a DOUBT."""
import re, sys, glob, os, json, difflib

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
R = r"C:\Users\thoma\Desktop\My Files\Website Projects\tc-ventures site"
OUT = sys.argv[1] if len(sys.argv) > 1 else None
TALLY = re.compile(r"`(\d+)\.(\d+)`")


def section(t):
    m = re.search(r"^### Traps.*?$(.*?)(?=^## \d|\Z)", t, re.M | re.S)
    return m.group(1) if m else ""


entries = []
for f in sorted(glob.glob(os.path.join(R, "handoff-0[0-9][0-9].md"))):
    n = int(re.search(r"handoff-(\d+)", f).group(1))
    if n < 19:
        continue
    kind, item = None, []
    def flush():
        if not item or kind is None:
            return
        txt = " ".join(item)
        if kind == "Dropped":
            q = re.search(r"[\"“](.+?)[\"”]", txt) or re.match(r"\*\*(.+?)\*\*", txt)
            lead = q.group(1) if q else re.split(r"\s*\(", txt)[0][:80]
        else:
            b = re.match(r"\*\*(.+?)\*\*", txt)          # a name in bold only if the item starts with it
            if b:
                lead = b.group(1)
            else:
                s = re.match(r"(.+?[.:])(\s|$)", txt)    # else its first sentence
                lead = s.group(1) if s else txt[:80]
        tl = TALLY.findall(txt)
        x, y = (int(tl[-1][0]), int(tl[-1][1])) if tl else (None, None)
        entries.append({"n": n, "kind": kind, "lead": re.sub(r"\s+", " ", lead).strip(), "x": x, "y": y, "text": txt})
    for line in section(open(f, encoding="utf-8").read().replace("\r\n", "\n")).splitlines():
        h = re.match(r"^\*\*(New|Dropped|Carried)[^*]*\*\*\s*(.*)$", line)
        if h:
            flush(); item = []; kind = h.group(1)
            if h.group(2).strip():                          # an item written on the heading line itself
                item = [h.group(2).strip()]
            continue
        if re.match(r"^\*\*[A-Z]", line):                  # another bold heading (e.g. "Audit"): not a trap list
            flush(); item = []; kind = None; continue
        if line.startswith("- "):
            flush(); item = [line[2:]]
        elif line.strip() and item:
            item.append(line.strip())
    flush()


def sim(a, b):
    a, b = re.sub(r"[`*]", "", a.lower()), re.sub(r"[`*]", "", b.lower())
    if a and b and (a in b or b in a):                     # one wording contains the other
        return 1.0
    return difflib.SequenceMatcher(None, a, b).ratio()


traps, doubts, notes = [], [], []
LINKS = [
    (20, "Never start a Bash command with", "Bash `cd` moves"),
    (20, "`.assetsignore`, `sitemap.xml`", "Git Bash `grep -c"),
    (27, "A gate must run on its own", "In PowerShell, `;`"),
]
entries = [e for e in entries if not (e["x"] is None and e["lead"].strip(" .").lower() in ("", "none"))]
for e in entries:
    if e["x"] is None:
        doubts.append(f"{e['n']:03d} {e['kind']}: no tally, not a trap? — {e['lead'][:70]}")
        continue
    start = e["n"] - e["x"]
    if e["kind"] == "Dropped":
        cands = [t for t in traps if t["last"] == e["n"] - 1 and "end" not in t]
    else:
        cands = [t for t in traps if t["last"] == e["n"] - 1 and "end" not in t]
    scored = sorted(((sim(e["lead"], t["leads"][-1]), t) for t in cands), key=lambda p: -p[0])
    best = scored[0] if scored else (0, None)
    same_start = [p for p in scored if p[1]["start"] == start]
    pick = None
    # A rewording the matcher can't see is an explicit link (handoff, new wording's start, old wording's
    # start). Each one is listed in copy-review-008 for Thomas to rule.
    link = next((l for l in LINKS if l[0] == e["n"] and e["lead"].startswith(l[1])), None)
    if link:
        hits = [t for t in cands if t["leads"][-1].startswith(link[2])]
        if len(hits) != 1:
            sys.exit(f"link {link} finds {len(hits)} traps")
        pick = hits[0]
        notes.append(f"{e['n']:03d} {e['kind']}: LINK '{link[2][:40]}' → '{link[1][:40]}' (starts {pick['start']:03d}/{start:03d})")
    elif same_start and same_start[0][0] >= 0.3:
        pick = same_start[0][1]
        if len(same_start) > 1 and same_start[1][0] >= 0.45 and same_start[0][0] - same_start[1][0] < 0.15:
            doubts.append(f"{e['n']:03d} {e['kind']}: two close matches with start {start:03d}: "
                          f"'{same_start[0][1]['leads'][-1][:40]}' / '{same_start[1][1]['leads'][-1][:40]}' for '{e['lead'][:40]}'")
    elif best[1] is not None and best[0] >= 0.6:
        pick = best[1]
        doubts.append(f"{e['n']:03d} {e['kind']}: matched by wording but the start differs "
                      f"({pick['start']:03d} vs {start:03d}): '{e['lead'][:60]}'")
    if e["kind"] == "Dropped":
        if pick is None:
            doubts.append(f"{e['n']:03d} Dropped: no carried trap matches '{e['lead'][:70]}' (start {start:03d})")
            continue
        t = pick
        t["end"] = e["n"]
        low = e["text"].lower()
        done = re.search(r"(it'?s|it is|is) in code|in code now|with a check|\bcarries it\b|§3 rule", low)
        maybe = re.search(r"belongs in code", low)
        t["how"] = "into code" if done else "retired"
        t["how_sure"] = bool(done) or not maybe
        t["drop_text"] = re.sub(r"\s+", " ", e["text"])[:220]
        continue
    if pick is None:
        if e["kind"] == "Carried" and e["n"] > 19:
            doubts.append(f"{e['n']:03d} Carried: starts a new trap, but it's listed as carried — '{e['lead'][:60]}'")
        if e["kind"] == "New" and e["x"] != 0:
            doubts.append(f"{e['n']:03d} New: tally {e['x']}.{e['y']}, expected 0.y — '{e['lead'][:60]}'")
        pick = {"start": start, "leads": [], "seen": [], "y": {}, "last": None}
        traps.append(pick)
    t = pick
    if e["lead"] not in t["leads"]:
        t["leads"].append(e["lead"])
    t["seen"].append(e["n"]); t["y"][e["n"]] = e["y"]; t["last"] = e["n"]

latest = max(e["n"] for e in entries)
for t in traps:
    if "end" not in t and t["last"] != latest:
        doubts.append(f"{t['last']:03d}: '{t['leads'][-1][:60]}' (start {t['start']:03d}) stops after {t['last']:03d} "
                      f"with no Dropped line")
    ys = sorted(t["y"].items())
    t["helped"] = [n for (p, yp), (n, yn) in zip(ys, ys[1:]) if yn > yp]
    first_n, first_y = ys[0]
    t["helped_before_lists"] = first_y if first_n == 19 else 0

for i, t in enumerate(sorted(traps, key=lambda t: (t["start"], t["seen"][0])), 1):
    t["id"] = f"T{i:02d}"
print(f"entries {len(entries)}, traps {len(traps)}, ended {sum('end' in t for t in traps)}, "
      f"open {sum('end' not in t and t['last'] == latest for t in traps)}, doubts {len(doubts)}")
for d in doubts:
    print("DOUBT", d)
for n_ in notes:
    print("NOTE ", n_)
print("--- drops (end, start, how, sure):")
for t in sorted([t for t in traps if "end" in t], key=lambda t: t["end"]):
    print(f"  {t['end']:03d} from {t['start']:03d} {t['how']:<9} {'' if t['how_sure'] else 'UNSURE '}"
          f"{t['leads'][-1][:50]} || {t['drop_text'][:110]}")
if OUT:
    data = [{"id": t["id"], "start": t["start"], "end": t.get("end"), "how": t.get("how"),
             "helped": t["helped"], "helped_before_lists": t["helped_before_lists"], "wordings": t["leads"],
             "seen": [t["seen"][0], t["seen"][-1]]} for t in sorted(traps, key=lambda t: t["id"])]
    json.dump(data, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", OUT)
