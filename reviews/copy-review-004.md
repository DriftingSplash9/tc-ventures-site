# Copy review 004 — the four remaining case studies, then the build ledger

**Written:** 2026-09-25
**Why:** Thomas ruled on 2026-09-25 that the four remaining case studies come before the build
ledger, in this order: the influence graph, then Bare Your Rare, then the Back Quarter and the
Desk together (plan-001 §5). He also ruled that the research repo,
`DriftingSplash9/Reports-Clustering`, is **meant to be public**. That makes one live sentence
on `/method` false (M9).
**Status:** M9, IG0–IG8 and P1 drafted 2026-09-25. **All ruled 2026-09-25:** M9 A (live),
IG0 A, IG1–IG7 OK, P1 OK, Q-IG1 to Q-IG3 answered; see "Rulings" at the end. Q-IG4 and Q-IG5
are open. The preview is built and checked (see the end).
**BYR0–BYR8 and P2 (Bare Your Rare) drafted 2026-09-25**, after Step 1 was ruled ("1 yes, 2 yes,
3 yes, 5 yes"). **Second round ruled 2026-09-25** (see "Rulings, BYR" at the end): H1 A, quote A,
Q-BYR2 to Q-BYR4 and Q-BYR6 answered. **Third round ruled 2026-09-26:** BYR2b A, BYR3–BYR7 and P2
OK, no Fig. 2, Q-BYR7 yes. Open: Q-BYR5 (Hostinger), which doesn't block the copy. The preview is
next.

Same format and marks as copy-review-001 to 003: `OK` · `KEEP` · `A` / `B` · `FIX` · `CUT`.

---

### M9 — `/method`, The rules: the "private" sentence

> **Live:** These are the rules I hold AI work to, across all of my projects. Each one was
> drawn from misses written down in handoffs, reviews and audits, and each row links one of
> them. Misses from the research project link to the inventory, because that project's files
> are private.

**⚠ FLAG: the last sentence is false.** GitHub's API reports the repo as `"visibility":
"public"` (checked 2026-09-25), and Thomas confirmed that it is meant to be. The sentence came
from handoff-017, which called the repo private. Nobody checked GitHub.

> **A (recommended):** cut the last sentence. The rows keep linking the inventory, which names
> the file behind each miss.
>
> **B:** "Misses from the research project link to the inventory, which names the file each
> one is recorded in."

A adds no words. The rows' links stay the same either way, and M8's "(→ R-045)" is not
affected. The rows could now link the research files directly, but that isn't proposed here
(see IG0).

---

## `/work/influence-graph` — the research graph (IG0–IG8)

**Drafted 2026-09-25.** Sources: the OK rows in `plans/receipts-001.md` §3C, the live
`/projects` graph section, and the research repo's own `START-HERE.md`, `CLAUDE.md`,
`PLAYBOOK-RENDER.md` and `HANDOFF.md`. Nothing in the research repo was changed, and no git
was run there.

**Checks run 2026-09-25:**
- **Excerpts:** every quoted excerpt was checked by script against the local file. A copy with
  one word changed failed, so the check can fail. Each quote was then found in the **public**
  copy on GitHub, which is what the page will link.
- **Receipt files:** all three return 200 when not logged in.
- **Receipts re-opened:** R-050, R-076 and R-110. R-110 is now ticked in receipts-001.

**Why these three misses.** There are 22 OK rows to choose from. These three are three
different kinds of miss: one in the app, one in the research, and one in the project's own
records. None of them is the miss told on the home page (R-061), and only R-050 is also on
`/method`. If you'd rather lead with others, the strongest alternatives are:
- **R-061**, the measurement-script bug (it would link the home page's story to its source)
- **R-075**, the footnote built from true parts
- **R-062**, the sweep baseline that never reproduced

### IG0 — ⚠ FLAG, read first: linking the research repo

Now that the repo is public, the page can link each miss to the file it's recorded in, the way
`/work/gprs` and `/work/this-site` do. One thing needs your call first.

**The outside research model's name (F-2).** You ruled 2026-09-23 that site copy never names
it. receipts-001 said the file names that carry it were "paths into a private repo and are
never published". They are published now:
- **52 file paths in the public repo contain the name** (counted by script from GitHub's file
  list, 2026-09-25). None of them is linked below.
- **The three files this page would link mention it in their text.** Lines matching the name:
  handoff 032, 12 · NZ `G.3.md`, 6 · `doc-audit-2026-09-07.md`, 1.
- **No other private topic matched** in those three files (searched: lander, rocket, family
  words, health words).

> **A (recommended):** link the three files as they are. The page's Repo link and the Source
> link already on `/projects` put the whole repo one click away, so routing around three files
> hides nothing. This is the same reasoning as T0 A.
>
> **B:** link receipts-001 §3C instead, as `/method` does. It's weaker, because the reader gets
> my inventory instead of the record itself.

The name in the research repo's archive is separate from this page. F-2 records your
2026-09-07 ruling that the research docs drop it. The archive still carries it. That's yours to
decide; I've changed nothing there.

### IG1 — header

> **Label:** Case study · a research project
> **H1:** The Economic Report Influence Graph
> **Claim:** A 3D map of where official numbers come from, where a line between two reports
> goes in only if a published document says it belongs there.
> **Spec table:** Stack: TypeScript · Vite · React · three-forcegraph · d3-force-3d · no
> backend · Status: In active development · Corpus: thousands of published reports and the
> documented dependencies between them, growing weekly · Coverage: well over a hundred
> countries · Evidence: every dependency graded A, B or C on how well its document supports it
> · Repo: DriftingSplash9/Reports-Clustering · Since: July 2026
> **Page title / link preview:** The Economic Report Influence Graph - Thomas Cheesman

Where it comes from:
- **H1:** the project's name, as on `/projects`. The sub-menu uses the H1 as its label, which
  makes this the longest item in the sub-menu (IG8).
- **Claim:** "A 3D map of where official numbers come from" is the live `/projects` link-preview
  text. The rest restates "No document, no edge".
- **Stack and Status:** the `/projects` label and spec table, unchanged.
- **Corpus:** "thousands of" instead of `/projects`' "Nearly 4,000". A description doesn't need
  re-checking as the corpus grows.
- **Coverage:** "well over a hundred countries" is `START-HERE.md`'s wording. `/projects` says
  "130+".

**Q-IG2 — Since.** The repo's first commit is dated 2026-08-07 ("Initial commit:
pre-reorganization snapshot", from GitHub's API). The inventory's earliest record of the
project is 2026-07-28 (R-040), and "July 2026" rests on that. When did you start it?

### IG2 — The ask

> **H2:** A question nobody could answer
>
> *(The first two paragraphs of the `/projects` section, unchanged: "Every important number in
> public life… This draws it… with no backend.")*
>
> *Pull quote, verbatim from the project's `START-HERE.md`:* "The question it's built to answer
> is: if this number changed, what else would have to change?"
>
> "It's a personal project, built for curiosity rather than for anyone in particular. There's
> no company behind it and nothing is being sold."

**⚠ FLAG: there is no brief in your words.**
- **Searched:** the research repo's `CLAUDE.md`, `README.md`, `START-HERE.md`, `REPORTS.md`
  and `HANDOFF.md`, and its `notes/` folder, for a line in your words about the project's
  purpose.
- **Closest:** `REPORTS.md` says `START-HERE.md` is "the plain-language description Thomas sends
  to other people". I can't tell whether you wrote it or approved a draft.

**Q-IG1:** one or two sentences on why you built it, in your words? If you give them, they
become the pull quote, as Q-G1 did on `/work/gprs`. If not, the `START-HERE.md` lines stand,
attributed to that file.

### IG3 — The standard

> **H2:** No document, no edge
>
> *(The `/projects` paragraph under "The rule the whole project runs on", unchanged: "No
> document, no edge. A line is drawn only if a published document says, in words I can quote,
> that one report uses the other as an input… a map that hides its own weak spots is worse than
> no map.")*
>
> *Excerpt, verbatim from the project's `CLAUDE.md`:* "No document, no edge. If nothing
> published says a dependency exists it does not go in the graph; unverifiable leads go to
> `_dropped` with a reason." · "`npm run validate` must pass before and after any data change."
>
> The checks that enforce it are on the Method page. (→ `/method`, "In the research graph, the
> checks are code")

The last line points at M8 rather than repeating it, so there is one copy of each fact.

### IG4 — What the AI got wrong

> **H2:** Three misses: a slider, a sentence, and the docs
>
> **1. Sliders that did nothing.** The layout has sliders for its physics, such as how hard
> the clusters of different countries push apart. Three times, a new force shipped with a
> slider that did nothing. Each time the force itself was correct, and a script measured it
> working. But moving the slider never restarted the simulation, and by the time anyone
> touched it the simulation had settled, so the force was being multiplied by almost nothing.
> *(looked right but was not measured · handoff 032)*
>
> **2. The right quote, the wrong subject.** A research session recommended a New Zealand
> dependency as checked and ready to add: New Zealand's government finance statistics, built
> on the international System of National Accounts. The quote behind it was real and copied
> correctly. But the sentence was about an international manual, not New Zealand's release. It
> said the manual is consistent with the System of National Accounts, not that New Zealand's
> figures are built from it. *(plausible but invented · NZ handoff G.3)*
>
> **3. Documents that were true when written.** Besides the handoff, which is rewritten every
> session, the project keeps standing documents: its rules, its playbooks and its
> plain-language description. The handoff was checked every session. Nothing checked the
> others. When they were read against the most recent handoffs, seven statements in them were
> false, and every one had been true when it was written. *(drift across sessions · doc audit,
> 2026-09-07)*

Checked against the receipts:
- **1:** handoff 032 L225–243. "Multiplying it by nothing": the simulation's energy "has
  decayed to ~0" before anyone touches a slider, hence "almost nothing". The three, by their
  names in the code, were `geoAffinity`, `galaxy` and `clusterRepulsion`.
- **2:** `G.3.md` L129–164. The sentence is "In 2018, we implemented the Government Finance
  Statistics Manual 2014 (GFSM2014), which follows the GFSM 2001 and is consistent with the
  System of National Accounts 2008 (SNA08)." Its subject is the manual, and the research had
  quoted it correctly.
- **3:** `doc-audit-2026-09-07.md` L80–100: "seven live false statements… every one of them a
  sentence that was true when written". The 25 handoffs it read span 2026-09-04 to 09-07, so
  the copy says "the most recent handoffs", not a length of time.

**"Seven" is an exact count.** It's a finished, historical figure about the docs, not a corpus
count, so it won't go stale. **KEEP** it, or **FIX** to "several".

### IG5 — How I caught it

> **H2:** Use it, read the sentence, sweep the rest
>
> **1. I used it.** The last two were caught the same way: I moved the slider, saw nothing
> change, and said so. The third time, my words were "I don't see any effect from it." The force
> was fine. The slider had never been wired to restart the simulation, as the working sliders
> were. The fix copied their wiring, and it was checked by dragging the slider in my browser.
> *(Became the rule: "verify by dragging the slider, not by measuring the force in a script" ·
> PLAYBOOK-RENDER.md)*
>
> **2. The next session read the sentence, not the summary.** The following session went back
> to the quoted sentence itself, instead of the last session's summary of it, and checked what
> the sentence was about. The dependency was not added. It went on the dropped list with the
> reasoning. The two other New Zealand dependencies recommended with it held up, and were
> added. *(Became the rule: "read the sentence as well as fetching it" · NZ handoff G.3)*
>
> **3. I asked for the documents to be checked against the record.** Too many recent sessions
> had been about the machinery, not the research: "many recent threads have had to do with the
> way this all works, not the actual work on the project." So I asked for the latest handoffs
> to be read against the standing documents. That read found the seven, and all seven were
> corrected. It is routine now: every fifth handoff sweeps the standing documents as well as
> itself. *(The rule now: sweep everything on every fifth handoff · HANDOFF.md)*
>
> *Rules table:* three rows, one per miss.

| The correction | The standing rule | Enforced in |
|---|---|---|
| Three sliders shipped doing nothing, while a script said each force worked (R-050) | Verify by dragging the slider, not by measuring the force in a script | `PLAYBOOK-RENDER.md` |
| A correctly quoted sentence was about something else (R-076) | A recommendation, a premise or a summary is a hypothesis until it is checked | `CLAUDE.md` · rule 13 |
| Seven statements in the standing documents had gone stale unnoticed (R-110) | Every fifth handoff sweeps everything, the standing documents included | `HANDOFF.md` |

Who caught what (the "I" rule):
- **1 is yours, for the last two.**
  - Handoff 032 records you saying "can you check out the cluster repulsion? I don't see any
    effect from it", and the fix being "verified live in Thomas's browser".
  - The galaxy slider: handoffs 006 and 007 (2026-08-20) both open with "Thomas: 'The galaxy
    pull doesn't appear to have…'".
  - The first slider (`geoAffinity`): I didn't find how it was caught. So the copy claims the
    last two, not all three.
  - **⚠ DOUBT:** `/method`'s ruled row says "I caught it by using them". That covers all three,
    and I can confirm two. It is not proposed for change. Say if you want it narrowed.
- **2 was the agent's,** so it's written impersonally.
- **3: you asked, and the audit found.** `doc-audit-2026-09-07.md` opens with your instruction,
  quoted above verbatim.

"Became" is checked for timing:
- **1:** handoff 032 says "Now PLAYBOOK rule 20" in the same session. The rule now lives in
  `PLAYBOOK-RENDER.md` L38–44, quoted verbatim.
- **2:** `G.3.md` L539 says "as of this session".
- **3 changed after it was made.** The audit proposed a sweep every 25th handoff. You ruled on
  2026-09-10 that the standing documents are swept on every fifth (`HANDOFF.md` L290–291). So
  the label says "the rule now", not "became".

**⚠ DOUBT on row 2 (reported, not overridden).** "Read the sentence as well as fetching it" is
not in the research project's current playbooks. I searched `PLAYBOOK*.md` for "read the
sentence", "grammatical" and "subject of". So the table row gives the truth rule it falls under
(`CLAUDE.md` rule 13) instead of a rule that is no longer carried forward. The caption says
"falls under", as on `/work/this-site`. Whether the research project should carry that rule
again is yours to decide, and out of scope here.

**`HANDOFF.md` is rewritten every session,** so its line numbers move. Its receipt link is
pinned to the commit that is current on GitHub (`8b2f593`), not to `main`. The archive files
don't change, so they link `main`.

### IG6 — What shipped

> **H2:** A graph that shows its own weak spots
>
> *(The live-graph section from `/projects`, moved here unchanged: "One city's budget, traced
> all the way back", the still, the load button, the legend, and "One path through it, in
> words" with its chain of six documents.)*
>
> *Fig. 1:* the application, filtered to national-tier reports (the `/projects` figure and
> caption, unchanged). *Fig. 2:* the sparser national view (likewise).
>
> **The honest limits:** *(The `/projects` paragraph "It is not finished, by design",
> unchanged.)* The live slice on this page is a snapshot from September 2026, and the full graph
> has moved on since. The grades also show how unevenly the map is drawn: some countries in
> depth, others by a single thread, which says who has looked, not what exists.

- **Snapshot date:** `public/assets/gp-budget-graph.json` was committed on 2026-09-16 and
  hasn't changed since.
- **"Unevenly drawn":** from `START-HERE.md`: the grading pass "exposed… how unevenly the map
  is drawn… a fact about who has looked, not about the country."
- **The H2** echoes the live line "a map that hides its own weak spots is worse than no map".

### IG7 — Receipts

- `START-HERE.md` (the ask, the honest limits)
- `CLAUDE.md` (the standard)
- `archive/Previous Handoffs/HANDOFF-2026-08-28-pre-trim-032.md` L225–243 (miss 1)
- `PLAYBOOK-RENDER.md` L38–44 (rule 1)
- `archive/NZ/G.3.md` L129–164, L536–541 (miss 2)
- `notes/doc-audit-2026-09-07.md` L1–5, L80–100 (miss 3)
- `HANDOFF.md` at `8b2f593`, L286–292 (rule 3)
- `receipts-001.md` §3C
- `/method`

All are in the research repo except the last two. If IG0 is B, the first seven become one link
to receipts-001 §3C.

### IG8 — what goes with it (not copy)

1. **The live demo moves here,** as plan-001 §3 already says ("keeps the live demo", "split
   out of projects"). That includes its data file and script. The figures move too. One copy
   of the demo, not two. `/projects` after the split is P1.
2. **The home page's graph card** (`index.html` L86) links `/projects#graph`. **Q-IG3:** should
   it point at the case study instead? I recommend yes. The card's words don't change.
3. **The sub-menu** gets "The Economic Report Influence Graph" under Projects, on all nine
   files. It's the longest label, so it needs checking at 375px.
4. **The usual checklist:** remove the banner, `noindex` and the `.assetsignore` lines; add the
   page to the sitemap; verify live (the check-run, curl, the console, 375px, keyboard).
5. **The security policy** isn't changed. The demo already runs under it on `/projects`, with
   the same files. The live console still gets read after the push.

### P1 — `/projects`, the graph section after the split

> **Proposed:** keep the label, the H2, the two opening paragraphs, and the application figure
> with its caption. Then add one line:
>
> "The rule it runs on, a live slice of one city's budget, and three things the AI got wrong
> while building it: read the case study."
>
> Keep the Source link. Everything else in the section moves to the case study (IG3, IG6) or
> is cut.

What gets cut from both pages, and why:
- **"What is actually hard about it", both paragraphs.**
  - The first says "eighty-odd research sessions". The research repo's
    `archive/Previous Handoffs/` now holds 97 files (GitHub's file list, 2026-09-25), so the
    figure may have gone stale. Files are not the same as sessions, so I haven't recounted.
  - The second, "each is measured rather than eyeballed", is IG4's first miss told in general
    terms.
  - **CUT** (recommended), or **KEEP** it in the case study under IG3.
- **The spec table.** It moves to the case study header (IG1), so there is one copy.

---

### Rulings (Thomas, 2026-09-25)

"m9 A, ig0 A, q-ig3 yes, p1 ok"
- **M9 A:** the "private" sentence is cut. Applied to `public/method.html` 2026-09-25 and
  shipped on its own, because it corrects a false line that was live.
- **IG0 A:** the case study links the three research files as they are.
- **Q-IG3 yes:** the home page's graph card will link the case study. It ships in the same push
  as the page, never as a link that 404s.
- **P1 OK:** the `/projects` graph section is cut down when the case study ships, not before.

"I made the Graph because I wanted to see how something at a municipal level is influenced by
something on the international level. I also wanted to see how organizations such as the EU and
Brics operate compared to nations., since july 2026, ig1-ig7 ok, seven keep" (verbatim)
- **Q-IG1 answered.** His first two sentences replace the `START-HERE.md` lines as IG2's pull
  quote. They are verbatim, except that "nations.," is closed up to "nations." (the comma
  belongs to the ruling that follows). "Graph" and "Brics" are as he wrote them. **Q-IG4:**
  "Brics" or "BRICS"? The research repo spells it "BRICS".
- **Q-IG2: July 2026.** "Since: July 2026" stands.
- **IG1–IG7 OK.** The three lead misses stand.
- **"Seven": KEEP.**

**Preview built 2026-09-25:** `public/work/influence-graph.html`, with a draft banner and
`noindex`, and listed in `.assetsignore`. It is built from the ruled copy, with the demo
markup and the reused `/projects` paragraphs copied unchanged.
- **The sub-menu** lists the graph first, matching the order of `/projects`.
- **Receipt links are pinned** to research-repo commit `8b2f593`, the archive files included.
  IG7 said the archive files would link `main`. Pinning also covers a file being moved, which
  that repo does (the 2026-09-07 audit found paths that had moved to `archive/`).
- **Line ranges:** the first and last line of each range were read from the pinned commit.
  `PLAYBOOK-RENDER.md` now starts at L33, where rule 18 begins, instead of L38.
- **The excerpt** keeps the "2." rule number, as the source line has it.

Checked locally in headless Chromium: 16 of 17 checks passed.
- **Passed:**
  - status, title, the six sections in order, and the sub-menu with `aria-current`
  - the graph loads from the keyboard, focus moves to the stage, and an arrow key reads out a
    dependency
  - no console errors, and no sideways scroll at 375px
  - with JavaScript off: the button and stage are hidden, and the still and the five-link chain
    show
  - 36 links, all 200 except LinkedIn (999, expected). A negative control (an unknown local
    URL) returns 404, so the link check can fail.
- **The one failure was the test (rule 3).** The browser reports the "Fig. N" rule, not the
  number it draws, so the numbering was checked in a screenshot instead: Fig. 1 and Fig. 2.
- **Looked at:** the header, misses, rules table and demo in light and dark at 1280px, and the
  header at 375px.
- **Not checked:** the live security policy, since `_headers` isn't served locally. The live
  console gets read after the push.

**Q-IG5 (new): the counts in Fig. 1.** The application screenshot shows the app's own exact
report and dependency counts in its side panel. That screenshot is the one ruled exception to
the no-exact-counts rule, on `/projects`. IG6, ruled OK, puts it on this page too. Does the
exception cover it here? I recommend yes. It's the same image, and it's the app's display, not
copy.

**Ruled (Thomas, 2026-09-25): "BRICS, q-ig5 yes, ship it".**
- **Q-IG4: BRICS.** The pull quote now reads "BRICS". This changes his quote, at his ruling.
- **Q-IG5 yes:** the Fig. 1 exception covers this page too.
- **Ship it.**

**Shipped 2026-09-25**, on the IG8 checklist, plus P1 and Q-IG3:
- The page: the draft banner, `noindex` and the `.assetsignore` line are removed. "BRICS"
  applied.
- The sitemap has `/work/influence-graph`, before `/work/gprs` (the sub-menu order).
- The sub-menu lists it first, on all nine other pages.
- `/projects` graph section (P1): the label, H2, two paragraphs, application figure, the new
  "read the case study" line and the Source link are kept. The rule paragraph, the demo, "What
  is actually hard", "It is not finished", the nations figure and the spec table are gone.
  `graph-demo.js` is no longer loaded there.
- **Home (Q-IG3):** the graph card links `/work/influence-graph`.
- **CSS, one additive line:** `.shot + .prose { margin-top: var(--block); }`. Without it,
  P1's new line sat close under the figure caption and read as part of it. A script found
  only that one place on the site where a figure is followed directly by a prose block.

Checked locally before the push:
- **Site-wide suite: 109 of 110 passed.** It checked every page's status, the nav order, both
  `aria-current` levels, no `noindex`, no draft banner, a clean console, and 375px. It also
  checked the sub-menu by keyboard (Tab reaches the toggle; Enter opens; the first item is the
  graph; Esc closes and returns focus), P1, and the home link. A negative control, the committed
  pre-release home page, is caught as having the old sub-menu.
- **The one failure was the test:** `/404` carries `noindex`, as it did before this release.
- **Case-study suite: 16 of 17 passed,** with the same known Fig.-number test limit as the
  preview.
- **Looked at:** `/projects` graph section at 1280px, and the sub-menu open at 375px. The
  longest label fits on one line.

**Was open before it shipped:** Q-IG4 (Brics / BRICS) and Q-IG5. Then it ships on IG8's
checklist, plus P1 and Q-IG3, when Thomas says so. Noticed, left for the design phase: the demo's
paragraph sits tight against its frame, the same as on `/projects`.

---

## `/work/bare-your-rare` — Bare Your Rare (BYR0–BYR8, P2)

**Drafted 2026-09-25.** Sources: receipts-001 §3E, `Claude outputs/byr-crawl-audit.md`,
`handoff-011.md`, `handoff-012.md`, the new `Claude outputs/byr-bot-check-2026-09-25.md`, the live
site fetched logged out, and the `bareyr` repo on GitHub (`DriftingSplash9/bareyourrare`,
private: read, never linked). Nothing in the research repo was touched.

### BYR0 — Step 1: the ground, checked (not copy)

**Ruled (Thomas, 2026-09-25): "1 yes, 2 yes, 3 yes, 5 yes"**, and Q-BYR1 answered (BYR2).

1. **O-13, the `NGO` schema: fixed at the origin, cached copies pending a purge.**
   - Before: all five guides and the HCS story page served the sitewide `NGO` block (checked
     logged out, 2026-09-25).
   - `bareyr` commit `6e07481`, pushed to `main`: `'@type' => 'Organization'`, the publisher type
     `inc/guide-schema.php` already uses. PHP lints clean. No other field changed.
   - After, uncached (before 21:51 UTC): `/about/`, `/faq/`, `/hcs-guide/`, and cache-busted fetches of
     `/hcs-guide/` and `/poems/` carry no `NGO`. So the deploy ran.
   - **Still `NGO`, from LiteSpeed's cache:** `/`, `/poems/`, `/sps/`, `/ecd/`, `/fechtner/`,
     `/hajdu-cheney-syndrome/`.
   - **Thomas purged the LiteSpeed cache.** Re-checked after, logged out: no `NGO` on `/`, the
     five guides, `/hajdu-cheney-syndrome/`, `/about/` or `/privacy/`, and each carries the
     sitewide `Organization` block. `/poems/` and `/ecd/` first got the host's "Bot Verification"
     page (see 2) and were checked on a retry 20 s later. **O-13 is closed.**
   - **The first "fixed" read was wrong (rule 3).** It matched the guide's publisher block, which
     has the same name and type, and called `/poems/` fixed. Re-counted by grepping for `"NGO"`.
2. **The host fault is only partly fixed.** Full log: `Claude outputs/byr-bot-check-2026-09-25.md`
   (script: `scripts/byr_bot_check.py`).
   - Every page LiteSpeed had cached was served to every agent tried.
   - Pages it had not cached were refused at the origin, behind Cloudflare, to three of the five AI
     agents tried: GPTBot got a 429 every time, Claude-User and PerplexityBot got LiteSpeed's
     reCAPTCHA "Bot Verification" 403 some of the time. ClaudeBot and ChatGPT-User got through.
   - One network, one evening, spoofed user-agents: a real crawler may be treated differently.
   - **After the purge it hit a browser too:** a Chrome user-agent, one request every 7 s, got
     the "Bot Verification" page on 2 of 10 pages, none of them cached yet. Added to the check
     file.
   - So plan-001 §3's frame, "the fix, verified", can't stand. BYR4 and BYR6 say what's true.
     Proposed as **R-150**.
   - **The fix is at Hostinger, not in the theme.** See Q-BYR5.
3. **Receipts added to receipts-001 §3E:** **R-148** (the audit read one day's failures as a
   standing block) and **R-149** (the audit said the hero image had no alt text; it had
   `alt=""`), both OK at "3 yes". **R-150** is added as pending; BYR4 rules it. "The fix" itself
   is not a row, because rows are misses. It's a receipt for BYR6, linked directly.
4. **Privacy read (R-026)** of every file BYR7 links: no symptom detail and nothing about family
   in `byr-crawl-audit.md` or the new check file. `handoff-011.md` and `handoff-012.md` carry the
   standing family rules (a name, "the three children", no children's names) and O-4's line about
   a disclosed address, without the address. **Precedent:** live pages already link
   `handoff-012.md` (`/work/this-site`) and `handoff-015.md`, which carry the same rules. So
   linking `handoff-011.md` adds nothing new.
5. **⚠ FLAG: the footer's social links.** R-140 says the March analysis made up social-profile
   URLs. Every BYR page's footer links `x.com/bareyourrare`, `facebook.com/bareyourrare`,
   `instagram.com/bareyourrare` and `tiktok.com/@bareyourrare` (`inc/footer.php` L104–131, there
   since the repo's first commit, 2026-04-05). The sitewide schema's `sameAs` is empty, under
   "TODO: add social profile URLs when accounts are live". I can't tell from here whether the
   accounts exist or are yours: social sites refuse scripted fetches. **Q-BYR6: are they yours?**
   If not, R-140 is still live on the site this page is about.
   - **Answered: "no, nobody has claimed them yet".** So every BYR page links four accounts that
     don't exist. Anyone who registers those names first gets the links.
   - **Q-BYR7: remove the four links from BYR's footer now?** I recommend yes: delete them from
     `inc/footer.php` and put them back when you claim the accounts. The alternative is to claim
     the four names first and keep the links.
   - **The case study doesn't mention the footer.** The links are in the repo's first commit, and
     R-140's analysis made up social links. But I can't show they're the same ones, so the page
     makes no claim about where they came from.

### BYR1 — header

> **Label:** Case study · a patient site
> **H1:** A rare-disease site, written by a patient *(ruled A)*
> **Claim:** Five plain-language guides to ultra-rare conditions, marked up so a search engine or
> an AI assistant can tell what each page is, who wrote it, and when it was last reviewed.
> **Spec table:** Stack: WordPress with a hand-coded Astra child theme · page content lives in
> the theme, not the editor · Status: Live · Hosted: Hostinger, behind Cloudflare since
> September 2026 · a push to `main` deploys · Repo: private · Since: March 2026, as a hand-coded
> theme
> **Page title / link preview:** *(the H1)* - Thomas Cheesman · description: the claim.

Where it comes from:
- **H1 A** describes the site, as `/work/gprs`'s "A housing society's website" does. The name
  alone tells a stranger nothing. The sub-menu uses the H1. A is 41 characters, six more than
  the graph's label, so it needs checking at 375px.
- **Claim:** each part was checked live on all five guides, 2026-09-25: `MedicalWebPage` with
  `medicalAudience: Patient`, `author` and `lastReviewed`, plus a `MedicalCondition`.
- **Stack:** `/work/gprs`'s wording. BYR is built the same way (`bareyr` `AGENTS.md`). WordPress
  appears once, here.
- **Hosted:** Cloudflare since 2026-09-20 (handoff-011, O-10). "A push to `main` deploys" was seen
  today: `6e07481` was pushed at 21:40 UTC and served to uncached requests before 21:51.
- **Repo: private.** It 404s logged out, so nothing links it. Or drop the row. Say if you'd
  rather.

**Q-BYR2, answered:** "the idea started in March as I had to move content from the old site to the
child theme". So **Since: March 2026, as a hand-coded theme.** The older site, built in the editor,
isn't dated on the page. Say if you want its start year there. *Was asked:* the repo's first
commit is 2026-04-05 ("Initial commit"), but the site is
older than the repo:
- the March 2026 site analysis (R-140, 2026-03-04)
- the logo's upload path, `2026/02`
- the schema's `foundingDate`, "2026"

When did you start it?

### BYR2 — The ask

> **H2:** What I would have wanted to find
>
> I have Hajdu-Cheney syndrome (HCS), a rare connective-tissue disorder.
>
> *(The `/projects` paragraph, unchanged: "Bare Your Rare is a patient-led site for ultra-rare
> conditions, built because most people searching for one of them find almost nothing… put into
> plain language.")*
>
> *Pull quote, Thomas, 2026-09-25:*
>
> **A (ruled), two typos closed up:** "I built it from a patient(me)'s point of view. I
> asked myself what would be helpful to me to come across on the internet? What can explain the
> nuances of HCS? And then I thought I may as well expand this to more rare disorders so I
> researched several others. I also wanted to work on my web design and building skills."
>
> **B, exactly as typed:** "…And then I th ought  I may as well expand this… my webb design and
> building skills."

- **A changes only two things:** "th ought" (and its double space) becomes "thought", and "webb"
  becomes "web". "patient(me)'s" and both question marks stay as you wrote them. This is the same
  kind of close-up as "nations.," on the graph.
- **The first line** is `/background`'s wording, plus "(HCS)", because the quote uses the
  abbreviation. The condition is named on purpose, and nothing about symptoms is added.
- The quote cites this review (Q-BYR1), as `/work/gprs` cites copy-review-003 for Q-G1.

### BYR2b — The ask, second half: why a hand-coded theme (new, from your Q-BYR2 answer)

> In March 2026 I started moving the site out of the page builders it had been built with and into
> a theme written for it.
>
> **A (ruled):** "I wanted freedom to do things I couldn't or that were a pain in the butt
> because of the extra weight handling the themes and plugins. Why pay for a plugin when I can ask
> [an AI] to make it my way for my content?"
>
> **B:** the first sentence only.
>
> *(Thomas, 2026-09-25 · copy-review-004, Q-BYR2)*

- **The lead-in** restates your answer ("the idea started in March as I had to move content from
  the old site to the child theme, prior I was building right in WordPress>blocks, Elementor,
  etc."). It says "page builders" instead of the product names, because WordPress stays out of
  the prose (it's in the spec table).
- **"[an AI]" is an edit to your words.** You wrote "ask you", meaning me. On the page, "you" reads
  as the visitor. Rule 8 says a quote is verbatim, so the brackets show the change. That's your
  call: A with the brackets, or B, which drops the line. The last line is the most on-point
  sentence for a page about directing AI, which is why A is recommended.
- `/work/gprs` has the same point in your words ("because I wanted more freedom to experiment
  with the code"). The two pages agree without repeating each other.

### BYR3 — The standard

> **H2:** Cited, dated, and readable before any script runs
>
> Each guide links to the medical literature and patient organisations it was written from, and
> says when it was last reviewed. The words are in the page the server sends, so nothing has to
> run before a reader, a search engine or an AI assistant can read them.
> (→ `byr-crawl-audit.md` §2, §5)
>
> The machine-readable copy says the same things. Each guide tells software what it is (a
> medical web page, written for patients), which condition it covers, who wrote it, and when it
> was last reviewed. That date comes from the same function as the date printed on the page, so
> the two can't disagree. (→ `handoff-012.md` §4, O-11)
>
> *Fig. 1:* part of the structured data `/hcs-guide/` serves, verbatim, trimmed to the fields
> named above.

Checked live, 2026-09-25:
- **Sources:** every guide links outside the site to sources. Across the five: PubMed and PMC,
  MedlinePlus, Orphanet, OMIM, NORD, journal publishers, and condition organisations.
- **Review date:** every guide shows "Last reviewed: April 2026", and its `MedicalWebPage` says
  `"lastReviewed": "2026-04"`.
- **"The same function":** handoff-012 says the visible line and the schema both read
  `byr_guide_review_date()`. Confirmed in `bareyr`: `inc/guide-schema.php` L66 and all five guide
  templates call it.
- **Fig. 1** is a code excerpt, not a screenshot, so no guide text appears in it.

### BYR4 — What the AI got wrong

> **H2:** A charity that didn't exist, and an audit that overreached
>
> **1. A charity that didn't exist.** A site analysis invented a registered charity for the site,
> "Bare Your Rare Foundation", and drafted its structured data and its summary for AI tools
> around it, with made-up social-media links to go with it. Bare Your Rare is one person's
> project. Part of that framing shipped: from April, every page told software the site was a
> non-governmental organisation, and went on saying so until September. *(plausible but invented
> · drift across sessions · receipts-001, R-140, R-141)*
>
> **2. Two problems that weren't there.** A crawl audit of the site said a poetry category
> collided with the POEMS syndrome guide. The category was empty. It said the header image had no
> text alternative on nearly every page. The image had carried an empty one since April, which is
> how a decorative image is marked. *(plausible but invented · not seen, so called missing ·
> receipts-001, R-147, R-149)*
>
> **3. A fix recorded as done.** The same audit's most serious finding was that the host refused
> automated fetchers. That matters here: when a patient asks an AI assistant about their
> condition, the assistant fetches the page on their behalf. The site was moved behind
> Cloudflare, and the notes recorded the problem as fixed. Five days later, pages the host had
> not cached were still being refused to some AI agents, by the host itself. *(looked right but
> was not measured · receipts-001, R-150)*

Checked against the receipts:
- **1:** R-140's row, and `/method`'s ruled wording for the same miss ("…with made-up social-media
  links to go with it"). The analysis file is on your disk, not in any repo I can read. R-140 is
  already ticked.
- **1, second half (R-141, un-cut at Q-BYR3):**
  - `bareyr` `457abbc` (2026-04-15), "Add sitewide NGO JSON-LD schema to wp_head".
  - `byr-crawl-audit.md` §3a: still served in September.
  - Fixed by `6e07481` (2026-09-25) and checked live after the purge (BYR0 1).
  - "Flagged in June" is in R-141's row, but the June audit is on your disk, so the copy leaves
    it out.
- **2:** `byr-crawl-audit.md` §3c and §3e. `handoff-012.md` §4 O-11: "(c)… it is an empty category
  (one unpublished post)" and "(e) needed nothing: the hero image already serves `alt=""`". The
  `alt=""` is in `bareyr` `inc/hero.php` from `1bee6ba` (2026-04-19).
- **3:** `handoff-011.md` §4 O-11: "§1 (host blocking) is fixed by O-10". Then
  `byr-bot-check-2026-09-25.md`.
- **"not seen, so called missing"** is a new kind label, for receipts-001's `absence`. No
  live page has used that kind yet. **FIX** it if you want other words.

**Q-BYR3, answered: "yes".** R-141 is un-cut in receipts-001 and is now in miss 1 above. *Was
asked:* un-cut R-141? It's the rest of miss 1: the invented framing shipped as sitewide `NGO`
schema in April, was flagged in June, and was still served until today. You cut it on
2026-09-23, before today's fix. With it, miss 1 ends with "…and every page went on telling
software the site was a non-governmental organisation for five months, until September." I
recommend un-cutting it: it's this page's subject, and today's fix closes it. If it stays cut,
miss 1 stands as drafted.

### BYR5 — How I caught it

> **H2:** Read it before fixing it, test it before believing it
>
> **1. A read-through, then a live check.** A later read-through took the invented foundation
> out, while the privacy page was rewritten in plain first person. The structured data kept the
> old framing for five more months. A check of what the live pages actually serve, made before
> this page was written, found it, and it was fixed that day. *(Falls under: never invent a date,
> a figure or an organisation; unknown means ask me · receipts-001, R-140, R-141)*
>
> **2. Reading the real thing before changing it.** The session that made the audit's fixes read
> the code and the live page first. The category held one unpublished post, so the fix became
> keeping any empty category out of search results. The image's empty text alternative was
> already there, so nothing needed doing. *(Falls under: say what you read, not what exists ·
> receipts-001, R-147, R-149)*
>
> **3. Testing from outside, before this page said "fixed".** A script fetched the site every six
> seconds, as a browser and as five AI agents, once with pages forced past the host's cache and
> once without. Everything cached came back. Past the cache, one agent was refused every time and
> two others some of the time. The refusals came from the host's own server, behind Cloudflare.
> *(Falls under: "done", "verified" and "deployed" are claims; prove them from outside ·
> receipts-001, R-150)*
>
> *Rules table:* three rows, one per miss.

| The correction | The standing rule | Enforced in |
|---|---|---|
| An analysis invented a charity for the site, and its schema outlived the correction (R-140, R-141) | Never invent a date, a figure or an organisation. Unknown means ask me | `CLAUDE.md` · rule 11 |
| An audit reported two problems that weren't there (R-147, R-149) | Say what you read, not what exists | `CLAUDE.md` · rule 6 |
| A host fix was recorded as done without a re-test (R-150) | "Done", "verified" and "deployed" are claims. Prove them from outside | `CLAUDE.md` · rule 2 |

Who caught what (the "I" rule):
- **1:** R-140 says "read-through (later audit; privacy rewrite)". The `bareyr` commit that
  removed it (`2e0eb63`, 2026-04-21) is co-authored by an AI. It doesn't say who spotted it, so
  it's impersonal. **Q-BYR4: did you catch the foundation yourself?** If so, 1 becomes "I read
  it", like the graph's sliders.
  - **Answered: "I don't know what you are referring to?"** No memory of it, so 1 stays
    impersonal. The live check that found R-141 was the agent's (handoff-019 step 1), so it's
    impersonal too.
- **2 and 3 were the agent's,** so they're impersonal. You asked for 3 ("2 yes"), but the
  refusals were found by the agent's test.

"Falls under", not "became", for all three:
- The truth rules were written on 2026-09-23 (`CLAUDE.md`), after misses 1 and 2.
- Miss 3 comes after them, but it didn't create rule 2.
- The rows link `tc-ventures-site/CLAUDE.md`, the public copy. BYR's own `CLAUDE.md` carries the
  same twenty rules (`bareyr` `fea5b2b`), but that repo is private.
- `/method` quotes rules 11 and 6 in this wording (rule 6 there also carries its example), so
  rows 1 and 2 match it. Rule 2 isn't on `/method`, so row 3 uses `CLAUDE.md`'s wording.

### BYR6 — What shipped

> **H2:** Readable by people and by software, with one gap left
>
> Every guide now tells software who wrote it and when it was last reviewed. It gives one
> breadcrumb trail instead of two. An empty category no longer appears in search results. The
> plain-language summary for AI tools, `llms.txt`, is linked from every page and from
> `robots.txt`. And the site no longer describes itself to software as a non-governmental
> organisation. (→ `handoff-012.md`, receipts-001 R-141)
>
> *~~Fig. 2~~: none (ruled 2026-09-26).*
>
> **The honest limits:** Checked in September 2026: the host still refuses some AI agents when a
> page isn't in its cache, and emptying the cache after an update reopens that gap. The filter is
> the host's, it sits behind Cloudflare, and it isn't fixed yet. The pages are also heavy for a
> phone on a rural connection, and that hasn't been worked on.

Checked live, 2026-09-25:
- one `BreadcrumbList` on each guide
- `<link rel="alternate" type="text/markdown" … href="…/llms.txt">` on the guides
- `robots.txt` ends "# Plain-language site summary for AI tools: https://bareyourrare.org/llms.txt"
- `/category/poems/` serves `noindex`

Other notes:
- **"Checked in September 2026"** dates the limit, so it won't become false when the host is
  fixed. It should still be updated then, like C-20.
- **Page weight** is the crawl audit's (g), still open (O-11g). "A rural connection" is the
  audit's point, not a new claim.
- **Fig. 2** needs you to look at the crop before it goes in (no symptom text). The alternative
  is no second figure. Say which.

### BYR7 — Receipts

- `plans/receipts-001.md` §3E (R-140, R-141, R-147 to R-150)
- `Claude outputs/byr-crawl-audit.md` (§1, §2, §3c, §3e, §5)
- `Claude outputs/byr-bot-check-2026-09-25.md`, and `scripts/byr_bot_check.py`
- `handoff-011.md` (§2 "Traps", §4 O-10, O-11)
- `handoff-012.md` (§4 O-11)
- `reviews/copy-review-004.md`, Q-BYR1 (the ask)
- `CLAUDE.md` (rules 2, 6, 11)
- the live site

All are in this repo, which is public. The `bareyr` repo is private, so it isn't linked.
**The two new files 404 on `main` until this branch is merged.** The preview's link check will
catch that.

### BYR8 — what goes with it (not copy)

1. **The page:** `public/work/bare-your-rare.html` (plan-001's path), built on the
   influence-graph pattern. The preview goes in `.assetsignore`, with the draft banner and
   `noindex`.
2. **The sub-menu:** its label is the H1. It goes second, after the graph and before the
   housing society, which is the `/projects` order (BYR is the first of "And four live sites").
   That's all ten files, plus the new one.
3. **P2** below: `/projects` and the home page link the case study, in the same push.
4. **The usual checklist:** sitemap; check-run, curl, console, 375px, keyboard; the site suite
   local and live.
5. **The check scripts from last session** (`site_check.py`, `ig_check.py`, `ig_shots.py`) were
   in that machine's scratchpad, not the repo (INFRA-13). They aren't here, so they get
   rewritten, into `scripts/` this time.
6. **The security policy** isn't changed. No new script.

### P2 — `/projects` and home: link the case study

> **`/projects`**, the BYR paragraph: unchanged, plus a final "Read the case study." linking
> `/work/bare-your-rare`, as the housing society's paragraph has.
>
> **Home**, the "Four live sites" card: "bareyourrare.org for rare-disease patients (read the case
> study)", as the housing society has.

### Open for Thomas (BYR)

- **Rule on:** BYR2b (A/B) · BYR3 · BYR4 as revised (and R-150) · BYR5 as revised · BYR6
  (Fig. 2 or none) · BYR7 · P2
- **Q-BYR5: the host filter.** It's at Hostinger, so it's your call. I recommend asking Hostinger
  support. Name the symptom: uncached requests from AI user-agents get a 429 or a LiteSpeed
  reCAPTCHA 403, through Cloudflare. And **ship the case study with the limit stated**, not
  waiting for Hostinger.
- ~~**Q-BYR7:** remove the four unclaimed social links from BYR's footer now? (BYR0 5)~~ Ruled yes, and
  done (see the rulings below).

### Rulings, BYR (Thomas, 2026-09-25)

**First round:** "1 yes, 2 yes, 3 yes, 5 yes", and Q-BYR1 (BYR2). Applied in BYR0.

**Second round, verbatim:**

"i did the lightspeed purge, Blocks: A...byr2 the idea started in March as I had to move content
from the old site to the child theme, prior I was building right in WordPress>blocks, Elementor,
etc. I wanted freedom to do things I couldn't or that were a pain in the butt because of the extra
weight handling the themes and plugins. Why pay for a plugin when I can ask you to make it my way
for my content? byr3 yes, byr4 I don't know what you are referring to? byr5 explain in greater
details. byr6 no, nobody has claimed them yet"

- **The purge:** done. Re-checked: O-13 is closed (BYR0 1).
- **"Blocks: A":** read as the two A/B choices then open. The H1 is A and the quote is A. The
  other blocks aren't ruled OK yet.
- **Q-BYR2:** March 2026 (BYR1). The rest of the answer became BYR2b.
- **Q-BYR3: yes.** R-141 is un-cut and is in BYR4 miss 1, BYR5 1 and BYR6.
- **Q-BYR4: doesn't recall.** Explained in the chat; 1 stays impersonal.
- **Q-BYR5: asked for more detail.** Explained in the chat; still open.
- **Q-BYR6: not his; the accounts are unclaimed.** That leads to Q-BYR7.

**Third round, verbatim (2026-09-26):** "byr2b A, rest ok, no fig 2, q-byr7 yes, q-byr5 what am i
asking hostinger for? explain it to me like you would to someone who hasn't heard a thing about
it."

- **BYR2b: A.** The second quote goes in with "[an AI]".
- **"rest ok":** BYR3, BYR4 (with R-150), BYR5, BYR6, BYR7 and P2 are OK as revised. R-150 is
  now OK in receipts-001.
- **No Fig. 2.** BYR6 has no second figure. Fig. 1, the code excerpt, stays.
- **Q-BYR7: yes.** `bareyr` `ed6b054` removes the footer's four social links. It also removes the
  lightbox share row's Instagram button, which linked the same unclaimed profile: same problem,
  same fix. PHP lints clean and the JS parses. Checked live after the push; see below.
- **Q-BYR5: explained again in the chat, from scratch.** It's still open, and the copy doesn't
  wait on it: BYR6's limit is stated and dated either way.

**Q-BYR7, checked live 2026-09-26:**
- Uncached `/about/` and `/hcs-guide/` carry no link to `x.com/bareyourrare`. `/about/` had one in
  the post-purge re-check the night before, so the check can fail.
- The lightbox script LiteSpeed serves (its optimised copy) has no `instagram.com/bareyourrare`
  and no `shareInstagram`. Its X share intent is still there.
- **Pages already in LiteSpeed's cache keep the old footer until the next purge. Thomas: purge
  again.**

**Preview built 2026-09-26:** `public/work/bare-your-rare.html`, with a draft banner and
`noindex`, and listed in `.assetsignore`. It's built from the ruled copy; the `/projects` paragraph
is copied unchanged.
- **The sub-menu** lists this page second, after the graph and before the housing society, on
  this page only. The other ten files change at ship.
- **Copy matches the ruled blocks,** checked by script sentence by sentence. The only misses were
  expected: editorial notes, the unruled quote B, sentences whose "(→ …)" became a receipt link,
  and tag spacing. A one-word change is caught, so the check can fail.
- **Fig. 1 carries no "Fig. 1" label.** The site numbers only screenshot figures (`.shot`), the
  same as the graph page's excerpt. With Fig. 2 ruled out, the page has no numbered figures.
- **The rules table's "Enforced in"** is plain `CLAUDE.md`, as on the graph page. The receipts list
  links it.
- **Receipt labels** (the left column of Receipts) are new wording, not in BYR7's file list. They
  describe the files; worth a glance.

Checked locally in headless Chromium with the new `scripts/cs_check.py`: 16 of 17 passed.
- **Passed:**
  - status, and a made-up URL gives 404
  - title, noindex and the banner
  - the six sections in order
  - the sub-menu order and both `aria-current` levels
  - by keyboard: Tab reaches the toggle, Enter opens, Esc closes and returns focus
  - no console errors in light or dark
  - no sideways scroll at 375px
  - with JavaScript off, every section, link and word is present
- **Negative control:** run against `/work/gprs` as if it were a preview, the script fails the
  preview checks and the sub-menu order. So those checks can fail. The run also showed that
  `/work/gprs`'s `<title>` has a straight apostrophe where its H1 has a curly one. That's
  cosmetic and was left alone.
- **The one failure is three links, and none of them is a fault on the page:**
  - the check file and its script 404 on `main` because they're only on this branch. They
    resolve when it merges.
  - `github.com/DriftingSplash9` got a 403 from this container's proxy, which refuses GitHub pages
    outside the session's repos ("sessions are bound to their configured repositories"). That's
    rule 7: it describes my network, not the site. The same footer link is on every live page.
- **Looked at:** each section at 1280px in light and dark, the excerpt and rules table in both
  themes, and the header at 375px. Nothing overlaps or runs off the page.
- **Not checked:** the live security policy, since `_headers` isn't served locally. The page adds
  no script, so the policy isn't touched.

**Open before it ships:** Thomas's "ship it". Then BYR8's checklist and P2, on the ten other files.

**Q-BYR5, the Hostinger toggle (2026-09-26):** Thomas turned off "Create LLMs.txt file" in the
Hostinger plugin, thinking it caused the refusals. It didn't:
- Re-tested after the change, BYR still refused GPTBot on every uncached request, and PerplexityBot
  and a browser once each.
- GPRS, with the toggle off and no Cloudflare, refused GPTBot the same way and dropped some
  connections outright.

Details: `byr-bot-check-2026-09-25.md`, addendum 2. BYR6's honest limit stands as written. The
toggle is still worth leaving off, because switching it on replaces the hand-written `llms.txt`.

**Q-BYR5 closed (Thomas, 2026-09-26): "1".** The choice is option 1: leave it as it is. Hostinger
support confirmed the 429 is their server-wide rate limiter, with no customer setting on shared
hosting (bot-check file, addendum 6). Two things stand:
- the LiteSpeed crawler, now hourly, keeps the pages cached
- BYR6's honest limit, as written

No Cloudflare HTML caching for now. The copy doesn't change.


**Shipped (Thomas, 2026-09-26: "ship it").** What changed with the ship:
- noindex and the draft banner are off the page
- the page is out of `.assetsignore`
- it is in the Projects sub-menu on all eleven pages, second after the graph
- it is in the sitemap
- it is linked from `/projects` (P2) and from the home page

Checked locally before the push:
- `scripts/site_check.py` passes every check on every sitemap page plus /404
- the same suite run against main's `public/` fails the sub-menu on all nine of its pages, which
  shows the check can fail
- `scripts/cs_check.py work/bare-your-rare` passes everything except three links: the two GitHub
  blob links to files that are only on this branch until it merges, and the GitHub profile, which
  this session's proxy refuses

The live check comes after the deploy.
