# Copy review 005 — the Back Quarter and the Desk and the Drawer

**Written:** 2026-09-26
**Why:** the last two case studies of Phase 1b (plan-001 §5 note, 2026-09-25):
`/work/back-quarter` and `/work/desk-and-drawer` (plan-001 §3). One receipts pass over
thomascheesman.ca covers both. Thomas chose a new review, 005, over adding to 004 (2026-09-26).
**Status:** Step 1 (BQD0) ruled 2026-09-26: Q-BQD1 A, Q-BQD2 answered, Q-BQD3 A, and R-160 to R-174 in
receipts-001 §3F (8 OK, 7 CUT; see "Rulings, round 2"). PJ1–PJ6 ruled and applied to `/projects` the
same day. No case-study copy drafted yet: that is step 2.

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
