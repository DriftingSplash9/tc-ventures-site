# handoff-003 — tc-ventures.ca

**Written:** 2026-09-12 (evening)
**Covers:** the voice session (item 2 of handoff-002 §6), a second rebuild of the
résumé, and the contact page.
**Status at wrap:** handoff-002's rewrite **verified serving** — every page and the
stylesheet on the live domain matched the repo byte-for-byte before this session's
résumé change. New résumé PDF and source, `contact.html`, the nav change on all
four other pages, the sitemap entry and a one-line CSS fix are on disk. **None of
that has been seen serving.**

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom.
2. `claude/thomas-study.md` in the Claude project "TC 'Ventures" — the voice study.
   Read it before writing any copy in Thomas's voice. It is not in this repo on
   purpose; it draws on personal files.
3. `reviews/copy-review-001.md` — Thomas's rulings on every block of site copy.
4. `briefs/brief-001-wow-and-contact.md` — the still-open work.
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
| Repo | `DriftingSplash9/tc-ventures-site` |
| Local | `C:\Users\thoma\Desktop\My Files\Website Projects\tc-ventures site` |
| Host | Cloudflare Worker `tc-ventures-site` (static assets only) |
| Config | `wrangler.jsonc` → serves `./public`, `not_found_handling: 404-page` |
| Deploy | push to `main` → Cloudflare builds → `npx wrangler deploy` |
| Also live at | `tc-ventures-site.thomasmcheesman.workers.dev` (INFRA-1) |
| Registrar | WordPress.com (registration only); DNS on Cloudflare |
| Contact email | `thomas@tc-ventures.ca` — live, forwards |
| Fonts | self-hosted in `public/assets/fonts/` |
| Résumé | `resume/resume-source.html` → rendered with headless Chromium → `public/assets/Thomas-Cheesman-Resume.pdf` |

## 2. What was done (2026-09-12, evening)

**Verified serving.** `index`, `projects`, `background`, `404`, `style.css` and
`sitemap.xml` on tc-ventures.ca matched disk (md5). Note: `/x.html` 307-redirects to
`/x`; use `curl -L` or the md5 is of an empty body.

**Voice session done.** Read all four sites, the timeline app, and from Thomas's own
files: goal sheets 2007–2025, both old résumés, letters to ministers, the Prose
folder, a Facebook extract, and the June 2026 life compilation. Output is
`claude/thomas-study.md` in the Claude project: voice mechanics with examples, a
sourced fact ledger, and open questions. **Facebook content is not for the site** —
Thomas's ruling.

**Résumé rebuilt again** — same design, stronger content. Handoff-002's version had the
kitchen career as one anonymous block ("hospitality operations, Alberta"). Now:
- Summary leads with the site's own claim ("I specify software precisely…").
- Experience names employers, with dates and outcomes from Thomas's own documents:
  The Keg (2002–2013, kitchen manager ~10 yrs, "best in the corporation for
  Alberta", built the Excel systems, apprenticed cooks, H&S committee); Ric's Grill →
  Township 71 (2013–2015, opened Nov 2014 into the oil crash, closed May 2015) with
  the GPRC semester folded in (wrote curriculum, lesson plans, assessments); Majors
  Homestyle & Tractor Jack's (2015–Mar 2019, banquets/catering, hospital-build crew
  contract, ~1 yr consulting after).
- Caregiver entry now says what it was: round-the-clock team, palliative teenage client.
- Projects reordered: graph, BYR, GPRS, personal site, Rocket Lander.
- Dropped the "Data & ops" skills row (duplicated the Keg bullet).
- CSS: body 9.4pt / line-height 1.38 (was 9.6 / 1.44); page margins 0.7in top,
  0.55in bottom (were 0.8 / 0.65), sides unchanged at 0.9in; `h2 { break-after:
  avoid }` so a section heading can't orphan at a page foot; last section
  `break-inside: avoid`.
- **Two pages, measured.** Page 1 ends after Rocket Lander with ~8 lines of air.
  Page 2 is full. Any added line goes to page 3.

**Dates — confirmed by Thomas after the rewrite:** Keg start 2002 (his life story says 2001; his old
résumé and the site say 2002); GPRC semester 2014 (he was teaching the week Township
71 opened, Nov 2014); Majors 2015 start (about seven weeks after Daniel was born).

**Contact page built** — `public/contact.html`. No form, no phone. Structure: the
address (with a copy button that only appears when the clipboard API exists), one
sentence on what happens after you write, five "different first moves" rows (role /
code first / talk / résumé for a system / the gap), and a Time band with the current
Grande Prairie time (inline JS, `Intl` with `America/Edmonton`; reads "Mountain Time"
without JS) beside a static offset table. Nav on `index`, `projects`, `background`
and `404` now points at `/contact.html` instead of `mailto:`. Added to `sitemap.xml`.
Verified in headless Chromium: no console errors, no failed requests, no horizontal
scroll at 1280 or 390, light and dark.

**CSS fix, site-wide:** `.wrap.narrow.prose` sections (Background intro,
Practicalities, the contact page's "what happens" band) were rendering centred
instead of left-aligned, because `.prose { max-width }` capped the wrapper itself
— the exact thing the comment above `.wrap.narrow` says must not happen. One added
rule: `.wrap.narrow.prose { max-width: 1040px; }`. Background will shift left when
this ships; that is the fix, not a regression.

### Traps worth knowing

- Cowork's default connected folder `Desktop\My Files\TC Ventures` is **empty and not
  this repo**. Request `Website Projects\tc-ventures site` explicitly.
- `device_commit_files` by `fileUuid` (from `SendUserFile`) writes correct bytes;
  by `stagedPath` it once wrote a stale copy. **Check byte counts on disk after any
  commit** — did that this session: 128,506 (PDF) and 13,754 (HTML).
- No Chromium on Thomas's machine. Render the résumé in the cloud container
  (Playwright, `prefer_css_page_size=True, print_background=True`), then commit.
- `git status` in the mounted repo fails on `index.lock` (mount is no-unlink). Use
  `git --no-optional-locks` or compare with curl instead.
- Live fetches can be cached for ~15 min by WebFetch. A "discrepancy" between live
  and repo was, this session, a stale fetch. Verify with curl before reporting.

## 3. Current design

Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
`prefers-color-scheme`. Familjen Grotesk / Source Serif 4 / IBM Plex Mono. Confirmed
by Thomas; stop re-litigating it.

**Standing rules:**
- `object-fit: contain`, never `cover`.
- Content must render without JavaScript. JS allowed; dependencies and a build step
  are not — prebuilt bundles copied into `assets/` only.
- Fonts self-hosted. No third-party font request.
- No phone number on the site. It is in the résumé PDF.
- **Never publish an exact node, edge, report or grade count.** Round or describe.
- **No vanity metrics.** No line counts.
- **Do not invent dates or figures.** Unknown → ask Thomas.
- Hajdu-Cheney syndrome is named on purpose. Symptom detail is not.
- WordPress stays once per spec table as a hiring keyword; out of headline prose.
- Nothing familial, nothing from Facebook.
- The GPRS logo is not this site's favicon.
- Edit `resume/resume-source.html` and re-render. Never edit the PDF. Measure page
  count after any content change; the target is exactly two pages.
- Melanie and Thomas are "the parents" of the three children, never "co-parents",
  and the relationship is not otherwise characterized anywhere. (Not relevant to this
  site, which carries nothing familial — recorded so no agent trips on it.)

## 4. Open items — carry these forward until closed

### COPY
| # | Item | Notes |
|---|---|---|
| C-2 | Rewritten pages unread by Thomas | He signed off on decisions, not sentences. Now also: the new résumé (he has the PDF). |

### CONTACT
| # | Item | Notes |
|---|---|---|
| CT-4 | Contact copy unread by Thomas | Built in his voice from the study; he has seen a screenshot, not ruled on sentences. The reply-time sentence ("within a working day") is a commitment only he can make. |

### GRAPH
| # | Item | Notes |
|---|---|---|
| G-1 | Wow decided: the live graph | Must not auto-load; demo something simple. |
| G-2 | Do not reuse the deployed bundle | Build a small demo from current data, ~100–150 nodes. |
| G-3 | Repo link unverified | `github.com/DriftingSplash9/Reports-Clustering` — GitHub profile shows it public (checked this session), data match not checked. |
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
| O-2 | `/projects` on thomascheesman.ca has third-person leakage | "The author is not a trained programmer…" — reads as an unedited draft. Not this repo. |

**Closed this session:** CT-1, CT-3 (contact page built, nav fixed, sitemap updated); CT-2 (voice session done); C-4 (résumé dates — Thomas confirmed Keg 2002, GPRC fall 2014, Majors 2015). Nothing was killed.

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

1. **See it serve:** contact page, the nav change, the résumé PDF, and Background
   after the CSS fix.
2. **Thomas rules on the contact sentences** (CT-4), especially the reply-time line.
3. **Then the graph demo.** G-1, G-2. Small, deliberate, does not auto-load. Tag: `GRAPH`.
4. **Close INFRA-1** once settled.
5. **Later:** the Godot rocket lander web build. Tag: `LANDER`.
