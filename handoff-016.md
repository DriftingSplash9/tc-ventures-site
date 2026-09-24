# handoff-016 — tc-ventures.ca

**Written:** 2026-09-24
**Covers:** Phase 1 step 1 closed (receipts inventory ruled, the twenty truth rules, the
top-ten write-up, the operating guide), and step 2 half done: **`/work/gprs` shipped** and is
linked from the home page and Projects.
**Status at wrap:** everything in §2 marked "live" was **deployed and verified live** (curl
from outside, plus a headless render of the live page). **The next job is `/work/this-site`.**
See §6.

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. §2 "Traps" before you touch git, grep, headers, DNS, a rebuild
   or a screenshot.
2. `CLAUDE.md` at repo root: the twenty truth rules. `plans/operating-guide.md` is how
   Thomas and the AI divide the work.
3. **`plans/plan-001-showcase.md`**: the plan. The audit's Phases 0–4 slot into it (PL-6).
   Nothing gets built outside it without Thomas agreeing.
4. **`plans/receipts-001.md`**: the ruled inventory. Only rows ruled **OK** may be used in
   copy; §2 findings F-1 to F-4 are ruled; §6 is the pre-sorted rules table for `/method`.
5. `reviews/copy-review-003.md`: the live review for Phase 1 copy (R1, G1–G9 ruled).
   Earlier reviews 001/002 set the format.
6. `public/work/gprs.html`: the first shipped case study. **Copy its structure** for the
   next one; `public/work/_template.html` still holds the draft `/work/this-site` sample copy.
7. `claude/thomas-study.md` and `claude/tc-ventures-site-decisions.md` in the Claude
   project "TC 'Ventures" (voice study, decisions). Not read this session.
8. `README.md`.
9. If the job is GPRS itself, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md`.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**.

**How Thomas works:** short answers when he asks for them; blunt when you are wrong;
makes the calls himself. Recommend one option; don't survey. He answers reviews tersely
("G3 A, OK to ship"), and that is a full ruling. He is self-taught and deliberately
model-agnostic (he treats the leading models as cars constantly overtaking each other), so
explain methods, not one model's tricks.

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
| Pages | `index`, `projects`, `background`, `contact`, `404`, **`work/gprs`** (case study, live 2026-09-24). Internal links, canonicals and sitemap use **clean URLs** (`/projects`); `/x.html` 307s to `/x`. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html` and `og-src/` off the live site. Both 404 live. |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. Reasons are commented in the file. |
| Link preview | `assets/img/og-card.png` 1200×630 on all four pages, with the R2 headline. Source `public/og-src/og.html`; re-render command in its `<style>` comment (needs a local server on :8788). |
| Analytics | Cloudflare Web Analytics, injected at the edge. The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` + the audit phases (PL-6) · receipts `plans/receipts-001.md` (ruled) · `plans/operating-guide.md` |
| Design system | `public/assets/style.css` — tokens in `:root`, case-study components under the `CASE STUDIES` banner at the end |
| Graph demo | `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js` |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. Thomas edits it himself. |
| Sister repo | `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` (thomascheesman.ca). Not connected by default; request access. |

## 2. What was done (2026-09-23 → 24, after handoff-015)

**Phase 1 step 1 — receipts inventory (PL-2): closed.**
- `plans/receipts-001.md`: 112 distinct receipted misses from about 450 documents across
  six projects. **Ruled by Thomas 2026-09-23 via `receipts-001.xlsx`: 36 OK, 76 CUT; every
  private (P) row CUT.** OK rows by section (counted with a script): 3A GPRS 2 · 3B this
  site 7 · 3C Reports Clustering 22 · 3D thomascheesman.ca 3 · 3E BareYourRare 2.
- Findings ruled: **F-1** the home "measurement script" sentence overstated its receipt, so
  it was rewritten (copy-review-003 R1); **live, verified 2026-09-24**. **F-2** never name the
  outside research model in site copy. **F-3** counts only rounded. **F-4** GPRS is thin
  because it predates session records; Thomas: leave it thin.
- `CLAUDE.md` (new, repo root): the twenty truth rules, distilled from the inventory.
  Also added to the GPRS repo's `CLAUDE.md`.
- `plans/top-ten-receipts.md`: ten receipts written up for a general reader.
- `plans/operating-guide.md`: how Thomas and the AI work; `CLAUDE.md` points to it.

**Phase 1 step 2 — `/work/gprs`: live.**
- Copy drafted in `reviews/copy-review-003.md` G1–G8 from the two OK GPRS receipts (R-001,
  R-007), live Projects/Background copy, C-13 and the public GPRS repo. All ruled 2026-09-24
  (rulings recorded at the end of the review). Notable: **"The ask" pull quote is Thomas's
  own line** (Q-G1); **R-007 links `AGENTS.md`, not commit `5a68be4`**, whose message tells
  the board-motion story (G4 B); the claim that the audit prompt changed *because of* the
  bad audit was **cut**, because Thomas doesn't recall (Q-G2).
- Figures: `assets/img/gprs-home.webp`, `gprs-rebuild.webp`: headless Chrome, 1280×720,
  light scheme, live GPRS pages, 2026-09-24. No people. The home hero's named quote
  (Travis McNally, 2004) was ruled fine.
- Shipped with title/description/OG from G1, in the sitemap, linked from Projects' GPRS
  paragraph and from the home "Four live sites" card ("read the case study", G9). **Not in
  the menu**; see PL-7.
- **Verified live 2026-09-24:** page, both images and every outbound link return 200 (LinkedIn
  answers 999 to scripts, which is its bot block, not a dead link); `/work/gprs.html` 307s to
  the clean URL; no `noindex`, no draft banner; console clean; analytics beacon loads under
  the CSP; a headless render of the live page and of the live home card looked right; at
  375px nothing overflows.

**Other:** C-15 résumé PDF: the served PDF was replaced 2026-09-23 (commit `bfb4ec6`); the
live file's md5 `0da7af62…` matches the repo and differs from the 09-21 export. The private
copy in `Family & Personal\resume\` was not checked.

### Traps worth knowing

- **Cloudflare Workers Builds can take 7–10 minutes just to start.** For that window the
  site looks like the push silently failed (404 on new pages, old sitemap). Check the build
  before diagnosing: `gh api repos/DriftingSplash9/tc-ventures-site/commits/<sha>/check-runs`
  (empty = not started; then `in_progress`; then `completed success`). Then curl.
- **The built-in browser pane can be hidden.** `document.visibilityState` is `"hidden"`,
  `innerWidth` is 0, lazy images never load, and every overflow check reports true.
  Screenshots come back blank. Don't trust layout numbers from a hidden pane; check
  `visibilityState` first, or use headless Chrome.
- **Headless Chrome has a minimum window width (~500px).** A `--window-size=390,…` shot is
  laid out wider and then clipped, so text looks cut off at the right edge. For phone
  width, use the browser pane's `mobile` preset and measure `scrollWidth`.
- **Lazy images render black in tall headless shots** unless they're near the top at phone
  width. A 1280×5200 window loads them on desktop.
- **`--blink-settings=preferredColorScheme=1`** makes headless Chrome render light mode
  (it defaults to dark).
- **A local `python -m http.server 8788` started from Git Bash survives `pkill`.** Stop it
  with PowerShell `Stop-Process -Id <pid>` (find the pid with `netstat -ano | grep :8788`).
  Port 8788 is also the og-card re-render port; don't leave it held.
- **A receipt's "rule it became" can be wrong about timing.** R-001's rule text exists in
  the audit prompt, but nothing shows it was added *because of* the miss. Before copy says
  "X became the rule", confirm the rule came after the miss, or say only that it is the rule now.
- **Linking a commit links its message.** A receipt that is safe can sit in a commit whose
  message isn't. Read the whole commit before linking it.
- **The repo is public.** Anything that quotes Thomas's private profiles, health detail,
  family or old résumés goes in `Family & Personal\`, not here.
- **`.cs-section > *`** is one class of specificity on purpose; the rail index is in the
  HTML twice on purpose; case-study-only CSS is scoped under `.cs-body`.
- Carried from 015 and still true: Cloudflare injects the analytics beacon at the edge, so
  after any CSP change read the live console; console logs persist across navigations in
  the built-in browser; any new inline `<script>` is blocked by the CSP; Python heredocs
  through Git Bash eat backslashes in Windows paths; grep, don't count from memory.

## 3. Current design

**Case studies live:** `/work/gprs` (2026-09-24). It is the reference implementation of
the template: six fixed sections, receipts as small mono links, figures in `.shot--pair`.
Every claim in "What the AI got wrong" and "How I caught it" links to a receipt that
returns 200 publicly, or is cut.

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
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Accessibility controls (motion full/reduced/off, theme, contrast, text size) are **built into the site**; OS preferences are the defaults, toggles override and persist. Order: **Phase 1** (receipts ✓ → `/work/gprs` ✓ + `/work/this-site` → `/method`) → Phase 2 (build ledger as home hero, static SVG) → Phase 3 (craft; **proposal first**) → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). |
| PL-7 | **"Work" in the menu waits for `/work/`** | Ruled 2026-09-24 (G9 A): no menu item until a `/work/` index exists, after `/work/this-site`. Until then `/work/gprs` is reached from the home "Four live sites" card and Projects. The case-study rail's "← All work" points at `/projects`. Plan-001 §3: `/projects` later becomes a redirect to `/work/`. |
| PL-4 | **"The ask" paragraph in `_template.html` §01 is Claude's wording** | Confirm it in the `/work/this-site` copy review before it ships. |
| PL-8 | **Page-weight / a11y numbers for `/work/this-site`** | Plan-001 §6 Q5: shown once, "measured by the budget script in §4e, never typed by hand". **The budget script doesn't exist yet.** Build it first, or ship this-site without the numbers. Ask Thomas. |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-18 | **copy-review-003 is the Phase 1 review** | R1 and G1–G9 ruled. Add `/work/this-site` blocks next, then `/method`. |
| C-19 | **Q-G2 unresolved: when did "read the actual code" enter the audit prompt?** | Thomas doesn't recall. The live page makes no causal claim. Don't reintroduce one. |
| C-15 | Résumé PDF: **site copy done**, private copy unchecked | Served PDF replaced 2026-09-23 (md5 `0da7af62…`, matches repo). Not checked: `Family & Personal\resume\Thomas_Cheesman_Resume.pdf`. Cosmetic: summary ends on a one-word line ("roles."). |
| C-16 | **Job history, from Thomas 2026-09-23. Use these** | GPRS board: elected at the **June 2023** AGM (first meeting September). Majors consulting: May 2019 – **June 2020**. **Head Chef, Ric's Grill, Sep 2013 – Jul 2014.** **Executive Chef, Township 71, Jul 2014 – Jun 2015** (renovation from Oct 2014, opened Nov 2014, closed May 2015, wind-down through June). **Taught one GPRC semester, Sep – Dec 2014.** |
| C-13 | GPRS site history | WordPress.com 2023; self-hosted WordPress.org on Hostinger 2025 "because I wanted more freedom to experiment with the code." Used in `/work/gprs`. No month-level dates without asking. |
| C-17 | R4 wording, his call | Live: "…then build it with help writing by AI." **Do not raise it again or change it unasked.** |
| C-9 | `page-thomas.php` ~2010: "I couldn't get past my kitchen manager" | His prose and his call. Flag it, do not rewrite it. |

### PROJECTS / GRAPH
| # | Item | Notes |
|---|---|---|
| P-6 | A fourth project? | Nothing queued; show finished work only. |
| G-6 | Demo still is a headless render | Thomas screenshots the live demo if he wants a hand-framed one. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add `/work/gprs` to that run. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-11 | **`www.tc-ventures.ca` did not answer** | Seen 2026-09-24: curl got no response. Anyone typing `www.` reaches nothing. Thomas's call whether to add a `www` → apex redirect; not yet put to him as a decision. |
| INFRA-12 | `public/.assetsignore` shows modified in the working tree | Line endings only; `git diff` shows no content change. Harmless. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address. |
| INFRA-6 | Dead lander CSS in `style.css` (search `lander embed`) | Delete if still unused by mid-October 2026. |
| INFRA-9 | HSTS 1 yr, no `includeSubDomains`, no `preload` | Deliberate; both are hard to undo. |
| INFRA-10 | LinkedIn Post Inspector | Not confirmed run. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | Harmless; detach when convenient. |
| D-2 | WP.com plan auto-renew | Do not cancel without confirming DNS for the live sites is unaffected. |
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. **Not confirmed paid** as of 2026-09-24. |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-2 | `/projects` third-person leakage on thomascheesman.ca | Thomas is writing this himself. |
| O-4 | bareyourrare history contains `permits/` and `3.jpg` | Instructions in `_Quarantine\bareyourrare-history-purge.md`. Thomas runs it. |
| O-5 | `bareyr\.git` lock-file junk | Cosmetic; Thomas deletes. |
| O-6 | Rocket Lander repo not public | On hold with the lander. |
| O-7 | Children's names in the Back Quarter world | **Thomas ruled: leave them.** They stay off this site regardless. |
| O-8 | thomascheesman.ca's open items live in `V0.42.md` | `three-r128.min.js` idle-loads for every visitor; the mouse wheel over a live stage does not scroll the page. |
| O-9 | `page-hcs.php` Keg paragraph, on disk, not deployed | Thomas pushes the theme and purges all three caches (Cloudflare, Hostinger CDN, LiteSpeed). |
| O-10 | bareyourrare.org and thomascheesman.ca behind Cloudflare since 2026-09-20 | thomascheesman.ca has three cache layers. Full detail in handoff-014 §4. |
| O-11 | bareyourrare.org crawl audit, mostly deployed | `Claude outputs/byr-crawl-audit.md`. Still open: (g) page weight. |
| O-12 | GPRS work has its own handoff | `GPRS Organization/00 Working Notes/gprs-handoff-001.md`. |
| O-13 | **BYR still serves `NGO` schema on guide pages** | From receipts-001 §5 (R-141). Fix is in `bareyr/functions.php` L707–715. Not re-checked live this session. |

**Closed this session:** PL-2 (receipts inventory, ruled 2026-09-23). F-1 (live).

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

## 6. Next up — Phase 1, step 2 continued

Before anything: remind Thomas once of **D-3** (email renewal, 8 October) if it's still
open. Each step ends with his ruling before the next starts.

### Step 2b — `/work/this-site`

1. **Sources:** the 7 OK rows in receipts-001 §3B (R-011, R-019, R-022, R-024, R-027,
   R-028, R-029); Reports Clustering OK rows only where they overlap this site's method;
   handoffs 001–016; copy-reviews 001–003; `plans/operating-guide.md` and
   `plans/top-ten-receipts.md` (both public). **Re-open each receipt before quoting it**
   (receipts-001 §0: unticked `chk` rows were not re-read by the coordinator).
2. **Start from the draft copy already in `_template.html`.** It is the this-site sample,
   written from handoff-013, never reviewed. Its three misses (the screensaver names, the
   exact counts, "available now") may or may not map to OK rows; check each against the
   inventory's rulings. **A CUT row does not come back through the template.**
3. PL-4: the "ask" paragraph is Claude's wording. Put it in the review as its own block.
4. PL-8: ask Thomas whether to build the budget script first or ship without numbers.
5. Draft into `reviews/copy-review-003.md` as T1…Tn, and preview as
   `public/work/this-site.html` **listed in `.assetsignore`** until ruled. Same shipping
   checklist as `/work/gprs`: remove banner and `noindex`, OG from the header, sitemap,
   links in, then verify live (check-run, curl, headless render, console).

### Step 2c — the `/work/` index and the menu (PL-7)

Once two case studies are live: a `/work/` index page, "Work" in the menu on every page,
and a decision on Projects (plan-001 §3 says it becomes a redirect to `/work/`; that would
remove the graph, Back Quarter and Desk write-ups until they are split into case studies, so ask).

### Step 3 — `/method`

Plan-001 §4b. The rules table is pre-sorted in receipts-001 §6; use only OK rows. Copy
review before it ships.

### After Phase 1

Phase 2 (build ledger) and Phase 3 (the motion/accessibility-controls proposal) per PL-6.
**Propose before building.**
