# handoff-019 — tc-ventures.ca

**Written:** 2026-09-25
**Covers:** Thomas reordered the plan: the **four remaining case studies come before the build
ledger**, in this order: the influence graph, then Bare Your Rare, then the Back Quarter and the
Desk together. **`/work/influence-graph` shipped.** The research repo is **public**, confirmed by
Thomas, so `/method`'s "files are private" line was cut (M9).
**Status at wrap:** everything in §2 marked "live" was **deployed and verified live**
2026-09-25. That means the check-run succeeded on every push, curl, a logged-out browser suite
against the live site, the graph loaded live under the real CSP, and live screenshots.

**The next job is the Bare Your Rare case study** (§6).

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. Read §2 "Traps" before you touch git, grep, line endings, a
   screenshot, the nav, or the `Reports Clustering` folder.
2. `CLAUDE.md` at repo root: the twenty truth rules. `plans/operating-guide.md` is how
   Thomas and the AI divide the work, and §4 there is the checking routine.
3. **`plans/plan-001-showcase.md`**: the plan. **The §5 note (2026-09-25)** holds the new order.
   §3 lists the case studies, and §4c is the build ledger that now comes after them.
4. **`plans/receipts-001.md`**: the ruled inventory, 37 OK / 75 CUT. Only OK rows go in copy.
   Tick `chk` before quoting a row.
5. **`reviews/copy-review-004.md`**: the current review. The next case studies' blocks go in it.
6. The shipped pages under `public/`. **`work/influence-graph.html` is the pattern to copy.**
7. `claude/thomas-study.md` and `claude/tc-ventures-site-decisions.md` in the Claude project
   "TC 'Ventures" (not on disk, not read this session).
8. `README.md`.
9. If the job is GPRS itself, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md`.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**.

**How Thomas works:** short answers when he asks for them; blunt when you are wrong; makes
the calls himself. Recommend one option; don't survey. He rules tersely ("BRICS, q-ig5 yes,
ship it"), and that is a full ruling. He is self-taught and model-agnostic, so explain
methods, not one model's tricks. **He commits and pushes himself, sometimes mid-session**
(again this session, `bd2b180`): re-read `git status` just before you commit.

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
| Pages | `index`, `projects`, `method`, `background`, `contact`, `404`, `work/gprs`, `work/this-site`, **`work/influence-graph`** (live 2026-09-25). Internal links, canonicals and sitemap use **clean URLs** (`/method`); `/x.html` 307s to `/x`. |
| Nav | **Projects (with a sub-menu of the case studies) · Method · Background · Contact**, on every page: **10 files** including `_template.html`. The sub-menu order is the `/projects` order: **The Economic Report Influence Graph · A housing society's website · This site**. The markup is copied into each page, since there is no build step. `assets/nav.js` (deferred, every page) makes the sub-menu a disclosure button. Below 420px the nav gap tightens to 14px and the nav wraps. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html` and `og-src/` off the live site. A preview goes in it until it ships. |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. Reasons are commented in the file. Unchanged since handoff-017. |
| Link preview | `assets/img/og-card.png` 1200×630 on all pages, with the R2 headline. Source `public/og-src/og.html`; re-render command in its `<style>` comment (needs a local server on :8788). |
| Analytics | Cloudflare Web Analytics, injected at the edge. The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` + the audit phases (PL-6) · receipts `plans/receipts-001.md` (ruled) · `plans/operating-guide.md` |
| Design system | `public/assets/style.css` — tokens in `:root`, case-study components under the `CASE STUDIES` banner at the end |
| Graph demo | **Now on `/work/influence-graph` only.** `assets/graph-demo.js` + `gp-budget-graph.json` (snapshot committed 2026-09-16) + prebuilt `3d-force-graph.min.js`. `/projects` no longer loads it. |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. Thomas edits it himself. |
| Browser tests | **Python Playwright + Chromium are installed.** This session's scripts are in the session scratchpad, not the repo (INFRA-13): `site_check.py local\|live` (every page's status, nav order, both `aria-current` levels, no `noindex`/banner, console, 375px, the sub-menu by keyboard, with a negative control), `ig_check.py` (the case study: demo keyboard path, JS off, every link, with a negative control) and `live_graph.py`. |
| Research repo | `C:\Users\thoma\Desktop\My Files\Reports Clustering`. **Public on GitHub** as `DriftingSplash9/Reports-Clustering` (API `"visibility": "public"`; Thomas confirmed it is intended, 2026-09-25). **Never run git there, not even `git status`** (its `CLAUDE.md` rule 1: the lock file blocks Thomas's GitHub Desktop). Read its files, and read it on GitHub through the API or raw URLs. |
| Sister repos | `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` = GitHub `DriftingSplash9/thomascheesman-ca-theme` (**public**; the old name 301s). `bareyr` (BYR): **404 on GitHub to a logged-out request**, so its files can't be linked as receipts. |

## 2. What was done (2026-09-25, after handoff-018)

**Rulings:**
- **The case studies come before the build ledger.** The order is graph → BYR → Back Quarter +
  Desk. Design waits until the content is mostly in place. This is recorded in plan-001 §5.
- **The research repo is meant to be public.** receipts-001's F-2 note and §3C intro are
  corrected in place, with the old wording kept.
- copy-review-004 rulings: **M9 A**, **IG0 A** (link the research files as they are),
  **IG1–IG7 OK**, **P1 OK**, **Q-IG3 yes**, **"seven" KEEP**, **Q-IG4 BRICS**, **Q-IG5 yes**
  (the Fig. 1 counts exception covers the case study too).
- **Q-IG1, the ask, in Thomas's words:** "I made the Graph because I wanted to see how
  something at a municipal level is influenced by something on the international level. I also
  wanted to see how organizations such as the EU and BRICS operate compared to nations." It is
  the pull quote. "nations.," was closed up, and "BRICS" is at his ruling.
- **Q-IG2: since July 2026.**
- **Traps now carry an `x.y` tally,** with a drop rule. Thomas's rule, so **§5 changed**
  (2026-09-25). The first audit is in "Traps" below.

**Live, and verified live:**
- **`/method` M9:** the "files are private" sentence is cut (`f49090a`).
- **`/work/influence-graph`** (`5dda7b6`):
  - The three misses are R-050, R-076 and R-110.
  - The demo moved here from `/projects`.
  - Receipts are pinned to research commit `8b2f593`.
  - It's in the sitemap, and first in the sub-menu on all ten files.
- **`/projects` (P1)** now has the intro, the app figure, "read the case study" and the Source
  link.
- **Home** links the case study.
- **CSS, one additive line:** `.shot + .prose`, for the one place on the site where prose
  follows a figure directly.
- **Verified live:**
  - The check-runs succeeded, and curl was run on every page, `.html` and an unknown URL.
  - The logged-out suite passed 100 of 101. The failure is `/404`'s intended `noindex`.
  - The graph loaded under the real CSP, with keyboard read-out, a clean console in both
    themes, and the beacon answering 200.

### Traps worth knowing

Each trap ends with its tally, **`x.y`** (§5). x was counted by grep across handoff-001 to 019,
older wordings included. y starts this session, because no earlier handoff recorded an avoided
trap. "Restored" marks six traps this handoff's first draft dropped without comment.

**New this session:**
- `getComputedStyle(el, '::before').content` returns the CSS expression (`"Fig. "
  counter(fig)`), not the number drawn. Check figure numbering in a screenshot. `0.0`
- Pin research-repo receipts to a commit SHA. Its `HANDOFF.md` is rewritten every session and
  its files move into `archive/`. Read the first and last line of each anchored range in the
  pinned commit via `raw.githubusercontent.com`. `0.0`

**Carried:**
- Bash `cd` moves the session's working directory (into `public/`, and once into `Reports
  Clustering`). Never start a Bash command with `cd`. Use absolute paths, `git -C`, or
  `( cd … && … )`. **Hit twice more this session despite the mention** (INFRA-14). `2.0`
- Full-page headless shots of a tall page: lazy images render black, and the shot tiles near the
  bottom. Shoot per section after `scrollIntoView` and about 700 ms (`ig_shots.py`). **Hit
  again this session despite the mention** (INFRA-14). `5.0`
- Git Bash `grep -c $'\r'` can't see carriage returns. Detect CRLF in Python. These are CRLF:
  `.assetsignore`, `sitemap.xml`, `projects.html`, `work/gprs.html`, `plans/receipts-001.md`.
  Edit byte-wise. `1.1`
- Python heredocs through Git Bash eat backslashes. Use forward slashes, or write the script
  to a file. `4.1`
- Run a local test server inside the Python process. A Git Bash `http.server` survives
  `pkill`. `2.1`
- Headless Chrome defaults to dark mode. Set the colour scheme for each browser context. `3.1`
- Wait about 400 ms after a click before a screenshot (restored). `2.1`
- `/404` answers 200. Test "not found" with an unknown URL. `1.1`
- Analytics can't be seen headless. Check that `beacon.min.js` answers 200 and the console has
  no CSP errors. `1.1`
- Cloudflare injects the beacon at the edge, so read the live console after any CSP change. A
  new inline `<script>` is blocked by the CSP; put it in `/assets/*.js` (restored). `4.0`
- Cloudflare's build start has ranged from about 1 to 10 minutes. Check the check-run before
  diagnosing a live page (restored). `3.1`
- A test that Tabs a fixed number of times can land on the wrong control. Loop until the
  target has focus. `1.1`
- A hidden browser pane fires no focus or blur events, so test focus logic in Playwright.
  Playwright's visibility checks see through `clip-path: inset(50%)` (that part restored).
  `2.1`
- A receipt's "caught" column can be a guess. Open the receipt before copy says "I". `2.1`
- A figure Thomas gives can have no source on disk. Say where you searched, and ask. `1.0`
- `gh api markdown` emits no heading ids (curl the blob page for `user-content-<anchor>`), and
  `git log -S` needs `--no-textconv` here (restored). `2.0`
- There's no LibreOffice, pandoc or `pdftoppm` here. Render a `.docx` through Word COM,
  read-only, with `Quit()` in `finally`, then make page images with PyMuPDF. `1.0`

**Audit, 2026-09-25:**
- **By the `x.y` rule, none goes yet.** Full-page shots, at `5.0`, goes next handoff unless it
  earns a use.
- **Five cut as repeats of rules written elsewhere** (rule 17):
  - copy-review-001 links (§3)
  - count from memory (`CLAUDE.md` 12)
  - the model's name in paths (§3, O-14)
  - review notes from memory (`CLAUDE.md` 11)
  - ten nav files (§3, INFRA-13)
- `cd` and full-page shots were hit again despite the mention, so they belong in code
  (INFRA-14).

## 3. Current design

**Pages live:** `/work/gprs` and `/work/this-site` (2026-09-24), `/method` and
**`/work/influence-graph`** (2026-09-25).

**The case studies:**
- **Six fixed sections**, receipts as small mono links, figures `Fig. N` per page.
- Every claim in "What the AI got wrong" and "How I caught it" links to a receipt that
  returns 200 publicly, or is cut.
- **"How I caught it" says "I" only for catches Thomas made.** Agent catches are written
  impersonally.
- **Rules-table captions say "falls under"**, not "became", unless the timing is confirmed in
  the receipt. "The rule now" is used where the rule changed after it was made.
- **"The ask" quotes Thomas's own words.** If there's no brief on disk, ask him (Q-G1, Q-IG1).
- A case study that takes content from `/projects` takes it unchanged. `/projects` keeps a
  short intro and a "read the case study" line (P1 is the pattern).

**`/method`:**
- **The H1, the lede and the page title are Thomas's rulings.** Don't edit them, explain the
  accessibility line, or raise them again unasked.
- Research-project rows still link receipts-001 §3C. That's fine now that the repo is
  public, and it isn't proposed for change.

**Nav:**
- Adding a case study means editing all **ten** files. A case study's sub-menu label is its H1,
  in the `/projects` order.
- Ship the page and its link in the same push, never a link that 404s.
- Check afterwards that every page's nav is identical (INFRA-13).

**Look and feel:**
- Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
  `prefers-color-scheme`.
- Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
- Confirmed; stop re-litigating it. **Thomas, 2026-09-25: design waits until the content is
  mostly in place.** Log layout nits for Phase 3 rather than fixing them, unless a change you
  made caused them.

**Case-study layout (approved 2026-09-22):** a wide lane (1040px) for headers, figures,
tables and lists and a reading lane (66ch) for prose; a sticky 200px rail at ≥1180px with
the section index, folding to a horizontal index below that; sections numbered by CSS
counters, figures `Fig. N` per page; receipts as small mono links with a leading `→`.

**Home page (live 2026-09-22):**
- **Label:** "Thomas Cheesman · Grande Prairie, Alberta · remote".
- **H1:** "I run a nonprofit's website, and I hold it to a written standard."
- **Lede:** from R3/R4.
- The graph card links `/work/influence-graph`. The "Four live sites" card links both site
  case studies. The "How I work" heading links `/method`.
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
- **The outside research model is never named in copy** (F-2), and no link's path may
  carry its name.

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
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Accessibility controls (motion full/reduced/off, theme, contrast, text size) are **built into the site**. OS preferences are the defaults; the toggles override them and persist. Order: Phase 1 ✓ (2026-09-25) → **Phase 1b, the remaining case studies (ruled 2026-09-25): graph ✓ → BYR → Back Quarter + Desk** → Phase 2 (the build ledger as the home hero, static SVG; plan-001 §4c) → Phase 3 (craft; **proposal first**) → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). |
| PL-8 | **Page-weight / a11y numbers: ruled ship without (2026-09-24)** | `/work/this-site` says none are shown because nothing measures them by script yet. When the Phase 4 budget script exists, the numbers go into that page's honest limits (plan-001 §6 Q5), through a copy review. |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-22 | **`/method` rules row 1 says "I caught it by using them"** (the three sliders) | The receipts confirm Thomas caught the last two (handoffs 006/007 and 032). Nothing found on how the first (`geoAffinity`) was caught. Reported as a DOUBT in copy-review-004. No change proposed. His call if he wants it narrowed. |
| C-23 | **`/projects` lede and meta after the splits** | The lede says "Three built in the open, in detail — what they are, what was hard, and what I got wrong." The graph's detail has moved to its case study, and the Back Quarter's and the Desk's will too. Review the lede and description when those two ship. Not raised with Thomas yet. |
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
| G-7 | **The demo's paragraph sits tight against its frame** | On `/work/influence-graph` (and formerly `/projects`): `.gd__frame` has no top margin after `.prose`. Phase 3 layout. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add `/work/gprs`, `/work/this-site`, `/method`, **`/work/influence-graph`** and the Projects sub-menu to that run. Left from 012: one real screen-reader run through the live graph, now on `/work/influence-graph`. **Two points for it:** the loop diagrams' links sit inside an SVG with `role="img"`, which may hide them from screen readers (the same links are in `/method`'s "originals" list); and the diagrams' connectors and arrows in `--rule` are faint on white (non-text contrast). |
| A-3 | **Sub-menu without JS cannot be dismissed with Esc** | Without JS the list shows on hover or focus (WCAG 1.4.13 asks for a dismiss key). With JS, Esc works. Accepted as the no-JS fallback; for A-1 to confirm. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-13 | **The nav is copied into ten files** | Adding a page means editing all ten. Rule 5 says the same miss twice becomes code. This session's `site_check.py` checks nav equality, both `aria-current` levels, keyboard, 375px and console, with a negative control; `ship_ig.py` makes the ten edits with asserted matches. **Both are still in the scratchpad, not in the repo.** Moving them into `scripts/` is the rule-5 step. |
| INFRA-14 | **Two traps the mention doesn't prevent** (§2, tallies `2.0` and `5.0`) | Rule 5: move them into code. (a) **Bash `cd`**: a Claude Code `PreToolUse` hook that refuses a Bash command starting with `cd`. That changes Thomas's harness settings, so it is **his call; not built**. (b) **Full-page screenshots**: move `ig_shots.py` (per-section shots) into `scripts/`, with INFRA-13. |
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
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. Thomas reminded 2026-09-24 and 2026-09-25 (twice). **Not confirmed paid.** |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-14 | **Research repo: 52 public file paths carry the outside model's name** | Thomas ruled 2026-09-07 that the research docs drop the name (F-2). The public archive still carries it, in paths and text. His call. Nothing was changed there. |
| O-15 | **Research repo: "read the sentence as well as fetching it" is not in its current playbooks** | It was written in `archive/NZ/G.3.md` L539 (2026-08-06). A grep of `PLAYBOOK*.md` for it, "grammatical" and "subject of" found nothing. `/work/influence-graph`'s table row uses `CLAUDE.md` rule 13 instead. His call whether the research project carries it again. |
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
| O-13 | **BYR still serves `NGO` schema on guide pages** | From receipts-001 §5 (R-141). Fix is in `bareyr/functions.php` L707–715. **Not re-checked live.** It matters now: the BYR case study is about the site's schema (§6). |

**Closed this session:**
- **`/work/influence-graph`:** live.
- **M9:** the false "private" line on `/method` is cut.
- **The research repo's visibility:** public, confirmed by Thomas.

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
- **Every trap ends with a tally `x.y`** (Thomas, 2026-09-25).
  - **x** is the number of handoffs the trap has been carried into since the one that recorded
    it. Add 1 each time it is carried.
  - **y** is the number of sessions where the mention changed what was done. Add 1 only when
    you can name what it changed.
  - **Drop a trap when x > 5 and y ≤ 1, and at x = 10 whatever y is.**
  - *Added with it by the agent, pending Thomas's OK:*
    - A trap hit again despite its mention gets no y. Say so on the line.
    - A trap still earning its place at x = 10 belongs in code (`CLAUDE.md` rule 5).
    - A "trap" that repeats a rule already in §3 or `CLAUDE.md` is not a trap: cut it.
    - A dropped trap gets one line in §2 of the handoff that drops it, naming it, and no more.

## 6. Next up — the Bare Your Rare case study

Before anything: remind Thomas once of **D-3** (the email renewal, due **2026-10-08**) if
it's still open. Each step ends with his ruling before the next starts.

### Step 1 — check the ground before drafting

1. **Re-check O-13 live.** Is bareyourrare.org still serving `NGO` schema on its guide pages?
   Curl logged out, and read the JSON-LD. plan-001 §3 frames the case study as "making a
   patient site legible to AI assistants (the audit, the schema, the host fault, the fix,
   verified)". If the wrong schema is still live, the fix probably lands on BYR before the
   case study ships. Put that to Thomas; don't decide it.
2. **Receipts.** §3E has two OK rows:
   - **R-140** (the invented charity). Its receipt is in the `bareyr` repo, which 404s
     publicly, so it links receipts-001 §3E, as `/method` does.
   - **R-147** (the empty category). Its receipt is `Claude outputs/byr-crawl-audit.md` in
     this repo, which is public.
   - A third can come from **this repo's handoff-011/012** (the host fault and the fix,
     verified live). Those are receipts, but they are not rows in receipts-001. Propose adding
     them as new rows for Thomas to rule on before the copy uses them.
   - Read every linked file against the privacy rules (R-026). BYR is a patient site: no
     symptom detail, and no family.
3. **"The ask" in his words.** Look for a BYR brief in the bareyr repo's `AGENTS.md` or its
   archive. If none, ask him, as Q-G1 and Q-IG1 did.

### Step 2 — draft in copy-review-004, then the preview, then ship

Follow the IG pattern: blocks BYR0–BYR8 (plus any `/projects` change) → Thomas rules → a
preview in `.assetsignore`, checked with adapted `ig_check.py`/`ig_shots.py` → "ship it" →
a `ship_ig.py`-style script → the site suite, local and live.

### After BYR

The Back Quarter and the Desk need **a receipts pass first**, over the thomascheesman.ca
theme repo's `V0.*.md` files. That repo is public, so its receipts can be linked. Then one
copy review covers both, and C-23 (the `/projects` lede) gets settled when they ship. Then
Phase 2, the build ledger proposal (plan-001 §4c). **Propose before building.**
