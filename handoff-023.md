# handoff-023 — tc-ventures.ca

**Written:** 2026-09-28
**Covers:** since handoff-022, the Back Quarter and Desk case studies went from copy to live:
- **Before this session:** another session shipped C-24 (PR #7) and recorded O-22 (PR #8). Neither wrote
  a handoff, so both are recorded here.
- **This session:**
  - The Desk re-trace found live `/projects` describing the old one-menu desk (C-25). Fixed live.
  - DD1–DD7 were ruled.
  - The previews were built and ruled on.
  - Both case studies shipped with P3, then C-23 (the `/projects` lede).
- **Phase 1b is done.** All six case studies are live.

**Status at wrap:**
- **Live on tc-ventures.ca, verified:** `main` at `7218179` (PR #11).
  - `/work/back-quarter` and `/work/desk-and-drawer` answer 200.
  - Curl: all 12 pages plus `sitemap.xml` are byte-identical to `main` (after #10). `/projects` was
    checked again after #11.
  - `site_check.py --live` passed 100 of 100 (after #10).
  - `/work/_template` answers 404, as it should.
- **thomascheesman.ca:** nothing changed this session. O-23 (the 429) and 1.0.758 are still unconfirmed.
  Thomas didn't answer the question this session.

**The next job is §6: Phase 2, the build ledger proposal.**

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. Read §2 "Traps" before you touch git, a checker script, a screenshot, the theme
   repo, a Hostinger site, or the `Reports Clustering` folder. **Especially: do not load thomascheesman.ca
   in a headless browser from Thomas's machine.**
2. `CLAUDE.md` at repo root: the twenty truth rules. `plans/operating-guide.md` is how Thomas and the AI
   divide the work, and §4 there is the checking routine.
3. **`plans/plan-001-showcase.md`**: the plan.
   - **The §5 note (2026-09-25)** holds the order.
   - **§4c** is the build ledger, next.
4. **`plans/receipts-001.md`**: the ruled inventory, 49 OK / 81 CUT. Only OK rows go in copy. Tick `chk`
   before quoting a row.
5. **`reviews/copy-review-005.md`**: every block is ruled and shipped (BQD0 through C-23). The next copy
   work opens `copy-review-006`.
6. The shipped pages under `public/`. **`work/back-quarter.html` and `work/desk-and-drawer.html` are the
   newest instances of the case-study pattern.**
7. **`scripts/`**: `site_check.py`, `cs_check.py`, `byr_bot_check.py`. Each script's docstring is its manual.
8. **If the job touches thomascheesman.ca:** the theme repo's `CLAUDE.md` and its newest `V0.*.md`
   (**V0.43**).
9. `claude/thomas-study.md` and `claude/tc-ventures-site-decisions.md` in the Claude project "TC 'Ventures"
   (not on disk, not read this session).
10. `README.md`.
11. If the job is GPRS itself, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md`.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**.

**How Thomas works:**
- Short answers when he asks for them. He's blunt when you are wrong, and he makes the calls himself.
- Recommend one option; don't survey.
- He rules tersely ("pj15-19 ok, A, dd3 A, keep, rest ok"), and that is a full ruling.
  - **Ask what a bare number means** ("1" meant OK).
  - **Say how you read a bare letter** ("A" was read as DD1's H1, the only A/B left) and record it.
- **He sometimes hands a call over** ("fix it", "up to you"). Make it, say in one line what you chose and
  why, and record it as delegated.
- **He changes his mind, and says so.** Record the new ruling next to the old one.
- **"pause here" means start nothing new.** Record what he ruled and wait.
- He is self-taught and model-agnostic, so explain methods, not one model's tricks.
- When he asks how something works, give him the plain version first.
- **He commits, pushes and merges himself, sometimes mid-session.** Re-read `git status` and `origin/main`
  just before you commit.
- **His merges don't always land** (§2 new trap). This session he asked the agent to merge #10 and #11 with
  `gh pr merge --merge`. That was per-PR permission, not a standing one.

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
| Deploy | **A merge to `main` deploys** → Cloudflare builds. **No cache to purge.** Branch pushes build too, and the bot calls them "Deployment successful", but they don't reach the site (trap below). This session #10 and #11 were live within minutes of the merge. |
| Contact email | `thomas@tc-ventures.ca` |
| Pages | `index`, `projects`, `method`, `background`, `contact`, `404`, `work/influence-graph`, `work/back-quarter`, `work/desk-and-drawer`, `work/bare-your-rare`, `work/gprs`, `work/this-site`. Internal links, canonicals and sitemap use **clean URLs** (`/method`); `/x.html` 307s to `/x`. No case study is planned. |
| Nav | **Projects (with a sub-menu of the case studies) · Method · Background · Contact**, on every page: **13 files** including `_template.html`. The sub-menu order is the `/projects` order: **The Economic Report Influence Graph · A homepage you drive around · A menu that is a photograph of my desk · A rare-disease site, written by a patient · A housing society's website · This site**. The markup is copied into each page; `assets/nav.js` makes the sub-menu a disclosure button. |
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
| Browser tests | Python Playwright + Chromium, scripts in `scripts/`:<br>- `site_check.py [--live] [--root DIR]`: every sitemap page plus /404, 100 checks now.<br>- `cs_check.py work/<page> [--preview] [--shots DIR]`: one case study. **`--preview` checks `PLANNED_SUBMENU`**, the menu a preview will ship with. It equals `SUBMENU` now; change it first for the next case study.<br>- Both serve `public/` in-process with clean URLs.<br>- **In a claude.ai cloud session:** `pip install playwright` first. The scripts launch the preinstalled Chromium by path (trap below).<br>- **`--live` is for tc-ventures.ca (Cloudflare) only. Never point a headless browser at a Hostinger site** (trap). |
| Research repo | `C:\Users\thoma\Desktop\My Files\Reports Clustering` = public `DriftingSplash9/Reports-Clustering`. **Never run git there.** Read its files, and read it on GitHub. |
| Sister repos | **Theme:** local `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` (not `Desktop\tc-ventures-child-theme`, which the global CLAUDE.md names) = GitHub `DriftingSplash9/thomascheesman-ca-theme`, **private since 2026-09-26**. A push to its `main` deploys to Hostinger; GitHub answers the push with "This repository moved" (the local remote uses the old name) and the push still lands. Cached pages then need a LiteSpeed purge and a Hostinger CDN purge (Thomas). Commit/push there is pre-authorized; bump `style.css` `Version:` on every theme-code commit. **BYR:** `bareyr` = GitHub `DriftingSplash9/bareyourrare`, **private**. A push to its `main` deploys to Hostinger, and cached pages then need a LiteSpeed purge (Thomas, in WordPress). |

## 2. What was done (2026-09-27 after handoff-022, and 2026-09-28)

**Before this session (no handoff was written for it):**
- **C-24 shipped** (PR #7, `e12f7ed`). PJ8–PJ14 put the Back Quarter copy on `/projects` and home in line
  with O-20. BQ1 and BQ6 were fixed in the draft. Thomas: "all ok, pj11 A".
- **O-22:** Thomas checked hPanel: there is no regenerate option (PR #8). See §4.

**This session. Rulings, all verbatim in copy-review-005:**
- **C-25**, the Desk re-trace, read at theme `ddbdadc` (1.0.758) without loading the site.
  - **Found:** since 2026-06-15 the plain list is the default menu. Since 2026-06-23 the header has two
    buttons: "Menu" (the plain list) and "T's Desktop" (the desk).
  - **So live `/projects` was false:** it called the desk "the site's navigation" and sent readers to
    "the button marked MENU".
  - **Also false:** the spec row said "non-fatal if either fails". Only the renderer is optional; if Matter
    fails, the pinball doesn't start.
  - **DD3's quote was from the wrong spec:** the Secret Drawer's (the escape room), not the pinball drawer's.
  - **Ruled:** PJ15–PJ19 OK. DD1 H1 A. DD3 A (only the touch-and-keyboard line). DD6 KEEP "five /
    thirteen". The rest OK, including both DD5 guesses at how Thomas caught R-168 and R-169, and P3.
- **The previews:**
  - The repeated first sentence under each "standard" H2 cut.
  - Bloom: "the painting" → "the farm" (wording delegated).
  - The desk caption: "which is a menu".
  - The R-162 link after the bloom paragraph cut.
- **C-23:** PJ20 A (the new `/projects` lede), PJ21 KEEP (both descriptions), PJ22 OK ("The Desk its
  second menu, both above, each with its own case study").

**Shipped, each verified live by curl against `main`:**
- **#9 (C-25).** Thomas's merge didn't land. It went in with #10, so GitHub shows #9 "closed", and its
  commit `61841c5` is in `main`.
- **#10 (`dcd2ed0`):**
  - Both case studies.
  - Both added to the sub-menu on all 13 files, and to the sitemap.
  - P3: `/projects` trimmed to intro, figure and "read the case study"; the home cards link the case
    studies.
  - `SUBMENU` updated in both scripts.
  - Merged by the agent at Thomas's word.
- **#11 (`7218179`):** PJ20 and PJ22. Merged by the agent at Thomas's word.

**How it was checked:**
- **Every text change:** a rendered-text check, with a control run against `main` that failed.
- **`site_check.py`:** 100 of 100, locally and `--live`. The same run on the pre-ship `public/` failed 10
  (control).
- **`cs_check.py`:** 17 of 17 on each page, both as a preview and as a live page. The same page without
  `--preview` failed on noindex, the banner and the sub-menu (control).
- **Screenshots looked at:** both pages in light, dark and at 375px, both trimmed `/projects` sections, and
  the open sub-menu at 375px.

**Tooling:**
- `cs_check.py` gained `PLANNED_SUBMENU` for `--preview`.
- The ship's edits were one script that writes nothing unless every edit matches exactly once
  (`ship.py`). It's in this session's scratchpad only; see INFRA-13.

**Found, not fixed:**
- **The open sub-menu at 375px widens the page to 379px.** It's the same on live BYR, so the new labels
  didn't cause it. DESIGN-1.

### Traps worth knowing

Each trap ends with its tally, **`x.y`** (§5).

**Dropped this handoff:**
- "Never start a Bash command with `cd`": `6.0`. Hit again this session despite the mention. INFRA-14a
  carries it.
- "A hidden browser pane fires no focus or blur events": `6.1`.
- "`gh api markdown` emits no heading ids": `6.0`.

**New this session:**
- **Thomas's "merged" may not have landed.** Twice, #9 and then #10, he said "merged" while GitHub showed
  the PR open, clean and mergeable. Run `gh pr view N --json state` before you check live or build on it.
  `0.0`
- **Theme docs name surfaces loosely.** "The drawer" in `SECRET-DRAWER-VISION.md` is the escape room, not
  the footer's pinball drawer, and the doc's own §0 says so. Read a spec's §0 before a caption says what
  it is the spec for. `0.0`

**Carried:**
- **Never load a Hostinger site in a headless browser from Thomas's machine.** Hostinger's CDN counts
  HeadlessChrome as a bot, and a few dozen loads got his home IP an empty 429 for hours. Test theme
  changes locally; ask Thomas to confirm live in his own browser; at most a couple of curls with a real
  browser UA. `platform: hostinger` + `x-hcdn-request-id` means Hostinger's edge refused you.
  - This session: C-25 was traced from the code, and the "T's Desktop" button's phone visibility was left
    unconfirmed rather than loaded. `1.1`
- **An offline rebuild of a live page can't judge a font-dependent width.** For a layout bug, the proof is
  the live page with the rule injected before load, against the same load without it. `1.0`
- **Astra's Customizer CSS beats the child theme's bare element rules.** Read the winning rule with
  DevTools' matched-rules list, not the source. `1.0`
- **Heredocs mangle scripts.** Write scripts with the Write tool. This session the check and ship scripts
  were written that way. `1.1`
- **A checker can read the wrong block, and a control can be unable to fail.** Anchor on the heading. A
  control must change a word that is in the text. This session every check ran a control. `2.2`
- **The Cloudflare bot says "Deployment successful" on branch pushes. Branch builds don't reach
  tc-ventures.ca.** Only a merge deploys. `2.0`
- **In a cloud session, `pip install playwright` installs a version whose default browser path doesn't
  exist.** Launch with `executable_path='/opt/pw-browsers/chromium'`. `2.0`
- **The cloud clone of the theme repo is shallow (50 commits).** Run `git fetch --unshallow` before
  reading history for receipts. `2.0`
- **`/projects` copy about thomascheesman.ca goes stale when the features change.** Re-trace a paragraph
  against the theme's code before a case study reuses it. This session the re-trace found the June
  two-button menu, which three months of copy had missed. `2.1`
- **To check a schema type is gone, count the old type's exact string.** `3.0`
- **`cf-ray` is on every response through Cloudflare.** A Cloudflare challenge carries
  `cf-mitigated: challenge`; `x-turbo-charged-by: LiteSpeed` means the origin answered. `3.1`
- **A check warms the cache it is checking.** Use a cache-busting query. Used this session (`?cb=`). `3.3`
- **The LiteSpeed Cache crawler's default interval is 302400 s.** It is set to 3600 s now. `3.0`
- **Chromium in a claude.ai cloud session rejects the session proxy's certificate.** Check live with
  curl instead. `3.1`
- **`getComputedStyle(el, '::before').content` returns the CSS expression, not the number drawn.** Check
  figure numbering in a screenshot. `4.0`
- **Pin research-repo receipts to a commit SHA.** Read the first and last line of each range in the
  pinned commit. `4.0`
- **Most of this repo is CRLF in Thomas's Windows checkout,** and so is most of the theme. Detect CRLF in
  Python and edit byte-wise. Used this session on every page edit. New files written by the Write tool
  are LF; Git warns and converts them. `5.4`
- **Run a local test server inside the Python process.** Used this session. `6.5`
- **Headless Chrome defaults to dark mode.** Set the colour scheme for each browser context. Used this
  session. `7.5`
- **Wait about 400 ms after a click before a screenshot.** Used this session. `6.2`
- **`/404` answers 200.** Test "not found" with an unknown URL. `5.2`
- **Analytics can't be seen headless.** Check that `beacon.min.js` answers 200 and the console has no CSP
  errors. `5.1`
- **Cloudflare's build start has ranged from about 1 to 10 minutes.** Check the check-run before
  diagnosing a live page. `7.2`
- **A test that Tabs a fixed number of times can land on the wrong control.** Loop until the target has
  focus. `5.2`
- **A receipt's "caught" column can be a guess.** Open the receipt before copy says "I". `6.2`
- **A figure Thomas gives can have no source on disk.** Say where you searched, and ask. `5.0`
- **There's no LibreOffice, pandoc or `pdftoppm` on Thomas's machine.** Render a `.docx` through Word COM,
  read-only. PHP is on the PATH (`php -l` works). `5.0`

## 3. Current design

**Pages live:**
- `/work/gprs` and `/work/this-site` (2026-09-24)
- `/method` and `/work/influence-graph` (2026-09-25)
- `/work/bare-your-rare` (2026-09-26)
- **`/work/back-quarter` and `/work/desk-and-drawer`** (2026-09-28)

**The case studies:**
- **Six fixed sections**, receipts as small mono links, figures `Fig. N` per page.
- Every claim in "What the AI got wrong" and "How I caught it" links to a receipt that returns 200
  publicly, or is cut. A receipt in a private repo (BYR's, the theme's) links its receipts-001 row
  instead.
- **"How I caught it" says "I" only for catches Thomas made.** Agent catches are written impersonally.
- **Rules-table captions say "falls under"**, not "became", unless the timing is confirmed in the receipt.
- **"The ask" quotes Thomas's own words.** If there's no brief on disk, ask him.
- A case study that takes content from `/projects` takes it unchanged, **after re-tracing it against its
  source** (BQD4 found six false lines, PJ7 a seventh, C-25 four more).
- `/projects` keeps a short intro, the figure and a "read the case study" line for each build (P1–P3). Its
  lede says each build has a case study (PJ20).
- **"Honest limits" in "What shipped" states what is still wrong.** These lines go stale when the thing
  they describe changes:
  - BYR's host limit (O-16).
  - The Back Quarter's "can't be driven on a phone or tablet yet" (O-20).
  - The Desk's "five / thirteen" (counted in `inc/desk-menu.php`).
- **A building on the Back Quarter opens on Enter.** Copy never says driving up opens it.
- **On thomascheesman.ca the plain list is the default menu.** The desk is a second menu behind "T's
  Desktop". Copy never calls the desk "the site's navigation" or points at the "Menu" button for it.
- **Theme specs are quoted verbatim with their date and section, and "The repo is private."** They are
  never linked (Q-BQD1 A).

**`/method`:**
- **The H1, the lede and the page title are Thomas's rulings.** Don't edit them, explain the
  accessibility line, or raise them again unasked.
- Research-project rows link receipts-001 §3C. That's fine, since the repo is public.

**Nav:**
- Adding a case study means editing all **thirteen** files. A case study's sub-menu label is its H1, in
  the `/projects` order. `SUBMENU` in `site_check.py` and in `cs_check.py` must change with it, and
  `PLANNED_SUBMENU` in `cs_check.py` for the preview.
- Ship the page and its link in the same push, never a link that 404s.
- Run `scripts/site_check.py` before and after (INFRA-13).

**Look and feel:**
- Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via `prefers-color-scheme`.
- Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
- Confirmed; stop re-litigating it. **Thomas, 2026-09-25: design waits until the content is mostly in
  place.** Log layout nits for Phase 3 rather than fixing them, unless a change you made caused them.

**Case-study layout (approved 2026-09-22):**
- Two lanes: a wide lane (1040px) for headers, figures, tables and lists, and a reading lane (66ch) for
  prose.
- A sticky 200px rail at ≥1180px with the section index. Below that it folds to a horizontal index.
- Sections are numbered by CSS counters, and figures `Fig. N` per page.
- Receipts are small mono links with a leading `→`.

**Home page (live 2026-09-22):**
- **Label:** "Thomas Cheesman · Grande Prairie, Alberta · remote".
- **H1:** "I run a nonprofit's website, and I hold it to a written standard."
- **Lede:** from R3/R4.
- Every project card links its case study: the graph, the Back Quarter and the Desk (P3). The "Four live
  sites" card links BYR, GPRS and this site. The "How I work" heading links `/method`.
- The lede is tall on desktop: a Phase 3 layout job, not a copy one.

**Standing rules:**
- **The Rocket Lander is private.** Not here, in any form.
- `object-fit: contain`, never `cover`.
- **Content renders without JavaScript.** JS is allowed on top (motion, 3D, controls); the words and links
  must not depend on it. No dependencies or build step — prebuilt bundles copied into `assets/` only.
- Fonts self-hosted. No third-party font request.
- No phone number on the site. It is in the résumé PDF.
- **Never publish an exact node, edge, report, grade or check count** *in copy*. Round or describe
  ("dozens"). **The app screenshot (`graph-app-ui.webp`) is the one ruled exception**, on `/projects` and
  on `/work/influence-graph` (Q-IG5).
- **No vanity metrics.** No line counts.
- **Do not invent dates or figures.** Unknown → ask Thomas.
- Hajdu-Cheney syndrome is named on purpose. Symptom detail is not. **BYR is a patient site: no symptom
  detail and no family, in copy or in any receipt it links.**
- WordPress stays once per spec table as a hiring keyword; out of headline prose.
- **Nothing familial**, except the ruled Back Quarter childhood paragraph and Thomas's Q-BQD2 quote on the
  two thomascheesman.ca case studies (Q-BQD3 A). Children's names never, including inside screenshots
  and alt text. (The desk's hotspot labels in the theme carry them; nothing on this site quotes those.)
- **Lead role: nonprofit website and digital operations.** Web development and accessibility are named
  once, as secondary (R6).
- **The résumé source is the Word file.** `resume-source.html` mirrors it — change both. Never edit the
  PDF. **Exactly two pages.** Thomas exports the PDF.
- Melanie and Thomas are "the parents" of the three children, never "co-parents".
- **New CSS is additive and token-based.** Case-study-only CSS under `.cs-body` / `.cs-*`.
- **Never ship a link that 404s**, including nav links to planned pages.
- **Copy ships only through a copy review** in the copy-review-001/002 format (numbered blocks; OK / KEEP
  / A / B / FIX / CUT). Template copy is not site copy.
- **Accessibility controls are built in, never an overlay widget** (PL-6).
- **Never link `reviews/copy-review-001.md` from a page** (T0, 2026-09-24).
- **Never run git in `Reports Clustering`.** Read its files; change nothing there unless Thomas asks.
- **The outside research model is never named in copy** (F-2), and no link's path may carry its name.
- **Don't link the `@bareyourrare` social accounts anywhere until Thomas says they are claimed** (O-18).
- **Never link a theme-repo file or commit.** The repo is private, and its handoffs and commit diffs carry
  family material. Read it for facts only. The case studies link receipts-001 §3F (Q-BQD1 A).
- **Never load a Hostinger site in a headless browser from Thomas's machine** (§2 trap).

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
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Accessibility controls (motion full/reduced/off, theme, contrast, text size) are **built into the site**. OS preferences are the defaults; the toggles override them and persist. Order: Phase 1 ✓ (2026-09-25) → **Phase 1b ✓ (2026-09-28): all six case studies live** → **Phase 2, next: the build ledger as the home hero, static SVG (plan-001 §4c); propose first** → Phase 3 (craft; **proposal first**) → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). |
| PL-8 | **Page-weight / a11y numbers: ruled ship without (2026-09-24)** | `/work/this-site` says none are shown because nothing measures them by script yet. When the Phase 4 budget script exists, the numbers go into that page's honest limits (plan-001 §6 Q5), through a copy review. |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-22 | **`/method` rules row 1 says "I caught it by using them"** (the three sliders) | The receipts confirm Thomas caught the last two (handoffs 006/007 and 032). Nothing found on how the first (`geoAffinity`) was caught. Reported as a DOUBT in copy-review-004. No change proposed. His call if he wants it narrowed. |
| C-19 | **Q-G2 unresolved: when did "read the actual code" enter the audit prompt?** | Thomas doesn't recall. The live page makes no causal claim. Don't reintroduce one. |
| C-20 | **`/work/this-site` states two things that will go stale** | "rebuild in progress" (header) and "has not had a screen-reader run-through yet" (honest limits). Update both when the rebuild ends and when A-1 is done. |
| C-15 | Résumé PDF: **site copy done**, private copy unchecked | Served PDF replaced 2026-09-23 (md5 `0da7af62…`, matches repo). Not checked: `Family & Personal\resume\Thomas_Cheesman_Resume.pdf`. Cosmetic: summary ends on a one-word line ("roles."). |
| C-16 | **Job history, from Thomas 2026-09-23. Use these** | GPRS board: elected at the **June 2023** AGM (first meeting September). Majors consulting: May 2019 – **June 2020**. **Head Chef, Ric's Grill, Sep 2013 – Jul 2014.** **Executive Chef, Township 71, Jul 2014 – Jun 2015** (renovation from Oct 2014, opened Nov 2014, closed May 2015, wind-down through June). **Taught one GPRC semester, Sep – Dec 2014.** |
| C-13 | GPRS site history | WordPress.com 2023; self-hosted WordPress.org on Hostinger 2025 "because I wanted more freedom to experiment with the code." Used in `/work/gprs`. No month-level dates without asking. |
| C-17 | R4 wording, his call | Live: "…then build it with help writing by AI." **Do not raise it again or change it unasked.** |
| C-21 | **`/method` H1, lede and title: his call (2026-09-25)** | Same standing as C-17. The H1 stands alone (Q-M5). |
| C-9 | `page-thomas.php` ~2010: "I couldn't get past my kitchen manager" | His prose and his call. Flag it, do not rewrite it. |

### DESIGN
| # | Item | Notes |
|---|---|---|
| DESIGN-1 | **The open sub-menu widens a 375px page to 379px** (seen 2026-09-28) | `#navsub-work` measures 375px wide from x=4. Same on live `/work/bare-your-rare`, so it predates the two new labels. `site_check.py` checks 375px with the sub-menu closed, so it doesn't catch this. Phase 3, and add an open-menu case to the check when it's fixed (rule 5). |

### PROJECTS / GRAPH
| # | Item | Notes |
|---|---|---|
| P-6 | A fourth project? | Nothing queued; show finished work only. |
| G-6 | Demo still is a headless render | Thomas screenshots the live demo if he wants a hand-framed one. |
| G-7 | **The demo's paragraph sits tight against its frame** | On `/work/influence-graph`: `.gd__frame` has no top margin after `.prose`. Phase 3 layout. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add `/work/gprs`, `/work/this-site`, `/method`, `/work/influence-graph`, `/work/bare-your-rare`, `/work/back-quarter`, `/work/desk-and-drawer` and the Projects sub-menu to that run. Left from 012: one real screen-reader run through the live graph, now on `/work/influence-graph`. **Two points for it:** the loop diagrams' links sit inside an SVG with `role="img"`, which may hide them from screen readers (the same links are in `/method`'s "originals" list); and the diagrams' connectors and arrows in `--rule` are faint on white (non-text contrast). |
| A-3 | **Sub-menu without JS cannot be dismissed with Esc** | Without JS the list shows on hover or focus (WCAG 1.4.13 asks for a dismiss key). With JS, Esc works. Accepted as the no-JS fallback; for A-1 to confirm. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-13 | **The nav is copied into thirteen files** | **Checker done (2026-09-26):** `site_check.py` checks every page's sub-menu. **Still manual:** the edit. This session's `ship.py` (scratchpad only) did it as all-or-nothing exact-match edits: the sub-menu li on every page lacking it, sitemap, `.assetsignore`, banner and noindex off, `SUBMENU`. A `scripts/` version that takes the new page, its label and its position is the rule-5 step. Not built. |
| INFRA-14 | **Two traps the mention doesn't prevent** | (a) **Bash `cd`** (trap dropped at `6.0` this handoff; still hit this session): a Claude Code `PreToolUse` hook that refuses a Bash command starting with `cd`. That changes Thomas's harness settings, so it is **his call; not built**. (b) **Full-page screenshots: done**, as `cs_check.py --shots`. |
| INFRA-16 | **A verbatim-quote checker in `scripts/`** | A shared script that takes the quote and the file, and runs its own control, is the rule-5 step. Not built. This session's quotes were checked by `sed` against the theme source. |
| INFRA-17 | **Theme-side test harnesses, in the scratchpad only (2026-09-27)** | (a) a page built from `front-page.php`'s Back Quarter markup + theme files, five Playwright cases; (b) an offline rebuild of a saved live page with DevTools' matched-rules list; (c) WebGL draw-call counting; (d) a live page with a rule injected by `add_init_script`. Worth a home in the theme repo (`tools/`?). **Mind the Hostinger trap:** (d) hits the live site. |
| INFRA-15 | **Cloudflare blocks GPTBot and ClaudeBot on tc-ventures.ca** | Re-checked 2026-09-26: both get 403; Claude-User and ChatGPT-User get 200. It's a setting in Thomas's Cloudflare dashboard (AI bot blocking). **His call; not raised as a recommendation.** |
| INFRA-11 | **`www.tc-ventures.ca` did not answer** | Seen 2026-09-24: curl got no response. Thomas's call whether to add a `www` → apex redirect. Raised with him 2026-09-25, and not yet ruled. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address. |
| INFRA-6 | Dead lander CSS in `style.css` (search `lander embed`) | Delete if still unused by mid-October 2026. |
| INFRA-9 | HSTS 1 yr, no `includeSubDomains`, no `preload` | Deliberate; both are hard to undo. |
| INFRA-10 | LinkedIn Post Inspector | Not confirmed run. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | Harmless; detach when convenient. |
| D-2 | WP.com plan auto-renew | Do not cancel without confirming DNS for the live sites is unaffected. |
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. Thomas reminded 2026-09-24 through 2026-09-28. **He will renew on 2026-10-07** (said 2026-09-27). **Not confirmed paid.** |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-23 | **Hostinger 429 on Thomas's home IP (2026-09-27, ~15:30 MDT on)** | Caused by headless checks (§2 trap). His phone recovered; **his PC still got 429 on 2026-09-28, about 21 hours in** (Thomas, asked at this session's wrap). That is past the "few hours" Hostinger's docs give, so live chat is the next step (his call). He lowered hPanel CDN **Security level Medium → Low**; putting it back is his call. If still blocked: Hostinger live chat, with request id `cc65655179b1a68ea57d03ef1468d64e-phx-edge6`. |
| O-25 | **The footer drawer on phones: the page may still be wider than the screen** | 1.0.758 (`baa7b24`, 2026-09-27) set the drawer's grid tracks to `minmax(0, 1fr)`. **Thomas's phone screenshot, 2026-09-28 12:38:** the header capsule sits fully inside the screen (the 1.0.758 symptom is gone), but the drawer's labels are clipped at the left edge, the quote card above it is flush left, and there's a strip of background on the right. That reads as the page scrolled sideways, so something is still wider than the viewport. **Not confirmed:** whether 1.0.758 is deployed and purged (no curl was made: the agent's curls share his blocked IP), and which element is too wide. Next: Thomas purges LiteSpeed and the Hostinger CDN, then drags the page sideways on his phone. If it still moves, find the wide element with the injected-rule method (§2 trap) from a machine Hostinger isn't blocking, or with Thomas's own browser tools. Theme work (V0.43). |
| O-24 | **thomascheesman.ca phone header, and the no-JS lede** | (a) The fixed header capsule covers the start of the "THOMAS CHEESMAN" name line on phones. (b) Without JS, `.bq-lede__name` and `.bq-lede__deck` stay at opacity 0 (`.kinetic-fade`). (c) Thomas said the menu was "wonky" before the 429s. **2026-09-28: he hasn't seen it since, and will screenshot it if he does.** (d) The phone line says "On a phone" but tablets see it too. Theme work, his call on each. |
| O-20 | **The Back Quarter: 3D on PCs only — SHIPPED 2026-09-27 (1.0.755)** | Plan and rulings: theme `docs/BQ-3D-ONLY-PLAN.md`. **3D on phones is a later job** (Thomas: "we will bring it to the mobile"). When it ships, `/work/back-quarter`'s "Where it runs" row, its honest limit and `/projects`' "A phone gets a still" line change with it. `back-quarter-3d.js`'s header comment "MOBILE PLAY … phones are IN" is stale. |
| O-21 | **Theme repo: family material in its files, history and commit diffs** | **Private since 2026-09-26.** The history still holds the material; cleaning it is Thomas's call. The details went to him in the chat on 2026-09-26, not here, because this repo is public. |
| O-22 | **Hostinger deploy webhook URL was in a public theme file for about seven weeks** | Anyone with the URL can trigger a redeploy of `main`, no more. **Checked by Thomas 2026-09-28: hPanel has no regenerate option.** Left as is: rotating means deleting and re-creating the deployment, and last time that meant moving the live theme folder aside (V0.41). **Rotate it the next time the deployment is rebuilt,** by switching to Hostinger's GitHub App method, which manages the webhook itself. Then delete the old SSH entry in hPanel and the old webhook in GitHub. |
| O-16 | **Hostinger refuses AI crawlers on uncached pages: ruled leave it ("1", 2026-09-26)** | GPTBot gets an empty 429 on all three Hostinger sites, and LiteSpeed's CAPTCHA 403s PerplexityBot and Claude-User on BYR. No customer control on shared hosting. **Mitigation:** the LiteSpeed crawler, hourly. Leave the Hostinger "Create LLMs.txt file" toggle **off**. Evidence: `Claude outputs/byr-bot-check-2026-09-25.md`. `/work/bare-your-rare`'s honest limit depends on this. |
| O-17 | **BYR `.htaccess`: Thomas's `E=verifycaptcha:off` block had no effect** | Not confirmed whether it is still in the file. His call whether to take it out. |
| O-18 | **`@bareyourrare` social accounts are unclaimed** | Links removed (`ed6b054`). Restore from that commit's parent once Thomas says the accounts are claimed. |
| O-19 | **GPRS: WordPress "critical error" on uncached pages, 2026-09-26** | Re-tested 2026-09-27: 200 cached and uncached. The critical-error email goes to WordPress's Administration Email Address; Thomas checks its junk for "Technical Issue" if he wants the cause. GPRS's own handoff owns any fix (O-12). |
| O-14 | **Research repo: 52 public file paths carry the outside model's name** | F-2. His call. Nothing was changed there. |
| O-15 | **Research repo: "read the sentence as well as fetching it" is not in its current playbooks** | It was in `archive/NZ/G.3.md` L539. His call whether the research project carries it again. |
| O-2 | `/projects` third-person leakage on thomascheesman.ca | Thomas is writing this himself. |
| O-4 | bareyourrare history contains `permits/` and `3.jpg` | Instructions in `_Quarantine\bareyourrare-history-purge.md`. Thomas runs it. |
| O-5 | `bareyr\.git` lock-file junk | Cosmetic; Thomas deletes. |
| O-6 | Rocket Lander repo not public | On hold with the lander. |
| O-7 | Children's names in the Back Quarter world | **Thomas ruled: leave them.** They stay off this site regardless. |
| O-8 | thomascheesman.ca's open items live in its newest `V0.*.md` (V0.43) | `three-r128.min.js` idle-loads for every visitor: **ruled keep on phones (2026-09-27), now 1x/~20 fps there** (stated in `/work/back-quarter`'s honest limits). The mouse wheel over a live stage does not scroll the page. |
| O-9 | `page-hcs.php` Keg paragraph, on disk, not deployed | Thomas pushes the theme and purges all three caches. **Check before the next theme push that it isn't swept in.** Not re-checked this session (no theme commit). |
| O-10 | bareyourrare.org and thomascheesman.ca behind Cloudflare since 2026-09-20 | thomascheesman.ca has three cache layers. Full detail in handoff-014 §4. BYR's domain is on Cloudflare DNS: **don't click "Connect domain"** in hPanel. |
| O-11 | bareyourrare.org crawl audit, mostly deployed | `Claude outputs/byr-crawl-audit.md`. Still open: (g) page weight. |
| O-12 | GPRS work has its own handoff | `GPRS Organization/00 Working Notes/gprs-handoff-001.md`. |

**Closed since handoff-022:**
- **C-24:** live 2026-09-28 (PR #7).
- **C-23:** PJ20 A, PJ21 KEEP, PJ22 OK. Live 2026-09-28 (#11).
- **The Back Quarter and Desk case studies, and P3:** live 2026-09-28 (#10). copy-review-005 is fully
  ruled and shipped.
- **O-22:** checked; rotation deferred to the next rebuild (row kept as a reminder).

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

## 6. Next up — Phase 2, the build ledger

Before anything: remind Thomas once of **D-3**. He said he'll renew on 2026-10-07, and it's due 2026-10-08.
Each step ends with his ruling before the next starts.

1. **Ask, don't test (O-23, O-25).** Ask Thomas whether his PC loads thomascheesman.ca yet, and whether his
   phone page still slides sideways after he purged the caches (O-25). The "wonky" menu (O-24 c): he
   hasn't seen it again and will send a screenshot if he does; don't ask again.
2. **Phase 2: propose the build ledger** (plan-001 §4c): the home hero as a static SVG ledger. **Propose
   before building.** Read plan-001 §4c and §5, and the home page as it is, first. The proposal names:
   - what the ledger shows and where each entry's facts come from (receipts only, no invented dates or
     counts, no exact counts in copy);
   - how it renders without JS;
   - what it replaces on the home page.
   Copy for it opens `reviews/copy-review-006.md`.
3. **Rule-5 work, if Thomas wants it before Phase 2:**
   - INFRA-13, a `scripts/` nav-and-ship tool from this session's `ship.py`;
   - DESIGN-1's open-menu case in `site_check.py`.
   Both are his call on order.

### After that

Phase 3 (craft), proposal first. DESIGN-1 and G-7 wait for it.
