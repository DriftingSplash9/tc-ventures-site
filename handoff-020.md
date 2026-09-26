# handoff-020 — tc-ventures.ca

**Written:** 2026-09-26
**Covers:** **`/work/bare-your-rare` shipped** (Thomas: "ship it"). Before it could ship:
- **O-13 is fixed on bareyourrare.org.** The sitewide schema says `Organization`, not `NGO`.
- **The links to the unclaimed `@bareyourrare` social accounts are gone.**
- **The host fault is re-diagnosed.** Hostinger's rate limiter and LiteSpeed's CAPTCHA refuse AI
  crawlers on uncached pages. Hostinger confirmed there is no customer control, and Thomas ruled
  to leave it.

**Status at wrap:** the §2 items marked "live" were **deployed and verified live** 2026-09-26:
- tc-ventures.ca by curl (TLS verified), comparing every page byte for byte with the files the
  local browser suite passed
- bareyourrare.org by curl after Thomas purged LiteSpeed

**The browser suite was not run against the live site** (trap below).

**The next job is the Back Quarter and the Desk** (§6), starting with a receipts pass.

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. Read §2 "Traps" before you touch git, grep, line endings, a
   screenshot, the nav, a Hostinger site, or the `Reports Clustering` folder.
2. `CLAUDE.md` at repo root: the twenty truth rules. `plans/operating-guide.md` is how
   Thomas and the AI divide the work, and §4 there is the checking routine.
3. **`plans/plan-001-showcase.md`**: the plan. **The §5 note (2026-09-25)** holds the order.
   §3 lists the case studies, and §4c is the build ledger that comes after them.
4. **`plans/receipts-001.md`**: the ruled inventory, **41 OK / 74 CUT** (header, 2026-09-26). Only
   OK rows go in copy. Tick `chk` before quoting a row.
5. **`reviews/copy-review-004.md`**: the current review. The next case studies' blocks go in it,
   or in a copy-review-005 if Thomas prefers.
6. The shipped pages under `public/`. **`work/influence-graph.html` and `work/bare-your-rare.html`
   are the patterns to copy.**
7. **`scripts/`**: `site_check.py` (every page), `cs_check.py` (one case study), and
   `byr_bot_check.py` (paced user-agent test). Each script's docstring is its manual.
8. `claude/thomas-study.md` and `claude/tc-ventures-site-decisions.md` in the Claude project
   "TC 'Ventures" (not on disk, not read this session).
9. `README.md`.
10. If the job is GPRS itself, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md`.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**.

**How Thomas works:**
- Short answers when he asks for them. He's blunt when you are wrong, and he makes the calls
  himself.
- Recommend one option; don't survey.
- He rules tersely ("byr2b A, rest ok", "1", "ship it"), and that is a full ruling.
- He is self-taught and model-agnostic, so explain methods, not one model's tricks.
- When he asks how something works ("explain it like you would to someone who hasn't heard a thing
  about it"), give him the plain version first.
- **He commits and pushes himself, sometimes mid-session.** Re-read `git status` just before you
  commit.

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
| Pages | `index`, `projects`, `method`, `background`, `contact`, `404`, `work/gprs`, `work/this-site`, `work/influence-graph`, **`work/bare-your-rare`** (live 2026-09-26). Internal links, canonicals and sitemap use **clean URLs** (`/method`); `/x.html` 307s to `/x`. |
| Nav | **Projects (with a sub-menu of the case studies) · Method · Background · Contact**, on every page: **11 files** including `_template.html`. The sub-menu order is the `/projects` order: **The Economic Report Influence Graph · A rare-disease site, written by a patient · A housing society's website · This site**. The markup is copied into each page, since there is no build step. `assets/nav.js` (deferred, every page) makes the sub-menu a disclosure button. Below 420px the nav gap tightens to 14px and the nav wraps. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html` and `og-src/` off the live site. A preview goes in it until it ships. |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. Reasons are commented in the file. Unchanged since handoff-017. |
| AI crawlers | **Cloudflare answers GPTBot and ClaudeBot 403 on tc-ventures.ca;** Claude-User and ChatGPT-User get 200 (re-checked 2026-09-26). This is a setting in Thomas's Cloudflare dashboard: INFRA-15. |
| Link preview | `assets/img/og-card.png` 1200×630 on all pages, with the R2 headline. Source `public/og-src/og.html`; re-render command in its `<style>` comment (needs a local server on :8788). |
| Analytics | Cloudflare Web Analytics, injected at the edge. The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` + the audit phases (PL-6) · receipts `plans/receipts-001.md` (ruled) · `plans/operating-guide.md` |
| Design system | `public/assets/style.css` — tokens in `:root`, case-study components under the `CASE STUDIES` banner at the end |
| Graph demo | On `/work/influence-graph` only. `assets/graph-demo.js` + `gp-budget-graph.json` (snapshot committed 2026-09-16) + prebuilt `3d-force-graph.min.js`. |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. Thomas edits it himself. |
| Browser tests | **Python Playwright + Chromium, scripts in `scripts/` (INFRA-13, 2026-09-26):** `site_check.py [--live] [--root DIR] [-v]` checks every sitemap page plus /404: status, the sub-menu and both `aria-current` levels, `noindex` only on /404, no draft banner, console, 375px, the sub-menu by keyboard, and an unknown-URL 404. `cs_check.py work/<page> [--preview] [--shots DIR]` checks one case study: sections, JS off, every link, and per-section screenshots. Both serve `public/` in-process with clean URLs. |
| Research repo | `C:\Users\thoma\Desktop\My Files\Reports Clustering`. **Public on GitHub** as `DriftingSplash9/Reports-Clustering`. **Never run git there, not even `git status`** (its `CLAUDE.md` rule 1: the lock file blocks Thomas's GitHub Desktop). Read its files, and read it on GitHub through the API or raw URLs. |
| Sister repos | `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` = GitHub `DriftingSplash9/thomascheesman-ca-theme` (**public**; the old name 301s). `bareyr` (BYR) = GitHub `DriftingSplash9/bareyourrare`, **private**, so its files can't be linked as receipts. A push to its `main` deploys to Hostinger. Cached pages then need a LiteSpeed purge (Thomas, in WordPress). |

## 2. What was done (2026-09-26, after handoff-019)

**Rulings.** All in copy-review-004, "Rulings, BYR", verbatim; in short:
- **BYR1–BYR8, BYR2b and P2** are ruled, including "byr2b A, rest ok, no fig 2, q-byr7 yes".
- **The ask is in Thomas's words.** It's the two pull quotes on the page.
- **Remove the social links:** "nobody has claimed them yet".
- **Q-BYR5 "1":** leave the host limit as it is.
- **"ship it."**

**Live, and verified live:**
- **`/work/bare-your-rare`** (merge `9b2eca9`):
  - Six sections. The misses are R-140/R-141, R-147/R-149 and R-150.
  - The rules table uses `CLAUDE.md` rules 11, 6 and 2.
  - It's in the sitemap, and second in the sub-menu on all eleven files.
  - `/projects` (P2) and the home page link it.
- **Verified:**
  - The branch check-run succeeded.
  - After the merge, every sitemap page plus /404 answered 200 and was byte-identical to the
    files that passed `site_check.py` locally, with every check passing.
  - The new page's only script is `/assets/nav.js`, which the CSP allows.
  - The receipt links to this repo's files answer 200.
  - Negative control: the same suite on the pre-ship `public/` fails the sub-menu on all nine of
    its pages.
- **bareyourrare.org, `6e07481`:** the sitewide JSON-LD is `Organization`, not `NGO`, with the
  reason in a comment (O-13). After Thomas's purge, no `"NGO"` string was found on the home page, the five
  guides, `/hajdu-cheney-syndrome/`, `/about/` or `/privacy/`.
- **bareyourrare.org, `ed6b054`:** the footer's social `<nav>` and the lightbox's Instagram share
  button are removed. `inc/footer.php` has a comment saying to restore them from history once the
  accounts are claimed. Verified on uncached pages and in the optimised JS.
- **Receipts:** R-148, R-149 and R-150 are added, all OK. R-141 is un-cut. §5's `NGO` note is
  closed.

**Found, not fixed (ruled to leave):**
- **The host fault:** `Claude outputs/byr-bot-check-2026-09-25.md`, six addenda with raw logs.
  - On **uncached** pages, Hostinger's server-level rate limiter answers GPTBot an empty 429. It
    does this on all three Hostinger sites (BYR, gpresidentialsociety.com, thomascheesman.ca).
  - LiteSpeed's server CAPTCHA answers 403 "Bot Verification" (`lsrecaptcha-form`) to
    PerplexityBot and Claude-User, and now and then to a browser after a purge.
  - Cached pages are always served.
  - **Hostinger support confirmed:** there is no customer setting or allowlist on shared hosting
    (addendum 6).
  - Tried, with no effect:
    - Thomas's `.htaccess` `E=verifycaptcha:off` block (addendum 4)
    - the Hostinger "Create LLMs.txt file" toggle, now off (addendum 2)
  - **Mitigation now on (addendum 5):** the LiteSpeed Cache crawler.
    - Custom sitemap: `https://bareyourrare.org/page-sitemap.xml`.
    - Crawl interval 3600 s, down from the default 302400 s.
- **tc-ventures.ca blocks GPTBot and ClaudeBot at Cloudflare** (INFRA-15).
- **GPRS:** see O-19.

**Tooling:** `site_check.py`, `cs_check.py` and `byr_bot_check.py` are now in `scripts/`
(INFRA-13, INFRA-14b).

### Traps worth knowing

Each trap ends with its tally, **`x.y`** (§5).

**Dropped this handoff:** full-page screenshots (`6.1`, x > 5 and y ≤ 1). It is in code now:
`cs_check.py --shots`.

**New this session:**
- To check a schema type is gone, count the old type's exact string (`"NGO"`). A page carries
  several JSON-LD blocks, and seeing the new type in one of them proves nothing. That mistake
  called `/poems/` fixed when it wasn't. `0.0`
- **`cf-ray` is on every response through Cloudflare. It doesn't mean Cloudflare refused you.**
  - A Cloudflare challenge carries `cf-mitigated: challenge`.
  - `x-turbo-charged-by: LiteSpeed` means the origin answered.
  - Hostinger support made exactly this mistake. `0.0`
- **A check warms the cache it is checking.** The first request to an uncached page caches it,
  so the second request tests the cache, not the origin. Use a cache-busting query to reach the
  origin (`byr_bot_check.py GAP N bust`). `0.0`
- **Pace requests to the Hostinger sites and keep runs small.** The logged runs used a 6 s gap,
  and even then the filter refused a browser on 2 of 10 uncached pages. Bulk runs on 2026-09-26
  fell in the same hours as an account CPU peak and a database deadlock (addendum 6). `0.0`
- **The LiteSpeed Cache crawler's default interval is 302400 s (3½ days).** A purge left pages
  uncached, and so refusing crawlers, until it came round. It is set to 3600 s now. `0.0`
- **Chromium in a claude.ai cloud session rejects the session proxy's certificate**
  (`ERR_CERT_AUTHORITY_INVALID`), so `site_check.py --live` can't run there.
  - The harness refuses `ignore_https_errors`.
  - Check live with curl, which verifies TLS: compare each page byte for byte with the file the
    local suite passed.
  - On Thomas's machine, `--live` runs as written. `0.0`

**Carried:**
- `getComputedStyle(el, '::before').content` returns the CSS expression (`"Fig. "
  counter(fig)`), not the number drawn. Check figure numbering in a screenshot. `1.0`
- Pin research-repo receipts to a commit SHA. Its `HANDOFF.md` is rewritten every session and
  its files move into `archive/`. Read the first and last line of each anchored range in the
  pinned commit via `raw.githubusercontent.com`. `1.0`
- **Never start a Bash command with `cd`.** It moves the session's working directory. Use
  absolute paths, `git -C`, or `( cd … && … )`.
  - **Hit again this session despite the mention:** most commands started with `cd`. The cloud
    harness reset the directory after each one, so there was no harm this time. No y.
  - INFRA-14a. `3.0`
- `.assetsignore`, `sitemap.xml`, `projects.html`, `work/gprs.html` and
  `plans/receipts-001.md` are CRLF **in Thomas's Windows checkout**. Git stores them LF (checked
  2026-09-26).
  - Git Bash `grep -c $'\r'` can't see the carriage returns. Detect CRLF in Python and edit
    byte-wise. `2.1`
- **Heredocs mangle scripts.** Through Git Bash they eat backslashes. Unquoted (`<<EOF`), Bash
  also runs backticks, and that corrupted a Markdown addendum this session. Quote the delimiter
  (`<<'EOF'`) or write the script to a file. Hit again despite the mention: no y. `5.1`
- Run a local test server inside the Python process. A Git Bash `http.server` survives
  `pkill`. Both scripts in `scripts/` now do. `3.2`
- Headless Chrome defaults to dark mode. Set the colour scheme for each browser context. Both
  scripts do. `4.2`
- Wait about 400 ms after a click before a screenshot. `3.1`
- `/404` answers 200. Test "not found" with an unknown URL. Both scripts' negative control
  does. `2.2`
- Analytics can't be seen headless. Check that `beacon.min.js` answers 200 and the console has
  no CSP errors. `2.1`
- Cloudflare injects the beacon at the edge, so read the live console after any CSP change. A
  new inline `<script>` is blocked by the CSP; put it in `/assets/*.js`. The new page was
  checked for inline scripts and handlers before it shipped. `5.1`
- Cloudflare's build start has ranged from about 1 to 10 minutes. Check the check-run before
  diagnosing a live page. `4.1`
- A test that Tabs a fixed number of times can land on the wrong control. Loop until the
  target has focus. Both scripts loop. `2.2`
- A hidden browser pane fires no focus or blur events, so test focus logic in Playwright.
  Playwright's visibility checks see through `clip-path: inset(50%)`. `3.1`
- A receipt's "caught" column can be a guess. Open the receipt before copy says "I". `3.1`
- A figure Thomas gives can have no source on disk. Say where you searched, and ask. `2.0`
- `gh api markdown` emits no heading ids (curl the blob page for `user-content-<anchor>`), and
  `git log -S` needs `--no-textconv` here. `3.0`
- There's no LibreOffice, pandoc or `pdftoppm` on Thomas's machine. Render a `.docx` through
  Word COM, read-only, with `Quit()` in `finally`, then make page images with PyMuPDF. `2.0`

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
- A case study that takes content from `/projects` takes it unchanged. `/projects` keeps a
  short intro and a "read the case study" line (P1, P2).
- **"Honest limits" in "What shipped" states what is still wrong.** BYR's states the host limit.
  If the host or plan changes, that line goes stale (O-16).

**`/method`:**
- **The H1, the lede and the page title are Thomas's rulings.** Don't edit them, explain the
  accessibility line, or raise them again unasked.
- Research-project rows link receipts-001 §3C. That's fine, since the repo is public.

**Nav:**
- Adding a case study means editing all **eleven** files. A case study's sub-menu label is its H1,
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
- **The outside research model is never named in copy** (F-2), and no link's path may
  carry its name.
- **Don't link the `@bareyourrare` social accounts anywhere until Thomas says they are claimed**
  (O-18).

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
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Accessibility controls (motion full/reduced/off, theme, contrast, text size) are **built into the site**. OS preferences are the defaults; the toggles override them and persist. Order: Phase 1 ✓ (2026-09-25) → **Phase 1b, the remaining case studies (ruled 2026-09-25): graph ✓ → BYR ✓ (2026-09-26) → Back Quarter + Desk** → Phase 2 (the build ledger as the home hero, static SVG; plan-001 §4c) → Phase 3 (craft; **proposal first**) → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). |
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
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add `/work/gprs`, `/work/this-site`, `/method`, `/work/influence-graph`, **`/work/bare-your-rare`** and the Projects sub-menu to that run. Left from 012: one real screen-reader run through the live graph, now on `/work/influence-graph`. **Two points for it:** the loop diagrams' links sit inside an SVG with `role="img"`, which may hide them from screen readers (the same links are in `/method`'s "originals" list); and the diagrams' connectors and arrows in `--rule` are faint on white (non-text contrast). |
| A-3 | **Sub-menu without JS cannot be dismissed with Esc** | Without JS the list shows on hover or focus (WCAG 1.4.13 asks for a dismiss key). With JS, Esc works. Accepted as the no-JS fallback; for A-1 to confirm. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-13 | **The nav is copied into eleven files** | **Checker done (2026-09-26):** `scripts/site_check.py` checks every page's sub-menu, both `aria-current` levels, keyboard, 375px and console, and it failed as expected on the pre-ship `public/`. **Still manual:** the edit itself. This session's nav-edit script (`ship_byr.py`, asserted single matches) stayed in the scratchpad. A `scripts/` version that takes the new li and its position is the remaining rule-5 step. |
| INFRA-14 | **Two traps the mention doesn't prevent** | (a) **Bash `cd`** (tally `3.0`, hit again): a Claude Code `PreToolUse` hook that refuses a Bash command starting with `cd`. That changes Thomas's harness settings, so it is **his call; not built**. (b) **Full-page screenshots: done**, as `cs_check.py --shots`. |
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
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. Thomas reminded 2026-09-24, 2026-09-25 (twice) and 2026-09-26. **Not confirmed paid.** |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-16 | **Hostinger refuses AI crawlers on uncached pages: ruled leave it ("1", 2026-09-26)** | GPTBot gets an empty 429 on all three Hostinger sites, and LiteSpeed's CAPTCHA 403s PerplexityBot and Claude-User on BYR. There is no customer control on shared hosting (Hostinger support). **Mitigation:** the LiteSpeed crawler, hourly, over `page-sitemap.xml`. Only a plan change or Cloudflare HTML caching would change it; both are his call. Leave the Hostinger "Create LLMs.txt file" toggle **off**: on, it replaces the hand-written `llms.txt`. Evidence is in `Claude outputs/byr-bot-check-2026-09-25.md`. `/work/bare-your-rare`'s honest limit depends on this. |
| O-17 | **BYR `.htaccess`: Thomas's `E=verifycaptcha:off` block had no effect** | Addendum 4. Not confirmed whether it is still in the file. His call whether to take it out. |
| O-18 | **`@bareyourrare` social accounts are unclaimed** | Links removed (`ed6b054`). Restore from that commit's parent once Thomas says the accounts are claimed. |
| O-19 | **GPRS: WordPress "critical error" on uncached pages, 2026-09-26** | Seen 08:34 UTC: uncached pages (`/timeline/`, `/our-story/`, `/accessibility/`) answered 500 "There has been a critical error on this website", and some requests got no connection. The last clean check before that was about 02:35 UTC. By 09:16, `/our-story/` answered 200 uncached. At 16:42–16:45, `/`, `/our-story/` and `/accessibility/` answered 200 with no error, **but `/timeline/` reset the connection on every try (09:16, 16:42, 16:44)**. From this session the site can't be told apart from the network path. Cause unknown. **Thomas:** open `/timeline/` in a browser, and look for WordPress's critical-error email to the admin address and the error log. GPRS's own handoff owns the fix (O-12). |
| O-14 | **Research repo: 52 public file paths carry the outside model's name** | Thomas ruled 2026-09-07 that the research docs drop the name (F-2). The public archive still carries it, in paths and text. His call. Nothing was changed there. |
| O-15 | **Research repo: "read the sentence as well as fetching it" is not in its current playbooks** | It was written in `archive/NZ/G.3.md` L539 (2026-08-06). A grep of `PLAYBOOK*.md` for it, "grammatical" and "subject of" found nothing. `/work/influence-graph`'s table row uses `CLAUDE.md` rule 13 instead. His call whether the research project carries it again. |
| O-2 | `/projects` third-person leakage on thomascheesman.ca | Thomas is writing this himself. |
| O-4 | bareyourrare history contains `permits/` and `3.jpg` | Instructions in `_Quarantine\bareyourrare-history-purge.md`. Thomas runs it. |
| O-5 | `bareyr\.git` lock-file junk | Cosmetic; Thomas deletes. |
| O-6 | Rocket Lander repo not public | On hold with the lander. |
| O-7 | Children's names in the Back Quarter world | **Thomas ruled: leave them.** They stay off this site regardless. |
| O-8 | thomascheesman.ca's open items live in `V0.42.md` | `three-r128.min.js` idle-loads for every visitor; the mouse wheel over a live stage does not scroll the page. |
| O-9 | `page-hcs.php` Keg paragraph, on disk, not deployed | Thomas pushes the theme and purges all three caches (Cloudflare, Hostinger CDN, LiteSpeed). |
| O-10 | bareyourrare.org and thomascheesman.ca behind Cloudflare since 2026-09-20 | thomascheesman.ca has three cache layers. Full detail in handoff-014 §4. BYR's domain is on Cloudflare DNS, so hPanel shows "Domain isn't connected": **don't click "Connect domain".** |
| O-11 | bareyourrare.org crawl audit, mostly deployed | `Claude outputs/byr-crawl-audit.md`. Still open: (g) page weight. |
| O-12 | GPRS work has its own handoff | `GPRS Organization/00 Working Notes/gprs-handoff-001.md`. |

**Closed this session:**
- **O-13:** BYR's schema is now `Organization`, verified live after the purge.
- **`/work/bare-your-rare`:** live.
- **INFRA-14b:** per-section shots are in code.

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

## 6. Next up — the Back Quarter and the Desk

Before anything: remind Thomas once of **D-3** (the email renewal, due **2026-10-08**) if it's
still open, and ask once about **O-19** (GPRS `/timeline/`). Each step ends with his ruling
before the next starts.

### Step 1 — receipts first

- **Source:** the thomascheesman.ca theme repo's `V0.*.md` files. The repo is public, so its
  receipts can be linked.
- **Propose new rows** for receipts-001 (misses, catches, the fix, verified) for Thomas to rule
  on before any copy uses them.
- **Read every linked file against the privacy rules:**
  - no children's names, including in screenshots
  - nothing familial beyond the ruled Back Quarter childhood paragraph
  - the Rocket Lander stays private
- **"The ask" in his words:** look for a brief in the theme repo first. If none, ask him.

### Step 2 — one copy review for both, then the previews, then ship

1. **Copy review.** Blocks in the BYR pattern, in copy-review-004 or a new 005 (ask which). Then
   Thomas rules.
2. **Previews.** Put them in `.assetsignore`. Check with
   `python scripts/cs_check.py work/<page> --preview --shots <dir>`, then **look at the shots**.
3. **Ship, on "ship it".** Take out `noindex` and the banner, and remove the `.assetsignore` line.
   - Add the sub-menu li to all eleven files, in the `/projects` order.
   - Update `SUBMENU` in both scripts.
   - Add the sitemap entry and the `/projects` line.
4. **Check locally.** Run `scripts/site_check.py`, plus a negative control with `--root` on the
   old `public/`.
5. **Push, then check live.** Use `--live` on Thomas's machine. In a cloud session, curl and
   compare byte for byte (trap).
6. **Settle C-23** (the `/projects` lede) when both have shipped.

### After that

Phase 2, the build ledger proposal (plan-001 §4c). **Propose before building.**
