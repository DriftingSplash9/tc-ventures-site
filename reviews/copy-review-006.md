# Copy review 006 — Phase 2, the build ledger

**Written:** 2026-09-29
**Why:** Phase 2 (PL-6, plan-001 §4c and §6 Q2 A): the home-page hero is the build ledger, a static SVG
of this site's own history. Propose before building.
**Status:** Step 1 (LG0, the proposal) **ruled 2026-09-29: "LG0 ok, all A"** (Q-LG1 to Q-LG5 all A; see
"Rulings" at the end). Step 2 (the build and the copy) in progress.

Same format and marks as copy-review-001 to 005: `OK` · `KEEP` · `A` / `B` · `FIX` · `CUT`.

---

## LG0 — Step 1: the proposal (not copy)

**To rule:** LG0 as a whole (OK / FIX), plus Q-LG1 to Q-LG5.

**Read 2026-09-29:** plan-001 §4c, §5 and §6; handoff-018 §6 (the first brief for this proposal);
`public/index.html` as it is; every handoff's `Written:` line, its §2 traps heading and its §4 tables,
parsed by a scratchpad script. Nothing on the site changed.

**The sketch:** drawn by that script from the real §4 tables, landscape, light and dark. It went to Thomas
in the chat. It isn't kept on disk, and it's a picture of the data, not a design.

### 1. What it shows

- **One column per handoff**, 001 to the newest, in order. Day labels run underneath where the date
  changes. The spacing is by session, not by calendar: three handoffs share 2026-09-19 and three share
  2026-09-21.
- **One thread per open item:** from the handoff whose §4 first lists it to the handoff where it closes.
  - Threads are grouped into bands by workstream (PLAN, COPY, DESIGN, PROJECTS, A11Y, INFRA, DOMAIN).
    CONTACT folds into COPY and GRAPH into PROJECTS, as the later handoffs already do.
  - A thread that closed ends in a tick.
  - A thread still open runs to the right edge in the accent colour.
- **Out of it:**
  - **Other repos' items (O-\*).** It's this site's ledger. They are also the rows with the most private
    material (O-4, O-7, O-21). They were the tallest band: without them, and with tighter spacing, the
    sketch went from 536 to 340 units tall.
  - **LANDER rows and L-\* IDs.** They are dropped before anything is drawn.
  - **Traps, for now.** Until handoff-019, each file lists new and carried traps under one heading, so a
    per-session count would be hand-sorted. They could be added from 019 on, later.
- **One line per handoff** in plain words ("Receipts inventory ruled; the twenty truth rules written"):
  - Written for the ledger and ruled here as LG blocks.
  - Never copied from the handoff. Some `Covers:` lines name the private project (007, 008).

**The risk the sketch showed:** most threads are still open, so at a glance it reads as a growing backlog.
Many of those rows aren't unfinished work. They are parked on purpose:
- C-17 and C-21: "Do not raise it again or change it unasked."
- INFRA-9: HSTS without preload, which is deliberate.
- D-1: harmless.
- A-1: deferred by Thomas.

**Q-LG1:** how to draw parked items.
> **A (recommended):** a parked item is drawn dotted, and the caption says what dotted means. Each item is
> marked parked or open from its own row's words. The list comes to you for OK in step 2.
>
> **B:** every item is drawn the same.

### 2. The data path (no build step)

- **`scripts/export-ledger.py`, run by hand:**
  - It reads `handoff-*.md` and `ledger/curation.json`, which is kept by hand. The curation file holds:
    - the ruled one-liners;
    - the parked flags;
    - the date fix (Q-LG5);
    - which reused IDs are two items;
    - the exclusions.
  - It writes the SVG and the list into `public/index.html`, between `<!-- ledger:begin -->` and
    `<!-- ledger:end -->`.
  - It's the same pattern as `export-gp-budget.py`.
- **Curated by construction:** the script copies no prose from a handoff. The page can only carry IDs,
  dates, workstream names and the ruled lines.
- **Checks (rule 5), each with a control that must fail:**
  - `--check` fails when the page's ledger block isn't what the script would write now, so a stale
    ledger is caught.
  - `site_check.py` gains three cases: the ledger is present, its list renders with JS off, and nothing
    is wider than the screen at 375px.
- **Upkeep:**
  - The session that writes handoff-NNN drafts its one-liner in the open copy review.
  - The column appears once Thomas rules the line. Until then the ledger stops at the last ruled
    handoff: behind, but never wrong.
- **Weight:** the sketch's SVG is about 18 KB raw and about 2.3 KB gzipped (measured). A second,
  portrait copy for phones (Q-LG4) about doubles that.

**Found in the data (the export reports these; the curation file decides, step 2):**
- **G-7 means two different items:** link midpoints (005) and the demo paragraph (019 on). The gap between
  them splits it into two threads.
- **Four more IDs in scope change wording between their first and last row:** C-15, G-2, INFRA-5, PL-7.
  I'll read each and propose "same item" or "two items". (O-3 and O-23 do too, but they are other-repo
  items, which are out.)
- **Some rows stay in §4 a handoff after they close** ("CLOSED", "RULED, live": O-23, PL-7). The thread
  ends at the row that says so.
- **013, 014 and 015 have no "Closed" list.** Their threads end where the rows disappear.

### 3. Without JavaScript, and for screen readers

- **The SVG is a picture:** `role="img"`, a title, a one-sentence description, and no links inside it.
  A-1 already doubts whether links inside an SVG image reach a screen reader.
- **The list is the equivalent and carries the links.** It's an ordered list of the handoffs, each with
  its date and ruled line. It sits in a `<details>` element ("The ledger as a list"), which opens without
  JS.
- **Phase 3 can add motion and click-to-read on top:** threads drawing in session by session, and a
  click on a column to read its line. The words never depend on either.

**Q-LG2:** what each line in the list links.
> **A (recommended):** each line links its handoff on GitHub. Pages already link seven handoffs (002,
> 003, 011, 012, 015, 016, 017), so this follows precedent. But every handoff mentions the private
> project, and 007 and 008 are mostly about it. Those two would be linked for the first time.
>
> **B:** no per-handoff links. One link under the ledger to the repo's list of handoffs.

### 4. Where it sits, and what it replaces

- **Order:** label, H1, lede (R3 and R4 unchanged, C-17), buttons, then the ledger as a wide figure
  closing the hero.
- **The caption** links `/work/this-site` and `/method`, describes rather than counts, and says what
  grey, teal, ticks and dots mean. It's drafted in step 2.
- **The final layout is Phase 3's job.**

**Q-LG3:** R5, the body paragraph under the lede.
> **A (recommended):** cut its first sentence (the research application). Card one says the same thing
> just below, with the same "nearly 4,000". Keep "I am looking for remote work running a nonprofit's
> website and digital operations." It's the only line on the first screen that says he's looking.
>
> **B:** keep R5 whole.
>
> **C:** cut R5 whole. The ask then appears first in "What I am looking for".

**Q-LG4:** phones. At 375px the landscape sketch's labels shrink to about 3px.
> **A (recommended):** the script also draws a portrait version (handoffs top to bottom, bands side by
> side), and CSS shows it below about 600px. No JS needed.
>
> **B:** phones get the list only, and the picture is hidden.

### 5. One date

**Q-LG5:** handoff-004 says "Written: 2026-09-17". handoff-005 says 004 "was dated a day ahead", and git
first saw 004 on 2026-09-16.
> **A (recommended):** the ledger shows 2026-09-16 for 004.
>
> **B:** show it as written.

### After LG0

1. **Step 2:** build the export script, the curation file and the checks, with controls. Draft the copy:
   - **LG1:** the caption.
   - **LG2 onward:** one line per handoff.
   - **R5:** the cut, per Q-LG3.
   - The parked list (Q-LG1) and the reused-ID calls.
2. **Step 3:** a local preview of the home page, light, dark and at 375px, for Thomas to look at.
3. **Ship** on his word, and check it live.

### Rulings, LG0 (2026-09-29)

Thomas, verbatim: **"LG0 ok, all A"**. Read as:
- LG0 OK as proposed.
- Q-LG1 A: parked items dotted.
- Q-LG2 A: each list line links its handoff on GitHub, 007 and 008 included.
- Q-LG3 A: cut R5's first sentence and keep "I am looking for…". The cut itself ships as a copy block
  in step 2.
- Q-LG4 A: a portrait version for phones.
- Q-LG5 A: 004 shows 2026-09-16.

---

## Step 2 — built, and the copy for Thomas to rule (2026-09-29)

**To rule:**
- LG1, LG2–LG24 and LG25 (OK / FIX / CUT each; "LG2–24 ok" is a full ruling).
- LGP and LGR (OK / FIX).
- Then look at the preview shots.

### What was built (on disk, not live)

- **`scripts/export-ledger.py`:** its docstring is the manual.
  - `--report` lists threads and doubts.
  - `--check` fails when the page's ledger isn't what it would write now.
  - `--draft --html PATH` is for previews only, and refuses `public/index.html`.
  - It stops at the first handoff whose line isn't ruled, and refuses any block that names the private
    project.
- **`ledger/curation.json`:** everything below that reaches the page, plus the parked flags, the 004 date and
  the reviewed IDs. Every `ruled` is null until you rule it.
- **`scripts/site_check.py` gains five ledger checks:**
  - the served block matches the script;
  - landscape shows at 1280px;
  - portrait shows at 375px;
  - the list opens with JS off;
  - every list link is a handoff file that exists, numbered from 001.
- **Not yet in `public/`:** the ledger CSS (a new block at the end of `style.css`), the R5 cut, and the
  markers in `index.html`. They go in at ship, and until then the real `public/` is unchanged.

**Checked:**
- **The preview** (a copy of `public/` with those edits and the draft lines): `site_check.py` passed 105
  of 105.
- **Control:** the same run on the real `public/` fails exactly the 5 ledger checks, and the other 100 pass.
- **Eleven more controls, each breaking one thing.** All behaved:
  - one changed character → only the block check fails;
  - no ledger CSS → only the two picture checks fail;
  - a link to handoff-099 → the links check fails;
  - an unreviewed wording change → reported;
  - the private project named in a line → refused;
  - lines ruled only up to 005 → the ledger stops at 005;
  - an unknown workstream → the export stops;
  - `--draft` against `public/` → refused;
  - and the `--check` comparison.
- **Screenshots looked at:** light and dark at 1280, both at 375, and the list opened. No sideways scroll
  at 1280 or 375.
- **Privacy read of the whole block's text:** 0 item IDs. It links only `/method`, `/work/this-site` and
  the 23 handoff files.
- **Weight (measured):** the home page goes from 11.6 KB to 50.5 KB raw, and 3.7 KB to 10.0 KB gzipped.

**Found, not fixed (Phase 3):** at 1280×900 the ledger sits below the fold, under the tall lede. The first
screen still shows H1, lede and buttons, as now. Where the ledger sits against them is Phase 3 layout
(LG0 §4).

### LG1 — the ledger's own copy

> **Caption:** The build ledger. Time runs in numbered handoffs: the files that pass this site's work from
> one session to the next. Each line is an item a handoff left open, running until the session that closed
> it. Teal lines are still open; dotted ones are parked on purpose or waiting on me. A script draws it from
> the handoffs themselves, and leaves out items about my other sites. *How I work* · *This site's case
> study* (links to `/method` and `/work/this-site`)
>
> **List heading** (the `<details>` summary): The ledger as a list, one line per handoff
>
> **Picture name** (screen readers): The build ledger
>
> **Picture description, desktop:** Each column is one numbered handoff, the file that passes this site's
> work from one session to the next, oldest on the left. Each line is an item a handoff left open, running
> from the handoff that opened it to the one that closed it, in bands by workstream. Lines still open run
> to the right edge; dotted ones are parked on purpose or waiting on me.
>
> **Picture description, phone:** the same, with "Each row", "oldest at the top" and "the bottom edge".

- **"Teal"** is the accent in both themes. In dark mode it's the lighter teal.
- **"Time runs in numbered handoffs"**, not "each column": on a phone the handoffs are rows.

### LG2–LG24 — one line per handoff

Each line rests on the handoff's own `Covers:` and `Status at wrap:` lines. The last column quotes them,
verbatim but shortened (…).
- **"I"** is used only where the handoff says Thomas did it.
- **Left out on purpose:**
  - 004's Bare Your Rare incident;
  - 008's removal of the private project;
  - 011's GPRS board work;
  - 022's 429.

| # | Handoff | Line | Rests on |
|---|---|---|---|
| LG2 | 001 · 2026-09-11 | From a standing start to a live site on tc-ventures.ca. | "everything from a standing start to a live site on the domain." |
| LG3 | 002 · 2026-09-12 | I read the copy that was already public and ruled on every block; all four pages were rewritten. | "the first session in which Thomas actually read the copy that was already public. The review, his rulings, the correction pass across all four pages" |
| LG4 | 003 · 2026-09-12 | A voice pass, a second résumé rebuild and the contact page. The rewrite before it was confirmed live, byte for byte. | "the voice session …, a second rebuild of the résumé, and the contact page"; "handoff-002's rewrite **verified serving** … matched the repo byte-for-byte" |
| LG5 | 004 · 2026-09-16 | Copy fixes from my own corrections, a third résumé pass, a new home-page lede, and scouting data for a graph demo. | "Copy fixes from Thomas's own corrections, a third résumé pass, the home lede, … and the graph-demo data scouting." Date per Q-LG5 A. |
| LG6 | 005 · 2026-09-16 | I chose where the graph demo goes and that it is 3D; it was built and tested locally. | "Thomas answered the two pending graph questions — **projects page, 3D** — and the demo was built, wired and tested"; "written and verified locally" |
| LG7 | 006 · 2026-09-16 | I annotated the previous handoff and handed it back; every ruling in it was acted on the same day. | "the same day as handoff-005, after Thomas returned it annotated. … This handoff is the state after acting on every one of them." |
| LG8 | 007 · 2026-09-18 | The first real deploy: pushed to GitHub, built by Cloudflare, verified serving. | "the first real deploy"; "the site is **deployed and verified serving**"; §1: "commit + push to `main` in GitHub Desktop → Cloudflare builds" |
| LG9 | 008 · 2026-09-19 | A real favicon, and two new project write-ups: the Back Quarter and the Desk and the Drawer. | "the real favicon, and two new project write-ups — The Back Quarter and The Desk and the Drawer." |
| LG10 | 009 · 2026-09-19 | The previous session's work taken live and verified; two more project write-ups, and the four sites written up as four briefs. | "everything in handoff-008 reaching the live site, plus two new project write-ups and the four-site briefs"; "**deployed and verified live.**"; §2: "The four-site section is four briefs" |
| LG11 | 010 · 2026-09-19 | A short clean-up: small open items closed, and one correction on my personal site. Nothing here changed. | "a short small-items session … Two open items closed, one copy correction made in the sister repo"; "the live site is **unchanged**" |
| LG12 | 011 · 2026-09-20 | Mostly other sites: a crawl audit of the rare-disease site, and two sites moved behind Cloudflare. Here, only the résumé changed. | "Most of it was not this site: … a crawl audit of bareyourrare.org, moving two Hostinger sites behind Cloudflare"; "tc-ventures.ca itself changed in one place — the served résumé PDF" |
| LG13 | 012 · 2026-09-21 | Cleared what could be closed without my input: markup fixes on the rare-disease site, and a keyboard path through the graph. Verified live. | "clearing the items an agent could close without Thomas: …, most of O-11 (bareyourrare.org markup), and the code half of A-1"; "**verified serving** … graph keyboard path" |
| LG14 | 013 · 2026-09-21 | The plan to take this site from skeleton to showcase, written and approved. | "**plan-001**, the plan to take this site from skeleton to showcase"; "The plan is written and approved" |
| LG15 | 014 · 2026-09-21 | The design system and the case-study template, built on one page with placeholder copy. | "the design system (tokens, lanes, components) and the case-study template, built on one page with placeholder copy" |
| LG16 | 015 · 2026-09-22 | An audit and a phased plan. Phase 0 shipped: clean addresses, security headers, and the home page rewritten from my rulings. | "a baseline audit and action plan (Phases 0–4), **Phase 0 shipped**, the home page rewritten from copy-review-002"; §2: "Clean URLs everywhere", "`public/_headers`" |
| LG17 | 016 · 2026-09-24 | The receipts inventory ruled, the truth rules written, and the first case study live: the housing society's site. | "receipts inventory ruled, the twenty truth rules, …: **`/work/gprs` shipped**" |
| LG18 | 017 · 2026-09-24 | This site's own case study live, and a Projects sub-menu on every page. | "**`/work/this-site` shipped**, and a **Projects sub-menu** listing both case studies is on every page" |
| LG19 | 018 · 2026-09-25 | The method page live, with my own headline and lede. | "**`/method` shipped** as its own menu item. It has Thomas's own H1 and lede" |
| LG20 | 019 · 2026-09-25 | I moved the case studies ahead of this ledger. The influence graph's case study live. | "Thomas reordered the plan: the **four remaining case studies come before the build ledger** … **`/work/influence-graph` shipped.**" |
| LG21 | 020 · 2026-09-26 | The rare-disease site's case study live, after a schema fix on that site and a second look at its host fault. | "**`/work/bare-your-rare` shipped** … **O-13 is fixed on bareyourrare.org.** The sitewide schema says `Organization`, not `NGO`. … **The host fault is re-diagnosed.**" |
| LG22 | 021 · 2026-09-27 | Receipts for the last two case studies ruled; their copy drafted, then paused at my word for a decision about the Back Quarter. | "**Step 1 (receipts) is ruled.** … **Step 2 (the copy) is drafted and partly ruled.** Thomas paused it on 2026-09-27, with a decision about the Back Quarter itself (O-20)." |
| LG23 | 022 · 2026-09-27 | The Back Quarter copy ruled, then work on my personal site: the 3D world on computers only, and three layout fixes. | "**BQ1–BQ7 are ruled.** … **O-20 is built and live:** the painted map is retired; the 3D world runs on PCs only." "**Three more theme fixes went live:**" |
| LG24 | 023 · 2026-09-28 | The last two case studies live, after a re-trace against the code found the Desk's description out of date. All six are done. | "The Desk re-trace found live `/projects` describing the old one-menu desk (C-25). Fixed live."; "**Phase 1b is done.** All six case studies are live." |

**LG25 (upkeep, not copy):** from now on, the session that writes a handoff drafts its line here, and the
column appears once you rule it. This session's own handoff (024) gets its line at wrap.

### LGR — R5, the body paragraph under the lede (Q-LG3 A)

> "I also built a research application that maps nearly four thousand official statistical reports and the
> documented dependencies between them. I am looking for remote work running a nonprofit's website and
> digital operations." →
> "I am looking for remote work running a nonprofit's website and digital operations."

### LGP — which open items are drawn dotted (Q-LG1 A), and the reused IDs

Read from each item's own row in handoff-023. **Dotted means** parked on purpose, or waiting on your
decision or your action.

**Solid (8), open work:**
- PL-6, the plan's phases.
- C-15: the private résumé copy is unchecked.
- DESIGN-1, G-7: Phase 3 layout.
- INFRA-13, INFRA-16: rule-5 scripts.
- INFRA-17: the theme harnesses.
- INFRA-10: the LinkedIn check, not confirmed run.

**Dotted (23):**
- **PLAN:** PL-1 (a record), PL-8 (waits for Phase 4).
- **COPY:**
  - C-9, C-17, C-21, C-22: your call.
  - C-13, C-16: records.
  - C-19: left unresolved on purpose.
  - C-20: waits for the rebuild and A-1.
- **PROJECTS:** P-6 (nothing queued), G-6 (your call).
- **A11Y:** A-1 (deferred by you), A-3 (accepted for now).
- **INFRA:**
  - INFRA-4, INFRA-11, INFRA-14, INFRA-15: your call.
  - INFRA-6: waits for a date.
  - INFRA-9: deliberate.
- **DOMAIN:** D-1 (harmless), D-2 (a caution), D-3 (yours, on a date you set).

**Doubt:** INFRA-10 could be yours to run (it's a LinkedIn tool). If so, it's dotted.

**Reused IDs (checked by reading every row):**
- **Same item, wording evolved:** C-15, G-2, INFRA-5, PL-7.
- **Two items:** G-7. The gap between its two runs splits it into two threads.

### Rulings, step 2 (2026-09-29)

Thomas, verbatim: **"LG1–LG24 ok, LGR ok, LGP ok, INFRA-10 dotted"**. Read as:
- LG1 to LG24 OK as drafted. Recorded in `ledger/curation.json` as `"LGn OK 2026-09-29"`.
- LGR OK: R5's first sentence is cut.
- LGP OK, with INFRA-10 moved to dotted. That makes 7 solid and 24 dotted.
- LG25 is procedure, not copy, and wasn't ruled. The next handoff's line comes here at wrap.

**Shipped:** PR #15 (merge `de37b8f`), live and verified 2026-09-29. Curl of `/` and `style.css` is
byte-identical to `main`, and `site_check.py --live` passed 105 of 105.

---

## LG25 — handoff-024's line (drafted 2026-09-29, for Thomas to rule)

| # | Handoff | Line | Rests on |
|---|---|---|---|
| LG25 | 024 · 2026-09-29 | This ledger: I ruled the proposal and every line on it, and a script draws it from the handoffs. | "**LG0, the proposal, ruled "LG0 ok, all A".**"; "**LG1–LG24, LGR and LGP ruled**, and shipped as PR #15." |

It's in `ledger/curation.json` with `"ruled": null`, so the live ledger stops at 023 until this is ruled.

**Ruled 2026-09-29.** Thomas, verbatim: **"LG25 ok"**. Recorded as `"LG25 OK 2026-09-29"`, and column 024
is drawn.

---

## LG26 — handoff-025's line (drafted 2026-09-29, for Thomas to rule)

| # | Handoff | Line | Rests on |
|---|---|---|---|
| LG26 | 025 · 2026-09-29 | A Display panel for motion, theme, contrast and text size, built into the site. I ruled the plan and the panel’s words. | "**P3-0, the Phase 3 proposal, ruled "p3-0 ok, all A".**"; "**Step 3, the Display panel, ruled "dp1-3 ok, merge 21, then wrap"**, and shipped as PR #21." |

It's in `ledger/curation.json` with `"ruled": null`, so the live ledger stops at 024 until this is ruled.

**Ruled 2026-09-29.** Thomas, verbatim, in `handoff-025-decisions.xlsx` row 1 ("A: ok as written"): **"A"**.
Recorded as `"LG26 OK 2026-09-29"`, and column 025 is drawn.

---

## LG27 — handoff-026's line (drafted 2026-09-30, for Thomas to rule)

| # | Handoff | Line | Rests on |
|---|---|---|---|
| LG27 | 026 · 2026-09-30 | A layout pass: the pages now reflow for readers who enlarge the text, and the www address works. I ruled each fix and set up the address myself. | "**"s4-1 A, s4-2 A"**"; "Every width breakpoint is now `em`."; "Thomas added the redirect rule and turned on Always Use HTTPS" |

It's in `ledger/curation.json` with `"ruled": null`, so the live ledger stops at 025 until this is ruled.
