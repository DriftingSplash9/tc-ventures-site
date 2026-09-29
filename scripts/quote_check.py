"""quote_check.py — is every quote verbatim in its source?

Usage: python scripts/quote_check.py FILE "quote" ["quote" ...]
       python scripts/quote_check.py --ledger [REVIEW]
       add -v to list every piece, not only the failures

A quote passes when it appears in FILE exactly as written, after two
normalisations only: line endings, and runs of whitespace (so a quote may
cross a line wrap). Nothing else is forgiven: not case, not curly quotes, not
markdown such as ** or `, and not two bullets joined into one quote. An
ellipsis (…) marks a cut: each piece between cuts must be verbatim on its own,
with the spaces and , : ; at its ends trimmed. Pieces under 4 characters are
skipped, and the summary counts them.

Every piece is also its own control: the same piece with one of its words
changed must NOT be found. If it is, the check could not have failed for that
piece, and the run fails (CLAUDE.md rule 3). A run that finds no quotes to
check fails too.

--ledger reads the "Rests on" column of every LG row in
reviews/copy-review-006.md (or REVIEW) and checks each quote against the
handoff the row names. In a cell, quotes are "..." and are separated by ; , or
a space. A quote may hold quotes of its own ("ruled "LG0 ok, all A"."): a
quote ends only at a " followed by ; , a space or the end of the cell.

Exit code 1 if any piece is not found or any control could not fail.
Written 2026-09-29 (INFRA-16), from the scratchpad check used for
copy-review-006, which caught a quote that joined two bullets.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, "..")
MIN_PIECE = 4
LG_ROW = re.compile(r"^\| (LG\d+) \| (\d{3}) · [\d-]+ \| .*? \| (.*) \|$", re.M)
QUOTE = re.compile(r'(?:^|(?<=[\s:]))"(.+?)"(?=[;,\s]|$)')


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def pieces(quote):
    """The parts of a quote between ellipses, trimmed; short ones come back as None."""
    out = []
    for part in quote.split("…"):
        p = norm(part).strip(" ,:;")
        out.append(p if len(p) >= MIN_PIECE else None)
    return out


def changed(piece):
    """The piece with one of its words changed: the longest word gets a q after its first letter."""
    words = re.findall(r"[^\W\d_]{3,}", piece) or re.findall(r"\w+", piece)
    if not words:
        return piece + "q"
    w = max(words, key=len)
    return piece.replace(w, w[0] + "q" + w[1:], 1)


def check_file(path, quotes, label, verbose, tally):
    """Check each quote against one file. Adds to tally: found, missing, skipped, bad controls."""
    src = norm(open(path, encoding="utf-8").read())
    for q in quotes:
        for p in pieces(q):
            if p is None:
                tally["skipped"] += 1
                continue
            found = p in src
            control = changed(p) not in src
            tally["found" if found else "missing"] += 1
            if not control:
                tally["bad_controls"] += 1
            if not found or not control or verbose:
                state = "ok" if found else "NOT FOUND"
                if not control:
                    state += ", CONTROL COULD NOT FAIL"
                print(f"{state:9} {label}: {p!r}")


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the Windows console is cp1252
    args = [a for a in sys.argv[1:] if a != "-v"]
    verbose = "-v" in sys.argv[1:]
    tally = {"found": 0, "missing": 0, "skipped": 0, "bad_controls": 0}
    if not args:
        sys.exit(__doc__)
    if args[0] == "--ledger":
        review = args[1] if len(args) > 1 else os.path.join(REPO, "reviews", "copy-review-006.md")
        rows = LG_ROW.findall(open(review, encoding="utf-8").read())
        for lg, num, cell in rows:
            quotes = QUOTE.findall(cell.strip())
            if not quotes:
                print(f"NO QUOTE  {lg}: its Rests on cell has none the parser can read")
                tally["missing"] += 1
            check_file(os.path.join(REPO, f"handoff-{num}.md"), quotes, f"{lg} (handoff-{num})", verbose, tally)
        where = f"{len(rows)} LG rows in {os.path.basename(review)}"
    else:
        path, quotes = args[0], args[1:]
        check_file(path, quotes, os.path.basename(path), verbose, tally)
        where = f"{len(quotes)} quote(s) against {os.path.basename(path)}"

    checked = tally["found"] + tally["missing"]
    print(f"{where}: {checked} pieces checked, {tally['found']} verbatim, {tally['missing']} not found, "
          f"{tally['skipped']} skipped (under {MIN_PIECE} characters); "
          f"{checked - tally['bad_controls']} of {checked} controls failed as they should")
    ok = checked > 0 and not tally["missing"] and not tally["bad_controls"]
    if checked == 0:
        print("FAIL: nothing was checked")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
