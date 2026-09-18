# handoff-007 — tc-ventures.ca

**Written:** 2026-09-18
**Covers:** the first real deploy, and the Rocket Lander page.
**Status at wrap:** the site is **deployed and verified serving**. Three files
changed *after* that deploy and are **on disk only** — one of them means the live
site currently documents the wrong game controls. See §2.

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
| Pages | `index`, `projects`, `background`, `contact`, `lander`, `404` |
| Graph demo | `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js`; data from `scripts/export-gp-budget.py` |
| Lander page | `public/lander.html` + `assets/lander.js`; expects the Godot export at `/lander/` |
| Scratch | `_to_delete/` at repo root — Cowork cannot delete files, so disposables go there |

**Hard limit that shapes everything below:** Cloudflare Workers static assets cap
**individual files at 25 MiB**. This is why the Godot build cannot live in this repo.

## 2. What was done (2026-09-18)

**The site deployed, and it serves.** Verified live: `projects.html` carries the
budget-graph section, "four live sites", and the link to the lander;
`lander.html` exists and renders. The workers.dev duplicate URL is gone — Thomas
checked it and got "not found", which is the change working, not a failure.
*(Worth saying plainly to him next time: that URL was listed as a check and read
as a link to the site. Bad wording on my part.)*

**`/lander.html` built.** A page for the Rocket Lander, framed as a work in
progress because that is what it is. Lede: *"A rocket with a real aerodynamic
flight model, running in your browser. It flies. I cannot land it yet, and neither
will you."* Linked from the Rocket Lander section of Projects, **deliberately not
in the primary nav** — a work in progress does not earn a nav slot.

**How the embed works.** An **iframe** at `/lander/index.html`, not the engine
hand-wired into the page. The Godot export ships an `index.html`, loader, `.wasm`
and `.pck` that expect to own the document; dropping the exported folder in
untouched makes an engine upgrade a folder swap rather than a re-integration.
Sandboxed `allow-scripts allow-same-origin allow-pointer-lock`; the page focuses
the frame on load, because the click that loaded it landed on the button.

**The page ships before the build does, safely.** `lander.js` does a `HEAD` on
`/lander/index.html` at load — one small file, not the 36 MB one — and only
reveals the button if it returns OK. Verified both ways. The day the build is
uploaded the button appears on its own; no second edit.

**The controls table was wrong and is now fixed on disk.** I wrote it from the
project's prose instead of reading `main.gd`, and got it backwards. The truth:
**Space is the engines**, W/S is **pitch**, A/D is **bank on the flaps and yaw on
the gimbal**. Also added, from the game's own header comment, the paragraph about
two control systems sharing one set of keys. **This is not deployed** — see the
table below.

### Not deployed — on disk only

| File | What changed | Why it matters |
|---|---|---|
| `public/lander.html` | Controls table corrected; two explanatory paragraphs added | **The live page currently tells readers the wrong controls.** Confirmed by fetching the live page. |
| `public/assets/lander.js` | `HEAD` build-presence check | Without it the button would appear and 404 |
| `public/assets/style.css` | `.gd__frame--tall`, iframe sizing, `kbd` styling | The lander page is unstyled in places without it |

One push fixes all three.

### Traps worth knowing

- **Cloudflare rejects any static asset over 25 MiB.** The Godot `.wasm` is
  36.1 MiB. It cannot go in `public/`. This was not checked before telling Thomas
  to export, which cost him an export cycle.
- **Git in a Cowork-mounted folder cannot unlink files.** `git status` creates
  `.git/index.lock` and can't remove it. Read-only git with `GIT_OPTIONAL_LOCKS=0`;
  better, don't run git in the mount at all.
- **GitHub Desktop merges, it does not force-push.** A merge takes the other side's
  deletions. Any history rewrite goes through the command line.
- **Cowork cannot delete anything in a mount**, and cannot `mv` a *directory*
  (that is a delete of the source). Files move fine. Hence `_to_delete/`.
- **Committing a file to the device re-encodes images.** Verify a committed image
  by staging it back, not by trusting the byte count.
- **The Facebook rule.** His public Facebook is linked from thomascheesman.ca. He
  has ruled it "between you and me only" — never material for this site.

## 3. Current design

Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
`prefers-color-scheme`. Familjen Grotesk / Source Serif 4 / IBM Plex Mono.
Confirmed; stop re-litigating it.

**Standing rules:**
- `object-fit: contain`, never `cover`.
- Content must render without JavaScript. JS allowed; dependencies and a build step
  are not — prebuilt bundles copied into `assets/` only.
- Fonts self-hosted. No third-party font request.
- No phone number on the site. It is in the résumé PDF.
- **Never publish an exact node, edge, report or grade count** *in copy*. Round or
  describe. One ruled exception: the application screenshot on Projects shows the
  app's own counters. The prose still rounds.
- **No vanity metrics.** No line counts.
- **Do not invent dates or figures.** Unknown → ask Thomas. **This includes game
  controls** — read the input code, do not infer them from prose. That mistake is
  in §2.
- Hajdu-Cheney syndrome is named on purpose. Symptom detail is not.
- WordPress stays once per spec table as a hiring keyword; out of headline prose.
- Nothing familial, nothing from Facebook.
- Edit `resume/resume-source.html` and re-render. Never edit the PDF. Exactly two
  pages.
- Melanie and Thomas are "the parents" of the three children, never "co-parents".

**Demo and embed rules:**
- **Nothing heavy loads before a click.** The graph renderer is 1.3 MB, the game is
  36 MB. Both are gated, and both were verified to request nothing before the click.
- **A gated page must degrade when the payload is absent** — hence the `HEAD` check.
  Never ship a button that 404s.
- **The 3D canvas keeps its own dark ground in both themes.** The panel under it
  stays on paper, because it is text.
- **`basis` is quoted, never paraphrased** in the graph demo.
- **The written chain under the graph demo is the accessible equivalent**, not
  decoration.
- **Nothing rearranges a layout on interaction.** Dim, highlight, fly the camera;
  never move a node to make a reading easier than the data earned.
- **Unfinished work is labelled unfinished.** The lander page says so in its lede.
  That is the site's argument working, not an embarrassment to hide.

## 4. Open items — carry these forward until closed

### COPY
| # | Item | Notes |
|---|---|---|
| C-2 | Demo and lander copy unread by Thomas | The graph demo block, the new figure caption, the four-sites sentences, and the entire lander page are all mine. 404 copy he has ruled acceptable for now. |
| C-5 | **`page-hcs.php` arithmetic** (thomascheesman.ca) | Two years up the line then "kitchen manager for 10 years" lands in 2014, not 2013, now the Keg start is 2002. His own voice, his number to rule on. Ask, do not guess. |

### GRAPH
| # | Item | Notes |
|---|---|---|
| G-6 | Demo still is a headless render | If Thomas wants a hand-framed still of the gp-budget slice, he screenshots the live demo and it swaps in. |
| G-8 | No keyboard path into the 3D scene | Folded into A-1. |

### LANDER
| # | Item | Notes |
|---|---|---|
| L-1 | **Three files written, not deployed** | See the table in §2. The live page has the wrong controls until this pushes. Highest priority on this list. |
| L-2 | **The build has nowhere to live** | 36.1 MiB `.wasm` vs a 25 MiB Cloudflare cap. Agreed direction: a Cloudflare R2 bucket with a custom domain, iframe pointed there instead of `/lander/`. One string in `lander.js` (`var BUILD`). Not built; Thomas has not yet been walked through creating the bucket. |
| L-3 | No still for the lander frame | The frame is bare dark ground with the button centred. A screenshot of the build mid-flight would fill it. |
| L-4 | Escape not in the controls table | It restarts now, same as R. One line, next time the page is touched. |
| L-5 | Game-side work | Tracked in the lander repo's `V0.3.md`, not here: the empty tuning panel, the `_dbg` block to remove, and the barge-vs-tower-catch design question. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Full accessibility pass, site-wide** | Thomas asked for it. Not started. Its own session, not bolted onto feature work: keyboard order, focus states, landmarks, contrast in both themes, the canvas's text equivalent, the résumé PDF's tagging. The lander iframe adds to this — a game canvas is a keyboard trap by nature. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-1 | workers.dev duplicate | **Closed.** Config deployed, URL verified dead. |
| INFRA-2 | Favicon is a placeholder | Thomas is finding the TC mark. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address within weeks. |
| INFRA-5 | `_to_delete/` folders | tc-ventures site: `gd-block.html`, `graph-demo.css`, `graph-everything.webp`. Reports Clustering: `dist-wp/`. Theme: orphaned `index-ev_2RCV6.js` in `report-graph/assets/`. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | Harmless; detach when convenient. |
| D-2 | WP.com plan auto-renew | Do not cancel without confirming DNS for the live sites is unaffected. |
| D-3 | Professional Email expiry ~2026-10-08 | Thomas may renew out of convenience. |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-1 | **Rebuilt graph written into the theme, not uploaded** | `tc-ventures-child-theme/assets/report-graph/`. `/reports-graph` will pull ~13 MB (11 MB of it `corpus-data.json`) against 2.4 MB before. Confirm the host gzips `.json`. The one thing to check after upload is that `corpus-data.json` loads from under the theme path — that is the bug this rebuild fixed. |
| O-2 | `/projects` on thomascheesman.ca third-person leakage | **Thomas is writing this himself.** |
| O-4 | bareyourrare history contains `permits/` and `3.jpg` | Instructions in `_Quarantine\bareyourrare-history-purge.md`. Thomas runs it. Until then, treat the address as disclosed. |
| O-5 | `bareyr\.git` lock-file junk | Cosmetic; Thomas deletes. |
| O-6 | **Rocket Lander repo not public** | Thomas asked for it. Content scanned clean. Was blocked on the repo's own docs contradicting the site; `V0.3.md` now closes that. No `gh` CLI — GitHub Desktop → Add Local Repository → Publish, untick private. |

**Closed this session:** INFRA-1 (verified dead); the first deploy; the lander page
built and linked. **Nothing was killed.**

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

1. **Push the three undeployed files** (L-1). The live page is currently wrong
   about the game's controls, which is the one thing on this site that is
   straightforwardly inaccurate.
2. **Cloudflare R2 for the build** (L-2). Create the bucket, attach a custom
   domain, upload `web-build/`, change `var BUILD` in `lander.js`. Thomas has
   not done this before — walk it, don't hand him a checklist.
3. **Upload the rebuilt graph** to thomascheesman.ca (O-1) and check
   `corpus-data.json` resolves under the theme path.
4. **C-5**, the "10 years" line. One question to Thomas.
5. **The accessibility pass** (A-1), as its own session.
6. **Favicon** when the mark arrives (INFRA-2).
