# handoff-004 — tc-ventures.ca

**Written:** 2026-09-17
**Covers:** 2026-09-13 → 09-17. Copy fixes from Thomas's own corrections, a third
résumé pass, the home lede, the GitHub account cleanup, and the graph-demo data
scouting. Plus a Bare Your Rare incident that lives in another repo but which the
next agent must know about before running git on any mounted folder.
**Status at wrap:** everything below is **verified serving** — `index`, `contact`,
`background` and the résumé PDF on the live domain match disk byte-for-byte as of
this writing.

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. §2 "Traps" before you touch git.
2. `claude/thomas-study.md` in the Claude project "TC 'Ventures" — the voice study.
   Read it before writing any copy in Thomas's voice.
3. `reviews/copy-review-001.md` — his rulings on every block of site copy.
4. `briefs/brief-001-wow-and-contact.md` — the wow brief. Contact is done; the
   graph demo is not.
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
| Repo | `DriftingSplash9/tc-ventures-site` — **public** since 2026-09-16 |
| Local | `C:\Users\thoma\Desktop\My Files\Website Projects\tc-ventures site` |
| Host | Cloudflare Worker `tc-ventures-site` (static assets only) |
| Config | `wrangler.jsonc` → serves `./public`, `not_found_handling: 404-page` |
| Deploy | push to `main` → Cloudflare builds → `npx wrangler deploy` |
| Also live at | `tc-ventures-site.thomasmcheesman.workers.dev` (INFRA-1) |
| Registrar | WordPress.com (registration only); DNS on Cloudflare |
| Contact email | `thomas@tc-ventures.ca` — live, forwards |
| Fonts | self-hosted in `public/assets/fonts/` |
| Résumé | `resume/resume-source.html` → headless Chromium → `public/assets/Thomas-Cheesman-Resume.pdf` |
| Pages | `index`, `projects`, `background`, `contact`, `404` |

## 2. What was done (2026-09-13 → 09-17)

**Copy, from Thomas's corrections:**
- Background ¶2: "family care and self-directed study" was wrong. Now: "a couple of
  surgeries, a few injuries, and being the stay-at-home parent. I decided to learn
  programming. When AI crashed that party, I decided the better bet was to understand
  AI itself…" His words.
- Home lede replaced (he called the old one cheesy): "I run the website for a
  nonprofit and three more for practice and, eventually, work. I set the objectives,
  design the thing, and then build it with AI. After seventeen years managing cooks, a
  team of AI is the easy part; knowing what to tell it is not." Meta descriptions match.
- "Email me" buttons on home and Background → "Get in touch" → `/contact.html`.
- Contact: reply line is "within a day or two" (his number). Call row says video/Zoom
  is fine and that his speech is not always clear on the first pass — his line, his call.

**Résumé, third pass.** Summary is now the home lede plus one sentence for the graph.
Named employers with dates he confirmed: The Keg 2002–2013 (**franchise**, not
corporate — his correction), Ric's Grill → Township 71 2013–2015 with the GPRC
semester (fall 2014) folded in, Majors 2015–Mar 2019. Site dates: GPRS 2023–, BYR
2025–, personal platform 2026. Career note carries the surgeries/stay-at-home line.
Still exactly two pages; body 9.4pt / 1.38, margins 0.7in top 0.55in bottom.

**GitHub account cleanup** (not this repo, but the portfolio links to it): `bareyr`
renamed `bareyourrare` and made public; `tc-ventures-site` and `gprs-site` public;
`tc-timeline` private; `tc-ventures-child-theme` renamed `thomascheesman-ca-theme`;
descriptions, websites and topics on every public repo; four repos pinned; profile
README at `DriftingSplash9/DriftingSplash9`; bio set. G-3 is therefore closed —
the graph repo is public and its data was cloned and read this week.

**Graph demo scouted, not built.** The corpus (405 slices, ~3,660 reports, ~3,350
dependencies at export) contains **City of Grande Prairie — City Budget Report**
(`gp-budget`). Its dependency closure is **54 reports / 76 edges**: municipal census
and assessment roll → Alberta LGFF, equalized assessment, MAPL → StatCan Census, CPI,
SEPH, national accounts → SNA 2008, the CPI Manual, GFSM 2014. Grades 22 A / 48 B /
6 C. Grande Spirit Foundation is in it. It is the right demo: his own city, and it
illustrates the home page's "how much your city gets for road repair" sentence.
Export script idea: load the repo's own `src/data/index.ts` corpus with `tsx`, walk
`source_report_id → target_report_id` upward from `gp-budget`, emit nodes+edges JSON
with `basis` text kept in full (~70 KB). **Two decisions are still Thomas's:** home
page or projects page; 3D (`3d-force-graph` prebuilt UMD, ~1.2 MB, load on click) or 2D
(~300 KB). Proposed and waiting.

### Traps worth knowing

- **Git in a Cowork-mounted folder cannot unlink files.** `git status` creates
  `.git/index.lock` and can't remove it; commits leave `HEAD.lock`, `ORIG_HEAD.lock`,
  `objects/maintenance.lock` and `objects/*/tmp_obj_*` behind. GitHub Desktop then
  refuses with "a lock file already exists". Rule: run read-only git with
  `GIT_OPTIONAL_LOCKS=0`, and after any write `mv` every non-stale `*.lock` aside.
  Better: don't run git in the mount at all; compare against the live site with curl.
- **GitHub Desktop merges, it does not force-push.** A rewritten local branch gets
  pull-merged, and a merge takes the other side's deletions. This is how the Bare Your
  Rare theme lost 17 files on the live server for a day (2026-09-16/17; fixed with a
  forward commit). Any history rewrite must be pushed from the command line.
- **The Facebook rule.** His public Facebook is linked from thomascheesman.ca. He has
  ruled it "between you and me only" — never material for this site.
- The Cowork default folder `Desktop\My Files\TC Ventures` is still empty and still
  not this repo.

## 3. Current design

Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
`prefers-color-scheme`. Familjen Grotesk / Source Serif 4 / IBM Plex Mono. Confirmed;
stop re-litigating it.

**Standing rules:**
- `object-fit: contain`, never `cover`.
- Content must render without JavaScript. JS allowed; dependencies and a build step
  are not — prebuilt bundles copied into `assets/` only.
- Fonts self-hosted. No third-party font request.
- No phone number on the site. It is in the résumé PDF.
- **Never publish an exact node, edge, report or grade count.** Round or describe.
  (A fixed demo snapshot still gets "fifty-odd reports" in copy.)
- **No vanity metrics.** No line counts.
- **Do not invent dates or figures.** Unknown → ask Thomas.
- Hajdu-Cheney syndrome is named on purpose. Symptom detail is not.
- WordPress stays once per spec table as a hiring keyword; out of headline prose.
- Nothing familial, nothing from Facebook.
- The GPRS logo is not this site's favicon.
- Edit `resume/resume-source.html` and re-render. Never edit the PDF. Measure page
  count after any content change; the target is exactly two pages, and page 2 is full.
- Melanie and Thomas are "the parents" of the three children, never "co-parents";
  the relationship is not otherwise characterized anywhere.

## 4. Open items — carry these forward until closed

### COPY
| # | Item | Notes |
|---|---|---|
| C-2 | Sentences unread by Thomas | He has ruled on the home lede, Background ¶2, the résumé and the contact reply/call lines. Projects page and 404 copy remain unread by him. |

### GRAPH
| # | Item | Notes |
|---|---|---|
| G-1 | Wow decided: the live graph | Must not auto-load; demo something simple. |
| G-2 | Demo data chosen: `gp-budget` closure, 54/76 | See §2. Export from the repo's own loader, not the stale bundle. |
| G-5 | **Two decisions pending from Thomas** | Home vs projects page; 3D vs 2D. Blocks the build. |
| G-4 | Rocket Lander has no source link | He can make the repo public. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-1 | workers.dev duplicate | `"workers_dev": false`, `"preview_urls": false` once settled. |
| INFRA-2 | Favicon is a placeholder | Thomas is finding the TC mark. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address within weeks. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | Harmless; detach when convenient. |
| D-2 | WP.com plan auto-renew | Do not cancel anything without confirming DNS for the three live sites is unaffected. |
| D-3 | Professional Email expiry ~2026-10-08 | Related to INFRA-4. |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-1 | Deployed graph bundle on thomascheesman.ca is stale (~302 reports) | Rebuild command in that repo's `functions.php` comment. |
| O-2 | `/projects` on thomascheesman.ca has third-person leakage | Reads as an unedited draft. Not this repo. |
| O-3 | thomascheesman.ca "long way round" says Keg 2001 | Thomas confirmed 2002. One-word fix over there. |
| O-4 | **bareyourrare history still contains `permits/` (his address) and `3.jpg`** | Commits 24a7e72 and 2014bed on GitHub. Live server is clean; forward-fix pushed 09-17. Thomas chose to do the rewrite + command-line force-push + GitHub support purge later. Quarantined copies: `My Files\_Quarantine\from-bareyr-repo(-2)`. |
| O-5 | `bareyr\.git` has `*.stale` lock files and `tmp_obj_*` junk | Cosmetic; Thomas to delete. |

**Closed this session:** CT-4 (contact sentences ruled on by Thomas); G-3 (graph repo
verified public, data read); C-4 carried from 003 stays closed. Nothing was killed.

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

1. **Get the two graph answers** (G-5): home or projects; 3D or 2D. Then build the
   demo from `gp-budget`: still image + "Load the live graph" button, no auto-load,
   colour by tier, size by in-degree, click an edge → grade + quoted basis. Verify at
   1280/390, light/dark, and that nothing 3D downloads before the click.
2. **Favicon** when Thomas supplies the mark (INFRA-2). One file swap.
3. **Close INFRA-1** once the demo is live and settled.
4. **Later:** the Godot rocket lander web build. Tag: `LANDER`.
