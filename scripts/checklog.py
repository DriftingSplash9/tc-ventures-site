"""checklog.py — every FAIL line of a check run, printed again as the run ends.

"Keep every FAIL line of a check run. A filter on the lines you expect hides the one that fails." That
trap stood at 9.8 in handoff-037, so it was due to drop at the next, and Thomas ruled it into code
(2026-10-03). So the checkers that print PASS and FAIL lines (site_check.py, budget.py, cs_check.py,
deploy_wait.py) keep each FAIL line, and as the process exits, however it exits, print them all again
on stderr, after everything else. A pipe through grep, tail or head filters stdout only, so it can't
hide them. (Only `2>&1 |` can; don't.)

    import checklog
    failed = checklog.failed()     # in the checker's check(): if not ok: failed.append(line)

Not used where FAIL lines are planted on purpose (budget.py --controls): those are expected.
"""
import atexit, sys


def failed():
    """A list for a checker's FAIL lines; whatever is in it when the process exits is printed again."""
    lines = []
    atexit.register(_again, lines)
    return lines


def _again(lines):
    if not lines:
        return
    sys.stdout.flush()
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")   # the Windows console is cp1252
    except (AttributeError, ValueError):
        pass
    print(f"\n{len(lines)} FAIL line{'' if len(lines) == 1 else 's'} in this run, again:", *lines,
          sep="\n", file=sys.stderr, flush=True)
