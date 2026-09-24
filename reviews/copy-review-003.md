# Copy review 003 — Phase 1 copy

**Written:** 2026-09-23
**Why:** Phase 1. Copy for `/work/gprs`, `/work/this-site` and `/method` will be added here
as it is drafted from `plans/receipts-001.md`. The first block is a correction found by
the receipts inventory.
**Status:** R1 ruled OK 2026-09-23 and applied to `public/index.html`. **G1–G8 (`/work/gprs`)
drafted 2026-09-23, ruled and shipped 2026-09-24** (see "Rulings" after G8). **T1–T10
(`/work/this-site`) drafted 2026-09-24, not yet ruled.**

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

---

## `/work/this-site` — the case study of this site (T1–T10)

**Drafted 2026-09-24.** Sources: the seven OK rows in `plans/receipts-001.md` §3B (R-011,
R-019, R-022, R-024, R-027, R-028, R-029). I re-opened each receipt before writing, the
draft in `_template.html`, and `handoff-016.md` §3 and §5. Already ruled: **PL-8 ship
without page-weight or accessibility numbers**, and **the lead misses are R-024, R-028 and
R-011** (Thomas, 2026-09-24).

Preview: `public/work/this-site.html`, with a draft banner and `noindex`. It and its two
figures are in `.assetsignore`, so none of it deploys. On 2026-09-24 every link on the page
returned 200. The two exceptions are expected: LinkedIn answers scripts with 999, and the
page's own canonical address 404s until it ships. The five section anchors are confirmed on
GitHub's rendered pages.

**What happened to the template's three misses.** The screensaver names are **P-03
(private, CUT)**. "Available now" is **R-013 (CUT)**. Only "exact counts" is **R-011 (OK)**.
The first two are gone and do not come back.

**⚠ Two template claims were false, and both are fixed in this draft.**
1. **"All caught before they shipped."** All three lead misses were live before they were
   caught:
   - **R-011:** copy-review-001's header says "every word below is live right now".
   - **R-028:** "it silently killed analytics for one deploy" (handoff-015, traps).
   - **R-024:** the 2026-09-16 `graph-demo.js` (`0e7544d`) hides the button with no
     `.focus()` call. It was deployed per handoff-007. The fix came 2026-09-21 (`5679e0f`).
2. **"The first drafts stated" the counts.** They were live copy, not drafts.

### T0 — ⚠ FLAG, read first: what the page links to

The repo is public, but linking a file from a hiring page puts it in front of more readers
(R-026 is the rule: every receipt is read against the privacy rules before it links).
Private-topic mentions in the files this page links, counted with grep:

- **Rocket Lander.** Every linked handoff mentions it: 002, 012, 015 and 016. brief-001 was
  redacted for exactly this (R-026). `/work/gprs` already links handoff-015.
- **Health disclosure.** handoff-002 records the decision to name the condition, and "the
  symptom detail he described in review does not go on the site".
- **Family.** Handoffs 012, 015 and 016 carry the family rules ("the parents", "children's
  names never"). These are rules, not names.

**Not linked at all: `reviews/copy-review-001.md`.** The template linked it five times. It
debates the health disclosure over three flags, carries the career-gap "family care" and
"caregiver" blocks (private under P-05), and describes the lander. R-011 now links
receipts-001 and handoff-002 §3 instead. The loop's "Review" node links copy-review-003.
Two table rows (R-019, R-022) link receipts-001 rather than handoff-005 and handoff-008,
because handoff-008 mentions the lander 35 times.

**A (recommended):** link handoffs 002, 012, 015 and 016 as they are. The page's own "Repo"
link and the footer's GitHub link already put every handoff one click away, so redacting
four files would hide nothing.
**B:** redact those four the way brief-001 was redacted, marked in each file.
**C:** no handoff links at all. Route everything through receipts-001 and `CLAUDE.md`.

### T1 — header

> **Label:** Case study · tc-ventures.ca
> **H1:** This site
> **Claim:** The site you are reading, built with AI agents one numbered session at a time.
> The handoffs, the rules and my rulings on its copy are public in the repo.
> **Spec table:** Stack: Hand-written HTML and CSS, with a little JavaScript on top · one
> stylesheet · no framework, no build step · Status: Live, rebuild in progress · Hosted:
> Cloudflare, static files · a push to `main` deploys · Repo: DriftingSplash9/tc-ventures-site
> · Since: September 2026 · one numbered handoff per session
> **Page title / link preview:** How this site was built - Thomas Cheesman

Changes from the template:
- **"07" dropped from the label.** `/work/gprs` has no number.
- **"handoff-001 to handoff-013" became "one numbered handoff per session".** A range goes
  stale with the next handoff.
- **The claim no longer says "every claim checked against the file that actually served".**
  R-028 shows that was not always true.

The title differs from the H1 because a search result or link preview shows only the title,
and "This site" alone says nothing there. "Since September 2026": the first commit is
2026-09-10, and handoff-001 (2026-09-11) records the site live.

### T2 — The ask: the pull quote

> **H2:** What I asked for, in my own words
>
> "Being a bit of a portfolio it should be unique, detailed, complex, and push the limits of
> what is modern with AI-assisted web design. It needs a 'wow' factor. Also, the contact page
> is not done and will get some special attention because contact pages always seem like a
> lame afterthought and they are generic." (Thomas · 2026-09-11 · brief-001)

This is still word for word in the redacted `briefs/brief-001-wow-and-contact.md`, which says
your quote was left untouched. **The date:** the brief has no date line. handoff-001, written
2026-09-11, names it as the next piece of work, and git first shows it on 2026-09-12. I used
09-11.

### T3 — The ask: the paragraph under it (PL-4, my wording)

> **Now (template):** I was looking for work, and "I build with AI" proves nothing on its
> own. So the site had to show it: built to the same rules it describes, with the working
> files left public for anyone to check.
>
> **Proposal:** "I build with AI" proves nothing on its own. So this site had to show it:
> built to the rules it describes, with its handoffs, reviews and plans public for anyone to
> check.

Two changes:
- **"I was looking for work" is gone.** Past tense reads as if the search is over. Present
  tense would be a claim that goes stale, the R-013 problem.
- **"The working files" became the named ones.** Not every working file is public: the raw
  receipts and the private résumé copies are not.

**OK** the proposal, **KEEP** the template, or give me your own line, as you did for Q-G1.

### T4 — The standard

> **H2:** What "good" meant, written down first
>
> Each session starts by reading the newest handoff: a numbered file that says where things
> stand and which rules hold. A session that changes anything ends by writing the next one.
> The rules carry forward; the story of each session does not. (→ handoff-016 §5)
>
> *Excerpt, verbatim from `handoff-016.md` §3:* "Content renders without JavaScript", "Never
> publish an exact node, edge, report or grade count", "Do not invent dates or figures", "Copy
> ships only through a copy review".

A script checked that each excerpt line matches the handoff exactly. It failed on a copy with
one word changed, so the check can fail. The excerpt now quotes handoff-016 instead of
handoff-013, because 016 is current.

Two template sentences are cut:
- "Every session started from a handoff… and ended by writing the next one." The first
  session had no handoff to start from, and §5 says a session that changed nothing writes
  none.
- "Most of them were born from a specific mistake, and a rule that is longer than the mistake
  it prevents does not get read." Nothing counts the first half, and the second half is an
  aphorism I can't back up.

### T5 — The standard: the loop

> **H3:** The loop each session runs through
>
> The brief is mine. The spec says what good means before anything is built. The agent
> builds. I review the copy block by block and rule on each one. A correction worth keeping
> becomes a rule, the rule goes into the next handoff, and the next session starts from there.
>
> *Diagram caption:* Each step links to a real file from this site's own build.

Changes from the template:
- **"I review every block and rule on it" became "I review the copy block by block".** You
  review copy, not every code change.
- **"Whatever I corrected becomes a rule" became "a correction worth keeping".** Not every
  correction became a rule.
- **Cut from the caption: "The return arrow is the part most AI work skips."** It's a claim
  about other people's work that I can't source.
- **Diagram links now point at handoff-016 and copy-review-003,** not handoff-013 and
  copy-review-001 (see T0). The diagram's own labels are unchanged.

### T6 — What the AI got wrong

> **H2:** Three misses that went live
>
> All three were on the live site before they were caught.
>
> **1. A clean accessibility report, and a keyboard that lost its place.** The 3D graph on
> the Projects page loads when you press a button. When the graph arrived, the button hid
> itself, and keyboard focus went with it: it fell back to the page as a whole instead of
> moving to the graph. The automated accessibility checker had found nothing wrong on any
> page. *(looked right but was not measured · handoff-012 §2)*
>
> **2. Passed locally, broke live.** The site got a content security policy: a header that
> tells browsers which scripts the site may run. It passed on a local server. The live site
> also runs an analytics script that Cloudflare adds as it serves the page, which the local
> copy never had, and the policy blocked it. Visitor analytics stopped for one deploy.
> *(looked right but was not measured · handoff-015, traps)*
>
> **3. Exact counts that disagreed with the graph.** The first live copy gave the research
> graph's size to the exact report. The copy of the graph a visitor could actually open, on
> another of my sites, held a small fraction of that. And the research keeps growing, so even
> a correct figure would have been wrong within weeks. *(drift across sessions · receipts-001,
> R-011)*

No count appears (F-3). The underlying figures sit in copy-review-001 X3 as roughly 3,600
against about 300. "Within weeks" is handoff-002 §3 ("a precise figure goes stale in
weeks"). "Content security policy" is explained in a clause because the lead role is
nonprofit web operations, not engineering.

### T7 — How I caught it

> **H2:** Use it, load it live, read every line
>
> **1. Went past the checker to the behaviour.** The checker's clean result was not taken as
> the answer. The pass looked at what a checker cannot see: where keyboard focus goes when
> the button disappears. Focus now moves to the graph when it loads, and the arrow keys step
> through the graph's connections, each one described in the panel. *(Became the rule: test
> the thing itself, not a proxy for it · CLAUDE.md, rule 1)*
>
> **2. Loaded the live site and read its console.** The deploy was checked from outside: the
> real site, in a browser, not the local copy. The browser console showed the blocked script.
> The policy now allows Cloudflare's analytics, and the script was confirmed loading on the
> live site. *(Became the rule: after any change to the security policy, load the live site
> and read the console · handoff-015, traps)*
>
> **3. A numbered review of every live sentence.** The first copy review put everything
> public on the site in front of me as numbered blocks, before I had read any of it, and
> flagged that the count on the page and the graph a visitor could reach disagreed. I ruled
> that counts are rounded or described, never exact. The home page now says "nearly four
> thousand". *(Became the rule: never publish an exact count in copy · handoff-002 §3)*

**⚠ FLAG: who caught 1 and 2.** In both, the agent ran the check: the code half of your
accessibility pass (A-1), and the live check after a deploy. So the copy uses "the pass" and
"the deploy was checked", not "I". Only 3 is written as yours: you ruled on X3, and
handoff-002 says "he was emphatic".

**⚠ DOUBT on 1 (reported, not overridden).** handoff-012 §2 records that axe found nothing,
what the fault was, and the fix. It does not say in so many words how the focus drop was
found. receipts-001 says "manual keyboard test", but that row was never ticked as re-read.
So the copy claims only that "the pass looked at" focus behaviour, not that someone tabbed
through it by hand.

**"Became the rule" is checked for timing** (the R-001 trap):
- **Rule 1 is in `CLAUDE.md`.** It was distilled on 2026-09-23 from the inventory, which
  lists R-024 under it (receipts-001 §6).
- **The console rule is handoff-015's own wording,** with "CSP" spelled out in plain words.
- **The count rule was written in handoff-002 because of X3.**

### T8 — How I caught it: the rules table

> *Caption:* Each correction, the standing rule it falls under, and where that rule lives.
> The first three are the misses above; the other four come from the same inventory.

| The correction | The standing rule | Enforced in |
|---|---|---|
| A clean checker report; keyboard focus lost when the graph loaded (R-024) | Test the thing itself, not a proxy for it: drag the slider, Tab through the page, load it logged out | `CLAUDE.md` · rule 1 |
| A security policy that passed locally blocked analytics live (R-028) | After any change to the security policy, load the live site and read the console | handoff traps · `CLAUDE.md` rule 2 |
| Exact counts that disagreed with the graph a visitor could open (R-011) | Never publish an exact node, edge, report or grade count in copy. Round or describe. | handoff §3, every session |
| A button marked hidden still showed with JavaScript off: a layout rule outranked the hidden attribute (R-019) | Content renders without JavaScript, and nothing heavy loads before a click. Test it with JavaScript off | handoff §3, every session |
| "Three or four" condition guides on the rare-disease site; its own menu listed five (R-022) | Count with a command, never from memory | `CLAUDE.md` · rule 12 |
| Links pointed at old `.html` addresses that redirect: on record in the third handoff, fixed in the fifteenth (R-027) | Clean addresses everywhere: menu, canonical links and sitemap | handoff §1 |
| Told me my LinkedIn had no About section; the page loads in parts and was never scrolled (R-029) | Say what you read, not what exists: "I could not see X", never "X is missing" | `CLAUDE.md` · rule 6 |

Every row carries a receipt link on the page. The caption says "falls under", not "became",
because R-019 broke a rule that already existed. **R-022:** "three or four" is not in any
committed version of the site, so the row doesn't say where it was written, only that it
was wrong. **R-027:** handoff-003 records the redirect, and handoff-015 §2 records the fix.
Rules 1, 6 and 12 are quoted word for word from `CLAUDE.md`.

### T9 — What shipped

> **H2:** A static site, one stylesheet, and its working files in the open
>
> The site is live at tc-ventures.ca. Its words and links render with JavaScript off, and the
> one heavy thing, the 3D graph, waits for a click. The fonts and the graph's code library
> are served from the site itself, not from a third party.
>
> *Fig. 1* The home page. *Fig. 2* The first case study, built from the same template as
> this page.
>
> **The honest limits:** As of September 2026 the rebuild is part-way through, and the plan
> it follows is public. There are no page-weight or accessibility scores on this page:
> nothing measures them by script yet, and I don't type figures in by hand. The site has not
> had a screen-reader run-through yet.

Changes and checks:
- **"Five pages" is gone.** The count was wrong and would go stale.
- **"Nothing outside the repo can rot underneath it" became "fonts and the graph's code
  library… not from a third party".** Cloudflare's analytics script comes from outside.
- **Checked:** there is one stylesheet (a glob found only `style.css`), and the graph library
  is the prebuilt `3d-force-graph.min.js` in `assets/`.

The honest limits:
- **Dated "As of September 2026",** so the line ages honestly.
- **The PL-8 sentence is new.**
- **"Screen-reader run-through"** is exactly what handoff-012 A-1 says is left. The template
  sentence it replaces was about your accessibility pass. **Cut it if you'd rather the page
  not mention that.**

**Q-T1 — the figures.** Both were taken 2026-09-24 in headless Chrome at 1280×720, light
scheme, from the live pages: `assets/img/this-site-home.webp` and `this-site-gprs.webp`.
Neither shows a person. Yes / no, or name a different figure.

### T10 — Receipts

> No document, no edge. Anything in sections three and four that could not be tied to a file
> was cut before it got here.

The list:
- brief-001 · 2026-09-11
- handoff-016 §3, §5
- handoff-002 §3
- handoff-012 §2
- handoff-015, traps
- receipts-001 §3B
- `CLAUDE.md`
- plan-001

"No document, no edge" is the graph's own rule (plan-001 §4a applies it to the portfolio).
The second sentence is true of this draft: every claim in sections 3 and 4 links to a receipt.

**Still to rule:** T0 (A / B / C), T1–T10, Q-T1. When ruled, it ships on the `/work/gprs`
checklist:
1. Remove the banner, `noindex` and the three `.assetsignore` lines.
2. Add the page to the sitemap.
3. Link it in. **Q-T2:** from where? I recommend both places that already describe the
   site: Projects' "The fourth is this one…" (`projects.html` L402) and the home "Four live
   sites" card's "…and this one." (`index.html` L127), matching G9.
4. Verify live: the build's check-run, curl, a headless render and the console.

### Rulings on T0–T10 (Thomas, 2026-09-24)

- **T0: A.** The handoffs are linked as they are. copy-review-001 stays unlinked.
- **T3: OK.** The proposal replaces the template paragraph.
- **T7, verbatim:** "i found it when testing it, i should not have trusted it worked but
  because it is so basic I assumed. my mistake." **Applied:** catch 1 is now yours ("Tested
  it myself"), in your words lightly tidied as prose, not as a quote, with this ruling as the
  receipt. The DOUBT is resolved: receipts-001's "manual keyboard test" was right. Catch 2
  stays the agent's.
- **Q-T1: yes.** Both figures ship.
- **Q-T2: OK.** Linked from Projects' "The fourth is this one…" and the home card's "…and
  this one", both as "read the case study", matching G9.
- **New, not in the review:** "Include this one and the last one in a sub menu under
  projects." This replaces PL-7's "no menu item until a `/work/` index exists". **Applied**
  on every page:
  - Projects gets a sub-menu listing both case studies, labelled with their H1s ("A housing
    society's website", "This site"). No new copy.
  - Without JavaScript it shows on hover and on keyboard focus.
  - With `assets/nav.js` it becomes a disclosure button: Esc closes it, and it closes when
    focus or a click goes elsewhere.
  - Case-study pages mark Projects as the current section.

Shipped 2026-09-24:
- Draft banner, `noindex` and the three `.assetsignore` lines removed.
- `/work/this-site` added to the sitemap.
