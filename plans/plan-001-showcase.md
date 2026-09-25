# plan-001 — tc-ventures.ca, from skeleton to showcase

**Written:** 2026-09-21 · **Status:** approved 2026-09-21 — answers in §6. Q5 has a default pending his word.
**Scope:** tc-ventures.ca only. No work on the other three sites except where a
case study needs a screenshot or a fact.

---

## 1. The problem, stated plainly

The site *says* Thomas directs AI well. It never *shows* it. Every page describes
results (a graph, a farm, a desk, four sites) and asserts a method ("specify
before building", "evidence over assertion"). A hiring manager has to take the
method on trust — which is exactly what the method itself says not to do.

Meanwhile the evidence of the method already exists and is unusually good:

| Evidence that exists today | Where |
|---|---|
| 13 numbered handoffs with fixed rules, workstream tags, traps, open-items tables carried forward | this repo, root |
| A written brief in Thomas's words, and agents working to it | `briefs/brief-001-wow-and-contact.md` |
| A 589-line copy review where Thomas ruled on every block (OK / CUT / FIX / SOFTEN) | `reviews/copy-review-001.md` |
| Standing rules born from specific corrections: no exact counts, no vanity metrics, no "WordPress" in headlines, "cheesy" lines cut, unfinished work kept off, children's names kept off | handoffs §3, decisions doc |
| A validator that fails the graph build on a dangling reference; extraction playbooks; A/B/C evidence grades | `Reports Clustering/` |
| A crawl audit that found a host-level fault, then a fix verified live | `Claude outputs/byr-crawl-audit.md`, handoff-011/012 |
| A version series for the personal site (`V0.NN.md`) | `tc-ventures-child-theme` |

**The thesis for the rebuild:** the product is judgement. Show the brief, the
spec, what the AI got wrong, how it was caught, and what shipped — with receipts.

## 2. What "done" looks like

A hiring manager, in order:

1. **10 seconds (home):** sees one sentence of what he does, and one live,
   real thing he built — not a stock effect. Knows this is not a template site.
2. **2 minutes (a case study):** sees the loop — brief → spec → AI output →
   the catch → the fix → the result — on real work, with links to the actual
   files and commits.
3. **5 minutes (method):** understands *how* he runs AI across many sessions
   without drift (handoffs, rules, validators, reviews), and that he can explain
   it plainly.
4. **Contact:** writes to him, because the page made it easy and specific.

And the site itself passes the standards it claims: fast, accessible, valid,
secure headers, correct link previews.

## 3. New structure

| Page | Job | Status |
|---|---|---|
| `/` Home | The argument in ten seconds, and the way in | rebuild |
| `/work/` | Index of case studies | **not built, ruled 2026-09-25**: case studies sit in a sub-menu under Projects instead |
| `/work/influence-graph` | Case study — the graph (keeps the live demo) | split out of projects |
| `/work/back-quarter` | Case study — the drivable homepage | split out of projects |
| `/work/desk-and-drawer` | Case study — the photograph menu | split out of projects |
| `/work/bare-your-rare` | Case study — making a patient site legible to AI assistants (the audit, the schema, the host fault, the fix, verified) | new |
| `/work/gprs` | Case study — the Grande Prairie Residential Society site: a volunteer nonprofit's public site, run solo since 2023, through the Margaret Edgson Manor fire and rebuild | new (ruled 2026-09-21) |
| `/work/this-site` | Case study — tc-ventures.ca itself, built across numbered handoffs | new |
| `/method` | **The centrepiece.** How he directs AI | new · **its own menu item, ruled 2026-09-25** |
| `/background` | Kitchens → career change → now; experience; résumé | tighten |
| `/contact` | One address, done properly | finish (brief-001) |
| `/404` | Keep — it is already on-thesis | keep |

~~`/projects.html` becomes a redirect to `/work/`~~ **Ruled 2026-09-25: no.** There is no
`/work/` index; `/projects` stays, with the case studies in a sub-menu under it (live
2026-09-24). GPRS gets its own case study (ruled 2026-09-21), so the
case-study template is used seven times, not six.

## 4. The pieces, in detail

### 4a. The case-study template (one component, used seven times)

Fixed sections, same order every time, so the method is visible by repetition:

1. **The ask** — the brief, in his words where a written one exists.
2. **The standard** — what "good" meant, written down before building.
3. **What the AI got wrong** — two or three real, specific misses. Sourced from
   handoff traps and review rulings, never invented.
4. **How I caught it** — the check that found it (a measurement, a validator, a
   read-through, a live fetch).
5. **What shipped** — figure(s), live link, the honest limits.
6. **Receipts** — links to the actual files: the handoff that recorded it, the
   commit, the validator, the review.

Rule: every claim in sections 3–4 links to a receipt or is cut. *No document, no
edge* applied to his own portfolio.

### 4b. The Method page

Short, concrete, and built from real artefacts, not adjectives:

- **The loop** — one diagram (inline SVG, both themes): brief → spec → build →
  review → rule → next session. Each node links to a real example.
- **Handoffs** — what they are, why numbered, why never forked. Show the fixed
  §5 rules verbatim (they are generic and already public in the repo).
- **Rules that came from corrections** — a table: the correction Thomas made →
  the standing rule it became → where it is enforced. E.g. "a line reading like
  an agency site was cut" → "hiring voice, no selling"; "exact node counts drift"
  → "never publish an exact count"; "WordPress reads as training wheels" → "once
  per spec table only". Each with a receipt.
- **Validators over vibes** — the graph's validator failing the build on a
  dangling reference; the crawl audit checking live HTML instead of the editor.
- **Where AI is weak and what he does about it** — plausible-but-wrong facts,
  drift across sessions, invented numbers, over-polish. One line each and the
  counter-measure. This is the section a technical hiring manager will read
  twice.

### 4c. The home-page "wow" — proposal, needs a yes (§6 Q2)

Not a stock effect. Two candidates, both built from his own material:

- **A — The build ledger.** A compact, live visual of this site's own history:
  every handoff as a mark on a timeline, open items opening and closing across
  sessions by workstream, traps logged. Click a mark to read its one-line state.
  Data comes from a small script (like `scripts/export-gp-budget.py`) that reads
  the handoffs and writes a curated JSON — **curated, never raw**, because the
  handoffs contain personal material. No build step: the script runs by hand,
  the JSON is committed. It shows, in one glance, disciplined multi-session AI
  work — which nobody else's portfolio can show.
- **B — The graph, promoted.** The existing gp-budget graph slice moved up to
  the home page behind the same click gate. Proven, already built, but it is
  "a 3D graph", which reads as a demo rather than a method.

Recommendation: **A on home, B stays on its case study.** A is the thing only he
has.

### 4d. Design — layout, not palette

Palette, fonts and dark mode are settled (handoff §3) and stay. The "skeleton"
feel is layout and rhythm:

- One type scale and spacing scale written down as tokens; applied everywhere.
- A proper page grid with a wide lane for figures and a reading lane for prose.
- Components: case-study header (title, one-line claim, stack, status, live
  link), receipt links (small, mono, consistent), figure + caption, rule table,
  the loop diagram, pull quote for his own words.
- Per-page Open Graph images, made from real figures.
- Screenshots re-framed consistently (same aspect per slot, `contain`, no crop
  that hides the point).

### 4e. Engineering quality — the site as its own evidence

- Security headers via a `_headers` file (CSP, referrer policy, permissions
  policy, HSTS) — static-assets Workers support this without code.
- Structured data: `Person` + `ProfilePage` on home, `CreativeWork` per case
  study, `BreadcrumbList`.
- Sitemap updated for the new URLs; `_redirects` for old ones.
- A performance budget per page, checked before every push (a small script in
  `scripts/`). Whether any figure appears *on* the site is §6 Q5.
- Everything still renders without JavaScript.

### 4f. Contact — finish brief-001

Keep: one address, no form, copy button, local time. Add: what to include in a
first message (role, hours, remote), what he is looking for in one line, and the
reply promise. Nothing generic.

## 5. Order of work (one session each unless noted)

| # | Session | Output | Needs from Thomas |
|---|---|---|---|
| 1 | **Answers + content inventory** | §6 answered; a receipts list: every candidate "AI got it wrong / how caught" story, each with its file and date | the §6 answers |
| 2 | **Design system + templates** | tokens, grid, components, case-study template on one page with placeholder copy | look and say yes/no |
| 3 | **Method page** | full draft, diagram, rules table with receipts | read + rule on it (copy-review style) |
| 4–5 | **Case studies** | graph, back quarter, desk split out and rebuilt; BYR and this-site written new | read + rule |
| 6 | **Home + the wow** | new home; build ledger (if Q2 = A) with its export script | yes/no on the ledger |
| 7 | **Background + contact** | tightened background, finished contact | read + rule |
| 8 | **Engineering pass** | headers, schema, OG images, redirects, sitemap, budget script; verify live | push |
| 9 | **Thomas's accessibility pass** | his run-through once design and content are final | him |

**Ruled 2026-09-25:** the four remaining case studies come **before** the build ledger (row 6),
in this order: the influence graph, then Bare Your Rare, then the Back Quarter and the Desk and
the Drawer together (one receipts pass over thomascheesman.ca covers both). Design waits until
the content is mostly in place. Drafts go in `reviews/copy-review-004.md`.

Every session ends with the next numbered handoff. Copy is drafted, then put in
front of Thomas in the copy-review format (numbered blocks, OK / CUT / FIX)
before it ships.

## 6. Thomas's answers (2026-09-21)

1. **Lead role:** "lead with the one most likely to fit my skills and abilities."
   Chosen: **nonprofit technology** — the person a small nonprofit hires to run
   its website and digital operations. Reasons: it is the one he already does
   (GPRS site since 2023, board member, committees); it uses the kitchen years
   directly (budgets, suppliers, systems, staff); it rewards the generalist who
   can build, write plainly and run the operation, where junior web-development
   roles are crowded and gated on hand-coding tests, and accessibility-specialist
   roles are gated on audit certifications. Accessibility and plain language stay
   as strengths *inside* that pitch, not a separate one. The other three roles
   remain named once on Background and Contact. **Thomas can overrule.**
2. **Home-page wow:** **A — the build ledger.** The graph demo stays on its case study.
3. **Process excerpts on the pages:** **yes** — curated excerpts from handoffs and
   the copy review, and real AI misses he caught. Curated, never raw; nothing
   personal; every excerpt read against the privacy rules before it ships.
4. **GPRS:** **its own case study** (`/work/gprs`).
5. **Page weight / accessibility results on the site:** explained to Thomas
   2026-09-21. **Default unless he says otherwise:** show them once, as evidence,
   inside `/work/this-site` (e.g. "every page under N KB; zero errors in automated
   accessibility testing, checked before each push"), not on every page footer.
   The numbers are measured by the budget script in §4e, never typed by hand.

## 7. Constraints carried from the standing rules

Hand-written static HTML, no framework, no build step · content renders without
JS · nothing heavy loads before a click · fonts self-hosted · `object-fit:
contain` · no phone number · no exact node/edge/report counts in copy · no
vanity metrics · no invented dates or figures — unknown means ask · WordPress
once per spec table, never in headlines · nothing familial beyond the Back
Quarter paragraph · children's names never, including inside screenshots · the
the private project stays private · show finished work, label anything unfinished ·
hiring voice, first person, past tense, no selling · palette and fonts settled.
