# handoff-008 — tc-ventures.ca

**Written:** 2026-09-19
**Covers:** pulling the Rocket Lander off the public site, closing O-1, the real
favicon, and The Back Quarter written up as the second project.
**Status at wrap:** the lander is gone from `index.html` and `projects.html` and
its two files are parked in `_to_delete/` — **on disk, not live yet**. O-1 is
**closed, verified in a real browser**.

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. §2 "Traps" before you touch git or a rebuild.
2. `claude/thomas-study.md` in the Claude project "TC 'Ventures" — the voice study.
   Read it before writing any copy in Thomas's voice.
3. `reviews/copy-review-001.md` — his rulings on every block of site copy.
4. `briefs/brief-001-wow-and-contact.md` — the wow brief.
5. `README.md`.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly.

**One standing rule added this session:** the Rocket Lander is **not public**.
Thomas: *"it is no good to mention anywhere. the lander exists only between you
and me for now."* Do not put it back on any page, in any meta tag, or in any
copy, until he says so.

---

## 1. What this is

**tc-ventures.ca** — Thomas Cheesman's hiring-facing portfolio. Hand-written static
HTML, no framework, no build step, no CMS. Cloudflare Workers static assets,
deploy-on-push from GitHub. Deliberately separate from thomascheesman.ca.

| | |
|---|---|
| Repo | `DriftingSplash9/tc-ventures-site` — public |
| Local | `C:\Users\thoma\Desktop\My Files\Website Projects\tc-ventures site` |
| Host | Cloudflare Worker `tc-ventures-site` (static assets only) |
| Config | `wrangler.jsonc` → serves `./public`, `404-page`, `workers_dev: false`, `preview_urls: false` |
| Deploy | commit + push to `main` in GitHub Desktop → Cloudflare builds. No command to run. |
| Contact email | `thomas@tc-ventures.ca` |
| Pages | `index`, `projects`, `background`, `contact`, `404` — **`lander` removed** |
| Graph demo | `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js`; data from `scripts/export-gp-budget.py` |
| Scratch | `_to_delete/` at repo root — Cowork cannot delete files, so disposables go there |

**Hard limit that still shapes any embed:** Cloudflare Workers static assets cap
**individual files at 25 MiB**.

## 2. What was done (2026-09-19)

**The Rocket Lander is off the public site**, on Thomas's instruction. Written to
disk, not yet live:

| File | Change |
|---|---|
| `public/index.html` | Rocket Lander proof card removed; section heading is now "**Two** things I have built" |
| `public/projects.html` | the whole `#rocket` article removed; "Rocket Lander" out of `<meta name="description">`; "a rocket with real aerodynamics" out of `og:description`; lede now "**One** built in the open, in detail — what **it is**…"; the "And four live sites" section takes `band--tint` so the light/tint alternation still holds with one project band above it |
| `public/lander.html` → `_to_delete/lander.html` | moved, so the URL stops existing |
| `public/assets/lander.js` → `_to_delete/lander.js` | moved |

Verified by grep: no case-insensitive match for "rocket" or "lander" remains in
`index.html` or `projects.html`. `sitemap.xml` never listed the lander page and
needed no change.

**O-1 is closed.** The rebuilt graph was already committed **and** already on the
live site — no upload was needed, only the verification the last handoff asked
for. Checked in Thomas's Chrome on `https://thomascheesman.ca/reports-graph`:

- `index-DPd_1gmX.js` (the rebuilt hash) — 200.
- `corpus-data.json` — **200 from under the theme path**, which is the bug the
  rebuild fixed. It resolves.
- **The host does compress it.** 11,372,275 bytes decoded, 3,932,449 encoded on
  the wire — about a 65% saving, so the ~11 MB figure that worried the last
  handoff is really ~3.9 MB over the network.
- Page renders: the intro overlay ("The graph opens folded") and the graph
  behind it. **No console errors.**

**The favicon is real now (INFRA-2 closed).** Thomas brought two candidate logos
(a blue gradient wordmark and a chrome-and-neon 3D render); both die at 16px —
overlapping words turn to noise, photoreal chrome turns to mud, and the blue
fights `#0F5F6B`. The mark under them (T and C in a ring) survived: four flat
teal treatments were drawn and rendered at 128/48/32/16 on light and dark tab
strips, and Thomas picked **T and C side by side, no outer ring**.

- `public/favicon.svg` — rewritten. **Paths, not a `text` element.** The old one
  set "TC" in Familjen Grotesk, which is not installed on most machines, so it
  rendered in whatever the system substituted. Paths render identically everywhere.
- **The T has no foot serif.** With one it reads as an I — the stem is then
  symmetrical top and bottom. The crossbar carries the weight instead. This was
  Thomas's catch, and it is the whole difference between the mark working and not.
- `public/apple-touch-icon.png` — 180x180, rendered from the same SVG, linked
  from all five pages. Verified on disk as a valid 180x180 PNG after the commit
  re-encoded it.

**The Back Quarter is project #2.** Thomas's call, and he corrected the framing:
it is not "the 3D menu" — it is a game, and it is the country he grew up in. Added
as `#quarter` on `projects.html`, plus a third proof card on `index.html`
("Three things I have built" again). Lead is the 3D build, labelled beta, per his
ruling. `public/assets/img/back-quarter-3d.webp` is his own daytime screenshot,
1600x900.

Facts in that copy came from the theme repo, not invention: the vehicle-handling
notes and the bloom/day-factor regression from `assets/js/back-quarter-3d.js` and
`V0.40.md`, the fire-synthesis rewrite from the same header, the Pixi/Matter
load-on-engage contract from `assets/js/back-quarter.js`, and the landmark list
from `docs/QUARTER-SECTION-SPEC.md`. **The biography in paragraph two is from his
own published prose** (Peace Country at ten; Teepee Creek bird farm, LaGlace, the
pig farm, Little Smokey with no gas, a wood furnace, a rabbit trapline). If any
of that is wrong it is a factual error on a hiring page — ask him, do not patch
it from memory.

**The four-site section is now four briefs, not one paragraph.** BYR carries
**five** condition guides, not "three or four" — Hajdu-Cheney, Erdheim-Chester,
Fechtner, POEMS, stiff person — counted off the live site's own navigation. GPRS
now says plainly that the site is his donation to the society he sits on the board
of. thomascheesman.ca points up at The Back Quarter instead of describing it twice.

### Traps worth knowing

- **Do not run git inside a Cowork mount.** It cannot unlink, so `index.lock`
  and ref locks are left behind. Read-only with `GIT_OPTIONAL_LOCKS=0` is fine —
  that is how this session read the theme repo's state — but nothing that writes.
- **CRLF hazard in `tc-ventures-child-theme`** (not this repo): working tree is
  CRLF, repo stores LF. A non-Windows git with `autocrlf` unset sees every text
  file as modified. Set `core.autocrlf true` before staging anything there.
- **Hostinger 403s some curl requests** that carry an explicit `Accept-Encoding`
  header, while the same URL is 200 in a browser and 200 from curl with default
  headers. Do not read a 403 from a scripted fetch as "the file is missing" —
  confirm in a real browser before writing it down. That cost this session
  three round trips.
- **Cloudflare rejects any static asset over 25 MiB.** The Godot `.wasm` is
  36.1 MiB. It cannot go in `public/`.
- **GitHub Desktop merges, it does not force-push.** Any history rewrite goes
  through the command line.
- **Cowork cannot delete anything in a mount**, and cannot `mv` a *directory*.
  Files move fine. Hence `_to_delete/`.
- **Committing a file to the device re-encodes images.** Verify a committed image
  by staging it back, not by trusting the byte count.
- **The Facebook rule.** His public Facebook is linked from thomascheesman.ca. He
  has ruled it "between you and me only" — never material for this site.

## 3. Current design

Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
`prefers-color-scheme`. Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
Confirmed; stop re-litigating it.

**Standing rules:**
- **The Rocket Lander is private.** Not on this site, not named in copy or meta.
- `object-fit: contain`, never `cover`.
- Content must render without JavaScript. JS allowed; dependencies and a build step
  are not — prebuilt bundles copied into `assets/` only.
- Fonts self-hosted. No third-party font request.
- No phone number on the site. It is in the résumé PDF.
- **Never publish an exact node, edge, report or grade count** *in copy*. Round or
  describe. One ruled exception: the application screenshot on Projects shows the
  app's own counters. The prose still rounds.
- **No vanity metrics.** No line counts.
- **Do not invent dates or figures.** Unknown → ask Thomas.
- Hajdu-Cheney syndrome is named on purpose. Symptom detail is not.
- WordPress stays once per spec table as a hiring keyword; out of headline prose.
- **Nothing familial, nothing from Facebook — with one ruled exception.** Thomas
  decided 2026-09-19 that The Back Quarter's write-up carries a short paragraph of
  his own childhood (the move north, the farms), because the world is that country
  and the project makes no sense without it. It names no family member and no
  child. That is the exception, not the new rule; everything else familial stays
  on thomascheesman.ca.
- Edit `resume/resume-source.html` and re-render. Never edit the PDF. Exactly two
  pages.
- Melanie and Thomas are "the parents" of the three children, never "co-parents".

**Demo and embed rules:**
- **Nothing heavy loads before a click.** The graph renderer is 1.3 MB and is gated.
- **A gated page must degrade when the payload is absent.** Never ship a button
  that 404s.
- **The 3D canvas keeps its own dark ground in both themes.** The panel under it
  stays on paper, because it is text.
- **`basis` is quoted, never paraphrased** in the graph demo.
- **The written chain under the graph demo is the accessible equivalent**, not
  decoration.
- **Nothing rearranges a layout on interaction.** Dim, highlight, fly the camera;
  never move a node to make a reading easier than the data earned.
- **Unfinished work is labelled unfinished** — or, as of this session, not shown
  at all. Thomas is job hunting and wants completed work on the page.

## 4. Open items — carry these forward until closed

### COPY
| # | Item | Notes |
|---|---|---|
| C-2 | Demo copy unread by Thomas | The graph demo block, the figure caption and the four-sites sentences are mine. 404 copy he has ruled acceptable for now. The lander copy this covered is gone. |
| C-5 | **`page-hcs.php` arithmetic** (thomascheesman.ca) | Two years up the line then "kitchen manager for 10 years" lands in 2014, not 2013, now the Keg start is 2002. His own voice, his number to rule on. Ask, do not guess. |
| C-6 | Projects page down to one project | **Closed 2026-09-19** — The Back Quarter fills the slot. |
| C-7 | Back Quarter and four-site copy unread by Thomas | All of it is mine except the facts. The childhood paragraph especially — it is his life on a hiring page. |

### PROJECTS
| # | Item | Notes |
|---|---|---|
| P-1 | The Back Quarter as project #2 | **Done on disk 2026-09-19.** Thomas corrected the scope himself: not the desk menu, the drivable farm. |
| P-2 | More stills for The Back Quarter | One daytime shot is in. His night screenshots are better-looking but show the treehouse name signs, which cannot go on the hiring site (nothing familial). A night shot framed away from the treehouses would earn its place. |
| P-3 | The desk menu and drawer are still unwritten-about | Separate from the Back Quarter: the desk-metaphor nav, the drawer footer, the pinball and arcade games, the leaderboard REST route. Could be a third project later, or a paragraph inside the thomascheesman.ca brief. Not started, no decision asked for yet. |

### GRAPH
| # | Item | Notes |
|---|---|---|
| G-6 | Demo still is a headless render | If Thomas wants a hand-framed still of the gp-budget slice, he screenshots the live demo and it swaps in. |
| G-8 | No keyboard path into the 3D scene | Folded into A-1. |

### LANDER
| # | Item | Notes |
|---|---|---|
| L-1 | Controls table | **Closed.** The corrected table is live: Space = engines, W/S = pitch, A/D = bank on flaps and yaw on gimbal, "R or Esc". Then the page itself came down — see L-6. |
| L-2 | R2 for the build | **Killed by Thomas 2026-09-17.** Do not restart. |
| L-6 | **Lander pulled from the public site** | **Done on disk 2026-09-19, by his instruction.** `lander.html` and `lander.js` are in `_to_delete/` — recoverable if he ever reverses it. The lander section of `style.css` (from the `/* ---- the lander embed` comment) is **still in the stylesheet**, unused and harmless; left there on purpose so restoring the page is a file move, not a rewrite. If it is still unused in a month, delete it. |
| L-3, L-4, L-5 | Lander page items | **Moot** — no public lander page. Game-side work stays in the lander repo's own `V0.x`. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Full accessibility pass, site-wide** | Thomas asked for it. Not started. Its own session, not bolted onto feature work: keyboard order, focus states, landmarks, contrast in both themes, the canvas's text equivalent, the résumé PDF's tagging. **The iframe keyboard-trap problem is gone with the lander page**, so this is now a smaller job than the last handoff implied. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-2 | Favicon | **Closed 2026-09-19.** Real mark, flat teal, drawn as paths. Source candidates and the comparison sheets are in the session output, not the repo — if a variant is ever wanted, the geometry is in `favicon.svg` and is easy to retune. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address within weeks. |
| INFRA-5 | `_to_delete/` folders | tc-ventures site: `gd-block.html`, `graph-demo.css`, `graph-everything.webp`, and now `lander.html` + `lander.js`. Reports Clustering: `dist-wp/`. Theme: orphaned `index-ev_2RCV6.js` still sits in `assets/report-graph/assets/` — 2.4 MB, tracked, never fetched by the live page (verified: only `index-DPd_1gmX.js` loads). Harmless; clear it next time that repo is open for real work. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | Harmless; detach when convenient. |
| D-2 | WP.com plan auto-renew | Do not cancel without confirming DNS for the live sites is unaffected. |
| D-3 | Professional Email expiry ~2026-10-08 | Thomas may renew out of convenience. |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-1 | Rebuilt graph on thomascheesman.ca | **Closed 2026-09-19, verified live** — see §2. |
| O-2 | `/projects` on thomascheesman.ca third-person leakage | **Thomas is writing this himself.** |
| O-4 | bareyourrare history contains `permits/` and `3.jpg` | Instructions in `_Quarantine\bareyourrare-history-purge.md`. Thomas runs it. Until then, treat the address as disclosed. |
| O-5 | `bareyr\.git` lock-file junk | Cosmetic; Thomas deletes. |
| O-7 | Children's names in the Back Quarter world | The live 3D build signs the three treehouses with the kids' first names, which contradicts OD-1 in `docs/QUARTER-SECTION-SPEC.md` ("no children's names, faces, or photos anywhere in the map art or labels") on a public, indexed homepage. **Raised 2026-09-19; Thomas ruled: leave the names.** Recorded so no future agent "fixes" it. They stay off tc-ventures.ca regardless. |
| O-6 | **Rocket Lander repo not public** | **Re-open with care.** He asked for this before; this session he ruled the lander private for now. Assume publishing the repo is also on hold until he says otherwise. |

**Closed this session:** O-1 (verified live); L-1 (verified live); L-6 (on disk).
**Killed/held by Thomas:** the lander's entire public presence; O-6 by implication.

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

1. **Everything from this session is on disk and not live**: the lander removal,
   the favicon, The Back Quarter, the four-site briefs. Until it ships, the live
   projects page still carries the Rocket Lander and a link to `/lander.html`.
   Nothing else in this list matters more.
2. **Thomas reads the new copy** (C-7) — particularly the childhood paragraph.
3. **C-5**, the "10 years" line. One question to Thomas.
4. **The accessibility pass** (A-1), as its own session — smaller now. The new
   figure needs its alt text checked in that pass like everything else.
