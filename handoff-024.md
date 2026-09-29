# handoff-024 — tc-ventures.ca

**Written:** 2026-09-29
**Covers:** Phase 2, the build ledger, from proposal to live:
- **LG0, the proposal, ruled "LG0 ok, all A".**
- **Built:** `scripts/export-ledger.py`, `ledger/curation.json`, and five ledger checks in `site_check.py`.
- **LG1–LG24, LGR and LGP ruled**, and shipped as PR #15.
- **Also recorded here:** a theme session after handoff-023 (theme `V0.45.md`) that closed O-27 and O-9 and
  shipped the HCS alt text and a Notch diagram. Thomas: "hcs looks fine" (2026-09-29).
- **Phase 2 is done.**

**Status at wrap:**
- **Live on tc-ventures.ca, verified 2026-09-29:** `main` at `de37b8f` (PR #15). Merged by the agent at
  Thomas's word, "merge 15".
  - The check-run "Workers Builds: tc-ventures-site" on `de37b8f` completed with success at 14:26:21 UTC.
  - Curl, cache-busted: `/` and `/assets/style.css` are byte-identical to `main`. Control: `/` differs from
    the pre-merge `index.html`.
  - `site_check.py --live` passed 105 of 105, including "served block matches export-ledger.py now".
- **thomascheesman.ca:** nothing changed this session. The theme is at 1.0.761 (V0.45).
- **Not live, on a branch:** this handoff, and LG25 (this handoff's ledger line, drafted for Thomas to rule).

**The next job is §6.**

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. Read §2 "Traps" before you touch git, a checker script, a screenshot, the theme
   repo, a Hostinger site, or the `Reports Clustering` folder. **Especially: do not load thomascheesman.ca
   in a headless browser from Thomas's machine.**
2. `CLAUDE.md` at repo root: the twenty truth rules. `plans/operating-guide.md` is how Thomas and the AI
   divide the work, and §4 there is the checking routine.
3. **`plans/plan-001-showcase.md`**: the plan.
   - **The §5 note (2026-09-25)** holds the order.
   - **§4c** is the build ledger, live since 2026-09-29. **Phase 3 (craft) is next** (PL-6).
4. **`plans/receipts-001.md`**: the ruled inventory, 49 OK / 81 CUT. Only OK rows go in copy. Tick `chk`
   before quoting a row.
5. **`reviews/copy-review-006.md`**: the build ledger's rulings.
   - Everything is shipped except **LG25**, this handoff's ledger line, which is for Thomas to rule.
   - Later handoffs' ledger lines go here too (LG26 and on).
   - Phase 3 copy opens `copy-review-007`.
6. The shipped pages under `public/`. **`work/back-quarter.html` and `work/desk-and-drawer.html` are the
   newest instances of the case-study pattern.** The home hero now ends with the build ledger (§3).
7. **`scripts/`**: `site_check.py`, `cs_check.py`, `byr_bot_check.py` and **`export-ledger.py`**, plus
   **`ledger/curation.json`**. Each script's docstring is its manual.
8. **If the job touches thomascheesman.ca:** the theme repo's `CLAUDE.md` and its newest `V0.*.md`
   (**V0.45**), and `docs/IMAGE-BURST-PLAN.md`.
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
- **His merges don't always land** (§2 trap).
  - On 2026-09-29 he said "merge 15", and the agent merged #15.
  - That was per-PR permission, not a standing one.

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
| Deploy | **A merge to `main` deploys** → Cloudflare builds. **No cache to purge.** Branch pushes build too, and the bot calls them "Deployment successful", but they don't reach the site (trap below). #15 (2026-09-29) finished building 37 seconds after the merge, and was live at the first curl. |
| Contact email | `thomas@tc-ventures.ca` |
| Pages | `index`, `projects`, `method`, `background`, `contact`, `404`, `work/influence-graph`, `work/back-quarter`, `work/desk-and-drawer`, `work/bare-your-rare`, `work/gprs`, `work/this-site`. Internal links, canonicals and sitemap use **clean URLs** (`/method`); `/x.html` 307s to `/x`. No case study is planned. |
| Nav | **Projects (with a sub-menu of the case studies) · Method · Background · Contact**, on every page: **13 files** including `_template.html`. The sub-menu order is the `/projects` order: **The Economic Report Influence Graph · A homepage you drive around · A menu that is a photograph of my desk · A rare-disease site, written by a patient · A housing society's website · This site**. The markup is copied into each page; `assets/nav.js` makes the sub-menu a disclosure button. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html` and `og-src/` off the live site. A preview goes in it until it ships. |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. Unchanged since handoff-017. |
| AI crawlers | Cloudflare answers GPTBot and ClaudeBot 403 on tc-ventures.ca; Claude-User and ChatGPT-User get 200 (checked 2026-09-26). INFRA-15. |
| Link preview | `assets/img/og-card.png` 1200×630 on all pages. Source `public/og-src/og.html`. |
| Analytics | Cloudflare Web Analytics, injected at the edge. The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` · receipts `plans/receipts-001.md` · `plans/operating-guide.md` |
| Design system | `public/assets/style.css` — tokens in `:root`, case-study components under the `CASE STUDIES` banner, then the `build ledger` block at the end |
| Build ledger | The end of the home hero. Written into `public/index.html` between `<!-- ledger:begin … -->` and `<!-- ledger:end -->` by `scripts/export-ledger.py`, from the handoffs plus `ledger/curation.json` (not deployed). **Never hand-edit the block.** No JS: a landscape SVG, a portrait SVG shown at 600px and under, and a `<details>` list with one ruled line per handoff. Rules: §3. |
| Graph demo | On `/work/influence-graph` only. `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js`. |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. |
| Browser tests | Python Playwright + Chromium, scripts in `scripts/`:<br>- `site_check.py [--live] [--root DIR] [--draft-ledger]`: every sitemap page plus /404, then the home
  ledger. 105 checks now.<br>- `cs_check.py work/<page> [--preview] [--shots DIR]`: one case study. **`--preview` checks `PLANNED_SUBMENU`**, the menu a preview will ship with. It equals `SUBMENU` now; change it first for the next case study.<br>- Both serve `public/` in-process with clean URLs.<br>- **In a claude.ai cloud session:** `pip install playwright` first. The scripts launch the preinstalled Chromium by path (trap below).<br>- **`--live` is for tc-ventures.ca (Cloudflare) only. Never point a headless browser at a Hostinger site** (trap). |
| Research repo | `C:\Users\thoma\Desktop\My Files\Reports Clustering` = public `DriftingSplash9/Reports-Clustering`. **Never run git there.** Read its files, and read it on GitHub. |
| Sister repos | **Theme:** local `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` (not `Desktop\tc-ventures-child-theme`, which the global CLAUDE.md names) = GitHub `DriftingSplash9/thomascheesman-ca-theme`, **private since 2026-09-26**. A push to its `main` deploys to Hostinger; GitHub answers the push with "This repository moved" (the local remote uses the old name) and the push still lands. Cached pages then need a LiteSpeed purge and a Hostinger CDN purge (Thomas). Commit/push there is pre-authorized; bump `style.css` `Version:` on every theme-code commit. **BYR:** `bareyr` = GitHub `DriftingSplash9/bareyourrare`, **private**. A push to its `main` deploys to Hostinger, and cached pages then need a LiteSpeed purge (Thomas, in WordPress). |

## 2. What was done (2026-09-29)

**Before this session (no tc-ventures handoff was written for either):**
- **PR #14** pointed handoff-023 at theme V0.44: O-23 closed (stacked CDNs), O-16 re-checked, O-27 opened.
- **A theme session** (theme `V0.45.md`, 1.0.759 → 1.0.761):
  - O-27 and O-9 closed (§4).
  - F3's premise was wrong.
  - The HCS alt text was ruled and went live (1.0.760), and a Notch diagram followed (1.0.761).
  - V0.45 was read for these facts only, not in full.

**This session. Rulings, all verbatim in copy-review-006:**
- **LG0: "LG0 ok, all A".**
  - Q-LG1: parked items are drawn dotted.
  - Q-LG2: each list line links its handoff, 007 and 008 included.
  - Q-LG3: R5's first sentence is cut.
  - Q-LG4: a portrait version for phones.
  - Q-LG5: 004 is shown as 2026-09-16.
- **Step 2: "LG1–LG24 ok, LGR ok, LGP ok, INFRA-10 dotted".**
- **On the theme:** "hcs looks fine".

**What the ledger is:**
- One column per handoff.
- One thread per in-scope open item, from the handoff that opened it to the one that closed it, in bands by
  workstream.
- At 023, `--report` counts 7 solid, 24 dotted and 39 closed.
- Other sites' items, the private project and traps are left out (LG0).

**Found in the data:**
- **G-7 is two items** (005, and 019 on). The gap between them splits it.
- **C-15, G-2, INFRA-5 and PL-7** are each one item whose wording changed. Checked by reading every row.
- **handoff-004's `Written:` date is a day ahead.** handoff-005 says so, and git agrees.
- **013–015 have no "Closed" list.**
- **At wrap, no in-scope row says CLOSED or KILLED.** The export ends a thread at any row that does.

**Shipped:** #15 (`1e42f70`, merge `de37b8f`), merged by the agent at Thomas's word. Verified live (see the
header).

**How it was checked:**
- **The preview** (a scratchpad copy of `public/` with the ship's edits): `site_check.py` passed 105 of 105.
  The same run on the pre-ship `public/` failed exactly the 5 ledger checks (control).
- **Eleven one-fault controls.** Each was caught by the check meant for it, and nothing else failed
  (copy-review-006, step 2).
- **The "rests on" quotes:** 51 fragments, all verbatim in their handoffs, with a control. The check caught
  one quote that joined two bullets. Fixed.
- **Screenshots looked at:**
  - light and dark at 1280;
  - both at 375;
  - the list opened;
  - the real `public/` again, before commit.
- **Privacy read of every text node in the block:** no item IDs. It links only `/method`, `/work/this-site` and
  the 23 handoffs.
- **Weight:** home goes from 3.7 to 10.0 KB gzipped (11.6 to 50.5 KB raw).

**Tooling:**
- **In the repo:** `export-ledger.py`, `ledger/curation.json`, and the ledger checks in `site_check.py`.
- **Scratchpad only:**
  - `patch.py` (INFRA-13);
  - `quote_check.py` (INFRA-16);
  - `controls.py`, `shots.py`, `build_preview.py`.

**Own misses:**
- **A commit message passed inline in PowerShell was split into pathspecs.** Nothing was committed, and the
  push that followed created the branch at `main`'s commit. Redone from a file.
- **A pre-merge `gh pr view` broke on PowerShell quoting, and the `gh pr merge` on the same line ran anyway.**
  Thomas had ruled it ("merge 15"). The state was read afterwards: merged.
- **A Bash command started with `cd`** (INFRA-14a), for the push of this handoff. It did no harm.
- **The proposal's first draft had three claims wrong against the survey output:**
  - which heights were compared;
  - how many handoffs share a date;
  - a paraphrase in quote marks.

  All three were caught by a re-read before it was sent.

**Found, not fixed:** DESIGN-2, the ledger below the fold at 1280×900.

### Traps worth knowing

Each trap ends with its tally, **`x.y`** (§5).

**Dropped this handoff:**
- "Analytics can't be seen headless": `6.1`.
- "A figure Thomas gives can have no source on disk": `6.0`.
- "There's no LibreOffice, pandoc or `pdftoppm` on Thomas's machine": `6.0`.

**New this session:**
- **PowerShell 5.1 splits an inline argument at its embedded double quotes.**
  - A commit message in a here-string became dozens of pathspecs, and `gh … --jq '…'` expressions broke.
  - Write a message or PR body to a file (`git commit -F file`, `gh pr create --body-file`), and run
    `gh --jq` in the Bash tool.

  `0.0`
- **In PowerShell, `;` runs the next command even when the one before it failed.** A failed pre-merge check
  didn't stop `gh pr merge`. Run a gate on its own, read it, then act. `0.0`

**Carried:**
- **Thomas's "merged" may not have landed.** Twice, #9 and then #10, he said "merged" while GitHub showed
  the PR open, clean and mergeable. Run `gh pr view N --json state` before you check live or build on it.
  This session the merge's state was read before the live check. `1.1`
- **Theme docs name surfaces loosely.** "The drawer" in `SECRET-DRAWER-VISION.md` is the escape room, not
  the footer's pinball drawer, and the doc's own §0 says so. Read a spec's §0 before a caption says what
  it is the spec for. `1.0`
- **A 429 behind Cloudflare may not be about your IP.**
  - If Cloudflare proxies to a second CDN (`*.cdn.hstgr.net`), that CDN's per-IP limit counts Cloudflare's
    edge IPs, so a whole region is blocked together. It cost two days on thomascheesman.ca (O-23).
  - Read the headers: `x-hcdn-*` means Hostinger's CDN; `x-turbo-charged-by: LiteSpeed` + `panel: hpanel`
    means the origin.
  - Then check what the Cloudflare DNS record points at.

  `1.0`
- **Never load a Hostinger site in a headless browser from Thomas's machine.**
  - Hostinger's CDN counts HeadlessChrome as a bot, and a few dozen loads got his home IP an empty 429 for
    hours.
  - Test theme changes locally; ask Thomas to confirm live in his own browser; at most a couple of curls
    with a real browser UA.
  - `platform: hostinger` + `x-hcdn-request-id` means Hostinger's edge refused you.
  - This session O-9 was settled from git and V0.45, with no request to the site.

  `2.2`
- **An offline rebuild of a live page can't judge a font-dependent width.** For a layout bug, the proof is
  the live page with the rule injected before load, against the same load without it. `2.0`
- **Astra's Customizer CSS beats the child theme's bare element rules.** Read the winning rule with
  DevTools' matched-rules list, not the source. `2.0`
- **Heredocs mangle scripts.** Write scripts with the Write tool. This session every script in the repo and
  the scratchpad was written that way. `2.2`
- **A checker can read the wrong block, and a control can be unable to fail.**
  - Anchor on the heading.
  - A control must change a word that is in the text.
  - This session every ledger check had a one-fault control.

  `3.3`
- **The Cloudflare bot says "Deployment successful" on branch pushes. Branch builds don't reach
  tc-ventures.ca.** Only a merge deploys. This session the live check waited on the merge commit's
  check-run. `3.1`
- **In a cloud session, `pip install playwright` installs a version whose default browser path doesn't
  exist.** Launch with `executable_path='/opt/pw-browsers/chromium'`. `3.0`
- **The cloud clone of the theme repo is shallow (50 commits).** Run `git fetch --unshallow` before
  reading history for receipts. `3.0`
- **`/projects` copy about thomascheesman.ca goes stale when the features change.** Re-trace a paragraph
  against the theme's code before a case study reuses it. `3.1`
- **To check a schema type is gone, count the old type's exact string.** `4.0`
- **`cf-ray` is on every response through Cloudflare.** A Cloudflare challenge carries
  `cf-mitigated: challenge`; `x-turbo-charged-by: LiteSpeed` means the origin answered. `4.1`
- **A check warms the cache it is checking.** Use a cache-busting query. This session's live curl used
  `?cb=`. `4.4`
- **The LiteSpeed Cache crawler's default interval is 302400 s.** It is set to 3600 s now. `4.0`
- **Chromium in a claude.ai cloud session rejects the session proxy's certificate.** Check live with
  curl instead. `4.1`
- **`getComputedStyle(el, '::before').content` returns the CSS expression, not the number drawn.** Check
  figure numbering in a screenshot. `5.0`
- **Pin research-repo receipts to a commit SHA.** Read the first and last line of each range in the
  pinned commit. `5.0`
- **Most of this repo is CRLF in Thomas's Windows checkout, and so is most of the theme.**
  - Detect CRLF in Python and edit byte-wise. This session `patch.py` kept each file's endings on every
    edit.
  - New files written by the Write tool are LF; Git warns and converts them.

  `6.5`
- **Run a local test server inside the Python process.** Used this session. `7.6`
- **Headless Chrome defaults to dark mode.** Set the colour scheme for each browser context. Used this
  session. `8.6`
- **Wait about 400 ms after a click before a screenshot.** Used this session. `7.3`
- **`/404` answers 200.** Test "not found" with an unknown URL. `6.2`
- **Cloudflare's build start has ranged from about 1 to 10 minutes.** Check the check-run before
  diagnosing a live page. Used this session. `8.3`
- **A test that Tabs a fixed number of times can land on the wrong control.** Loop until the target has
  focus. `6.2`
- **A receipt's "caught" column can be a guess.** Open the receipt before copy says "I". `7.2`

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
- **Lede:** from R3/R4. **R5 under it is now one sentence**: "I am looking for remote work running a
  nonprofit's website and digital operations." (LGR, 2026-09-29).
- Every project card links its case study: the graph, the Back Quarter and the Desk (P3). The "Four live
  sites" card links BYR, GPRS and this site. The "How I work" heading links `/method`.
- **The lede is tall on desktop.** At 1280×900 it pushes the ledger below the fold (DESIGN-2). That's a
  Phase 3 layout job, not a copy one.

**The build ledger (live 2026-09-29; copy-review-006):**
- **Order in the hero:** label, H1, lede, R5, the buttons, then the ledger.
- **The block is generated.** To change it:
  1. Edit `ledger/curation.json` or the handoffs.
  2. Run `python scripts/export-ledger.py`, then `--check`, then `site_check.py`.
  3. Ship.
- **A handoff's column appears only once its line is ruled** (`ruled` in the curation). At wrap:
  1. Draft the new handoff's line in copy-review-006 (LG25 for 024, LG26 for 025, and so on).
  2. Add it to the curation with `"ruled": null`.
  3. After Thomas rules, set `ruled`, export and ship.
- **A line:**
  - never copies handoff prose;
  - says "I" only for what Thomas did;
  - leaves out the private project, other sites' incidents and anything familial.
- **Items are drawn solid unless the curation's `parked` lists them** (dotted means parked on purpose, or
  waiting on Thomas). When a handoff opens or parks an item in scope, update `parked`. `--report` doesn't
  flag an unclassified new item: it just draws it solid.
- **What's never drawn:** O-\* and L-\* items, and rows under OTHER REPOS or LANDER.
- **A new §4 workstream heading stops the export** until the curation's `bands`, `fold` or `exclude` says
  where it goes.
- **An ID whose wording changes is a DOUBT in `--report`** until `reviewed_ids` or `split` records it. G-7
  is two items, split by its gap.
- **`site_check.py --live` fails whenever the live block isn't what the script writes now,** including
  after a curation change that hasn't shipped. That's intended.

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
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Accessibility controls (motion full/reduced/off, theme, contrast, text size) are **built into the site**. OS preferences are the defaults; the toggles override them and persist. Order: Phase 1 ✓ (2026-09-25) → **Phase 1b ✓ (2026-09-28): all six case studies live** → **Phase 2 ✓ (2026-09-29): the build ledger live in the home hero** → **Phase 3, next (craft; proposal first)**: motion, the built-in toggles, the ledger's place against the fold (DESIGN-2) and its later layers (PL-9) → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). |
| PL-8 | **Page-weight / a11y numbers: ruled ship without (2026-09-24)** | `/work/this-site` says none are shown because nothing measures them by script yet. When the Phase 4 budget script exists, the numbers go into that page's honest limits (plan-001 §6 Q5), through a copy review. |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers. |
| PL-9 | **The ledger's later layers (Phase 3)** | Left out of the static version (LG0): **traps** (separable per session only from handoff-019 on, when "New this session" began); **click a column to read its line**; **motion** (threads drawing in session by session, under the motion toggle). The words never depend on any of them. |

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
| DESIGN-2 | **The ledger sits below the fold at 1280×900** (seen 2026-09-29) | The first screen shows the H1, the tall lede and the buttons, as before. Where the ledger sits against them is Phase 3 layout (LG0 §4). |
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
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add `/work/gprs`, `/work/this-site`, `/method`, `/work/influence-graph`, `/work/bare-your-rare`, `/work/back-quarter`, `/work/desk-and-drawer` and the Projects sub-menu to that run. Left from 012: one real screen-reader run through the live graph, now on `/work/influence-graph`. **Two points for it:** the loop diagrams' links sit inside an SVG with `role="img"`, which may hide them from screen readers (the same links are in `/method`'s "originals" list); and the diagrams' connectors and arrows in `--rule` are faint on white (non-text contrast). **Also the home ledger:** two `role="img"` SVGs with a `<desc>` each, and its `<details>` list. |
| A-3 | **Sub-menu without JS cannot be dismissed with Esc** | Without JS the list shows on hover or focus (WCAG 1.4.13 asks for a dismiss key). With JS, Esc works. Accepted as the no-JS fallback; for A-1 to confirm. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-13 | **The nav is copied into thirteen files** | **Checker done (2026-09-26):** `site_check.py` checks every page's sub-menu. **Still manual:** the edit. This session's `ship.py` (scratchpad only) did it as all-or-nothing exact-match edits: the sub-menu li on every page lacking it, sitemap, `.assetsignore`, banner and noindex off, `SUBMENU`. A `scripts/` version that takes the new page, its label and its position is the rule-5 step. Not built. **2026-09-29:** the scratchpad `patch.py` is its core: all-or-nothing exact-match edits that keep each file's line endings. |
| INFRA-14 | **Two traps the mention doesn't prevent** | (a) **Bash `cd`** (trap dropped at `6.0` in handoff-023; hit again 2026-09-28 and 2026-09-29): a Claude Code `PreToolUse` hook that refuses a Bash command starting with `cd`. That changes Thomas's harness settings, so it is **his call; not built**. (b) **Full-page screenshots: done**, as `cs_check.py --shots`. |
| INFRA-16 | **A verbatim-quote checker in `scripts/`** | A shared script that takes the quote and the file, and runs its own control, is the rule-5 step. Not built. 2026-09-28's quotes were checked by `sed` against the theme source. 2026-09-29's were checked by a scratchpad `quote_check.py` (51 fragments, with a control), which caught one quote that joined two bullets. |
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
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. Thomas reminded 2026-09-24 through 2026-09-29. **He will renew on 2026-10-07** (said 2026-09-27). **Not confirmed paid.** |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-25 | **The home page slides sideways on phones (only the home page)** | 1.0.758 is deployed (1.0.759 too); the drawer fix holds on other pages. The home-only slide isn't found yet; the lead is content that scripts draw. Owned by the theme's newest `V0.*.md` Open (V0.45). |
| O-24 | **thomascheesman.ca phone header, and the no-JS lede** | (a) The fixed header capsule covers the start of the "THOMAS CHEESMAN" name line on phones. (b) Without JS, `.bq-lede__name` and `.bq-lede__deck` stay at opacity 0 (`.kinetic-fade`). (c) Thomas said the menu was "wonky" before the 429s. **2026-09-28: he hasn't seen it since, and will screenshot it if he does.** (d) The phone line says "On a phone" but tablets see it too. Theme work, his call on each. |
| O-20 | **The Back Quarter: 3D on PCs only — SHIPPED 2026-09-27 (1.0.755)** | Plan and rulings: theme `docs/BQ-3D-ONLY-PLAN.md`. **3D on phones is a later job** (Thomas: "we will bring it to the mobile"). When it ships, `/work/back-quarter`'s "Where it runs" row, its honest limit and `/projects`' "A phone gets a still" line change with it. `back-quarter-3d.js`'s header comment "MOBILE PLAY … phones are IN" is stale. |
| O-21 | **Theme repo: family material in its files, history and commit diffs** | **Private since 2026-09-26.** The history still holds the material; cleaning it is Thomas's call. The details went to him in the chat on 2026-09-26, not here, because this repo is public. |
| O-22 | **Hostinger deploy webhook URL was in a public theme file for about seven weeks** | Anyone with the URL can trigger a redeploy of `main`, no more. **Checked by Thomas 2026-09-28: hPanel has no regenerate option.** Left as is: rotating means deleting and re-creating the deployment, and last time that meant moving the live theme folder aside (V0.41). **Rotate it the next time the deployment is rebuilt,** by switching to Hostinger's GitHub App method, which manages the webhook itself. Then delete the old SSH entry in hPanel and the old webhook in GitHub. |
| O-16 | **AI crawlers on the Hostinger sites: ruled leave it ("1", 2026-09-26); re-checked on thomascheesman.ca 2026-09-28** | After the O-23 DNS fix, from Thomas's IP with each crawler's name: **ClaudeBot, Claude-User, PerplexityBot, OAI-SearchBot and ChatGPT-User get 200.** **GPTBot gets an instant, empty 429 from the origin** (`x-turbo-charged-by: LiteSpeed`, `panel: hpanel`): a name rule on Hostinger's server, not the CDN. Cloudflare's AI Crawl Control for that zone was not looked at. **BYR and GPRS were not re-checked.** O-27 (theme V0.45) found neither has the stacked-CDN DNS, so that doesn't explain BYR's refusals. Leave the Hostinger "Create LLMs.txt file" toggle **off**. Evidence for BYR: `Claude outputs/byr-bot-check-2026-09-25.md`. `/work/bare-your-rare`'s honest limit depends on this. |
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
| O-8 | thomascheesman.ca's open items live in its newest `V0.*.md` (**V0.45**) | Theme at 1.0.761. F3's premise was wrong: the HCS photos were already lazy `<img>` tags. The HCS alt text (1.0.760) and a Notch diagram (1.0.761) are live. Thomas: "hcs looks fine" (2026-09-29). `three-r128.min.js` idle-loads for every visitor: ruled keep on phones (2026-09-27), now 1x/~20 fps there. |
| O-10 | bareyourrare.org and thomascheesman.ca behind Cloudflare since 2026-09-20 | thomascheesman.ca has three cache layers. Full detail in handoff-014 §4. BYR's domain is on Cloudflare DNS: **don't click "Connect domain"** in hPanel. |
| O-11 | bareyourrare.org crawl audit, mostly deployed | `Claude outputs/byr-crawl-audit.md`. Still open: (g) page weight. |
| O-12 | GPRS work has its own handoff | `GPRS Organization/00 Working Notes/gprs-handoff-001.md`. |

**Closed since handoff-023:**
- **Phase 2, the build ledger:** LG0, LG1–LG24, LGR and LGP were ruled 2026-09-29. Live the same day (#15).
- **O-23:** closed in handoff-023 (two CDNs stacked). The row is dropped.
- **O-27:** neither BYR nor GPRS has the stacked-CDN DNS. BYR is proxied by Cloudflare straight to the
  origin; GPRS isn't on Cloudflare. Checked 2026-09-28 in a theme session (theme `V0.45.md`).
- **O-9:** the `page-hcs.php` Keg paragraph has been in HEAD since `ca61ffc` (2026-09-21), and is live (V0.45
  L183). On 2026-09-29 `git status` showed no uncommitted change to the file.

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

## 6. Next up — LG25, then the Phase 3 proposal

Before anything: remind Thomas once of **D-3**, if it's still open. He said he'll renew on 2026-10-07, and
it's due 2026-10-08. Each step ends with his ruling before the next starts.

1. **LG25, this handoff's ledger line** (copy-review-006). On his OK:
   1. Set `ruled` for `024` in `ledger/curation.json`.
   2. Run `python scripts/export-ledger.py`, then `--check`, then `site_check.py`.
   3. Open a PR, and merge on his word.
   4. Curl `/` against `main`, and run `site_check.py --live`.
2. **Phase 3, the craft proposal (PL-6). Propose before building.** It names:
   - motion, and the built-in accessibility toggles: motion full/reduced/off, theme, contrast, text size;
   - where the ledger sits against the tall lede (DESIGN-2);
   - the ledger's later layers (PL-9);
   - DESIGN-1 and G-7.

   Its copy opens `reviews/copy-review-007.md`.
3. **Rule-5 work, if Thomas wants it first:**
   - INFRA-13: `patch.py` into `scripts/`, as the core of the nav-and-ship tool;
   - INFRA-16: `quote_check.py` into `scripts/`;
   - DESIGN-1's open-menu case in `site_check.py`.

   The order is his call.

### After that

Phase 4: headers, schema, OG per page, and the budget script. PL-8's numbers go into `/work/this-site` once the
budget script exists, through a copy review.
