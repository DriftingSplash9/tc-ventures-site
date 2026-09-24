# handoff-017 — tc-ventures.ca

**Written:** 2026-09-24
**Covers:** Phase 1 step 2 closed: **`/work/this-site` shipped**, and a **Projects sub-menu**
listing both case studies is on every page (Thomas's request, replacing PL-7's "Work"
menu item).
**Status at wrap:** everything in §2 marked "live" was **deployed and verified live**
2026-09-24: the Cloudflare check-run completed with success; curl; a full real-browser test
suite run against the live site; console and analytics beacon checked on every page; a
headless render of the live page. **The next job is `/method`**, after one question to
Thomas (§6).

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. §2 "Traps" before you touch git, grep, headers, DNS, a rebuild,
   a screenshot or the nav.
2. `CLAUDE.md` at repo root: the twenty truth rules. `plans/operating-guide.md` is how
   Thomas and the AI divide the work.
3. **`plans/plan-001-showcase.md`**: the plan. The audit's Phases 0–4 slot into it (PL-6).
   Nothing gets built outside it without Thomas agreeing.
4. **`plans/receipts-001.md`**: the ruled inventory. Only rows ruled **OK** may be used in
   copy. Tick `chk` on a row before quoting it (§0 of that file). §6 is the rules table for
   `/method`; §6 of this handoff says which of its rows are OK.
5. `reviews/copy-review-003.md`: the Phase 1 review. R1, G1–G9 and T0–T10 are all ruled,
   with the rulings recorded after each set.
6. `public/work/gprs.html` and `public/work/this-site.html`: the two shipped case studies.
   Copy their structure. `public/work/_template.html` is the bare template; its sample copy
   is superseded by this-site.
7. `claude/thomas-study.md` and `claude/tc-ventures-site-decisions.md` in the Claude
   project "TC 'Ventures" (voice study, decisions). Not on disk; not read this session.
8. `README.md`.
9. If the job is GPRS itself, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md`.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**.

**How Thomas works:** short answers when he asks for them; blunt when you are wrong;
makes the calls himself. Recommend one option; don't survey. He answers reviews tersely
("t0-A, t3- ok, q-T1- yes"), and that is a full ruling. He is self-taught and deliberately
model-agnostic, so explain methods, not one model's tricks.

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
| Pages | `index`, `projects`, `background`, `contact`, `404`, **`work/gprs`**, **`work/this-site`** (both case studies live 2026-09-24). Internal links, canonicals and sitemap use **clean URLs** (`/projects`); `/x.html` 307s to `/x`. |
| Nav | **Projects has a sub-menu** of the case studies, on every page (8 files including `_template.html`). Markup is copied into each page (no build step). `assets/nav.js` (deferred, every page) makes it a disclosure button; CSS under "Projects sub-menu" in `style.css`. |
| Not deployed | `public/.assetsignore` keeps `work/_template.html` and `og-src/` off the live site. Both 404 live. |
| Headers | `public/_headers` — CSP, HSTS (1 yr, no subdomains/preload), nosniff, X-Frame DENY, referrer, permissions, COOP; fonts `immutable`. Reasons are commented in the file. |
| Link preview | `assets/img/og-card.png` 1200×630 on all pages, with the R2 headline. Source `public/og-src/og.html`; re-render command in its `<style>` comment (needs a local server on :8788). |
| Analytics | Cloudflare Web Analytics, injected at the edge. The CSP allows `static.cloudflareinsights.com` + `cloudflareinsights.com`. |
| Plan | `plans/plan-001-showcase.md` + the audit phases (PL-6) · receipts `plans/receipts-001.md` (ruled) · `plans/operating-guide.md` |
| Design system | `public/assets/style.css` — tokens in `:root`, case-study components under the `CASE STUDIES` banner at the end |
| Graph demo | `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js` |
| Résumé | Source `resume/Thomas-Cheesman-Resume-source.docx`; mirror `resume/resume-source.html`; served PDF `public/assets/Thomas-Cheesman-Resume.pdf` |
| LinkedIn | `https://www.linkedin.com/in/thomas-cheesman-20234285/` — in every footer. Thomas edits it himself. |
| Browser tests | **Python Playwright + Chromium are installed** (`%LOCALAPPDATA%\ms-playwright\chromium-1217`). Real Tab/Enter/Esc, hover, touch, true 375px. The sub-menu suite used this session is described in §2. |
| Sister repo | `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` (thomascheesman.ca). Not connected by default; request access. |

## 2. What was done (2026-09-24, after handoff-016)

**`/work/this-site`: live.**
- Drafted as copy-review-003 T0–T10 from the seven OK rows in receipts-001 §3B. Rulings
  2026-09-24:
  - **PL-8:** ship without page-weight or accessibility numbers.
  - **Lead misses:** R-024 (focus lost, checker passed), R-028 (CSP broke analytics live),
    R-011 (exact counts). The other four go in the rules table.
  - **T0 A:** link the handoffs as they are.
  - **T3 OK:** PL-4's paragraph, reworded.
  - **T7:** **Thomas caught R-024 himself by testing** (his words are verbatim in the
    review). The copy says so, including "My mistake".
  - **Q-T1 yes:** the two figures ship.
  - **Q-T2 OK:** linked from the home "Four live sites" card and Projects' "The fourth is
    this one", as "read the case study".
- **The template's own copy was wrong in two places, and both were fixed before review.**
  "All caught before they shipped": all three lead misses were live first. "The first
  drafts stated" the counts: they were live copy.
- Of the template's three misses, only R-011 survived. The screensaver names are P-03
  (private) and "available now" is R-013 (CUT).
- **`reviews/copy-review-001.md` is linked nowhere on the page.** It debates the health
  disclosure and carries the private career-gap blocks. R-019 and R-022 link receipts-001
  rather than handoff-005/008; handoff-008 mentions the lander 35 times.
- Figures: `assets/img/this-site-home.webp` and `this-site-gprs.webp`, taken with headless
  Chrome at 1280×720, light scheme, from the live pages, 2026-09-24. **Fig. 1 predates the
  sub-menu, so the nav in it has no chevron.** It's a dated screenshot Thomas approved, so
  it was left as is.
- receipts-001: R-011, R-019, R-022, R-024 and R-027 ticked as re-read. R-024's "caught"
  corrected to Thomas.

**Projects sub-menu: live on every page.** Thomas: "Include this one and the last one in a
sub menu under projects." This replaces PL-7's "Work" menu item.
- **Labels are the case studies' H1s**, so there is no new copy.
- **Without JS:** the list is visually hidden but in the tab order. It shows on hover and
  on `:focus-within`, and Projects links to both case studies.
- **With JS:** `nav.js` makes it a WAI-ARIA disclosure. The button toggles `aria-expanded`;
  Esc closes it and returns focus to the button; it closes on focus-out or a click
  elsewhere. Mouse hover opens it after a 250 ms close delay, and a click pins it open.
- **The button appears from first paint** via `@media (scripting: enabled)`, so nothing
  shifts. Older browsers fall back to `[data-enhanced]`.
- **Case-study pages mark Projects `aria-current="true"`** and their own link
  `aria-current="page"`.
- **Verified with a Playwright suite, 32 checks, run locally and then against the live
  site: all pass.** It covers keyboard walk, Esc, Space, hover travel onto the list,
  click-outside, JS-off Tab and hover, and every page at 375px touch (no sideways scroll,
  menu inside the screen). **A negative control, with `nav.js` blocked, correctly fails.**
  The script is in the session scratchpad, not the repo; see INFRA-13.
- **Live:** no console errors on any page (the 404 page logs its own 404), and the
  analytics beacon returns 200 on every page, so the CSP is unaffected.

### Traps worth knowing

- **The built-in browser pane was hidden again**, and in a hidden page `el.focus()` moves
  `activeElement` but fires **no focus or blur events**. Focus-out logic cannot be tested
  there. Use Playwright: it does real keys, hover and touch, and at a true 375px, which
  also sidesteps the headless-Chrome minimum-width trap.
- **Playwright's `is_visible()` and bounding boxes see through `clip-path: inset(50%)`.** A
  visually-hidden element also needs `width/height: 1px` with `min-width: 0; padding: 0;
  border: 0`. Otherwise `min-width` keeps a 240px box, and a size check fails even though
  nothing shows.
- **A screenshot taken right after a click catches CSS transitions halfway.** The chevron
  looked bent. Wait about 400 ms.
- **`cd` inside a Bash call moved the session's working directory** to `public/` twice. Use
  absolute paths.
- **`gh api markdown` does not emit heading ids.** To confirm a GitHub anchor, curl the blob
  page and grep for `user-content-<anchor>`. A misspelt anchor returns nothing.
- **`git log -S` fails on this repo** (a `.docx` textconv). Add `--no-textconv`.
- **A receipt's "caught" column can be a reader's guess.** R-024 said "manual keyboard
  test", unticked. Ask Thomas before copy says who caught something.
- **Every handoff mentions the Rocket Lander.** Ruled fine to link (T0 A). copy-review-001
  is the file never to link.
- **This session, Cloudflare built in about a minute** (the 7–10 minute start delay from 016
  did not happen). Still check the check-run before diagnosing.
- Carried and still true:
  - Cloudflare injects the analytics beacon at the edge, so read the live console after any
    CSP change.
  - Console logs persist across navigations in the built-in browser.
  - Any new inline `<script>` is blocked by the CSP. Put it in `/assets/*.js`.
  - Headless Chrome defaults to dark mode (`--blink-settings=preferredColorScheme=1` for
    light).
  - Lazy images render black in tall headless shots unless the window is tall.
  - A local `http.server` from Git Bash survives `pkill`: stop it with PowerShell
    `Stop-Process`, found via `Get-NetTCPConnection -LocalPort`.
  - Python heredocs through Git Bash eat backslashes in Windows paths.
  - Grep, don't count from memory.

## 3. Current design

**Case studies live:** `/work/gprs` and `/work/this-site` (both 2026-09-24).
- **Six fixed sections**, receipts as small mono links, figures in `.shot--pair`.
- Every claim in "What the AI got wrong" and "How I caught it" links to a receipt that
  returns 200 publicly, or is cut.
- **"How I caught it" says "I" only for catches Thomas made.** Agent catches are written
  impersonally ("the deploy was checked").
- A rules table row may carry its own receipt link.
- The caption says "the rule it falls under", not "became", unless the timing is confirmed.

**Adding a case study now means editing the nav in all eight pages** (index, projects,
background, contact, 404, the two case studies, `_template`). Use the case study's H1 as the
label, and ship the page and the nav link in the same push (never a link that 404s).

Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
`prefers-color-scheme`. Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
Confirmed; stop re-litigating it.

**Case-study layout (approved 2026-09-22):**
- **Lanes:** a wide lane (1040px) for headers, figures, tables and lists; a reading lane
  (66ch) for prose.
- **Rail:** a sticky side rail (200px) at ≥1180px carries the six-section index, folding
  into a horizontal index below that.
- **Numbering:** sections auto-numbered from CSS counters; figures `Fig. N` per page.
- **Receipts** are small mono links with a leading `→`.
- **Six fixed sections:** The ask · The standard · What the AI got wrong · How I caught it ·
  What shipped · Receipts.

**Home page (live 2026-09-22):**
- **Label:** "Thomas Cheesman · Grande Prairie, Alberta · remote".
- **H1:** "I run a nonprofit's website, and I hold it to a written standard."
- **Lede:** from R3/R4.
- The "Four live sites" card links both case studies.
- The lede is tall on desktop: a Phase 3 layout job, not a copy one.

**Standing rules:**
- **The Rocket Lander is private.** Not here, in any form.
- `object-fit: contain`, never `cover`.
- **Content renders without JavaScript.** JS is allowed on top (motion, 3D, controls);
  the words and links must not depend on it. No dependencies or build step — prebuilt
  bundles copied into `assets/` only.
- Fonts self-hosted. No third-party font request.
- No phone number on the site. It is in the résumé PDF.
- **Never publish an exact node, edge, report or grade count** *in copy*. Round or
  describe. The application screenshot on Projects is the one ruled exception.
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
| PL-6 | **Audit action plan; direction RULED 2026-09-22** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** Accessibility controls (motion full/reduced/off, theme, contrast, text size) are **built into the site**; OS preferences are the defaults, toggles override and persist. Order: **Phase 1** (receipts ✓ → `/work/gprs` ✓ + `/work/this-site` ✓ → `/method`) → Phase 2 (build ledger as home hero, static SVG) → Phase 3 (craft; **proposal first**) → Phase 4 (headers/schema/OG per page/budget script; then CSSDA/Godly, then Awwwards). |
| PL-7 | **Nav: RULED 2026-09-24, live** | Case studies sit in a **sub-menu under Projects**, not a "Work" item. **Open question:** does plan-001 §3's `/work/` index (and `/projects` → `/work/` redirect) still happen? The redirect would remove the graph, Back Quarter and Desk write-ups until they are split into case studies. Ask Thomas (§6). |
| PL-8 | **Page-weight / a11y numbers: ruled ship without (2026-09-24)** | `/work/this-site` says none are shown because nothing measures them by script yet. When the Phase 4 budget script exists, the numbers go into that page's honest limits (plan-001 §6 Q5), through a copy review. |
| PL-1 | plan-001 approved 2026-09-21 | §6 of the plan holds his answers. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-18 | **copy-review-003 is the Phase 1 review** | R1, G1–G9 and T0–T10 are ruled. `/method` blocks go next (M1…), here or in a new copy-review-004. |
| C-19 | **Q-G2 unresolved: when did "read the actual code" enter the audit prompt?** | Thomas doesn't recall. The live page makes no causal claim. Don't reintroduce one. |
| C-20 | **`/work/this-site` states two things that will go stale** | "rebuild in progress" (header) and "has not had a screen-reader run-through yet" (honest limits). Update both when the rebuild ends and when A-1 is done. |
| C-15 | Résumé PDF: **site copy done**, private copy unchecked | Served PDF replaced 2026-09-23 (md5 `0da7af62…`, matches repo). Not checked: `Family & Personal\resume\Thomas_Cheesman_Resume.pdf`. Cosmetic: summary ends on a one-word line ("roles."). |
| C-16 | **Job history, from Thomas 2026-09-23. Use these** | GPRS board: elected at the **June 2023** AGM (first meeting September). Majors consulting: May 2019 – **June 2020**. **Head Chef, Ric's Grill, Sep 2013 – Jul 2014.** **Executive Chef, Township 71, Jul 2014 – Jun 2015** (renovation from Oct 2014, opened Nov 2014, closed May 2015, wind-down through June). **Taught one GPRC semester, Sep – Dec 2014.** |
| C-13 | GPRS site history | WordPress.com 2023; self-hosted WordPress.org on Hostinger 2025 "because I wanted more freedom to experiment with the code." Used in `/work/gprs`. No month-level dates without asking. |
| C-17 | R4 wording, his call | Live: "…then build it with help writing by AI." **Do not raise it again or change it unasked.** |
| C-9 | `page-thomas.php` ~2010: "I couldn't get past my kitchen manager" | His prose and his call. Flag it, do not rewrite it. |

### PROJECTS / GRAPH
| # | Item | Notes |
|---|---|---|
| P-6 | A fourth project? | Nothing queued; show finished work only. |
| G-6 | Demo still is a headless render | Thomas screenshots the live demo if he wants a hand-framed one. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass, deferred by Thomas (2026-09-21)** | He does it when design and content are final. Do not raise it before he does. Add `/work/gprs`, `/work/this-site` and the Projects sub-menu to that run. Left from 012: one real screen-reader run through Projects and the live graph. |
| A-3 | **Sub-menu without JS cannot be dismissed with Esc** | Without JS the list shows on hover or focus (WCAG 1.4.13 asks for a dismiss key). With JS, Esc works. Accepted as the no-JS fallback; for A-1 to confirm. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-13 | **The nav is copied into eight files** | A new case study means editing all eight by hand. Rule 5 says the same miss twice becomes code: a small script in `scripts/` that fails if the navs differ (and that runs the sub-menu Playwright checks) would catch it. Not built. |
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
| D-3 | **Professional Email renewal, due 2026-10-08** | Subscription 27350377, CA$48/yr, on the gpresidentialsociety.wordpress.com site, auto-renew off. Link: `https://wordpress.com/checkout/renew/27350377`. Thomas reminded 2026-09-24. **Not confirmed paid.** |

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
- **PL-4:** T3 ruled OK.
- **PL-7:** superseded by the sub-menu. The `/work/` index question moves into PL-7's new row.
- **INFRA-12:** the `.assetsignore` line-ending noise was not seen on 2026-09-24.
- **`/work/this-site`:** live.

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

## 6. Next up — Phase 1, step 3

Before anything: remind Thomas once of **D-3** (email renewal, 8 October) if it's still
open. Each step ends with his ruling before the next starts.

### Step 3a — one question first (PL-7)

Ask: now that the case studies sit under Projects, does the `/work/` index still happen, and
does `/projects` still become a redirect (plan-001 §3)? Recommend **no index for now**: two
case studies don't need one, and the redirect would remove the graph, Back Quarter and Desk
write-ups. Record his answer in plan-001 §3.

### Step 3b — `/method`

Plan-001 §4b. Draft as copy-review blocks M1…Mn; preview at `public/method.html` listed in
`.assetsignore` until ruled. **A new top-level page needs its own nav link on all eight
pages. Ask Thomas where it goes** (its own menu item, or in the sub-menu).

The rules table comes from receipts-001 §6, **OK rows only**. A script counted which of its
rows are OK (2026-09-24):

| Rule (receipts-001 §6) | OK rows |
|---|---|
| Measure the thing itself, not a proxy | R-019, R-024, R-050, R-062, R-129 |
| "Verified", "clean", "deployed" are claims | R-007, R-028 |
| The checker can be wrong too — test the test | R-045, R-061 |
| Say what you read, not what exists | R-029, R-080, R-089, R-091 |
| A quote is verbatim or it is empty | R-075 |
| A recommendation, a premise or a summary is a hypothesis | R-072, R-085 |
| Don't invent dates, figures or entities — ask | R-022, R-140 |
| **No selling** | **none: all six rows are CUT.** Ask Thomas before this rule appears. |
| One copy of each fact | R-007, R-110, R-111 |
| An extracting reader doesn't adjudicate | R-070, R-071 |

Rules on these rows:
- **F-2:** never name the outside research model.
- **F-3:** counts only rounded.
- **Reports Clustering receipts are in a private repo,** so they link to receipts-001, not
  to the source file.
- **Re-open and tick each row before quoting it.**

### After Phase 1

Phase 2 (build ledger) and Phase 3 (the motion/accessibility-controls proposal) per PL-6.
**Propose before building.**
