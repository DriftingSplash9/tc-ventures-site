# handoff-015 — tc-ventures.ca

**Written:** 2026-09-22, finalised 2026-09-23
**Covers:** a baseline audit and action plan (Phases 0–4), **Phase 0 shipped**, the home
page rewritten from copy-review-002, the template approved, brief-001 redacted, and the
résumé and LinkedIn brought in line with the site.
**Status at wrap:** everything in §2 is **deployed and verified live** except the résumé
work, which is **on disk and committed; the PDF has not been exported yet** (C-15).
**The next job is Phase 1**, starting with the receipts inventory. See §6.

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. §2 "Traps" before you touch git, grep, headers, DNS or a rebuild.
2. **`plans/plan-001-showcase.md`** — the plan. The audit's Phases 0–4 slot into it
   (PL-6); they do not replace it. Nothing gets built outside it without Thomas agreeing.
3. `claude/thomas-study.md` in the Claude project "TC 'Ventures" — the voice study.
4. `claude/tc-ventures-site-decisions.md` in the same project.
5. `reviews/copy-review-001.md` and `reviews/copy-review-002.md` — his rulings, and the
   format every copy review uses.
6. `public/work/_template.html` — the approved case-study template (preview locally; it
   does not deploy).
7. `README.md`.
8. If the job is GPRS, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md` instead.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**.

**How Thomas works (this session):** he wants short answers when he asks for them, is
blunt when you are wrong ("idk what you are smoking" = you asserted something from an
incomplete read), and makes the calls himself. Recommend one option; don't survey.

---

## 1. What this is

**tc-ventures.ca** — Thomas Cheesman's hiring-facing portfolio. Hand-written
static HTML, no framework, no build step, no CMS. Cloudflare Workers static
assets, deploy-on-push from GitHub. Deliberately separate from thomascheesman.ca.

| | |
|---|---|
| Repo | `DriftingSplash9/tc-ventures-site` — **public** |
| Local | `C:\Users\thoma\Desktop\My Files\Website Projects\tc-ventures site` |
| Host | Cloudflare Worker `tc-ventures-site` (static assets only) |
| Config | `wrangler.jsonc` → serves `./public`, `404-page`, `workers_dev: false`, `preview_urls: false` |
| Deploy | commit + push to `main` → Cloudflare builds. **No cache to purge.** |
| Contact email | `thomas@tc-ventures.ca` |
| Pages | `index`, `projects`, `background`, `contact`, `404`. Internal links, canonicals and sitemap use **clean URLs** (`/projects`); `/x.html` 307s to `/x`. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html` and `og-src/` off the live site. Both 404 live. |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. Reasons are commented in the file. |
| Link preview | `assets/img/og-card.png` 1200×630 on all four pages, with the R2 headline. Source `public/og-src/og.html`; re-render command in its `<style>` comment (needs a local server on :8788). |
| Analytics | Cloudflare Web Analytics, injected at the edge. The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` + the audit phases (PL-6) |
| Design system | `public/assets/style.css` — tokens in `:root`, case-study components under the `CASE STUDIES` banner at the end |
| Graph demo | `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js` |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. Thomas edits it himself. |
| Sister repo | `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` (thomascheesman.ca). Not connected by default; request access. |

## 2. What was done (2026-09-22 → 23, after handoff-014)

**Audit.** Thomas asked for a brutally honest audit and a plan to make the site
"Awwwards worthy". Baseline (rough, Awwwards weights): Design 5, Usability 7,
Creativity 3.5, Content 7, **about 5.3**. Findings: the site asserts the method and
never shows it; the home page undersold ("for practice") and named four roles; the
planning ran well ahead of what had shipped. The plan: Phase 0 quick wins → Phase 1
proof (receipts, two case studies, `/method`) → Phase 2 the build ledger as home hero
→ Phase 3 craft (motion, type, built-in accessibility controls) → Phase 4 engineering
pass and award submissions. Direction ruled: see PL-6.

**Shipped and verified live:**
- Clean URLs everywhere (nav, canonicals, `og:url`, sitemap).
- `public/_headers`; contact's inline script moved to `public/assets/contact.js`.
- `.assetsignore` (template + `og-src/` off the live site). INFRA-7 closed.
- New link-preview card, `og:image:width/height/alt` on all four pages.
- LinkedIn first in every footer's "Elsewhere" list.
- **Home page from copy-review-002:** R1 A (title/og:title "websites and digital
  operations for nonprofits"), R2 A (H1 "I run a nonprofit's website, and I hold it to
  a written standard."; name moved to the label; `.hero h1 { max-width: 20ch; }`), R3,
  **R4 in Thomas's own words** (only edit: "straightforward" as one word), R5, R6.
- CSP fix for the analytics beacon (see traps). Beacon verified loading (200) live.
- 3D graph verified working live under the CSP.

**On disk and committed, not fully shipped:**
- **Template approved** by Thomas. All four `[Confirm…]` brackets resolved; "the ask"
  paragraph is **Claude's suggestion** (PL-4).
- **`briefs/brief-001…md` redacted** (lander, exact counts, "hand and arm pain"),
  marked `[redacted: …]` with a dated note. Git history still has the original.
- **Résumé docx + html:** summary follows R3–R6; LinkedIn on the contact line; Ric's /
  Township 71 split into two entries with Thomas's dates (C-16). Word test export:
  **2 pages**. The served PDF is still the **2026-09-21 export** (C-15).

**Outside this repo (Thomas's, private):**
- LinkedIn rebuilt by Thomas from a Claude draft at
  `Family & Personal\resume\LinkedIn-profile-draft-2026-09-22.md` (**deliberately not in
  this public repo**; it quotes his old profile). Thomas reports LinkedIn **done**. The
  Services "About" text and headline were given in chat.

**Closed this session:** INFRA-7, INFRA-8, C-11 (html has the Power Engineering line),
C-12, C-14, PL-3, PL-5.

### Traps worth knowing

- **Cloudflare injects scripts at the edge** (the Web Analytics beacon). A CSP that
  passes on a local server can still break things live; it silently killed analytics
  for one deploy. After any CSP change, load the live site and read the console.
- **Browser console logs persist across navigations** in the built-in browser. A stale
  CSP error can look current; check `performance.getEntriesByType('resource')` or
  the live header with `curl -sI` instead.
- **The 3D graph bundle contains `new Function`** (ngraph). The d3 engine never calls
  it, so `script-src` needs no `'unsafe-eval'`. An EvalError would mean that changed.
- **Any new inline `<script>` is blocked by the CSP.** Put it in `/assets/*.js`.
- **LinkedIn lazy-loads profile sections.** Reading it via `get_page_text` without
  scrolling to the bottom missed the About section and most of Experience, and Claude
  wrongly told Thomas they were missing. Scroll the whole page first, or say "I could
  not see X", never "X is missing".
- **Python heredocs through Git Bash eat backslashes in Windows paths** (`\r` in
  `\resume` became a carriage return, twice). Write paths with `chr(92)` or put the
  script in a file; grep the result.
- **Headless Chrome renders dark mode**; `og-src/og.html` therefore declares only
  `@font-face`, not `style.css`. An HTML comment inside `<style>` kills the next rule.
- **Grep, don't count from memory:** the template had four `[Confirm…]` brackets, not three.
- **python-docx edits keep formatting** when you change `runs[0].text` on
  single-run paragraphs. New résumé entries were made by `deepcopy` of an existing
  title/meta/bullet paragraph. Check page count with Word COM export
  (`ComputeStatistics(2)`), then render with PyMuPDF (`fitz`) to look.
- **The repo is public.** Anything that quotes Thomas's private profiles, health
  detail, family or old résumés goes in `Family & Personal\`, not here.
- **`.cs-section > *`** is one class of specificity on purpose; the rail index is in the
  HTML twice on purpose; case-study-only CSS is scoped under `.cs-body`; lazy images
  render black in full-page headless shots. (Carried from 014.)

## 3. Current design

Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
`prefers-color-scheme`. Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
Confirmed; stop re-litigating it.

**Case-study layout (approved 2026-09-22):** wide lane (1040px) for headers, figures,
tables and lists; reading lane (66ch) for prose; a sticky side rail (200px) at ≥1180px
carrying the six-section index, folding into a horizontal index below that. Sections
auto-numbered from CSS counters; figures `Fig. N` per page; receipts are small mono
links with a leading `→`. Six fixed sections: The ask · The standard · What the AI got
wrong · How I caught it · What shipped · Receipts.

**Home page (live 2026-09-22):** label "Thomas Cheesman · Grande Prairie, Alberta ·
remote"; H1 "I run a nonprofit's website, and I hold it to a written standard."; lede
from R3/R4. The lede is now four sentences in a 34ch column — tall on desktop; a
Phase 3 layout job, not a copy one.

**Standing rules:**
- **The Rocket Lander is private.** Not here, in any form.
- `object-fit: contain`, never `cover`.
- **Content renders without JavaScript.** JS is allowed on top (motion, 3D, controls);
  the words and links must not depend on it. No dependencies or build step — prebuilt
  bundles copied into `assets/` only.
- Fonts self-hosted. No third-party font request.
- No phone number on the site. It is in the résumé PDF.
- **Never publish an exact node, edge, report or grade count** *in copy*. Round or
  describe. The application screenshot on Projects is the one ruled exception.
- **No vanity metrics.** No line counts.
- **Do not invent dates or figures.** Unknown → ask Thomas.
- Hajdu-Cheney syndrome is named on purpose. Symptom detail is not.
- WordPress stays once per spec table as a hiring keyword; out of headline prose.
- **Nothing familial**, except the ruled Back Quarter childhood paragraph. Children's
  names never, including inside screenshots.
- **Lead role: nonprofit website and digital operations.** Web development and
  accessibility are named once, as secondary (R6).
- **The résumé source is the Word file.** `resume-source.html` mirrors it — change
  both. Never edit the PDF. **Exactly two pages.** Thomas exports the PDF.
- Melanie and Thomas are "the parents" of the three children, never "co-parents".
- **New CSS is additive and token-based.** Case-study-only CSS under `.cs-body` / `.cs-*`.
- **Never ship a link that 404s**, including nav links to planned pages.
- **Copy ships only through a copy review** in the copy-review-001/002 format
  (numbered blocks; OK / KEEP / A / B / FIX / CUT). Template copy is not site copy.
- **Accessibility controls are built in, never an overlay widget** (PL-6).

**Demo and embed rules:** nothing heavy loads before a click; a gated page degrades
when the payload is absent; the 3D canvas keeps its own dark ground; `basis` is quoted,
never paraphrased; the written chain under the graph is the accessible equivalent;
nothing rearranges a layout on interaction; **show finished work** — unfinished work is
labelled honestly or left off.

## 4. Open items — carry these forward until closed

### PLAN
| # | Item | Notes |
|---|---|---|
| PL-2 | **Receipts inventory — the next job** | See §6. List every real "AI got it wrong / how it was caught" story with its file, section and date. **Never invent one.** Feeds every case study and `/method`. |
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Novel design and motion are in scope. Accessibility controls (motion full/reduced/off, theme, contrast, text size) are **built into the site**; OS preferences are the defaults, toggles override and persist. Order: **Phase 1** (receipts → `/work/gprs` + `/work/this-site` → `/method`) → Phase 2 (build ledger as home hero, static SVG) → Phase 3 (craft; **proposal first**, build after his yes) → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers: lead role nonprofit technology; home wow = the build ledger; curated process excerpts allowed; GPRS gets its own case study; page-weight/a11y results shown once inside `/work/this-site`. |
| PL-4 | **"The ask" paragraph in `_template.html` §01 is Claude's wording** | Thomas said FIX and asked for a suggestion. Confirm it in the `/work/this-site` copy review before it ships. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-15 | **Résumé PDF not yet exported** | Docx is final (2 pages in Word's own count). Thomas exports it and replaces `public/assets/Thomas-Cheesman-Resume.pdf` **and** `Family & Personal\resume\Thomas_Cheesman_Resume.pdf`, then pushes. As of 2026-09-23 both are still the 2026-09-21 export (md5 `86e947b7…`). Cosmetic: the summary ends on a one-word line ("roles."). |
| C-16 | **Job history, from Thomas 2026-09-23 — use these** | GPRS board: elected at the **June 2023** AGM (first meeting September). Majors consulting: May 2019 – **June 2020**. **Head Chef, Ric's Grill, Sep 2013 – Jul 2014.** **Executive Chef, Township 71, Jul 2014 – Jun 2015** (renovation from Oct 2014, opened Nov 2014, closed May 2015, wind-down through June). **Taught one GPRC semester, Sep – Dec 2014**, during the Ric's-to-T71 transition. Résumé docx and html carry this. |
| C-13 | GPRS site history | First version on WordPress.com in 2023; rebuilt in 2025 as self-hosted WordPress.org on Hostinger "because I wanted more freedom to experiment with the code." For `/work/gprs`. No month-level dates without asking. |
| C-17 | R4 wording, his call | Live: "…then build it with help writing by AI." Could read as AI writing the words, not the code. Offered "…with AI writing the code" once; **do not raise it again or change it unasked.** |
| C-9 | `page-thomas.php` ~2010: "I couldn't get past my kitchen manager" | His prose and his call — flag it, do not rewrite it. |

### PROJECTS / GRAPH
| # | Item | Notes |
|---|---|---|
| P-6 | A fourth project? | Nothing queued; show finished work only. |
| G-6 | Demo still is a headless render | Thomas screenshots the live demo if he wants a hand-framed one. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass — deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Candidates for that run: Projects, the live graph, the template's `.loop__scroll`. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address. |
| INFRA-6 | Dead lander CSS in `style.css` (search `lander embed`) | Delete if still unused by mid-October 2026. |
| INFRA-9 | HSTS 1 yr, no `includeSubDomains`, no `preload` | Deliberate; both are hard to undo. |
| INFRA-10 | LinkedIn Post Inspector | Thomas was shown how (paste `https://tc-ventures.ca` at linkedin.com/post-inspector, Inspect). Not confirmed run. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | Harmless; detach when convenient. |
| D-2 | WP.com plan auto-renew | Do not cancel without confirming DNS for the live sites is unaffected. |
| D-3 | **Professional Email renewal — due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link given: `https://wordpress.com/checkout/renew/27350377`. Confirm it is paid. |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-2 | `/projects` third-person leakage on thomascheesman.ca | Thomas is writing this himself. |
| O-4 | bareyourrare history contains `permits/` and `3.jpg` | Instructions in `_Quarantine\bareyourrare-history-purge.md`. Thomas runs it. |
| O-5 | `bareyr\.git` lock-file junk | Cosmetic; Thomas deletes. |
| O-6 | Rocket Lander repo not public | On hold with the lander. |
| O-7 | Children's names in the Back Quarter world | **Thomas ruled: leave them.** They stay off this site regardless. |
| O-8 | thomascheesman.ca's open items live in `V0.42.md` | `three-r128.min.js` idle-loads for every visitor; the mouse wheel over a live stage does not scroll the page. |
| O-9 | `page-hcs.php` Keg paragraph — on disk, not deployed | Thomas pushes the theme and purges all three caches (Cloudflare, Hostinger CDN, LiteSpeed). |
| O-10 | bareyourrare.org and thomascheesman.ca behind Cloudflare since 2026-09-20 | thomascheesman.ca has three cache layers. gpresidentialsociety.com was not moved (external DNS). Full detail in handoff-014 §4. |
| O-11 | bareyourrare.org crawl audit — mostly deployed | `Claude outputs/byr-crawl-audit.md`. Still open: (g) page weight. |
| O-12 | GPRS work has its own handoff | `GPRS Organization/00 Working Notes/gprs-handoff-001.md`. |

## 5. HOW TO WRITE THE NEXT HANDOFF

**This section is fixed. Copy it forward verbatim into every handoff.**

### Naming and location

- Handoffs live at repo root: `handoff-001.md`, `handoff-002.md`, `handoff-003.md`…
- **Zero-padded to three digits.** Sequential, never reused, never renumbered.
- One handoff per meaningful session. A session that changed nothing does not earn one.
- **The highest-numbered file is the only current one.** Everything below it is
  history. Do not read old handoffs unless you are chasing why a decision was made.

### Forking

Work will fork — design, contact page, the graph embed, the Godot build, copy.
**Do not fork the file series.** Numbering stays one straight line. Instead:

- Every open item carries a **workstream tag** in SCREAMING-CASE: `DESIGN`,
  `CONTACT`, `GRAPH`, `LANDER`, `COPY`, `INFRA`, `DOMAIN`.
- §4 (open items) is grouped by tag once there is more than one tag in play.
- If two agents work in parallel, each writes its own numbered handoff and the
  later one merges the earlier one's open items into its §4. Nothing is dropped
  silently — an item leaves §4 only when it is **done** or **explicitly killed by
  Thomas**, and the handoff says which.

### Required sections

Every handoff has these, in this order, with these numbers:

```
0. Read this first if you are a fresh agent
1. What this is            — stack table. Update only when the stack changes.
2. What was done           — THIS SESSION only. Not a changelog of all time.
3. Current design          — the rules a new agent would otherwise break.
4. Open items              — the table. Tagged. Carried forward.
5. HOW TO WRITE THE NEXT HANDOFF   — verbatim copy of this section.
6. Next up                 — what the next agent should actually do, in order.
```

### Rules

- **State, not narrative.** "The X is broken because Y" beats a story about
  discovering it. Nobody needs your journey.
- **Traps are worth more than successes.** If something cost you an hour, write it
  down in one sentence so it costs the next agent nothing. The stale-clone and
  `index.lock` notes in handoff-001 §2 are the model.
- **Never claim something is done that you have not verified.** "Deployed" means you
  saw it serve. "Written" means it is on disk. Say which.
- **Do not state git state and do not tell Thomas to commit.** That is his routine.
- Keep it under ~400 lines. If §2 is getting long, you are writing a diary.

## 6. Next up — Phase 1

Before anything: remind Thomas once of **C-15** (résumé PDF) and **D-3** (email renewal,
8 October) if still open. Then Phase 1, in this order. Each step ends with Thomas's
ruling before the next starts.

### Step 1 — the receipts inventory (PL-2, plan session 1)

**Output:** `plans/receipts-001.md`. The repo is public, so the inventory is curated:
nothing familial, no health detail beyond the named condition, nothing from private
files quoted. If a good story lives only in a private file, list it as "private
source — needs Thomas's OK" without quoting it.

**One entry per real miss**, as a table row:
`ID · date · project · what the AI got wrong (one line) · kind of miss · how it was
caught (measurement / validator / read-through / live check / Thomas) · the rule it
became · receipt (file + section, public URL if public) · public-safe? (Y / needs OK)`

**Kinds of miss to tag:** looked right but was not measured · plausible but invented
fact · drift across sessions · over-polish / selling · incomplete read asserted as
absence · privacy leak · tooling error.

**Sources, in this order:**
1. `handoff-001.md` … `handoff-015.md` — every §2 "Traps" list and every correction
   story. (This is the one time a fresh agent *should* read old handoffs.)
2. `reviews/copy-review-001.md` and `-002.md` — the FLAGs and his rulings.
3. `briefs/brief-001…md` (redacted) and `plans/plan-001-showcase.md` §1.
4. `C:\Users\thoma\Desktop\My Files\Reports Clustering\` — `PLAYBOOK*.md`,
   `HANDOFF.md`, `validate.bat` and the validator in `scripts/`, and `notes/`
   (`doc-audit-*`, `grader-rulings-*`, `camera-fit-measurement-*`,
   `flicker-tests-*`). The home page's "calibrated against a measurement script with a
   bug in it" story should be traceable to one of these; find its receipt or flag it.
   **Separate repo: request access to the folder first.**
5. `Claude outputs/byr-crawl-audit.md` — the host-level fault found by live fetch.
6. `tc-ventures-child-theme\V0.*.md` — needs directory access; ask first.

**Real candidates from this session (verify each against this file before listing):**
- The CSP passed locally and blocked Cloudflare's analytics beacon live. Caught by
  reading the live console. Rule: after any CSP change, check live.
- Claude told Thomas his LinkedIn had no About section. It did; the read was
  incomplete (lazy-loaded page). Caught by Thomas. Rule: say "could not see", never
  "missing".
- brief-001, a public receipt, contained symptom detail. Caught on the redaction
  read-through. Rule: every receipt is read against the privacy rules before it links.
- The template had four confirmation brackets; the working count was three. Caught by
  an assertion in the edit script. Rule: grep, don't count from memory.
- Windows paths lost a backslash in scripted edits (twice). Caught by grepping the result.

**Target:** enough receipts that each case study has 2–3 real misses with
catches. Then show Thomas the inventory for OK / CUT per row, copy-review style.

### Step 2 — two case studies, not seven

From `public/work/_template.html` (approved): **`/work/gprs`** first (closest to the
lead role; C-13 history; the MEM fire/rebuild period), then **`/work/this-site`**
(handoffs, rules, reviews; PL-4's "ask" paragraph; page weight and accessibility
results shown once here, measured, never typed). Draft copy only from the inventory
and ruled facts, then **copy-review-003** before anything ships. Adding `/work/` pages
means: sitemap entries, nav decision (no link to an unbuilt page), and removing the
template's `.draft` banner on the real pages.

### Step 3 — `/method`

Plan-001 §4b: the loop diagram (inline SVG, both themes), handoffs, the
rules-from-corrections table (every row with a receipt), validators over vibes, and
"where AI is weak and what I do about it". Copy review before it ships.

### After Phase 1

Phase 2 (build ledger) and Phase 3 (the motion/accessibility-controls proposal) per
PL-6. **Propose before building.**
