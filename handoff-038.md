# handoff-038 — tc-ventures.ca

**Written:** 2026-10-03
**Covers:** the session that continued from handoff-037, 2026-10-03:
- **handoff-037** merged (#73); **ledger column 037** (LG38, #74).
- **The monogram folds to a clean TC, and Menu doesn't wobble** (#75, copy-review-012).
- **Two traps into code** (#76): FAIL lines repeated at a run's end; `site_check.py --live` only from `main`.
- **Thomas's Chrome in the checks, and every ceiling doubled** (#77, open).
- **The third pass, proposed:** copy-review-013 (TP-0), with award winners to study.

**Status at wrap:**
- **Live on tc-ventures.ca, verified 2026-10-03:** `main` at `5bffd55` (#76).
  - `deploy_wait.py`: #74 7 of 7, #75 7 of 7, #76 3 of 3 (no served file). #73 changed no served file.
  - `site_check.py --live` (from an archive of `origin/main`): **264 of 264** after #76, the gate's first pass.
  - `budget.py --live`: **51 of 51** after #76. PW3 holds, with `/projects` 786 kB on the wire of its 790.
- **Open, for Thomas's merge:** **#77** (244 of 244 locally, in Chromium and in Chrome) and **this
  handoff's PR** (copy-review-012's "keep the lean", copy-review-013, LG39's draft, `traps.json` to 038).
- **Waiting on Thomas:** D-3, DESIGN-8, the two merges, LG39 and TP-0 with Q-TP1 to Q-TP4 (§6). Q-SP5 stands
  at "5 none yet".
- **thomascheesman.ca:** nothing changed from this session.
- **LG39,** this handoff's ledger line, is drafted in copy-review-006 with `"ruled": null`, and
  **`ledger/traps.json` already holds this handoff's traps.** The live ledger stops at 037 until LG39 is
  ruled, and its column ships after #77 (the line says the checks use his Chrome).

**The next job is §6.**

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. Read §2 "Traps" before you touch git, a checker script, a screenshot, the
   app's browser pane, the theme repo, a Hostinger site, or the `Reports Clustering` folder. **Especially:
   do not load thomascheesman.ca in a headless browser from Thomas's machine.**
2. The twenty truth rules: in Thomas's global `C:\Users\thoma\.claude\CLAUDE.md` (the source copy) and in
   this repo's `CLAUDE.md` (kept for cloud sessions; INFRA-20 ruled). `plans/operating-guide.md` is how
   Thomas and the AI divide the work, and §4 there is the checking routine.
3. **`reviews/copy-review-013.md`: the third pass, proposed** (TP-0, not yet ruled), with award winners to
   study. **`reviews/copy-review-012.md`: the header that collapses,** ruled and shipped, every ruling
   verbatim (and TH3d), ending with "The monogram, and no wobble". **`reviews/copy-review-011.md`:**
   the second pass (SP-0 to SP-C, TH3b, TH3c) and, at its end, "Motion made visible".
4. **`reviews/copy-review-010.md`: the 3D hero**, from the proposal to the cleanup list, every ruling
   verbatim. Its §2 is how the scene is meant to behave.
5. **`plans/plan-001-showcase.md`**: the plan. Phases 1 to 4 are done; PL-6 says what follows.
6. **`plans/receipts-001.md`**: the ruled inventory, 49 OK / 81 CUT. Only OK rows go in copy. Tick `chk`
   before quoting a row.
7. **`reviews/copy-review-006.md`**: the build ledger's rulings. LG39, this handoff's line, is drafted there.
8. The shipped pages under `public/`. **`public/assets/ledger-scene.js` is the 3D hero**; read its header
   comment first. The second pass lives in `style.css` (the opener, the section heads and the rail, each
   under its own banner comment) and in `prefs.js` (the carried picture, beside M1). **`assets/header.js`
   is the header** and **`assets/opener.js` the opener's settle**; read each one's header comment first.
9. **`scripts/`**: each script's docstring is its manual.
   - The checkers: `site_check.py`, `budget.py`, `cs_check.py`, `byr_bot_check.py`, `shots_diff.py`,
     `quote_check.py`, and after a merge `deploy_wait.py`. The four that print PASS and FAIL lines repeat
     every FAIL line at the end, on stderr (`checklog.py`). `site_check.py --live` refuses any copy but
     `origin/main`'s; `--chrome` runs it in Thomas's Chrome.
   - The writers: `export-ledger.py` (plus `ledger/curation.json`), `schema.py`, `og_cards.py`, `patch.py`,
     `ship_case_study.py`. `export-ledger.py`, `schema.py` and `og_cards.py` have a `--check`; `schema.py`,
     `og_cards.py` and `budget.py` have `--controls`.
10. **If the job touches thomascheesman.ca:** the theme repo's `CLAUDE.md` and its newest `V0.*.md`
    (V0.46 when last read), and `docs/IMAGE-BURST-PLAN.md`.
11. `claude/thomas-study.md`, `claude/tc-ventures-site-decisions.md` (the Claude project; not on disk).
12. `README.md`.
13. If the job is GPRS itself, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md`.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**.

**How Thomas works:**
- Short answers, right to the point; recommend one to four options, the most recommended first.
- He rules tersely ("sd1 ok, sd2 ok, all A"), and that is a full ruling.
  - **"do the next handoff" meant: work through the newest handoff's §6.**
- **He sometimes hands a call over** ("fix it", "up to you"). Make it, say in one line what you chose and
  why, and record it as delegated.
- **He changes his mind, and says so.** Record the new ruling next to the old one.
- **"pause here" means start nothing new.** Record what he ruled and wait.
- He is self-taught and model-agnostic: explain methods, not one model's tricks, and the plain version first.
- **He commits, pushes and merges himself, sometimes mid-session, sometimes from his phone.** Re-read
  `git status` and `origin/main` just before you commit, and check a PR's state before you act on "merged".
- **A merge needs his word, per PR** ("merge 74, 75, 76"), and **only on a passing check** (the #63 trap):
  wait for the check, read it, then `gh pr merge` by hand. The agent merged #59 to #76 that way.
- **He designs by looking, on his own PC.** He reacts to each recording and steers the next ("it does need
  box", "sharper edges"); "i do not even notice" meant motion too quiet: make it plainly visible, then let him
  turn it down. Send a recording at every step; treat his description as the ruling; ask only what it leaves
  open.
- **He asks "what is next" as three lists:** for him, for the agent, for both. Give each short.
- **When he asks for examples, give him links he can open:** each fetched (200), and each award read on the
  award's own page (2026-10-03).
- **He does dashboard work himself** (Cloudflare, WordPress.com), with the agent giving the steps and
  checking the result by curl. A screenshot of where he's stuck is his way of asking.
- **He may be working in his own Chrome while you use the app's browser pane.**
- **A download needs his OK first, with its name, source and size** (Three.js, 2026-10-02).
- **He wants the site spectacular before any award submission** ("I do not intend to submit it unless it
  is spectacular. so far it feels plain."), and JavaScript is fine ("java script is fine, why are you being
  averse to it?"). Don't hold back motion or 3D out of caution; the limits are the ruled ones in §3.

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
| Deploy | **A merge to `main` deploys** → Cloudflare builds. **No cache to purge.** Branch pushes build too, and the bot calls them "Deployment successful", but they don't reach the site. **After a merge, run `python scripts/deploy_wait.py N`** (§3): it gates on the merge, waits on the merge commit's own check-run, and compares every changed served file byte for byte. |
| Addresses | **`www.tc-ventures.ca` 301s to `https://tc-ventures.ca`, keeping the path and query.** **Always Use HTTPS is on.** Cloudflare serves documents over HTTP/3 (`h3`) to Chrome. **`/work` and `/work/` 301 to `/projects`** (`public/_redirects`, Q-P4-6 A). |
| Contact email | `thomas@tc-ventures.ca` |
| Pages | `index`, `projects`, `method`, `background`, `contact`, `404`, `work/influence-graph`, `work/back-quarter`, `work/desk-and-drawer`, `work/bare-your-rare`, `work/gprs`, `work/this-site`. Internal links, canonicals and sitemap use **clean URLs** (`/method`); `/x.html` 307s to `/x`. No case study is planned. |
| Nav | **Projects (with a sub-menu of the case studies) · Method · Background · Contact**, then the **Display** button, on every page: **13 files** including `_template.html`. **With scripts, `assets/header.js` folds them into a Menu button as the page scrolls, and always on a phone; Display is a symbol button** (copy-review-012). The sub-menu order is the `/projects` order: **The Economic Report Influence Graph · A homepage you drive around · A menu that is a photograph of my desk · A rare-disease site, written by a patient · A housing society's website · This site**. `assets/nav.js` makes the sub-menu a disclosure button. **To ship a case study, run `scripts/ship_case_study.py`**, then the Phase 4 writers (§3). |
| Display settings | **`assets/prefs.js`**, loaded without `defer` in every `<head>`, puts the saved choices on `<html>` (`data-motion`, `data-theme`, `data-contrast`, `data-text`, `data-lg-wait` for M2, and `data-lg-scene` for the 3D hero) before the first paint. **`assets/display.js`** builds the panel. Saved in `localStorage` under `tcv-display`, this browser only. Rules: §3. |
| Motion | **M1:** the opt-in `<style>@view-transition { navigation: auto; }</style>` **inline in each page's `<head>`** (DESIGN-5); its names and times in `style.css`; the page-swap hooks in `prefs.js`. **M2 and the scrubber:** `assets/ledger.js`, `defer`, home only. **M3:** `assets/loop.js`, `defer`, `/method` only. **The 3D hero:** `assets/ledger-scene.js`, `type="module"`, home only, with Three.js from `assets/vendor/three/`. **The second pass:** the opener's settle, the section heads' gradient and the rail in `style.css` (CSS only); the picture carried from `/projects` in `prefs.js`. **The opener's settle:** `assets/opener.js`, `defer`, case studies only. **The header:** `assets/header.js`, `defer`, every page, after `display.js`. Rules: §3. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html`, `og-src/` and `assets/vendor/three/SOURCE.md` off the live site. A preview goes in it until it ships. Nothing outside `public/` deploys (`scripts/`, `reviews/`, `ledger/`). |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. **No inline `<script>` except JSON-LD data blocks** (CSP `script-src 'self'`; Q-P4-4 A); inline `<style>` and `style=""` are allowed. Unchanged since handoff-017; the 3D hero needed no change. **`site_check.py --live` compares the served headers with `_headers`, exactly.** |
| Structured data | **`scripts/schema.py`** writes one JSON-LD block at the end of `<head>` on home (`ProfilePage` + `Person`, SD1) and each case study (`CreativeWork` + `BreadcrumbList`, SD2), from the page's own words. **Never hand-edit the block.** |
| AI crawlers | **Allowed since 2026-09-30 (INFRA-15 ruled B).** `robots.txt` allows all. The setting is in Thomas's Cloudflare dashboard (AI Crawl Control). |
| Link preview | **The six case studies and `/method` have their own card**, `assets/img/og/<page>.png`, 1200×630, from **`scripts/og_cards.py`**, with the ruled alt text OG1–OG7. Home, Projects, Background and Contact keep `assets/img/og-card.png` (source `public/og-src/og.html`); 404 has none. **An image card carries its picture's sha256**: re-run `og_cards.py` after changing a card's picture. |
| Analytics | Cloudflare Web Analytics. **Cloudflare adds its `<script>` to an HTML page unless the request's `Accept` is `*/*`** (curl sends `*/*`; Python's default sends none, and gets the script). The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` · receipts `plans/receipts-001.md` · `plans/operating-guide.md` · Phase 4 `reviews/copy-review-009.md` · **the 3D hero `reviews/copy-review-010.md`** · **the second pass `reviews/copy-review-011.md` (shipped)** · **the header `reviews/copy-review-012.md` (shipped)** |
| Design system | `public/assets/style.css` — tokens in `:root` (type in rem; theme, contrast and motion tokens after it, then M1's view-transition names and times), case-study components under the `CASE STUDIES` banner, the loop diagram (with M3), then the `build ledger` block, the 3D hero's rules at its end. The second pass: the opener after the case-study header, the section heads and the rail after the numbered sections, and the `--grad-*` tokens beside `--accent`. The header's block is last (`--metal-*` and `--smoke-*` in it, the same in both themes on purpose; `--slab-*` in it, with dark values). **Every width breakpoint is in `em`** (§3). |
| Build ledger | The end of the home hero. Written into `public/index.html` between `<!-- ledger:begin … -->` and `<!-- ledger:end -->` by `scripts/export-ledger.py`, from the handoffs plus `ledger/curation.json` (not deployed). **Never hand-edit the block.** The export also writes **`public/assets/ledger-data.json`** for the 3D hero. With WebGL: the 3D scene behind the headline. Without: a landscape SVG, a portrait SVG shown at 37.5em (600px) and under, each with a TRAPS band. Both: the scrubber (scripts only), and a `<details>` list with one ruled line per handoff. Rules: §3. |
| Graph demo | On `/work/influence-graph` only. `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js`. It reads the site's motion setting, and still waits for a click. |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. |
| Browser tests | Python Playwright + Chromium, scripts in `scripts/`:<br>- `site_check.py [--live] [--root DIR] [--draft-ledger] [-v]`: every sitemap page plus /404, the home ledger (the SVG checks run with WebGL off, `SCENE_OFF`), **the 3D hero** (draws, its data, the fallback with a control, motion, drag, the Three.js pin), the theme and contrast, the Display panel, the motion (M1, M2, M3, the scrubber), and every page's structured data and link preview; with `--live` also every header and redirect. **237 checks locally, 264 live on `main` (#76); #77 adds seven paint checks (244 locally); no known faults.** **`--live` refuses to run unless every file of `origin/main` is the same in its copy (and `--root`'s), line endings set aside (#76).** **`--chrome` runs every check in the installed Google Chrome; the paint check draws seven states in Playwright's Chromium and that Chrome and fails where they differ, wherever Chrome is installed (#77).** Every FAIL line comes again at the end, on stderr (`checklog.py`).<br>- **`budget.py [--live] [--controls] [-v]`**: each page's weight against its ruled ceiling, and axe-core's WCAG A/AA rules in light and dark. **48 checks locally, 51 live (`--live` adds the three PW3 checks, INFRA-23); one known fault, A-1's.**<br>- `cs_check.py work/<page> [--preview] [--shots DIR]`: one case study, its links fetched live.<br>- **`shots_diff.py BEFORE [AFTER] [--self] [--inject CSS] [--out DIR]`**: every page, light and dark, 1280 and 375, pixel for pixel, **with reduced motion** (the 3D hero drawn still). Run `--self` and `--inject` as controls (the footer is `footer`).<br>- All of them serve `public/` in-process with clean URLs. **Playwright's Chromium draws WebGL in software** (trap). **Playwright disables the HTTP cache once a route is set.**<br>- **In a claude.ai cloud session:** `pip install playwright` first; the scripts launch the preinstalled Chromium by path.<br>- **`--live` is for tc-ventures.ca (Cloudflare) only. Never point a headless browser at a Hostinger site** (trap). |
| Edit tools | **`patch.py`**: exact-match edits across files, all or none, keeping each file's line endings. **`ship_case_study.py`**: ships case-study previews (§3). **`schema.py`** and **`og_cards.py`**: the structured data and the cards (§3). **`quote_check.py FILE "quote"…` / `--ledger`**: each quote verbatim in its source. **`traps_curate.py [OUT]`**: drafts the traps grouping from the handoffs, with its doubts (§3). |
| Vendored | **`scripts/vendor/axe-core/`**: axe-core 4.11.4, pinned by sha512 (`budget.py` refuses a changed copy). Never deployed. **`public/assets/vendor/three/`**: Three.js 0.186.1 from cdnjs, downloaded 2026-10-02 with Thomas's OK, MIT `LICENSE`, **served**. `three.core.js` is cdnjs's `three.core.min.js` under the name the module imports. Pinned by cdnjs's sha512 (`site_check.py`'s `THREE_SHA512` checks the served files). **`.gitattributes` keeps both vendor folders byte for byte.** |
| Claude Code hook | **`.claude/settings.json`** (this repo only, ruled INFRA-14a A): a `PreToolUse` hook runs `.claude/hooks/no_cd.py`, which refuses a Bash command whose first word is `cd`. **`.claude/launch.json`** (untracked, ruled: not committed): a local preview server, `python -m http.server 8765` over `public/`, for the app's browser pane. Not clean-URL: open `/work/x.html`. |
| Research repo | `C:\Users\thoma\Desktop\My Files\Reports Clustering` = public `DriftingSplash9/Reports-Clustering`. **Never run git there** from this project's sessions. |
| Sister repos | **Theme:** local `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` = GitHub `DriftingSplash9/thomascheesman-ca-theme`, **private since 2026-09-26**. A push to its `main` deploys to Hostinger. Cached pages then need a LiteSpeed purge and a Hostinger CDN purge (Thomas). Commit/push there is pre-authorized; bump `style.css` `Version:` on every theme-code commit. **BYR:** `bareyr` = GitHub `DriftingSplash9/bareyourrare`, **private**. A push to its `main` deploys to Hostinger, then a LiteSpeed purge (Thomas). **`.htaccess` is not in the BYR repo**; it lives on the server only. |

## 2. What was done (2026-10-03, from handoff-037)

**Rulings, verbatim, in order:** "merge 73, LG38 yes, 3 yes.  look at the "C" in the "TC", it looks like
cheesman stacked instead of collapse to a "C". also, we can kill the wobble in the menu button, no need to
draw attention like that." (with a screenshot from his Chrome); "5 none yet."; "merge 74, 75, 76, keep the
lean"; "write handoff-038, and yes to the Chrome checks, headroom can be increased 100%, go ahead and tell me
what can be spectacular, remember I need to show off some skills so give me links to some award winning sites
that use modern and "spectacular" effects." Read as: "3 yes", both high-tally traps into code (#76); "5 none
yet", Q-SP5 with no award picked; the rest in copy-review-006 (LG38), 012 (the header), 013 and #77.

**Shipped, each checked live, each merged by the agent at Thomas's word after its check passed:**
- **#73** (`1938f0a`): handoff-037. **#74** (`4c1968a`): column 037 (LG38).
- **#75** (`e0e8548`): **the clean monogram and no wobble** (§3), with two header checks in `site_check.py`.
- **#76** (`5bffd55`): **two traps into code:** `scripts/checklog.py`, and `site_check.py --live`'s gate (§1).

**Open:** **#77** (`chrome-checks`): `--chrome` and the paint check (seven states in Playwright's Chromium and
Thomas's Chrome; its control is the stacked C, `dea074c`), and all twelve ceilings at the measured weight
plus 100%. Locally: `site_check.py` 244 of 244, and 244 of 244 with `--chrome`; `budget.py` 48 of 48.
**This handoff's PR:** copy-review-012's "keep the lean", copy-review-013 (TP-0), LG39's draft, `traps.json`
to 038. **Along the way:** INFRA-21 is gone (`cs_check.py work/this-site` 17 of 17).

**Own misses:**
- **The stacked C shipped in #72:** every check ran in Playwright's Chromium, which paints it clean; Thomas saw
  it in his Chrome. Now #75, and the paint check (#77).
- **handoff-037's §6 said no trap reached its drop** ("Keep every FAIL line" stood at 9.8) and left out #73,
  which column 037 needed first; caught in this session's review. **New LG38 quotes were proposed before
  reading `quote_check.py`'s rule** (trap). **A `$'\r'` broke a commit command** (trap). **The `--live` gate
  first refused an up-to-date checkout** for its line endings (trap). **A control's result went into
  copy-review-012 before the run ended;** held out of the commit until it did.

### Traps worth knowing

Each trap ends with its tally, **`x.y`** (§5).

**Dropped this handoff:**
- "Keep every FAIL line of a check run": `10.9`. Into code: `checklog.py` (#76).
- "`site_check.py --live` compares the live ledger with what the local checkout would export": `9.9`. Into
  code: `--live` refuses any copy but `origin/main`'s (#76).

**New this session:**
- **Thomas's Chrome and Playwright's Chromium can paint the same page differently.** Reproduce what he
  reports with Playwright's `channel="chrome"` (a fresh profile, never his); the paint check compares the
  two (#77). `0.0`
- **A gradient drawn with `background-clip: text` shows through every child's text, whatever the child's
  opacity or overflow, and Chrome versions disagree on it.** Where children hide, give each its own
  background. `0.0`
- **`quote_check.py --ledger` reads a row's quotes only from that row's own handoff.** Quote in §2,
  verbatim, every ruling the line will rest on. `0.0`
- **In Git Bash, `$'\r'` inside `$(...)` inside double quotes breaks the whole command.** Count line
  endings with Python. `0.0`

**Carried:**
- **A shell `&` inside a tool call may not outlive the call.** A check started that way left an empty log. Use
  the tool's `run_in_background`. `1.0`
- **Letters split into inline-blocks lose the font's pair spacing, and measured before the web font loads
  they're clipped too narrow.** Keep text inline at rest (as #75 did); measure after `document.fonts.ready`. `1.1`
- **A check run that is still going when you edit reads a mix of old and new files.** Stop it and start a clean
  run, or run from a `git archive` snapshot (as this session did). `1.1`
- **A PR stacked on another PR merges into that PR's branch if it's merged before GitHub retargets it.** Base
  every PR on `main`; check each PR's base before merging, and its merge commit on `origin/main` after. `4.4`
- **Under Playwright's software WebGL a screenshot takes one to four seconds,** so a check that times two
  captures of a moving scene measures the screenshot, not the scene. Compare pictures taken at moments that
  don't depend on how long a capture takes, and require each to have content (`colours() > 20`). `4.0`
- **A wait loop that merges when a check reports any result merges on a failure.** Wait for a pass; on a
  fail, stop and tell Thomas. `3.2`
- **A Cloudflare build can fail at the instant it starts, after minutes pending, with no log on GitHub.**
  The dashboard's "Retry build" deploys it. `3.0`
- **An Edit-tool edit or a `sed -i` on a CRLF file can rewrite the whole file as LF.** Use `patch.py` for repo
  files, and check the endings of what you changed before you commit (done this session, with Python). `3.3`
- **A background command stops at 30 minutes unless it is given a longer `timeout`.** Every long check this
  session had up to 90 minutes. `3.3`
- **`site_check.CHROMIUM` is the cloud session's Chromium path.** A scratch script that launches it fails on
  Thomas's machine; fall back to `pw.chromium.launch()` (this session's scripts and the paint check do). `3.3`
- **The app's browser pane can't take a screenshot while Claude's window is behind others,** and port 8765
  may already be held by another chat's server over this checkout. Record with Playwright
  (`record_video_dir`) instead, as this session did, in Thomas's Chrome. `3.3`
- **A scroll-driven animation whose `animation-timeline` is `none` still draws its end state.** Give the
  animation no name instead (`animation: var(--name, none) …`). `3.0`
- **An element with a view-transition name is a backdrop root, so nothing inside it can blur the page
  behind it.** `2.1`
- **At 200% text a breakpoint in `em` doubles,** so a 1280px check gets the phone layout (45em is 1440px).
  Expect it, and test the phone layout there too. `2.0`
- **A CSS transition on `font-size` makes text lag a change of text size,** and `site_check.py`'s text-size
  check reads the old size. Set a size directly, not through a transition. `2.0`
- **Wire weights exist only live,** so a change that adds to every page can make PW3 untrue, and only
  `budget.py --live` after the deploy shows it. Run after #76 this session. `2.2`
- **A change of page that starts while a view transition runs cuts it short, and its `finished` fires during
  the next page swap.** Clean-up tied to `finished` then wipes the new names; stand it down once a swap
  begins. `2.0`
- **A probe that counts one half of a view transition as a carry passes a broken carry.** Require both the
  old and the new pseudo-element. `2.0`
- **Cloudflare adds its analytics script to an HTML page unless the request's `Accept` is `*/*`.** A byte
  comparison of a page needs `Accept: */*` (curl sends it; Python's default sends none). `7.2`

## 3. Current design

**Pages live:** every page since 2026-09-28 (`/work/back-quarter` and `/work/desk-and-drawer` last); the
Display panel (2026-09-29); the step 4 layout and the step 5 motion (2026-09-30); M3, the DESIGN-5 and DESIGN-6
fixes and the `/work` redirect (2026-10-01); structured data, the link-preview cards and PL-8 (2026-10-02);
**the 3D hero** (2026-10-02); **the second pass** (2026-10-02 to 03); **the motion made visible and the header
that collapses** (2026-10-03), and its clean monogram (#75).

**The 3D hero (copy-review-010; live 2026-10-02):**
- **What it is:** the build ledger as a WebGL scene behind the home headline, from `assets/ledger-data.json`.
  Time runs into depth: a gate per handoff (its number on the left post), the newest nearest. The bands are
  lanes side by side; each item is a filament from the gate where it opened to the gate where it closed.
  Carried: teal, to the front edge, with a soft glow. Closed: muted, a square cap. Parked: dotted. The traps
  are a layer under a translucent floor: into code a cube, retired a bar, an open ring where it helped,
  dotted where a start is inferred.
- **The headline stays HTML** over the left of the scene, on a scrim (`.hero--home::after`). Above 45em
  the canvas fills the hero to under the slider (`--lg-scene-h`, set by the scene). At 45em and under it
  sits in the figure above the slider, time running up the screen.
- **It follows `ledger.js`:** every step of the slider and of M2's draw-in arrives as an `lg:show` event
  on the figure. A drag on the scene moves the slider (and so the line and the spoken value). Hover lights
  one thread and its gates and dims the rest. **No words of its own** (Q-H3 A): gate numbers and band names
  are on the page already.
- **Scrolling** (Q-H2 A): the page scrolls as normal. Under Full, the camera rises to the whole ledger as
  the hero leaves.
- **Motion:** Full: the opening (M2's draw-in, the camera pulling back), pointer tilt, easing, the rise.
  Reduced and Off: drawn whole and still; the slider jumps. **The draw-in watches the hero above 45em**
  (it starts at load), and the figure at 45em and under, as before.
- **Theme and contrast:** colours are read from the page's tokens (`--paper`, `--ink`, `--muted`,
  `--rule`, `--accent`); the glow is additive in dark, normal in light. Contrast More: no glow, filaments
  1.6× thicker, the floor 90% opaque (not fully: an opaque floor hides the traps; ruled with S2).
- **The fallback:** `prefs.js` marks `<html>` `data-lg-scene` on the home page when WebGL2 and modules
  exist; CSS hides the SVG pictures while the mark is on. The scene sets it to `on` once it draws, and
  removes it, and its canvas, if anything fails (no WebGL, Three.js or the data not loading). Three.js is
  imported inside the scene's code, so a failed load gives up at once. `prefs.js` lifts the mark after 5 s
  if the scene hasn't drawn.
- **The top bar sits above it** (`.topbar { position: relative; z-index: 30 }`), or the scene's stacking
  context covers the Display panel and the sub-menu.
- **Its marks are counted from the data:** a mark with no room logs a console error. If you add a kind of
  mark, size its instanced mesh from the data the same way.
- **Speed:** pixel ratio capped at 2 (1.5 at 45em and under); drawing stops off-screen and in a hidden tab,
  and when nothing moves. **Frame times on real hardware haven't been measured** (DESIGN-8).
- **Weight:** Three.js is 808 kB decoded; home's ceiling is in `CEILINGS`.

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
  says each build has a case study (PJ20). **Since SP-B every build has a picture there, each marked
  `data-carry="/work/<slug>"`**, the four live sites included (captions SPB1 to SPB3).
- **Every case study's `<title>` is its H1 plus " - Thomas Cheesman"**, and `og:title` repeats the title
  (C-26 fixed 2026-10-02).
- **"Honest limits" in "What shipped" states what is still wrong.** These lines go stale when the thing
  they describe changes:
  - BYR's host limit (O-16).
  - The Back Quarter's "can't be driven on a phone or tablet yet" (O-20).
  - The Desk's "five / thirteen" (counted in `inc/desk-menu.php`).
  - `/work/this-site`'s known fault on two pages and its screen-reader line (A-1). Its weights are dated
    ("Measured on 2 October 2026"), so they don't go stale; new numbers come only from `budget.py --live`,
    through a copy review.
  - **`/work/this-site`'s "Two things are heavy"** (TH1) and its rules row (TH2) name the home ledger and
    the graph: they change if either does.
  - **PW3's range on `/work/this-site`** ("Measured on 3 October 2026, … between about 220 kB and 790 kB",
    TH3d): **`budget.py --live` checks it (INFRA-23)**: the lightest page within 5% of the lower number, the
    heaviest at or under the upper and within 5% of it, and the heaviest `/projects`. **Run it after every
    merge that adds weight**; SP-B and the header each broke it once.
- **A building on the Back Quarter opens on Enter.** Copy never says driving up opens it.
- **On thomascheesman.ca the plain list is the default menu.** The desk is a second menu behind "T's
  Desktop".
- **Theme specs are quoted verbatim with their date and section, and "The repo is private."** They are
  never linked (Q-BQD1 A).
- **A screenshot of this site goes stale when the site changes.** `/work/this-site` has two. Its home page
  (Fig. 1, the opener) was retaken 2026-10-02 with the 3D hero, and its card re-made from it. Its GPRS
  case-study screenshot was retaken 2026-10-02 after SP-A, with its alt text (SPA2). Both: light, Reduced,
  1280×720, WebP quality 70.

**`/method`:**
- **The H1, the lede and the page title are Thomas's rulings.** Don't edit them, explain the
  accessibility line, or raise them again unasked.
- Research-project rows link receipts-001 §3C.

**Nav:**
- **To ship a case study:**
  1. `python scripts/ship_case_study.py work/<slug> [work/<slug> …]` (`--dry-run` first). It refuses,
     writing nothing, unless `PLANNED_SUBMENU`, the live sub-menu, every page and label = H1 agree. It
     doesn't touch `/projects` or the home cards: that's copy.
  2. `python scripts/schema.py`: its structured-data block.
  3. Its card: a `CARDS` line and an `ALT` line in `og_cards.py` (the alt text through a copy review), then
     `python scripts/og_cards.py`.
  4. Its ceiling in `budget.py`'s `CEILINGS` (a ruled number).
  5. **Its opener (SP-A) and its picture on `/projects` with `data-carry` (SP-B)**, plus its section ids
     if they are new (SP-C).
  - `site_check.py` fails a case study without its block (2), and `budget.py` one without a ceiling (4).
    **Nothing fails a case study without a card (3):** it just keeps the site card.
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
- **The button:** after the nav; it shows only when scripts run. Since the header (copy-review-012) it is a
  smoked-glass button with the accessibility symbol; its name for screen readers is still "Display". If
  `display.js` fails to load while scripts run, the button shows and does nothing (accepted).
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
  - **The opt-in is inline in each page's `<head>`, never in `style.css`** (DESIGN-5). `site_check.py`
    holds `style.css` back 300ms and needs the transition every time.
  - Chrome/Edge 126+ and Safari 18.2+; others change pages as before.
  - The top bar is `topbar`, and **its three parts are named apart** (`tb-name`, `tb-nav`, `tb-display`):
    they slide over `--move` (0.6s). **The page sinks back as the new one lifts 56px into place, over
    0.7s** (the moves times `--move`, so Reduced is a plain cross-fade). Made visible 2026-10-03.
  - **Under Full only,** `prefs.js` names the clicked `#navsub-work` link and the new page's `main h1`
    `cs-title` for that one change of page (0.9s), and clears them after. **`site_check.py`'s M1 checks
    hold these ruled times;** change both together.
  - Reduced: the cross-fade, nothing moving. Off: `prefs.js` skips the transition on both pages.
  - `prefs.js` handles the promises of any transition it sees (`quiet()`).
- **M2, the draw-in:** under Full, `ledger.js` clips the threads to 001 and draws them to the newest (0.11s
  a handoff) the first time its target is 35% in view (the hero above 45em when the 3D hero is loading,
  otherwise the figure). Reduced and Off: whole from the start. Touching the slider stops it.
  - **Never shown whole first (DESIGN-6):** on the home page under Full, `prefs.js` marks `<html>` with
    `data-lg-wait` before the first paint, and `style.css` hides the SVG threads while it's on. `ledger.js`
    lifts it on every path. If `ledger.js` hasn't run after 3s, `prefs.js` lifts it.
- **M3, the method loop:** under Full, the first time `/method`'s loop diagram is half in view,
  `loop.js` adds `.is-tracing`. Each step and arrow pulses teal in the loop's order (0.5s each, 0.22s
  apart), then the dashed return arrow (1.2s).
- **The scrubber:**
  - A native `<input type="range">`, one step per handoff, starting at the newest. Label LS1, "Step
    through the handoffs" (curation `copy.scrub`).
  - Moving it clips both SVG pictures' threads at that column, marks the column, shows that handoff's
    line, and moves the 3D scene to that handoff.
  - **At a past handoff a thread that closed later is drawn open** (Q-S5-1 B), in the SVGs and the scene.
  - **All lines are stacked in one grid cell**, so its height never changes.
  - The spoken value: "handoff-017, 2026-09-24: <the ruled line>".
  - In the SVG landscape layout its track ends sit under the first and last columns (`--lg-from`,
    `--lg-to`); with the scene on, it's full width, at most 34rem above 45em.
  - Scripts only; the list carries every line without them. **The export leaves the scrubber out unless
    `copy.scrub.ruled` is set.**

**Phase 4 (copy-review-009; live 2026-10-01 to 2026-10-02):**
- **The budget (`budget.py`):** each page's weight is its own files as decoded, once scrolled to the end,
  the larger of 1280 and 375 wide. **The ceilings are ruled numbers** (Q-P4-8 A: the measured weight plus
  10%, rounded up to the next 10 kB; later 25% and 33%). **Raising one is a change Thomas rules,** and the
  comment by `CEILINGS` holds every number with its ruling. **With #77, all twelve are the measured weight plus
  100%** (Thomas, 2026-10-03: "headroom can be increased 100%"). PW3 is not a ceiling: it's a sentence of
  fact. A page without a ceiling fails. `--live` adds what crossed the wire.
- **The accessibility rules (`budget.py`):** axe-core's WCAG 2.0 to 2.2 A and AA rules, every page, light
  and dark; any violation fails. **`KNOWN` marks a violation by page and rule,** owned by an open item. Now:
  A-1's `nested-interactive` on the two loop diagrams (Q-P4-9 A). Adding a line to `KNOWN` is Thomas's call.
- **Structured data (`schema.py`):** the block is written from the page's own words. **Re-run it after
  editing any of those.** **The only inline `<script>` allowed is a JSON-LD block** (Q-P4-4 A).
- **The cards (`og_cards.py`):** drawn from the page. **The alt text in `ALT` is ruled copy (OG1–OG7).**
  Each card stores its page, H1 and (image cards) its picture's sha256, so **a card left behind by a
  changed H1 or picture fails `--check`: re-run the script.**
- **Headers and redirects:** `site_check.py --live` compares every served header with `_headers` and every
  `_redirects` line with what's served.
- **After every merge: `python scripts/deploy_wait.py N`.** Then `site_check.py --live` from an up-to-date
  `main` (a `git archive origin/main` into the scratchpad does it without touching the checkout; any other
  copy is refused, #76).
- **PL-8 (live 2026-10-02):** `/work/this-site`'s honest limits carry the budget's numbers, on the wire and
  dated (Q-PW1 A). They are ruled copy (PW1 to PW5, TH3 to TH3d): change them only through a copy review. The
  range is TH3d's, 220–790 kB, measured 3 October 2026 (#69).

**The header (copy-review-012; live 2026-10-03, second form #72):**
- **`assets/header.js`** on every page, `defer`, after `display.js`. Without it the bar is the plain one (no
  rule since #72).
- **At the top of a wide page:** no fill, no rule. The name, then Projects (its arrow inside), Method,
  Background and Contact as smoked metallic pills, then Display (the accessibility symbol).
- **Folded** (`data-compact`, from half-way through the first 160px of scroll; always on a phone or wherever
  the four pills don't fit beside the name): TC, the faint page name, **Menu, then Display at the far right**,
  on the **slab**.
- **The slab** (`.topbar__inner::before`): a square-section bar, 3px corners, a lit top face, a shaded bottom
  and depth. Under Full it turns a few degrees to face the pointer (or with a phone's tilt; `--bx`, `--by`),
  its light sliding as it turns (`--lx`, `--ly`): warm sun on the light theme, cool moon on the dark
  (`--slab-*`). Level and still while the menu is open, and under Reduced and Off. Contrast More: plain and
  solid. **No blur:** the bar's view-transition name makes it a backdrop root (trap).
- **The name:** the link keeps `aria-label="Thomas Cheesman"`. Its letters are inline at rest (the font's own
  spacing) and boxes only while folding (`data-folding`); measured after `document.fonts.ready`. **While it
  folds, each letter paints its own slice of the gradient** (`--wm-grad`; `header.js` places it from layout
  positions, since the slab turns): painted through the whole name, the gradient showed through the fallen
  letters, piled on the C in Chrome 154 (#75). Contrast More and forced colours set `--wm-grad: none`. Where the
  full name doesn't fit beside the buttons, the monogram shows from the start. The name is in the teal
  gradient on every page, scripts or not (`--grad-3t`, 4.6:1).
- **The pills** (`.glassbtn` and the nav's links): smoked glass, metallic light-teal lettering and rims, the
  same on both themes (`--metal-*`, `--smoke-*`); every lettering stop 4.5:1 or better on the smoke. The page
  you're on has a brighter rim. In the Menu panel the links are plain words on a solid panel.
- **Menu** leans (pointer; a phone's tilt, an iPhone asks once on the first tap). **No wobble** (Thomas, 2026-10-03;
  "keep the lean"). **Back to top**
  (HD2) sits at the bottom left once a screen is scrolled.
- **The faint page name** (its nav label) sits on the slab, with the section being read on a case study or
  `/method`; no label words (never "you are here"). **No progress line** (Thomas dropped it).
- **`site_check.py` opens Menu first** wherever the bar is compact. Section links stop below the bar. **A new
  page needs `<script src="/assets/header.js" defer></script>`** after `display.js`, as the 13 have.

**Look and feel:**
- Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode by the OS or the Display panel.
- Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
- Confirmed; stop re-litigating it.

**Case-study layout (approved 2026-09-22):**
- Two lanes: a wide lane (1040px) for headers, figures, tables and lists, and a reading lane (66ch) for
  prose. A sticky 200px rail at 73.75em and wider with the section index.
- Sections are numbered by CSS counters, figures `Fig. N` per page. Receipts are small mono links with a
  leading `→`.

**The second pass (copy-review-011; live 2026-10-02 to 2026-10-03):**
- **The opener (SP-A):** each case study's own picture, moved with its caption, sits under the claim and
  before the meta strip, in the wide lane: `figure.cs-opener` > `.cs-opener__frame` (the frame clips the
  motion), loaded eagerly with `fetchpriority="high"`. It is Fig. 1: the `fig` counter starts at
  `.cs-layout__main`. Bare Your Rare's is its structured-data excerpt, set large, its caption unnumbered.
  Under Full and System, `opener.js` settles the picture from 1.2× (the excerpt 1.08) with a parallax drift
  as the page scrolls through the first 70% of a screen, eased so a stepped wheel glides; `prefs.js` sets
  the starting pose before the first paint (`data-opener`).
- **The carried picture (SP-B):** under Full, `prefs.js` names the build's `[data-carry]` picture on
  `/projects` and the case study's `.cs-opener__frame` `cs-pic`, both ways (Back too), only when on screen,
  reading the other page from the Navigation API. 0.9s, and the new page waits 0.18s behind it (the `carry`
  view-transition type). **On Back, `/projects` brings the picture into view before naming it** (the browser
  restores the scroll too late), and a swap that starts mid-transition stands the old clean-up down.
  Reduced: the cross-fade. Off: skipped, as M1.
- **The section heads (SP-C):** the section number is set large (up to 7.5rem) in the display face beside
  the section's name, filled with a teal gradient (`--grad-1` to `--grad-3`, with `--dark-grad-*`; each
  3:1 or better on its ground) that drifts on three loops of 23, 37 and 53 s, each section offset. Contrast
  More: the solid accent; forced colours: `CanvasText`. `/method` shares the template and has them too.
- **The rail's progress (SP-C):** at 73.75em and wider, under Full and System, each index line fills with a
  teal bar while its section is read: a view timeline per section id, `timeline-scope` on `.cs-layout`.
  **A new section id needs its timeline name, its scope entry and its `--cs-tl`/`--cs-fill` pair**, or its
  line has no bar (never a full one).
- **Scroll-driven and endless animations are gated by selector,** not by `--move`: `:root[data-motion="full"]`
  plus `:root:not([data-motion])` under `prefers-reduced-motion: no-preference`. A scroll timeline has no
  time to multiply. **New motion of this kind follows the same pattern.**

**Home page:**
- **Label:** "Thomas Cheesman · Grande Prairie, Alberta · remote".
- **H1:** "I run a nonprofit's website, and I hold it to a written standard."
- **Lede** from R3/R4, 52ch. **R5 under it is one sentence**: "I am looking for remote work running a
  nonprofit's website and digital operations."
- Every project card links its case study. The "How I work" heading links `/method`.

**The build ledger (copy-review-006):**
- **Order in the hero:** label, H1, lede, R5, the buttons, then the ledger (the scene or the pictures, the
  scrubber, the caption), then its list.
- **The block is generated.** To change it: edit `ledger/curation.json` or the handoffs; run
  `python scripts/export-ledger.py` (it writes the block and `ledger-data.json`), then `--check`, then
  `site_check.py`; ship.
- **A handoff's column appears only once its line is ruled** (`ruled` in the curation). At wrap:
  1. Draft the new handoff's line in copy-review-006 (LG35 for 034, LG36 for 035, and so on).
  2. Add it to the curation with `"ruled": null`.
  3. Run `python scripts/quote_check.py --ledger` on its "Rests on" quotes.
  4. After Thomas rules, set `ruled`, export and ship.
- **The ledger's list links each handoff file on GitHub `main`,** so a handoff's PR merges before its
  column ships.
- **A line** never copies handoff prose, says "I" only for what Thomas did, and leaves out the private
  project, other sites' incidents and anything familial.
- **Items are drawn solid unless the curation's `parked` lists them** (dotted). **Parking only changes a
  thread still open at the last column.**
- **What's never drawn:** O-\* and L-\* items, and rows under OTHER REPOS or LANDER.
- **A new §4 workstream heading stops the export** until the curation's `bands`, `fold` or `exclude` says
  where it goes.
- **An ID whose wording changes is a DOUBT in `--report`** until `reviewed_ids` or `split` records it.
- **`site_check.py --live` fails whenever the live block or `ledger-data.json` isn't what the script writes
  now.** That's intended.
- **The caption's traps sentence starts "Under the items are the traps"** (TC1): true of the SVG and the
  scene. The SVGs' own descriptions (`desc_land`, `desc_port`) still say "bottom band" / "right-hand band",
  true of the SVGs.

**The traps (copy-review-008; live 2026-10-01):**
- **`ledger/traps.json`** holds one entry per trap: `start`, `end` (or null while carried), `how` (`into
  code` or `retired`), `helped` (handoffs where its y rose) and `wordings` (every name it had, for matching).
- **The page never shows a trap's words.**
- **The export refuses to write when `traps.json` doesn't match the handoffs** (every trap line matched
  to one trap by its bold lead and start; Dropped lines counted against ended traps by handoff and
  start). **So a carried trap keeps its lead word for word,** or its new lead goes into `wordings`.
- **At every wrap, before the handoff's column can ship:** add the handoff's traps to `traps.json`:
  - a new trap: a new ID (T58, T59 …), `start` this handoff, `end` null, its lead as its wording;
  - each carried trap whose y rose: this handoff in `helped`; a reworded lead: add it to `wordings`;
  - each dropped trap: `end` this handoff and its `how`. **"Into code" only when code now does the
    job;** "belongs in code" with nothing built is retired (TD4).
  - Then `python scripts/export-ledger.py --report --draft` must show no traps line.

**Standing rules:**
- **The Rocket Lander is private.** Not here, in any form.
- `object-fit: contain`, never `cover`.
- **Content renders without JavaScript.** JS is allowed on top, as much as the design wants; the words
  and links must not depend on it. **No build step. A library is allowed as a pinned, vendored file served
  from `/assets/`** (ruled 2026-10-02, "both ok"; Three.js is the first). A tool for the checks lives in
  `scripts/` and is never deployed.
- **No inline script** (the CSP), **except a JSON-LD data block** (Q-P4-4 A). Code that must run before the
  first paint goes in a small file in `/assets/`, as `prefs.js` does. Data a script needs goes in a file
  (`ledger-data.json`), not an inline block.
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
- **Copy ships only through a copy review** (numbered blocks; OK / KEEP / A / B / FIX / CUT). **A change
  that makes shipped copy untrue ships with its fix** (TH1 to TH4 shipped with the hero).
- **Accessibility controls are built in, never an overlay widget** (PL-6).
- **Never link `reviews/copy-review-001.md` from a page** (T0).
- **Never run git in `Reports Clustering`** from this project's sessions.
- **The outside research model is never named in copy** (F-2), and no link's path may carry its name.
- **Don't link the `@bareyourrare` social accounts anywhere until Thomas says they are claimed** (O-18).
- **Never link a theme-repo file or commit.** Read it for facts only (Q-BQD1 A).
- **Never load a Hostinger site in a headless browser from Thomas's machine.**
- **A change meant to be invisible is proved with `shots_diff.py`**, with its `--self` and `--inject`
  controls.
- **Base every PR on `main`** (the #55 trap).

**Demo and embed rules:**
- **Nothing heavy loads before a click, except the home page's 3D hero** (ruled 2026-10-02, "both ok"). A
  gated page degrades when the payload is absent.
- The 3D canvas on `/work/influence-graph` keeps its own dark ground, in both themes. The home scene takes
  the page's ground.
- `basis` is quoted, never paraphrased. The written chain under the graph is the accessible equivalent.
- Nothing rearranges a layout on interaction; the sub-menu and the Display panel overlay and move nothing,
  and the scrubber keeps one height.
- **Show finished work:** unfinished work is labelled honestly or left off.

## 4. Open items — carry these forward until closed

### PLAN
| # | Item | Notes |
|---|---|---|
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Phases 1 to 4 ✓ → the 3D hero ✓ (2026-10-02, copy-review-010) → **the second pass ✓ (2026-10-03, copy-review-011)** → **the third pass proposed (copy-review-013, TP-0, 2026-10-03), for Thomas to rule**. Q-SP5: "5 none yet" (no award picked); when he picks, the agent prepares what each asks for, proposed before built. |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-20 | **`/work/this-site` states things that will go stale** | "rebuild in progress" (header) and "has not had a screen-reader run-through yet" (honest limits). Update each when its thing changes. |
| C-15 | Résumé: **the summary ends on a one-word line ("roles.")** | **Ruled A: fix it at the next résumé edit,** in the Word file and its HTML mirror; Thomas exports; exactly two pages. |
| C-16 | **Job history, from Thomas 2026-09-23. Use these** | GPRS board: elected at the **June 2023** AGM (first meeting September). Majors consulting: May 2019 – **June 2020**. **Head Chef, Ric's Grill, Sep 2013 – Jul 2014.** **Executive Chef, Township 71, Jul 2014 – Jun 2015** (renovation from Oct 2014, opened Nov 2014, closed May 2015, wind-down through June). **Taught one GPRC semester, Sep – Dec 2014.** |
| C-13 | GPRS site history | WordPress.com 2023; self-hosted WordPress.org on Hostinger 2025 "because I wanted more freedom to experiment with the code." No month-level dates without asking. |
| C-17 | R4 wording, his call | Live: "…then build it with help writing by AI." **Do not raise it again or change it unasked.** |
| C-21 | **`/method` H1, lede and title: his call (2026-09-25)** | Same standing as C-17. |
| C-9 | `page-thomas.php` ~2010 | Ruled B, done by the theme session in 1.0.762. The theme's V0.46 owns it. |

### DESIGN
| # | Item | Notes |
|---|---|---|
| DESIGN-8 | **The motion's frame times on real hardware** | Only measured in Playwright's software WebGL. Thomas's PC (and a phone, if he has one to hand) would show whether the 3D hero's opening and drag, the scroll, the picture carried from `/projects`, the drifting section numbers and **the header's fold, the slab's turn, and Menu's lean** stay smooth. **The phone's tilt has only been simulated:** try it on a real phone (an iPhone asks first). Check before any submission. |

### PROJECTS / GRAPH
| # | Item | Notes |
|---|---|---|
| — | No open items | |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add every case study, `/method` and the Projects sub-menu to that run. One real screen-reader run through the live graph on `/work/influence-graph`. **Points for it:** the loop diagrams' links sit inside an SVG with `role="img"` (axe-core's `nested-interactive`, a known fault in `budget.py`); the diagrams' connectors in `--rule` are faint on white; the home ledger's `role="img"` SVGs and its `<details>` list; **the 3D hero: its canvas is `aria-hidden`, so the slider's spoken value and the list carry the ledger; the text over the scene sits on a scrim (axe can't judge contrast over a canvas)**; the Display panel's radio rows and real Windows high contrast; **the second pass: the section numbers are text over a gradient with transparent fill (check them in real Windows high contrast and with a screen reader), the rail's bars, the carried picture and the opener's settle with reduce-motion on**; a real browser at 200% text; the scrubber with a screen reader; M1, M2, M3 and the scene with the OS's reduce-motion on; **the header: the slab's contrast as it turns and its light slides, the pills' metal lettering, the Menu button and its panel with a screen reader and the keyboard, the monogram's name, Display as a symbol, Back to top's focus, and the glass in Windows high contrast**. |
| A-3 | **Sub-menu without JS cannot be dismissed with Esc** | Accepted as the no-JS fallback; for A-1 to confirm. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-22 | **Cloudflare's automatic builds failed at their start, 2026-10-03** | Both of #63's (branch and `main`): minutes pending, then failed at the instant they started, no log on GitHub. Thomas's manual "Retry build" deployed `d02bc52`. If it happens again, read the build's log in the dashboard before anything else. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address. |
| INFRA-9 | HSTS 1 yr, no `includeSubDomains`, no `preload` | Deliberate; both are hard to undo. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. **He will renew on 2026-10-07** (said 2026-09-27). Reminded every day since 2026-09-30, twice on 2026-10-02, and three times on 2026-10-03. **Not confirmed paid.** |
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

**Closed since handoff-037:** INFRA-21 (re-tested 2026-10-03: `cs_check.py work/this-site` 17 of 17, links
answer 200).

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

## 6. Next up — Thomas rules the third pass

Before anything: remind Thomas once of **D-3**, if it's still open. It's due 2026-10-08; he said he'd renew
on 2026-10-07.

1. **Put the open rulings to him in one numbered list**, each a yes or no with your recommendation:
   - **Merge #77** and **this handoff's PR**, each on his word after a passing check. #77 changes no served
     file, so `deploy_wait.py` only gates it and reads the build; then `site_check.py --live` from an archive
     of `origin/main`, the paint checks' first live run.
   - **LG39**, this handoff's line (copy-review-006), after #77 is merged; no change to `parked`. When it's
     OK, ship column 038 as 037's was (#74): set `ruled`, export, `--check`, `--report`, `quote_check.py
     --ledger`, `site_check.py`, a PR **based on `main`**, merged on his word **after a passing check**, then
     `deploy_wait.py N`, `site_check.py --live` and `budget.py --live`.
   - **TP-0 with Q-TP1 to Q-TP4** (copy-review-013), with the recommendations written there.
2. **Then build the third pass in the order he rules,** one piece per PR, based on `main`, with a recording in
   his Chrome at every step (`channel="chrome"`, a fresh profile; light, dark, a phone) and each new state in
   `site_check.py`'s `PAINT`. **Weight added to `/projects` breaks PW3** (786 of 790 kB on the wire, found
   2026-10-03): its sentence goes through a copy review (TH3e) in the same PR.
3. **DESIGN-8:** he tries the live site on his PC and a phone, the tilt on a real phone too.
4. **At the next wrap** no trap reaches its drop. At 040: "Under Playwright's software WebGL…"; at 041: the
   analytics-script trap (x = 10), "A Cloudflare build can fail…" and "A scroll-driven animation…" (y = 0).
