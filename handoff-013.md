# handoff-013 — tc-ventures.ca

**Written:** 2026-09-21
**Covers:** the end of the 2026-09-21 session after handoff-012: the O-9 Keg
paragraph fixed, the tagged résumé PDF served, both new figures, handoff-012's
work verified live — and **plan-001**, the plan to take this site from skeleton
to showcase.
**Status at wrap:** all site changes before plan-001 are pushed and verified
serving. The plan is written and approved (§6 of the plan); no building has started.

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
| Pages | `index`, `projects`, `background`, `contact`, `404` — restructure proposed in `plans/plan-001-showcase.md` |
| Projects on the page | The Economic Report Influence Graph · The Back Quarter · The Desk and the Drawer · then the four live sites |
| Plan | `plans/plan-001-showcase.md` — the rebuild from skeleton to showcase. Read it before any site work. |
| Graph demo | `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js` |
| Icons | `public/favicon.svg` (paths, not text) + `public/apple-touch-icon.png`, linked from all five pages |
| Scratch | **`_to_delete/` is gone.** Files can now be deleted outright — see §2. |
| Sister repo | `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` (thomascheesman.ca). Not connected by default; request access. |

## 2. What was done (2026-09-21, after handoff-012)

- **Verified live** after Thomas's push: tc-ventures.ca (tagged résumé PDF,
  byte-identical to his file; both new figures; graph keyboard path; contact
  status), bareyourrare.org (one `MedicalWebPage`, one `BreadcrumbList`, llms.txt
  link and robots line, privacy meta description, noindex on `/category/poems/`),
  theme script deleted (404). The live Desk figure was re-checked under a 6×
  contrast stretch: no names.
- **Résumé:** Thomas re-exported from Word with Save As PDF — tagged, `lang=en`,
  titled, two pages, text identical to the previous export. Served. Its home is
  `My Files\Family & Personal\resume\Thomas_Cheesman_Resume.pdf`.
- **O-9:** the Keg paragraph in `page-hcs.php` reordered at Thomas's request —
  "eleven years" moved to the end ("…and I ran it for the seven after that —
  eleven years at The Keg in all."). No facts changed. **Written, not deployed.**
- **plan-001** written at `plans/plan-001-showcase.md`. README updated: `plans/`
  listed, and the stale line that still named the lander in `projects.html` removed.

### Traps worth knowing

- **Figures Thomas pushes may not be byte-identical to what an agent committed** —
  the live webps differed in size from the files written this session (his
  pipeline re-saves them). Verify the *served* file visually, not by checksum
  against your own output.
- **A screensaver over the contents page is not enough to hide names** — the list
  showed through at about 2% brightness and was readable when zoomed. Stretch
  contrast on any screen-bearing screenshot before it ships.
- **`README.md` is public.** It named the lander until today. Grep the whole repo,
  not just `public/`, for anything under a privacy rule.
- Every trap in handoff-011 and handoff-012 §2 still stands.

## 3. Current design

Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
`prefers-color-scheme`. Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
Confirmed; stop re-litigating it.

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
| PL-1 | **plan-001 approved 2026-09-21** | `plans/plan-001-showcase.md` §6 holds his answers: lead role **nonprofit technology** (his instruction was "the one most likely to fit my skills and abilities"; he can overrule); home wow **A, the build ledger**; curated process excerpts **allowed**; **GPRS gets its own case study**; page-weight and accessibility results shown once inside `/work/this-site` by default, pending his word. |
| PL-2 | Session 1 of the plan: receipts inventory | Next. List every real "AI got it wrong / how caught" story with its file and date, from handoffs 001–013, `reviews/copy-review-001.md`, the Reports Clustering playbooks and validator, and the BYR audit. **Never invent one.** |

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
| A-1 | **Accessibility pass — deferred by Thomas (2026-09-21)** | He will do it when design and content are final; the site is a skeleton now. The code pass is done (axe 0 violations, graph keyboard path, focus handoff, live regions). Left for then: one real screen-reader run through Projects and the live graph. Do not raise it before he does. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address within weeks. |
| INFRA-6 | Dead lander CSS | The lander block in `public/assets/style.css` (from line 670) is unused and harmless; kept so restoring the page would be a file move. Delete it if still unused by mid-October 2026. |

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
| O-10 | **bareyourrare.org and thomascheesman.ca were moved behind Cloudflare on 2026-09-20** | Both were dropping connections from non-browser clients before HTTP — every Hostinger-hosted site on the account did, while Cloudflare-hosted tc-ventures.ca answered fine. Hostinger's own CDN is *inactive* on bareyourrare.org and gpresidentialsociety.com, so that was not the cause; the filtering is upstream, at the shared-hosting network layer, and nothing in hPanel touches it. Both zones now sit on `eoin`/`hazel.ns.cloudflare.com`, SSL **Full (strict)**, with Search/Agent/Training bot policies set to Allow. Mail records (MX, SPF, DMARC, DKIM) are DNS-only on both; bareyourrare.org's DKIM TXT had to be rebuilt by hand because Cloudflare's scanner skipped it. thomascheesman.ca's apex is a flattened CNAME to `thomascheesman.ca.cdn.hstgr.net` — Hostinger's CDN *is* active on that one, so it now has **three cache layers** (Cloudflare, Hostinger CDN, LiteSpeed). When markup there looks stale, purge all three. **gpresidentialsociety.com was not moved**: its domain is external, on `ns1/ns2.infotechdomains.com`, and Thomas does not control that account. |
| O-11 | **bareyourrare.org crawl audit — mostly written, not deployed** | Full audit: `Claude outputs/byr-crawl-audit.md`. **Deployed and verified live 2026-09-21:** (a) new `inc/guide-schema.php` emits a `MedicalWebPage` on each of the five guides with `author` (Thomas, as on the visible bylines), `lastReviewed`, `about`, publisher, dates; review dates now come from one function, `byr_guide_review_date()` in `inc/review-date.php`, which the visible "Last reviewed" line also reads; (b) the theme's own `BreadcrumbList` hooks (B11) removed from `functions.php` — Rank Math's, which has an `@id`, stays; (d) meta-description fallbacks for `/privacy/` and `/terms/` in new `inc/head-extras.php`, only used while the Rank Math field is empty or under 90 characters; (f) `llms.txt` linked from the head and named in the generated `robots.txt` (same file). All PHP lints clean. (e) needed nothing: the hero image already serves `alt=""`. (c) resolved without a decision: the audit was wrong to call `/category/poems/` poetry — it is an empty category (one unpublished post) serving a "can't find" page; `inc/head-extras.php` now noindexes any category archive with nothing published. **Still open:** (g) page weight. After deploy: purge caches, then check one guide's source for the `MedicalWebPage` block and a single `BreadcrumbList`, and fetch `/robots.txt`. |
| O-12 | **GPRS work has its own handoff** | Board reports, the fundraising drafts, the Cloudflare zone for gpresidentialsociety.com, SPF and Trevor: `GPRS Organization/00 Working Notes/gprs-handoff-001.md`. Not tracked here. |
| O-9 | **`page-hcs.php` Keg paragraph — final wording on disk, not deployed** | 2026-09-21: Thomas asked for the clause order fixed. "…and I would go on to give the place eleven years" moved out of the Power Engineering sentence; the paragraph now ends "…and I ran it for the seven after that &mdash; eleven years at The Keg in all." No facts changed. Live thomascheesman.ca/hcs still shows the older version until the theme is pushed and all three caches purged. |


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

1. **Plan session 1:** the receipts inventory (PL-2) — including GPRS, now a case study.
2. **Plan session 2:** design system and the case-study template.
3. **Thomas pushes the theme** for the O-9 paragraph and purges all three
   thomascheesman.ca caches; verify /hcs serves it.
4. **D-3:** confirm the Professional Email renewal is paid before 8 October.
