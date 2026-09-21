# handoff-011 — tc-ventures.ca

**Written:** 2026-09-20
**Covers:** the long 2026-09-20 session after handoff-010. Most of it was not
this site: the résumé rebuild, a crawl audit of bareyourrare.org, moving two
Hostinger sites behind Cloudflare, and a run of GPRS board work.
**Status at wrap:** tc-ventures.ca itself changed in one place — the served
résumé PDF. GPRS work is handed off separately (O-12).

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom. §2 "Traps" before you touch git, grep, DNS or a rebuild.
2. `claude/thomas-study.md` in the Claude project "TC 'Ventures" — the voice study.
3. `claude/tc-ventures-site-decisions.md` in the same project.
4. `reviews/copy-review-001.md` — his rulings on every block of site copy.
5. `README.md`.
6. If the job is GPRS, stop here and read `GPRS Organization/00 Working Notes/gprs-handoff-001.md` instead.

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
| Pages | `index`, `projects`, `background`, `contact`, `404` |
| Projects on the page | The Economic Report Influence Graph · The Back Quarter · The Desk and the Drawer · then the four live sites |
| Graph demo | `assets/graph-demo.js` + `gp-budget-graph.json` + prebuilt `3d-force-graph.min.js` |
| Icons | `public/favicon.svg` (paths, not text) + `public/apple-touch-icon.png`, linked from all five pages |
| Scratch | **`_to_delete/` is gone.** Files can now be deleted outright — see §2. |
| Sister repo | `C:\Users\thoma\Desktop\My Files\tc-ventures-child-theme` (thomascheesman.ca). Not connected by default; request access. |

## 2. What was done (2026-09-20)

- **Résumé rebuilt and served.** Two pages, ATS-safe single column, corrected
  education (C-11). Thomas exported the PDF from Word himself; it replaced
  `public/assets/Thomas-Cheesman-Resume.pdf` (656,098 bytes, 2 pages, no Rocket
  Lander). Word source at `resume/Thomas-Cheesman-Resume-source.docx`.
  **`resume-source.html` is stale** — see C-8. Written to disk; serving depends on his push.
- **bareyourrare.org audited for search and AI readability.** Markup is strong
  (real `MedicalCondition` schema with ICD-10, citations, `llms.txt`). The one
  critical finding was host-level blocking of non-browser clients. Remaining
  markup gaps are O-11.
- **bareyourrare.org and thomascheesman.ca moved behind Cloudflare** (O-10).
  BYR mail survived the cutover — live send test passed before nameservers moved.
- **Keg paragraph in `page-hcs.php` rewritten four times** as Thomas corrected
  the facts; final text is his ("I started cooking at The Keg in 2002…"). Still
  undeployed and unread back (O-9).

### Traps worth knowing

- **Cloudflare's record scanner skips long TXT records.** BYR's DKIM had to be
  rebuilt by hand. Paste it without surrounding quotes and check the length.
- **Force every mail record DNS-only** (MX, SPF, DKIM, DMARC, mail/autodiscover
  CNAMEs) before switching nameservers, then send a live test.
- **The Cloudflare "Connect your domain" field can silently empty after typing.**
  Read the field back before pressing Continue.
- **Hostinger clipboard:** `navigator.clipboard` and `execCommand('copy')` both
  fail in hPanel. Real ctrl+A / ctrl+C keystrokes in the edit dialog work; then Cancel, never Update.
- **The Chrome extension blocks JS results that look like cookies or base64.**
  Return lengths or booleans instead.
- **Bot blocking on the Hostinger sites is not constant.** On the evening of
  2026-09-20 an automated request with a ClaudeBot user-agent to
  gpresidentialsociety.com — still on Hostinger, untouched — returned **200**,
  where earlier the same day every such request timed out. It may depend on the
  requesting IP. Re-test from more than one place before treating it as fixed or broken.
- Every 2026-09-19 trap in handoff-010 §2 still stands (no git in a mount,
  no unfiltered grep in the theme repo, three caches on thomascheesman.ca now).

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
| C-7 | **The Back Quarter and Desk copy unread by Thomas** | Especially the childhood paragraph — it is his life on a hiring page, and the facts came from his own published prose, not from him directly. |
| C-8 | **The résumé PDF is now generated from Word, not from `resume-source.html`** | Settled 2026-09-20. Thomas exported `public/assets/Thomas-Cheesman-Resume.pdf` from the rebuilt .docx and it is in place: two pages, letter, **no Rocket Lander** (which closes the privacy leak logged as C-10), corrected education. The Word source sits beside the old HTML at `resume/Thomas-Cheesman-Resume-source.docx`. **`resume-source.html` is now stale and no longer the source of the served PDF** — either update it to match or retire it, but do not re-render from it, which would put the lander back on a public download. |
| C-9 | **`page-thomas.php` ~2010: "I couldn't get past my kitchen manager"** | Reads oddly now that he was the kitchen manager from ~2006. It may mean the senior manager above him. His prose and his call — flag it, do not rewrite it. |
| C-11 | **Education, settled by Thomas 2026-09-20** | Four academic years at GPRC (now Northwestern Polytechnic), fall 1999 to spring 2003: **B.Sc. Pre-Pharmacy credits, 1999–2002** (three academic years), then **Power Engineering 4th Class and Class 3B plus Gas Plant Operations Levels I and II, 2002–2003**. Journeyman Chef, Red Seal, SAIT, 2012. The rebuilt .docx carries exactly this. `resume/resume-source.html` already has the B.Sc. span right; what it lacks is the Power Engineering dates, Class 3B and the college's name (see C-8 on the render path). |

### PROJECTS
| # | Item | Notes |
|---|---|---|
| P-4 | Better first figure for The Desk | The monitor is the proof that the desk *is* the menu, and the current crop leaves it out because its contents rows name the children. A frame with the monitor showing the arcade, the cursor-trail drawer or the screensaver would swap straight in. |
| P-5 | The Back Quarter still may want reshooting | The project figure is a daytime frame and still reads true, but a fresh one framed away from the treehouses is worth taking. |
| P-6 | A fourth project? | Nothing is queued — and per the "show finished work" rule, nothing goes up until it is done. |

### GRAPH
| # | Item | Notes |
|---|---|---|
| G-6 | Demo still is a headless render | If Thomas wants a hand-framed still of the gp-budget slice, he screenshots the live demo and it swaps in. |
| G-8 | No keyboard path into the 3D scene | Folded into A-1. |

### A11Y
| # | Item | Notes |
|---|---|---|
| A-1 | **Full accessibility pass, site-wide** | Thomas asked for it. Not started, and it is the biggest open item on this site. Its own session: keyboard order, focus states, landmarks, contrast in both themes, the canvas's text equivalent, the résumé PDF's tagging, and the alt text on the three new figures. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works; he wants a non-general address within weeks. |
| INFRA-5 | Leftovers in the **other** repos | This repo is clean. Still open: Reports Clustering `dist-wp/`, and the orphaned `index-ev_2RCV6.js` under the theme's `assets/report-graph/assets/` (2.4 MB, tracked, never fetched). Both can now be deleted with permission rather than quarantined. |
| INFRA-6 | Dead lander CSS | The lander block in `public/assets/style.css` (from line 670) is unused and harmless; kept so restoring the page would be a file move. Delete it if still unused by mid-October 2026. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | Harmless; detach when convenient. |
| D-2 | WP.com plan auto-renew | Do not cancel without confirming DNS for the live sites is unaffected. |
| D-3 | **Professional Email expiry ~2026-10-08** | Put to Thomas 2026-09-19; **he deferred the decision.** Raise it again before 8 October. |

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
| O-11 | **bareyourrare.org crawl audit — markup gaps still open** | Full audit: `Claude outputs/byr-crawl-audit.md`. §1 (host blocking) is fixed by O-10. Still open, in value order: (a) `MedicalWebPage` with `lastReviewed` + `author` on the five condition guides; (b) duplicate `BreadcrumbList` (theme + SEO plugin); (c) `/poems/` (POEMS syndrome) collides with `/category/poems/` (poetry, empty `h1`) — rename the slug to `/category/poetry/` or noindex it; (d) meta descriptions on `/privacy/` and `/terms/`; (e) `handshcshero.png` needs `alt=""` or a description; (f) point to `llms.txt` from the head and `robots.txt`; (g) page weight. Then read access logs monthly for AI crawler user-agents. |
| O-12 | **GPRS work has its own handoff** | Board reports, the fundraising drafts, the Cloudflare zone for gpresidentialsociety.com, SPF and Trevor: `GPRS Organization/00 Working Notes/gprs-handoff-001.md`. Not tracked here. |
| O-9 | **`page-hcs.php` edit is undeployed** | The C-5 rewrite is on disk in the theme repo only. It also has not been read back by Thomas. |

**Closed this session:** C-10 (lander in the résumé PDF). **Answered:** C-8's render path (Word, not HTML), C-11.

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

1. **Thomas reads the rewritten `page-hcs.php` paragraph**, then deploys it (O-9), and reads C-7.
2. **Decide C-8:** update `resume-source.html` to match the Word file, or retire it.
3. **BYR `MedicalWebPage` markup** (O-11a) — the highest-value item left from the audit.
4. **The accessibility pass** (A-1) as its own session.
5. **D-3 before 8 October.**
