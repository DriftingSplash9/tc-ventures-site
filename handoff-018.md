# handoff-018 — tc-ventures.ca

**Written:** 2026-09-25
**Covers:** Phase 1 closed: **`/method` shipped** as its own menu item. It has Thomas's own
H1 and lede, the loop drawn as bubbles pointing to the files each step writes, and a
paragraph on the research graph's checks (M8). No `/work/` index (ruled). R-014 un-cut.
Thomas also got a private Word list of the research project's logic tests.
**Status at wrap:** everything in §2 marked "live" was **deployed and verified live**
2026-09-25: check-run success on both pushes, curl, a logged-out browser suite against the
live site, and live screenshots on desktop and phone.

**The next job is Phase 2: propose the build ledger** (§6).

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. §2 "Traps" before you touch git, grep, line endings, a
   screenshot, the nav, or the `Reports Clustering` folder.
2. `CLAUDE.md` at repo root: the twenty truth rules. `plans/operating-guide.md` is how
   Thomas and the AI divide the work, and §4 there is the checking routine.
3. **`plans/plan-001-showcase.md`**: the plan. **§4c is Phase 2's build ledger**, and §6 Q2
   holds Thomas's "A". Nothing gets built outside the plan without Thomas agreeing.
4. **`plans/receipts-001.md`**: the ruled inventory, **37 OK / 75 CUT** since R-014 was
   un-cut on 2026-09-25. Only OK rows may be used in copy. Tick `chk` on a row before
   quoting it.
5. `reviews/copy-review-003.md`: the Phase 1 review. **Fully ruled:** R1, G1–G9, T0–T10,
   M1–M8, Q-M1–Q-M5. Phase 2 copy goes in a new `copy-review-004.md`.
6. The shipped pages: `public/work/gprs.html`, `public/work/this-site.html` and
   `public/method.html`. `public/work/_template.html` is the bare template.
7. `claude/thomas-study.md` and `claude/tc-ventures-site-decisions.md` in the Claude
   project "TC 'Ventures" (the voice study and the decisions). They are not on disk and were
   not read this session.
8. `README.md`.
9. If the job is GPRS itself, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md`.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**.

**How Thomas works:** short answers when he asks for them; blunt when you are wrong; makes
the calls himself. Recommend one option; don't survey. He rules tersely ("m8 A, diagram ok -
ship it"), and that is a full ruling. He is self-taught and model-agnostic, so explain
methods, not one model's tricks. **He commits and pushes himself, sometimes mid-session:**
re-read `git status` just before you commit.

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
| Pages | `index`, `projects`, **`method`** (live 2026-09-25), `background`, `contact`, `404`, `work/gprs`, `work/this-site`. Internal links, canonicals and sitemap use **clean URLs** (`/method`); `/x.html` 307s to `/x`. |
| Nav | **Projects (with a sub-menu of the case studies) · Method · Background · Contact**, on every page (9 files including `_template.html`). The markup is copied into each page, since there is no build step. `assets/nav.js` (deferred, every page) makes the sub-menu a disclosure button. Below 420px the nav gap tightens to 14px and the nav wraps. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html` and `og-src/` off the live site. |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. Reasons are commented in the file. Unchanged since handoff-017. |
| Link preview | `assets/img/og-card.png` 1200×630 on all pages, with the R2 headline. Source `public/og-src/og.html`; re-render command in its `<style>` comment (needs a local server on :8788). |
| Analytics | Cloudflare Web Analytics, injected at the edge. The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` + the audit phases (PL-6) · receipts `plans/receipts-001.md` (ruled) · `plans/operating-guide.md` |
| Design system | `public/assets/style.css` — tokens in `:root`, case-study components under the `CASE STUDIES` banner at the end |
| Graph demo | `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js` |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. Thomas edits it himself. |
| Browser tests | **Python Playwright + Chromium are installed.** This session's suite is `ship_check.py local\|live`, in the session scratchpad and not the repo (INFRA-13). It covers every page's status, nav order, `aria-current`, console, 375px width, and real-key Tab/Enter/Esc on the sub-menu, plus a negative control. |
| Research repo | `C:\Users\thoma\Desktop\My Files\Reports Clustering`. **Private. Never run git there, not even `git status`** (its `CLAUDE.md` rule 1: the lock file blocks Thomas's GitHub Desktop). `/method` M8 describes its validator. |
| Sister repo | `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` (thomascheesman.ca). Not connected by default; request access. |

## 2. What was done (2026-09-25, after handoff-017)

**`/method`: live.** All rulings are in copy-review-003 (M1–M8, Q-M1–Q-M5) and date from
2026-09-25.
- **No `/work/` index.** `/projects` stays, recorded in plan-001 §3. Method is its own menu
  item.
- **R-014 un-cut**, so the "No selling" rule has a receipt: the contact page's "within a
  working day", which Thomas changed to "within a day or two".
- **M1, in Thomas's words.** H1: "How AI is a tool I work with and an accessibility feature
  itself". The lede is his too.
  - The page title stays "How I work with AI - Thomas Cheesman" (Q-M3).
  - The H1 stands alone, with no explanatory sentence (Q-M5).
- **M2–M6 OK.** W4 is A. Thomas: the Back Quarter copy went live early so he could test it
  and deal with any issues. That was not copy skipping review.
- **Q-M2:** the loop is drawn as bubbles, each step pointing to the file it writes.
  - Brief → `brief-001-wow-and-contact.md`; Spec → `plan-001-showcase.md`;
    Build → commits (dashed outline); Review → `copy-review-003.md`; Rule → `CLAUDE.md`;
    Next session → `handoff-NNN.md`.
  - This version is on `/method` only. The CSS is additive (`.loop--files`), so
    `/work/this-site` keeps the row version.
- **M8, A:** "In the research graph, the checks are code…", which says **"dozens of
  checks"**. Thomas said "28 tests for each data point". No file I searched states 28, and he
  ruled "dozens".
- **Q-M1:** the home page's "How I work" heading links to `/method`. Linking the existing
  heading added no new words.
- **Phone nav:** with four items, the nav had a 5px right margin at 375px. Below 420px the
  gap is now 14px and the nav wraps. At 375px the margin is 29px; at 320px, Contact wraps.
- **Verified live:**
  - The check-run succeeded.
  - curl: every page 200; `/method.html` → 307 `/method`; an unknown URL 404s with the new
    nav; `/method` is in the sitemap and carries no `noindex` or draft banner; Method links
    on every page.
  - Browser suite, logged out: status, nav order, `aria-current`, console, 375px, keyboard.
    All pass.
  - The analytics script answers 200 on every page, with no CSP errors.
- **Found after the live check:** M6's list said "M1–M7". Fixed to M1–M8, pushed and
  confirmed live.

**Reports Clustering, read-only** (Thomas pointed at it for the "28 tests" figure):
- **Counted with commands:** `validate()` in `src/lib/graph.ts` has 59 checks, 36 on reports
  and 23 on edges.
- **`scripts/test-logic.ts` has 128 logic tests.** Run 2026-09-25: "logic: all 128 checks
  pass".
- **`Reports Clustering/Claude outputs/logic-tests-2026-09-25.docx`** lists all 128, named
  word for word from the code (parsed, not retyped), in ten areas. It's for Thomas and is
  **not linked from the site**.

### Traps worth knowing

- **Git Bash `grep -c $'\r'` cannot see carriage returns.** It prints 0 on a CRLF file.
  - Detect line endings in Python (`b"\r\n" in open(p, "rb").read()`) or with `od -c`.
  - **The repo is mixed:** `.assetsignore`, `sitemap.xml`, `projects.html` and
    `work/gprs.html` are CRLF; the rest are LF.
  - Edit byte-wise and keep each file's own ending.
- **`cd` inside a Bash call moved the session's working directory again.** Once it went
  into `public/`, and once into `Reports Clustering`, where git is forbidden. Use
  `( cd … && … )` subshells or absolute paths.
- **`/404` serves `404.html` with a 200.** Test "not found" with an unknown URL; that one
  returns a real 404.
- **The analytics report itself is not visible to a headless browser.** It was not seen
  even after leaving the page. What can be checked: `beacon.min.js` answers 200, and the
  console shows no CSP errors.
- **A test that Tabs a fixed number of times can land on the wrong control.** The sub-menu
  check first failed because Shift+Tab landed on Contact and Enter followed the link. The
  failure was in the test (rule 3). Reload and Tab exactly onto the toggle.
- **This machine has no LibreOffice, pandoc or `pdftoppm`.** To look at a `.docx`, open it
  read-only through Word's COM object (PowerShell `Word.Application`), `ExportAsFixedFormat`
  to PDF, `Quit()` in a `finally`, then make page images with PyMuPDF (`fitz`). The npm
  `docx` package is global only: `C:/Users/thoma/AppData/Roaming/npm/node_modules/docx`.
- **A figure Thomas gives can have no source on disk.** "28 tests" was searched for and not
  found. Say where you searched, and ask. Don't reconcile it yourself.
- Carried and still true:
  - A hidden browser pane fires no focus or blur events; use Playwright for focus logic.
    Playwright's visibility checks see through `clip-path: inset(50%)`.
  - Wait about 400 ms after a click before a screenshot.
  - `gh api markdown` emits no heading ids (curl the blob page for `user-content-<anchor>`),
    and `git log -S` needs `--no-textconv` here.
  - A receipt's "caught" column can be a guess; ask Thomas before copy says who caught it.
  - Linking handoffs is ruled fine despite the lander mentions. Never link
    `reviews/copy-review-001.md`.
  - Cloudflare built in under a minute this session; still check the check-run first.
  - The analytics beacon is injected at the edge: read the live console after any CSP
    change. A new inline `<script>` is blocked by the CSP.
  - Headless Chrome defaults to dark mode, and lazy images render black in tall shots.
  - Run a local test server inside the Python process; a Git Bash `http.server` survives
    `pkill`. Python heredocs through Git Bash eat backslashes, so use forward slashes.
  - Grep, don't count from memory.

## 3. Current design

**Pages live:** `/work/gprs` and `/work/this-site` (2026-09-24), and **`/method`**
(2026-09-25).

**The case studies:**
- **Six fixed sections**, receipts as small mono links, figures in `.shot--pair`.
- Every claim in "What the AI got wrong" and "How I caught it" links to a receipt that
  returns 200 publicly, or is cut.
- **"How I caught it" says "I" only for catches Thomas made.** Agent catches are written
  impersonally ("the deploy was checked").
- A rules table row may carry its own receipt link.
- The caption says "the rule it falls under", not "became", unless the timing is confirmed.

**`/method`:**
- It uses the case-study layout, with five sections: The loop · Handoffs · The rules ·
  Where AI is weak · The originals.
- The rules table has ten rules, one OK receipt each. The weaknesses list uses
  `.mc--weak` ("W1"…).
- M8 sits under the weaknesses list. Research-repo claims link receipts-001 §3C, because the
  repo is private.
- **The H1, the lede and the page title are Thomas's rulings.** Don't edit them, explain the
  accessibility line, or raise them again unasked.
- It links handoff-017 by name (the M3 excerpt and the diagram's "Next session"). Those
  links stay valid as the handoffs go on.

**Nav:**
- Adding a page to the nav means editing all **nine** files: index, projects, method,
  background, contact, 404, the two case studies and `_template`.
- A case study's sub-menu label is its H1.
- Ship the page and its link in the same push, never a link that 404s.
- Check afterwards that every page's nav is identical (INFRA-13).

**Look and feel:**
- Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
  `prefers-color-scheme`.
- Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
- Confirmed; stop re-litigating it.

**Case-study layout (approved 2026-09-22):** a wide lane (1040px) for headers, figures,
tables and lists and a reading lane (66ch) for prose; a sticky 200px rail at ≥1180px with
the section index, folding to a horizontal index below that; sections numbered by CSS
counters, figures `Fig. N` per page; receipts as small mono links with a leading `→`.

**Home page (live 2026-09-22):**
- **Label:** "Thomas Cheesman · Grande Prairie, Alberta · remote".
- **H1:** "I run a nonprofit's website, and I hold it to a written standard."
- **Lede:** from R3/R4.
- The "Four live sites" card links both case studies. The "How I work" heading links
  `/method`.
- The lede is tall on desktop: a Phase 3 layout job, not a copy one.

**Standing rules:**
- **The Rocket Lander is private.** Not here, in any form.
- `object-fit: contain`, never `cover`.
- **Content renders without JavaScript.** JS is allowed on top (motion, 3D, controls);
  the words and links must not depend on it. No dependencies or build step — prebuilt
  bundles copied into `assets/` only.
- Fonts self-hosted. No third-party font request.
- No phone number on the site. It is in the résumé PDF.
- **Never publish an exact node, edge, report, grade or check count** *in copy*. Round or
  describe ("dozens"). The application screenshot on Projects is the one ruled exception.
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
- **Never link `reviews/copy-review-001.md` from a page** (T0, 2026-09-24).
- **Never run git in `Reports Clustering`.** Read its files; change nothing there unless
  Thomas asks.

**Demo and embed rules:**
- Nothing heavy loads before a click.
- A gated page degrades when the payload is absent.
- The 3D canvas keeps its own dark ground.
- `basis` is quoted, never paraphrased.
- The written chain under the graph is the accessible equivalent.
- Nothing rearranges a layout on interaction; the sub-menu overlays and moves nothing.
- **Show finished work:** unfinished work is labelled honestly or left off.

## 4. Open items — carry these forward until closed

### PLAN
| # | Item | Notes |
|---|---|---|
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Accessibility controls (motion full/reduced/off, theme, contrast, text size) are **built into the site**. OS preferences are the defaults; the toggles override them and persist. Order: **Phase 1 ✓ complete 2026-09-25** (receipts, `/work/gprs`, `/work/this-site`, `/method`) → **Phase 2** (the build ledger as the home hero, static SVG; plan-001 §4c) → Phase 3 (craft; **proposal first**) → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). |
| PL-8 | **Page-weight / a11y numbers: ruled ship without (2026-09-24)** | `/work/this-site` says none are shown because nothing measures them by script yet. When the Phase 4 budget script exists, the numbers go into that page's honest limits (plan-001 §6 Q5), through a copy review. |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-19 | **Q-G2 unresolved: when did "read the actual code" enter the audit prompt?** | Thomas doesn't recall. The live page makes no causal claim. Don't reintroduce one. |
| C-20 | **`/work/this-site` states two things that will go stale** | "rebuild in progress" (header) and "has not had a screen-reader run-through yet" (honest limits). Update both when the rebuild ends and when A-1 is done. |
| C-15 | Résumé PDF: **site copy done**, private copy unchecked | Served PDF replaced 2026-09-23 (md5 `0da7af62…`, matches repo). Not checked: `Family & Personal\resume\Thomas_Cheesman_Resume.pdf`. Cosmetic: summary ends on a one-word line ("roles."). |
| C-16 | **Job history, from Thomas 2026-09-23. Use these** | GPRS board: elected at the **June 2023** AGM (first meeting September). Majors consulting: May 2019 – **June 2020**. **Head Chef, Ric's Grill, Sep 2013 – Jul 2014.** **Executive Chef, Township 71, Jul 2014 – Jun 2015** (renovation from Oct 2014, opened Nov 2014, closed May 2015, wind-down through June). **Taught one GPRC semester, Sep – Dec 2014.** |
| C-13 | GPRS site history | WordPress.com 2023; self-hosted WordPress.org on Hostinger 2025 "because I wanted more freedom to experiment with the code." Used in `/work/gprs`. No month-level dates without asking. |
| C-17 | R4 wording, his call | Live: "…then build it with help writing by AI." **Do not raise it again or change it unasked.** |
| C-21 | **`/method` H1, lede and title: his call (2026-09-25)** | Same standing as C-17. The H1 stands alone (Q-M5). |
| C-9 | `page-thomas.php` ~2010: "I couldn't get past my kitchen manager" | His prose and his call. Flag it, do not rewrite it. |

### PROJECTS / GRAPH
| # | Item | Notes |
|---|---|---|
| P-6 | A fourth project? | Nothing queued; show finished work only. |
| G-6 | Demo still is a headless render | Thomas screenshots the live demo if he wants a hand-framed one. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add `/work/gprs`, `/work/this-site`, **`/method`** and the Projects sub-menu to that run. Left from 012: one real screen-reader run through Projects and the live graph. **Two points for it:** the loop diagrams' links sit inside an SVG with `role="img"`, which may hide them from screen readers (the same links are in `/method`'s "originals" list); and the diagrams' connectors and arrows in `--rule` are faint on white (non-text contrast). |
| A-3 | **Sub-menu without JS cannot be dismissed with Esc** | Without JS the list shows on hover or focus (WCAG 1.4.13 asks for a dismiss key). With JS, Esc works. Accepted as the no-JS fallback; for A-1 to confirm. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-13 | **The nav is copied into nine files** | Adding a page means editing all nine by hand. Rule 5 says the same miss twice becomes code. This session's `ship_check.py` checks nav equality, keyboard, 375px and console, with a negative control. It is the draft of a `scripts/` checker. Not in the repo. |
| INFRA-11 | **`www.tc-ventures.ca` did not answer** | Seen 2026-09-24: curl got no response. Anyone typing `www.` reaches nothing. Thomas's call whether to add a `www` → apex redirect; not yet put to him as a decision. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address. |
| INFRA-6 | Dead lander CSS in `style.css` (search `lander embed`) | Delete if still unused by mid-October 2026. |
| INFRA-9 | HSTS 1 yr, no `includeSubDomains`, no `preload` | Deliberate; both are hard to undo. |
| INFRA-10 | LinkedIn Post Inspector | Not confirmed run. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | Harmless; detach when convenient. |
| D-2 | WP.com plan auto-renew | Do not cancel without confirming DNS for the live sites is unaffected. |
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. Thomas reminded 2026-09-24 and 2026-09-25. **Not confirmed paid.** |

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

**Closed this session:**
- **PL-7:** no `/work/` index, and `/projects` stays (ruled 2026-09-25, in plan-001 §3).
- **C-18:** copy-review-003 is fully ruled.
- **`/method`:** live. Phase 1 is complete.

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

## 6. Next up — Phase 2: the build ledger

Before anything: remind Thomas once of **D-3** (the email renewal, due **2026-10-08**) if
it's still open. Each step ends with his ruling before the next starts.

### Step 1 — the proposal (propose before building, PL-6)

Plan-001 §4c, option A, which Thomas chose in §6 Q2. It is a compact visual of this site's
own history: every handoff as a mark on a timeline, open items opening and closing by
workstream, and traps logged. PL-6 puts it on the home page as the hero, **as a static SVG
first**.

Put a short proposal to Thomas that settles:
1. **What each mark shows, from which handoff fields, public-safe only.** The data must be
   **curated, never raw** (§4c). Handoffs carry personal material, and every one mentions
   the Rocket Lander, which must never appear.
2. **The data path:** a script run by hand that reads the handoffs and writes a committed,
   curated JSON (like `scripts/export-gp-budget.py`). No build step.
3. **How it works without JS:** the static SVG and its words, plus a text equivalent.
4. **Where it sits against the home H1 and the tall lede.** The layout itself is Phase 3's
   job.
5. **Counts:** the number of handoffs and open items is public on GitHub, but copy still
   rounds or describes. No vanity numbers.

Any copy goes into `reviews/copy-review-004.md`.

### After Phase 2

Phase 3 is the craft proposal: motion, plus the built-in accessibility controls (PL-6).
Then Phase 4. **Propose before building.**
