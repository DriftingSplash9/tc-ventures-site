# Copy review 003 — Phase 1 copy

**Written:** 2026-09-23
**Why:** Phase 1. Copy for `/work/gprs`, `/work/this-site` and `/method` will be added here
as it is drafted from `plans/receipts-001.md`. The first block is a correction found by
the receipts inventory.
**Status:** R1 ruled OK 2026-09-23 and applied to `public/index.html`. **G1–G8 (`/work/gprs`)
drafted 2026-09-23, ruled and shipped 2026-09-24** (see "Rulings" at the end).

Same format and marks as copy-review-001/002: `OK` · `KEEP` · `A` / `B` · `FIX` · `CUT`.

---

### R1 — home page, "How I work" card: the measurement-script sentence

> **Now:** A layout force I had already shipped turned out to have been calibrated against
> a measurement script with a bug in it. I found that, threw out the calibration, and
> rebuilt it.

**⚠ FLAG — does not match its receipt** (receipts-001 F-1). The receipt says the 1/d²
calibration was "a real false start, caught before shipping"
(`Reports Clustering/archive/Previous Handoffs/HANDOFF-2026-08-28-pre-trim-032.md`
L256–263; receipts-001 R-061).

> **Proposal:** A layout force I was about to ship turned out to have been calibrated
> against a measurement script with a bug in it. I caught that before it went out, threw
> out the calibration, and rebuilt it.

**Ruling (2026-09-23): OK.**

---

## `/work/gprs` — the GPRS case study (G1–G8)

**Drafted 2026-09-23** from the two OK receipts in `plans/receipts-001.md` §3A (R-001,
R-007), the live Projects and Background copy, handoff-015 C-13, and the public GPRS repo
(`DriftingSplash9/gprs-site`). No new fact is asserted. Where one would be needed, it is a
question. Every link in the preview returned 200 on 2026-09-23.

**Read first: this case study is thin, and says so.** Only two GPRS receipts survived the
ruling, and the site predates your session records (F-4). The draft does not pad that out.
It says so in G6's "honest limits". If two misses is too few, the choice is between
un-cutting a GPRS row (R-004 the "Own the public website" copy or R-006 the P3 photo
colour bug are both public-safe) and leaving it at two.

### G1 — header

> **Label:** Case study · gpresidentialsociety.com
> **H1:** A housing society's website
> **Claim:** The public site of a volunteer-run housing nonprofit, which I have built and
> run on my own since 2023, at no cost to the society.
> **Spec table:** Stack: WordPress with a hand-coded Astra child theme · page content lives
> in the theme, not the editor · Status: Live · Hosted: Self-hosted on Hostinger · a push
> to `main` deploys · Repo: DriftingSplash9/gprs-site · Since: 2023 · rebuilt 2025

WordPress appears once, in the spec table. "At no cost to the society" is from the live
Projects page.

### G2 — The ask

> **H2:** A board seat, and a site nobody was paid to run
>
> The Grande Prairie Residential Society is a volunteer-run nonprofit providing
> barrier-free housing: 87 units before the Margaret Edgson Manor fire, with the rebuild
> under way and the final count not yet settled. I joined the board in June 2023, and the
> website is my donation to it.
>
> The first version went up on WordPress.com in 2023. In 2025 I rebuilt it as a
> self-hosted site:
>
> > "…because I wanted more freedom to experiment with the code." (Thomas, on the 2025
> > rebuild · handoff-015, C-13)

**⚠ FLAG.** There is no written brief for GPRS, so "the ask" has no brief to quote. The
pull quote is the only thing on record in your words, and it covers the 2025 move, not
the site's purpose.

**Q-G1:** In one or two sentences, what did the society need the site to do? If you give
a line, it replaces the pull quote. If not, the pull quote stays.

### G3 — The standard

> **H2:** Written into the repo, for every agent that opens it
>
> Accessibility and plain language are first-order requirements on this site, not
> decoration. The working rules live in one file at the top of the repo, and every AI
> agent reads it before it changes anything.
>
> *Excerpt, verbatim from `AGENTS.md`:* the "content is in theme PHP" rule, "Treat every
> push as publishing", and "Run `php -l` on every changed file first".

**⚠ FLAG.** The "Treat every push as publishing" line in the excerpt mentions copy
"awaiting board or marketing approval" and "a motion not yet declared carried". It is
already public in the repo, but quoting it on a hiring page puts it in front of more
readers. **A:** keep it verbatim. **B:** cut that line and keep the other two.

### G4 — What the AI got wrong

> **H2:** Two misses, both confident
>
> **1. An audit of a site that no longer existed.** In March 2026 I had more than one AI
> tool audit the site. One gave it a failing score and listed what it lacked: a hero
> section, calls to action, a donate button. The live site had all three. The tool had
> reviewed an old copy of the site, or invented one.
>
> **2. "Safe to push," three times.** In September 2026 the agent working on the site told
> me three times that pushing changes was safe, because the site had no automatic
> deployment and needed a manual step to go live. It wrote that manual step into the repo.
> There was no manual step: the host picks up every push within a minute or two.

No tool is named, and "a failing score" stands in for the exact score (58/100).

**⚠ FLAG on 2 — the consequence.** R-007's ruling says "describe the miss, not what was
published". The draft leaves out what went live. But **commit 5a68be4, which the page
links as a receipt, says in its message that copy gated on an uncarried board motion was
published.** Linking the commit puts that one click away. **A:** link the commit anyway
(it is already public). **B:** link `AGENTS.md` "Deploying" instead, which states the
rule without the story.

### G5 — How I caught it

> **H2:** By checking against the real thing
>
> **1. Read it against the code.** Another audit had been given the theme's code and told
> to reference it. Side by side, the first audit's findings matched nothing on the live
> site, and I discarded it. The standard audit prompt now says to read the actual code and
> not guess from the front end.
>
> **2. Asked why the site already looked updated.** The live pages already carried the
> change. The agent fetched them to confirm it, and the deploy notes were rewritten the
> same day to say a push is a publish. The wrong belief had been written into three
> separate notes, which is why it looked settled.
>
> *Rules table:* two rows, one per miss.

**⚠ DOUBT on 1 (not overridden, reported).** The receipt says the rule became "read and
reference the actual code, do not guess". That wording is in the standard prompt in
`AUDIT-NOTES.md` (L24, L88), and the file is dated 2026-03-25, the day after the failing
audit. But I could not confirm that the line was **added because of** that audit. It may
have been in the prompt all three tools were given. If it was already there, sentence 3
of block 1 is wrong. **Q-G2:** Was "read the actual code" added after the failing audit,
or was it there from the start?

`AUDIT-NOTES.md` is not in a public repo, so R-001's receipt link goes to the receipts
inventory, not the source file.

### G6 — What shipped

> **H2:** A live site the society does not pay for
>
> The site is live at gpresidentialsociety.com, including the society's Margaret Edgson
> Manor rebuild page.
>
> **The honest limits:** Most of this site was built before I kept session records, so
> there are no handoffs from 2023 to 2025 and this page has two receipts, not more. The
> repo starts in April 2026, as a copy of the theme already running live.

"Starts in April 2026" comes from the repo's first commit (2026-04-22, "Initial commit —
GPRS child theme baseline from live site").

**Q-G3:** The page needs a figure. Recommendation: I take a desktop screenshot of the
live home page and one of the rebuild page, look at both before they go in, and you
confirm neither shows a resident, a name or a photo that shouldn't be on a hiring site.
Yes / no?

### G7 — Receipts

`gprs-site/AGENTS.md` · commit `953907a` (the manual deploy procedure that did not
exist) · commit `5a68be4` (the correction; see the G4 flag) · `receipts-001.md` §3A ·
`handoff-015.md` C-13.

### G8 — what goes with it (not copy)

When G1–G7 are ruled: remove the draft banner and the `.assetsignore` line, add
`/work/gprs` to the sitemap, and **decide the nav**. There is no `/work/` index yet, so
the rail's "← All work" link points at `/projects`. **Q-G4:** Should Projects link to
the case study from the GPRS paragraph until `/work/` exists?

---

### Rulings on G1–G8 (Thomas, 2026-09-24)

- **Thin: leave it at the two.** "It is ok that GPRS is thin because I made that site. I
  made it before I knew these lessons."
- **Q-G1 answered, verbatim:** "What we need the site to do: inform potential tenants how
  to apply, how to determine if they qualify, and if we are the right fit for them. We
  don't have a physical office so this is our main interface with the community."
  **Applied:** it replaces the pull quote. The C-13 line moves into the prose as a paraphrase
  with its receipt.
- **Q-G2: "i don't recall."** So the claim that the audit prompt changed *because of* the
  failing audit is **cut** from G5 block 1. The rule is kept as present practice ("an audit
  that does not cite the code does not count"). It does not say when it started.
- **G4 flag: B.** Commit `5a68be4` is no longer linked from the page. Miss 2's catch
  links `AGENTS.md` "Deploying" instead. Commit `953907a` (the wrong procedure) stays.
- **Q-G3: ok.** Screenshots taken 2026-09-24 (headless Chrome, 1280×720, light scheme),
  saved as `assets/img/gprs-home.webp` and `gprs-rebuild.webp`, and in `.assetsignore`
  until ruled. Neither shows a person. **⚠ FLAG:** the home-page hero carries a quote
  attributed by name ("Travis McNally (2004)"). The rebuild page quotes Lesra Martin, a
  public figure. **Q-G5:** Is the named quote on the home screenshot OK on a hiring page?
- **Q-G4: yes.** When `/work/gprs` ships, the GPRS paragraph on Projects links to it.
  Not applied yet: the link would 404 until the page is live.

**Still open:** G3 (A keep the "Treat every push as publishing" line verbatim, or B cut it)
and Q-G5. Then G1–G7 as a whole: OK to ship?

**Ruled 2026-09-24:** Q-G5 the McNally quote is fine · **G3 A** (excerpt stays verbatim) ·
**G1–G7 OK to ship.** Shipped 2026-09-24: draft banner, `noindex` and the `.assetsignore`
lines removed; title, description and link-preview tags taken from G1; `/work/gprs` added
to the sitemap; Projects' GPRS paragraph links to it (Q-G4).

### G9 — home page, "Four live sites" card: a way in to `/work/gprs`

> **Proposed:** …gpresidentialsociety.com for a volunteer-run nonprofit providing
> barrier-free housing (read the case study), thomascheesman.ca, and this one…

The case study had no link from the home page or the menu. "Work" goes in the menu once
`/work/` exists (after `/work/this-site`).

**Ruling (2026-09-24): A.** Applied to `public/index.html`.
