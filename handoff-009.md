# handoff-009 — tc-ventures.ca

**Written:** 2026-09-19
**Covers:** everything in handoff-008 reaching the live site, plus two new
project write-ups and the four-site briefs.
**Status at wrap:** **deployed and verified live.** The Rocket Lander is gone
from the public site, the favicon is real, and the projects page carries three
projects.

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. §2 "Traps" before you touch git or a rebuild.
2. `claude/thomas-study.md` in the Claude project "TC 'Ventures" — the voice
   study. Read it before writing any copy in Thomas's voice.
3. `claude/tc-ventures-site-decisions.md` in the same project — the decisions
   that should not be re-argued, including the two exceptions ruled this week.
4. `reviews/copy-review-001.md` — his rulings on every block of site copy.
5. `README.md`.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**Standing rule, ruled 2026-09-19:** the Rocket Lander is **private**. Not on
this site, not in copy, not in a meta tag, and assume its repo stays unpublished
until Thomas says otherwise.

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
| Pages | `index`, `projects`, `background`, `contact`, `404` |
| Projects on the page | The Economic Report Influence Graph · The Back Quarter · The Desk and the Drawer · then the four live sites |
| Graph demo | `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js` |
| Icons | `public/favicon.svg` (paths, not text) + `public/apple-touch-icon.png`, linked from all five pages |
| Scratch | `_to_delete/` at repo root — Cowork cannot delete files, so disposables go there |

## 2. What was done (2026-09-19)

All of it is **live and verified** by fetching the pages.

- **The Rocket Lander is off the site.** Article, home-page card, meta
  descriptions, and the page itself (`/lander.html` now 404s; the files sit in
  `_to_delete/`). His instruction: *"it is no good to mention anywhere."*
- **Real favicon** — a flat teal tile, T and C side by side, drawn as paths
  rather than a `text` element so it does not depend on an installed font. **No
  foot serif on the T**: with one it reads as an I at 16px. Thomas's catch.
  `apple-touch-icon.png` (180x180) ships beside it.
- **The Back Quarter** is project #2 (`#quarter`), **The Desk and the Drawer**
  is project #3 (`#desk`), and the home page says "Four things I have built".
- **The four-site section is four briefs**, not one paragraph. BYR carries
  **five** condition guides (Hajdu-Cheney, Erdheim-Chester, Fechtner, POEMS,
  stiff person) — counted off its own navigation, not from memory. GPRS now says
  plainly that the site is his donation to a board he sits on.
- **O-1 closed**: the rebuilt graph on thomascheesman.ca was already deployed;
  what was missing was the check. `corpus-data.json` resolves under the theme
  path and the host compresses it — 11.37 MB decoded, 3.93 MB on the wire.
- **The Back Quarter copy was rewritten again at the end of the day**, because
  the 3D build stopped being a beta and became the default (see thomascheesman.ca's
  `V0.42.md`). Nothing on this site says "beta" any more.

### Traps worth knowing

- **This site has no cache.** Its sister site has two (LiteSpeed *and*
  Hostinger's CDN), and a push there can deploy while the old HTML keeps
  serving. If a change to **thomascheesman.ca** seems not to have landed, fetch
  it with a query string (`/?cb=123`): if the new markup appears, it is purely
  cache. An incognito window proves nothing — the staleness is server-side.
- **Do not run git inside a Cowork mount.** It cannot unlink, so lock files are
  left behind. Read-only with `GIT_OPTIONAL_LOCKS=0` is fine.
- **Hostinger 403s scripted requests that carry an explicit `Accept-Encoding`
  header** while the same URL is 200 in a browser. Do not read that as "the file
  is missing".
- **Cowork cannot delete anything in a mount**, and cannot `mv` a *directory*.
  Files move fine. Hence `_to_delete/`.
- **Committing a file to the device re-encodes images.** Verify a committed
  image by staging it back, not by trusting the byte count.
- **The Facebook rule.** His public Facebook is linked from thomascheesman.ca.
  It is never material for this site.

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
  controls: read the input code.
- Hajdu-Cheney syndrome is named on purpose. Symptom detail is not.
- WordPress stays once per spec table as a hiring keyword; out of headline prose.
- **Nothing familial — with one ruled exception.** The Back Quarter write-up
  carries a short paragraph of Thomas's own childhood (the move north, the
  farms), because the world in that project *is* that country. It names no
  family member and no child. Everything else familial stays on
  thomascheesman.ca. **Children's names never appear here, including inside
  screenshots** — which is why the desk figure is cropped below the monitor.
- Edit `resume/resume-source.html` and re-render. Never edit the PDF. Exactly
  two pages.
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

### COPY
| # | Item | Notes |
|---|---|---|
| C-2 | Graph demo copy unread by Thomas | The demo block, the figure caption and the four-sites briefs are mine. |
| C-5 | **`page-hcs.php` arithmetic** (thomascheesman.ca) | Two years up the line then "kitchen manager for 10 years" lands in 2014, not 2013, now the Keg start is 2002. His number to rule on. Ask, do not guess. |
| C-7 | **The Back Quarter and Desk copy unread by Thomas** | Especially the childhood paragraph — it is his life on a hiring page, and the facts came from his own published prose, not from him directly this session. |

### PROJECTS
| # | Item | Notes |
|---|---|---|
| P-4 | Better first figure for The Desk | The monitor is the proof that the desk *is* the menu, and the current crop leaves it out because its contents rows name the children. A frame with the monitor showing the arcade, the cursor-trail drawer or the screensaver would swap straight in. |
| P-5 | The Back Quarter still may want reshooting | The hero promotion shipped on thomascheesman.ca the same day. The project figure is a daytime frame and still reads true, but a fresh one framed away from the treehouses is worth taking. |
| P-6 | A fourth project? | The graph, the farm and the desk are up. Nothing is queued — and per the "show finished work" rule, nothing goes up until it is done. |

### GRAPH
| # | Item | Notes |
|---|---|---|
| G-6 | Demo still is a headless render | If Thomas wants a hand-framed still of the gp-budget slice, he screenshots the live demo and it swaps in. |
| G-8 | No keyboard path into the 3D scene | Folded into A-1. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Full accessibility pass, site-wide** | Thomas asked for it. Not started, and it is now the biggest open item on this site. Its own session: keyboard order, focus states, landmarks, contrast in both themes, the canvas's text equivalent, the résumé PDF's tagging, and the alt text on the three new figures. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address within weeks. |
| INFRA-5 | `_to_delete/` folders | This repo: `gd-block.html`, `graph-demo.css`, `graph-everything.webp`, `lander.html`, `lander.js`. Reports Clustering: `dist-wp/`. Theme: the orphaned `index-ev_2RCV6.js` under `assets/report-graph/assets/` (2.4 MB, tracked, never fetched). |
| INFRA-6 | Dead lander CSS | The lander block in `public/assets/style.css` is unused and harmless; kept so restoring the page would be a file move. If it is still unused in a month, delete it. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | Harmless; detach when convenient. |
| D-2 | WP.com plan auto-renew | Do not cancel without confirming DNS for the live sites is unaffected. |
| D-3 | **Professional Email expiry ~2026-10-08** | About three weeks out. Thomas may renew out of convenience. |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-2 | `/projects` third-person leakage on thomascheesman.ca | **Thomas is writing this himself.** |
| O-4 | bareyourrare history contains `permits/` and `3.jpg` | Instructions in `_Quarantine\bareyourrare-history-purge.md`. Thomas runs it. Until then, treat the address as disclosed. |
| O-5 | `bareyr\.git` lock-file junk | Cosmetic; Thomas deletes. |
| O-6 | **Rocket Lander repo not public** | On hold with the rest of the lander. |
| O-7 | Children's names in the Back Quarter world | The 3D build signs the three treehouses with the kids' first names, against OD-1 in that theme's own spec, on a public indexed homepage. **Raised 2026-09-19; Thomas ruled: leave them.** Recorded so nobody "fixes" it. They stay off this site regardless. |
| O-8 | **thomascheesman.ca's own open items live in `V0.42.md`** in `tc-ventures-child-theme` | Two worth knowing here: `three-r128.min.js` is idle-loaded for every visitor including phones that now get the Painted Map, and the mouse wheel over a live stage does not scroll the page. |

**Closed this session:** the lander removal, the favicon, O-1, L-1, C-6, P-1,
P-3, INFRA-1, INFRA-2 — all live. **Killed or held by Thomas:** the lander's
public presence, R2 for the Godot build, O-6.

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

1. **Thomas reads the new copy** (C-7) — the childhood paragraph first. It is
   the one piece of this site that came from his prose rather than his mouth.
2. **The accessibility pass** (A-1) as its own session. It is the largest
   honest gap on a site whose own copy sells accessibility as a first-order
   requirement, and the three new figures need their alt text checked in it.
3. **C-5**, the "10 years" line. One question to Thomas.
4. **P-4**, a name-free frame of the desk monitor, whenever he takes one.
5. **D-3** before 8 October, if he wants to keep that mailbox.
