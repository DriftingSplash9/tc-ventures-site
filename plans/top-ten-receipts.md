# Ten receipts: what AI got wrong, and how it was caught

*Written 2026-09-23. Chosen by Claude from the 112 receipts in `plans/receipts-001.md`.*

Thomas Cheesman builds and runs several websites and a research application with AI doing
most of the writing of code and text. The AI works in sessions, and at the end of each one it
writes a handoff: what it did, what went wrong, and what the next session should know. Over
several months those handoffs, audits and commit logs built up a written record of every time
the AI got something wrong and someone noticed. In September 2026 that record was read end to
end, about 450 documents across six projects, and each documented mistake was logged as a
"receipt": what went wrong, how it was caught, the rule it became, and the file that proves
it. The ten below are the most instructive. They cover four projects:

- **thomascheesman.ca**, Thomas's personal site (WordPress).
- **BareYourRare**, a rare-disease awareness site (WordPress).
- **GPRS**, the website of a volunteer nonprofit housing society whose board Thomas sits on.
- **Reports Clustering**, a research application that maps which official statistical
  reports depend on which. Every link in it has to be backed by a word-for-word quote from
  the source document.

The receipt number after each title points back to the full inventory.

---

### 1. A complete report for a page that didn't exist (R-083)

In August 2026 an agent working on Reports Clustering's Africa research asked an AI fetch
tool to summarise a Botswana Auditor-General report from a URL. The tool returned exactly
what a real report would contain: a date, the officer's name, figures and a section
reference. None of it was real. The URL returned a 404; there was no page at all. The same
week, the same tool produced funding figures for Somalia that no source contained. The agent
caught it by checking the raw HTTP status with `curl`, outside the AI tool. **Rule:** before
trusting anything a summarising tool says about a page, confirm the page exists and returns
a success code.

### 2. Three sliders that did nothing (R-050)

Reports Clustering draws its reports as a 3D graph laid out by simulated forces, with sliders
that strengthen or weaken each force. Between 20 and 28 August three sliders shipped that had
no visible effect. Each force had been checked by a script, and each script said it worked.
The cause was that moving a slider never restarted the simulation. By the time anyone touched
it, the simulation had come to rest, so the force was correct but multiplied by nearly zero.
The same omission shipped three times before Thomas said, "I don't see any effect from it."
**Rule:** verify a control by using it (drag the slider and watch), not by measuring the code
behind it.

### 3. The grader that couldn't read its own evidence (R-052)

Reports Clustering grades every link A, B or C by checking that its quote really appears in
the cited document. The quote was stored in its own field, but the grader passed that field
through a function built to find text *inside quotation marks*. Stored quotes have no
quotation marks, so the grader found nothing in its own evidence and marked good quotes as
unquoted. This went on for weeks, and a recommendation about when to make a minimum grade
mandatory was based on those grades. It was caught on 3 September, when a batch of reviewed,
accepted quotes was re-graded and almost none came back as A. **Rule:** a checker can be
wrong too. Test it against a case where you already know the answer.

### 4. "Site verified" while visitors saw "Coming Soon" (R-123)

On 15 May 2026 thomascheesman.ca went live. The agent's smoke test loaded every page and got
a normal response from each, and the site was called verified. But the host had a
"Coming Soon" mode still switched on. Logged-in administrators bypass it; the public doesn't.
The agent's checks ran as an administrator, so every page passed while every ordinary visitor
saw a placeholder. The next session caught it. **Rule:** check the site the way a visitor
sees it, logged out.

### 5. Two months without a medical disclaimer (R-142)

BareYourRare has a guide page for each of five rare conditions. On 18 April a change added a
medical disclaimer, structured data for search engines, styling and scripts to all five. Its
description said so, and the to-do list marked it "Deployed for all 5… with proper guards."
But the code that decided which pages were condition guides had the wrong file path for two of
them, so those two pages silently received none of it. An April audit had even noticed the
missing structured data on those pages, but the item stayed marked as done. A full audit with
live checks found it on 20 June, about two months later. **Rule:** "deployed" is a claim.
Confirm it on every page it is meant to reach, on the live site.

### 6. "Safe to push," said three times (R-007)

On 18 September an agent working on the GPRS site told Thomas three times that pushing changes
was safe, because the site had no automatic deployment and needed a manual step to go live.
That was wrong: the site deployed automatically within minutes. The agent had also committed
written instructions for a manual deploy process that didn't exist. Thomas asked why the site
already looked updated, and a check of the live site confirmed it. The belief had been
repeated in several of the agent's own notes; an older note from April had it right. **Rule:**
a claim repeated in three notes is still one claim. Repetition is not confirmation.

### 7. A footnote built from true parts (R-075)

In August an agent researching Australian sources used an AI-summarising reader on a
government report. It came back with a footnote citing a specific national statistics release,
with an exact title and release date. Every part was plausible: the agency is real, the data
product is real, the date had the right shape. But the footnote does not exist. A later session
extracted the document's text directly and found nothing. When another session read the
chapter the citation was supposedly borrowed from, it wasn't there either, so even the first
explanation for the mistake was wrong. **Rule:** for anything you quote, read the source
directly. True parts don't prove the whole.

### 8. "A sian" tidied into "Asian" (R-078)

A PDF's text layer had a broken word, "A sian Development Bank", the kind of glitch PDF
extraction produces. An outside research model quoted the passage but quietly corrected it
to "Asian". The fix looked helpful. But anyone searching the document for the quote found
nothing, because the document says "A sian". Proving the quote was genuine took Thomas twenty
minutes. **Rule:** quote ugly. Copy the source exactly as it is, glitches included. The rule
was later extended the other way too: don't decorate either, after another quote came back
with a link added that the page didn't have.

### 9. "Read and empty — do not re-fetch" (R-090)

In September, Reports Clustering's research on China recorded one city's statistics source as
"read and empty, do not re-fetch." In fact the source had two layers of files and only one had
been opened. A province's second layer went unopened for four rounds for the same reason. A
sweep that opened both layers found the material. The instruction "do not re-fetch" turned a
partial read into a closed door. **Rule:** a refusal is a statement about the documents you
read, not about what exists.

### 10. The focus ring that showed on nothing (R-129)

In June an accessibility pass on thomascheesman.ca was declared complete after the automated
checker's one finding was fixed. Then Thomas noticed that moving through the site with the
keyboard showed no highlight at all. Tabbing through every page found 41 interactive items
with no visible focus. The site's focus style had been written in a way that gave it zero
priority, so the parent theme's styles overrode it everywhere. The automated checker cannot
see this kind of problem. **Rule:** automated accessibility checks are a floor. Tab through
the page yourself.

---

## What the ten have in common

None of these failures was hidden. In every case the work *looked* finished: a script passed,
a page responded, a to-do was ticked, a quote read smoothly, a checker came back clean. What
caught each one was a direct look at the real thing: the raw HTTP status, the slider on the
screen, the page as a logged-out visitor sees it, the exact text of the source, a keyboard
pressed Tab by Tab. The rules that came out of them are short and they repeat across projects:
test the thing itself, not a stand-in for it; treat "done", "verified" and "deployed" as
claims until they are checked from outside; say what you read, not what exists; quote
exactly. Several catches came from Thomas simply looking and asking. That is not a failure of
the method; it is part of it. These rules are now written into the instructions every agent
on these projects reads at the start of a session, so the next agent starts where these ten
mistakes left off.
