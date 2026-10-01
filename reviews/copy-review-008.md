# Copy review 008 — the ledger's traps layer

**Written:** 2026-10-01
**Why:** PL-9, the last of Phase 3. Ruled Q-P3-6 A (2026-09-29): "traps later, in their own review".
Started at Thomas's word, "go ahead with the traps layer". Propose before building.
**Status:** TL0, the proposal, for Thomas to rule. Nothing is built.

Same format and marks as copy-review-001 to 007: `OK` · `KEEP` · `A` / `B` · `FIX` · `CUT`.

---

## TL0 — the proposal (not copy)

**To rule:** TL0 as a whole (OK / FIX), plus Q-TL1 to Q-TL4. The words come after, as TL1 onward.

### 1. What the handoffs hold (read 2026-10-01, by script)

- **From handoff-019 on, every handoff has a traps section** with "New this session" and "Carried", and from
  020 a "Dropped this handoff" list. Every trap line ends with its tally `x.y` (§5 of any handoff):
  - **x:** handoffs carried since the one that recorded it;
  - **y:** sessions where its mention changed what was done.
- **Before 019,** handoffs have a "Traps" heading but no tallies and no "dropped" list.
- **Counted, 019 to 029:** 32 "New" lines and 31 "Dropped" lines.
  - Matched by exact wording, the "New" and "Carried" lines name 81 traps. **That's too many:** traps are
    reworded as they're carried, so one trap can appear under several wordings. Matching them is a
    curation pass (§3).
- **A tally dates a trap.** A trap tallied `x.y` in handoff N was recorded at N − x. By that reading, traps
  date back to 014, and 38 of the 81 wordings imply a start before 019.
- **When a trap helped can be read too.** Its y rises from one handoff to the next only in a session where
  its mention changed something, so each rise marks a handoff.

### 2. What it would look like

- **A new band, TRAPS, under DOMAIN,** in both pictures. Each trap is a thread, like an open item:
  - it starts at the handoff that recorded it;
  - it runs while it's carried;
  - **it ends where it was dropped,** with an end mark that says how:
    - **"into code":** dropped because a check or a script now does the job (rule 5);
    - **"retired":** dropped because it never helped (x > 5, y ≤ 1) or reached x = 10.
  - A trap still carried runs to the edge.
- **A small dot on the thread at each handoff where it helped** (y rose).
- **Colours as now:** carried traps in the accent, dropped ones muted. Nothing new in the palette, and
  nothing in the existing bands moves.
- **The scrubber covers it with no change:** at a past handoff, the TRAPS band shows the traps as they
  stood.
- **No trap's words appear.** The picture shows how many traps there were, how long each lasted, how it
  ended and when it helped. The traps' text stays in the handoffs, which the list already links. That
  follows LG0: no handoff prose on the page.

### 3. The curation pass

- **A new file, `ledger/traps.json`,** gives each trap an ID, and lists every wording it had, the handoff
  that recorded it, the handoff that dropped it and how it ended. The export reads it, never the prose.
- **The agent drafts it from the handoffs; Thomas rules on the doubtful matches** (truth rule 15: whoever
  extracts doesn't also decide).
  - A doubt is any pair of wordings that may be one trap, or a drop whose reason the handoff doesn't say.
  - The doubts go in a table here, one row each, for A / B.
- **`export-ledger.py --report`** gains a traps line: every trap wording in 019 onward matched to an ID, or
  it's a DOUBT, and the export stops. So a new handoff's traps can't slip in unmatched.

### 4. Checks (rule 5)

- `export-ledger.py --check` and `site_check.py` as now: the served block must be what the export writes.
- **New in `--report`:** every trap line from 019 onward matched to exactly one ID. The control is one
  wording removed from `traps.json`, which must fail.
- **New in the export, refused if wrong:** each trap's start equals its first handoff minus x (where the
  tally says so); a trap can't end before it starts; a dropped trap has an end kind.
- `shots_diff.py`: every page but the home page identical. The home page is looked at.

### Questions

**Q-TL1:** traps recorded before 019.
> **A (recommended):** draw them from the handoff their tally implies (back to 014), with the stretch before
> 019 dotted: there, the start is inferred from the tally, not read from a list.
>
> **B:** start every thread at 019, where the lists begin. Simpler, but 38 wordings would look newer than
> they are.

**Q-TL2:** how a dropped trap's ending shows.
> **A (recommended):** two end marks, "into code" and "retired", explained in the caption.
>
> **B:** one end mark for every drop, like a closed item.

**Q-TL3:** the "helped" dots.
> **A (recommended):** yes, a dot at each handoff where its y rose.
>
> **B:** no dots; the thread alone.

**Q-TL4:** the list under the picture (the text equivalent).
> **A (recommended):** add to each handoff's line from 019 on a short count, like "Traps: 2 recorded, 6
> retired". The words are a copy block (TL3), and the numbers come from `traps.json`.
>
> **B:** leave the list as it is, and say in the SVG's description that the TRAPS band isn't in the list.

### What the words will be (drafted after TL0 is ruled)

- **TL1:** the band's label ("TRAPS" or another word).
- **TL2:** the caption's added sentence, explaining the band and its end marks.
- **TL3:** the list's per-handoff count wording, if Q-TL4 is A.
- **TL4:** the two pictures' `<desc>` additions.

### The steps

1. TL0 ruled.
2. The curation pass: `traps.json` drafted, its doubts listed here for ruling.
3. The export, the picture and the checks built; TL1 to TL4 drafted; a local preview with screenshots.
4. Shipped on his word, and checked live from an up-to-date `main`.
