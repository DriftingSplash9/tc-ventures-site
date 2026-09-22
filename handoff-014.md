# handoff-014 — tc-ventures.ca

**Written:** 2026-09-21
**Covers:** plan-001 **session 2** — the design system (tokens, lanes, components)
and the case-study template, built on one page with placeholder copy. Session 1
(the receipts inventory) was **skipped at Thomas's choice** and is still open.
**Status at wrap:** written to disk, verified in a headless browser at three widths
and both colour schemes, HTML-validated. **Not deployed.** Thomas has not yet looked
at it or said yes/no.

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. §2 "Traps" before you touch git, grep, DNS or a rebuild.
2. **`plans/plan-001-showcase.md`** — the current plan for this site. Nothing gets built
   outside it without Thomas agreeing.
3. `claude/thomas-study.md` in the Claude project "TC 'Ventures" — the voice study.
4. `claude/tc-ventures-site-decisions.md` in the same project.
5. `reviews/copy-review-001.md` — his rulings on every block of site copy, and the
   format to use for the next review.
6. `README.md`.
7. If the job is GPRS, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md` instead.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**.

---

## 1. What this is

**tc-ventures.ca** — Thomas Cheesman's hiring-facing portfolio. Hand-written
static HTML, no framework, no build step, no CMS. Cloudflare Workers static
assets, deploy-on-push from GitHub. Deliberately separate from thomascheesman.ca.

| | |
|---|---|
| Repo | `DriftingSplash9/tc-ventures-site` — public |
| Local | `C:\Users\thoma\Desktop\My Files\Website Projects\tc-ventures site` |
| Host | Cloudflare Worker `tc-ventures-site` (static assets only) |
| Config | `wrangler.jsonc` → serves `./public`, `404-page`, `workers_dev: false`, `preview_urls: false` |
| Deploy | commit + push to `main` → Cloudflare builds. **No cache to purge** — unlike the WordPress sites. |
| Contact email | `thomas@tc-ventures.ca` |
| Pages | `index`, `projects`, `background`, `contact`, `404` — plus **`public/work/_template.html`** (session 2, unlinked, noindex) |
| Projects on the page | The Economic Report Influence Graph · The Back Quarter · The Desk and the Drawer · then the four live sites |
| Plan | `plans/plan-001-showcase.md` — the rebuild from skeleton to showcase. Session 2 done, session 1 open. |
| Design system | `public/assets/style.css` — tokens in `:root` (`--s-*`, `--t-*`, `--lane-*`), components under the `CASE STUDIES` banner at the end of the file |
| Graph demo | `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js` |
| Icons | `public/favicon.svg` (paths, not text) + `public/apple-touch-icon.png`, linked from all five pages |
| Sister repo | `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` (thomascheesman.ca). Not connected by default; request access. |

## 2. What was done (2026-09-21, after handoff-013)

Thomas asked to "pimp up" the site; offered session 1 (receipts) or session 2
(design) of plan-001; **he chose session 2**. Nothing else was touched.

- **`public/assets/style.css`** — additive only. Two things changed:
  1. `:root` gained the scales from plan §4d: spacing `--s-1`…`--s-9` (4px base),
     type `--t-label`…`--t-h1` (fixed for mono, fluid `clamp()` for display), lanes
     `--lane-read` (66ch) / `--lane-wide` (1040px) / `--lane-page` (1280px) / `--rail`
     (200px), and rhythm `--block` / `--section`. Values equal what the pages already
     used, so nothing moved.
  2. A `CASE STUDIES` block appended at the end: `.wrap--page`, `.cs-layout` (main
     lane + sticky side rail ≥1180px), `.cs-head` + `.cs-head__meta` + `.tag`,
     `.cs-index` (on-this-page, numbered), `.cs-section` + `.cs-section__num`
     (auto-numbered `01 — THE ASK` etc.), `.receipt` (inline mark) + `.receipts`
     (closing list), `.shot--fixed` / `.shot--paper` / `.shot--pair` + numbered
     `Fig.` captions (scoped to `.cs-body`), `.rules` (table, stacks under 640px via
     `data-th`), `.pull` (his words), `.excerpt` (curated slice of a working file),
     `.mc` / `.mc--catch` (misses M1–M3 paired with catches C1–C3), `.loop` (inline
     SVG diagram, theme-aware, scrolls sideways on phones), `.draft` (banner), `.work`
     (the future `/work/` index rows).
  - **Regression-checked:** `index.html` and `projects.html` rendered pixel-identical
    with the old and new stylesheet at 1400px and 390px. `stylelint` clean.
- **`public/work/_template.html`** — the case-study template, all six fixed sections
  in order, every component used once. Sample copy is a **draft of `/work/this-site`**
  written from handoff-013 §2–§3, plan-001 and brief-001 — real facts only, square
  brackets where a ruling still needs confirming. **Not reviewed by Thomas. Not
  linked. Not in the sitemap. `noindex, nofollow`.** A black "Template" banner sits
  above the top bar; delete the `.draft` element when copy is ruled on. Nav is the
  live one (Projects / Background / Contact), because `/work/` and `/method` do not
  exist yet and a link that 404s is banned. `html-validate` clean.
- Verified with headless Chromium at 1400 / 1000 / 390px, light and dark; no console
  errors, no failed requests. Screenshots were shown to Thomas in chat, not committed.

### Traps worth knowing

- **`.cs-section > *` is deliberately one class of specificity.** It sets the reading
  lane on every child; `.wide` opts out; `.cs-section h2` (0,1,1) must still win for
  its 24ch cap. Writing it as `> :not(.wide)` (0,2,0) silently broke the h2 width.
- **The on-this-page index is in the HTML twice** (inline under the header, and in
  the rail). CSS displays exactly one at any width. Don't add `aria-hidden` or
  `tabindex="-1"` to either — that hid the only visible copy from AT at desktop.
- **`loading="lazy"` images render black in a full-page headless screenshot** unless
  you scroll the page first and `await img.decode()`. Not a site bug.
- **Anything with a bare `.shot figcaption::before` leaks onto `projects.html`.**
  Case-study-only styling must be scoped under `.cs-body`.
- **`briefs/brief-001…md` names the lander and carries exact node/edge counts.** It is
  in the public repo and the template links to it as a receipt. Thomas's call whether
  that file stays as-is, gets a redaction, or the receipt points elsewhere.
- Every trap in handoff-011, -012 and -013 §2 still stands.

## 3. Current design

Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
`prefers-color-scheme`. Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
Confirmed; stop re-litigating it.

**Layout, as of session 2 (pending Thomas's yes/no):** case studies use a wide lane
(1040px) for headers, figures, tables and lists, a reading lane (66ch) for prose,
and a sticky side rail (200px) on screens ≥1180px carrying the six-section index.
Below that the rail folds into a horizontal index under the header. Sections are
auto-numbered from CSS counters; figures are numbered `Fig. N` per page. Receipts are
small mono links with a leading `→`, the same everywhere.

**Standing rules:**
- **The Rocket Lander is private.** Not here, in any form.
- `object-fit: contain`, never `cover`.
- Content must render without JavaScript. JS allowed; dependencies and a build
  step are not — prebuilt bundles copied into `assets/` only.
- Fonts self-hosted. No third-party font request.
- No phone number on the site. It is in the résumé PDF.
- **Never publish an exact node, edge, report or grade count** *in copy*. Round
  or describe. The application screenshot on Projects is the one ruled exception.
- **No vanity metrics.** No line counts.
- **Do not invent dates or figures.** Unknown → ask Thomas. This includes game
  controls: read the input code. C-5 is the model: the number came from him, not
  from arithmetic on the prose.
- Hajdu-Cheney syndrome is named on purpose. Symptom detail is not.
- WordPress stays once per spec table as a hiring keyword; out of headline prose.
- **Nothing familial — with one ruled exception.** The Back Quarter write-up
  carries a short paragraph of Thomas's own childhood (the move north, the
  farms), because the world in that project *is* that country. It names no
  family member and no child. Everything else familial stays on
  thomascheesman.ca. **Children's names never appear here, including inside
  screenshots** — which is why the desk figure is cropped below the monitor.
- **The résumé source is the Word file** `resume/Thomas-Cheesman-Resume-source.docx`;
  Thomas exports the PDF himself. `resume/resume-source.html` is a content mirror of
  it (synced 2026-09-21) — if one changes, change the other. Never edit the PDF.
  Exactly two pages.
- Melanie and Thomas are "the parents" of the three children, never "co-parents".
- **New CSS is additive and token-based.** Pick from `--s-*` / `--t-*`; do not type
  new pixel values. Anything case-study-only is scoped under `.cs-body` or `.cs-*`.
- **Never ship a link that 404s** — including nav links to pages that are planned
  but not built.
- **Template copy is not site copy.** Anything in `_template.html` ships only after
  a copy review in the `copy-review-001` format.

**Demo and embed rules:**
- **Nothing heavy loads before a click.** The graph renderer is 1.3 MB and gated.
- **A gated page must degrade when the payload is absent.** Never ship a button
  that 404s.
- **The 3D canvas keeps its own dark ground in both themes.**
- **`basis` is quoted, never paraphrased** in the graph demo.
- **The written chain under the graph demo is the accessible equivalent**, not
  decoration.
- **Nothing rearranges a layout on interaction.**
- **Show finished work.** He is job hunting. Unfinished work is labelled
  honestly or left off — that is why the lander went.

## 4. Open items — carry these forward until closed

### PLAN
| # | Item | Notes |
|---|---|---|
| PL-1 | **plan-001 approved 2026-09-21** | `plans/plan-001-showcase.md` §6 holds his answers: lead role **nonprofit technology** (he can overrule); home wow **A, the build ledger**; curated process excerpts **allowed**; **GPRS gets its own case study**; page-weight and accessibility results shown once inside `/work/this-site` by default, pending his word. |
| PL-2 | Session 1: receipts inventory — **still open, skipped in favour of session 2** | List every real "AI got it wrong / how caught" story with its file and date, from handoffs 001–014, `reviews/copy-review-001.md`, the Reports Clustering playbooks and validator, and the BYR audit. **Never invent one.** |
| PL-3 | **Session 2 built, awaiting Thomas's yes/no** | `public/work/_template.html` + the CSS block. He needs to look at it (locally or after a push — it is unlinked and noindexed) and rule on layout, rail, numbering, receipts style, loop diagram. Then session 3 (Method page) or session 1. |
| PL-4 | Sample copy in the template carries `[Confirm …]` brackets | Three rulings to confirm before any of it is reused: how he'd phrase "the ask" for this site; that "Available now" was softened to "open to work" on his ruling (Q1 in copy-review-001); the "honest limits" wording. |
| PL-5 | `brief-001` as a public receipt | See §2 traps. Decide before the this-site case study ships. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-9 | **`page-thomas.php` ~2010: "I couldn't get past my kitchen manager"** | Reads oddly now that he was the kitchen manager from ~2006. It may mean the senior manager above him. His prose and his call — flag it, do not rewrite it. |
| C-11 | **Education, settled by Thomas 2026-09-20** | Four academic years at GPRC (now Northwestern Polytechnic), fall 1999 to spring 2003: **B.Sc. Pre-Pharmacy credits, 1999–2002** (three academic years), then **Power Engineering 4th Class and Class 3B plus Gas Plant Operations Levels I and II, 2002–2003**. Journeyman Chef, Red Seal, SAIT, 2012. The rebuilt .docx carries exactly this. `resume/resume-source.html` already has the B.Sc. span right; what it lacks is the Power Engineering dates, Class 3B and the college's name (see C-8 on the render path). |

### PROJECTS
| # | Item | Notes |
|---|---|---|
| P-6 | A fourth project? | Nothing is queued — and per the "show finished work" rule, nothing goes up until it is done. |

### GRAPH
| # | Item | Notes |
|---|---|---|
| G-6 | Demo still is a headless render | If Thomas wants a hand-framed still of the gp-budget slice, he screenshots the live demo and it swaps in. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Accessibility pass — deferred by Thomas (2026-09-21)** | He will do it when design and content are final; the site is a skeleton now. The code pass is done (axe 0 violations, graph keyboard path, focus handoff, live regions). Left for then: one real screen-reader run through Projects and the live graph. Do not raise it before he does. The template's scrollable loop diagram (`.loop__scroll`, `tabindex="0"`, `role="group"`) is a candidate for that run. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address within weeks. |
| INFRA-6 | Dead lander CSS | The lander block in `public/assets/style.css` (search `lander embed`) is unused and harmless; kept so restoring the page would be a file move. Delete it if still unused by mid-October 2026. |
| INFRA-7 | `public/work/_template.html` will be served if pushed | Unlinked and `noindex`, so harmless, but it is a public URL. Move it out of `public/` (e.g. `templates/`) or delete it once the first real case study exists. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | Harmless; detach when convenient. |
| D-2 | WP.com plan auto-renew | Do not cancel without confirming DNS for the live sites is unaffected. |
| D-3 | **Professional Email renewal — Thomas said renew (2026-09-21)** | It is subscription 27350377, CA$48/yr, **on the gpresidentialsociety.wordpress.com site**, auto-renew off, expires 2026-10-08. Renewal checkout link given to him: `https://wordpress.com/checkout/renew/27350377`. Not paid until he completes it — confirm before 8 October. |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-2 | `/projects` third-person leakage on thomascheesman.ca | **Thomas is writing this himself.** |
| O-4 | bareyourrare history contains `permits/` and `3.jpg` | Instructions in `_Quarantine\bareyourrare-history-purge.md`. Thomas runs it. Until then, treat the address as disclosed. |
| O-5 | `bareyr\.git` lock-file junk | Cosmetic; Thomas deletes. |
| O-6 | **Rocket Lander repo not public** | On hold with the rest of the lander. |
| O-7 | Children's names in the Back Quarter world | The 3D build signs the three treehouses with the kids' first names, against OD-1 in that theme's own spec, on a public indexed homepage. **Raised 2026-09-19; Thomas ruled: leave them.** Recorded so nobody "fixes" it. They stay off this site regardless. |
| O-8 | **thomascheesman.ca's own open items live in `V0.42.md`** in `tc-ventures-child-theme` | Two worth knowing here: `three-r128.min.js` is idle-loaded for every visitor including phones that now get the Painted Map, and the mouse wheel over a live stage does not scroll the page. |
| O-9 | **`page-hcs.php` Keg paragraph — final wording on disk, not deployed** | 2026-09-21: clause order fixed at Thomas's request; the paragraph now ends "…and I ran it for the seven after that &mdash; eleven years at The Keg in all." No facts changed. Live thomascheesman.ca/hcs still shows the older version until the theme is pushed and all three caches purged. |
| O-10 | **bareyourrare.org and thomascheesman.ca were moved behind Cloudflare on 2026-09-20** | Both were dropping connections from non-browser clients before HTTP — every Hostinger-hosted site on the account did, while Cloudflare-hosted tc-ventures.ca answered fine. Hostinger's own CDN is *inactive* on bareyourrare.org and gpresidentialsociety.com, so that was not the cause; the filtering is upstream, at the shared-hosting network layer, and nothing in hPanel touches it. Both zones now sit on `eoin`/`hazel.ns.cloudflare.com`, SSL **Full (strict)**, with Search/Agent/Training bot policies set to Allow. Mail records (MX, SPF, DMARC, DKIM) are DNS-only on both; bareyourrare.org's DKIM TXT had to be rebuilt by hand because Cloudflare's scanner skipped it. thomascheesman.ca's apex is a flattened CNAME to `thomascheesman.ca.cdn.hstgr.net` — Hostinger's CDN *is* active on that one, so it now has **three cache layers** (Cloudflare, Hostinger CDN, LiteSpeed). When markup there looks stale, purge all three. **gpresidentialsociety.com was not moved**: its domain is external, on `ns1/ns2.infotechdomains.com`, and Thomas does not control that account. |
| O-11 | **bareyourrare.org crawl audit — mostly deployed** | Full audit: `Claude outputs/byr-crawl-audit.md`. Deployed and verified live 2026-09-21: `MedicalWebPage` schema on the five guides via `inc/guide-schema.php`; review dates from `byr_guide_review_date()` in `inc/review-date.php`; theme `BreadcrumbList` hooks removed (Rank Math's stays); meta-description fallbacks for `/privacy/` and `/terms/` in `inc/head-extras.php`; `llms.txt` linked and in `robots.txt`; empty category archives noindexed. **Still open:** (g) page weight. |
| O-12 | **GPRS work has its own handoff** | `GPRS Organization/00 Working Notes/gprs-handoff-001.md`. Not tracked here. |

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

## 6. Next up

In order:

1. **Thomas looks at `public/work/_template.html`** (open the file locally, or push
   and visit `/work/_template` — unlinked, noindexed) at desktop and phone width, in
   both colour schemes, and rules on it: layout, rail, numbering, receipts style, the
   loop diagram, the miss/catch pairing. Anything he wants changed is changed
   before a single real case study is written from it.
2. **PL-4 / PL-5:** the three bracketed confirmations and the brief-001 question.
3. **Plan session 1** (PL-2, the receipts inventory) — it feeds sessions 3–5 and is
   the reason no case study can be written yet.
4. **Plan session 3:** the Method page, on the template's components.
5. **Thomas pushes the theme** for the O-9 paragraph and purges all three
   thomascheesman.ca caches; verify /hcs serves it.
6. **D-3:** confirm the Professional Email renewal is paid before 8 October.
