# handoff-021 — tc-ventures.ca

**Written:** 2026-09-27
**Covers:** Phase 1b's last two case studies, the Back Quarter and the Desk and the Drawer:
- **Step 1 (receipts) is ruled.** The rows are receipts-001 §3F.
- **Six `/projects` lines were fixed and shipped.**
- **A privacy problem in the theme repo:** Thomas made the repo private.
- **Step 2 (the copy) is drafted and partly ruled.** Thomas paused it on 2026-09-27, with a decision about
  the Back Quarter itself (O-20).

**Status at wrap:**
- **Live, verified 2026-09-26 22:02 UTC:** `/projects` PJ1–PJ6 and the Desk's opening line (merge `0b9c4eb`,
  PR #4). Checked by curl: byte-identical to `main`, and every sitemap page answered 200.
- **On PR #5, not live:**
  - copy-review-005 step 2;
  - `public/projects.html` with BQD4 1–6 and BQD5.
  - Merging PR #5 ships those `/projects` lines.
- **Paused at Thomas's word:** the rest of step 2, and O-20.

**The next job is §6.**

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. Read §2 "Traps" before you touch git, a checker script, a screenshot, the theme
   repo, a Hostinger site, or the `Reports Clustering` folder.
2. `CLAUDE.md` at repo root: the twenty truth rules. `plans/operating-guide.md` is how Thomas and the AI
   divide the work, and §4 there is the checking routine.
3. **`plans/plan-001-showcase.md`**: the plan. **The §5 note (2026-09-25)** holds the order; §3 lists the
   case studies (`/work/back-quarter`, `/work/desk-and-drawer`).
4. **`plans/receipts-001.md`**: the ruled inventory, **49 OK / 81 CUT** (header, 2026-09-26). **§3F** holds
   the rows for these two case studies. Only OK rows go in copy. Tick `chk` before quoting a row.
5. **`reviews/copy-review-005.md`**: the current review.
   - **BQD0:** the receipts, ruled.
   - **PJ1–PJ6:** shipped.
   - **Step 2:** BQD4 and BQD5 ruled; BQ1–BQ8, DD1–DD8 and P3 open.
   - Each block's rulings are at its end, verbatim.
6. The shipped pages under `public/`. **`work/bare-your-rare.html` and `work/influence-graph.html` are the
   patterns to copy.**
7. **`scripts/`**: `site_check.py`, `cs_check.py`, `byr_bot_check.py`. Each script's docstring is its manual.
8. `claude/thomas-study.md` and `claude/tc-ventures-site-decisions.md` in the Claude project "TC 'Ventures"
   (not on disk, not read this session).
9. `README.md`.
10. If the job is GPRS itself, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md`.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**.

**How Thomas works:**
- Short answers when he asks for them. He's blunt when you are wrong, and he makes the calls himself.
- Recommend one option; don't survey.
- He rules tersely ("pj1- a, pj2- ok", "medic hut", "merge pr4"), and that is a full ruling.
- **He sometimes hands a call over** ("you decide which up to 8"). Make it, say in one line what you chose
  and why, and record it as delegated.
- **"pause here" means start nothing new.** Record what he ruled and wait.
- He is self-taught and model-agnostic, so explain methods, not one model's tricks.
- When he asks how something works, give him the plain version first.
- **He commits, pushes and merges himself, sometimes mid-session** (he merged PR #3 during this one).
  Re-read `git status` and `origin/main` just before you commit.

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
| Deploy | **A merge to `main` deploys** → Cloudflare builds. **No cache to purge.** Branch pushes build too, and the bot calls them "Deployment successful", but they don't reach the site (trap below). |
| Contact email | `thomas@tc-ventures.ca` |
| Pages | `index`, `projects`, `method`, `background`, `contact`, `404`, `work/gprs`, `work/this-site`, `work/influence-graph`, `work/bare-your-rare`. Planned: `work/back-quarter`, `work/desk-and-drawer`. Internal links, canonicals and sitemap use **clean URLs** (`/method`); `/x.html` 307s to `/x`. |
| Nav | **Projects (with a sub-menu of the case studies) · Method · Background · Contact**, on every page: **11 files** including `_template.html`, and 13 once the two planned pages ship. The sub-menu order is the `/projects` order. Today it's **The Economic Report Influence Graph · A rare-disease site, written by a patient · A housing society's website · This site**. After the ship: graph · Back Quarter · Desk · BYR · GPRS · this site. The markup is copied into each page; `assets/nav.js` makes the sub-menu a disclosure button. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html` and `og-src/` off the live site. A preview goes in it until it ships. |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. Unchanged since handoff-017. |
| AI crawlers | Cloudflare answers GPTBot and ClaudeBot 403 on tc-ventures.ca; Claude-User and ChatGPT-User get 200 (checked 2026-09-26). INFRA-15. |
| Link preview | `assets/img/og-card.png` 1200×630 on all pages. Source `public/og-src/og.html`. |
| Analytics | Cloudflare Web Analytics, injected at the edge. The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` · receipts `plans/receipts-001.md` · `plans/operating-guide.md` |
| Design system | `public/assets/style.css` — tokens in `:root`, case-study components under the `CASE STUDIES` banner at the end |
| Graph demo | On `/work/influence-graph` only. `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js`. |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. |
| Browser tests | Python Playwright + Chromium, scripts in `scripts/`: `site_check.py [--live] [--root DIR]` (every sitemap page plus /404) and `cs_check.py work/<page> [--preview] [--shots DIR]` (one case study). Both serve `public/` in-process with clean URLs. **In a claude.ai cloud session:** `pip install playwright` first. The scripts launch the preinstalled Chromium by path (trap below). |
| Research repo | `C:\Users\thoma\Desktop\My Files\Reports Clustering` = public `DriftingSplash9/Reports-Clustering`. **Never run git there.** Read its files, and read it on GitHub. |
| Sister repos | **Theme:** `tc-ventures-child-theme` = GitHub `DriftingSplash9/thomascheesman-ca-theme`, **private since 2026-09-26**. Checked: the API says `"private": true`, and an anonymous raw fetch answers 404. Hostinger deploys it over SSH with a deploy key. **BYR:** `bareyr` = GitHub `DriftingSplash9/bareyourrare`, **private**. A push to its `main` deploys to Hostinger, and cached pages then need a LiteSpeed purge (Thomas, in WordPress). |

## 2. What was done (2026-09-26 to 09-27, after handoff-020)

**Rulings.** All in copy-review-005, verbatim, at the end of each block. In short:
- **BQD0:**
  - **Q-BQD1 A:** the case studies link receipts-001 rows, never theme files.
  - **Q-BQD2:** why he built the site, in his words.
  - **Q-BQD3 A:** that quote is a second ruled exception to "nothing familial".
  - **Catchers:** he supplied the catcher for seven rows.
  - **"You decide which up to 8":** the agent kept R-160, R-162, R-163, R-164, R-168, R-169, R-170 and
    R-172. The other seven are CUT.
- **PJ1–PJ6:** "pj1- a, pj2- ok, pj3- ok, pj4 cut, pj5 - A, pj 6 - cut", then "change the claim, merge,
  merge pr4".
- **Step 2:** BQD4 1 fix, 2 medic hut, 3 fix, 4 OK, 5 fix (read as A), 6 fix. BQD5: cut "The game always
  starts." Then **"pause here"**, with the Back Quarter decision (O-20).

**Live, and verified live:**
- **`/projects`:** PJ1–PJ6 and the Desk's "ignoring it costs a visitor almost nothing" (PR #4, merge
  `0b9c4eb`).
  - Served by 22:02 UTC on 2026-09-26, about a minute after the merge.
  - Checked by curl: byte-identical to `main`. Every sitemap page answered 200.
- **receipts-001 §3F:** R-160 to R-174, 8 OK and 7 CUT. The totals are now 49 OK and 81 CUT, counted by
  command. The case studies link §3F, not the theme files.

**On PR #5, checked locally, not live:**
- `public/projects.html`: BQD4 1–6 and BQD5.
  - `site_check.py` passed 84 of 84.
  - The rendered text carries the new lines and none of the removed ones, and a control with one word
    changed fails.
  - Looked at in a screenshot at 375px.
- copy-review-005 step 2: BQD4, BQD5, BQ1–BQ8, DD1–DD8 and P3. Every excerpt and quote in it was checked
  verbatim by script, with a control.

**Found, and handled by Thomas:**
- **The theme repo was public, and it exposed family material** (O-21). Thomas made it private on
  2026-09-26 (checked). The details are in the chat only.
- **Two old gallery images were still in thomascheesman.ca's media library.** Thomas deleted them on
  2026-09-26. The site's media search no longer finds either, and it does find a known image (control).
- **A Hostinger deploy webhook was in a formerly public file** (O-22).

**Found, not fixed:**
- **BQD0 said both `/projects` sections had been traced. They hadn't been, fully.** Tracing the rest
  against the theme's code found six more false Back Quarter lines (BQD4) and one untested Desk claim
  (BQD5). The fixes are on PR #5.
- **O-19:** re-tested 2026-09-27. `/timeline/` answered 200 cached and uncached, and it was the real page
  (title checked).

**Tooling:** nothing new in `scripts/`. The ad-hoc checks this session (the rendered text with a control,
the section screenshots) stayed in the scratchpad. That's INFRA-16.

### Traps worth knowing

Each trap ends with its tally, **`x.y`** (§5).

**Dropped this handoff** (x > 5 and y ≤ 1):
- **Heredocs mangle scripts** (`6.1`). It bit again this session: a quoted heredoc kept `\"` literally,
  which changed a verbatim quote. The quote check caught it. By §5 it belongs in code.
- **Cloudflare's edge-injected beacon and a new inline script under the CSP** (`6.1`).

**New this session:**
- **A checker can read the wrong block, and a control can be unable to fail.** Three hits this session.
  - A regex anchored on a phrase that appears twice matched the Status line, not the rulings.
  - One control replaced a word that wasn't in the text.
  - Another control's change ("arcade" to "arcad") was still a substring of the text.
  - The fix: anchor on the heading. A control must change a word that is in the text, and leave no
    substring match. `0.0`
- **The Cloudflare bot says "Deployment successful" on branch pushes and links a "production" build.
  Branch builds don't reach tc-ventures.ca.** After a branch push, the live page stayed byte-identical to
  `main`. Only a merge deploys. `0.0`
- **In a cloud session, `pip install playwright` installs a version whose default browser path doesn't
  exist.** Launch with `executable_path='/opt/pw-browsers/chromium'`. The scripts in `scripts/` already
  do; ad-hoc scripts must too. `0.0`
- **The cloud clone of the theme repo is shallow (50 commits).** Run `git fetch --unshallow` before
  reading history for receipts. `0.0`
- **`/projects` copy about thomascheesman.ca goes stale when the features change.**
  - A grain elevator became a medic hut.
  - A barn was described as booting the games, and never did.
  - The sound design gained recorded samples.
  - Re-trace a `/projects` paragraph against the theme's code before a case study reuses it. `0.0`

**Carried:**
- **To check a schema type is gone, count the old type's exact string.** `1.0`
- **`cf-ray` is on every response through Cloudflare.** A Cloudflare challenge carries
  `cf-mitigated: challenge`; `x-turbo-charged-by: LiteSpeed` means the origin answered. `1.0`
- **A check warms the cache it is checking.** Use a cache-busting query to reach the origin. Used this
  session for the GPRS re-test. `1.1`
- **Pace requests to the Hostinger sites and keep runs small.** Used this session: 6 s gaps on the GPRS
  and thomascheesman.ca checks. `1.1`
- **The LiteSpeed Cache crawler's default interval is 302400 s.** It is set to 3600 s now. `1.0`
- **Chromium in a claude.ai cloud session rejects the session proxy's certificate.** Check live with
  curl instead: compare each page byte for byte with the file the local suite passed. Used this session.
  `1.1`
- **`getComputedStyle(el, '::before').content` returns the CSS expression, not the number drawn.** Check
  figure numbering in a screenshot. `2.0`
- **Pin research-repo receipts to a commit SHA.** Read the first and last line of each range in the
  pinned commit. `2.0`
- **Never start a Bash command with `cd`.** Use absolute paths, `git -C`, or `( cd … && … )`.
  - **Hit twice again this session despite the mention.** No y.
  - INFRA-14a. `4.0`
- **`.assetsignore`, `sitemap.xml`, `projects.html`, `work/gprs.html` and `plans/receipts-001.md` are
  CRLF in Thomas's Windows checkout.** Detect CRLF in Python and edit byte-wise. This session the line
  endings were checked in Python before `projects.html` was edited. `3.2`
- **Run a local test server inside the Python process.** Used this session: the ad-hoc check served
  `public/` in-process. `4.3`
- **Headless Chrome defaults to dark mode.** Set the colour scheme for each browser context. Used this
  session. `5.3`
- **Wait about 400 ms after a click before a screenshot.** `4.1`
- **`/404` answers 200.** Test "not found" with an unknown URL. `3.2`
- **Analytics can't be seen headless.** Check that `beacon.min.js` answers 200 and the console has no CSP
  errors. `3.1`
- **Cloudflare's build start has ranged from about 1 to 10 minutes.** Check the check-run before
  diagnosing a live page. Used this session: the merge waited for the check-run, and the live page was
  polled until the new text appeared. `5.2`
- **A test that Tabs a fixed number of times can land on the wrong control.** Loop until the target has
  focus. `3.2`
- **A hidden browser pane fires no focus or blur events.** Test focus logic in Playwright. `4.1`
- **A receipt's "caught" column can be a guess.** Open the receipt before copy says "I". Used this
  session: the catchers were asked of Thomas, and he supplied seven. `4.2`
- **A figure Thomas gives can have no source on disk.** Say where you searched, and ask. `3.0`
- **`gh api markdown` emits no heading ids**, and `git log -S` needs `--no-textconv` here. `4.0`
- **There's no LibreOffice, pandoc or `pdftoppm` on Thomas's machine.** Render a `.docx` through Word COM,
  read-only. `3.0`

## 3. Current design

**Pages live:**
- `/work/gprs` and `/work/this-site` (2026-09-24)
- `/method` and `/work/influence-graph` (2026-09-25)
- **`/work/bare-your-rare`** (2026-09-26)

**The case studies:**
- **Six fixed sections**, receipts as small mono links, figures `Fig. N` per page.
- Every claim in "What the AI got wrong" and "How I caught it" links to a receipt that
  returns 200 publicly, or is cut. A receipt in a private repo (BYR's) links its receipts-001
  row instead.
- **"How I caught it" says "I" only for catches Thomas made.** Agent catches are written
  impersonally.
- **Rules-table captions say "falls under"**, not "became", unless the timing is confirmed in
  the receipt. "The rule now" is used where the rule changed after it was made.
- **"The ask" quotes Thomas's own words.** If there's no brief on disk, ask him, as for GPRS,
  the graph and BYR.
- A case study that takes content from `/projects` takes it unchanged, **after re-tracing it against its
  source** (BQD4 found six false lines in live copy). `/projects` keeps a
  short intro and a "read the case study" line (P1, P2).
- **"Honest limits" in "What shipped" states what is still wrong.** BYR's states the host limit.
  If the host or plan changes, that line goes stale (O-16).

**`/method`:**
- **The H1, the lede and the page title are Thomas's rulings.** Don't edit them, explain the
  accessibility line, or raise them again unasked.
- Research-project rows link receipts-001 §3C. That's fine, since the repo is public.

**Nav:**
- Adding a case study means editing all **eleven** files (thirteen once the two planned pages ship). A case study's sub-menu label is its H1,
  in the `/projects` order. `site_check.py`'s `SUBMENU` and `cs_check.py`'s `SUBMENU` must
  change with it.
- Ship the page and its link in the same push, never a link that 404s.
- Run `scripts/site_check.py` before and after (INFRA-13).

**Look and feel:**
- Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
  `prefers-color-scheme`.
- Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
- Confirmed; stop re-litigating it. **Thomas, 2026-09-25: design waits until the content is
  mostly in place.** Log layout nits for Phase 3 rather than fixing them, unless a change you
  made caused them.

**Case-study layout (approved 2026-09-22):**
- Two lanes: a wide lane (1040px) for headers, figures, tables and lists, and a reading lane
  (66ch) for prose.
- A sticky 200px rail at ≥1180px with the section index. Below that it folds to a horizontal
  index.
- Sections are numbered by CSS counters, and figures `Fig. N` per page.
- Receipts are small mono links with a leading `→`.

**Home page (live 2026-09-22):**
- **Label:** "Thomas Cheesman · Grande Prairie, Alberta · remote".
- **H1:** "I run a nonprofit's website, and I hold it to a written standard."
- **Lede:** from R3/R4.
- The graph card links `/work/influence-graph`. The "Four live sites" card links both site
  case studies and, since P2, `/work/bare-your-rare`. The "How I work" heading links `/method`.
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
  describe ("dozens"). **The app screenshot (`graph-app-ui.webp`) is the one ruled
  exception**, on `/projects` and on `/work/influence-graph` (Q-IG5).
- **No vanity metrics.** No line counts.
- **Do not invent dates or figures.** Unknown → ask Thomas.
- Hajdu-Cheney syndrome is named on purpose. Symptom detail is not. **BYR is a patient site:
  no symptom detail and no family, in copy or in any receipt it links.**
- WordPress stays once per spec table as a hiring keyword; out of headline prose.
- **Nothing familial**, except the ruled Back Quarter childhood paragraph and Thomas's Q-BQD2 quote on
  the two new case studies (Q-BQD3 A, copy-review-005). Children's
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
- **The outside research model is never named in copy** (F-2), and no link's path may
  carry its name.
- **Don't link the `@bareyourrare` social accounts anywhere until Thomas says they are claimed**
  (O-18).
- **Never link a theme-repo file or commit.** The repo is private, and its handoffs and commit diffs
  carry family material. Read it for facts only. The case studies link receipts-001 §3F (Q-BQD1 A).

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
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Accessibility controls (motion full/reduced/off, theme, contrast, text size) are **built into the site**. OS preferences are the defaults; the toggles override them and persist. Order: Phase 1 ✓ (2026-09-25) → **Phase 1b, the remaining case studies (ruled 2026-09-25): graph ✓ → BYR ✓ (2026-09-26) → Back Quarter + Desk (receipts ruled 2026-09-26; copy drafted and partly ruled 2026-09-27, copy-review-005)** → Phase 2 (the build ledger as the home hero, static SVG; plan-001 §4c) → Phase 3 (craft; **proposal first**) → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). |
| PL-8 | **Page-weight / a11y numbers: ruled ship without (2026-09-24)** | `/work/this-site` says none are shown because nothing measures them by script yet. When the Phase 4 budget script exists, the numbers go into that page's honest limits (plan-001 §6 Q5), through a copy review. |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-22 | **`/method` rules row 1 says "I caught it by using them"** (the three sliders) | The receipts confirm Thomas caught the last two (handoffs 006/007 and 032). Nothing found on how the first (`geoAffinity`) was caught. Reported as a DOUBT in copy-review-004. No change proposed. His call if he wants it narrowed. |
| C-23 | **`/projects` lede and meta after the splits** | The lede says "Three built in the open, in detail — what they are, what was hard, and what I got wrong." The graph's and BYR's detail now live in their case studies, and the Back Quarter's and the Desk's will too. Review the lede and description when those two ship. Not raised with Thomas yet. |
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
| G-7 | **The demo's paragraph sits tight against its frame** | On `/work/influence-graph`: `.gd__frame` has no top margin after `.prose`. Phase 3 layout. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add `/work/gprs`, `/work/this-site`, `/method`, `/work/influence-graph`, `/work/bare-your-rare`, the two planned pages and the Projects sub-menu to that run. Left from 012: one real screen-reader run through the live graph, now on `/work/influence-graph`. **Two points for it:** the loop diagrams' links sit inside an SVG with `role="img"`, which may hide them from screen readers (the same links are in `/method`'s "originals" list); and the diagrams' connectors and arrows in `--rule` are faint on white (non-text contrast). |
| A-3 | **Sub-menu without JS cannot be dismissed with Esc** | Without JS the list shows on hover or focus (WCAG 1.4.13 asks for a dismiss key). With JS, Esc works. Accepted as the no-JS fallback; for A-1 to confirm. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-13 | **The nav is copied into eleven files** | **Checker done (2026-09-26):** `scripts/site_check.py` checks every page's sub-menu, both `aria-current` levels, keyboard, 375px and console, and it failed as expected on the pre-ship `public/`. **Still manual:** the edit itself. This session's nav-edit script (`ship_byr.py`, asserted single matches) stayed in the scratchpad. A `scripts/` version that takes the new li and its position is the remaining rule-5 step. |
| INFRA-14 | **Two traps the mention doesn't prevent** | (a) **Bash `cd`** (tally `4.0`, hit twice again 2026-09-26/27): a Claude Code `PreToolUse` hook that refuses a Bash command starting with `cd`. That changes Thomas's harness settings, so it is **his call; not built**. (b) **Full-page screenshots: done**, as `cs_check.py --shots`. |
| INFRA-16 | **A verbatim-quote checker in `scripts/`** | This session's ad-hoc text checks read the wrong block once and had two controls that could not fail (§2 trap). A shared script that takes the quote and the file, and runs its own control, is the rule-5 step. Not built. |
| INFRA-15 | **Cloudflare blocks GPTBot and ClaudeBot on tc-ventures.ca** | Re-checked 2026-09-26: both get 403; Claude-User and ChatGPT-User get 200. So AI search can cite the site when a user asks, but those two companies' crawlers can't index it. It's a setting in Thomas's Cloudflare dashboard (AI bot blocking). **His call; not raised as a recommendation.** |
| INFRA-11 | **`www.tc-ventures.ca` did not answer** | Seen 2026-09-24: curl got no response. Anyone typing `www.` reaches nothing. Thomas's call whether to add a `www` → apex redirect. Raised with him 2026-09-25, and not yet ruled. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address. |
| INFRA-6 | Dead lander CSS in `style.css` (search `lander embed`) | Delete if still unused by mid-October 2026. |
| INFRA-9 | HSTS 1 yr, no `includeSubDomains`, no `preload` | Deliberate; both are hard to undo. |
| INFRA-10 | LinkedIn Post Inspector | Not confirmed run. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | Harmless; detach when convenient. |
| D-2 | WP.com plan auto-renew | Do not cancel without confirming DNS for the live sites is unaffected. |
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. Thomas reminded 2026-09-24, 2026-09-25 (twice) and 2026-09-26. **He will renew on 2026-10-07** (said 2026-09-27). **Not confirmed paid.** |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-20 | **The Back Quarter decision (Thomas, 2026-09-27): retire the 2D painted map; the 3D world on PCs only; phones get neither** | A theme change on a plan-first surface, **paused at his word**. **Today's code differs:** touch screens under 820px and browsers without WebGL get the painted map (`back-quarter.js`, `prefersPaintedMap()`). **Open for the plan:** what phones see instead; tablets (touch at 820px and up gets 3D today); what "PC" means in code; retiring `back-quarter.js` and the Pixi and Matter vendor files; three.js's idle-load (O-8). **When it ships, this repo's copy follows:** PJ1's phone sentence, the spec rows "The Painted Map" and "Input", BQ1's stack and BQ6's phone limit. Copy never runs ahead of the site. |
| O-21 | **Theme repo: family material in its files, history and commit diffs** | It was public. **Private since 2026-09-26** (checked). The history still holds the material; cleaning it is Thomas's call. The details went to him in the chat on 2026-09-26, not here, because this repo is public. |
| O-22 | **Hostinger deploy webhook URL was in a public theme file for about seven weeks** | Anyone with the URL can trigger a redeploy of `main`, no more. Hostinger's Git docs show no "regenerate" (docs.hostinger.com/websites/git, fetched 2026-09-27). **Thomas:** look in hPanel → Advanced → Git → the repository's Auto Deployment for a regenerate option. If there isn't one, rotate it when the deployment is next rebuilt; Hostinger now recommends its GitHub App method. |
| O-16 | **Hostinger refuses AI crawlers on uncached pages: ruled leave it ("1", 2026-09-26)** | GPTBot gets an empty 429 on all three Hostinger sites, and LiteSpeed's CAPTCHA 403s PerplexityBot and Claude-User on BYR. There is no customer control on shared hosting (Hostinger support). **Mitigation:** the LiteSpeed crawler, hourly, over `page-sitemap.xml`. Only a plan change or Cloudflare HTML caching would change it; both are his call. Leave the Hostinger "Create LLMs.txt file" toggle **off**: on, it replaces the hand-written `llms.txt`. Evidence is in `Claude outputs/byr-bot-check-2026-09-25.md`. `/work/bare-your-rare`'s honest limit depends on this. |
| O-17 | **BYR `.htaccess`: Thomas's `E=verifycaptcha:off` block had no effect** | Addendum 4. Not confirmed whether it is still in the file. His call whether to take it out. |
| O-18 | **`@bareyourrare` social accounts are unclaimed** | Links removed (`ed6b054`). Restore from that commit's parent once Thomas says the accounts are claimed. |
| O-19 | **GPRS: WordPress "critical error" on uncached pages, 2026-09-26** | Seen 08:34 UTC: uncached pages (`/timeline/`, `/our-story/`, `/accessibility/`) answered 500 "There has been a critical error on this website", and some requests got no connection. The last clean check before that was about 02:35 UTC. By 09:16, `/our-story/` answered 200 uncached. At 16:42–16:45, `/`, `/our-story/` and `/accessibility/` answered 200 with no error, **but `/timeline/` reset the connection on every try (09:16, 16:42, 16:44)**. **Thomas opened `/timeline/` with no problem (2026-09-26, after wrap),** so the resets were this session's network path or the host's bot filter, not the site. The 08:34 errors were real. Cause unknown. The critical-error email goes to the address under WordPress **Settings → General → Administration Email Address**, not Thomas's Gmail (searched, spam included: nothing in 3 days). Thomas checks that mailbox's junk for "Technical Issue" if he wants the cause. GPRS's own handoff owns any fix (O-12). **Re-tested 2026-09-27 ~03:00 UTC:** `/timeline/` answered 200 cached and uncached, and it was the real page (title checked). |
| O-14 | **Research repo: 52 public file paths carry the outside model's name** | Thomas ruled 2026-09-07 that the research docs drop the name (F-2). The public archive still carries it, in paths and text. His call. Nothing was changed there. |
| O-15 | **Research repo: "read the sentence as well as fetching it" is not in its current playbooks** | It was written in `archive/NZ/G.3.md` L539 (2026-08-06). A grep of `PLAYBOOK*.md` for it, "grammatical" and "subject of" found nothing. `/work/influence-graph`'s table row uses `CLAUDE.md` rule 13 instead. His call whether the research project carries it again. |
| O-2 | `/projects` third-person leakage on thomascheesman.ca | Thomas is writing this himself. |
| O-4 | bareyourrare history contains `permits/` and `3.jpg` | Instructions in `_Quarantine\bareyourrare-history-purge.md`. Thomas runs it. |
| O-5 | `bareyr\.git` lock-file junk | Cosmetic; Thomas deletes. |
| O-6 | Rocket Lander repo not public | On hold with the lander. |
| O-7 | Children's names in the Back Quarter world | **Thomas ruled: leave them.** They stay off this site regardless. |
| O-8 | thomascheesman.ca's open items live in `V0.42.md` | `three-r128.min.js` idle-loads for every visitor (it's also BQD4 5 B in copy-review-005: stopping it is the theme-side fix); the mouse wheel over a live stage does not scroll the page. |
| O-9 | `page-hcs.php` Keg paragraph, on disk, not deployed | Thomas pushes the theme and purges all three caches (Cloudflare, Hostinger CDN, LiteSpeed). |
| O-10 | bareyourrare.org and thomascheesman.ca behind Cloudflare since 2026-09-20 | thomascheesman.ca has three cache layers. Full detail in handoff-014 §4. BYR's domain is on Cloudflare DNS, so hPanel shows "Domain isn't connected": **don't click "Connect domain".** |
| O-11 | bareyourrare.org crawl audit, mostly deployed | `Claude outputs/byr-crawl-audit.md`. Still open: (g) page weight. |
| O-12 | GPRS work has its own handoff | `GPRS Organization/00 Working Notes/gprs-handoff-001.md`. |

**Closed this session:**
- **Two old gallery images on thomascheesman.ca:** deleted from the media library by Thomas on 2026-09-26.
  Verified by the site's media search, with a control.
- **The theme repo's public exposure:** the repo is private (the history is O-21).
- **The six `/projects` lines in BQD0 §4 (PJ1–PJ6):** live 2026-09-26.

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
- Keep it under ~750 lines (Thomas, 2026-09-25; it was ~400). If §2 is getting long, you are
  writing a diary.
- **Every trap ends with a tally `x.y`** (Thomas, 2026-09-25).
  - **x** is the number of handoffs the trap has been carried into since the one that recorded
    it. Add 1 each time it is carried.
  - **y** is the number of sessions where the mention changed what was done. Add 1 only when
    you can name what it changed.
  - **Drop a trap when x > 5 and y ≤ 1, and at x = 10 whatever y is.** "y ≤ 1" is Thomas's
    confirmed meaning: a trap that never helped goes too.
  - *Added with it by the agent, pending Thomas's OK:*
    - A trap hit again despite its mention gets no y. Say so on the line.
    - A trap still earning its place at x = 10 belongs in code (`CLAUDE.md` rule 5).
    - A "trap" that repeats a rule already in §3 or `CLAUDE.md` is not a trap: cut it.
    - A dropped trap gets one line in §2 of the handoff that drops it, naming it, and no more.

## 6. Next up — finish the Back Quarter and the Desk

Before anything: remind Thomas once of **D-3**. He said he'll renew on 2026-10-07, and it's due 2026-10-08.
Each step ends with his ruling before the next starts. **Nothing starts that he paused** (O-20, step 2)
until he says so.

1. **PR #5.** It carries copy-review-005 step 2 and the BQD4/BQD5 lines in `/projects`. Merge it on his
   word, or let him merge it. Then curl `/projects` and compare it byte for byte with `main`.
2. **The rest of step 2** (copy-review-005):
   - BQ1–BQ7: H1 A or B, and the quote A or B.
   - DD1–DD7: H1 A or B; the DD3 flag (there's no written standard for the Desk); the two DD5 guesses at
     how he caught R-168 and R-169; "five / thirteen", KEEP or FIX.
   - P3.
3. **O-20, the Back Quarter change, in the theme repo.**
   - Plan first, and read the theme's `CLAUDE.md` and latest `V0.*.md` before touching it.
   - Answer the plan's open questions with him (O-20).
   - Once it ships, the Back Quarter copy here follows it.
4. **Previews** for both pages, in `.assetsignore`. Check them with
   `python scripts/cs_check.py work/<page> --preview --shots <dir>`, then **look at the shots**.
5. **Ship, on "ship it":**
   - The sub-menu li on all thirteen files, in the order in §1.
   - `SUBMENU` in both scripts.
   - The sitemap.
   - P3 (`/projects` trimmed, the home cards linked).
   - Then `site_check.py` locally, a negative control with `--root` on the old `public/`, and the live
     check by curl.
6. **Settle C-23** (the `/projects` lede) once both have shipped.

### After that

Phase 2, the build ledger proposal (plan-001 §4c). **Propose before building.**
