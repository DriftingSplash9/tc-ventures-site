# handoff-026 — tc-ventures.ca

**Written:** 2026-09-30
**Covers:** one session, 2026-09-29 evening to 2026-09-30:
- **Thomas's rulings on handoff-025's open points,** from his filled-in `handoff-025-decisions.xlsx` (32 rows).
- **LG26 ruled; ledger column 025 live** (PR #23, which also landed #22, handoff-025).
- **The `cd` hook (INFRA-14a),** `www.tc-ventures.ca`, Always Use HTTPS and the AI crawlers (INFRA-11, INFRA-15).
- **Phase 3 step 4, the layout,** at Thomas's word "go straight to Phase 3 step 4": DESIGN-1, 2, 3, the new
  DESIGN-4, and G-7. Ruled "s4-1 A, s4-2 A", shipped as PR #24 on "merge 24".

**Status at wrap:**
- **Live on tc-ventures.ca, verified 2026-09-30:** `main` at `55f8469` (PR #24). Merged by the agent at
  Thomas's word.
  - The check-run "Workers Builds: tc-ventures-site" on `55f8469` completed with success at 16:00:46 UTC.
  - Curl, cache-busted: `/assets/style.css`, `/` and `/404` are byte-identical to `main`. Control: each
    differs from the pre-merge `421c009`.
  - `site_check.py --live` passed 193 of 193, **with no known faults left.**
- **#23** (ledger column 025 and the hook) was checked live the same way when it merged (§2).
- **thomascheesman.ca:** nothing changed from this session. A separate theme session did the items Thomas
  ruled (C-9, O-24a, b, d, INFRA-17): the theme's `main` is at `8116d50`, "V0.46: handoff-025 theme
  rulings (1.0.762) and tools/ harnesses". Read here: its commit log and its diary row only, not V0.46,
  the code or the live site.
- **LG27,** this handoff's ledger line, is drafted in copy-review-006 with `"ruled": null`. The live ledger
  stops at 025 until it's ruled.

**The next job is §6.**

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. Read §2 "Traps" before you touch git, a checker script, a screenshot, the theme
   repo, a Hostinger site, or the `Reports Clustering` folder. **Especially: do not load thomascheesman.ca
   in a headless browser from Thomas's machine.**
2. The twenty truth rules: in Thomas's global `C:\Users\thoma\.claude\CLAUDE.md` (it says it's the only copy
   since 2026-09-29) and, as of this wrap, still in this repo's `CLAUDE.md` too (§4 INFRA-20).
   `plans/operating-guide.md` is how Thomas and the AI divide the work, and §4 there is the checking
   routine.
3. **`plans/plan-001-showcase.md`**: the plan. The §5 note (2026-09-25) holds the order.
4. **`reviews/copy-review-007.md`: Phase 3.**
   - Steps 2, 3 and 4 are built, ruled and live.
   - **Step 5, the motion, is next.**
   - Its copy block (the scrubber's label) goes here too.
5. **`plans/receipts-001.md`**: the ruled inventory, 49 OK / 81 CUT. Only OK rows go in copy. Tick `chk`
   before quoting a row.
6. **`reviews/copy-review-006.md`**: the build ledger's rulings. LG27, this handoff's line, is drafted there.
7. The shipped pages under `public/`. **`work/back-quarter.html` and `work/desk-and-drawer.html` are the
   newest instances of the case-study pattern.** The home hero ends with the build ledger (§3).
8. **`scripts/`**: each script's docstring is its manual.
   - The checkers: `site_check.py`, `cs_check.py`, `byr_bot_check.py`, `shots_diff.py`, `quote_check.py`.
   - The writers: `export-ledger.py` (plus `ledger/curation.json`), `patch.py`, `ship_case_study.py`.
9. **If the job touches thomascheesman.ca:** the theme repo's `CLAUDE.md` and its newest `V0.*.md`
   (**V0.46**), and `docs/IMAGE-BURST-PLAN.md`.
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
- He rules tersely ("pj15-19 ok, A, dd3 A, keep, rest ok"), and that is a full ruling.
  - **Ask what a bare number means** ("1" meant OK).
  - **Say how you read a bare letter** ("A" was read as DD1's H1, the only A/B left) and record it.
  - **This session he ruled in a spreadsheet** the agent built (`Claude outputs/handoff-025-decisions.xlsx`,
    filled copy on his Desktop): a letter per row, "EXPLAIN BETTER" for one, a pasted URL for another.
    Read the options column to know what each letter means.
- **He sometimes hands a call over** ("fix it", "up to you"). Make it, say in one line what you chose and
  why, and record it as delegated.
- **He changes his mind, and says so.** Record the new ruling next to the old one.
- **"pause here" means start nothing new.** Record what he ruled and wait.
- He is self-taught and model-agnostic, so explain methods, not one model's tricks.
- When he asks how something works, give him the plain version first.
- **He commits, pushes and merges himself, sometimes mid-session.** Re-read `git status` and `origin/main`
  just before you commit.
- **His merges don't always land** (§2 trap).
  - This session he said "merge 23" and "merge 24", and the agent merged each one.
  - Each was per-PR permission, not a standing one.
- **He does dashboard work himself** (Cloudflare, WordPress.com), with the agent giving the steps and
  checking the result by curl. A screenshot of where he's stuck is his way of asking.

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
| Deploy | **A merge to `main` deploys** → Cloudflare builds. **No cache to purge.** Branch pushes build too, and the bot calls them "Deployment successful", but they don't reach the site (trap below). This session's two merges were each live at the first curl, after their merge commit's check-run completed. |
| Addresses | **`www.tc-ventures.ca` 301s to `https://tc-ventures.ca`, keeping the path and query** (2026-09-30): a proxied `www` CNAME plus the Redirect Rule "www to apex 301" (`https://www.tc-ventures.ca/*` → `https://tc-ventures.ca/${1}`). **Always Use HTTPS is on** (2026-09-30), so `http://` on either host 301s to https first. All four combinations checked by curl. |
| Contact email | `thomas@tc-ventures.ca` |
| Pages | `index`, `projects`, `method`, `background`, `contact`, `404`, `work/influence-graph`, `work/back-quarter`, `work/desk-and-drawer`, `work/bare-your-rare`, `work/gprs`, `work/this-site`. Internal links, canonicals and sitemap use **clean URLs** (`/method`); `/x.html` 307s to `/x`. No case study is planned. |
| Nav | **Projects (with a sub-menu of the case studies) · Method · Background · Contact**, then the **Display** button, on every page: **13 files** including `_template.html`. The sub-menu order is the `/projects` order: **The Economic Report Influence Graph · A homepage you drive around · A menu that is a photograph of my desk · A rare-disease site, written by a patient · A housing society's website · This site**. The markup is copied into each page; `assets/nav.js` makes the sub-menu a disclosure button. **To ship a case study, run `scripts/ship_case_study.py`** (§3). |
| Display settings | **`assets/prefs.js`**, loaded without `defer` in every `<head>`, puts the saved choices on `<html>` (`data-motion`, `data-theme`, `data-contrast`, `data-text`) before the first paint. **`assets/display.js`** builds the panel. The choices are saved in `localStorage` under `tcv-display`, in this browser only. With no choice (System), the OS settings decide through CSS. Rules: §3. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html` and `og-src/` off the live site. A preview goes in it until it ships. |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. **No inline script** (CSP `script-src 'self'`). Unchanged since handoff-017. |
| AI crawlers | **Allowed since 2026-09-30 (INFRA-15 ruled B):** GPTBot, ClaudeBot, ChatGPT-User and Claude-User each get 200 on `/`, checked by curl with each one's user agent. `robots.txt` allows all. The setting is in Thomas's Cloudflare dashboard (AI Crawl Control). |
| Link preview | `assets/img/og-card.png` 1200×630 on all pages. Source `public/og-src/og.html`. LinkedIn's copy matches it (INFRA-10, 2026-09-30). |
| Analytics | Cloudflare Web Analytics, injected at the edge. The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` · receipts `plans/receipts-001.md` · `plans/operating-guide.md` · Phase 3 `reviews/copy-review-007.md` |
| Design system | `public/assets/style.css` — tokens in `:root` (type in rem; theme, contrast and motion tokens after it), case-study components under the `CASE STUDIES` banner, then the `build ledger` block at the end. **Every width breakpoint is in `em`** (§3). |
| Build ledger | The end of the home hero. Written into `public/index.html` between `<!-- ledger:begin … -->` and `<!-- ledger:end -->` by `scripts/export-ledger.py`, from the handoffs plus `ledger/curation.json` (not deployed). **Never hand-edit the block.** No JS: a landscape SVG, a portrait SVG shown at 37.5em (600px) and under, and a `<details>` list with one ruled line per handoff. Rules: §3. |
| Graph demo | On `/work/influence-graph` only. `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js`. It reads the site's motion setting. |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. |
| Browser tests | Python Playwright + Chromium, scripts in `scripts/`:<br>- `site_check.py [--live] [--root DIR] [--draft-ledger] [-v]`: every sitemap page plus /404, the home ledger, the theme and contrast, and the Display panel. **193 checks, no known faults.** "Text at 200%" is set the way the browser's own text-size setting sets it (CDP `Page.setFontSizes`), at 375, 480, 760 and 1280px, with the sub-menu shut and open.<br>- `cs_check.py work/<page> [--preview] [--shots DIR]`: one case study. **`--preview` checks `PLANNED_SUBMENU`**, the menu a preview will ship with.<br>- **`shots_diff.py BEFORE [AFTER] [--self] [--inject CSS]`**: every page, light and dark, 1280 and 375, pixel for pixel between two copies of `public/`. It's the proof of "no visible change". Run `--self` and `--inject` as controls.<br>- All of them serve `public/` in-process with clean URLs.<br>- **In a claude.ai cloud session:** `pip install playwright` first. The scripts launch the preinstalled Chromium by path (trap below).<br>- **`--live` is for tc-ventures.ca (Cloudflare) only. Never point a headless browser at a Hostinger site** (trap). |
| Edit tools | **`patch.py`**: exact-match edits across files, all or none, keeping each file's line endings. A match found twice is refused; for one rewrite that applies to every copy, pass the whole file as one edit. **`ship_case_study.py`**: ships case-study previews (§3). **`quote_check.py FILE "quote"…` / `--ledger`**: each quote verbatim in its source, and each piece is its own control. |
| Claude Code hook | **`.claude/settings.json`** (this repo only, ruled INFRA-14a A): a `PreToolUse` hook runs `.claude/hooks/no_cd.py`, which refuses a Bash command whose first word is `cd`. A `cd` later in a command passes. |
| Research repo | `C:\Users\thoma\Desktop\My Files\Reports Clustering` = public `DriftingSplash9/Reports-Clustering`. **Never run git there** from this project's sessions. Read its files, and read it on GitHub. |
| Sister repos | **Theme:** local `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` (not `Desktop\tc-ventures-child-theme`, which the global CLAUDE.md names) = GitHub `DriftingSplash9/thomascheesman-ca-theme`, **private since 2026-09-26**. A push to its `main` deploys to Hostinger; GitHub answers the push with "This repository moved" (the local remote uses the old name) and the push still lands. Cached pages then need a LiteSpeed purge and a Hostinger CDN purge (Thomas). Commit/push there is pre-authorized; bump `style.css` `Version:` on every theme-code commit. **BYR:** `bareyr` = GitHub `DriftingSplash9/bareyourrare`, **private**. A push to its `main` deploys to Hostinger, and cached pages then need a LiteSpeed purge (Thomas, in WordPress). **`.htaccess` is not in the BYR repo** (`git ls-files`, 2026-09-30); it lives on the server only. |

## 2. What was done (2026-09-29 to 2026-09-30)

**Rulings, verbatim:**
- **The decisions sheet** (`handoff-025-decisions.xlsx`, column "Your ruling"; each letter reads against
  that row's options). Recorded against each item in §4, and in "Closed since handoff-025" below.
  - "A" on LG26, §5 tally, INFRA-11, INFRA-14a, INFRA-17, C-22, C-19, Display fallback, C-15a, C-15b,
    G-6, P-6, D-1, D-2, O-24a, O-24b, O-24d, O-21, O-17, O-14, O-15, and M3 + traps.
  - "B" on O-19. "B. I COULDN'T GET AROUND THE HEAD CHEF" on C-9 (read as sentence case).
  - "EXPLAIN BETTER" on INFRA-15, then in chat **"b, allow them"**, read as INFRA-15 B.
  - A LinkedIn image URL on INFRA-10, read as "run".
  - No ruling on D-3, INFRA-4, O-18, O-4, O-5 and O-2.
- "merge 23", "go straight to Phase 3 step 4", **"s4-1 A, s4-2 A"**, "merge 24", "write handoff-026".

**Shipped, each checked live (curl against `main` with a pre-merge control, then `site_check.py --live`):**
- **#23** (merge `421c009`): ledger column 025 (LG26), and the `cd` hook. It also landed #22, handoff-025.
  Live `/` byte-identical to `main`; `site_check.py --live` 169 of 169.
- **#24** (merge `55f8469`), **Phase 3 step 4:**
  - DESIGN-2: the home lede at 52ch, scoped by `.hero--home` (the 404 shares the hero and keeps 34ch).
  - DESIGN-1: the open sub-menu fits the screen in the header's phone layout.
  - G-7: the `--block` gap above the graph's frame.
  - DESIGN-3: text at 200% on a 375px screen no longer runs off.
  - DESIGN-4 (found this session): the same at 480 to 1024px. Every width breakpoint is now `em`.
  - `site_check.py`: the DESIGN-1 and DESIGN-3 marks off; 200% set the browser's way, at four widths.

**Done outside the repo, checked by the agent:**
- **INFRA-11:** Thomas added the redirect rule and turned on Always Use HTTPS; the `www` record was already
  there from his first try. Curl: all four of `http`/`https` × apex/`www` end at `https://tc-ventures.ca/…`
  with the path and query kept.
- **INFRA-15:** Thomas allowed the AI crawlers. Curl with each user agent: 200.
- **INFRA-10:** the image Thomas pasted from LinkedIn is the same 1200×630 card as `og-card.png`, compared
  side by side. The Post Inspector page itself wasn't seen.
- **C-15a:** the private résumé copy, the repo copy and the live PDF have the same md5, `0da7af62…`.
- **O-19 (B):** no "Technical Issue" or "critical error" email in Thomas's personal Gmail in the 14 days
  to 2026-09-30, in any folder including spam and trash. The GPRS site's WordPress admin email may be
  another inbox.
- **Handed to separate sessions** (Thomas started both, 2026-09-30): the theme items (C-9, O-24a, b, d,
  INFRA-17), done there as 1.0.762 and V0.46, and the research-repo item (O-15), whose result wasn't read
  here. The INFRA-17 harnesses
  were copied out of the Windows Temp scratchpad first, to `Claude outputs/infra-17-harnesses/`.

**How it was checked (the full record is in copy-review-007 and the PR bodies):**
- **The fault marks proved the fixes from outside:** with the DESIGN-1 and DESIGN-3 marks still on, both
  checks failed on all 12 pages with "passes now". Then the marks came off.
- **Every new check was run against trees that must fail it:**
  - `main` fails the 375px checks and the new 200% sweep on all 12 pages;
  - `962efe8`, step 4 without the `em` breakpoints, fails the sweep only at 480 and 760, on all 12 pages.
- **`shots_diff.py`:**
  - `main` against #24: `/projects`, `/background`, `/contact` and `/404` identical.
  - The home page and `/work/influence-graph` differ as intended.
  - Six receipt pages are 5 to 36px shorter (Q-S4-2 A, accepted).
  - `962efe8` against #24: 48 of 48 identical, so the `em` change is invisible at default text.
  - `--self`: 48 of 48. `--inject` (1px on the footer): 0 of 48.
- **Screenshots looked at before Thomas saw them:**
  - the home page at 1280×900;
  - the sub-menu at 375;
  - the graph's gap;
  - the footer and a receipt at 375 with text at 200%;
  - at 200% text: the home page at 480, the sub-menu at 1024, and `/method`'s table at 760.

**Found in the data:**
- **A `1fr` grid column never shrinks below its longest word.** One long URL in the footer widened the
  whole footer at 200% text. `minmax(0, 1fr)` fixed it everywhere it was used (§3).
- **Media queries don't see a `:root` font-size override,** but they do see the browser's own text-size
  setting. So the old 200% checks missed every layout that a breakpoint should have reflowed.
- **Lines that held an inline `nowrap` receipt were a few pixels taller than the rest.** As
  `inline-block` they aren't.
- **Two copies of the truth rules** (§4 INFRA-20).

**Own misses:**
- **Three short heredocs:** a JSON edit, a crop script and an empty `python -` that sat waiting on input
  until it was stopped (its work had already finished). The heredoc trap, again.
- **An awk filter read the wrong field** (`$3`, the word "scrollWidth", not the number), so the first width
  sweep reported nothing. It was caught by the empty result, and re-run.
- **The first 200% screenshots were at default size.** A full-page shot drops the CDP text size (new
  trap). They were caught by looking at them, and redone as viewport shots.
- **Two screenshot clips took viewport coordinates as page coordinates** and showed the page top. They
  were caught by looking at them, and redone.
- **The first draft of this handoff named Thomas's personal email address** (O-19). The privacy read
  before commit caught it; it never reached the repo.
- **The first DESIGN-1 fix sized the list to its 240px minimum,** the same miss as the first try in
  P3-0. It was caught by the probe; `width: max-content` fixed it.

**Found, not fixed:** nothing new beyond §4.

### Traps worth knowing

Each trap ends with its tally, **`x.y`** (§5).

**Dropped this handoff:**
- "To check a schema type is gone, count the old type's exact string": `6.0`.
- "`cf-ray` is on every response through Cloudflare": `6.1`.
- "The LiteSpeed Cache crawler's default interval is 302400 s": `6.0`.
- "Chromium in a claude.ai cloud session rejects the session proxy's certificate": `6.1`.
- "Headless Chrome defaults to dark mode": `10.8`. It's in code: `shots_diff.py` and `site_check.py` set the
  colour scheme per context.
- "Cloudflare's build start has ranged from about 1 to 10 minutes": `10.5`. Still earning its place, so it
  goes into code as INFRA-18.

**New this session:**
- **A Playwright full-page screenshot drops CDP `Page.setFontSizes`.** The root fell from 32px to 16px.
  Take viewport screenshots (scroll first) when the browser's text size is set, and read the root's font
  size at the shot. `0.0`

**Carried:**
- **Lazy, async-decoded images can paint as empty boxes in a Playwright full-page screenshot.** Before a
  shot, set `loading = 'eager'` and `decoding = 'sync'`, then await each `img.decode()`. `shots_diff.py`
  does this. `1.0`
- **Python on Thomas's console prints in cp1252, and a `→` or `’` crashes it.** Start a script with
  `sys.stdout.reconfigure(encoding="utf-8", errors="replace")`, or run with `PYTHONIOENCODING=utf-8`. This
  session's scripts did. `1.1`
- **`git rev-parse --short` takes one revision.** With two it fails with "Needed a single revision". `1.0`
- **PowerShell 5.1 splits an inline argument at its embedded double quotes.**
  - Write a message or PR body to a file (`git commit -F file`, `gh pr create --body-file`), and run
    `gh --jq` in the Bash tool.
  - This session every commit and PR body went through a file.

  `2.2`
- **In PowerShell, `;` runs the next command even when the one before it failed.** Run a gate on its own,
  read it, then act. This session each merge's gate ran as its own command first. `2.2`
- **Thomas's "merged" may not have landed.** Run `gh pr view N --json state` before you check live or build
  on it. This session each merge's state was read after the merge. `3.3`
- **Theme docs name surfaces loosely.** Read a spec's §0 before a caption says what it is the spec for.
  `3.0`
- **A 429 behind Cloudflare may not be about your IP.**
  - If Cloudflare proxies to a second CDN (`*.cdn.hstgr.net`), that CDN's per-IP limit counts Cloudflare's
    edge IPs, so a whole region is blocked together. It cost two days on thomascheesman.ca (O-23).
  - Read the headers: `x-hcdn-*` means Hostinger's CDN; `x-turbo-charged-by: LiteSpeed` + `panel: hpanel`
    means the origin.
  - Then check what the Cloudflare DNS record points at.

  `3.0`
- **Never load a Hostinger site in a headless browser from Thomas's machine.**
  - Hostinger's CDN counts HeadlessChrome as a bot, and a few dozen loads got his home IP an empty 429 for
    hours.
  - Test theme changes locally; ask Thomas to confirm live in his own browser; at most a couple of curls
    with a real browser UA.
  - `platform: hostinger` + `x-hcdn-request-id` means Hostinger's edge refused you.

  `4.2`
- **An offline rebuild of a live page can't judge a font-dependent width.** For a layout bug, the proof is
  the live page with the rule injected before load, against the same load without it. `4.0`
- **Astra's Customizer CSS beats the child theme's bare element rules.** Read the winning rule with
  DevTools' matched-rules list, not the source. `4.0`
- **Heredocs mangle scripts, and `python -` with nothing on stdin waits forever.** Write scripts with the
  Write tool. **Hit again this session despite the mention** (three short ones, §2), so no y. INFRA-19
  proposes a hook. `4.3`
- **A checker can read the wrong block or field, and a control can be unable to fail.**
  - Anchor on the heading. A control must change a word that is in the text.
  - **Hit again this session** (an awk field, §2), so no y.

  `5.4`
- **The Cloudflare bot says "Deployment successful" on branch pushes. Branch builds don't reach
  tc-ventures.ca.** Only a merge deploys. This session each live check waited on the merge commit's
  check-run. `5.3`
- **In a cloud session, `pip install playwright` installs a version whose default browser path doesn't
  exist.** Launch with `executable_path='/opt/pw-browsers/chromium'`. `5.0`
- **The cloud clone of the theme repo is shallow (50 commits).** Run `git fetch --unshallow` before
  reading history for receipts. `5.0`
- **`/projects` copy about thomascheesman.ca goes stale when the features change.** Re-trace a paragraph
  against the theme's code before a case study reuses it. `5.1`
- **A check warms the cache it is checking.** Use a cache-busting query. This session's live curls used
  `?cb=`. `6.6`
- **Most of this repo is CRLF in Thomas's Windows checkout, and so is most of the theme.**
  - Edit through `scripts/patch.py`, which matches on LF and writes each file back with its own endings.
    Every edit to an existing file this session went through it.
  - New files written by the Write tool are LF; Git warns and converts them.

  `8.7`
- **Run a local test server inside the Python process.** Used this session by every probe and checker.
  `9.8`
- **Wait about 400 ms after a click before a screenshot.** Used this session. `9.5`
- **`/404` answers 200.** Test "not found" with an unknown URL. `8.2`
- **A test that Tabs a fixed number of times can land on the wrong control.** Loop until the target has
  focus. `8.3`
- **A receipt's "caught" column can be a guess.** Open the receipt before copy says "I". `9.2`

## 3. Current design

**Pages live:**
- `/work/gprs` and `/work/this-site` (2026-09-24)
- `/method` and `/work/influence-graph` (2026-09-25)
- `/work/bare-your-rare` (2026-09-26)
- `/work/back-quarter` and `/work/desk-and-drawer` (2026-09-28)
- The Display panel on every page (2026-09-29)
- **The step 4 layout on every page** (2026-09-30)

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
- **Rules row 1's "I caught it by using them" is to be narrowed** to the two catches with receipts, through
  a copy block (C-22, ruled A).

**Nav:**
- **To ship a case study, run `python scripts/ship_case_study.py work/<slug> [work/<slug> …]`** (`--dry-run`
  first).
  - It reads the label and the position from the preview's own sub-menu.
  - It refuses, writing nothing, unless `PLANNED_SUBMENU`, the live sub-menu, every page and label = H1
    agree.
  - It edits all 13 files, `.assetsignore`, the sitemap and both checkers' `SUBMENU`.
  - It doesn't touch `/projects` or the home cards: that's copy.
- A preview carries the sub-menu it will ship with, with its own entry marked `aria-current="page"`. Set
  `PLANNED_SUBMENU` in `cs_check.py` first.
- Ship the page and its link in the same push, never a link that 404s.
- Run `scripts/site_check.py` before and after.
- **Any other edit to the nav or the header** is a 13-file edit. Do it with a `patch.py` script, never by
  hand.
- **In the header's phone layout (45em and under)** the open sub-menu is capped to the screen, with the
  same margin on each side, and a label may wrap (DESIGN-1).

**Layout at any text size (step 4, live 2026-09-30):**
- **Width breakpoints are in `em`, never `px`** (px ÷ 16: `640px` is `40em`). At the default text size they
  are the same width; with the browser's text size raised they move with the text, as they already do
  under page zoom. **A new breakpoint is written in `em`.**
- **A grid column that holds text is `minmax(0, 1fr)`, not `1fr`.** A `1fr` column never shrinks below
  its longest word.
- **`body` has `overflow-wrap: break-word`:** a word breaks only when it would otherwise run off its line.
- **Receipts are `inline-block`:** one moves to the next line whole, and one wider than the whole line
  wraps inside itself.
- **The stacked rules table (40em and under) is `table-layout: fixed`.**
- **To check text at 200%, set it the way the browser does** (CDP `Page.setFontSizes`, `standard: 32`), not
  with a `:root` override, which media queries don't see. Screenshot it with viewport shots only (§2
  trap).
- **The home lede is 52ch** (`.hero--home .hero__lede`). Other `.hero__lede`s keep 34ch; `.pagehead` ledes
  are 52ch.

**The Display panel (copy-review-007; live 2026-09-29):**
- **The button:** "Display", after the nav. In the header's phone layout (45em and under) it moves up to
  the name's line. It shows only when scripts run (`@media (scripting: enabled)`).
  - **If `display.js` fails to load while scripts run, the button shows and does nothing.** Accepted
    (ruled 2026-09-30): the Projects caret makes the same trade, and showing the button only after the
    script runs would shift the bar on every load.
- **The panel:** built by `display.js`. It's a disclosure like the sub-menu, and overlays the page.
  - Four radio rows:
    - Motion: System · Full · Reduced · Off
    - Theme: System · Light · Dark
    - Contrast: System · Standard · More
    - Text size: Standard · Large · Larger
  - The note under the rows: "Saved in this browser only." (DP1–DP3, ruled).
- **System means no mark on `<html>`:** the OS decides through plain CSS, which is also what happens with
  JavaScript off.
- **Motion:**
  - Anything that moves takes its time as `calc(<time> * var(--move))`, and any fade as
    `calc(<time> * var(--fade))`.
  - Reduced sets `--move: 0`. Off sets both to 0 and switches off every transition and animation.
  - Under System, the OS's "reduce motion" means Reduced (Q-P3-2 A).
  - **New motion must follow this.** `site_check.py` checks the times at every level, and it checks
    that nothing animates under Off.
  - Scripts ask `window.tcvMotion()` (`prefs.js`), as `graph-demo.js` does.
- **Theme:**
  - The dark colours are written once, as `--dark-*`.
  - Two routes reach them: the OS's dark mode unless `data-theme="light"`, or `data-theme="dark"`.
  - `color-scheme` follows the theme.
  - **A new colour token gets a dark value in the same pattern,** and `site_check.py` checks that the two
    routes give the same colours.
- **Contrast More:**
  - The `-more` colours: muted, the accent and the rules, each mixed toward the ink until text passes
    7:1 and rules pass 3:1 on both grounds. Also 3px focus rings (`--focus-w`).
  - Standard is today's palette, and every text pair passes 4.5:1.
  - Both are checked.
- **Type:** every HTML text size is in rem, so the reader's browser text size works. **SVG labels stay in
  px:** they're in the picture's own units. Text size Large is 112.5% and Larger is 125%, on the root
  (so they don't move `em` breakpoints; the browser's own setting does).

**Look and feel:**
- Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode by the OS or the Display panel.
- Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
- Confirmed; stop re-litigating it. **Phase 3 is the design pass now** (copy-review-007), in the ruled
  steps.

**Case-study layout (approved 2026-09-22):**
- Two lanes: a wide lane (1040px) for headers, figures, tables and lists, and a reading lane (66ch) for
  prose.
- A sticky 200px rail at 73.75em (1180px) and wider with the section index. Below that it folds to a
  horizontal index.
- Sections are numbered by CSS counters, and figures `Fig. N` per page.
- Receipts are small mono links with a leading `→`.

**Home page (live 2026-09-22; lede width 2026-09-30):**
- **Label:** "Thomas Cheesman · Grande Prairie, Alberta · remote".
- **H1:** "I run a nonprofit's website, and I hold it to a written standard."
- **Lede:** from R3/R4, 52ch wide (6 lines at 1280; the ledger's top shows on a 1280×900 screen). **R5
  under it is one sentence**: "I am looking for remote work running a nonprofit's website and digital
  operations." (LGR, 2026-09-29).
- Every project card links its case study: the graph, the Back Quarter and the Desk (P3). The "Four live
  sites" card links BYR, GPRS and this site. The "How I work" heading links `/method`.

**The build ledger (live 2026-09-29; copy-review-006):**
- **Order in the hero:** label, H1, lede, R5, the buttons, then the ledger.
- **The block is generated.** To change it:
  1. Edit `ledger/curation.json` or the handoffs.
  2. Run `python scripts/export-ledger.py`, then `--check`, then `site_check.py`.
  3. Ship.
- **A handoff's column appears only once its line is ruled** (`ruled` in the curation). At wrap:
  1. Draft the new handoff's line in copy-review-006 (LG27 for 026, LG28 for 027, and so on).
  2. Add it to the curation with `"ruled": null`.
  3. Run `python scripts/quote_check.py --ledger` on its "Rests on" quotes.
  4. After Thomas rules, set `ruled`, export and ship.
- **A line:**
  - never copies handoff prose;
  - says "I" only for what Thomas did;
  - leaves out the private project, other sites' incidents and anything familial.
- **Items are drawn solid unless the curation's `parked` lists them** (dotted means parked on purpose, or
  waiting on Thomas). When a handoff opens or parks an item in scope, update `parked`. `--report` doesn't
  flag an unclassified new item: it just draws it solid.
  - **A `parked` change redraws past columns,** so `site_check.py --live` fails until it ships. Make it in
    the same PR as the column it belongs to.
- **What's never drawn:** O-\* and L-\* items, and rows under OTHER REPOS or LANDER.
- **A new §4 workstream heading stops the export** until the curation's `bands`, `fold` or `exclude` says
  where it goes.
- **An ID whose wording changes is a DOUBT in `--report`** until `reviewed_ids` or `split` records it. G-7
  is two items, split by its gap.
- **`site_check.py --live` fails whenever the live block isn't what the script writes now,** including
  after a curation change that hasn't shipped. That's intended.
- **Phase 3 layers (PL-9, ruled Q-P3-6 A):** the scrubber and the draw-in in step 5; traps later.

**Standing rules:**
- **The Rocket Lander is private.** Not here, in any form.
- `object-fit: contain`, never `cover`.
- **Content renders without JavaScript.** JS is allowed on top (motion, 3D, controls); the words and links
  must not depend on it. No dependencies or build step — prebuilt bundles copied into `assets/` only.
- **No inline script** (the CSP). Code that must run before the first paint goes in a small file in
  `/assets/`, as `prefs.js` does.
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
- **Accessibility controls are built in, never an overlay widget** (PL-6). They're live now: the Display
  panel.
- **Never link `reviews/copy-review-001.md` from a page** (T0, 2026-09-24).
- **Never run git in `Reports Clustering`** from this project's sessions. Read its files; change nothing
  there unless Thomas asks.
- **The outside research model is never named in copy** (F-2), and no link's path may carry its name.
  The research repo's 52 paths that carry it stay as they are (O-14, ruled A).
- **Don't link the `@bareyourrare` social accounts anywhere until Thomas says they are claimed** (O-18).
- **Never link a theme-repo file or commit.** The repo is private, and its handoffs and commit diffs carry
  family material. Read it for facts only. The case studies link receipts-001 §3F (Q-BQD1 A).
- **Never load a Hostinger site in a headless browser from Thomas's machine** (§2 trap).
- **A change meant to be invisible is proved with `shots_diff.py`**, with its `--self` and `--inject`
  controls.

**Demo and embed rules:**
- Nothing heavy loads before a click.
- A gated page degrades when the payload is absent.
- The 3D canvas keeps its own dark ground, in both themes.
- `basis` is quoted, never paraphrased.
- The written chain under the graph is the accessible equivalent.
- Nothing rearranges a layout on interaction; the sub-menu and the Display panel overlay and move nothing.
- **Show finished work:** unfinished work is labelled honestly or left off.

## 4. Open items — carry these forward until closed

### PLAN
| # | Item | Notes |
|---|---|---|
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Order: Phase 1 ✓ (2026-09-25) → Phase 1b ✓ (2026-09-28) → Phase 2 ✓ (2026-09-29) → **Phase 3, in progress (copy-review-007): step 2 ✓ (#20), step 3 ✓ (#21, the Display panel), step 4 ✓ live (#24, the layout, 2026-09-30) → step 5, the motion (M1, M2 and the scrubber)** → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). **M3 (the method loop) and the ledger's traps layer: ruled "A: decide after step 5 ships"** (2026-09-30). |
| PL-8 | **Page-weight / a11y numbers: ruled ship without (2026-09-24)** | `/work/this-site` says none are shown because nothing measures them by script yet. When the Phase 4 budget script exists, the numbers go into that page's honest limits (plan-001 §6 Q5), through a copy review. |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers. |
| PL-9 | **The ledger's later layers (Phase 3)** | **Ruled Q-P3-6 A (2026-09-29):** in step 5, a native slider under the picture reads one handoff's line at a time, and the threads draw in on first view (M2). **Traps later, in their own review** (separable per session only from handoff-019 on). The words never depend on any of them. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-22 | **`/method` rules row 1 says "I caught it by using them"** (the three sliders) | **Ruled A (2026-09-30): narrow it to the two catches with receipts** (handoffs 006/007 and 032), through a copy block. Nothing found on how the first (`geoAffinity`) was caught. Not drafted yet. |
| C-20 | **`/work/this-site` states two things that will go stale** | "rebuild in progress" (header) and "has not had a screen-reader run-through yet" (honest limits). Update both when the rebuild ends and when A-1 is done. |
| C-15 | Résumé: **the summary ends on a one-word line ("roles.")** | **Ruled A (2026-09-30): fix it at the next résumé edit,** in the Word file and its HTML mirror; Thomas exports; exactly two pages. The private copy matches the served PDF (md5 `0da7af62…`, 2026-09-30). |
| C-16 | **Job history, from Thomas 2026-09-23. Use these** | GPRS board: elected at the **June 2023** AGM (first meeting September). Majors consulting: May 2019 – **June 2020**. **Head Chef, Ric's Grill, Sep 2013 – Jul 2014.** **Executive Chef, Township 71, Jul 2014 – Jun 2015** (renovation from Oct 2014, opened Nov 2014, closed May 2015, wind-down through June). **Taught one GPRC semester, Sep – Dec 2014.** |
| C-13 | GPRS site history | WordPress.com 2023; self-hosted WordPress.org on Hostinger 2025 "because I wanted more freedom to experiment with the code." Used in `/work/gprs`. No month-level dates without asking. |
| C-17 | R4 wording, his call | Live: "…then build it with help writing by AI." **Do not raise it again or change it unasked.** |
| C-21 | **`/method` H1, lede and title: his call (2026-09-25)** | Same standing as C-17. The H1 stands alone (Q-M5). |
| C-9 | `page-thomas.php` ~2010: "I couldn't get past my kitchen manager" | **Ruled B, his words (2026-09-30): "I COULDN'T GET AROUND THE HEAD CHEF"**, read as sentence case. Done by the theme session in 1.0.762 ("get around the head chef", before/after OK'd by Thomas, per its diary row). Live state not checked from here; the theme's V0.46 owns it. |

### DESIGN
| # | Item | Notes |
|---|---|---|
| — | No open design items | DESIGN-1 to 4 and G-7 closed in step 4 (below). |

### PROJECTS / GRAPH
| # | Item | Notes |
|---|---|---|
| — | No open items | P-6 and G-6 closed (below). |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add `/work/gprs`, `/work/this-site`, `/method`, `/work/influence-graph`, `/work/bare-your-rare`, `/work/back-quarter`, `/work/desk-and-drawer` and the Projects sub-menu to that run. Left from 012: one real screen-reader run through the live graph, now on `/work/influence-graph`. **Two points for it:** the loop diagrams' links sit inside an SVG with `role="img"`, which may hide them from screen readers (the same links are in `/method`'s "originals" list); and the diagrams' connectors and arrows in `--rule` are faint on white (non-text contrast). **Also the home ledger:** two `role="img"` SVGs with a `<desc>` each, and its `<details>` list. **Also the Display panel** (2026-09-29): its radio rows with a screen reader, and the panel in real Windows high contrast (only Chromium's emulation was seen). **Reflow at 200% text is now checked by script** (step 4); a real browser at 200% is still worth one look. |
| A-3 | **Sub-menu without JS cannot be dismissed with Esc** | Without JS the list shows on hover or focus (WCAG 1.4.13 asks for a dismiss key). With JS, Esc works. Accepted as the no-JS fallback; for A-1 to confirm. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-18 | **A script that waits for the merge commit's deploy** | The trap "Cloudflare's build start has ranged from about 1 to 10 minutes" reached `x = 10` still earning its place (§5: it belongs in code). This session's waits were an ad hoc loop on the check-runs API. A `scripts/` tool that polls the merge commit's "Workers Builds" check-run, then curls the named paths against `main` with a pre-merge control, would replace both. Not built. |
| INFRA-19 | **A hook that refuses a heredoc in a Bash command?** | The heredoc trap was hit three times this session despite its mention (`4.3`), the same pattern that led to the `cd` hook. A hook changes his harness settings, so it's **his call; not built.** |
| INFRA-20 | **The truth rules are in two places** | Thomas's global `CLAUDE.md` says it's "the only copy", moved there 2026-09-29 from the per-project files; this repo's `CLAUDE.md` still holds all twenty (read 2026-09-30). One copy of each fact (rule 17). Which to keep is **his call**; nothing was changed. |
| INFRA-17 | **Theme-side test harnesses** | **Ruled A (2026-09-30): the offline ones go in the theme repo's `tools/`; leave out the one that loads the live site.** Copies saved at `Claude outputs/infra-17-harnesses/` (untracked): `bq_test.py`, `bq_test2.py`, `wash_test.py`, and `drawer_inject.py`, which loads the live site and stays out. The "offline rebuild with matched rules" harness was not among the saved files. **Done by the theme session:** commit `51d2cbc` "tools/: the offline Back Quarter and wash harnesses (INFRA-17)" on the theme's `main`. The saved copies in `Claude outputs/infra-17-harnesses/` can go once Thomas is happy with that. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address. No ruling 2026-09-30. |
| INFRA-6 | Dead lander CSS in `style.css` (search `lander embed`) | Delete if still unused by mid-October 2026. |
| INFRA-9 | HSTS 1 yr, no `includeSubDomains`, no `preload` | Deliberate; both are hard to undo. Always Use HTTPS is on since 2026-09-30, so first visits over `http` are redirected too. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. **He will renew on 2026-10-07** (said 2026-09-27). **Not confirmed paid** as of 2026-09-30. |
| D-1 | WordPress.com still claims the domain | **Ruled A (2026-09-30): detach when convenient.** Thomas's to do. Harmless meanwhile. |
| D-2 | WP.com plan auto-renew | **Ruled A (2026-09-30): leave for now; revisit before 2027-08-22.** Do not cancel without confirming DNS for the live sites is unaffected. |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-25 | **The home page slides sideways on phones (only the home page)** | 1.0.758 is deployed (1.0.759 too); the drawer fix holds on other pages. The home-only slide isn't found yet; the lead is content that scripts draw. Owned by the theme's newest `V0.*.md` Open (V0.45). |
| O-24 | **thomascheesman.ca phone header, and the no-JS lede** | **Ruled 2026-09-30:** (a) the fixed header capsule covers the start of the "THOMAS CHEESMAN" name line on phones: **A, fix**. (b) Without JS, `.bq-lede__name` and `.bq-lede__deck` stay at opacity 0 (`.kinetic-fade`): **A, fix**. (d) The phone line says "On a phone" but tablets see it too: **A, reword to cover tablets**, his words. (c) The "wonky" menu: he'll screenshot it if he sees it again. (a), (b) and (d) were done by the theme session in 1.0.762 (per its commit log and diary row; the V0.46 file, the code and the live site weren't read here). The theme's V0.46 owns them now. |
| O-21 | **Theme repo: family material in its files, history and commit diffs** | **Ruled A (2026-09-30): leave it while private; clean it before it could ever go public.** Private since 2026-09-26. The details went to him in the chat on 2026-09-26, not here, because this repo is public. |
| O-17 | **BYR `.htaccess`: Thomas's `E=verifycaptcha:off` block had no effect** | **Ruled A (2026-09-30): remove it if it's there.** `.htaccess` isn't in the BYR repo, so Thomas checks the live file in hPanel's File Manager. |
| O-19 | **GPRS: WordPress "critical error" on uncached pages, 2026-09-26** | Re-tested 2026-09-27: 200 cached and uncached. **Ruled B (2026-09-30): search for the "Technical Issue" email.** Not in Thomas's personal Gmail (§2). Which inbox is GPRS's WordPress admin email is Thomas's to say. GPRS's own handoff owns any fix (O-12). |
| O-15 | **Research repo: "read the sentence as well as fetching it" is not in its current playbooks** | **Ruled A (2026-09-30): a research session adds it.** It was in `archive/NZ/G.3.md` L539. Handed to a separate session 2026-09-30; not confirmed. |
| O-20 | **The Back Quarter: 3D on PCs only — SHIPPED 2026-09-27 (1.0.755)** | Plan and rulings: theme `docs/BQ-3D-ONLY-PLAN.md`. **3D on phones is a later job** (Thomas: "we will bring it to the mobile"). When it ships, `/work/back-quarter`'s "Where it runs" row, its honest limit and `/projects`' "A phone gets a still" line change with it. `back-quarter-3d.js`'s header comment "MOBILE PLAY … phones are IN" is stale. |
| O-22 | **Hostinger deploy webhook URL was in a public theme file for about seven weeks** | Anyone with the URL can trigger a redeploy of `main`, no more. **Checked by Thomas 2026-09-28: hPanel has no regenerate option.** **Rotate it the next time the deployment is rebuilt,** by switching to Hostinger's GitHub App method, which manages the webhook itself. Then delete the old SSH entry in hPanel and the old webhook in GitHub. |
| O-16 | **AI crawlers on the Hostinger sites: ruled leave it ("1", 2026-09-26); re-checked on thomascheesman.ca 2026-09-28** | After the O-23 DNS fix, from Thomas's IP with each crawler's name: **ClaudeBot, Claude-User, PerplexityBot, OAI-SearchBot and ChatGPT-User get 200.** **GPTBot gets an instant, empty 429 from the origin** (`x-turbo-charged-by: LiteSpeed`, `panel: hpanel`): a name rule on Hostinger's server, not the CDN. **BYR and GPRS were not re-checked.** Leave the Hostinger "Create LLMs.txt file" toggle **off**. Evidence for BYR: `Claude outputs/byr-bot-check-2026-09-25.md`. `/work/bare-your-rare`'s honest limit depends on this. (tc-ventures.ca's own crawler setting is INFRA-15, now allowed.) |
| O-18 | **`@bareyourrare` social accounts are unclaimed** | Links removed (`ed6b054`). Restore from that commit's parent once Thomas says the accounts are claimed. No answer 2026-09-30. |
| O-2 | `/projects` third-person leakage on thomascheesman.ca | Thomas is writing this himself. |
| O-4 | bareyourrare history contains `permits/` and `3.jpg` | Instructions in `_Quarantine\bareyourrare-history-purge.md`. Thomas runs it. |
| O-5 | `bareyr\.git` lock-file junk | Cosmetic; Thomas deletes. |
| O-6 | Rocket Lander repo not public | On hold with the lander. |
| O-7 | Children's names in the Back Quarter world | **Thomas ruled: leave them.** They stay off this site regardless. |
| O-8 | thomascheesman.ca's open items live in its newest `V0.*.md` (**V0.46**) | Theme at 1.0.762 on `main` (2026-09-30). `three-r128.min.js` idle-loads for every visitor: ruled keep on phones (2026-09-27), now 1x/~20 fps there. |
| O-10 | bareyourrare.org and thomascheesman.ca behind Cloudflare since 2026-09-20 | thomascheesman.ca has three cache layers. Full detail in handoff-014 §4. BYR's domain is on Cloudflare DNS: **don't click "Connect domain"** in hPanel. |
| O-11 | bareyourrare.org crawl audit, mostly deployed | `Claude outputs/byr-crawl-audit.md`. Still open: (g) page weight. |
| O-12 | GPRS work has its own handoff | `GPRS Organization/00 Working Notes/gprs-handoff-001.md`. |

**Closed since handoff-025:**
- **DESIGN-2, the ledger below the fold:** the home lede at 52ch (Q-P3-4 A). Live in #24.
- **DESIGN-1, the open sub-menu at 375px:** fits the screen. Its check's mark came off. Live in #24.
- **DESIGN-3, text at 200% on a 375px screen:** nothing runs off. Its check's mark came off. Live in #24.
- **DESIGN-4, text at 200% between 375 and 1280px** (found and closed this session, Q-S4-1 A): `em`
  breakpoints, and a check at 375, 480, 760 and 1280. Live in #24.
- **G-7, the graph's paragraph against its frame:** the `--block` gap. Live in #24.
- **INFRA-14, two traps the mention didn't prevent:** (a) the `cd` hook, ruled A for this repo only, live
  in `.claude/settings.json` (#23); (b) was done before.
- **INFRA-11, `www.tc-ventures.ca`:** ruled A; 301 to the apex, and Always Use HTTPS on (§1).
- **INFRA-15, AI crawlers on tc-ventures.ca:** ruled B, allow them; GPTBot and ClaudeBot get 200 (§1).
- **INFRA-10, LinkedIn Post Inspector:** run by Thomas; LinkedIn's image matches `og-card.png`.
- **C-19, when "read the actual code" entered the audit prompt:** ruled A, closed as unknown. The live
  page makes no causal claim, and none is to be reintroduced.
- **The Display button's fallback** (handoff-025 §2 "Found, not fixed"): ruled A, accepted (§3).
- **G-6, the graph demo's still:** ruled A, keep the headless render.
- **P-6, a fourth project:** ruled A, closed; reopen when a project is finished.
- **O-14, the research repo's 52 paths carrying the outside model's name:** ruled A, leave them.

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

## 6. Next up — LG27, then Phase 3 step 5

Before anything: remind Thomas once of **D-3**, if it's still open. He said he'll renew on 2026-10-07, and
it's due 2026-10-08. Each step ends with his ruling before the next starts.

1. **LG27, this handoff's ledger line,** drafted in copy-review-006. When he rules it:
   1. Set `ruled` for 026 in `ledger/curation.json`.
   2. **In the same change, update `parked`** for this handoff's items: C-22, C-15, INFRA-17 and INFRA-18
      are work now, not parked; INFRA-19 and INFRA-20 are his call (parked).
      - `export-ledger.py --report --draft` (2026-09-30) raises 7 DOUBTs, "marked parked in curation but
        not open at the last column": C-19, P-6, G-6, INFRA-10, INFRA-11, INFRA-14, INFRA-15, all closed
        in this handoff. Before removing their `parked` entries, check how the exporter draws a closed
        thread's past (dotted or solid) with `--draft --html`, and keep their history as it was drawn.
   3. Run `python scripts/export-ledger.py`, then `--check`, `--report` and `site_check.py`.
   4. Open a PR, and merge on his word.
   5. Curl `/` against `main`, and run `site_check.py --live`.
2. **Phase 3 step 5, the motion** (copy-review-007 §4, §5 and §7):
   - M1: page to page, where the sub-menu label grows into the H1, by cross-document view transitions.
     Check which browsers support it at build, not from memory.
   - M2: the ledger draws itself in.
   - The scrubber (PL-9). Its label is a copy block in copy-review-007.
   - All of it through `--move` and `--fade`, with Reduced and Off states, and the checks extended.
   - Build, show him screenshots (viewport shots if the text size is set), and ship on his word.
3. **C-22's copy block** can go with step 5's copy review or on its own: his choice when it's drafted.

### After that

M3 and the ledger's traps layer, decided after step 5 ships. Then Phase 4: headers, schema, OG per page,
and the budget script. PL-8's numbers go into `/work/this-site` once the budget script exists, through a
copy review.
