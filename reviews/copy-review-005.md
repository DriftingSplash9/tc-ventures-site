# Copy review 005 — the Back Quarter and the Desk and the Drawer

**Written:** 2026-09-26
**Why:** the last two case studies of Phase 1b (plan-001 §5 note, 2026-09-25):
`/work/back-quarter` and `/work/desk-and-drawer` (plan-001 §3). One receipts pass over
thomascheesman.ca covers both. Thomas chose a new review, 005, over adding to 004 (2026-09-26).
**Status:** Step 1 (BQD0) ruled 2026-09-26: Q-BQD1 A, Q-BQD2 answered, Q-BQD3 A, and R-160 to R-174 in
receipts-001 §3F (8 OK, 7 CUT; see "Rulings, round 2"). PJ1–PJ6 ruled and applied to `/projects` the
same day. **Step 2 (BQD4, BQD5, BQ1–BQ8, DD1–DD8, P3) drafted 2026-09-27, for Thomas to rule.**

Same format and marks as copy-review-001 to 004: `OK` · `KEEP` · `A` / `B` · `FIX` · `CUT`.

---

## BQD0 — Step 1: receipts, the ask, and the live copy (not copy)

**Read 2026-09-26.** The theme repo (`DriftingSplash9/thomascheesman-ca-theme`), full history:
- **Handoffs:** V0.05–V0.09 from git history, V0.10–V0.42 on disk. I could not see a V0.08 anywhere in the
  history. Each file was read in full, or, where it wasn't about these three surfaces, by keyword with the
  text around each hit.
- **Specs:** `docs/QUARTER-SECTION-SPEC.md`, `HERO-PROMOTION-SPEC.md`, `SECRET-DRAWER-VISION.md`,
  `back-quarter-art-prompts.md`.
- **Commit messages:** every one touching the Back Quarter, desk-menu or drawer files: 106, 78 and 94
  commits.
- **Who read what:** three readers extracted; I re-opened every receipt cited in the table below
  (`chk` ✓). Nothing in the theme repo was changed.

### 1. ⚠ FLAG, read first: what the pages link (Q-BQD1)

The rows below point at theme-repo files and commits, as receipts-001 §3D already does. Whether the
pages link those files is a privacy call; the reasons went to Thomas in the chat.

> **A (recommended):** the case studies link the receipts-001 rows, not theme files. This is how BYR's
> private repo was handled.
>
> **B:** link theme files one by one, each after a whole-file privacy read. A commit link on GitHub
> shows the diff as well as the message, so the read covers the diff.

### 2. The ask: no brief in Thomas's words (Q-BQD2)

- **Searched:** the four specs above, V0.06, V0.10 and V0.38–V0.42.
- **Closest, Back Quarter:** `QUARTER-SECTION-SPEC.md` §0, "Thomas asked (2026-07-01) for the homepage
  to become a BHAG matching the desk menu and the secret drawer". It is the agent's paraphrase, not a
  quote.
- **Closest, Desk:** V0.06 (from history) leaves the surface "TBD pending Thomas's decision". Nothing
  records why a desk.

**Q-BQD2:** one or two sentences on why you built each one, in your words. They become each page's
pull quote, as on the other case studies.

Also noted: the Back Quarter spec's art-pipeline decision (§7 D2) names the outside model (F-2). No
page would quote it. It only matters under Q-BQD1 B.

### 3. Proposed rows, a new §3F in receipts-001

Numbered from R-160, because §3D has only eight free numbers. Every row is a miss the record states. The
line numbers for a commit are lines of `git log -1 --format=%B <hash>`.

**The Back Quarter**

| ID | date | what the AI got wrong | kind | caught | rule it became | receipt | public-safe? | chk | Ruling |
|---|---|---|---|---|---|---|---|---|---|
| R-160 | 2026-07-09 | Built the bloom effect's bundle from grep hits that were dependency checks, not definitions, and committed it as "the lights glow". The effect threw on load, and the fallback quietly booted the farm without bloom | tooling | not stated (fixed 3 minutes later) | Bundle order written into the vendor file's header | `5207d03` (the claim); `0f2f9f3` L3–8 | Y | ✓ | |
| R-161 | 2026-07-09 | The fixed bundle was live on the server, but browsers kept running the broken copy: its URL had no cache-buster, and "a LiteSpeed purge can't reach the browser HTTP cache" | tooling | not stated | Bust the URL (V0.40 L44–46) | `2a6edd7` L3–6 | Y | ✓ | |
| R-162 | 2026-07-10 | Tuned the bloom threshold at dusk only; in daylight "the white church blazed featureless white and BLOOMED" | unmeasured | Thomas (his screenshot) | "Bloom thresholds are day-driven — don't re-tune night values without checking noon" | `6430c92` L3–5; V0.40 L49–51, L140–141 | Y | ✓ | |
| R-163 | 2026-07-11 | The fire's first crackle clicked "like tiny firecrackers". Its fix sent every pop through the same resonant filter, so each rang the same note | unmeasured | Thomas, both times: "the fire sounds like tin bashing." | — | `e5dba29` L3–6; `d1367d5` L3–6 | Y | ✓ | |
| R-164 | 2026-07-05→11 | Shipped livestock "with graze/wander AI". Each move was one push that friction killed in under a second, so for six days the animals "stood like statues" | unmeasured | Thomas: "the animals are too still" | — | `fe821f7` L19–20; `5e355e3` L3, L7–12 | Y | ✓ | |
| R-165 | 2026-07-07 | Thomas's feel-test note, that the buggy was too rigid and should lean, "never got addressed while we built the quarter" | drift | not stated (the agent recorded it when it got there) | — | `53f6490` L3–4 | Y | ✓ | |
| R-166 | 2026-07-09, 07-11 | A deploy check grepped for a string whose case didn't match the file, in two sessions running | tooling | not stated | "match case exactly (bit us again)": a note, not a check | V0.39 L168–169; V0.40 L148 | Y | ✓ | |
| R-167 | 2026-07-08 | Custom buttons kept rendering with invisible text, and the cause was rediscovered each time | unmeasured | Thomas: "recurring, Thomas flags it often" | The cause and the defence written into `style.css`, "so we stop rediscovering it": a comment, not a check | `bebf5c3` L29–33; `style.css` L776 | Y | ✓ | |

**The Desk**

| ID | date | what the AI got wrong | kind | caught | rule it became | receipt | public-safe? | chk | Ruling |
|---|---|---|---|---|---|---|---|---|---|
| R-168 | 2026-05-13 | Three versions of a hover sheen shipped without being seen to render. Two commits blamed Chrome ("parsing issue some Chrome builds have"). The cause was an older rule of the agent's own, overriding the new animation | invented | live check: "came back invisible on user's Chrome" (the user isn't named) | — | `e3962e0` L3–4; `b2d382a` L5–6; `525d1a6` L3–4; `17c073d` L3–7 | Y | ✓ | |
| R-169 | ≤2026-05-17 | The "View as a plain list" toggle, the desk's way out to ordinary links, sat inside the monitor's clipped area: "it was unreachable" | unmeasured | not stated | — | `bca7b22` L3–4 | Y | ✓ | |
| R-170 | 2026-06-17→19 | The agent's own site audit listed a focus trap for the desk overlay as a 3–5 hour job. The overlay had had one since 2026-06-12 | absence | read-through: "Spent real effort verifying; all confirmed against live code" | V0.33: "strike these off" | V0.31 L65 (L33: the audit was built from "the local theme files"); V0.33 L20–25; the trap, `00e175d` | Y | ✓ | |

**The Drawer and the pinball**

| ID | date | what the AI got wrong | kind | caught | rule it became | receipt | public-safe? | chk | Ruling |
|---|---|---|---|---|---|---|---|---|---|
| R-171 | 2026-05-27 | Declared "The puzzle is complete." Choices made in its pop-up dialogs changed the state in memory but were never saved or redrawn: "a bug for two days" | unmeasured | not stated ("Phase 4 play-test fixes") | "Anyone adding another modal action MUST do the epilogue trio" | `aa6b356` L44–45; `4fc1ef4` L3–12; V0.16 L266–272 | Y (describe the bug, not the puzzle) | ✓ | |
| R-172 | 2026-06-23→24 | A pinball fix was "validated in-browser" with test balls, and Thomas's play still found balls stuck at the sides. The next fix's one failing drop was written off as "a rare flipper-base settle that real momentum clears". The next day's commit calls it "the recurring flipper-base trap" | unmeasured | Thomas: "it keeps getting stuck to the right and left" | — (falls under `CLAUDE.md` rule 1) | `0fc31ac` L3–6; `0905002` L3–12; `f037e11` L12–14 | Y | ✓ | |
| R-173 | 2026-06-25 | "Debugged" a blank game canvas at length; it was a background tab, which pauses animation | tooling | not stated (the agent's own note) | "Check `document.hidden` before concluding 'blank = broken.'" | V0.36 L21, L96 | Y | ✓ | |
| R-174 | 2026-05-20 | The flippers stuck in place because the agent divided by the frame time "under the wrong assumption" about the physics library's velocity units | invented | not stated | — | `12f7b8f` L3–8 | Y | ✓ | |

*Ruled 2026-09-26: the rows now live in receipts-001 §3F, which is the copy to use. The tables above are the proposal as it was put.*

**Who caught what (the "I" rule), as proposed:** Thomas is named in R-162, R-163, R-164, R-167 and R-172. R-168's
catch is "the user's Chrome", which the record doesn't name, so it stays impersonal unless you say it
was you. The rest are the agent's.

**Also found, not proposed** (recorded, but weaker, off-topic, or not re-opened by me): on the Back
Quarter, the mound mesh drawn taller than its physics (`5a96b1c`), corner lean inverted (`5a96b1c`),
the church first inside its hill and then floating (`ee58d9d`, `f8084f4`), a cow sample that read as a
sheep (`f8084f4`), horses grown into giraffes (`8784098`), a ramp buried by a building scale-up
(`cec8cd0`), engine revs falling in mud (`97f79a6`), headlights aimed over the ground (`29d4d7e`), haze
that ignored instancing (`16de069`), wedge roofs (`809eb3e`), a floating church window (`faa7763`), a
double shadow (`3867505`), and mud discs that floated twice (`d426083`); on the Desk, dangling
references after the old overlay was retired (`231382d`), a second cursor trail on top of the first
(`ae8ab02`), and "misread the previous request" (`c493feb`, `62ae02d`); on the Drawer, a handoff that
sent the next session to the wrong images (`ea11d46`), UTC where Mountain Time was meant (`41e71ea`), a
funnel wall across the plunger lane (`27b5f33`), a leaderboard risk called "well-understood"
(`22731f3`, `5c5db69`), balls tunnelling past the flipper tips (`3a4540b`), and a drag fix re-fixed
seven minutes later (`6e163d6`). Any of them can be raised to a row on request.

### 4. ⚠ FLAG: the live `/projects` copy against its record

The case studies reuse `/projects` paragraphs unchanged (the P1 and P2 pattern), so each of the two
sections' claims was traced. Six don't match the record or the code:

1. **"Early on the buggy pivoted like a tank."** Tank steering wasn't an early miss. The first build had
   speed-scaled steering (`faca583` L8–10). Tank steering was added on purpose in "Drive-test round two
   from Thomas" (`b62ec1a`, 2026-07-03, L11–13). It came out of the 3D build on 2026-07-12, when Thomas
   asked for "a realistic turning radius" (`5f9b755` L3–4, L11–16). That commit touches only the 3D
   script. **The painted map, which phones get, still turns on the spot** (`back-quarter.js`
   L399–401).
2. **"For one version the daylight walls glowed too, and the whole farm looked like moulded plastic."**
   The record says the white church "blazed featureless white" (R-162) and that the regression "happened
   once" (V0.40 L51). "Moulded plastic", "one version" and "the whole farm" aren't in it.
3. **"Same amount of code, completely different room."** The fire fix added 53 lines and removed 23 in
   the 3D script (`git show --numstat d1367d5`).
4. **"A full keyboard path through every hotspot."** At the current commit, 5 of the desk's 18 hotspots
   take keyboard focus: the ones that open something. The other 13 are hover cards (`role="group"`, no
   `tabindex`), per `inc/desk-menu.php`. I read the source; I didn't Tab through it.
5. **"Same for the arcade."** The live home page loads the arcade script, deferred, for every visitor
   (checked 2026-09-26, logged out: `tc-desk-games-js`). The pinball engine does wait for the click.
6. **"Most of a megabyte between them."** The physics engine and renderer files are about 540 KB
   uncompressed and about 160 KB gzipped (the theme's `assets/js/vendor/`). I didn't check what the
   server actually sends.

Matched: seven games (7 in `inc/desk-menu.php`); the ember-and-pops fix ("12-45ms" pops, each "through
its own lowpass"); lazy loading of the pinball engine; the Escape order. The canvas fallback exists in
code (`28b8e5f`), but I found no record of it being tested.

**Recommended:** fix 1–6 in the case-study copy (step 2). `/projects` then keeps a short intro and
a "read the case study" line (P1), so the claims leave it when the pages ship. Until then they stay
live as they are.

### 5. Open for Thomas (BQD0)

- **Rule on R-160 to R-174:** OK / CUT / FIX each.
- **Q-BQD1:** A or B.
- **Q-BQD2:** why you built each one, in your words.
- **§4:** agree to fix those six lines in the case studies, or say which you'd keep.

### Rulings, BQD0 (Thomas, 2026-09-26)

Verbatim: "thomascheesman.ca is private in gh. show me r-160 to 174. BDQ1 rows, BDQ2 which ones? i
made my personal site mostly for family. Social media is messy and can get hard to use for some. I
wanted somewhere I could tell the story of where my ancestors came from and how we came to exist in
Grande Prairie as a happy family. I wanted to make it with easter eggs for them to discover if they
wanted to/ there's games and puzzles and such, a literal arcade, a map you race around and collect
coins while exploring the "back Quarter". TBH, I doubt it will see much traffic until I pass on but
that's  ok, for now I am here :) fix the 6 projects' lines."

- **The theme repo is private.** Checked 2026-09-26: GitHub's API reports `"private": true`, and an
  anonymous fetch of a raw file answers 404.
- **Q-BQD1: A.** The case studies link receipts-001 rows, not theme files.
- **Q-BQD2: answered**, for the site as a whole. It covers both pages: the arcade, games and puzzles
  are the Desk and the Drawer; "a map you race around" is the Back Quarter. How it's used goes in the
  step-2 blocks, with a verbatim version and a closed-up one, as for BYR. **Q-BQD3 (new), below.**
- **R-160 to R-174:** shown in the chat; not ruled yet.
- **"fix the 6":** read as a ruling to fix all six. The wording is below (PJ1–PJ6), for his OK before it
  ships. Each fix also carries into the case studies.

**Q-BQD3: the quote is familial.** The standing rule is "nothing familial, except the ruled Back Quarter
childhood paragraph". The answer names no one, but it is about family: "mostly for family", "where my
ancestors came from", "a happy family", "easter eggs for them".

> **A (recommended):** a second ruled exception, for this quote on these two pages. It is the reason the
> site exists, and it names no one.
>
> **B:** quote only the sentences without family ("Social media is messy…", "games and puzzles and
> such, a literal arcade, a map you race around…").

### Rulings, round 2 (Thomas, 2026-09-26)

Verbatim: "BQD3  - A, 160- me, 161- me, 165- me, 166you, 168 -me, 169 me, 174 me. you decide which up to
8 are worthy of keeping. pj1- a, pj2- ok, pj3- ok, pj4 cut, pj5 - A, pj 6 - cut"

- **Q-BQD3: A.** The Q-BQD2 answer is a second ruled exception to "nothing familial", for this quote on
  these two pages.
- **Catchers, in his words:** Thomas caught R-160, R-161, R-165, R-168 (the record's "user"), R-169 and
  R-174. The agent caught R-166. "How I caught it" can say "I" for his.
- **"You decide which up to 8":** the agent kept 8, four per page, so each case study has three misses
  and a spare:
  - **Back Quarter:** R-160 (a bundle built from the wrong grep hits; the fallback hid it), R-162
    (daylight bloom), R-163 (the fire), R-164 (animals declared wandering, standing still). R-162 and
    R-163 also back the `/projects` lines fixed in PJ2 and PJ3.
  - **Desk and Drawer:** R-168 (Chrome blamed for the agent's own rule), R-169 (the way out was
    unreachable), R-170 (an audit asked for work already done), R-172 (test balls passed, real play
    didn't).
  - **Why these:** Thomas caught seven of the eight, and the four on each page are different kinds of
    miss. The first alternate is R-165 (the feel-test note that was dropped), the only drift row.
  - **CUT:** R-161, R-165, R-166, R-167, R-171, R-173, R-174. Any can be swapped back in.
- **PJ:** see "Ruled" at the end of PJ1–PJ6.

---

## PJ1–PJ6 — `/projects`, the six lines (BQD0 §4), at "fix the 6"

These fix the live page now, as M9 did, and ship on their own. The live text is quoted from
`public/projects.html`.

### PJ1 — the buggy's steering (Back Quarter, "Three things the build taught me", 1)

> **Live:** "**A vehicle that can turn on the spot does not feel like a vehicle.** Early on the buggy
> pivoted like a tank and nothing about it read as driving. The fix was not more physics, it was less
> permission: yaw rate now follows forward speed, so she has to be rolling before she will turn, and she
> eases into it. Grip drops in the wet. Reversing flips the steering sense, the way it does in a real
> yard."
>
> **A (recommended):** "**A vehicle that can turn on the spot does not feel like a vehicle.** For most
> of the build the buggy could pivot in place, and turning felt harsh. The fix was not more physics, it
> was less permission: in the 3D world the yaw rate now follows forward speed, so she has to be rolling
> before she will turn, and she eases into it. Grip drops in the wet. Reversing flips the steering
> sense, the way it does in a real yard. The painted map that phones get still turns on the spot."
>
> **B:** keep the live wording, and change the painted map's steering to match the 3D world. That's a
> theme change on thomascheesman.ca, and plan-first.

Sources: `faca583` L8–10 (the first build's steering scaled with speed); `b62ec1a` L11–13 (tank
steering, 2026-07-03); `5f9b755` L3–4, L11–16 ("turning and acceleration/deceleration are harsh", the
turning radius and the reversed steering, 2026-07-12, 3D script only); `97f79a6` L18–19 ("Traction
drops to match… in the wet"); `back-quarter.js` L399–401 (the painted map).

### PJ2 — daylight bloom (Back Quarter, 2)

> **Live:** "…I learned that the hard way: for one version the daylight walls glowed too, and the whole
> farm looked like moulded plastic. Light has to behave like light, or the painting stops being a place."
>
> **A:** "…I learned that the hard way: the glow was first tuned at dusk, and in daylight the white
> church blazed featureless white. Light has to behave like light, or the painting stops being a place."

Source: R-162 (`6430c92` L3–5). "I" stands: Thomas's screenshot caught it.

### PJ3 — the fire (Back Quarter, 3)

> **Live:** "…Nothing rings. Same amount of code, completely different room."
>
> **A:** "…Nothing rings. A completely different room."

Source: `git show --numstat d1367d5` (53 lines added, 23 removed in the 3D script).

### PJ4 — the keyboard path (Desk, "Three things the build taught me", 1, and the spec table)

> **Live, paragraph:** "…a separate ordinary navigation for phones, a full keyboard path through every
> hotspot, and an Escape key…"
>
> **A:** "…a separate ordinary navigation for phones, a keyboard path to every object that opens
> something, and an Escape key…"
>
> **Live, spec table:** "Accessibility — Plain-list mode, separate phone navigation, full keyboard path,
> layered Escape"
>
> **A:** "Accessibility — Plain-list mode, separate phone navigation, a keyboard path to everything
> that opens, layered Escape"

Source: `inc/desk-menu.php` at the current commit: 5 of 18 hotspots take focus, the ones that open
something (`00e175d`: "the five clickable hotspots get role=button + tabindex=0"). The other 13 are
hover cards. Read in the source, not Tabbed through.

### PJ5 — the arcade (Desk, 2)

> **Live:** "…Same for the arcade, the slideshow and the desk art itself. A visitor who never clicks pays
> nothing for any of it, which is the only honest way to put a game in a footer."
>
> **A (recommended):** "…Same for the slideshow and the desk art itself. The arcade's game script is the
> exception: it still loads with every page. A visitor who never clicks pays almost nothing, which is the
> only honest way to put a game in a footer."
>
> **B:** keep the live wording, and make the arcade load on demand in the theme. The desk is a BHAG
> surface, so that's a plan-first change on thomascheesman.ca.

Checked live 2026-09-26, the home page logged out: the arcade script (`tc-desk-games-js`) is in the
page, deferred. The desk art is referenced only in the link-preview meta tags, and no slideshow markup
is in the page.

### PJ6 — the pinball's weight (Desk, 2)

> **Live:** "The physics engine and the renderer behind the pinball table are most of a megabyte between
> them…"
>
> **A:** "The physics engine and the renderer behind the pinball table are about half a megabyte between
> them…"

Source: the theme's `assets/js/vendor/`: `matter-0.20.0.min.js` 83,476 bytes + `pixi-7.4.2.min.js`
456,133 bytes = about 540 KB before compression (about 162 KB gzipped). What the server sends wasn't
checked.

### Ruled (Thomas, 2026-09-26): "pj1- a, pj2- ok, pj3- ok, pj4 cut, pj5 - A, pj 6 - cut"

- **PJ1 A, PJ2 OK, PJ3 OK, PJ5 A:** applied as drafted.
- **PJ4 CUT and PJ6 CUT:** read as cutting the claim itself, not keeping the live wording (the live
  wording is what was wrong). Applied:
  - PJ4, paragraph: "…a separate ordinary navigation for phones, and an Escape key that closes exactly
    one layer at a time…". Spec table: "Plain-list mode, separate phone navigation, layered Escape".
  - PJ6: "Neither the physics engine nor the renderer behind the pinball table touches the network
    until a visitor clicks the marble." (the size clause is gone).

Checked locally before the push:
- `scripts/site_check.py`: 84 of 84 checks passed.
- The rendered `/projects` text carries all nine ruled sentences and none of the seven cut phrases
  ("Early on", "moulded plastic", "Same amount of code", "full keyboard path", "most of a megabyte",
  "Same for the arcade", "pays nothing for any of it"). The same check with one word changed fails,
  so it can fail.
- Looked at: both sections at 1280px and 375px, light and dark.

Noticed, not changed: the Desk section's opening still says the whole thing "costs a visitor nothing to
ignore", and the arcade script loads with every page (PJ5). Small, but the same kind of claim.

**The Desk's opening line (Thomas, 2026-09-26: "change the claim, merge, merge pr4").** He ruled the change
without a wording round, so the agent chose the smallest true change, matching PJ5's "almost nothing":

> **Live:** "None of that is the interesting part. The interesting part is that it costs a visitor nothing to
> ignore."
>
> **Now:** "None of that is the interesting part. The interesting part is that ignoring it costs a visitor
> almost nothing."

---

# Step 2 — the case-study copy (drafted 2026-09-27)

Sources: receipts-001 §3F (the eight OK rows), the live `/projects` sections as fixed by PJ1–PJ6, the
Q-BQD2 answer, and the theme repo (private since 2026-09-26: read, never linked). Two excerpts are
quoted from its specs; each was checked verbatim against the file.

## BQD4 — ⚠ FLAG, read first: six more `/projects` lines, all in the Back Quarter section

**BQD0 §4 overstated what was traced.** It said both sections' claims were traced. The readers traced
the lessons and the loading and keyboard claims, not the opening paragraph, the rule paragraph or the
spec table. Those were traced on 2026-09-27, against the theme's code at its current commit. Six don't
match, and the case study would reuse all of them:

1. **"the farmhouse is the about page"**
   - What the code does: the farmhouse opens `/thomas` ("The farmhouse — step inside, this is me"); the
     cookshack opens `/about`.
   - Both builds, `LANDMARKS` in each script.
   - **Fix:** "the farmhouse is the page about me"
2. **"the grain elevator is the page about my diagnosis"**
   - What the code does: in the 3D world, the default, that landmark has been a medic hut since 1.0.731
     (2026-07-11). The grain elevator is only on the painted map.
   - **Fix:** "the medic hut is the page about my diagnosis"
3. **"the arcade barn boots the games"**
   - What the code does: neither build links the barn yet. The 3D world says "the arcade moves in soon";
     the painted map says "the games are moving in here soon".
   - **Fix:** cut the clause
4. **"the painted farm is a real image before any of it boots"**
   - What the code does: the still is now a frame of the 3D world (V0.42, `back-quarter-poster.webp`).
   - **Fix:** "the farm is a real image before any of it boots"
5. **"Nothing heavy loads until the visitor asks for it — the engines sit behind a click"**
   - What the code does: the Back Quarter's own engines do wait. But the site's decorative background
     loads three.js, about 600 KB before compression, for every visitor once the page is idle, unless
     reduced motion is on (`main.js`, `tcLoadWebGLBackground`).
   - V0.42 recorded it: "Cost: every visitor pays for it, including the phone visitors who now get the
     Painted Map."
   - **Fix, A (recommended):** "Nothing heavy of its own loads until the visitor asks for it — its
     engines sit behind a click —". The case study states the three.js cost as an honest limit (BQ6).
   - **Fix, B:** stop idle-loading three.js in the theme, then keep the live line. A theme change, and
     V0.42 already calls it "worth revisiting".
6. **Spec table, Sound: "Synthesised in the browser — engine, fire, machinery. No sample library"**
   - What the code does: there are ten recorded sounds (`assets/audio/bq-*.mp3`: the engine, animals, a
     splash, a crowd, a creak), fetched on the first sound-on, each with a synthesised fallback (V0.39
     L68–74). The 3D script references all ten. Fire, wind and tires are synthesised.
   - **Fix:** "Synthesised in the browser — fire, wind, tires — plus ten recorded farm and engine sounds,
     fetched only when sound is switched on"

Checked and matched: the church opens `/heritage` in both builds; bloom and colour grading run on
WebGL2 and a plain render on WebGL1; there is no CDN; the painted map is what touch and small screens
get, and also any browser without WebGL.

**Recommended:** fix all six on `/projects` now, as PJ1–PJ6 were, and carry them into the case study.

## BQD5 — ⚠ FLAG: "The game always starts" (Desk section, "Plan for the dependency that does not arrive")

The fallback exists in the code (`28b8e5f`). I found no record of it being tested by making the
renderer fail. The claim is a guess until someone forces the failure.
- **A (recommended):** test it before the Desk page ships: block the renderer script and load the
  pinball. If it starts, the line stands.
- **B:** soften the line to "It is built to start either way."

---

## `/work/back-quarter` (BQ1–BQ8)

### BQ1 — header

> **Label:** Case study · a personal site's front page
> **H1, A (recommended):** A homepage you drive around · **B:** The Back Quarter
> **Claim:** The front page of my personal site is a quarter section of Peace Country farmland you drive
> around in a buggy. Drive up to most of its buildings and press Enter, and a page of the site opens.
> The ordinary menu still works if none of it loads. *(Fixed 2026-09-27, round 4: nothing opens on
> arrival.)*
> **Spec table:** Stack: WordPress with a hand-coded Astra child theme · Three.js and Matter for the 3D
> world · Status: Live · Hosted: thomascheesman.ca, on Hostinger · Repo: Private · Since: July 2026. Then
> the `/projects` rows (3D world as fixed in PJ11, Where it runs, Surfaces, Sound as fixed in BQD4, Input
> as fixed in PJ12, Dependencies), moved here so there is one copy. *(Fixed 2026-09-27, C-24.)*
> **Page title / link preview:** *(the H1)* - Thomas Cheesman · description: the claim.

- **H1 A** tells a stranger what it is, which a name can't. This is the BYR reasoning. The sub-menu uses
  the H1.
- **"Most of its buildings":** the farmhouse, cookshack, medic hut and church open pages, and the tower
  opens bareyourrare.org. The barn, shed and mailbox open nothing yet.
- **Since:** the spec was written 2026-07-01 (`4f8e693`); the first drivable build was 2026-07-02
  (`faca583`).
- **WordPress** appears once, here.

### BQ2 — The ask

> **H2:** Somewhere to tell the story
>
> *Pull quote, Thomas, 2026-09-26 (Q-BQD2; Q-BQD3 A):*
>
> **A (recommended), two things closed up:** "I made my personal site mostly for family. Social media is
> messy and can get hard to use for some. I wanted somewhere I could tell the story of where my
> ancestors came from and how we came to exist in Grande Prairie as a happy family. I wanted to make it
> with easter eggs for them to discover if they wanted to/ there's games and puzzles and such, a literal
> arcade, a map you race around and collect coins while exploring the "back Quarter". TBH, I doubt it
> will see much traffic until I pass on but that's ok, for now I am here :)"
>
> **B:** exactly as typed ("i made…", "that's  ok").
>
> *Then the `/projects` opening paragraph (as fixed in BQD4) and the ruled childhood paragraph ("I grew up
> on that land…"), unchanged.*

- **A changes only two things:** "i" becomes "I" at the start, and the double space in "that's  ok" is
  closed. The slash, "TBH", ":)" and "back Quarter" stay as he wrote them.
- **The H2** takes his words "somewhere I could tell the story".
- **"collect coins"** is in the 3D script.

### BQ3 — The standard

> **H2:** A homepage has to stay a homepage
>
> *The `/projects` paragraph under "The rule underneath it", as fixed in BQD4 4–5.*
>
> *Excerpt, verbatim from the build spec:* "Performance budget: zero new bytes on first paint beyond the
> preview image (≤ ~180KB webp) + the invitation chip. Pixi/Matter/engine/painting lazy-load on
> engagement only."
>
> *Caption:* From the build spec, §4, written 2026-07-01, the day before the first drivable build. The
> repo is private.

- **Checked verbatim** against `docs/QUARTER-SECTION-SPEC.md` L142–144.
- **Only the budget is quoted.** The same section says the old hero stays at the top. The September
  promotion (`HERO-PROMOTION-SPEC.md`) changed that, so quoting it would be out of date.

### BQ4 — What the AI got wrong

> **H2:** Right in the code, wrong on the screen
>
> **1. Glow that never switched on.** The bloom effect, the glow around lights at night, was committed as
> "the lights glow". Its files had been bundled from search hits that were only checks for the pieces
> it needed, not the pieces themselves. The effect failed as it loaded, and the fallback quietly started
> the farm without it, so nothing looked broken. *(a tooling error · receipts-001, R-160)*
>
> **2. A fix that made a new noise.** The campfire's crackle clicked like tiny firecrackers. The fix sent
> every pop through the same tuned filter, so every pop rang the same note. *(looked right but was not
> measured · receipts-001, R-163)*
>
> **3. Animals that were said to wander.** The cows and sheep shipped with "graze/wander AI". Each move
> was a single push that the physics' friction killed in under a second, so for six days they stood
> still between moves. *(looked right but was not measured · receipts-001, R-164)*

- **Checked against the receipts:**
  - **1:** `5207d03` (the claim, 09:31) and `0f2f9f3` L3–8 (the fix, 09:34, 2026-07-09).
  - **2:** `e5dba29` L3–6 and `d1367d5` L3–6.
  - **3:** `fe821f7` L19–20 (2026-07-05) and `5e355e3` L7–12 (2026-07-11).
- **"a tooling error"** is a new kind label. No live page has used it yet. FIX it if you want other words.
- **R-162 (daylight bloom) is the spare.** It already backs the bloom lesson, which moves into BQ6.

### BQ5 — How I caught it

> **H2:** I looked, I listened, I watched
>
> **1. I looked.** I caught it. The fix came three minutes after the commit that claimed the glow: the
> missing pieces went in, in the order they depend on each other. *(Falls under: "done", "verified" and
> "deployed" are claims; prove them from outside · receipts-001, R-160)*
>
> **2. I listened.** Both times it was my ear: first the firecrackers, then "the fire sounds like tin
> bashing." The third version is a low ember roar with short pops, each through its own randomly tuned
> filter. Nothing rings. *(Falls under: test the thing itself, not a proxy for it · receipts-001, R-163)*
>
> **3. I watched.** I said the animals were too still. The cause was in the physics, and a walk now holds
> its heading for a few seconds and is pushed every frame. The agent's test browser can't run the
> animation, so only someone driving the farm could have seen it. *(Falls under: a build or a script
> cannot judge how something looks · receipts-001, R-164)*
>
> *Rules table:* three rows, one per miss.

| The correction | The standing rule | Enforced in |
|---|---|---|
| The glow was committed as working while the fallback hid its failure (R-160) | "Done", "verified" and "deployed" are claims. Prove them from outside | `CLAUDE.md` · rule 2 |
| A sound fix was judged by its code, and rang like tin (R-163) | Test the thing itself, not a proxy for it | `CLAUDE.md` · rule 1 |
| The animals were said to wander, and nobody had watched them (R-164) | A build or a script cannot judge how something looks. Look at it rendered | `CLAUDE.md` · rule 4 |

- **Who caught what:** all three are Thomas's, so "I" throughout.
  - R-160: his word, 2026-09-26. The record doesn't say how, so the copy says only "I caught it" and
    what the fix did.
  - R-163 and R-164: in the record ("Thomas: …").
- **"Three minutes"** comes from the two commits' timestamps.
- **"Only someone driving it"** comes from `back-quarter.js`'s header: automation tabs freeze the
  animation, so "the FEEL check is Thomas driving it in a foreground tab".
- **"Falls under", not "became":** the truth rules date from 2026-09-23, after all three misses. This is
  the same as on BYR.

### BQ6 — What shipped

> **H2:** A farm that is also a menu
>
> *The `/projects` steering and bloom paragraphs (live since PJ1 and PJ2), unchanged. Fig. 1, the 3D
> build (`back-quarter-3d.webp`) with its `/projects` caption, unchanged. The "Drive it on
> thomascheesman.ca" line, unchanged.*
>
> **The honest limits:** Checked in September 2026. The farm can't be driven on a phone or tablet yet,
> and the barn doesn't open anything. The site's decorative background still loads the 3D library, about
> 600 KB before compression, for every visitor once the page is idle, including phone visitors, who can't
> drive the farm at all. *(Fixed 2026-09-27, C-24.)*

- **The fire paragraph isn't repeated here.** BQ4 2 and BQ5 2 tell it with receipts.

### BQ7 — Receipts

- `reviews/copy-review-005.md`, Q-BQD2 (why I built it, in my words)
- `plans/receipts-001.md` §3F (R-160, R-163, R-164; R-162 behind the bloom paragraph)
- `CLAUDE.md` (rules 1, 2, 4)
- the live site, thomascheesman.ca

The theme repo is private, so the specs and commits aren't linked (Q-BQD1 A).

### BQ8 — what goes with it (not copy)

1. **The page:** `public/work/back-quarter.html` (plan-001's path), on the BYR pattern. The preview goes
   in `.assetsignore`, with the draft banner and `noindex`.
2. **The sub-menu:** the label is the H1. It goes second, after the graph and before BYR, which is the
   `/projects` order. The Desk page goes third. That makes 13 files once both ship.
3. **P3:** `/projects` and home link the case study, in the same push.
4. **Fig. 1** is already on the site. No new image.
5. **The usual checklist.** The security policy isn't changed and no script is added.

---

## `/work/desk-and-drawer` (DD1–DD8)

### DD1 — header

> **Label:** Case study · a personal site's menu and footer
> **H1, A (recommended):** A menu that is a photograph of my desk · **B:** The Desk and the Drawer
> **Claim:** My personal site's navigation is a photograph of my desk, and its footer is a drawer with a
> pinball table in it. A visitor who wants a plain list of links gets one, one click in.
> **Spec table:** Stack: WordPress with a hand-coded Astra child theme · plain JavaScript and CSS, no
> framework · Status: Live · Hosted: thomascheesman.ca, on Hostinger · Repo: Private · Since: May 2026.
> Then the `/projects` rows (Loaded on demand, Accessibility as fixed in PJ4, Scores, Nice touches),
> moved here. "Built with" folds into Stack.
> **Page title / link preview:** *(the H1)* - Thomas Cheesman · description: the claim.

- **Since:** the desk menu dates from 2026-05-12 (`265cb03`); the drawer and pinball from 2026-05-20
  (`541143c`).
- **H1 A** is 38 characters, the longest in the sub-menu. It needs checking at 375px.

### DD2 — The ask

> **H2:** Things to find, if you want to
>
> *Pull quote, the same answer, cut to its middle:* "I wanted to make it with easter eggs for them to
> discover if they wanted to/ there's games and puzzles and such, a literal arcade, …"
>
> *Then the `/projects` Desk opening paragraph and "None of that is the interesting part…" (live since
> 2026-09-26), unchanged.*

- **The quote is verbatim, cut with an ellipsis.** It's the same answer as BQ2, so there's one source
  and one citation.
- **A and B** from BQ2 don't touch this part, so it's the same either way.

### DD3 — The standard

> **H2:** A picture that is still a menu
>
> *The `/projects` paragraph "An interface that is a picture still has to be a menu" (as fixed by PJ4),
> unchanged.*
>
> *Excerpt, verbatim from the drawer's spec:* "Performance: the drawer + libs are lazy-loaded on first open
> — visitors who never trigger it pay nothing. Keep it that way; budget download weight." · "Mobile +
> desktop, touch + keyboard. Touch is not an afterthought."
>
> *Caption:* From the drawer's spec, §5 "Constraints & guardrails", written 2026-06-22, before the June
> pinball rebuild. The repo is private.

- **Checked verbatim** against `docs/SECRET-DRAWER-VISION.md` L201–203. The source's bold marks are
  dropped.
- **The same section** also names an outside model and carries a privacy rule about family content.
  Neither is quoted.
- **⚠ FLAG: there's no written standard for the Desk itself.** Nothing written before the desk was built
  (2026-05-12) turned up. The closest is the theme `CLAUDE.md`'s "plan + propose" rule for these
  surfaces (2026-05-20), which is about process, not what good looks like. So the Desk half of the
  standard is the principle as the page states it.

### DD4 — What the AI got wrong

> **H2:** It blamed the browser, hid the exit, and trusted the test balls
>
> **1. The browser got the blame.** A shimmer that sweeps across each object on the desk was changed three
> times without anyone seeing it render. Two of those commits blamed Chrome, "a parsing issue some
> Chrome builds have". The cause was an older style rule of the agent's own, overriding the new
> animation. *(plausible but invented · receipts-001, R-168)*
>
> **2. The way out was out of reach.** The "View as a plain list" button, the desk's way out to an
> ordinary list of links, sat inside the monitor's clipped area, where it couldn't be reached. *(looked
> right but was not measured · receipts-001, R-169)*
>
> **3. The test balls passed; play didn't.** A pinball fix was "validated in-browser" with dropped test
> balls, and real play still found balls stuck at the sides. The next fix's one failing drop was
> written off as "a rare flipper-base settle that real momentum clears". The next day's commit calls it
> "the recurring flipper-base trap". *(looked right but was not measured · receipts-001, R-172)*

- **Checked against the receipts:**
  - **1:** `e3962e0`, `b2d382a` L5–6, `525d1a6`, and `17c073d` L3–7 (the root cause).
  - **2:** `bca7b22` L3–4.
  - **3:** `0fc31ac` L3–6, `0905002` L3–12, and `f037e11` L12–14.
- **R-170 (the audit that asked for work already done) is the spare.**

### DD5 — How I caught it

> **H2:** I used it
>
> **1. I saw nothing there.** I caught it in my browser: none of the three versions showed. The fix
> removed the old rule and brought back the technique the commits had said Chrome couldn't handle.
> *(Falls under: a recommendation, a premise or a summary is a hypothesis until it is checked ·
> receipts-001, R-168)*
>
> **2. I went looking for the way out.** I caught it. The button moved out from under the monitor's edge
> to sit below it. *(Falls under: a build or a script cannot judge how something looks · receipts-001,
> R-169)*
>
> **3. I played it.** "It keeps getting stuck to the right and left." The bar that fixed those two traps
> was my idea: a bar "in line with the top of the blue triangles". The trap written off as rare got a
> watchdog the next day: a ball that sits still for about three seconds gets a nudge. *(Falls under:
> test the thing itself, not a proxy for it · receipts-001, R-172)*
>
> *Rules table:* three rows, one per miss.

| The correction | The standing rule | Enforced in |
|---|---|---|
| A bug of the agent's own was blamed on the browser (R-168) | A recommendation, a premise or a summary is a hypothesis until it is checked | `CLAUDE.md` · rule 13 |
| The plain-list button was unreachable, and nobody had looked (R-169) | A build or a script cannot judge how something looks. Look at it rendered | `CLAUDE.md` · rule 4 |
| Test balls passed while real play still stuck (R-172) | Test the thing itself, not a proxy for it | `CLAUDE.md` · rule 1 |

- **Who caught what:** all three are Thomas's.
  - R-168: the record's "user's Chrome", his word 2026-09-26.
  - R-169: his word.
  - R-172: the record quotes him.
- **R-168 and R-169:** the record doesn't say how he found them. The copy says "I caught it" and what the
  fix did, nothing more. **"I saw nothing there" and "I went looking for the way out" are guesses at
  how. FIX them if they're wrong.**
- **"The bar… was my idea":** `0905002` ("Thomas's fix… his 'bar in line with the top of the blue
  triangles'").
- **"About three seconds":** `f037e11` L13 ("~3s").

### DD6 — What shipped

> **H2:** A desk you can ignore, and a drawer with a game in it
>
> *The `/projects` paragraphs "Nothing loads until someone asks for it" (live since PJ5 and PJ6) and "Plan
> for the dependency that does not arrive" (as settled by BQD5), unchanged. Fig. 1, the desk; Fig. 2,
> the arcade; both with their `/projects` captions, unchanged. The "Open the menu on thomascheesman.ca"
> line, unchanged.*
>
> **The honest limits:** Checked in September 2026. Only the five objects that open something can be
> reached with the keyboard. The other thirteen are hover cards, so their notes can't be read without a
> mouse. The arcade's script loads with every page.

- **"Five" and "thirteen"** come from `inc/desk-menu.php` at the current commit: 5 `role="button"` with
  `tabindex="0"`, and 13 `role="group"`. I read the source; I didn't Tab through it.
- **These are counts of the page's own parts, not of a corpus,** so they won't go stale unless the desk
  changes. **KEEP** them, or **FIX** to "most of the objects".

### DD7 — Receipts

- `reviews/copy-review-005.md`, Q-BQD2
- `plans/receipts-001.md` §3F (R-168, R-169, R-172)
- `CLAUDE.md` (rules 1, 4, 13)
- the live site, thomascheesman.ca

### DD8 — what goes with it (not copy)

1. **The page:** `public/work/desk-and-drawer.html`, on the same pattern, with a preview first.
2. **The sub-menu:** third, after the Back Quarter.
3. **P3.** Both figures are already on the site. The security policy isn't changed.

---

## P3 — `/projects` and home, once both pages ship

> **`/projects`, Back Quarter:** keep the label, the H2, the two opening paragraphs (as fixed in BQD4),
> the figure and the "Drive it" line. Add: "What it was built to, three things the AI got wrong while
> building it, and how I caught them: read the case study." "Three things the build taught me", "The
> rule underneath it" and the spec table move to the case study.
>
> **`/projects`, Desk:** keep the label, the H2, the two opening paragraphs, the desk figure and the "Open
> the menu" line. Add the same "read the case study" line. "Three things", the arcade figure and the spec
> table move.
>
> **Home:** the two cards link the case studies instead of `/projects#quarter` and `/projects#desk`, as
> Q-IG3 did for the graph. The cards' words don't change.

Noticed on the home cards, not proposed: the Desk card says "nothing heavy loads for a visitor who
never asks for it". For the desk itself that's true, but three.js loads site-wide (BQD4 5). Say if you
want it changed with PJ7–PJ12.

**C-23** (the `/projects` lede) is settled after both pages ship.

## Open for Thomas (step 2)

- **BQD4:** fix the six lines on `/projects` now (PJ7–PJ12). For 5, A or B.
- **BQD5:** A (test the pinball fallback) or B (soften).
- **BQ1–BQ7:** H1 A or B; quote A or B; the rest OK / FIX / CUT.
- **DD1–DD7:** H1 A or B; the DD3 flag; the two "how" guesses in DD5; "five / thirteen" KEEP or FIX; the
  rest OK / FIX / CUT.
- **P3:** OK.

### Rulings, step 2, round 1 (Thomas, 2026-09-27)

Verbatim: "pause here. the phone won't get the 2d nor 3d map/menu's. It is high time we benched the 2d menu
altogether. So, to keep this simple - only have the 3d menu and only on pc. BDQ4 - fix, N/A, fix. ok, fix,
fix. BDQ5 why are we talking about this anyway?"

- **Decision for thomascheesman.ca (a theme change, not copy):**
  - The painted map (2D) is retired.
  - The 3D world runs on PCs only.
  - Phones get neither.
  - **Today's code differs:** touch screens under 820px, and browsers without WebGL, get the painted map
    (`back-quarter.js`, `prefersPaintedMap()`). So this is a change still to make, not a description of the
    live site.
  - The Back Quarter is a plan-first surface, so it gets a plan before code. **Paused at his word.**
- **What it changes here, once it's live:**
  - PJ1's last sentence ("The painted map that phones get still turns on the spot") goes.
  - The spec rows "The Painted Map" and "Input" change.
  - BQ1's stack loses "Pixi and Matter".
  - BQ6's phone limit goes.
  - The copy changes when the theme does, not before, because copy describes what's live.
- **BQD4:** 1 fix · 2 N/A · 3 fix · 4 OK · 5 fix, read as A (the copy fix; B, the theme change, stays open) ·
  6 fix.
  - **Reading of 2:** with the painted map retired, the grain elevator leaves the site, so the line then
    needs the medic hut or a cut. Asked.
- **BQD5:** he asked why it's here; answered in the chat.
- **Nothing is applied to `/projects` yet**, at "pause here".

### Rulings, step 2, round 2 (Thomas, 2026-09-27)

Verbatim: "medic hut, cut the game always starts, write handoff-021"

- **BQD4 2: the medic hut.**
- **BQD5: cut** "The game always starts."
- **Applied to `public/projects.html` on the branch (PR #5); live once PR #5 is merged:**
  - BQD4 1–6, with 5 as A.
  - BQD5.
- **Checked locally:**
  - `scripts/site_check.py` passed 84 of 84.
  - The rendered page carries the four new lines and none of the seven removed phrases. The same check
    with one word changed fails.
  - Looked at in a screenshot, the Back Quarter section at 375px.
- **Not changed, on purpose:** PJ1's phone sentence and the painted-map rows in the spec table. They're
  true until the theme change (handoff-021 O-20) lands.
- **Still to rule in step 2:** BQ1–BQ7 and DD1–DD7 (H1 A/B, quote A/B, the DD3 flag, the two DD5 guesses,
  "five / thirteen"), and P3.

### Rulings, step 2, round 3 (Thomas, 2026-09-27)

Verbatim: "A, A, ok, 1, ok, why is there a painted map"

- **BQ1: A**, the H1 is "A homepage you drive around".
- **BQ2: A**, the quote with "I" capitalised and the double space closed.
- **BQ3: OK.**
- **BQ4: OK.** Asked what "1" meant; Thomas: "1 means ok".
- **BQ5: OK.**
- **BQ6:** he asked why there is a painted map. Answered in the chat: the theme at the local checkout still serves
  it to touch screens under 820px and to browsers without WebGL (`back-quarter.js` L128–140), and O-20
  (retire it) hasn't been built. Not ruled.
- **BQ7: OK** ("bq7 ok").
- **Next, at his word ("plan O-20 next"):** the O-20 plan in the theme repo, before the Desk copy. BQ6's
  painted-map limit and BQ1's "Pixi and Matter" wait for it.

### Rulings, step 2, round 4 (Thomas, 2026-09-27)

Verbatim: "both ok, fix pj7 and bq1, build it."

- **Found while planning O-20:** in the 3D world a building opens only on Enter (`back-quarter-3d.js`
  `enterLandmark`, called on Enter). Driving up shows a prompt and nothing more. Thomas: "the buildings
  don't open".
- **PJ7, `/projects` Back Quarter opening paragraph:** "Drive up to one and it opens." →
  "Drive up to one and press Enter to step inside." Applied to `public/projects.html`.
- **BQ1 claim:** "Drive up to most of its buildings and a page of the site opens, and the ordinary menu
  still works if none of it loads." → "Drive up to most of its buildings and press Enter, and a page of
  the site opens. The ordinary menu still works if none of it loads." Fixed in the draft above.
- **"both ok":** the theme's homepage lede and the phone line in the O-20 plan (theme repo,
  `docs/BQ-3D-ONLY-PLAN.md`). Theme copy, not this site's.
- **"build it":** O-20 is being built in the theme repo.

---

## C-24 — the Back Quarter copy follows O-20 (PJ8–PJ14, and fixes to BQ1 and BQ6)

**Written:** 2026-09-27, after handoff-022.
**Why:** O-20 shipped in the theme (1.0.755, `4a8eb03`). The painted map is gone, so seven live lines on
tc-ventures.ca now describe something that isn't there. Copy follows the site (round 1).

**Traced against:** the theme at `baa7b24` (1.0.758), by reading the code. Nothing was loaded from
thomascheesman.ca. `back-quarter-3d.js` didn't change between O-20 and `baa7b24`, so BQD4's traces of the
3D world, Surfaces and Sound rows still hold.

**What the code does now:**
- **Who gets the 3D world:** a device whose main pointer is a mouse or trackpad (`(hover: hover) and
  (pointer: fine)`), with WebGL (`back-quarter.js`, `isPC()` and `hasWebGL()`).
- **Phones and tablets:** the poster, and "The farm is a 3D world built for a computer. On a phone, the
  menu up top goes everywhere." (`front-page.php` L55). No button.
- **A PC without WebGL:** "This browser can’t run the 3D world. The menu up top goes everywhere."
- **A failed load:** "The 3D world couldn’t start. The menu up top goes everywhere." The button stays for
  a retry.
- **What loads on engage:** Matter, three r128, the bloom stack and `back-quarter-3d.js`, only on the
  button or W / Up arrow (`engage3d`). **Matter is the 3D world's physics** (`back-quarter-3d.js`
  L1278 on). **Pixi isn't used by the Back Quarter at all** (no match in either script or
  `front-page.php`). It stays in `vendor/` for the drawer's pinball.
- **Controls shown:** "W A S D or arrows · Enter steps inside · Esc hops out" (`front-page.php` L53).
- **The site-wide wash** still idle-loads three.js for every visitor unless reduced motion is on. Phones
  now draw it at 1x pixels and about 20 fps (`main.js`, 1.0.757).

### PJ8 — `/projects` label (Back Quarter)

> **Live:** "The front page itself · Three.js, Pixi, Matter"
> **FIX:** "The front page itself · Three.js, Matter"

### PJ9 — `/projects`, the steering lesson's last sentence (PJ1)

> **Live:** "…Reversing flips the steering sense, the way it does in a real yard. The painted map that
> phones get still turns on the spot."
> **CUT** the last sentence. The paragraph ends at "real yard."

### PJ10 — `/projects`, Fig. caption

> **Live:** "The 3D build, mid-afternoon. The same quarter section as the painted map, modelled and lit,
> with a day and night cycle running over it."
> **FIX:** "The 3D world, mid-afternoon: the quarter section modelled and lit, with a day and night cycle
> running over it."

### PJ11 — `/projects` spec table: the 3D world row and the Painted Map row

> **Live:** "3D world — Three.js · custom vehicle handling · bloom and colour grade on WebGL2, plain render
> on WebGL1" and "The Painted Map — Pixi and Matter over a painted board — the fallback: phones, no WebGL,
> or a failed load"
> **FIX, 3D world:** "Three.js, with Matter for the physics · custom vehicle handling · bloom and colour
> grade on WebGL2, plain render on WebGL1"
> **A (recommended), replace the Painted Map row:** "Where it runs — A computer with a mouse or trackpad
> and WebGL. Phones and tablets see a still of the farm and a line pointing at the menu"
> **B:** cut the row, and say nothing about phones in the table.

- **Why A:** a hiring reader is likely to open it on a phone. The table should tell them before they
  try, and the fallback is part of the design, not an apology.
- **Why Matter moves into the 3D row:** with the Painted Map row gone, the label would name Matter and
  nothing in the table would say what it does.

### PJ12 — `/projects` spec table, Input

> **Live:** "Keyboard, and a touch build with a reduced tier for small screens"
> **FIX:** "Keyboard: W A S D or the arrows, Enter to step inside, Esc to hop out"

- The touch controls are still in the 3D script, kept for the later phone job (O-20), but no phone or
  tablet reaches them now.

### PJ13 — `/projects`, the "Drive it" line

> **Live:** "Drive it on thomascheesman.ca — the 3D world is what the button opens, and the painted map is
> what a phone gets, or a browser that cannot run the engine. Neither one loads until someone asks for
> it."
> **FIX:** "Drive it on thomascheesman.ca, on a computer — the 3D world is what the button opens, and it
> doesn't load until someone asks for it. A phone gets a still of the farm and the ordinary menu."

- The link text stays "Drive it on thomascheesman.ca". ", on a computer" sits outside the link.

### PJ14 — home page, the Back Quarter card

> **Live:** "Built with — Three.js · Pixi · Matter · no build step"
> **FIX:** "Built with — Three.js · Matter · no build step"

- The card's paragraph ("…it degrades to an ordinary menu if the graphics never load") is still true. No
  change.

### BQ1 FIX — the case study's spec table

> **Draft:** "Stack: WordPress with a hand-coded Astra child theme · Three.js for the 3D world · Pixi and
> Matter for the painted map · …" Then the `/projects` rows (3D world, The Painted Map, Surfaces, Sound,
> Input, Dependencies).
> **FIX:** "Stack: WordPress with a hand-coded Astra child theme · Three.js and Matter for the 3D world ·
> …" Then the `/projects` rows as fixed by PJ11 and PJ12 (3D world, Where it runs or nothing, Surfaces,
> Sound, Input, Dependencies).

### BQ6 FIX — the case study's honest limits

> **Draft:** "Checked in September 2026. The painted map that phones get still turns on the spot, and
> neither build's barn opens anything yet. The site's decorative background loads the 3D library, about
> 600 KB before compression, for every visitor once the page is idle, including phone visitors, who get
> the painted map and never use it."
> **FIX:** "Checked in September 2026. The farm can't be driven on a phone or tablet yet, and the barn
> doesn't open anything. The site's decorative background still loads the 3D library, about 600 KB
> before compression, for every visitor once the page is idle, including phone visitors, who can't drive
> the farm at all."

- "Yet": Thomas, "we will bring it to the mobile" (O-20). The line goes when that ships.
- The barn: `back-quarter-3d.js` is unchanged since BQD4 3, so the barn still opens nothing.

### Open for Thomas (C-24)

- **PJ8–PJ10, PJ12–PJ14:** OK / FIX / CUT.
- **PJ11:** A (a "Where it runs" row) or B (cut the row).
- **BQ1 and BQ6 fixes:** OK / FIX.
- **On your word,** PJ8–PJ14 go on `/projects` and home, checked locally with `site_check.py` and a
  rendered-text check with a control, then curled live against `main` after the merge.

### Rulings, C-24 (Thomas, 2026-09-27)

Verbatim: "all ok, pj11 A"

- **PJ8–PJ10, PJ12–PJ14: OK.** Applied to `public/projects.html` and `public/index.html`.
- **PJ11: A**, the "Where it runs" row, and Matter in the 3D row. Applied.
- **BQ1 and BQ6 fixes: OK.** Fixed in the drafts above.
