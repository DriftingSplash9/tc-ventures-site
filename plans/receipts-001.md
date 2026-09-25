# receipts-001 — the receipts inventory (PL-2)

**Written:** 2026-09-23 · **Status:** ruled by Thomas 2026-09-23 (via receipts-001.xlsx): 36 OK, 76 CUT; every private (P) row CUT. **R-014 un-cut 2026-09-25: now 37 OK, 75 CUT** · **Feeds:**
`/work/gprs`, `/work/this-site`, `/method`

Every row is a real, documented case of an AI getting something wrong on one of Thomas's
projects, how it was caught, and the rule it became. Nothing here is inferred or invented:
each row points at the file (and line or section) where the miss is recorded. A row with no
receipt did not make the table.

**This repo is public.** So this file is curated: nothing familial, no health detail beyond
the named condition, nothing quoted from private files. Private stories are listed in §4 by
label only.

---

## 0. How to rule

Mark each row in the **Ruling** column, copy-review style:

- **OK** — true, public-safe, usable in a case study or on `/method`.
- **CUT** — leave it out (for any reason; no reason needed).
- **FIX** — usable, but the wording or the facts need changing. Say what.

`✓` in the **chk** column means the coordinator opened the receipt and read the passage
this session. Unticked rows were read by one of the source readers (see §7) but not
re-opened by the coordinator; tick them before they are quoted.

Nothing in this file is site copy. Anything that ships goes through copy-review-003.

**Kinds** (the `kind` column): `unmeasured` = looked right but was not measured ·
`invented` = plausible but invented fact · `drift` = drift across sessions ·
`selling` = over-polish / selling · `absence` = incomplete read asserted as absence ·
`privacy` = privacy leak · `tooling` = tooling error.

**Caught by** (the `caught` column): measurement · validator · read-through · live check ·
Thomas.

---

## 1. What was read, and what it found

About 450 process documents across six projects, read in full by 20 parallel readers:
this site's handoffs 001–015, reviews and git history; thomascheesman.ca's V0.01–V0.42 and
git history; Reports Clustering's current docs, 150+ archived handoffs, five regional
branches (EU, AF, AU, CA, NZ), notes, planning, playbooks and research briefs; the earlier
research bundles; BareYourRare's audits, handoff and git history; GPRS's handoff, repo,
March audits; the cross-site diary. **About 700 raw misses** came back. This file keeps the
**112 that are distinct, receipted and useful**, and merges repeats into one row with the
earliest receipt.

**What the pile says, in one paragraph.** The single biggest class is `unmeasured`: work
declared done, verified, clean or live that was not — sliders that did nothing, audits that
passed while visitors saw a Coming Soon page, a validator that exited 0 while printing
failures. Second is `absence`: "not there", "blocked", "no document" asserted from a
partial read — a truncated fetch, one layer of a two-layer site, one network out of three.
Third is `invented`, and it is concentrated in two places: outside research models (made-up
quotes, URLs, figures, whole reports for dead links) and AI summarising fetchers. The rules
that came out of all three are the same few, restated per project: **measure the thing, not
a proxy for it; say what you read, not what exists; a quote is verbatim or it is empty.**

---

## 2. Findings that need a decision before anything ships

| # | Finding | Why it matters | Recommendation |
|---|---|---|---|
| F-1 | **The live home page overstates its own receipt.** `public/index.html:167-169` says a layout force "I had already shipped turned out to have been calibrated against a measurement script with a bug in it." The receipt (`Reports Clustering/archive/Previous Handoffs/HANDOFF-2026-08-28-pre-trim-032.md` L256–263) says that 1/d² calibration was **"a real false start, caught before shipping."** What *did* ship was a different miss: a sweep baseline that never reproduced, used to raise the slider ceiling 3→10→15 (`scripts/measure-forces.ts` header L7–11; `archive/audits/audit-2026-08-31-second-independent.md` F-10). No code bug is recorded for that one. | The page making the "I measure, I don't trust" claim is itself un-measured on this point. A reader who asks for the receipt gets a mismatch. | **RULED 2026-09-23: match R-061.** The sentence is rewritten to the R-061 story (caught before shipping) in copy-review-003. Wording ruled OK in copy-review-003 R1 and applied to `public/index.html` on 2026-09-23. |
| F-2 | Rows involving the outside research model name it in the receipts. On 2026-09-07 Thomas ruled that Reports Clustering docs drop its name "as if it never existed." | Public case studies would contradict that ruling if they name it. | **RULED 2026-09-23: don't name it.** Case studies, `/method` and all site copy say "an outside research model" or similar. (File names in the receipt paths still contain the name; they are paths into a private repo and are never published.) |
| F-3 | Several of the strongest Reports Clustering stories rest on exact counts (edges refused, share graded A). | Standing rule: no exact counts in copy. | Rows marked **[count]** can be used only in rounded or descriptive form ("about half", "most"). |
| F-4 | GPRS has thin coverage: the GPRS repo and handoff record few AI misses that are both public-safe and not about the Margaret Edgson Manor rebuild. | `/work/gprs` needs 2–3 real misses. | **Thomas, 2026-09-23:** GPRS was built before he used Claude Code or Cowork; there were no handoffs, so there is no session record to mine. R-001–R-003 (the March 2026 audits) are the pre-method record; R-006–R-008 are from after. |

---

## 3. The inventory

### 3A. GPRS — gpresidentialsociety.com (`/work/gprs`)

| ID | date | what the AI got wrong | kind | caught | rule it became | receipt | public-safe? | chk | Ruling |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | 2026-03-24 | Another AI's site audit scored the site 58/100 describing a site that no longer existed (no hero, no calls to action, no donate button) | invented | read-through (second audit compared it with the code) | Audit prompts say "read and reference the actual code, do not guess" | `Website Projects/Shared & Misc/AUDIT-NOTES.md` §"Preamble: GPT vs Grok Audit Comparison" L111–113 | Y | ✓ | OK |
| R-002 | 2026-03-25 | Donate-page copy from an earlier AI tool showed the society's address as link text but the `mailto:` went to an unrelated organisation, with an AI-tool referrer tag | invented | read-through (audit) | Replace AI-generated copy with human-written copy | `Website Projects/GPRS Website/gprs-audit-report-march-2026.md` L183; `gprs-theme-fixes-2026-03-25/CHANGES.md` L75 | Y (omit the other org's address) | ✓ | CUT |
| R-003 | 2026-03-24/25 | An audit scored the site 87/100 on 24 March; the next day's audit found a /volunteer/ 404, an inconsistent /apply/ header and broken Donate links | absence | read-through | "Next audit should verify all high-impact items" | `gprs-audit-report-march-2026.md` L5, L580, L612 | **unverified:** the file does not say those faults existed on the 24th | ✓ | CUT |
| R-004 | 2026-09-11 | First copy described a non-executive board seat as "Own the public website" | selling | Thomas (copy review) | Entry rewritten in his words | `reviews/copy-review-001.md` B11 L371–377; `handoff-002.md` §2 L76–77 | Y | | CUT |
| R-005 | 2026-09-11 | Copy stated a unit count as current when it was the pre-fire figure | invented | Thomas | Stated as the pre-fire count; final count not settled | `copy-review-001.md` H8 L101–102; `handoff-002.md` §2 L74–75 | Y | | CUT |
| R-006 | 2026-08-27 | HEIC photo conversion dropped the Display P3 colour profile, so every photo came out oversaturated | tooling | other: visual check | Convert P3→sRGB explicitly | `Claude-Diary/diary.csv` row 2026-08-27 "P3 colour bug caught" | Y | | CUT |
| R-007 | 2026-09-18 | Told Thomas three times that pushes were safe because GPRS "had no CI, manual deploy"; pushes went live in minutes, and a manual-deploy procedure that doesn't exist was committed | drift | Thomas, then live check (curl) | "A push IS a publish"; "a claim repeated in three notes is still one claim" | `diary.csv` row 2026-09-18 "CORRECTION… GPRS AUTO-DEPLOYS" (line 94); GPRS repo `AGENTS.md` "Deploying"; commits `953907a` → `5a68be4` | Y (describe the miss, not what was published) | ✓ | OK |
| R-008 | 2026-09-18 | Read WordPress.com domain receipts as proof of where the site is hosted | absence | Thomas | WordPress.com receipts = domain, not hosting | `diary.csv` row 2026-09-18 CORRECTION | Y | | CUT |

### 3B. This site — tc-ventures.ca (`/work/this-site`)

| ID | date | what the AI got wrong | kind | caught | rule it became | receipt | public-safe? | chk | Ruling |
|---|---|---|---|---|---|---|---|---|---|
| R-010 | 2026-09-11 | First copy said "in about eighteen months", contradicting the 2023 dates elsewhere on the site | invented | read-through (FLAG X1), Thomas | "Do not invent dates or figures" | `reviews/copy-review-001.md` H3 L53–59, X1; `handoff-002.md` §3 | Y | ✓ | CUT |
| R-011 | 2026-09-11 | Published exact corpus counts that disagreed with the bundle a visitor could reach, and would go stale within weeks | drift | read-through (X3), Thomas | Never publish an exact node/edge/report/grade count | `copy-review-001.md` X3 L503–512, P9 | Y | ✓ | OK |
| R-012 | 2026-09-11 | Used a line count as a proof point | selling | Thomas | No vanity metrics | `copy-review-001.md` H6 L78–81 | Y | | CUT |
| R-013 | 2026-09-11 | "Available now" five times — a claim that goes stale, published without sign-off | selling | Thomas → "open to work" | (The template's example miss/catch pair) | `copy-review-001.md` H12 L135–140 | Y | | CUT |
| R-014 | 2026-09-12 | Contact page promised a reply "within a working day" — a commitment only Thomas could make | selling | read-through (self-flagged), Thomas | Commitments in his name are his to set | `handoff-003.md` CT-4; commits `be77991` → `fe69dd7` | Y | ✓ | OK (un-cut by Thomas 2026-09-25) |
| R-015 | 2026-09-12 | Résumé labelled The Keg "corporate"; it was a franchise | invented | Thomas | — | commit `fff6a64` → `ffaddab`; `handoff-004.md` §2 L65–66 | Y | | CUT |
| R-016 | 2026-09-12 | A commit tool reported success but wrote a stale résumé to disk | tooling | measurement (byte count) | Check byte counts on disk after any commit | `handoff-002.md` traps L116–119 | Y | | CUT |
| R-017 | 2026-09-12 | Reordering résumé entries silently pushed it to three pages | unmeasured | measurement (page count) | Exactly two pages; measure after every change | `handoff-002.md` traps L120–122 | Y | | CUT |
| R-018 | 2026-09-12 | An md5 "match" between live and repo hashed the empty body of a 307 redirect | tooling | measurement | `curl -L` | `handoff-003.md` §2 L51–52 | Y | | CUT |
| R-019 | 2026-09-16 | `[hidden]` was overridden by `display` rules, so the graph button showed with JS off and an empty canvas showed before the click | unmeasured | measurement (headless JS-off / pre-click) | Content renders without JS; nothing heavy before a click | `handoff-005.md` §2 L96–102 | Y | ✓ | OK |
| R-020 | 2026-09-16 | The graph bundle fetched its data root-absolute; a plain rebuild would have shipped a broken graph under the theme path | unmeasured | read-through before rebuild; live check | Fixed to `BASE_URL`; trap written into `functions.php` | `handoff-006.md` traps L145–151; `handoff-008.md` §2 | Y | | CUT |
| R-021 | 2026-09-16→19 | Several handoffs asserted the tooling could not delete files in a mounted folder; it could | absence | a later session | Convention retired | `handoff-010.md` traps L75–79 (corrects 006–009) | Y | | CUT |
| R-022 | 2026-09-19 | Said BareYourRare had "three or four" condition guides; it has five | invented | live check (counted off the nav) | Count from the live site, not memory | `handoff-008.md` §2 L116–119 | Y | ✓ | OK |
| R-023 | 2026-09-19 | Placeholder favicon set "TC" as text in a font most machines don't have | unmeasured | read-through | Favicon drawn as paths | `handoff-008.md` §2 L89–91 | Y | | CUT |
| R-024 | 2026-09-21 | The graph's load button hid itself and dropped keyboard focus to `<body>`; the automated accessibility checker found nothing | unmeasured | Thomas, testing it (confirmed by him 2026-09-24, copy-review-003 T7) | Focus moves to the stage | `handoff-012.md` §2 L54–63 | Y | ✓ | OK |
| R-025 | 2026-09-21 | A bare `.shot figcaption::before` leaked case-study styling onto the Projects page | unmeasured | measurement (pixel regression) | Case-study CSS scoped under `.cs-body` | `handoff-014.md` traps L98–99 | Y | | CUT |
| R-026 | 2026-09-21 | brief-001, public and linked as a receipt, carried a private project, exact counts and a symptom detail | privacy | read-through (redaction) | Every receipt is read against the privacy rules before it links | `handoff-014.md` traps L100–102; `handoff-015.md` §2 | needs OK (describe without the detail) | | CUT |
| R-027 | 2026-09-22 | Nav, canonicals and sitemap pointed at `.html` URLs that 307 — known since handoff-003, fixed a week later | drift | site audit | Clean URLs everywhere | `handoff-003.md` §2 L51–52; `handoff-015.md` §2 | Y | ✓ | OK |
| R-028 | 2026-09-22 | The CSP passed locally and blocked Cloudflare's edge-injected analytics beacon live, for one deploy | unmeasured | live check (console) | After any CSP change, load the live site and read the console | `handoff-015.md` traps L108–110 | Y | ✓ | OK |
| R-029 | 2026-09-22 | Told Thomas his LinkedIn had no About section; the page was lazy-loaded and never scrolled | absence | Thomas | Say "I could not see X", never "X is missing" | `handoff-015.md` §0 L32–34, traps L117–120 | Y | ✓ | OK |
| R-030 | 2026-09-22 | A handoff said the template had three confirmation brackets; it had four | invented | validator (assertion in the edit script) | Grep, don't count from memory | `handoff-015.md` traps L126 | Y | ✓ | CUT |
| R-031 | 2026-09-22 | Scripted edits through Git Bash turned `\r` in Windows paths into a carriage return, twice | tooling | measurement (grep of the result) | Build paths with `chr(92)` or a script file; grep the result | `handoff-015.md` traps L121–123 | Y | ✓ | CUT |
| R-032 | 2026-09-23 | The served résumé PDF was two days stale; the handoff said it was "not yet exported" when Thomas had already exported it | absence | Thomas ("I am positive I have the correct one") | Check the file's own timestamp and text before saying it does not exist | this session: `Family & Personal/resume/Thomas-Cheesman-Resume-source.pdf` (06:56, 2026-09-23) vs `public/assets/Thomas-Cheesman-Resume.pdf` | Y | ✓ | CUT |
| R-033 | 2026-09-23 | The home page's own "measurement script with a bug" line does not match its receipt | selling | read-through (this inventory) | — (see F-1) | `public/index.html:167-169` vs `HANDOFF-…-032.md` L256–263 | Y | ✓ | CUT |

### 3C. Reports Clustering — the influence graph (`/method`, and `/work/this-site` where it overlaps)

Paths are relative to `C:\Users\thoma\Desktop\My Files\Reports Clustering\` (private repo;
no public URLs). `PH/` = `archive/Previous Handoffs/`. `TT/` = the earliest research bundle,
`Research/Grok Handoff Bundles/THREE-TIER-COMPLETE-V0.14-2026-08-01/` (outside that repo).

**Measurement and verification**

| ID | date | what the AI got wrong | kind | caught | rule it became | receipt | public-safe? | chk | Ruling |
|---|---|---|---|---|---|---|---|---|---|
| R-040 | 2026-07-28 | Spent two rounds tuning the colours of scene objects that were never mounted | unmeasured | Thomas | "When a toggle has no visible effect, check whether the thing is mounted" | `TT/…/early-version-notes/V0.2.md` L131–143; `…/context-history/V1.5.md` §"The room that was never mounted" L205 | Y | ✓ | CUT |
| R-041 | 2026-07-29 | Four features logged as working had never worked: arrows buried inside spheres, a glow threshold no node crossed, haze frozen at load, a mis-set country field | unmeasured | live check (a checkbox became a slider) | "An attribute nothing reads is an attribute nobody checks; a boolean toggle disguises a broken feature as a taste" | `TT/…/V0.7.md` L23–64; `…/V2.10.md` L226–240 | Y | | CUT |
| R-042 | 2026-07-28→29 | Three sessions shipped visuals marked "not verified"; tuning chosen at 33 nodes had expired by 121 | unmeasured | live check | "Build output cannot make a visual judgement"; legibility check after every tier | `TT/…/V0.5.md` L193–239 | Y | | CUT |
| R-043 | 2026-07-29 | The palette was called "the single biggest legibility win"; the shades inside one country family could not be told apart on a real screen | selling | Thomas (real display) | Families span 2–3 hues; palette constraints in code | `TT/…/V0.12.md` L91–132 | Y | | CUT |
| R-044 | 2026-08-07 | The validator printed ✗ invariant failures but still exited 0 — "the permanently-red validator" | tooling | read-through | ✗ now fails the exit code | `archive/notes/REORG-2026-08-07.md` L46–49 | Y | ✓ | CUT |
| R-045 | ≤2026-08-07 | A validator check reduced algebraically to a constant: a tautology that could never fail | tooling | code review | Replaced with a behavioural check | `archive/planning/MISSION-TODO.md` P3-13 L176–178; `archive/code-review-2026-08-12/CODE-REVIEW-2026-08-12.md` §1 | Y | ✓ | OK |
| R-046 | 2026-08-09 | An edge defined three times silently discarded two of its three statutory citations; the validator printed it and passed | tooling | validator line nobody failed on | SUPERSEDED now fails the run | `archive/EU/G.73.md` F5 L69–77; `G.74.md` F4 | Y | | CUT |
| R-047 | 2026-08-09 | A defect was reported as one record and "validate-catchable"; it was many records with no rule; a red run was then called "clean" | absence | validator (full output read end to end) | Read the whole validator output | `archive/EU/G.73.md` L11, F1 L33–41; `R2.72.md` L57 | Y **[count]** | | CUT |
| R-048 | 2026-08-12 | Earlier test harnesses' hand-rolled screen projection was wrong, so two broken runs looked like passes | tooling | measurement | Use the library's own `.project(camera)` | `PH/handoffs/HANDOFF-2026-08-12-autofit.md` §3 "Testing trap" L105–111 | Y | | CUT |
| R-049 | 2026-08-12 | Blank tiers were blamed on the camera fit; the cause was the far clipping plane, with the test suite green throughout | unmeasured | Thomas, then measurement | Measure the fit's correctness, not its outcome | same file, Addendum L126–166 | Y | | OK |
| R-050 | 2026-08-20→28 | Three slider-driven forces shipped inert. Each force measured correctly in a script; none of the sliders did anything in the app | unmeasured | Thomas ("I don't see any effect") | Verify by dragging the slider, not by measuring the force in a script | `PH/HANDOFF-2026-08-28-pre-trim-032.md` L225–243 | Y | ✓ | OK |
| R-051 | 2026-08-25→09-01 | A render fix was declared "correct by construction" and never confirmed; the symptom returned and two more causes were found | unmeasured | live check in Thomas's browser | — | `PH/…-030.md` L470–477; `…-035.md` §3 L93–107 | Y | | CUT |
| R-052 | 2026-09-03 | For weeks the evidence grader could not read its own quote field (it was run through the wrong extractor), so good quotes graded as unquoted — including the figure behind a grading recommendation | tooling | measurement (re-grade) | "`evidence_quote` IS the span" | `archive/notes/grader-quote-backfill-2026-09-03.md` §2 L43–65 | Y **[count]** | ✓ | CUT |
| R-053 | 2026-09-03 | A curl status separator was written as a literal backslash-n; every status parsed as NaN and a whole fetch strategy cached "nothing found" for every URL, silently | tooling | not stated | Split in a pure helper with a self-test | `archive/playbook/PLAYBOOK-2026-09-04-1938-pre-split.md` §6 L639–648 | Y | | CUT |
| R-054 | 2026-09-04 | Frame-rate readings of 8.6 / 28 / 3.6 fps all had the same median, because the window was hidden behind DevTools | tooling | measurement | Sample inside the render loop; log visibility | same file §6 L753–765 | Y | | CUT |
| R-055 | 2026-09-04 | A draw-call census counted two frames as one and doubled the figure | tooling | measurement (reproduced to within 0.04%) | Corrected recipe | `PH/…-050.md` §3 L146–156 | Y **[count]** | | CUT |
| R-056 | 2026-09-04 | A page capture retyped by hand came back shorter than the original, so its checksum matched nothing reproducible | tooling | measurement (character count) | Checksummed transport; never retype | `PLAYBOOK-2026-09-04-1938-pre-split.md` §6 L850–860 | Y | | CUT |
| R-057 | 2026-09-05 | The grader's name-match bar read presence, not meaning: a quote saying a classification is "not in conformity with" a standard could grade A | tooling | read-through | Negated-quote guard; "the A bar reads presence, not meaning" | `PH/…-061.md` §2 L52–55; `Claude outputs/dsbb-som-source-review-2026-09-05.md` §B | Y | | CUT |
| R-058 | 2026-09-07 | Hand grades on a block ran above the grader's verdict | unmeasured | validator | "Every grade is the grader's" | `PH/…-075.md` §2 L96–100 | Y **[count]** | | CUT |
| R-059 | 2026-09-09 | A sample predicted about three times the real yield of a source; the full sweep measured it | unmeasured | measurement | Sweep before sampling when the corpus is small | `PH/…-080.md` §3 L262–269 | Y **[count]** | | OK |
| R-060 | 2026-09-06→11 | Four handoffs in a row named the wrong section as the place to cut a bloated doc; measurement showed the indexes were most of the file ("the diagnosis was wrong every time") | unmeasured | measurement | "An index line is one line" | `PH/…-085.md` §1 L87–96 | Y | | CUT |
| R-061 | 2026-08-27 | **The measurement-script bug.** The first cluster-repulsion force was calibrated against a throwaway script that let simulation state leak between sweep runs, making a negligible effect look real. Caught **before shipping** by a clean re-run from fresh starts | tooling | measurement | "Measure before believing": committed harness, fresh state per run, more than one seed | `PH/HANDOFF-2026-08-28-pre-trim-032.md` L256–263; `scripts/measure-forces.ts` header L28–33; `archive/playbook/…pre-split.md` §2 rule 8 L67–73 | Y | ✓ | OK |
| R-062 | 2026-08-28→31 | A sweep baseline that never reproduced was used to raise the shipped slider ceiling twice; the committed harness could not reproduce it | unmeasured | measurement (committed harness; independent audit) | Same rule | `scripts/measure-forces.ts` header L7–11; `archive/audits/audit-2026-08-31-second-independent.md` F-10 L93–97 | Y | ✓ | OK |
| R-063 | 2026-08-19 | A "Cluster spread" slider scaled a force and two lengths by one factor, so it nearly cancelled itself; Thomas was running it at 375% | unmeasured | Thomas, then measurement | Split the control | `archive/planning/phase-4-brief.md` §3.1 L187–205 | Y | | CUT |

**Reading, sources and quotes**

| ID | date | what the AI got wrong | kind | caught | rule it became | receipt | public-safe? | chk | Ruling |
|---|---|---|---|---|---|---|---|---|---|
| R-070 | 2026-07-29 | An outside research model marked an edge DOCUMENTED on an agency-only line; the phrase it relied on is not in the document | invented | measurement (full-text search) | "You extract, I adjudicate": the second reader quotes, the project decides | `archive/research-input/Grok-Research-Brief-II.pdf` §0; `archive/notes/SESSION-NOTES-unlogged.md` L219–235 | Y (see F-2) | ✓ | OK |
| R-071 | 2026-07-29 | The same model noticed its quote ran the opposite direction, wrote that down, and kept the edge anyway | invented | read-through | "Never override your own doubt silently"; report conflicts, don't resolve them | `SESSION-NOTES-unlogged.md` L244–249; `Grok-Research-Brief-IV.md` L57–68 | Y (F-2) | ✓ | OK |
| R-072 | 2026-07-29→30 | Three of one session's four recommendations rested on something false, including a quote cited to the wrong place (the second reader had it right) | invented | read-through | "A recommendation written from a summary is a hypothesis about a document" | `TT/…/V0.10.md` L31–59, L127–176 | Y | ✓ | OK |
| R-073 | 2026-07-29 | Nearly declared a phrase absent after grepping a fetch that held a quarter of the document | absence | caught before asserting | "Whole-file greps on a truncated fetch prove nothing about absence" | `TT/…/V2.10.md` L284–293 | Y | | CUT |
| R-074 | 2026-07-30 | A cost used to block a node for two sessions had the wrong sign when measured | invented | measurement | "A stated cost is a hypothesis about a number" | `TT/…/V0.11.md` L30–76 | Y | | CUT |
| R-075 | 2026-08-06 | A research sub-agent working through an AI-summarising reader reported a footnote with an exact title and date. The footnote does not exist; it was assembled from true parts | invented | read-through (byte-for-byte extraction) | Direct extraction for any quoted basis; true parts don't prove the quote | `archive/AU/G.1.md` L116–128; `AU/G.3.md` L189–203 | Y | ✓ | OK |
| R-076 | 2026-08-06 | A session recommended an edge as verified from a correctly quoted sentence whose subject was a different body | invented | read-through | "Read the sentence as well as fetching it" | `archive/NZ/G.3.md` L131–164, L539 | Y | ✓ | OK |
| R-077 | 2026-08-06 | An outside research round returned a quote that appears in neither of the two documents it named | invented | measurement (full-text grep) | "The quote field contains a verbatim passage or it contains an empty string. Never anything else." | `archive/NZ/G.2.md` L69–83; `archive/research-input/Grok-Research-Brief-X.md` L22–49 | Y (F-2) | | CUT |
| R-078 | undated | A quote tidied a PDF's broken "A sian" into "Asian"; proving the quote existed took Thomas twenty minutes | selling | Thomas | "Quote ugly" — and later "do not tidy, and do not decorate" | `archive/research-input/Grok-Research-Brief-VII.md` L50–54; `Brief-XI.md` L36–39 | Y | ✓ | CUT |
| R-079 | 2026-08-05→32 | A finding from a secondary report ("agency only, no named release") was raised to a headline result; the primary text names both releases | absence | live check (primary read) | A secondary-sourced finding stays open until the primary is read | `archive/EU/G.22.md` F1 L184–188; `G.32.md` L104–128, Corrections #1 | Y | | CUT |
| R-080 | 2026-08-05→31 | For about ten sessions a legal database was recorded as "anti-bot gated to every client here"; a real browser loaded it on the first try | absence | live check | Re-test a block before repeating it | `archive/EU/G.22.md` L57–63; `G.31.md` L53–63, F3 | Y | ✓ | OK |
| R-081 | 2026-08-10→13 | Sessions wrote research briefs with false premises (an election assumed held, an authority that doesn't exist); the dispatched agents caught them | invented | the dispatched agents | "A research brief's premise is itself a hypothesis" | `archive/AF/G.17.md` §3 L27; `G.18.md` L47, L67; `G.19.md` L43, L66 | Y | | CUT |
| R-082 | 2026-08-10 | Three sessions wrote a country off as unsourceable without testing it; the next found a working, IMF-corroborated series | absence | live check | Test a stated reason for exclusion before repeating it | `archive/AF/G.10.md` L20–54 | Y | | OK |
| R-083 | 2026-08-13 | An AI fetch tool fabricated a complete Auditor-General report — date, spelling, figures, section — for a URL that returned 404 | invented | measurement (raw HTTP status with curl) | Raw-verify that a URL returns success before trusting any summarised quote | `archive/AF/G.24.md` L41; `G.22.md` §4 L35 | Y | ✓ | CUT |
| R-084 | 2026-08-13 | A post-compaction summary claimed two reports contained real figures; re-fetching showed they didn't | invented | live check (re-fetch) | Re-verify after compaction; save agent output to a file immediately | `archive/AF/G.20.md` L15, L37, L47 | Y | | CUT |
| R-085 | 2026-08-09 | A compaction summary lost the only (screenshot) verification of a result; proceeding on it would have been a miss | absence | read-through (images recovered from the transcript) | "Treat a compaction summary as a lead, not a fact" | `archive/EU/G.68.md` L19; `R1.68.md` L164–177 | Y | | OK |
| R-086 | 2026-08-09 | A fetch tool truncated a quote and filled the gap with its own reconstruction | tooling | live check (re-fetch from the official host) | Direct download and local extraction before judging a document | `archive/EU/G.64.md` F2 L56; `G.65.md` F4 L47 | Y | | CUT |
| R-087 | 2026-08-09 | The PDF viewer silently kept showing the previous country's document, with no error | tooling | live re-check | Navigate directly to each document's URL | `archive/EU/G.65.md` L13; `G.68.md` L12–13, L43–45 | Y | | CUT |
| R-088 | 2026-09-06 | For four rounds every grep missed table numbers because the PDF uses a non-breaking hyphen (U+2011) | tooling | read-through (Chrome read) | Search the whole hyphen class; "never retype a span you can copy" | `PH/…-071.md` §3 L131–137; `…-076.md` L398–405 | Y | | CUT |
| R-089 | 2026-09-07 | Two rounds worked from a note about a table instead of the table; the note hid the two best rows | absence | read-through | "Read the source table, not the note about it" | `PH/…-076.md` §2 L244–253 | Y | | OK |
| R-090 | 2026-09-09→10 | A source was recorded as "read and empty, do not re-fetch" when only one of its two layers had been opened; the claim was carried for four rounds | absence | read-through (two-layer sweep) | "A refusal is a statement about the documents you READ" | `PH/…-083.md` L27–30, L146–153, L177 | Y | ✓ | CUT |
| R-091 | 2026-09-03 | Months of "site is walled" verdicts were really "this sandbox can't reach it"; another machine read what the sandbox couldn't | absence | measurement (same URLs from two networks) | Say which network you were on; re-test from the other | `archive/playbook/…pre-split.md` §6 L466–480 | Y | | OK |
| R-092 | 2026-08-31→09-02 | Two independent audits found that about one bulk-imported edge in five cited a homepage or nothing, and in a random sample only about half the edges fully held | invented | independent audit | Evidence grades; assertion-only edges go to `_dropped`; "an index page is a bare homepage with a path" | `START-HERE.md` L182–197; `Claude outputs/AUDIT-2026-09-02-independent-technical-audit.md` §0, §A2 | Y **[count]** (F-2) | | CUT |
| R-093 | undated | An outside model reported confident figures (a capacity target, a peak asset value) that primary sources put lower | invented | live check | Exact figures from the source, or describe qualitatively | `archive/planning/GROK-PIPELINE.md` §2e L128–130 | Y (F-2) | | OK |

**Process and handoffs**

| ID | date | what the AI got wrong | kind | caught | rule it became | receipt | public-safe? | chk | Ruling |
|---|---|---|---|---|---|---|---|---|---|
| R-100 | 2026-07-28 | Five research agents were told to write one file at the end; a session limit killed all five and the work was lost | tooling | the session limit | Write as you go; one file per agent | `TT/…/V0.2.md` L159–169; `archive/EU/extraction/Research.1-superseded_2026-08-05.md` L368 | Y | | OK |
| R-101 | 2026-07-28 | The flagship example was presented as one directed chain; half of it runs backwards | selling | read-through | Recorded as a mistake not to repeat | `TT/…/V0.3.md` L40–58 | Y | | CUT |
| R-102 | 2026-07-29 | Wrote two session logs nobody asked for | selling | Thomas | "Offer, then write. Never write first." | `TT/…/V0.7.md` L195–202 | Y | | OK |
| R-103 | 2026-08-04→05 | The governing briefs were reported as "did not arrive" for four sessions while they sat on disk as .docx files | absence | read-through (the files were opened) | ".docx is not a wall" | `archive/EU/G.19.md` L73–77; `G.20.md` L32–38, Corrections #4 | Y | | CUT |
| R-104 | 2026-08-05 | Five handoffs in one day for a branch that had imported nothing — "over-servicing the chain" | selling | review | One handoff per batch of real work | `archive/EU/G.26.md` L64–67 | Y | | CUT |
| R-105 | 2026-08-08 | Agent git commands kept leaving lock files that blocked Thomas's commits; two wrong theories came first, and a handoff told the next agent to keep running git | tooling | Thomas (testing a theory) | Agents run no git on this repo | `archive/EU/G.53.md` L179–196; `G.54.md` L25–67; `G.56.md` Corrections 6 | Y | | OK |
| R-106 | 2026-08-08 | Three proposal files were written only to a sandbox `/tmp` and lost; Thomas's answers were left with nothing to review | tooling | read-through (next session) | "A draft that is not in the repo does not exist" | `archive/notes/Decisions-2026-08-08_EU-open-questions.md` L10–31 | Y | | CUT |
| R-107 | 2026-08-08→09 | Eighteen handoffs carried two work blocks as "untouched" after both were closed | drift | read-through (survey) | Name the underlying document beside every block label | `archive/EU/G.75.md` L29–56 | Y | | CUT |
| R-108 | 2026-08-29/30 | The main handoff was overwritten three times in one session without being archived | tooling | reconstruction after the fact | "Archive first, then rewrite" + checksum | `PH/…-033.md` L1–5; `notes/handoff-procedure.md` step 2 | Y | | CUT |
| R-109 | ≤2026-09-06 | Agents kept telling Thomas to commit ("you need to stop reminding me to commit") | selling | Thomas | Never tell Thomas to commit | `archive/playbook/PLAYBOOK-2026-09-06-pre-3way-split.md` §2 rule 1 L42–53 | Y | | CUT |
| R-110 | 2026-09-07 | The first audit of the slow-layer docs found seven live false statements, the oldest about three weeks old | drift | read-through (sweep) | Periodic sweep; correct in place, showing the old wording | `notes/doc-audit-2026-09-07.md` §1 L80–107 | Y | | OK |
| R-111 | 2026-09-02 | Handoffs carried false claims for weeks, including "uncommitted bodies of work" and memory entries that did not exist | drift | independent audit | No doc states git status | `Claude outputs/AUDIT-2026-09-02-independent-technical-audit.md` §1, §C1 | Y | | OK |

### 3D. thomascheesman.ca — the personal site (supporting examples)

Paths relative to `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme\`.

| ID | date | what the AI got wrong | kind | caught | rule it became | receipt | public-safe? | chk | Ruling |
|---|---|---|---|---|---|---|---|---|---|
| R-120 | 2026-04-29/30 | Guessed an image's wheel offset twice (15%, then 8%); measuring the file gave 0.2% | unmeasured | measurement | "When a guess about an image's proportions feels wrong, measure the file" | `git show 70fb966^:timeline-build-log/V0.03.md` L292 | Y | | CUT |
| R-121 | 2026-05-01 | A commit message claimed a cache-busting version bump that never reached the file, so visitors got stale JS | unmeasured | live check | "Always verify Version: actually changed" | commit `b2a0e50`; V0.05 L282 | Y | | CUT |
| R-122 | 2026-05-14/15 | Called the site "ready to go live" with hundreds of image URLs still hard-coded to the staging host | unmeasured | read-through (page-by-page) | Root-relative media URLs | `V0.10.md` "Where things stand"; `V0.12.md` §5 | Y | | OK |
| R-123 | 2026-05-15 | The go-live smoke test passed every page while logged-out visitors were seeing the host's "Coming Soon" page (admins bypassed it) | unmeasured | next session's checks | Confirm Coming Soon is off, logged out, at go-live | `V0.11.md` smoke-test table; `V0.12.md` §2 | Y | | CUT |
| R-124 | 2026-05-15 | Diagnosed video playback from `readyState` in an automated browser that cannot decode H.264 | tooling | Thomas (real browser) | "Do not re-diagnose video by readyState" | `V0.11.md` sharp edge 1 | Y | | CUT |
| R-125 | 2026-05-21 | About five false fixes for a registration bug; one commit called a red herring the "confirmed" cause | invented | measurement (captured the framework's notices) | Capture the framework's own warnings first | `V0.14.md` "The bug hunt"; commits `ab65ce7`, `43786d9`, `f3824e6`, `f4d3abc` | Y | | CUT |
| R-126 | 2026-06-15 | The first audit said the site was tracking-free; analytics were inside the combined bundles | absence | read-through (second pass) | Grep the combined bundles, not just the inline HTML | `V0.29.md` para 1 | Y | | CUT |
| R-127 | 2026-06-16→18 | Dropped `'unsafe-eval'` from the CSP as "audited unused"; it blanked the admin media library | unmeasured | Thomas | Keep it for wp-admin | `V0.30.md` G9; `V0.32.md` §3 | Y | | CUT |
| R-128 | 2026-06-17 | A content-creation tool the agent built defaulted to publishing immediately | unmeasured | audit | Draft by default | `V0.31.md` SEC-1; commit `c24c1ce` | Y | | OK |
| R-129 | 2026-06-19 | An accessibility pass was declared complete after the automated checker; the sitewide focus ring showed on nothing, and a Tab-through found 41 items with no focus cue | unmeasured | Thomas, then a manual Tab-through | The automated checker can't see this; do a Tab-through | `V0.34.md` L54, L59; commit `d8ebf3f` | Y | ✓ | OK |
| R-130 | 2026-08-06 | Handoffs treated pushes as deploys; the host's deploy hook had vanished and nothing new reached the site for about a month | unmeasured | live check | "Verify deploys from OUTSIDE" (curl the live version string) | `V0.41.md` "Read first" 1–3 | Y | ✓ | CUT |
| R-131 | 2026-09-19 | A "hidden" beta button had been visible to every visitor since it shipped (a class's `display` beat `[hidden]`) — the same bug class as R-019 | unmeasured | read-through (spec audit) | "A class with display beats [hidden]" | `docs/HERO-PROMOTION-SPEC.md` §5b item 3; `V0.42.md` | Y | | CUT |

### 3E. BareYourRare — bareyourrare.org (supporting examples)

Paths relative to `C:\Users\thoma\Desktop\My Files\Website Projects\BareYourRare Website\`;
commits in `bareyr`.

| ID | date | what the AI got wrong | kind | caught | rule it became | receipt | public-safe? | chk | Ruling |
|---|---|---|---|---|---|---|---|---|---|
| R-140 | 2026-03-04 | A site analysis invented a registered charity, "Bare Your Rare Foundation", and drafted schema and llms.txt around it, including made-up social-profile URLs | invented | read-through (later audit; privacy rewrite) | BYR is a personal patient-led project, not a charity | `_archive/loose/BYR-Website-Analysis-March2026.md` L8, §3.1; commit `2e0eb63` body | Y | ✓ | OK |
| R-141 | 2026-04-15→09 | The same framing shipped as sitewide `NGO` schema; flagged in June, still served in September | drift | read-through; live crawl | — (still open: see §5) | commit `457abbc`; `_archive/loose/BYR-FULL-AUDIT-2026-06.md` L68; `tc-ventures site/Claude outputs/byr-crawl-audit.md` §3a | Y | | CUT |
| R-142 | 2026-04-18→06-20 | For two months two condition pages silently lacked their medical disclaimer, schema, styling and scripts — a template check was missing a path prefix — while the to-do list marked them "Deployed for all 5" | unmeasured | live check + read-through (full audit) | — | commit `87c618b`; `_archive/loose/BYR-Master-Todo-List.docx` "Already resolved"; `BYR-FULL-AUDIT-2026-06.md` L26; fixes `35ea9a3`, `abf64d2` | Y | ✓ | CUT |
| R-143 | 2026-04-19/21 | An audit called a stray `</div>` in an accordion script "cosmetic — the accordion still works"; the syntax error meant no click handler had ever attached | unmeasured | behaviour test at fix time | — | `_archive/loose/byr-theme-audit.docx` Exec item 2, §4.5; fix `5883d52` | Y | | CUT |
| R-144 | 2026-04-23 | Four commits in a row tuned CSS in two files the theme never loaded | unmeasured | live check | Source-of-truth markers at the top of each file | commits `2574b85`, `22a43f5`, `12c0b31`, `75b8abf`; resolution `23e35b0` | Y | | CUT |
| R-145 | 2026-04-12 | A theme commit shipped 18 unresolved merge-conflict lines and crashed the site | tooling | live check (site down) | — | commits `ad1c3d4` → `40732e3` | Y | | CUT |
| R-146 | 2026-04-21 | A rewrite introduced a misspelling of Thomas's surname and repeated it five times | tooling | read-through (next day) | — | commit `787c5da` body | Y | | CUT |
| R-147 | 2026-09-20 | The crawl audit said a category page was poetry colliding with a disease name; it was an empty category | invented | read-through while fixing | Noindex empty category archives | `tc-ventures site/Claude outputs/byr-crawl-audit.md` §3c | Y | | OK |

---

## 4. Private — needs Thomas's OK (label only; not quoted)

These are real and receipted, but the receipts sit in private files or the story touches
something the standing rules keep off the site. Listed so nothing is dropped silently.
**Ruled 2026-09-23: all CUT.**

| ID | project | label | why it's here |
|---|---|---|---|
| P-01 | thomascheesman.ca | Heritage drafts stated invented family facts as true; several rounds of correction | family |
| P-02 | thomascheesman.ca | Kids' pages: invented details in a voice pass; identifying details published, later locked down | children |
| P-03 | this site | A public handoff was committed with children's names and removed in the next commit; a screenshot showed names at very low brightness | children |
| P-04 | this site | An early agent put a medical-accommodation offer on the hiring site without asking | health disclosure |
| P-05 | this site | Career-gap wording was wrong and self-contradictory | family/health |
| P-06 | thomascheesman.ca | A footer link exposed a personal email address | personal contact |
| P-07 | thomascheesman.ca | A credential appeared in chat history and was revoked | credential |
| P-08 | BareYourRare | A history-rewrite merge put private documents back on the main branch | ID documents |
| P-09 | GPRS | Several misses during the rebuild-period work | board / insurance matter |
| P-10 | memory files | Many "feedback" rules born from corrections (morning brief, BYR, TC) | private source |
| P-11 | private project | Four rows withheld | standing rule: private project |
| P-12 | research bundles | An outside model's handoff recorded personal circumstances it had no need for | health / personal |

---

## 5. Things the inventory turned up that are still live

Not receipts for a case study; open problems found while reading.

- **F-1** (above): the home page's measurement-script sentence.
- **BYR still serves `NGO` schema** on its guide pages (R-141). The fix is in
  `bareyr/functions.php` L707–715.
- Several misses recur across projects with the same rule re-learned each time — e.g.
  `display` beating `[hidden]` (R-019, R-131); "pushes are not deploys" (R-007, R-130);
  "the automated checker passed" (R-024, R-129). That recurrence is itself a `/method` point.

---

## 6. For `/method` — the rules table, pre-sorted

Each rule below has at least two rows behind it, from at least two projects.

| Rule | Rows |
|---|---|
| Measure the thing itself, not a proxy for it (drag the slider; Tab through the page; load it logged out) | R-019, R-024, R-042, R-050, R-062, R-123, R-129, R-131 |
| "Verified", "clean", "deployed" are claims — check them from outside | R-007, R-028, R-044, R-047, R-121, R-130, R-142 |
| The checker can be wrong too — test the test | R-045, R-048, R-052, R-053, R-055, R-061 |
| Say what you read, not what exists | R-021, R-029, R-073, R-080, R-089, R-090, R-091, R-103, R-126 |
| A quote is verbatim or it is empty | R-075, R-077, R-078, R-083, R-086 |
| A recommendation, a premise or a summary is a hypothesis | R-072, R-074, R-081, R-084, R-085 |
| Don't invent dates, figures or entities — ask | R-010, R-015, R-022, R-030, R-140 |
| No selling: no stale claims, no vanity numbers, no commitments that aren't yours | R-012, R-013, R-014, R-043, R-101, R-104 |
| One copy of each fact; a claim repeated in three notes is still one claim | R-007, R-107, R-110, R-111 |
| An extracting reader doesn't adjudicate; doubts get reported, not overridden | R-070, R-071 |

---

## 7. Sources, and what was not read

Read in full or near-full: everything listed in §1. The per-reader raw notes (about 700
rows, including the private ones) are **not** in this repo; they are kept outside it at
`Family & Personal\tc-ventures-private\receipts-001-raw\`.

Not read or only searched: `.zip` archives in the BYR `_archive`; code-dump `.docx` files;
the JSON data slices of Reports Clustering (searched only); the regional handoffs' JSON
sidecars; `claude/thomas-study.md` and `claude/tc-ventures-site-decisions.md` (in the Claude
project, not on disk); the Rocket Lander repo (private by standing rule); Heritage Research
(family).
