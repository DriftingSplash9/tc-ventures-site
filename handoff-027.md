# handoff-027 — tc-ventures.ca

**Written:** 2026-09-30
**Covers:** one session, 2026-09-30:
- **LG27 ruled; ledger column 026 live** (PR #26, which also landed #25, handoff-026).
- **Phase 3 step 5, the motion,** at Thomas's word "go ahead with step 5": M1 (page to page), M2 (the
  ledger draws itself in) and the scrubber. Ruled "ls1 A, q-s5-1 B", shipped as PR #27 on "merge 27".
- **M1 skips live** (found at the live check of #27): Chrome aborts some label-into-H1 transitions on
  tc-ventures.ca. Ruled "a": quiet the skip and retry the live check (#28), say so on `/work/this-site`
  (TS1, "ts1 ok", #29). The cause is open (DESIGN-5).

**Status at wrap:**
- **Live on tc-ventures.ca, verified 2026-09-30:** `main` at `a23ea0c` (PR #29). Each of #26 to #29 was
  merged by the agent at Thomas's word, each after a separate state check.
  - The check-run "Workers Builds: tc-ventures-site" on `a23ea0c` completed with success at 23:59:02 UTC.
  - Curl, cache-busted: `/work/this-site` is byte-identical to `main`, and differs from the pre-merge
    `b23c2aa`. #27's and #28's changed files were checked the same way when each merged (§2).
  - `site_check.py --live` passed 199 of 199. **M1 passes there only because the check now retries**
    (DESIGN-5).
- **thomascheesman.ca:** nothing changed from this session.
- **LG28,** this handoff's ledger line, is drafted in copy-review-006 with `"ruled": null`. The live ledger
  stops at 026 until it's ruled.

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
   - Steps 2 to 5 are built, ruled and live.
   - "M1 live: Chrome skips some transitions" is the record behind DESIGN-5.
   - **What's left of Phase 3:** M3 and the ledger's traps layer, both ruled "decide after step 5 ships"
     (§6).
5. **`plans/receipts-001.md`**: the ruled inventory, 49 OK / 81 CUT. Only OK rows go in copy. Tick `chk`
   before quoting a row.
6. **`reviews/copy-review-006.md`**: the build ledger's rulings. LG28, this handoff's line, is drafted there.
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
- He rules tersely ("ls1 A, q-s5-1 B"), and that is a full ruling.
  - **Ask what a bare number means** ("1" meant OK).
  - **Say how you read a bare letter** ("a" was read as Q-M1-1 A, the only open question) and record it.
  - He has also ruled in a spreadsheet the agent built (handoff-025's). Read its options column to know
    what each letter means.
- **He sometimes hands a call over** ("fix it", "up to you"). Make it, say in one line what you chose and
  why, and record it as delegated.
- **He changes his mind, and says so.** Record the new ruling next to the old one.
- **"pause here" means start nothing new.** Record what he ruled and wait.
- He is self-taught and model-agnostic, so explain methods, not one model's tricks.
- When he asks how something works, give him the plain version first.
- **He commits, pushes and merges himself, sometimes mid-session.** Re-read `git status` and `origin/main`
  just before you commit.
- **His merges don't always land** (§2 trap).
  - This session he said "merge 26", "merge 27", "merge 28" and "merge 29", and the agent merged each.
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
| Deploy | **A merge to `main` deploys** → Cloudflare builds. **No cache to purge.** Branch pushes build too, and the bot calls them "Deployment successful", but they don't reach the site (trap below). This session's four merges were each live at the first curl, after their merge commit's check-run completed. |
| Addresses | **`www.tc-ventures.ca` 301s to `https://tc-ventures.ca`, keeping the path and query** (a proxied `www` CNAME plus the Redirect Rule "www to apex 301"). **Always Use HTTPS is on**, so `http://` on either host 301s to https first. |
| Contact email | `thomas@tc-ventures.ca` |
| Pages | `index`, `projects`, `method`, `background`, `contact`, `404`, `work/influence-graph`, `work/back-quarter`, `work/desk-and-drawer`, `work/bare-your-rare`, `work/gprs`, `work/this-site`. Internal links, canonicals and sitemap use **clean URLs** (`/method`); `/x.html` 307s to `/x`. No case study is planned. |
| Nav | **Projects (with a sub-menu of the case studies) · Method · Background · Contact**, then the **Display** button, on every page: **13 files** including `_template.html`. The sub-menu order is the `/projects` order: **The Economic Report Influence Graph · A homepage you drive around · A menu that is a photograph of my desk · A rare-disease site, written by a patient · A housing society's website · This site**. The markup is copied into each page; `assets/nav.js` makes the sub-menu a disclosure button. **To ship a case study, run `scripts/ship_case_study.py`** (§3). |
| Display settings | **`assets/prefs.js`**, loaded without `defer` in every `<head>`, puts the saved choices on `<html>` (`data-motion`, `data-theme`, `data-contrast`, `data-text`) before the first paint. **`assets/display.js`** builds the panel. The choices are saved in `localStorage` under `tcv-display`, in this browser only. With no choice (System), the OS settings decide through CSS. Rules: §3. |
| Motion (step 5) | **M1:** `@view-transition` in `style.css`; the page-swap hooks are in `prefs.js` (the only script that runs before the new page's first paint). **M2 and the scrubber:** `assets/ledger.js`, `defer`, home page only. Rules: §3. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html` and `og-src/` off the live site. A preview goes in it until it ships. |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. **No inline script** (CSP `script-src 'self'`); inline `style=""` is allowed. Unchanged since handoff-017. |
| AI crawlers | **Allowed since 2026-09-30 (INFRA-15 ruled B):** GPTBot, ClaudeBot, ChatGPT-User and Claude-User each get 200 on `/`. `robots.txt` allows all. The setting is in Thomas's Cloudflare dashboard (AI Crawl Control). |
| Link preview | `assets/img/og-card.png` 1200×630 on all pages. Source `public/og-src/og.html`. LinkedIn's copy matches it (INFRA-10). |
| Analytics | Cloudflare Web Analytics, injected at the edge for browsers (curl doesn't see it). The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` · receipts `plans/receipts-001.md` · `plans/operating-guide.md` · Phase 3 `reviews/copy-review-007.md` |
| Design system | `public/assets/style.css` — tokens in `:root` (type in rem; theme, contrast and motion tokens after it, then M1's view-transition rules), case-study components under the `CASE STUDIES` banner, then the `build ledger` block at the end. **Every width breakpoint is in `em`** (§3). |
| Build ledger | The end of the home hero. Written into `public/index.html` between `<!-- ledger:begin … -->` and `<!-- ledger:end -->` by `scripts/export-ledger.py`, from the handoffs plus `ledger/curation.json` (not deployed). **Never hand-edit the block.** A landscape SVG, a portrait SVG shown at 37.5em (600px) and under, **the scrubber** (scripts only), and a `<details>` list with one ruled line per handoff. Rules: §3. |
| Graph demo | On `/work/influence-graph` only. `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js`. It reads the site's motion setting. |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. |
| Browser tests | Python Playwright + Chromium, scripts in `scripts/`:<br>- `site_check.py [--live] [--root DIR] [--draft-ledger] [-v]`: every sitemap page plus /404, the home ledger, the theme and contrast, the Display panel, and **the motion: M1 at each level (up to `M1_TRIES` = 3 changes of page per case, DESIGN-5), M2, the scrubber**. **199 checks, no known faults.** "Text at 200%" is set the way the browser's own text-size setting sets it (CDP `Page.setFontSizes`), at 375, 480, 760 and 1280px.<br>- `cs_check.py work/<page> [--preview] [--shots DIR]`: one case study. **`--preview` checks `PLANNED_SUBMENU`**.<br>- **`shots_diff.py BEFORE [AFTER] [--self] [--inject CSS]`**: every page, light and dark, 1280 and 375, pixel for pixel between two copies of `public/`. The proof of "no visible change". Run `--self` and `--inject` as controls (the footer is `footer`, not `.site-footer`).<br>- All of them serve `public/` in-process with clean URLs.<br>- **Playwright's default Chromium is the headless shell, started with `PaintHolding` and `RenderDocument` switched off** (trap).<br>- **In a claude.ai cloud session:** `pip install playwright` first; the scripts launch the preinstalled Chromium by path.<br>- **`--live` is for tc-ventures.ca (Cloudflare) only. Never point a headless browser at a Hostinger site** (trap). |
| Edit tools | **`patch.py`**: exact-match edits across files, all or none, keeping each file's line endings. **`ship_case_study.py`**: ships case-study previews (§3). **`quote_check.py FILE "quote"…` / `--ledger`**: each quote verbatim in its source, and each piece is its own control. |
| Claude Code hook | **`.claude/settings.json`** (this repo only, ruled INFRA-14a A): a `PreToolUse` hook runs `.claude/hooks/no_cd.py`, which refuses a Bash command whose first word is `cd`. It fired once this session, as intended. |
| Research repo | `C:\Users\thoma\Desktop\My Files\Reports Clustering` = public `DriftingSplash9/Reports-Clustering`. **Never run git there** from this project's sessions. Read its files, and read it on GitHub. |
| Sister repos | **Theme:** local `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` = GitHub `DriftingSplash9/thomascheesman-ca-theme`, **private since 2026-09-26**. A push to its `main` deploys to Hostinger; GitHub answers the push with "This repository moved" and the push still lands. Cached pages then need a LiteSpeed purge and a Hostinger CDN purge (Thomas). Commit/push there is pre-authorized; bump `style.css` `Version:` on every theme-code commit. **BYR:** `bareyr` = GitHub `DriftingSplash9/bareyourrare`, **private**. A push to its `main` deploys to Hostinger, then a LiteSpeed purge (Thomas). **`.htaccess` is not in the BYR repo**; it lives on the server only. |

## 2. What was done (2026-09-30)

**Rulings, verbatim:**
- "restore it, LG27 ok": `reviews/copy-review-006.md` had lost its last 114 lines in the working copy
  (LG27's draft among them); restored from `HEAD`. LG27 recorded as `"LG27 OK 2026-09-30"`.
- "merge 26", "go ahead with step 5", **"ls1 A, q-s5-1 B"**, "merge 27".
- **"a"** on Q-M1-1 (the live skips), read as A.
- "merge 28, ts1 ok", "merge 29, then write handoff-027".
- Mid-session he said "pane is open now, run it there" and "now try, i was in my chrome, not your side
  panel": the pane test needed the Claude window in front (§2 trap).

**Shipped, each checked live (merge commit's check-run, then curl against `main` with a pre-merge control,
then `site_check.py --live`):**
- **#26** (merge `d0333b0`): ledger column 026 (LG27). `parked` dropped C-22 and the seven items closed in
  handoff-026, and added INFRA-19 and INFRA-20. A draft render before and after differed only on those
  three threads. It also landed #25, handoff-026. `site_check.py --live` 193 of 193.
- **#27** (merge `da64359`), **Phase 3 step 5:**
  - M1: cross-document view transitions; the bar's three parts named apart (§3); under Full the clicked
    case-study label grows into the H1.
  - M2: the draw-in, clipped before the first paint (46ms against a first paint at 148ms).
  - The scrubber, aligned under the columns (within 1px at 700 to 1600px), with Q-S5-1 B: at a past
    handoff, threads that closed later are drawn open.
  - `site_check.py`: six new checks. Live it passed 198 of 199; the failure was M1 (below).
- **#28** (merge `b23c2aa`): `prefs.js` handles a skipped transition's promises; `site_check.py` retries
  each M1 case up to three times. Live 199 of 199, twice; tries used `[1, 1, 2, 1, 3]` on the second.
- **#29** (merge `a23ea0c`): TS1, one sentence in `/work/this-site`'s "The honest limits". Live 199 of 199.

**How it was checked (the full record is in copy-review-007 and the PR bodies):**
- **Browser support for M1 read at build** from MDN's `browser-compat-data`, raw, HTTP 200: Chrome and
  Edge 126+, Safari 18.2+, not Firefox.
- **Every new check was run against copies that must fail it:**
  - this repo's `public/` before LS1 was ruled, and `main` before step 5;
  - copy A: the label unnamed, the bar sliding under Reduced, no spoken value;
  - copy B: Off not skipped, the draw-in ignoring the setting, the lines hidden with `display: none`, the
    slider shown without scripts;
  - copy C: the past-colouring removed.
  - All 10 faults were caught. Pre-step-5 `main` fails "no transition in 3 tries" in every M1 case.
- **`shots_diff.py`, `main` against step 5:** 44 of 48 identical; the home page differs by the slider.
  `--self` 48 of 48 with the draw-in running; `--inject footer{padding-top:1px}` 0 of 48.
- **Looked at:** M1 frozen at 0, 30, 60 and 90% before and after the bar fix; the slider at 1280 light and
  375 dark, at rest, mid draw-in and at 017, before and after Q-S5-1 B. GIFs of M1 and M2 went to Thomas
  (`Claude outputs/step5-shots/`, untracked).

**Found in the data:**
- **The top bar isn't in the same place on every page.** A case study's lane is wider, so the name and
  nav sit about 120px further out than on `/projects`. Cross-faded as one picture the bar showed doubled
  text; named apart, each part slides.
- **Live, Chrome aborts some label-into-H1 transitions** (DESIGN-5). Headless: 4 of 12, 2 of 8, 5 of 10,
  3 of 12, 6 of 16, 5 of 16. The app's browser pane (Chrome 152, on screen): 3 of 7. Locally: 0 of 40, with
  60ms latency and the live headers. The old page starts the transition every time, with unique names, and
  Chrome then logs "AbortError: Transition was skipped". Not the analytics beacon, not paint holding.
- **The H1's empty `style` attribute is a tell:** `prefs.js` sets and then clears the H1's name only when a
  transition reaches the new page, which leaves `style=""`. It matched the probe's own record in 32 of 32
  runs. Useful wherever an init script can't be added (the pane).
- **A skipped transition's error shows only sometimes in Playwright's console:** the old code logged it in
  2 of 11 runs under Off, the new in 0 of 11. Thin evidence; the fix (every promise handled) is simple.

**Own misses:**
- **Two empty `python -` heredocs,** each left in a command by habit; each hung until stopped. The
  heredoc trap, hit again despite the mention (INFRA-19).
- **Two control faults that couldn't fail:** removing only the old page's Off skip (the new page skips
  too), and un-stacking the scrubber's lines (hidden lines still take space, so one height). Caught by
  their passing; replaced.
- **An `--inject` control named a class that doesn't exist** (`.site-footer`), so it changed nothing. Caught
  by its 44 of 48; redone with `footer`.
- **The keyboard check crashed on a missing spoken value** instead of failing. Fixed to fail.
- **The 1280 scrubber shot clipped above the slider,** by capping the clip at the viewport. Caught by
  looking; redone.
- **Started a build on `main` before noticing handoff-026 wasn't on it** (PR #25 open). Caught by the
  export stopping at column 025; rebuilt on the `handoff-026` branch.
- **The diary wasn't read at session start,** as the global `CLAUDE.md` asks. Read at wrap.

**Found, not fixed:** DESIGN-5 (§4).

### Traps worth knowing

Each trap ends with its tally, **`x.y`** (§5).

**Dropped this handoff:**
- "In a cloud session, `pip install playwright` installs a version whose default browser path doesn't
  exist": `6.0`.
- "The cloud clone of the theme repo is shallow (50 commits)": `6.0`.
- "`/projects` copy about thomascheesman.ca goes stale when the features change": `6.1`.
- "Run a local test server inside the Python process": `10.9`. It's in code: every checker does it.
- "Wait about 400 ms after a click before a screenshot": `10.6`. It's in code: `site_check.py` waits.
- "A receipt's 'caught' column can be a guess": `10.2`.

**New this session:**
- **A cross-document view transition can pass locally and skip live.** On tc-ventures.ca Chrome aborts
  some (DESIGN-5); on a local server it never did. Test M1 against the live site, more than once. `0.0`
- **Playwright's default Chromium is the headless shell, started with `PaintHolding` and `RenderDocument`
  switched off** (`Browser.getBrowserCommandLine` shows it). Neither explained DESIGN-5, but motion and
  navigation behaviour there may differ from a real Chrome. `0.0`
- **The app's browser pane draws only while the Claude window is in front and the pane is showing.**
  `tabs_context` says "hidden", or a screenshot times out "did not finish rendering": then clicks fail and
  a motion test means nothing. Ask Thomas to bring the window forward. `0.0`

**Carried:**
- **A Playwright full-page screenshot drops CDP `Page.setFontSizes`.** Take viewport screenshots when the
  browser's text size is set. `1.0`
- **Lazy, async-decoded images can paint as empty boxes in a Playwright full-page screenshot.**
  `shots_diff.py` forces the decode. `2.0`
- **Python on Thomas's console prints in cp1252, and a `→` or `’` crashes it.** Run with
  `PYTHONIOENCODING=utf-8`. This session's scripts did. `2.2`
- **`git rev-parse --short` takes one revision.** `2.0`
- **PowerShell 5.1 splits an inline argument at its embedded double quotes.** Write a message or PR body
  to a file (`git commit -F`, `gh pr create --body-file`). This session every commit and PR body went
  through a file. `3.3`
- **A gate must run on its own, then you act.** In PowerShell `;` runs the next command even when the one
  before failed. This session each merge's state check ran as its own command first. `3.3`
- **Thomas's "merged" may not have landed.** Run `gh pr view N --json state` before you check live or build
  on it. This session each merge's state was read after the merge. `4.4`
- **Theme docs name surfaces loosely.** Read a spec's §0 before a caption says what it is the spec for.
  `4.0`
- **A 429 behind Cloudflare may not be about your IP.** If Cloudflare proxies to a second CDN
  (`*.cdn.hstgr.net`), that CDN's per-IP limit counts Cloudflare's edge IPs. `x-hcdn-*` means Hostinger's
  CDN; `x-turbo-charged-by: LiteSpeed` + `panel: hpanel` means the origin. `4.0`
- **Never load a Hostinger site in a headless browser from Thomas's machine.** Hostinger's CDN counts
  HeadlessChrome as a bot, and a few dozen loads got his home IP an empty 429 for hours. Test theme
  changes locally; ask Thomas to confirm live in his own browser. `5.2`
- **An offline rebuild of a live page can't judge a font-dependent width.** `5.0`
- **Astra's Customizer CSS beats the child theme's bare element rules.** `5.0`
- **Heredocs mangle scripts, and `python -` with nothing on stdin waits forever.** Write scripts with the
  Write tool. **Hit twice again this session despite the mention**, so no y (INFRA-19). `5.3`
- **A checker can read the wrong block or field, and a control can be unable to fail.** Anchor on the
  heading; a control must change something the check reads. **Hit again this session** (two control
  faults and an `--inject` selector), so no y. `6.4`
- **The Cloudflare bot says "Deployment successful" on branch pushes. Branch builds don't reach
  tc-ventures.ca.** Only a merge deploys. This session each live check waited on the merge commit's
  check-run. `6.4`
- **A check warms the cache it is checking.** Use a cache-busting query. This session's curls used `?cb=`.
  `7.7`
- **Most of this repo is CRLF in Thomas's Windows checkout.** Edit through `scripts/patch.py`. Every edit to
  an existing file this session went through it. `9.8`
- **`/404` answers 200.** Test "not found" with an unknown URL. `9.2`
- **A test that Tabs a fixed number of times can land on the wrong control.** Loop until the target has
  focus. `9.3`

## 3. Current design

**Pages live:**
- `/work/gprs` and `/work/this-site` (2026-09-24)
- `/method` and `/work/influence-graph` (2026-09-25)
- `/work/bare-your-rare` (2026-09-26)
- `/work/back-quarter` and `/work/desk-and-drawer` (2026-09-28)
- The Display panel on every page (2026-09-29)
- The step 4 layout on every page (2026-09-30)
- **The step 5 motion** (2026-09-30)

**The case studies:**
- **Six fixed sections**, receipts as small mono links, figures `Fig. N` per page.
- Every claim in "What the AI got wrong" and "How I caught it" links to a receipt that returns 200
  publicly, or is cut. A receipt in a private repo (BYR's, the theme's) links its receipts-001 row
  instead.
- **"How I caught it" says "I" only for catches Thomas made.** Agent catches are written impersonally.
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
  - **`/work/this-site`'s M1 sentence (TS1): stale when DESIGN-5 is fixed.**
- **A building on the Back Quarter opens on Enter.** Copy never says driving up opens it.
- **On thomascheesman.ca the plain list is the default menu.** The desk is a second menu behind "T's
  Desktop".
- **Theme specs are quoted verbatim with their date and section, and "The repo is private."** They are
  never linked (Q-BQD1 A).

**`/method`:**
- **The H1, the lede and the page title are Thomas's rulings.** Don't edit them, explain the
  accessibility line, or raise them again unasked.
- Research-project rows link receipts-001 §3C.
- **Rules row 1's "I caught it by using them" is to be narrowed** to the two catches with receipts, through
  a copy block (C-22, ruled A, not drafted).

**Nav:**
- **To ship a case study, run `python scripts/ship_case_study.py work/<slug> [work/<slug> …]`** (`--dry-run`
  first). It refuses, writing nothing, unless `PLANNED_SUBMENU`, the live sub-menu, every page and
  label = H1 agree. It doesn't touch `/projects` or the home cards: that's copy.
- A preview carries the sub-menu it will ship with. Set `PLANNED_SUBMENU` in `cs_check.py` first.
- Ship the page and its link in the same push, never a link that 404s.
- **Any other edit to the nav or the header** is a 13-file edit. Do it with a `patch.py` script.
- **In the header's phone layout (45em and under)** the open sub-menu is capped to the screen (DESIGN-1).
- **The label is the H1** (a standing rule), and M1 depends on it.

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

**The motion (step 5, live 2026-09-30; copy-review-007):**
- **M1, page to page:**
  - `@view-transition { navigation: auto; }`. Chrome/Edge 126+ and Safari 18.2+; others change pages as
    before.
  - The top bar is `topbar`, and **its three parts are named apart** (`tb-name`, `tb-nav`, `tb-display`):
    they slide over `--move` (0.35s) because the case-study lane puts them elsewhere. The rest cross-fades
    over `--fade` (0.25s).
  - **Under Full only,** `prefs.js` names the clicked `#navsub-work` link and the new page's `main h1`
    `cs-title` for that one change of page (0.5s), and clears them after.
  - Reduced: the cross-fade, nothing moving. Off: `prefs.js` skips the transition on both pages.
  - **A skipped transition's promises are handled** (`quiet()` in `prefs.js`).
  - **Live, Chrome skips some of them** (DESIGN-5). `site_check.py` retries each case up to `M1_TRIES`.
- **M2, the draw-in:** under Full, the threads are clipped to 001 before the first paint and drawn to the
  newest (0.11s a handoff) the first time the ledger is 35% in view. Reduced and Off: whole from the
  start. Touching the slider stops it.
- **The scrubber:**
  - A native `<input type="range">` under the picture, inside the figure, one step per handoff, starting
    at the newest. Its label is LS1, "Step through the handoffs" (curation `copy.scrub`).
  - Moving it clips both pictures' threads at that column (`.lg__threads` group, a `clipPath` added by
    `ledger.js`), marks the column (`lg__col--on`) and shows that handoff's line.
  - **At a past handoff a thread that closed later is drawn open** (Q-S5-1 B): the export writes each
    closed thread's closing column as `data-e`, and `ledger.js` adds `lg__then-open`.
  - **All lines are stacked in one grid cell**, so its height never changes and nothing below moves.
  - The spoken value: "handoff-017, 2026-09-24: <the ruled line>".
  - In landscape its track ends sit under the first and last columns (`--lg-from`, `--lg-to`, written by
    the export from `svg_land`'s `LEFT`, `RIGHT` and `W`, minus half a 16px thumb). Change those
    constants and the inline style follows.
  - Scripts only (`@media (scripting: enabled)`); the list carries every line without them.
  - **The export leaves the scrubber out unless `copy.scrub.ruled` is set.**

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
  1. Draft the new handoff's line in copy-review-006 (LG28 for 027, LG29 for 028, and so on).
  2. Add it to the curation with `"ruled": null`.
  3. Run `python scripts/quote_check.py --ledger` on its "Rests on" quotes.
  4. After Thomas rules, set `ruled`, export and ship.
- **A line** never copies handoff prose, says "I" only for what Thomas did, and leaves out the private
  project, other sites' incidents and anything familial.
- **Items are drawn solid unless the curation's `parked` lists them** (dotted). **Parking only changes a
  thread still open at the last column;** a closed thread draws closed whether parked or not. A `parked`
  change goes in the same PR as the column it belongs to.
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
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Phase 1 ✓ → Phase 1b ✓ → Phase 2 ✓ → **Phase 3: steps 2 to 5 ✓ live (step 5, the motion, #27, 2026-09-30)** → **M3 (the method loop) and the ledger's traps layer: ruled "A: decide after step 5 ships", so due now** → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). |
| PL-8 | **Page-weight / a11y numbers: ruled ship without (2026-09-24)** | When the Phase 4 budget script exists, the numbers go into `/work/this-site`'s honest limits through a copy review. |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers. |
| PL-9 | **The ledger's later layers (Phase 3)** | Ruled Q-P3-6 A. **The scrubber and the draw-in are live (#27).** Traps later, in their own review (separable per session only from handoff-019 on). |

### COPY
| # | Item | Notes |
|---|---|---|
| C-22 | **`/method` rules row 1 says "I caught it by using them"** (the three sliders) | **Ruled A (2026-09-30): narrow it to the two catches with receipts** (handoffs 006/007 and 032), through a copy block. Not drafted yet. |
| C-20 | **`/work/this-site` states things that will go stale** | "rebuild in progress" (header); "has not had a screen-reader run-through yet" (honest limits); **and TS1's M1 sentence (2026-09-30), stale when DESIGN-5 is fixed.** Update each when its thing changes. |
| C-15 | Résumé: **the summary ends on a one-word line ("roles.")** | **Ruled A: fix it at the next résumé edit,** in the Word file and its HTML mirror; Thomas exports; exactly two pages. |
| C-16 | **Job history, from Thomas 2026-09-23. Use these** | GPRS board: elected at the **June 2023** AGM (first meeting September). Majors consulting: May 2019 – **June 2020**. **Head Chef, Ric's Grill, Sep 2013 – Jul 2014.** **Executive Chef, Township 71, Jul 2014 – Jun 2015** (renovation from Oct 2014, opened Nov 2014, closed May 2015, wind-down through June). **Taught one GPRC semester, Sep – Dec 2014.** |
| C-13 | GPRS site history | WordPress.com 2023; self-hosted WordPress.org on Hostinger 2025 "because I wanted more freedom to experiment with the code." No month-level dates without asking. |
| C-17 | R4 wording, his call | Live: "…then build it with help writing by AI." **Do not raise it again or change it unasked.** |
| C-21 | **`/method` H1, lede and title: his call (2026-09-25)** | Same standing as C-17. |
| C-9 | `page-thomas.php` ~2010 | Ruled B, done by the theme session in 1.0.762. The theme's V0.46 owns it. |

### DESIGN
| # | Item | Notes |
|---|---|---|
| DESIGN-5 | **Live, Chrome aborts some M1 transitions** (found 2026-09-30) | On tc-ventures.ca, roughly a quarter to a half of label-into-H1 changes of page get no transition (headless, the six plain batches: 25 of 74; the app's pane, Chrome 152, 3 of 7). Locally never (0 of 40, with latency and the live headers). The old page starts it with unique names; Chrome logs "AbortError: Transition was skipped" and the new page never receives it. Not the analytics beacon, not paint holding. **Ruled Q-M1-1 A:** skips are quiet (#28), the live check retries (`M1_TRIES` = 3), TS1 says so on `/work/this-site` (#29). **Leads:** serve locally over HTTPS (or HTTP/2) and see if it reproduces; try with the bar's parts unnamed, then with only `cs-title` named; read Chrome's view-transition skip reasons (chrome://tracing or DevTools). When fixed: C-20 (TS1), the retry, this row. Record in copy-review-007 "M1 live". |

### PROJECTS / GRAPH
| # | Item | Notes |
|---|---|---|
| — | No open items | |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add every case study, `/method` and the Projects sub-menu to that run. One real screen-reader run through the live graph on `/work/influence-graph`. **Points for it:** the loop diagrams' links sit inside an SVG with `role="img"`; the diagrams' connectors in `--rule` are faint on white; the home ledger's two `role="img"` SVGs and its `<details>` list; the Display panel's radio rows and real Windows high contrast; a real browser at 200% text. **New (step 5): the scrubber with a screen reader (its spoken value is the whole line), and the M1 and M2 motion with the OS's reduce-motion on.** |
| A-3 | **Sub-menu without JS cannot be dismissed with Esc** | Accepted as the no-JS fallback; for A-1 to confirm. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-18 | **A script that waits for the merge commit's deploy** | Not built. This session's four waits were again an ad hoc loop on the check-runs API, then curls against `main` with a pre-merge control. A `scripts/` tool doing both would replace them. |
| INFRA-19 | **A hook that refuses a heredoc in a Bash command?** | **Hit twice more this session** (two empty `python -` heredocs, each hung until stopped), on top of three last session. A hook changes his harness settings, so it's **his call; not built.** |
| INFRA-20 | **The truth rules are in two places** | Thomas's global `CLAUDE.md` and this repo's `CLAUDE.md` both hold all twenty. Which to keep is **his call**; nothing was changed. |
| INFRA-17 | **Theme-side test harnesses** | Done by the theme session (commit `51d2cbc` in the theme repo). The saved copies in `Claude outputs/infra-17-harnesses/` (untracked) can go once Thomas is happy with that. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address. |
| INFRA-6 | Dead lander CSS in `style.css` (search `lander embed`) | Delete if still unused by mid-October 2026. |
| INFRA-9 | HSTS 1 yr, no `includeSubDomains`, no `preload` | Deliberate; both are hard to undo. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. **He will renew on 2026-10-07** (said 2026-09-27). Reminded 2026-09-30. **Not confirmed paid.** |
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

**Closed since handoff-026:**
- **Phase 3 step 5** (M1, M2 and the scrubber): live in #27, with LS1 A and Q-S5-1 B.
- **Q-M1-1:** ruled A; the skip is quiet and the live check retries (#28); TS1 live (#29). The cause stays
  open as DESIGN-5.

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

## 6. Next up — LG28, then what's left of Phase 3

Before anything: remind Thomas once of **D-3**, if it's still open. He said he'll renew on 2026-10-07, and
it's due 2026-10-08. Each step ends with his ruling before the next starts.

1. **LG28, this handoff's ledger line,** drafted in copy-review-006. When he rules it:
   1. Set `ruled` for 027 in `ledger/curation.json`. `parked` needs no change: DESIGN-5 is work (solid),
      and INFRA-19 and INFRA-20 are already parked.
   2. Run `python scripts/export-ledger.py`, then `--check`, `--report` and `site_check.py`.
   3. Open a PR, and merge on his word.
   4. Curl `/` against `main` with a pre-merge control, and run `site_check.py --live`.
2. **Ask him to decide M3 and the ledger's traps layer** (both ruled "decide after step 5 ships"). Recommend
   one: the traps layer needs a curation pass and its own copy review; M3 is the method loop's arrows
   tracing once on `/method`, under the same `--move` rules.
3. **DESIGN-5,** if he wants it before more motion: the leads in its row. Prove any fix live, more than
   once, and only then take the retry and TS1 out (C-20).
4. **C-22's copy block** can go with the next copy review or on its own: his choice when it's drafted.

### After that

Phase 4: headers, schema, OG per page, and the budget script. PL-8's numbers go into `/work/this-site`
once the budget script exists, through a copy review.
