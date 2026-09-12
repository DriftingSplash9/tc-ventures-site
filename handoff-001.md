# handoff-001 — tc-ventures.ca

**Written:** 2026-09-11
**Covers:** everything from a standing start to a live site on the domain.
**Status at wrap:** site is LIVE at https://tc-ventures.ca and resolving correctly.

---

## 0. Read this first if you are a fresh agent

1. This file, top to bottom.
2. `briefs/brief-001-wow-and-contact.md` — the next piece of work.
3. `README.md` — the two-line version of the stack.

Then say what you understand the next job to be, and check before building.
§5 defines how you write the handoff that replaces this one. Follow it exactly;
the scheme only works if every agent uses it.

---

## 1. What this is

**tc-ventures.ca** — Thomas Cheesman's hiring-facing portfolio. Hand-written
static HTML, no framework, no build step, no CMS. Deployed to Cloudflare Workers
static assets, deploy-on-push from GitHub.

It is deliberately **separate from thomascheesman.ca**, which is the personal and
family site (heritage archive, kids, an in-browser pinball game, a "desk" metaphor
navigation). Nothing personal, familial or medical belongs on tc-ventures.ca.

| | |
|---|---|
| Repo | `DriftingSplash9/tc-ventures-site` |
| Local | `C:\Users\thoma\Desktop\My Files\Website Projects\tc-ventures site` |
| Host | Cloudflare Worker `tc-ventures-site` (static assets only) |
| Config | `wrangler.jsonc` → serves `./public`, `not_found_handling: 404-page` |
| Deploy | push to `main` → Cloudflare builds → `npx wrangler deploy` |
| Also live at | `tc-ventures-site.thomasmcheesman.workers.dev` (see §4) |
| Registrar | WordPress.com (registration only) |
| DNS | Cloudflare nameservers `eoin.ns.cloudflare.com` / `hazel.ns.cloudflare.com` |

## 2. What was done (2026-09-10 → 2026-09-11)

**Origin.** Thomas had a meeting at an employability service and wanted to know how
to present two projects that weren't on his résumé: the Economic Report Influence
Graph and a Godot rocket-lander game.

**On thomascheesman.ca (the other repo — done, deployed):**
- Built `page-projects.php` + `assets/css/projects.css` + screenshots, live at
  `/projects`, added to the header nav under "Elsewhere".
- **Trap worth knowing:** `C:\Users\thoma\tc-ventures-child-theme` is a STALE clone
  (v1.0.11, April). The real theme is `Desktop\My Files\tc-ventures-child-theme`
  (v1.0.75x). Work went into the stale one first and had to be redone.
- **Trap worth knowing:** running `git status` in that repo over the device mount
  strands `.git/index.lock` and blocks his GitHub Desktop. Rename, never delete.

**The WordPress.com audit:**
- Three WordPress.com **Premium** plans on dormant Simple sites, plus four domain
  registrations. All three live sites are served by Hostinger, not WordPress.com.
- Premium = Simple platform = no plugins, no SFTP, no custom code. It can never
  host the Godot build, the graph bundle, or hand-written HTML. That is why this
  site exists on Cloudflare instead.

**This site, built from nothing:**
- `public/index.html` — name, positioning, three proofs, "How I work", what he wants
- `public/projects.html` — the graph and Rocket Lander in detail, plus the three
  live WordPress sites
- `public/background.html` — kitchens → software, skills, experience, résumé download
- `public/404.html`, `public/assets/style.css`, two graph screenshots, the résumé
- Deployed, custom domain attached, DNS verified, resolving.

**Domain path (for context, all complete):** tc-ventures.ca was registered at
WordPress.com and mis-attached to the GPRS site → moved to the TC 'ventures site →
zone added to Cloudflare → nameservers switched → old WordPress A records deleted →
Worker custom domain attached → resolves.

## 3. Current design

Light paper, near-black ink, one deep-teal accent, dark mode via
`prefers-color-scheme`. Familjen Grotesk (headings) / Source Serif 4 (body) /
IBM Plex Mono (labels and data). Chosen to contrast with thomascheesman.ca's dark
instrument-panel look: this should read as a well-set document.

Verified headless: no console errors, no horizontal scroll at 390px on any page.

**Standing rules:**
- `object-fit: contain`, never `cover`. Applies across all of Thomas's repos.
- Content must render without JavaScript.
- No phone number on the site (it's in the résumé download).

## 4. Open items — carry these forward until closed

| # | Item | Notes |
|---|---|---|
| 1 | **Copy not reviewed by Thomas** | The site makes claims in his voice — "available now", what he's looking for — that he has not signed off. Highest priority; it is public. |
| 2 | **Health disclosure wording** | `background.html` says "a connective-tissue condition made kitchen work unsustainable". Thomas names Hajdu-Cheney openly on his other sites. Naming it here is HIS call, not a default. |
| 3 | **workers.dev duplicate** | Site also answers at `tc-ventures-site.thomasmcheesman.workers.dev`. Two public copies = an SEO own-goal. Fix: `"workers_dev": false` and `"preview_urls": false` in `wrangler.jsonc`. Keep while testing. |
| 4 | **WordPress.com still claims the domain** | tc-ventures.ca is still the primary domain on the WP.com "TC 'ventures" site. DNS overrules it, so harmless, but detaching keeps the record honest. |
| 5 | **WP.com plan auto-renew** | Three Premium plans on dormant sites; one renews 2027-09-18, one 2027-08-22, one is already off. Purchases are >2 years old so there is no refund window — the lever is auto-renew, not cancellation. **Do not cancel anything without confirming it won't disturb the DNS for the three live sites.** |
| 6 | **Professional Email expiry** | Expired or expiring 2026-10-08 on the BYR-named WP.com site, auto-renew off. |
| 7 | **`/graph` and `/lander` on this domain** | Long-term: host the graph and the Godot build here. See §6. |
| 8 | **Deployed graph bundle is stale** | The copy at `/reports-graph` on thomascheesman.ca is ~302 reports; the corpus is 3,632. Rebuild command is in that repo's `functions.php` comment. |

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
  `index.lock` notes in §2 are the model.
- **Never claim something is done that you have not verified.** "Deployed" means you
  saw it serve. "Written" means it is on disk. Say which.
- **Do not state git state and do not tell Thomas to commit.** That is his routine.
- Keep it under ~400 lines. If §2 is getting long, you are writing a diary.

## 6. Next up

In order:

1. **Get Thomas to read the live site.** Items 1 and 2 in §4 are copy about him,
   already public, unreviewed. Nothing else should ship before that is settled.
2. **`briefs/brief-001-wow-and-contact.md`** — the portfolio "wow factor" and the
   contact page. Propose the direction before building. Tags: `DESIGN`, `CONTACT`.
3. **Close item 3** (turn off workers.dev) once the site is settled.
4. **Then** consider `/graph` — a live, interactive version of the influence graph
   on this domain, which is the strongest single thing this portfolio could have.
   Tag: `GRAPH`.
5. **Later, not now:** the Godot rocket lander web build. It is blocked on the game
   itself (no touch controls; Tab opens the tuning panel and fights the browser),
   and Thomas has parked it until the graph project is more or less self-updating.
   Tag: `LANDER`.
