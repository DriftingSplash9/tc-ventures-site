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

**Still open before it ships:** Q-IG4 (Brics / BRICS) and Q-IG5. Then it ships on IG8's
checklist, plus P1 and Q-IG3, when Thomas says so. Noticed, left for the design phase: the demo's
paragraph sits tight against its frame, the same as on `/projects`.
