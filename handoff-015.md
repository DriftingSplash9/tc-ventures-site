# handoff-015 — tc-ventures.ca

**Written:** 2026-09-22
**Covers:** a baseline site audit (given in chat), then **Phase 0** of the action plan
from it: clean URLs, security headers, a real link-preview image, the template taken
off the live site, and a copy review of the home page's first screen.
**Status at wrap:** Phase 0 **deployed and verified live** (Thomas pushed mid-session).
Later in the session, and **on disk, not yet deployed**: copy-review-002 rulings applied
to the home page, the CSP fix for Cloudflare's analytics beacon, the re-rendered card,
the template brackets resolved, and brief-001 redacted.

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
| Pages | `index`, `projects`, `background`, `contact`, `404`. Internal links, canonicals and sitemap use **clean URLs** (`/projects`, not `/projects.html`). `public/work/_template.html` is local-only (`.assetsignore`) |
| Headers | `public/_headers` — CSP, HSTS, nosniff, frame, referrer, permissions, COOP; fonts cached a year |
| Link preview | `assets/img/og-card.png` 1200×630, all four pages. Source `public/og-src/og.html` (not deployed); re-render command is in its `<style>` comment |
| Projects on the page | The Economic Report Influence Graph · The Back Quarter · The Desk and the Drawer · then the four live sites |
| Plan | `plans/plan-001-showcase.md` — the rebuild from skeleton to showcase. Session 2 done, session 1 open. |
| Design system | `public/assets/style.css` — tokens in `:root` (`--s-*`, `--t-*`, `--lane-*`), components under the `CASE STUDIES` banner at the end of the file |
| Graph demo | `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js` |
| Icons | `public/favicon.svg` (paths, not text) + `public/apple-touch-icon.png`, linked from all five pages |
| Sister repo | `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` (thomascheesman.ca). Not connected by default; request access. |

## 2. What was done (2026-09-22, after handoff-014)

Thomas asked for a brutally honest audit and a plan to make the site "Awwwards
worthy". The audit was given in chat. Baseline (rough, Awwwards weights): Design 5,
Usability 7, Creativity 3.5, Content 7, about **5.3 overall**. The action plan
(Phases 0–4) **slots into plan-001**; it does not replace it. Headline findings: the
site still describes the method without showing it; the home page undersells ("for
practice") and names four roles; the planning is well ahead of what has shipped.
Recommended direction, **not yet ruled by Thomas**: "Awwwards-grade craft within the
standing rules" (CSS View Transitions, scroll-driven CSS, the build ledger as the
home hero), not a WebGL agency showreel. He then said "start with phase 0".

- **Clean URLs.** Live Cloudflare answers `/x.html` with a **307** to `/x`. Every nav
  link, canonical, `og:url` and sitemap entry pointed at the redirecting form. All
  now use `/projects`, `/background`, `/contact` (index, projects, background,
  contact, 404, template, sitemap).
- **`public/_headers`** (new). Policy and the reasons are commented in the file.
- **Contact's inline `<script>` moved** verbatim to `public/assets/contact.js`
  (`defer`), so the CSP needs no inline-script allowance.
- **`public/.assetsignore`** (new): `work/_template.html`, `og-src/`. The template is
  now **local-preview only**, so INFRA-7 is closed. Push makes `/work/_template` a 404.
- **Link preview:** `assets/img/og-card.png` (1200×630, light paper, the gp-budget
  graph still, `contain`), with `og:image:width/height/alt`, replacing the `.webp`
  UI screenshot on all four pages. Card copy is existing ruled copy only.
- **`reviews/copy-review-002.md`** (new): home title, H1, lede, body, "looking for"
  band, as blocks R1–R6 with A/B options, plus Q1 (GPRS site "since 2023"?) and Q2
  (LinkedIn URL?). **No site copy was changed.** Later the same session Thomas
  answered both: Q1 yes (see C-13), and Q2 gave the URL. **LinkedIn is now in the
  footer's Elsewhere list on all six pages**, which is the only copy change.
- `README.md` tree updated.
- **Verified locally** (Node server in scratchpad applying `_headers` minus HSTS and
  upgrade-insecure-requests): the live 3D graph loads and renders under the CSP with
  no console errors; contact's local time and copy button work; fonts load; 404
  renders; every internal `href`/`src`/`content` path on every page returns 200.
  **Not verified:** the headers on live Cloudflare (needs a push), or the LinkedIn
  and Facebook preview debuggers.

**Second half of the session (after Thomas's rulings):**

- **Phase 0 verified live:** all seven headers served, `/projects` 200 with no
  redirect, `/work/_template` + `/og-src/` + `/_headers` + `/.assetsignore` all 404,
  fonts `immutable`, and the live graph renders under the CSP.
- **Found live: the CSP was blocking Cloudflare Web Analytics.** Cloudflare injects
  `static.cloudflareinsights.com/beacon.min.js` at the edge, so a local server never
  sees it. Analytics were silently off from the Phase 0 push. `_headers` now allows
  `https://static.cloudflareinsights.com` (script) and `https://cloudflareinsights.com`
  (connect). **On disk, needs a push.**
- **copy-review-002 applied** to `index.html`: R1 A (title + og:title), R2 A (name
  moved to the label; H1 is the sentence; `.hero h1 { max-width: 20ch; }` added to
  `style.css`), R3 OK, **R4 in Thomas's own words**, R5 OK, R6 OK (both sentences).
  Meta and og descriptions rebuilt from the ruled sentences only. The one edit to his
  R4 text: "straight forward" to "straightforward". The card (`og-card.png`) was
  re-rendered with the R2 sentence, because its old line was the pre-R4 wording.
- **Template approved** (PL-3: "yes"). The four `[Confirm...]` brackets are resolved:
  "the ask" rewritten as a suggestion (he said FIX, asked for one); both halves of
  the "available now" miss/catch pair state the fact once (handoff-002 records the
  change to "open to work"); "honest limits" OK as written.
- **brief-001 redacted** for use as a receipt: the lander bullet, the exact counts, and
  "hand and arm pain" (symptom detail, against the Hajdu-Cheney rule) replaced with
  `[redacted: ...]` markers, with a dated note at the top. **Git history still has the
  original**; the redaction is presentation, not secrecy.
- **Resume:** Thomas attached `Family & Personal\resume\Thomas Cheesma1.docx`. It is
  dated **April 2025**, an old version (lists "basic Java", no tc-ventures.ca,
  and it names his former caregiving client). Neither file was touched. See C-15.

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
- **The 3D graph bundle contains `new Function`** (ngraph layout). The default d3
  engine never calls it, so `script-src 'self'` holds. If the graph ever throws an
  EvalError, that is why. Do not add `'unsafe-eval'` without checking first.
- **Headless Chrome renders dark mode** and the site stylesheet recolours the text.
  That is why `og-src/og.html` declares only `@font-face` and does not link `style.css`.
- **An HTML comment inside `<style>` silently kills the next CSS rule.** Cost one
  re-render.
- **Any new inline `<script>` will be blocked by the CSP.** Put it in `/assets/*.js`.
- **Cloudflare injects scripts at the edge** (Web Analytics beacon), so a CSP that passes
  on a local server can still break things live. After any CSP change, load the live
  site and read the console.
- **`_template.html` had four `[Confirm...]` brackets, not three.** The miss/catch pair
  on "available now" carried one each. Grep, don't count from memory.
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
| PL-6 | **Audit action plan, 2026-09-22; direction RULED** | Thomas: **"Awwwards - novel designs and motions, it needs all the accessibility toggles, I don't want a generic app like A11y taking over the features."** So: novel design and motion are in scope (Phase 3 grows). Accessibility controls are **built into the site**, never a third-party overlay widget. OS preferences (reduced motion, colour scheme, contrast) are the defaults; on-page toggles override them and persist. Standing rules still hold: the words render without JS, heavy things load on demand. Phase 1 (receipts, two case studies, `/method`) still comes before Phase 3. |
| PL-1 | **plan-001 approved 2026-09-21** | `plans/plan-001-showcase.md` §6 holds his answers: lead role **nonprofit technology** (he can overrule); home wow **A, the build ledger**; curated process excerpts **allowed**; **GPRS gets its own case study**; page-weight and accessibility results shown once inside `/work/this-site` by default, pending his word. |
| PL-2 | Session 1: receipts inventory — **still open, skipped in favour of session 2** | List every real "AI got it wrong / how caught" story with its file and date, from handoffs 001–014, `reviews/copy-review-001.md`, the Reports Clustering playbooks and validator, and the BYR audit. **Never invent one.** |
| PL-3 | **Template approved by Thomas 2026-09-22** | Layout, rail, numbering, receipts, loop diagram, miss/catch: yes. Copy in it still ships only through a copy review. |
| PL-4 | Template brackets resolved; **"the ask" paragraph is Claude's suggestion** | Thomas said FIX and asked for a suggestion. The new wording is in `_template.html` section 01. Confirm it in the `/work/this-site` copy review. |
| PL-5 | brief-001 **redacted 2026-09-22** (Thomas: "redact") | The current file is clean; the git history is not. Only a history rewrite would change that, and nobody has asked for one. |

### COPY
| # | Item | Notes |
|---|---|---|
| C-12 | **Closed: copy-review-002 live 2026-09-22** | Flagged to Thomas, his call: R4 "build it with help writing by AI" could read as AI writing the words rather than the code. Offer "...with AI writing the code"; do not change it unasked. |
| C-13 | **GPRS site history, from Thomas 2026-09-22** | First version on WordPress.com in 2023; rebuilt in 2025 as self-hosted WordPress.org on Hostinger, for more freedom to experiment with the code. For `/work/gprs`. Do not add month-level dates without asking. |
| C-15 | **Resume updated 2026-09-22** | Thomas confirmed the live PDF is the one to use (identical to `public/assets/Thomas-Cheesman-Resume.pdf`, exported from the repo docx). The docx summary now follows R3 to R6; LinkedIn added to the contact line. Word test export: **2 pages**, contact line fits on one line; the summary ends on a one-word line ("roles."). `resume-source.html` mirrored. **Thomas exports the PDF** and replaces `public/assets/Thomas-Cheesman-Resume.pdf` and his `Family & Personal\resume\Thomas_Cheesman_Resume.pdf`. |
| C-16 | **Job history corrected by Thomas 2026-09-23** | GPRS board: elected at the June 2023 AGM (first meeting Sept), so **June 2023**. Majors consulting: May 2019 – **June 2020**. **Head Chef, Ric's Grill, Sep 2013 – Jul 2014**; **Executive Chef, Township 71, Jul 2014 – Jun 2015** (renovation from Oct 2014, opened Nov 2014, closed May 2015, wind-down through June). Taught one GPRC semester, **Sep – Dec 2014**, during the Ric's-to-T71 transition. The resume docx and `resume-source.html` were split into two entries 2026-09-23 (Word test export: 2 pages). LinkedIn fixes are Thomas's to enter; the draft is in `Family & Personal\resume\LinkedIn-profile-draft-2026-09-22.md` (private, not in this repo). |
| C-14 | LinkedIn on the resume: **done** (see C-15) | When structured data lands (Phase 4), the URL also goes in `Person.sameAs`. |
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
| INFRA-8 | **Closed 2026-09-22: verified live** | Headers, clean URLs, 404s, graph under CSP, and the analytics beacon now loads (200) under the updated CSP. Left for Thomas: paste the URL into LinkedIn's Post Inspector to refresh the cached preview. |
| INFRA-9 | HSTS is 1 year, no `includeSubDomains`, no `preload` | Deliberate: both are hard to undo. Revisit only if every subdomain is HTTPS-only. |

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

1. **Thomas exports the resume PDF** from the updated docx (C-15), replaces the copy in
   `public/assets/`, and pushes. Then he runs LinkedIn's Post Inspector.
2. (Done this session: INFRA-8, C-12, C-14.)
3. **Plan session 1** (PL-2, the receipts inventory).
4. The two case studies (`/work/gprs` with C-13, `/work/this-site`), then `/method`.
5. **Phase 3 design** per the PL-6 ruling: a proposal first (motion concept +
   accessibility-controls panel), built only after he says yes.
6. **Thomas pushes the theme** for O-9 and purges all three thomascheesman.ca caches.
7. **D-3:** Professional Email renewal paid before 8 October.
