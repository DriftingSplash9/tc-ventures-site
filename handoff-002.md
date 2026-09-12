# handoff-002 — tc-ventures.ca

**Written:** 2026-09-12
**Covers:** the first session in which Thomas actually read the copy that was already
public. The review, his rulings, the correction pass across all four pages, the font
move, and a rebuilt résumé.
**Status at wrap:** all four pages and the résumé rewritten on disk and verified in a
headless browser. **Not seen serving.** Nothing here has been checked on the live
domain since the rewrite.

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom.
2. `reviews/copy-review-001.md` — every block of site copy, numbered, with Thomas's
   own markup. Read it when you need to know *why* a line reads the way it does
   before you change it.
3. `briefs/brief-001-wow-and-contact.md` — the still-open work: the wow moment and
   the contact page.
4. `README.md` — the two-line version of the stack.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly;
the scheme only works if every agent uses it.

---

## 1. What this is

**tc-ventures.ca** — Thomas Cheesman's hiring-facing portfolio. Hand-written static
HTML, no framework, no build step, no CMS. Deployed to Cloudflare Workers static
assets, deploy-on-push from GitHub.

Deliberately **separate from thomascheesman.ca**, the personal and family site.
Nothing familial belongs here. Health is now a deliberate exception — see §3.

| | |
|---|---|
| Repo | `DriftingSplash9/tc-ventures-site` |
| Local | `C:\Users\thoma\Desktop\My Files\Website Projects\tc-ventures site` |
| Host | Cloudflare Worker `tc-ventures-site` (static assets only) |
| Config | `wrangler.jsonc` → serves `./public`, `not_found_handling: 404-page` |
| Deploy | push to `main` → Cloudflare builds → `npx wrangler deploy` |
| Also live at | `tc-ventures-site.thomasmcheesman.workers.dev` (see INFRA-1) |
| Registrar | WordPress.com (registration only) |
| DNS | Cloudflare nameservers `eoin.ns.cloudflare.com` / `hazel.ns.cloudflare.com` |
| Contact email | `thomas@tc-ventures.ca` — live, forwards to his main address |
| Fonts | self-hosted in `public/assets/fonts/`, nothing third-party |
| Résumé | built from `resume/resume-source.html` → `public/assets/Thomas-Cheesman-Resume.pdf` |

## 2. What was done (2026-09-12)

**The review.** Every block of copy on all four pages was extracted into
`reviews/copy-review-001.md`, numbered (H1–H12, P1–P15, B1–B16, S1–S4) and flagged.
Thomas marked up all of it in Word and returned it with his résumé. That document is
the record of his rulings; his answers are folded into the pages and into §3.

**Copy corrections, all four pages:**
- Health disclosure **decided: name it.** `background.html` says "I have Hajdu-Cheney
  syndrome, a rare connective-tissue disorder." His call, explicit, not a default.
- The accommodations sentence is **cut**, and replaced with "The work is remote and
  that is the only thing I need it to be." He needs no accommodation beyond working
  from home. The symptom detail he described in review does not go on the site.
- **All exact counts removed** — no 3,632 / 3,272 / 24,700 / grade tallies. Replaced
  on `projects.html` with a short block saying the corpus grows and any exact figure
  would be wrong by the time you read it, which makes the vagueness a statement of
  method rather than a dodge. Now a standing rule, §3.
- **Duration claims removed.** "In about eighteen months" is gone; what replaced it is
  that the three sites are three deliberately different designs, not one template
  reused. His point, and the stronger one.
- Kitchens corrected to 2002–2019 (17 years, matching the résumé) plus about a year
  of consulting afterward; culinary *arts*; human resources and staffing added.
- **87 units** reframed: 87 before the Margaret Edgson Manor fire, rebuild under way,
  final count not settled. Off the home page entirely.
- GPRS board entry rewritten in his words — created and publish the site; maintenance,
  marketing and special projects committees; fundraising committee starting.
- Education: "B.Sc. — credits earned"; Power Engineering 3B dropped (an error on his
  old résumé); Gas Plant Operator Levels 1 and 2.
- WordPress demoted, not deleted — out of headline prose, kept once in each spec
  table. He wanted it gone entirely ("training wheels"); it stays as a hiring keyword
  the nonprofit and small-org market filters on, and he accepted that.
- Email changed everywhere to `thomas@tc-ventures.ca`; "available now" → "open to
  work"; Mountain Time added to the footer.
- **404 rewritten** as "no document, no edge" — a 404 framed as a dependency that
  could not be sourced, with a small inline SVG of a broken edge and a dashed
  `unsourced` node. CSS only, no JS, `prefers-reduced-motion` respected.
- **Added:** Open Graph and Twitter card tags on every page (`@TCheesy_`), canonical
  URLs, `favicon.svg`, `robots.txt`, `sitemap.xml`.

**Fonts self-hosted.** Eight woff2 files in `public/assets/fonts/`, 324 KB, latin and
latin-ext. Familjen Grotesk and Source Serif 4 are variable fonts, so Google was
serving the same file once per weight — one file per family covers every weight via a
`font-weight` range. The `@font-face` block is at the top of `style.css`; the three
Google `<link>`s are gone from all four pages, replaced by two preloads.

**Résumé rebuilt.** Not edited — rebuilt as HTML rendered to PDF, so it carries the
site's own typography and the two documents look like one person made them. Source at
`resume/resume-source.html`; output at `public/assets/Thomas-Cheesman-Resume.pdf`.
Two pages, 9.6pt on generous leading, 0.8in / 0.9in margins — he asked for margins
that breathe and that constraint won over fitting one page. Every error above fixed.
**The influence graph and Rocket Lander were added; his old résumé mentioned neither**,
so a hiring manager reading only the PDF would never have learned the graph exists.
The old `.docx` is in `_unused/` at repo root, not deleted.

**Verified:** all four pages parse with balanced tags; all four font families load
from `/assets/fonts/` with no external requests; no console errors, no failed
requests, no horizontal scroll at 1280px or 390px in light or dark; the résumé is two
pages. **Not verified:** anything serving from the live domain.

### Traps worth knowing

- The folder a Cowork session connects by default is `Desktop\My Files\TC Ventures`,
  which is **empty and is not this repo**. The repo is
  `Desktop\My Files\Website Projects\tc-ventures site`. Request that path explicitly.
- `device_commit_files` with a `stagedPath` silently wrote a **stale** copy of the
  résumé — the tool reported success and the old bytes landed. Committing by
  `fileUuid` from `SendUserFile` worked. Check the byte count on the device after any
  commit that replaces an existing file.
- Reordering the résumé entries to fill the bottom of page 1 pushed the document to
  three pages, because `break-inside: avoid` moves a whole block. The current order
  packs correctly. Measure page count after any content change.

## 3. Current design

Light paper, near-black ink, one deep-teal accent (`#0F5F6B`), dark mode via
`prefers-color-scheme`. Familjen Grotesk (headings) / Source Serif 4 (body) /
IBM Plex Mono (labels and data). Reads as a well-set document, deliberately unlike
thomascheesman.ca's dark instrument-panel look. **Thomas confirmed he wants this
kept.** Stop re-litigating it.

**Standing rules:**
- `object-fit: contain`, never `cover`. Applies across all of Thomas's repos.
- Content must render without JavaScript.
- **JavaScript is allowed. Dependencies and a build step are not.** Inline vanilla JS
  enhancing HTML that already rendered. A library means copying a prebuilt bundle into
  `assets/` — never npm and a bundler in this repo.
- Fonts are self-hosted. Do not reintroduce a third-party font request.
- No phone number on the site. It is in the résumé PDF, and he is fine with that.
- **Never publish an exact node, edge, report or grade count.** The corpus grows and
  he intends to automate that growth. Round or describe — "nearly four thousand". He
  was emphatic; a precise figure goes stale in weeks and nobody updates the site.
- **No vanity metrics.** Line counts are out, by his instruction.
- **Do not invent dates or figures.** Where a date was unknown the résumé said "in
  development" until he supplied one. He holds strict-sourcing standards elsewhere and
  they apply here.
- Hajdu-Cheney syndrome is named on purpose. Symptom detail is not, and does not go on
  the site.
- The GPRS logo is **not** this site's favicon — it is another organisation's brand
  mark, and using it would read as this site belonging to them.
- Edit `resume/resume-source.html` and re-render. Never edit the PDF.

## 4. Open items — carry these forward until closed

### COPY
| # | Item | Notes |
|---|---|---|
| C-2 | **Rewritten pages unread by Thomas** | He signed off on the decisions, not on the sentences that implement them. He has seen the résumé. |

### CONTACT
| # | Item | Notes |
|---|---|---|
| CT-1 | **Contact page not built** | Decided: **no form.** He wrote both "should be a form" and "forget the form" in the same markup; asked directly, he chose no form. Do not reopen without him. |
| CT-2 | Blocked on the voice session | See §6.2. Writing it in the previous agent's voice is how the unreviewed health disclosure happened in the first place. |
| CT-3 | Nav "Contact" is still a `mailto:` | Fires the visitor's mail client unannounced. Fixed when the page exists. Add the page to `sitemap.xml` then — it was deliberately left out. |

### GRAPH
| # | Item | Notes |
|---|---|---|
| G-1 | **Wow decided: the live graph** | Chosen over the evidence-grading alternative. His constraints: **must not auto-load**, and demo something **simple** rather than the full corpus. |
| G-2 | Do not reuse the deployed bundle | The copy at `/reports-graph` on thomascheesman.ca is ~302 reports against a corpus near 4,000. Build a small demo from current data instead — one country's chain back to its foundational releases, ~100–150 nodes. Sidesteps the stale bundle entirely. |
| G-3 | Repo link unverified | `github.com/DriftingSplash9/Reports-Clustering` is linked from `projects.html`. Nobody has confirmed it is public or that its data matches. A dead link is worse than no link. |
| G-4 | Rocket Lander has no source link | The graph has one; this does not. He said he can make the repo public if it is private. |

### INFRA
| # | Item | Notes |
|---|---|---|
| INFRA-1 | **workers.dev duplicate** | Site also answers at `tc-ventures-site.thomasmcheesman.workers.dev`. Two public copies = an SEO own-goal. Fix: `"workers_dev": false`, `"preview_urls": false` in `wrangler.jsonc`. Keep while testing. |
| INFRA-2 | Favicon is a placeholder | `public/favicon.svg` is a TC monogram written this session. Thomas is finding the TC mark he used on thomascheesman.ca. Swap that one file; nothing else needs touching. He first sent the GPRS logo by mistake — see §3. |
| INFRA-4 | Permanent email undecided | `thomas@tc-ventures.ca` works and forwards. He has a few weeks to settle on something that is not his general address. |

### DOMAIN
| # | Item | Notes |
|---|---|---|
| D-1 | WordPress.com still claims the domain | tc-ventures.ca is still primary on the WP.com "TC 'ventures" site. DNS overrules it, so harmless, but detaching keeps the record honest. |
| D-2 | WP.com plan auto-renew | Three Premium plans on dormant sites; one renews 2027-09-18, one 2027-08-22, one already off. No refund window; the lever is auto-renew. **Do not cancel anything without confirming it won't disturb the DNS for the three live sites.** |
| D-3 | Professional Email expiry | Expired or expiring 2026-10-08 on the BYR-named WP.com site, auto-renew off. Related to INFRA-4. |

### OTHER REPOS
| # | Item | Notes |
|---|---|---|
| O-1 | Deployed graph bundle is stale | `/reports-graph` on thomascheesman.ca serves ~302 reports. Rebuild command is in that repo's `functions.php` comment. No longer blocks this site (see G-2) but is still wrong over there. |

**Closed this session:** C-1 (résumé errors — rebuilt), C-3 (unknown project dates —
supplied by Thomas), INFRA-3 (Google fonts — self-hosted). Nothing was killed.

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

1. **See it serve.** Everything in §2 is on disk and has never been loaded from the
   live domain. Check the 404's inline SVG in both colour schemes and at 390px, check
   the self-hosted fonts serve with the right content type, and check an OG preview
   renders when the link is pasted somewhere.
2. **The voice session.** Thomas offered one — goals, family, health, Hajdu-Cheney —
   and pointed at the prose on his own sites as the source for how he writes. Do this
   **before** writing the contact page. Tag: `CONTACT`.
3. **Build the contact page.** No form. The job is to answer the hesitation: is he
   available, will he reply, what happens next, does the time zone work, what should
   I send. Different first moves for different readers. He pushed back on the "what
   happens next" idea ("do you expect fireworks?") — the argument that landed is that
   the reader does not *know* he will reply, and one sentence removes the doubt. Keep
   it to one sentence. Tags: `CONTACT`, `COPY`.
4. **Then the graph demo.** See G-1 and G-2. Small, deliberate, does not auto-load.
   Tag: `GRAPH`.
5. **Close INFRA-1** (turn off workers.dev) once the site is settled.
6. **Later, not now:** the Godot rocket lander web build. Blocked on the game itself
   (no touch controls; Tab opens the tuning panel and fights the browser), and parked
   until the graph project is more or less self-updating. Tag: `LANDER`.
