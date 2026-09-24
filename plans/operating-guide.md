# Operating guide: how Thomas works with AI

*Written 2026-09-23. Distilled from the receipts inventory (`plans/receipts-001.md`), the ten
highlighted in `plans/top-ten-receipts.md`, and the truth rules in `CLAUDE.md`. Receipt
numbers (R-NNN) point back to the inventory.*

The main idea: **Thomas decides what gets built and is the final check. The AI does the
drafting and the legwork.** In every one of the ten top receipts the work looked finished. It
was caught when someone looked at the real thing, often Thomas. So the goal isn't to trust the
AI more. It's to make checking quick, routine and built into how the work is done.

---

## 1. Before the session: set up the ground truth

**Keep one current file per project that says where things stand.** Here that's the
highest-numbered `handoff-NNN.md`, and `CLAUDE.md` points to it. Every session should begin by
reading it. If it doesn't, say "read the handoff first."

**Keep one copy of each fact.** The "safe to push, no auto-deploy" mistake (R-007) came from a
wrong belief copied into three notes, while an older correct note was ignored. When a fact
changes:
- Change it in **one** place (the handoff or the memory file that owns it).
- Replace duplicates elsewhere with a pointer like "see handoff-012 §3" rather than a second
  copy.
- If two notes disagree, stop and settle it before any work that depends on it.

The global CLAUDE.md already says the project list is copied in three places and has to be kept
in sync. That's a known source of drift. The fewer copies, the fewer ways to pick up a stale
one.

**Write down facts about the infrastructure, and check them.** Deploy method, caching,
maintenance or Coming Soon modes, what CI does. These are the facts the AI is most likely to
get confidently wrong (R-007, R-123), and they're cheap to check once and record with a date:
"Verified YYYY-MM-DD: site auto-deploys within minutes of push to main."

---

## 2. Giving the AI a task: how to phrase requests

**Define "done" as something you can see.**
- Weak: "Add a focus style."
- Strong: "Add a focus style. Done means: Tab through the home page and the contact page
  logged out, and every link and button shows a visible ring."

When "done" describes what you should see, the AI has to test that. When it's vague, it tends
to test whatever is easiest, like the checker, the script or the build.

**Ask for the evidence along with the claim.**
- "Show me the curl output, not a summary of it."
- "Paste the exact line from the source."
- "Which pages did you actually check?"
- "What did you *not* check?" (The most useful one. It pulls out the gaps that turn into
  receipts.)

**Say what's out of scope.** Rule 19, stay inside the request, works both ways. "Only touch
`inc/contact.php`" stops unrequested "improvements" that then have to be accounted for.

**Split big tasks into units you can check.** "Add the disclaimer to all five condition guides"
is really five checks. R-142 happened because five pages were treated as one claim. Ask for a
per-page result: page, URL, disclaimer present yes/no, how it was checked.

---

## 3. While the AI works: what to watch for

| The AI says… | What it often means | What to ask |
|---|---|---|
| "Verified" / "confirmed" / "deployed" | It checked *something*, possibly a stand-in for the real thing | "Verified how, from where, logged in or out?" |
| "The script passes" / "all checks green" | The checker ran, and may not be able to fail (R-052) | "Show me it failing on a known-bad case." |
| "X doesn't exist" / "no data" / "empty" | It didn't find it in what it read (R-090) | "What exactly did you open?" |
| A tidy quote, figure, date or citation from a fetch/summary tool | It may be made up or cleaned up (R-083, R-075, R-078) | "Fetch the raw page and confirm a 200. Paste the verbatim text." |
| "As noted in the handoff…" / "per memory…" | Possibly a stale or copied claim (R-007) | "When was that last checked against the live system?" |
| "Safe to…" about deploys or anything irreversible | A belief about infrastructure | "Check it now, don't recall it." |
| A number with no command behind it | A count from memory (rule 12) | "Count it with a command." |

**Trust your eyes over the report.** "I don't see any effect from it" caught three shipped bugs
(R-050). If what you see disagrees with what the AI said, what you see wins, every time.

**Watch for "fixed" after only one attempt.** If the same kind of thing has failed before, the
fix probably covers the symptom it was shown, not the cause. Ask: "Why did it fail, and where
else could the same cause bite?"

---

## 4. Checking the work: a short routine for each kind of change

**Website changes (TC / BYR / GPRS):**
1. Open the live URL in a **private or logged-out window**, never as admin (R-123).
2. Check **every page** the change was meant to reach, not a sample (R-142).
3. Use it: click, submit, drag, **Tab through with the keyboard** (R-129).
4. Look at it on a phone-width screen.
5. Look at it yourself. A build passing says nothing about how it looks (rule 4).

**Research and quotes (Reports Clustering):**
1. Every quote gets a raw fetch with a 200 status (R-083).
2. Search the source document for the quote as written. If search can't find it, it isn't a
   quote (R-078).
3. Distrust anything that came through a summarising tool, even when every part of it is
   plausible (R-075).
4. Record "not found" as "not found in [these specific files]", never as "doesn't exist"
   (R-090).

**Checkers, validators and scripts:**
1. Before trusting a checker, run it on something you know is bad. If it passes, the checker
   is broken (R-052).
2. Check that it reads the field you think it reads.

**You don't have to do all of this yourself.** Tell the AI to do it with outside evidence: "curl
every changed URL logged out and show me the status and a grep for the disclaimer text." Your
job then shrinks to spot-checking its evidence and taking one real look.

---

## 5. Commits and deploys

- **Commit and push are pre-authorised for finished, reviewed units.** This removes friction
  without removing judgement.
- **Never `git add .`** Staging explicit paths stops temp files, Office lock files (`~$…docx`)
  and half-finished work from sneaking in, which matters extra because **this repo is public**
  (rule 20).
- **"Pushed" is not "live."** Confirm the deploy method against the real system, then check the
  live URL after pushing.
- **Before anything public:** check it against the privacy rules. On a public repo, a commit
  counts as publishing.

---

## 6. Ending a session: the handoff is the product

A session's most lasting output is often its handoff, not its code. Ask for these every time:
1. **What was done**, with how each item was checked and from where.
2. **What was *not* checked.** Name it explicitly.
3. **What went wrong or nearly went wrong.** This is where receipts come from.
4. **What's next**, with dates written as dates, not "tomorrow."
5. **Any fact that changed.** Update its single home and don't add a new copy.
6. Append the row to the cross-site diary.

**Read the handoff critically before closing the session.** Anything in it that says
"verified" or "done" is a claim the next session will inherit as fact. If it's wrong there, it
gets repeated (R-007).

---

## 7. Turning mistakes into safeguards

- **First time a mistake happens:** it becomes a receipt and a rule.
- **Second time:** it becomes **code**, meaning a validator, a test or a pre-push check that
  fails loudly (rule 5). A rule in a note depends on the AI reading and following it. A failing
  check doesn't depend on the AI at all.
- **Periodically:** re-read the receipts and ask which rules could be turned into checks.
  Good candidates:
  - A logged-out smoke test that fails on "Coming Soon" or maintenance text.
  - A per-page live check that the condition-guide disclaimer is present.
  - A focus-visible check via a keyboard-traversal script, as a floor, not a replacement for
    tabbing yourself.
  - A quote validator that fails when the stored quote isn't found verbatim in the fetched
    source.
  - A grader self-test with known A/B/C examples that must come back correctly.

---

## 8. How to divide the work

**The AI is good at:** drafting, reading a lot quickly, writing code and scripts, running
checks when told exactly what counts as proof, keeping records consistent, and finding
patterns across documents.

**The AI is unreliable at:** knowing whether something *looks* right, knowing whether something
exists when it didn't find it, anything it "remembers" about infrastructure, quotes that came
through a summarising tool, and saying its own work is finished.

**Only Thomas can do:** decide what matters, make commitments (rule 16), supply facts the AI
doesn't have (rule 11: unknown means ask Thomas), and take the one real look that ends the
argument.

**Default stance:** treat AI output as a good draft that hasn't been checked yet. The job isn't
to redo it. It's to ask "how do you know?" and then look once for yourself.
