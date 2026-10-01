# handoff-028 — tc-ventures.ca

**Written:** 2026-10-01
**Covers:** the rest of the session handoff-027 began, 2026-09-30 to 2026-10-01:
- **LG28 ruled; ledger column 027 live** (PR #31, which also landed #30, handoff-027).
- **M3, the method loop,** ruled "A" (M3 before the traps layer); shipped as PR #32.
- **DESIGN-5 found and fixed:** Chrome settles a page's view-transition opt-in before a late `style.css`
  arrives. The opt-in is inline now (#33). With it holding live, the checker's retries and TS1's sentence
  came out (#34, TS2 "A").
- **C-22,** ruled "c22 A": `/method` rules row 1 narrowed to the two catches with receipts (#35).

**Status at wrap:**
- **Live on tc-ventures.ca, verified 2026-10-01:** `main` at `f4ee703` (PR #35). Each of #31 to #35 was
  merged by the agent at Thomas's word, each after a separate state check.
  - The check-run "Workers Builds: tc-ventures-site" on `f4ee703` completed with success at 14:47:35 UTC.
  - Curl, cache-busted: `/method` is byte-identical to `main`, and differs from the pre-merge `eb9f887`.
    #31 to #34's changed files were checked the same way when each merged (§2).
  - `site_check.py --live`: 200 of 201, then 201 of 201 twice. The failure was M2 on a slow load
    (DESIGN-6, new).
- **thomascheesman.ca:** nothing changed from this session.
- **LG29,** this handoff's ledger line, is drafted in copy-review-006 with `"ruled": null`. The live ledger
  stops at 027 until it's ruled.

**The next job is §6.**

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. Read §2 "Traps" before you touch git, a checker script, a screenshot, the
   app's browser pane, the theme repo, a Hostinger site, or the `Reports Clustering` folder. **Especially:
   do not load thomascheesman.ca in a headless browser from Thomas's machine.**
2. The twenty truth rules: in Thomas's global `C:\Users\thoma\.claude\CLAUDE.md` and, as of this wrap,
   still in this repo's `CLAUDE.md` too (§4 INFRA-20). `plans/operating-guide.md` is how Thomas and the AI
   divide the work, and §4 there is the checking routine.
3. **`plans/plan-001-showcase.md`**: the plan. The §5 note (2026-09-25) holds the order.
4. **`reviews/copy-review-007.md`: Phase 3.**
   - Steps 2 to 5, M3 and DESIGN-5 are built, ruled and live; C22 too.
   - **What's left of Phase 3:** the ledger's traps layer (PL-9), and DESIGN-6.
5. **`plans/receipts-001.md`**: the ruled inventory, 49 OK / 81 CUT. Only OK rows go in copy. Tick `chk`
   before quoting a row.
6. **`reviews/copy-review-006.md`**: the build ledger's rulings. LG29, this handoff's line, is drafted there.
7. The shipped pages under `public/`. **`work/back-quarter.html` and `work/desk-and-drawer.html` are the
   newest instances of the case-study pattern.** The home hero ends with the build ledger and its scrubber
   (§3).
8. **`scripts/`**: each script's docstring is its manual.
   - The checkers: `site_check.py`, `cs_check.py`, `byr_bot_check.py`, `shots_diff.py`, `quote_check.py`.
   - The writers: `export-ledger.py` (plus `ledger/curation.json`), `patch.py`, `ship_case_study.py`.
9. **If the job touches thomascheesman.ca:** the theme repo's `CLAUDE.md` and its newest `V0.*.md`
   (V0.46 when last read), and `docs/IMAGE-BURST-PLAN.md`.
10. `claude/thomas-study.md` and `claude/tc-ventures-site-decisions.md` in the Claude project "TC 'Ventures"
    (not on disk, not read this session).
11. `README.md`.
12. If the job is GPRS itself, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md`.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**.

**How Thomas works:**
- Short answers when he asks for them. He's blunt when you are wrong, and he makes the calls himself.
- Recommend one option; don't survey.
- He rules tersely ("ts2 A, merge 34"), and that is a full ruling.
  - **Ask what a bare number means** ("1" meant OK).
  - **Say how you read a bare letter** and record it. This session "A" after a three-way question was read
    as its option A; "a" with one open question as that question's A.
  - **"do the next handoff" meant: work through the newest handoff's §6.** Read that way and confirmed by
    his next ruling.
- **He sometimes hands a call over** ("fix it", "up to you"). Make it, say in one line what you chose and
  why, and record it as delegated.
- **He changes his mind, and says so.** Record the new ruling next to the old one.
- **"pause here" means start nothing new.** Record what he ruled and wait.
- He is self-taught and model-agnostic, so explain methods, not one model's tricks.
- When he asks how something works, give him the plain version first.
- **He commits, pushes and merges himself, sometimes mid-session.** Re-read `git status` and `origin/main`
  just before you commit.
- **His merges don't always land** (§2 trap).
  - This session he said "merge 31" to "merge 35", and the agent merged each.
  - Each was per-PR permission, not a standing one.
- **He does dashboard work himself** (Cloudflare, WordPress.com), with the agent giving the steps and
  checking the result by curl. A screenshot of where he's stuck is his way of asking.
- **He may be working in his own Chrome while you use the app's browser pane.** The pane draws only while
  the Claude window is in front (§2 trap). Ask him to bring it forward; he will.

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
| Deploy | **A merge to `main` deploys** → Cloudflare builds. **No cache to purge.** Branch pushes build too, and the bot calls them "Deployment successful", but they don't reach the site (trap below). This session's five merges were each live at the first curl, after their merge commit's check-run completed. |
| Addresses | **`www.tc-ventures.ca` 301s to `https://tc-ventures.ca`, keeping the path and query.** **Always Use HTTPS is on.** Cloudflare serves documents over HTTP/3 (`h3`) to Chrome. |
| Contact email | `thomas@tc-ventures.ca` |
| Pages | `index`, `projects`, `method`, `background`, `contact`, `404`, `work/influence-graph`, `work/back-quarter`, `work/desk-and-drawer`, `work/bare-your-rare`, `work/gprs`, `work/this-site`. Internal links, canonicals and sitemap use **clean URLs** (`/method`); `/x.html` 307s to `/x`. No case study is planned. |
| Nav | **Projects (with a sub-menu of the case studies) · Method · Background · Contact**, then the **Display** button, on every page: **13 files** including `_template.html`. The sub-menu order is the `/projects` order: **The Economic Report Influence Graph · A homepage you drive around · A menu that is a photograph of my desk · A rare-disease site, written by a patient · A housing society's website · This site**. `assets/nav.js` makes the sub-menu a disclosure button. **To ship a case study, run `scripts/ship_case_study.py`** (§3). |
| Display settings | **`assets/prefs.js`**, loaded without `defer` in every `<head>`, puts the saved choices on `<html>` (`data-motion`, `data-theme`, `data-contrast`, `data-text`) before the first paint. **`assets/display.js`** builds the panel. Saved in `localStorage` under `tcv-display`, this browser only. Rules: §3. |
| Motion | **M1:** the opt-in `<style>@view-transition { navigation: auto; }</style>` **inline in each page's `<head>`** (DESIGN-5); its names and times in `style.css`; the page-swap hooks in `prefs.js`. **M2 and the scrubber:** `assets/ledger.js`, `defer`, home only. **M3:** `assets/loop.js`, `defer`, `/method` only, and the `.is-tracing` block in `style.css`. Rules: §3. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html` and `og-src/` off the live site. A preview goes in it until it ships. |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. **No inline script** (CSP `script-src 'self'`); inline `<style>` and `style=""` are allowed. Unchanged since handoff-017. |
| AI crawlers | **Allowed since 2026-09-30 (INFRA-15 ruled B).** `robots.txt` allows all. The setting is in Thomas's Cloudflare dashboard (AI Crawl Control). |
| Link preview | `assets/img/og-card.png` 1200×630 on all pages. Source `public/og-src/og.html`. |
| Analytics | Cloudflare Web Analytics, injected at the edge for browsers (curl doesn't see it). The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` · receipts `plans/receipts-001.md` · `plans/operating-guide.md` · Phase 3 `reviews/copy-review-007.md` |
| Design system | `public/assets/style.css` — tokens in `:root` (type in rem; theme, contrast and motion tokens after it, then M1's view-transition names and times), case-study components under the `CASE STUDIES` banner, the loop diagram (with M3), then the `build ledger` block at the end. **Every width breakpoint is in `em`** (§3). |
| Build ledger | The end of the home hero. Written into `public/index.html` between `<!-- ledger:begin … -->` and `<!-- ledger:end -->` by `scripts/export-ledger.py`, from the handoffs plus `ledger/curation.json` (not deployed). **Never hand-edit the block.** A landscape SVG, a portrait SVG shown at 37.5em (600px) and under, the scrubber (scripts only), and a `<details>` list with one ruled line per handoff. Rules: §3. |
| Graph demo | On `/work/influence-graph` only. `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js`. It reads the site's motion setting. |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. |
| Browser tests | Python Playwright + Chromium, scripts in `scripts/`:<br>- `site_check.py [--live] [--root DIR] [--draft-ledger] [-v]`: every sitemap page plus /404, the home ledger, the theme and contrast, the Display panel, and **the motion: M1 at each level (one try each, `M1_TRIES` = 1), M1 with `style.css` held back 300ms, M2, M3, the scrubber**. **201 checks, no known faults** (but DESIGN-6 can fail M2 live).<br>- `cs_check.py work/<page> [--preview] [--shots DIR]`: one case study.<br>- **`shots_diff.py BEFORE [AFTER] [--self] [--inject CSS]`**: every page, light and dark, 1280 and 375, pixel for pixel between two copies of `public/`. Run `--self` and `--inject` as controls (the footer is `footer`).<br>- All of them serve `public/` in-process with clean URLs.<br>- **Playwright's default Chromium is the headless shell, started with `PaintHolding` and `RenderDocument` switched off** (trap). **Playwright disables the HTTP cache once a route is set**, so a routed request always reaches the handler.<br>- **In a claude.ai cloud session:** `pip install playwright` first; the scripts launch the preinstalled Chromium by path.<br>- **`--live` is for tc-ventures.ca (Cloudflare) only. Never point a headless browser at a Hostinger site** (trap). |
| Edit tools | **`patch.py`**: exact-match edits across files, all or none, keeping each file's line endings. **`ship_case_study.py`**: ships case-study previews (§3). **`quote_check.py FILE "quote"…` / `--ledger`**: each quote verbatim in its source, and each piece is its own control. |
| Claude Code hook | **`.claude/settings.json`** (this repo only, ruled INFRA-14a A): a `PreToolUse` hook runs `.claude/hooks/no_cd.py`, which refuses a Bash command whose first word is `cd`. |
| Research repo | `C:\Users\thoma\Desktop\My Files\Reports Clustering` = public `DriftingSplash9/Reports-Clustering`. **Never run git there** from this project's sessions. Read its files (its old handoffs are under `archive/Previous Handoffs/`), and read it on GitHub. |
| Sister repos | **Theme:** local `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` = GitHub `DriftingSplash9/thomascheesman-ca-theme`, **private since 2026-09-26**. A push to its `main` deploys to Hostinger; GitHub answers the push with "This repository moved" and the push still lands. Cached pages then need a LiteSpeed purge and a Hostinger CDN purge (Thomas). Commit/push there is pre-authorized; bump `style.css` `Version:` on every theme-code commit. **BYR:** `bareyr` = GitHub `DriftingSplash9/bareyourrare`, **private**. A push to its `main` deploys to Hostinger, then a LiteSpeed purge (Thomas). **`.htaccess` is not in the BYR repo**; it lives on the server only. |

## 2. What was done (2026-09-30 to 2026-10-01, after handoff-027)

**Rulings, verbatim:**
- "merge 30, lg28 ok, do the next handoff" ("do the next handoff" read as: work through handoff-027 §6).
- **"merge 31, A"**: A on handoff-027 §6 step 2's question, M3 now and the traps layer later.
- "merge 32", "go ahead with DESIGN-5", "merge 33", **"ts2 A, merge 34"**, "go ahead with C-22",
  **"c22 A"**, "merge 35, then write handoff-028".

**Shipped, each checked live (merge commit's check-run, then curl against `main` with a pre-merge control,
then `site_check.py --live`):**
- **#30** (merge `2eab0b0`): handoff-027 and LG28's draft. Not part of the site.
- **#31** (merge `75c7d6c`): ledger column 027 (LG28). Live 199 of 199.
- **#32** (merge `1673dcd`): **M3**, the method loop traces itself once (§3). Live 200 of 200.
- **#33** (merge `12bf939`): **DESIGN-5's fix**, the M1 opt-in inline on all 13 pages and out of
  `style.css`; a new check holds `style.css` back 300ms. Live: **0 skips in 24 plain M1 runs** (about 40%
  before).
- **#34** (merge `eb9f887`): `M1_TRIES` back to 1; TS2 A, TS1's sentence cut from `/work/this-site`.
  Live 201 of 201.
- **#35** (merge `f4ee703`): **C22 A**, `/method` rules row 1 ends "I caught the last two by using them."
  Live 200 of 201 (M2, DESIGN-6), then 201 of 201 twice.

**How DESIGN-5 was found** (the full record is in copy-review-007, "DESIGN-5"):
- **Not the network:**
  - Locally, 0 skips of 60 with HTTPS (a self-signed cert), Cloudflare's revalidation headers, the live
    security headers and latency.
  - Live, the protocol is HTTP/3. With QUIC off, 5 of 12 skipped, the same as with it on.
- **The new page owned the skip.** An `unhandledrejection` listener put "AbortError: Transition was
  skipped" on `/work/gprs`. Skips came when the new page's first paint followed the end of parsing.
- **Reproduced locally by holding `style.css` back:** 10 of 10 skipped at 100ms and at 300ms, even with
  our scripts emptied. Holding `prefs.js` back instead: 0 of 10.
- **The fix:** the opt-in inline. 0 of 10 at both delays.
- **The checks:** `main` fails the new check 3 of 3. `shots_diff.py` 48 of 48 identical.

**How M3 was checked** (copy-review-007, "M3"):
- Controls, each failing M3 only:
  - the script ungated and the times without `--move`;
  - two steps swapped;
  - tracing at load.
- The script ungated alone could not fail the check: under Reduced, `--move` makes every time 0. That
  control was paired with removing `--move`, on purpose.
- `shots_diff.py` 48 of 48 identical. Frames looked at, before and after the return arrow got its pulse.

**C22's evidence:** the research repo's handoffs 006 and 007 (L15) and 032 (L225–238), read in
`archive/Previous Handoffs/`. All 8 quotes passed `quote_check.py`.

**Found in the data:**
- **DESIGN-5's cause:** Chrome settles a new page's `@view-transition` opt-in before a late stylesheet
  arrives. Live, `style.css` is revalidated (304) on every change of page, so it was sometimes late.
- **#28's "quiet" handling never covered DESIGN-5's skips.** They rejected on the new page before
  `prefs.js` ran. Recorded as a correction in copy-review-007.
- **DESIGN-6 (new), M2 on a slow load:** on one live run the first paint came at 816ms and `ledger.js`
  clipped the threads at 851ms, after it. So the whole ledger can show for a moment before the draw-in
  starts. 1 failure in 3 live runs at wrap. It is a likely, unconfirmed match for an earlier 200 of 201
  whose failure wasn't captured.

**Own misses:**
- **A third empty `python -`** this session, hung until stopped. It wrote nothing. INFRA-19.
- **A live check's output filtered to the M1 lines,** so one failing check went uncaptured. The likely
  candidate is DESIGN-6, unconfirmed.
- **The first C22 draft quoted with stray Markdown marks** (`**`, `*"`) from the source. Caught before
  `quote_check.py` ran; redone as clean verbatim pieces, 8 of 8.
- **Git Bash turned `-subj "/CN=localhost"` into a Windows path.** Caught by openssl's error; rerun with
  `MSYS_NO_PATHCONV=1`.

**Found, not fixed:** DESIGN-6 (§4).

### Traps worth knowing

Each trap ends with its tally, **`x.y`** (§5).

**Dropped this handoff:**
- "A cross-document view transition can pass locally and skip live": `1.1`. Not a trap any more. Its
  cause is a §3 rule now (the inline opt-in), with a check that fails without it.
- "An offline rebuild of a live page can't judge a font-dependent width": `6.0`.
- "Astra's Customizer CSS beats the child theme's bare element rules": `6.0`.
- "Most of this repo is CRLF in Thomas's Windows checkout": `10.9`. It's in code: `patch.py`.
- "`/404` answers 200": `10.2`. It's in code: `site_check.py`'s negative control.
- "A test that Tabs a fixed number of times can land on the wrong control": `10.3`. It's in code: the
  checkers loop until focus.

**New this session:**
- **Git Bash rewrites an argument that starts with `/` into a Windows path** (`/CN=localhost` became
  `C:/Program Files/Git/CN=localhost`). Set `MSYS_NO_PATHCONV=1` for that command. `0.0`
- **Keep every FAIL line of a check run.** A filter on the lines you expect hides the one that fails, and
  a flaky failure may not come back. `0.0`

**Carried:**
- **Playwright's default Chromium is the headless shell, started with `PaintHolding` and `RenderDocument`
  switched off** (`Browser.getBrowserCommandLine` shows it). `1.0`
- **The app's browser pane draws only while the Claude window is in front and the pane is showing.**
  `tabs_context` says "hidden", or a screenshot times out: clicks fail and a motion test means nothing.
  `1.0`
- **A Playwright full-page screenshot drops CDP `Page.setFontSizes`.** Take viewport screenshots when the
  browser's text size is set. `2.0`
- **Lazy, async-decoded images can paint as empty boxes in a Playwright full-page screenshot.**
  `shots_diff.py` forces the decode. `3.0`
- **Python on Thomas's console prints in cp1252, and a `→` or `’` crashes it.** Run with
  `PYTHONIOENCODING=utf-8`. This session's runs did. `3.3`
- **`git rev-parse --short` takes one revision.** `3.0`
- **PowerShell 5.1 splits an inline argument at its embedded double quotes.** Write a message or PR body
  to a file. This session every PR body went through a file. `4.4`
- **A gate must run on its own, then you act.** This session each merge's state check ran as its own
  command first. `4.4`
- **Thomas's "merged" may not have landed.** Run `gh pr view N --json state` before you check live or build
  on it. This session each merge's state was read after the merge. `5.5`
- **Theme docs name surfaces loosely.** Read a spec's §0 before a caption says what it is the spec for.
  `5.0`
- **A 429 behind Cloudflare may not be about your IP.** If Cloudflare proxies to a second CDN
  (`*.cdn.hstgr.net`), that CDN's per-IP limit counts Cloudflare's edge IPs. `x-hcdn-*` means Hostinger's
  CDN; `x-turbo-charged-by: LiteSpeed` + `panel: hpanel` means the origin. `5.0`
- **Never load a Hostinger site in a headless browser from Thomas's machine.** Hostinger's CDN counts
  HeadlessChrome as a bot, and a few dozen loads got his home IP an empty 429 for hours. `6.2`
- **Heredocs mangle scripts, and `python -` with nothing on stdin waits forever.** Write scripts with the
  Write tool. **Hit again since handoff-027** (a `python -` left at the front of a command), so no y
  (INFRA-19). `6.3`
- **A checker can read the wrong block or field, and a control can be unable to fail.** Anchor on the
  heading; a control must change something the check reads. This session it shaped M3's controls: the
  ungated script alone could not fail, so it was paired. `7.5`
- **The Cloudflare bot says "Deployment successful" on branch pushes. Branch builds don't reach
  tc-ventures.ca.** Only a merge deploys. This session each live check waited on the merge commit's
  check-run. `7.5`
- **A check warms the cache it is checking.** Use a cache-busting query. This session's curls used `?cb=`.
  `8.8`

## 3. Current design

**Pages live:**
- `/work/gprs` and `/work/this-site` (2026-09-24)
- `/method` and `/work/influence-graph` (2026-09-25)
- `/work/bare-your-rare` (2026-09-26)
- `/work/back-quarter` and `/work/desk-and-drawer` (2026-09-28)
- The Display panel on every page (2026-09-29)
- The step 4 layout on every page (2026-09-30)
- The step 5 motion (2026-09-30); M3 on `/method` (2026-10-01)

**The case studies:**
- **Six fixed sections**, receipts as small mono links, figures `Fig. N` per page.
- Every claim in "What the AI got wrong" and "How I caught it" links to a receipt that returns 200
  publicly, or is cut. A receipt in a private repo (BYR's, the theme's) links its receipts-001 row
  instead.
- **"How I caught it" says "I" only for catches Thomas made.** Agent catches are written impersonally.
  **The same goes for `/method`** (C22: "I caught the last two by using them").
- **Rules-table captions say "falls under"**, not "became", unless the timing is confirmed in the receipt.
- **"The ask" quotes Thomas's own words.** If there's no brief on disk, ask him.
- A case study that takes content from `/projects` takes it unchanged, **after re-tracing it against its
  source**.
- `/projects` keeps a short intro, the figure and a "read the case study" line for each build. Its lede
  says each build has a case study (PJ20).
- **"Honest limits" in "What shipped" states what is still wrong.** These lines go stale when the thing
  they describe changes:
  - BYR's host limit (O-16).
  - The Back Quarter's "can't be driven on a phone or tablet yet" (O-20).
  - The Desk's "five / thirteen" (counted in `inc/desk-menu.php`).
- **A building on the Back Quarter opens on Enter.** Copy never says driving up opens it.
- **On thomascheesman.ca the plain list is the default menu.** The desk is a second menu behind "T's
  Desktop".
- **Theme specs are quoted verbatim with their date and section, and "The repo is private."** They are
  never linked (Q-BQD1 A).

**`/method`:**
- **The H1, the lede and the page title are Thomas's rulings.** Don't edit them, explain the
  accessibility line, or raise them again unasked.
- Research-project rows link receipts-001 §3C.

**Nav:**
- **To ship a case study, run `python scripts/ship_case_study.py work/<slug> [work/<slug> …]`** (`--dry-run`
  first). It refuses, writing nothing, unless `PLANNED_SUBMENU`, the live sub-menu, every page and
  label = H1 agree. It doesn't touch `/projects` or the home cards: that's copy.
- A preview carries the sub-menu it will ship with. Set `PLANNED_SUBMENU` in `cs_check.py` first.
- Ship the page and its link in the same push, never a link that 404s.
- **Any other edit to the nav or the header** is a 13-file edit. Do it with a `patch.py` script.
- **In the header's phone layout (45em and under)** the open sub-menu is capped to the screen (DESIGN-1).
- **The label is the H1** (a standing rule), and M1 depends on it.
- **A new page carries the inline M1 opt-in** in its `<head>`, before the stylesheet link, as the 13 do
  (`_template.html` has it).

**Layout at any text size (step 4):**
- **Width breakpoints are in `em`, never `px`.** A new breakpoint is written in `em`.
- **A grid column that holds text is `minmax(0, 1fr)`, not `1fr`.**
- **`body` has `overflow-wrap: break-word`.** Receipts are `inline-block`. The stacked rules table (40em
  and under) is `table-layout: fixed`.
- **To check text at 200%, set it the way the browser does** (CDP `Page.setFontSizes`). Screenshot it
  with viewport shots only.
- **The home lede is 52ch** (`.hero--home .hero__lede`).

**The Display panel (live 2026-09-29):**
- **The button:** "Display", after the nav; it shows only when scripts run. If `display.js` fails to load
  while scripts run, the button shows and does nothing (accepted).
- **The panel:** four radio rows (Motion: System · Full · Reduced · Off; Theme: System · Light · Dark;
  Contrast: System · Standard · More; Text size: Standard · Large · Larger) and "Saved in this browser
  only." (DP1–DP3).
- **System means no mark on `<html>`:** the OS decides through plain CSS.
- **Motion:**
  - Anything that moves takes its time as `calc(<time> * var(--move))`, any fade as
    `calc(<time> * var(--fade))`. Reduced sets `--move: 0`; Off sets both to 0 and switches off every
    transition and animation.
  - Under System, the OS's "reduce motion" means Reduced (Q-P3-2 A).
  - **New motion must follow this.** Scripts ask `window.tcvMotion()` (`prefs.js`).
- **Theme:** the dark colours are written once, as `--dark-*`; **a new colour token gets a dark value in
  the same pattern**.
- **Contrast More:** the `-more` colours, text 7:1 and rules 3:1 on both grounds, 3px focus rings.
- **Type:** HTML text in rem; SVG labels in px. Large is 112.5% and Larger 125%, on the root.

**The motion (copy-review-007):**
- **M1, page to page:**
  - **The opt-in is inline in each page's `<head>`, never in `style.css`** (DESIGN-5). Chrome settles
    the new page's opt-in before a late stylesheet arrives. `site_check.py` holds `style.css` back 300ms
    and needs the transition every time.
  - Chrome/Edge 126+ and Safari 18.2+; others change pages as before.
  - The top bar is `topbar`, and **its three parts are named apart** (`tb-name`, `tb-nav`, `tb-display`):
    they slide over `--move` (0.35s), because the case-study lane puts them elsewhere. The rest
    cross-fades over `--fade` (0.25s).
  - **Under Full only,** `prefs.js` names the clicked `#navsub-work` link and the new page's `main h1`
    `cs-title` for that one change of page (0.5s), and clears them after.
  - Reduced: the cross-fade, nothing moving. Off: `prefs.js` skips the transition on both pages.
  - `prefs.js` handles the promises of any transition it sees (`quiet()`).
- **M2, the draw-in:** under Full, `ledger.js` clips the threads to 001 and draws them to the newest (0.11s
  a handoff) the first time the ledger is 35% in view. Reduced and Off: whole from the start. Touching
  the slider stops it. **On a slow load the clip can come after the first paint** (DESIGN-6).
- **M3, the method loop:** under Full, the first time `/method`'s loop diagram is half in view,
  `loop.js` adds `.is-tracing`. Each step and arrow pulses teal in the loop's order (0.5s each, 0.22s
  apart, `--k` 0 to 10), then the dashed return arrow (1.2s). It only highlights what is drawn, so
  nothing is hidden before it runs.
- **The scrubber:**
  - A native `<input type="range">` under the picture, inside the figure, one step per handoff,
    starting at the newest. Label LS1, "Step through the handoffs" (curation `copy.scrub`).
  - Moving it clips both pictures' threads at that column, marks the column (`lg__col--on`) and shows
    that handoff's line.
  - **At a past handoff a thread that closed later is drawn open** (Q-S5-1 B; `data-e` from the export,
    `lg__then-open` from `ledger.js`).
  - **All lines are stacked in one grid cell**, so its height never changes.
  - The spoken value: "handoff-017, 2026-09-24: <the ruled line>".
  - In landscape its track ends sit under the first and last columns (`--lg-from`, `--lg-to`, written by
    the export from `svg_land`'s `LEFT`, `RIGHT` and `W`, minus half a 16px thumb).
  - Scripts only; the list carries every line without them. **The export leaves the scrubber out unless
    `copy.scrub.ruled` is set.**

**Look and feel:**
- Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode by the OS or the Display panel.
- Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
- Confirmed; stop re-litigating it.

**Case-study layout (approved 2026-09-22):**
- Two lanes: a wide lane (1040px) for headers, figures, tables and lists, and a reading lane (66ch) for
  prose. A sticky 200px rail at 73.75em and wider with the section index.
- Sections are numbered by CSS counters, figures `Fig. N` per page. Receipts are small mono links with a
  leading `→`.

**Home page:**
- **Label:** "Thomas Cheesman · Grande Prairie, Alberta · remote".
- **H1:** "I run a nonprofit's website, and I hold it to a written standard."
- **Lede** from R3/R4, 52ch. **R5 under it is one sentence**: "I am looking for remote work running a
  nonprofit's website and digital operations."
- Every project card links its case study. The "How I work" heading links `/method`.

**The build ledger (copy-review-006):**
- **Order in the hero:** label, H1, lede, R5, the buttons, then the ledger (pictures, scrubber, caption),
  then its list.
- **The block is generated.** To change it: edit `ledger/curation.json` or the handoffs; run
  `python scripts/export-ledger.py`, then `--check`, then `site_check.py`; ship.
- **A handoff's column appears only once its line is ruled** (`ruled` in the curation). At wrap:
  1. Draft the new handoff's line in copy-review-006 (LG29 for 028, LG30 for 029, and so on).
  2. Add it to the curation with `"ruled": null`.
  3. Run `python scripts/quote_check.py --ledger` on its "Rests on" quotes.
  4. After Thomas rules, set `ruled`, export and ship.
- **A line** never copies handoff prose, says "I" only for what Thomas did, and leaves out the private
  project, other sites' incidents and anything familial.
- **Items are drawn solid unless the curation's `parked` lists them** (dotted). **Parking only changes a
  thread still open at the last column;** a closed thread draws closed whether parked or not.
- **What's never drawn:** O-\* and L-\* items, and rows under OTHER REPOS or LANDER.
- **A new §4 workstream heading stops the export** until the curation's `bands`, `fold` or `exclude` says
  where it goes.
- **An ID whose wording changes is a DOUBT in `--report`** until `reviewed_ids` or `split` records it.
- **`site_check.py --live` fails whenever the live block isn't what the script writes now.** That's
  intended.
- **Phase 3 layers (PL-9):** the scrubber and the draw-in are live; traps later, in their own review.

**Standing rules:**
- **The Rocket Lander is private.** Not here, in any form.
- `object-fit: contain`, never `cover`.
- **Content renders without JavaScript.** JS is allowed on top; the words and links must not depend on
  it. No dependencies or build step.
- **No inline script** (the CSP). Code that must run before the first paint goes in a small file in
  `/assets/`, as `prefs.js` does.
- Fonts self-hosted. No phone number on the site.
- **Never publish an exact node, edge, report, grade or check count** *in copy*. The app screenshot
  (`graph-app-ui.webp`) is the one ruled exception (Q-IG5).
- **No vanity metrics.** **Do not invent dates or figures.** Unknown → ask Thomas.
- Hajdu-Cheney syndrome is named on purpose. Symptom detail is not. **BYR is a patient site: no symptom
  detail and no family, in copy or in any receipt it links.**
- WordPress stays once per spec table as a hiring keyword; out of headline prose.
- **Nothing familial**, except the ruled Back Quarter childhood paragraph and Thomas's Q-BQD2 quote on the
  two thomascheesman.ca case studies (Q-BQD3 A). Children's names never.
- **Lead role: nonprofit website and digital operations.** Web development and accessibility are named
  once, as secondary (R6).
- **The résumé source is the Word file.** `resume-source.html` mirrors it. Never edit the PDF. **Exactly
  two pages.** Thomas exports the PDF.
- Melanie and Thomas are "the parents" of the three children, never "co-parents".
- **New CSS is additive and token-based.** Case-study-only CSS under `.cs-body` / `.cs-*`.
- **Never ship a link that 404s.**
- **Copy ships only through a copy review** (numbered blocks; OK / KEEP / A / B / FIX / CUT).
- **Accessibility controls are built in, never an overlay widget** (PL-6).
- **Never link `reviews/copy-review-001.md` from a page** (T0).
- **Never run git in `Reports Clustering`** from this project's sessions.
- **The outside research model is never named in copy** (F-2), and no link's path may carry its name.
- **Don't link the `@bareyourrare` social accounts anywhere until Thomas says they are claimed** (O-18).
- **Never link a theme-repo file or commit.** Read it for facts only (Q-BQD1 A).
- **Never load a Hostinger site in a headless browser from Thomas's machine** (§2 trap).
- **A change meant to be invisible is proved with `shots_diff.py`**, with its `--self` and `--inject`
  controls.

**Demo and embed rules:**
- Nothing heavy loads before a click. A gated page degrades when the payload is absent.
- The 3D canvas keeps its own dark ground, in both themes.
- `basis` is quoted, never paraphrased. The written chain under the graph is the accessible equivalent.
- Nothing rearranges a layout on interaction; the sub-menu and the Display panel overlay and move nothing,
  and the scrubber keeps one height.
- **Show finished work:** unfinished work is labelled honestly or left off.

## 4. Open items — carry these forward until closed

### PLAN
| # | Item | Notes |
|---|---|---|
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Phase 1 ✓ → Phase 1b ✓ → Phase 2 ✓ → **Phase 3: steps 2 to 5 ✓, M3 ✓ (#32); left: the ledger's traps layer (PL-9) and DESIGN-6** → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). |
| PL-8 | **Page-weight / a11y numbers: ruled ship without (2026-09-24)** | When the Phase 4 budget script exists, the numbers go into `/work/this-site`'s honest limits through a copy review. |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers. |
| PL-9 | **The ledger's later layers (Phase 3)** | Ruled Q-P3-6 A. The scrubber and the draw-in are live (#27). **Traps: next, in their own review** (ruled "A" 2026-09-30: after M3). Handoffs list each session's new traps only from 019 on, so it needs a curation pass first. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-20 | **`/work/this-site` states things that will go stale** | "rebuild in progress" (header) and "has not had a screen-reader run-through yet" (honest limits). Update each when its thing changes. (TS1's M1 sentence came out in #34.) |
| C-15 | Résumé: **the summary ends on a one-word line ("roles.")** | **Ruled A: fix it at the next résumé edit,** in the Word file and its HTML mirror; Thomas exports; exactly two pages. |
| C-16 | **Job history, from Thomas 2026-09-23. Use these** | GPRS board: elected at the **June 2023** AGM (first meeting September). Majors consulting: May 2019 – **June 2020**. **Head Chef, Ric's Grill, Sep 2013 – Jul 2014.** **Executive Chef, Township 71, Jul 2014 – Jun 2015** (renovation from Oct 2014, opened Nov 2014, closed May 2015, wind-down through June). **Taught one GPRC semester, Sep – Dec 2014.** |
| C-13 | GPRS site history | WordPress.com 2023; self-hosted WordPress.org on Hostinger 2025 "because I wanted more freedom to experiment with the code." No month-level dates without asking. |
| C-17 | R4 wording, his call | Live: "…then build it with help writing by AI." **Do not raise it again or change it unasked.** |
| C-21 | **`/method` H1, lede and title: his call (2026-09-25)** | Same standing as C-17. |
| C-9 | `page-thomas.php` ~2010 | Ruled B, done by the theme session in 1.0.762. The theme's V0.46 owns it. |

### DESIGN
| # | Item | Notes |
|---|---|---|
| DESIGN-6 | **M2's clip can come after the first paint on a slow load** (found 2026-10-01) | `ledger.js` is `defer`, so on a slow load the page can paint the whole ledger before the script clips it to 001 for the draw-in. Live: first paint 816ms, clip 851ms, on 1 of 3 runs at wrap; `site_check.py`'s M2 check caught it. Visible only where the ledger's top shows on the first screen (1280×900 shows its column numbers and first band). **Proposed, not built:** `prefs.js` (before first paint) marks `<html>` on the home page under Full; CSS hides `.lg__threads` while the mark is on; `ledger.js` removes it when it takes over, with a fallback in `prefs.js` that removes it after a few seconds if `ledger.js` never runs. Prove it with a local slow-script run, the way DESIGN-5 was proved. Recommend to Thomas before building. |

### PROJECTS / GRAPH
| # | Item | Notes |
|---|---|---|
| — | No open items | |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add every case study, `/method` and the Projects sub-menu to that run. One real screen-reader run through the live graph on `/work/influence-graph`. **Points for it:** the loop diagrams' links sit inside an SVG with `role="img"`; the diagrams' connectors in `--rule` are faint on white; the home ledger's two `role="img"` SVGs and its `<details>` list; the Display panel's radio rows and real Windows high contrast; a real browser at 200% text; the scrubber with a screen reader (its spoken value is the whole line); M1, M2 and M3 with the OS's reduce-motion on. |
| A-3 | **Sub-menu without JS cannot be dismissed with Esc** | Accepted as the no-JS fallback; for A-1 to confirm. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-18 | **A script that waits for the merge commit's deploy** | Not built. This session's five waits were again an ad hoc loop on the check-runs API, then curls against `main` with a pre-merge control. A `scripts/` tool doing both would replace them. |
| INFRA-19 | **A hook that refuses a heredoc in a Bash command?** | **Hit once more since handoff-027** (a `python -` left at the front of a command, hung until stopped): three times this session, and three the session before. A hook that refused `python -` and `<<` would have stopped each. It changes his harness settings, so it's **his call; not built.** |
| INFRA-20 | **The truth rules are in two places** | Thomas's global `CLAUDE.md` and this repo's `CLAUDE.md` both hold all twenty. Which to keep is **his call**; nothing was changed. |
| INFRA-17 | **Theme-side test harnesses** | Done by the theme session (commit `51d2cbc` in the theme repo). The saved copies in `Claude outputs/infra-17-harnesses/` (untracked) can go once Thomas is happy with that. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address. |
| INFRA-6 | Dead lander CSS in `style.css` (search `lander embed`) | Delete if still unused by mid-October 2026. |
| INFRA-9 | HSTS 1 yr, no `includeSubDomains`, no `preload` | Deliberate; both are hard to undo. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. **He will renew on 2026-10-07** (said 2026-09-27). Reminded 2026-09-30 and 2026-10-01. **Not confirmed paid.** |
| D-1 | WordPress.com still claims the domain | Ruled A: detach when convenient. Thomas's to do. |
| D-2 | WP.com plan auto-renew | Ruled A: leave for now; revisit before 2027-08-22. Do not cancel without confirming DNS for the live sites is unaffected. |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-25 | **The home page slides sideways on phones (only the home page)** | thomascheesman.ca. Owned by the theme's newest `V0.*.md`. |
| O-24 | **thomascheesman.ca phone header, and the no-JS lede** | (a), (b) and (d) done by the theme session in 1.0.762; (c) the "wonky" menu: he'll screenshot it if he sees it again. The theme's V0.46 owns them. |
| O-21 | **Theme repo: family material in its files, history and commit diffs** | Ruled A: leave it while private; clean it before it could ever go public. |
| O-17 | **BYR `.htaccess`: Thomas's `E=verifycaptcha:off` block had no effect** | Ruled A: remove it if it's there. Thomas checks the live file in hPanel's File Manager. |
| O-19 | **GPRS: WordPress "critical error" on uncached pages, 2026-09-26** | Re-tested 2026-09-27: 200. Ruled B: search for the "Technical Issue" email; not in Thomas's personal Gmail. Which inbox is GPRS's WordPress admin email is Thomas's to say. GPRS's own handoff owns any fix. |
| O-15 | **Research repo: "read the sentence as well as fetching it" is not in its current playbooks** | Ruled A: a research session adds it. Handed to a separate session 2026-09-30; not confirmed. |
| O-20 | **The Back Quarter: 3D on PCs only — SHIPPED 2026-09-27 (1.0.755)** | **3D on phones is a later job.** When it ships, `/work/back-quarter`'s "Where it runs" row, its honest limit and `/projects`' "A phone gets a still" line change with it. |
| O-22 | **Hostinger deploy webhook URL was in a public theme file for about seven weeks** | Rotate it the next time the deployment is rebuilt, by switching to Hostinger's GitHub App method. Then delete the old SSH entry in hPanel and the old webhook in GitHub. |
| O-16 | **AI crawlers on the Hostinger sites: ruled leave it** | On thomascheesman.ca GPTBot gets an instant, empty 429 from the origin; the others 200. BYR and GPRS not re-checked. Leave the Hostinger "Create LLMs.txt file" toggle **off**. `/work/bare-your-rare`'s honest limit depends on this. |
| O-18 | **`@bareyourrare` social accounts are unclaimed** | Links removed (`ed6b054`). Restore from that commit's parent once Thomas says they are claimed. |
| O-2 | `/projects` third-person leakage on thomascheesman.ca | Thomas is writing this himself. |
| O-4 | bareyourrare history contains `permits/` and `3.jpg` | Instructions in `_Quarantine\bareyourrare-history-purge.md`. Thomas runs it. |
| O-5 | `bareyr\.git` lock-file junk | Cosmetic; Thomas deletes. |
| O-6 | Rocket Lander repo not public | On hold with the lander. |
| O-7 | Children's names in the Back Quarter world | **Thomas ruled: leave them.** They stay off this site regardless. |
| O-8 | thomascheesman.ca's open items live in its newest `V0.*.md` | Theme at 1.0.762 on `main` when last read (2026-09-30). |
| O-10 | bareyourrare.org and thomascheesman.ca behind Cloudflare since 2026-09-20 | Full detail in handoff-014 §4. BYR's domain is on Cloudflare DNS: **don't click "Connect domain"** in hPanel. |
| O-11 | bareyourrare.org crawl audit, mostly deployed | `Claude outputs/byr-crawl-audit.md`. Still open: (g) page weight. |
| O-12 | GPRS work has its own handoff | `GPRS Organization/00 Working Notes/gprs-handoff-001.md`. |

**Closed since handoff-027:**
- **DESIGN-5,** the live M1 skips: the cause found and fixed (#33). The retries and TS1's sentence came out
  (#34, TS2 A).
- **C-22,** `/method` rules row 1: C22 A live (#35).
- **M3** (part of PL-6): live (#32).

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
  - *Added by the agent 2026-09-29; OK'd by Thomas 2026-09-30 ("§5 tally", A):*
    - A trap hit again despite its mention gets no y. Say so on the line.
    - A trap still earning its place at x = 10 belongs in code (`CLAUDE.md` rule 5).
    - A "trap" that repeats a rule already in §3 or `CLAUDE.md` is not a trap: cut it.
    - A dropped trap gets one line in §2 of the handoff that drops it, naming it, and no more.

## 6. Next up — LG29, then DESIGN-6, then the traps layer

Before anything: remind Thomas once of **D-3**, if it's still open. He said he'll renew on 2026-10-07, and
it's due 2026-10-08. Each step ends with his ruling before the next starts.

1. **LG29, this handoff's ledger line,** drafted in copy-review-006. When he rules it:
   1. Set `ruled` for 028 in `ledger/curation.json`. `parked` needs no change: DESIGN-6 is work (solid).
   2. Run `python scripts/export-ledger.py`, then `--check`, `--report` and `site_check.py`.
   3. Open a PR, and merge on his word.
   4. Curl `/` against `main` with a pre-merge control, and run `site_check.py --live`. Keep every FAIL
      line.
2. **DESIGN-6:** recommend the fix in its row and build it on his word. Reproduce the late clip locally
   first (hold `ledger.js` back), prove the fix the same way, and keep `site_check.py`'s M2 check as the
   live proof.
3. **The ledger's traps layer (PL-9):** a curation pass over the handoffs' traps (019 on), then its own
   copy review. Propose before building.

### After that

Phase 4: headers, schema, OG per page, and the budget script. PL-8's numbers go into `/work/this-site`
once the budget script exists, through a copy review.
