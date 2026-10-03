# Copy review 011 — the second pass: the case studies and the way between pages

**Written:** 2026-10-02
**Why:** PL-6 names Awwwards. Thomas ruled no submission yet (copy-review-010, the cleanup list, item 12):
the hero is the first screen that isn't plain, and the rest of the site is still the template. This is the
proposal for the rest. Started at Thomas's word, "2 go".
**Status:** SP-0 and Q-SP1 to Q-SP5 ruled A, Q-TH3b OK (2026-10-02; see the end). Being built in Q-SP4's order.

Same format and marks as copy-review-001 to 010: `OK` · `KEEP` · `A` / `B` · `FIX` · `CUT`.

---

## SP-0 — the proposal (not copy)

**To rule:** SP-0 as a whole (OK / FIX), plus Q-SP1 to Q-SP5. Any new words (alt text, captions) come
after, as numbered blocks.

### 1. Where it stands (read 2026-10-02, `main` at `22e1abb`)

- **Every case study opens the same way:** the label, the H1, the claim, the spec table, the section index.
  Its first picture sits further down the page, and Bare Your Rare has none. The template is the same six
  times, by design (approved 2026-09-22), and that's what reads as plain.
- **`/projects`** shows pictures for three of its six builds (the graph's app, the Back Quarter, the desk).
  GPRS, Bare Your Rare and this site have none there.
- **Between pages,** M1 is a 0.25 s cross-fade, the top bar sliding, and under Full the clicked sub-menu
  label growing into the next page's H1. It's correct and almost invisible.
- **Weight:** `budget.py` weighs each page scrolled to the end, so it already counts every picture on a
  page. A picture moved up a page adds nothing to its ceiling.

### 2. The pieces

**SP-A: each case study opens on its own picture.**
- Under the H1 and the claim, the case study's own picture, wide (the wide lane, or the full width of the
  window), before the spec table. It's a file already on the page: the graph, the farm, the desk, the GPRS
  home page, this site's home page. No new picture, nothing cropped (`contain`, a standing rule).
- **Bare Your Rare has no picture,** and its site is a patient site (no symptom detail, no family). Q-SP2.
- **Motion, under Full only:** as the reader scrolls, the picture settles from slightly larger to its place,
  and the spec table rises in behind it. CSS scroll-driven animation (`animation-timeline: view()`), no
  script. Reduced and Off: the picture in place, still. Browsers without it: the picture in place.
- `Fig. N` numbering follows the picture. The opener is Fig. 1, and the rest move up one.

**SP-B: the picture carries across the change of page.**
- On `/projects`, a build's picture and its case study's opener picture share a view-transition name.
  Under Full, clicking "Read the case study" grows the picture from its place on `/projects` into the
  opener, while the rest cross-fades. It's the same mechanism as M1's label-to-H1, in `prefs.js`, with no
  library.
- Back from the case study (the browser's Back) reverses it.
- Reduced: the cross-fade only. Off: none. Browsers without view transitions change pages as now.
- **It needs a picture at both ends:** three builds have one on `/projects` today. Q-SP3.

**SP-C: the section heads.**
- The numbered heads ("01 — The ask") grow into a larger editorial mark, the numeral set big in the
  display face beside the heading. Under Full, the rail's section index fills a thin teal bar as the reader
  passes each section. CSS only, with no new words.

**Not in this pass:** Background, Contact and the 404 stay as they are. The home page has its hero.

### 3. What it rests on

- No new library and no new download. The pictures and fonts are already on the site.
- `prefs.js` gains the picture's view-transition name next to M1's. `style.css` gains the opener, the
  heads and the scroll-driven rules, all under the motion tokens (`--move`, `--fade`).
- The Display panel's rules hold: Full, Reduced and Off as above; Contrast More and the text sizes
  unchanged in meaning.

### 4. Checks

- `site_check.py`: each case study's opener picture shows, whole, at 1280 and 375. Under Full the
  transition from `/projects` names the picture on both pages and runs. Under Reduced and Off it doesn't.
  Each check gets a control.
- `budget.py`: every ceiling unchanged, or a measured number for ruling.
- `shots_diff.py` on the pages this pass doesn't touch: identical.
- **Looked at:** a recording of each piece, in both themes, for Thomas to rule before anything ships.

### Questions

**Q-SP1:** how wide the opener picture is.
> **A (recommended):** the wide lane (1040px), the width the case studies' figures already use. It sits
> in the template's own grid, and a screenshot stays sharp.
>
> **B:** the full width of the window. More dramatic, and screenshots taken at 1280 go soft on a wider
> screen.

**Q-SP2:** Bare Your Rare's opener.
> **A (recommended):** its structured-data excerpt, the figure its card already uses, set large as the
> opener. It's on the page already and shows nothing about any patient.
>
> **B:** no picture; it keeps the text opener.

**Q-SP3:** the three builds with no picture on `/projects` (GPRS, Bare Your Rare, this site).
> **A (recommended):** add each one's opener picture to `/projects`, so all six carry across. GPRS and this
> site have screenshots already; Bare Your Rare uses its excerpt (Q-SP2). That adds weight to `/projects`
> (657 of its 720 kB now), so a measured ceiling comes for ruling, and any new alt text comes as blocks.
>
> **B:** the morph for the three that have pictures; the other three change pages as now.

**Q-SP4:** the order.
> **A (recommended):** SP-A, then SP-B (it needs the openers), then SP-C. Each built, recorded for you to
> look at, ruled and shipped before the next.
>
> **B:** all three in one change.

**Q-SP5:** after this pass.
> **A (recommended):** you look at the whole site and decide on the submissions yourself. The agent can
> then prepare what CSSDA, Godly and Awwwards each ask for, proposed before built.
>
> **B:** another pass first (say on what).

### The steps

1. SP-0 ruled.
2. SP-A built on a branch, run locally, recorded; ruled; shipped on your word.
3. SP-B the same.
4. SP-C the same.

---

## SP-A — built, for Thomas to rule (2026-10-02, branch `sp-a-openers`)

**What moved:** each case study's picture moved up, caption and all, to sit under the claim and before the
meta strip. It's the same figure, not a copy, so it's now Fig. 1:
- the graph: the application screenshot;
- the farm: the 3D world;
- the desk: the desk photograph;
- Bare Your Rare: the structured-data excerpt, set large (Q-SP2 A);
- GPRS: the home page;
- this site: the home page.

Where a picture left a pair (GPRS, this site), the other figure now stands alone in the reading lane. The
settle and the rise run under Full and System only (the OS's reduce-motion means still).

**The look:** `Claude outputs/sp-a/`:
- `sp-a-light.webm` and `sp-a-dark.webm`: each page under Full, 1280 wide;
- phone stills at 375, and Reduced stills at 1280, in both themes.

**Two moves make shipped words untrue, so each comes with its fix:**

| # | Where | Now | Proposed |
|---|---|---|---|
| SPA1 | `/work/bare-your-rare`, the excerpt's caption | "…trimmed to the fields named above. …" | "…trimmed to the fields named below. …" (the fields are named in "The standard", now under it) |
| SPA2 | `/work/this-site`, the alt text of the GPRS case-study screenshot (retaken 2026-10-02: the old one showed the meta table where the opener now sits) | "The GPRS case study: the heading A housing society's website, a one-line summary, a table of stack, status and hosting, and a side index of the six sections." | "The GPRS case study: the heading A housing society's website, a one-line summary, and the society's home page as its first picture, with a side index of the six sections." |

**Q-SPA:** the look OK / FIX (say what), and SPA1 and SPA2 OK / FIX.

**Ruled 2026-10-02.** Thomas, verbatim: **"1-3 yes, merge 59"**, where 1 was the look, 2 SPA1, 3 SPA2. Read as:
the look OK, SPA1 OK, SPA2 OK; and merge #59 (merged by the agent at his word).

---

## SP-B — built, for Thomas to rule (2026-10-02, branch `sp-b-carry`)

**What it does:** under Full, the picture carries across the change of page:
- from `/projects` into the case study's opener, by any link to it;
- and back again with the browser's Back.

`prefs.js` names the two `cs-pic`, only when the picture is on screen, and reads the other page from the
Navigation API. Under Reduced the page only cross-fades, and Off skips the transition, as M1 does.

**`/projects` gains three pictures** (Q-SP3 A), each after its build's paragraph in "And four live sites":
- Bare Your Rare's excerpt;
- the GPRS home page;
- this site's home page.

Each picture's alt text is the case study's own ruled alt text, word for word, and the excerpt's code is
copied as is.

**The look:** `Claude outputs/sp-b/`:
- `sp-b-light.webm` and `sp-b-dark.webm`: all six, from `/projects` and back, under Full, 1280 wide;
- stills of the new section at 1280 and 375, in both themes.

**Checks, local:**
- A probe of each page change, under Full, Reduced and Off, at 1280 and 375. Every case passes, and both
  controls carry nothing: `/projects` → `/method`, and one case study to another.
- `site_check.py` 235 of 235.
- `shots_diff.py` against `main`: only `/projects` differs (44 of 48 pairs identical).
- `budget.py` 46 of 48: the two ceilings below.

**New captions, for ruling:**

| # | Where | Proposed |
|---|---|---|
| SPB1 | `/projects`, under Bare Your Rare's excerpt | "Part of the structured data `/hcs-guide/` serves, verbatim, trimmed. “…” marks what was left out." (the case study's caption without its "to the fields named below") |
| SPB2 | `/projects`, under the GPRS picture | "The society’s home page." |
| SPB3 | `/projects`, under this site's picture | "This site’s home page." |

**Two ceilings, for ruling** (Q-P4-8 A: the measured weight plus 10%, rounded up to the next 10 kB):

| # | Page | Now | Measured | Proposed | Why |
|---|---|---|---|---|---|
| SPB-C1 | `/projects` | 720 kB | 829 kB | **920 kB** | the three pictures (Q-SP3 A said a ceiling would come) |
| SPB-C2 | `/work/this-site` | 400 kB | just over 400 kB | **450 kB** | `prefs.js` is about 1.5 kB larger on every page; this page sat at 398 of 400 |

**Q-SPB:** the look OK / FIX, SPB1 to SPB3 OK / FIX, SPB-C1 and SPB-C2 OK.

**Ruled 2026-10-02.** Thomas, verbatim: **"1-4 yes, go ahead and increase the ceilings by 25% instead of ~10%"**,
where 1 was the look, 2 SPB1 to SPB3, 3 SPB-C1, 4 SPB-C2. Read as: the look OK, SPB1 to SPB3 OK, and the two
ceilings set by the measured weight plus 25% (not 10%), rounded up to the next 10 kB: `/projects` **1,040 kB**
(829 × 1.25 = 1,036), `/work/this-site` **510 kB** (just over 400 × 1.25 = just over 500). Read as for these
two only; Q-P4-8's 10% stays the rule for the others.

---

## Also for ruling: PW3 after the hero (copy-review-010, cleanup item 4)

`budget.py --live`, 2026-10-02, after #54 (`22e1abb`): every page's own files are **203 kB to 601 kB on
the wire**. `/projects` is still the heaviest (601 kB); home is 434 kB (1,197 kB decoded, under its
1,320 kB ceiling). 48 of 48.

So PW3's measurement still holds with the hero live, and TH3's "before the home page's 3D ledger" isn't
needed.

| # | Now | Proposed |
|---|---|---|
| TH3b | "Measured on 2 October 2026, before the home page’s 3D ledger, each page’s own files download in between about 200 kB and 600 kB, …" | "Measured on 2 October 2026, each page’s own files download in between about 200 kB and 600 kB, …" (PW3 as ruled in copy-review-009, unchanged). |

**Q-TH3b:** OK / KEEP (keep TH3's words).

---

## Rulings

**2026-10-02.** Thomas, verbatim: **"1-10 yes"**, to a numbered list where 1 was SP-0, 2 to 6 were Q-SP1 to
Q-SP5 (each "A, yes" recommended), and 7 was Q-TH3b (take the words out). Read as: **SP-0 OK; Q-SP1 A,
Q-SP2 A, Q-SP3 A, Q-SP4 A, Q-SP5 A; TH3b OK.** (8 to 10 were LG35 and its parked changes, recorded in
copy-review-006.)

- TH3b shipped with ledger column 034, the first PR after the ruling.
- Next: SP-A, the case-study openers, on its own branch from `main`.
