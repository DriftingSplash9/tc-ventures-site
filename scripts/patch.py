"""patch.py — exact-match text edits across files: all of them, or none.

Most of this repo is CRLF in a Windows checkout, and some files are LF. An edit
made with a heredoc, sed or a tool that normalises line endings can flip a whole
file, or match the wrong place. This does neither:

  - Each file is read as UTF-8 and matched with its CRLF read as LF, so `old`
    and `new` are always written with plain \\n. It is written back with the
    endings it had. A file with mixed endings is refused.
  - Edits to one file apply in order, and each `old` must occur exactly once
    in the file as the edits before it left it. Zero or two matches is an
    error, never a guess.
  - Nothing is written until every edit in every file has matched. Then all
    files are written; otherwise none is, and every problem is listed.

As a module (scripts/ship_case_study.py uses it):

    from patch import Patch
    p = Patch()
    p.edit("public/contact.html", old, new)     # queue; nothing is read yet
    p.text("public/contact.html")               # the file as LF text, with the
                                                # edits queued so far applied
    print(p.apply())                            # or p.apply(dry=True)

From the shell, with the edits in a JSON file (write it with an editor or the
Write tool, not a heredoc):

    python scripts/patch.py EDITS.json [--dry-run]

    EDITS.json: {"public/contact.html": [["old", "new"], ...], ...}
    Paths are relative to the current directory, or absolute.

Exit code 1, and nothing written, if any edit fails to match exactly once.
Written 2026-09-29 (INFRA-13), from the scratchpad patch.py of 2026-09-29 and
ship.py of 2026-09-28. Unlike the first, it is all-or-nothing across files,
not only within one.
"""
import json, os, sys


class PatchError(SystemExit):
    pass


def key(path):
    """One key per file, however its path is spelled (Windows paths ignore case)."""
    return os.path.normcase(os.path.abspath(path))


def shown(path, base=None):
    try:
        return os.path.relpath(path, base or os.getcwd()).replace(os.sep, "/")
    except ValueError:      # another drive
        return path


class Patch:
    def __init__(self):
        self.edits = {}      # key -> [(old, new), ...], in the order queued
        self.paths = {}      # key -> the path as first given, made absolute

    def edit(self, path, old, new):
        self.paths.setdefault(key(path), os.path.abspath(path))
        self.edits.setdefault(key(path), []).append((old, new))

    @staticmethod
    def read(path):
        """(text with LF endings, 'CRLF' or 'LF'); refuses a file with mixed endings."""
        raw = open(path, "rb").read().decode("utf-8")
        crlf, lf = raw.count("\r\n"), raw.count("\n")
        if crlf and crlf != lf:
            raise PatchError(f"{path}: mixed line endings ({crlf} CRLF of {lf}); nothing written")
        return raw.replace("\r\n", "\n"), "CRLF" if crlf else "LF"

    def _run(self, path):
        """Apply this file's queued edits in memory: (text, endings, problems)."""
        text, endings = self.read(path)
        problems = []
        for old, new in self.edits.get(key(path), []):
            n = text.count(old) if old else 0
            if n != 1:
                problems.append(f"{n} matches for {old[:80]!r}")
                continue
            text = text.replace(old, new)
        return text, endings, problems

    def text(self, path):
        """The file as LF text, with the edits queued for it so far applied."""
        text, _, problems = self._run(path)
        if problems:
            raise PatchError(f"{shown(path)}: nothing written: " + "; ".join(problems))
        return text

    def apply(self, dry=False, base=None):
        """Write every queued edit, or none. The report shows paths relative to base (default: here)."""
        done, problems = {}, []
        for k, path in self.paths.items():
            try:
                text, endings, bad = self._run(path)
            except (OSError, UnicodeDecodeError, PatchError) as e:
                problems.append(f"{shown(path, base)}: {e}")
                continue
            problems += [f"{shown(path, base)}: {b}" for b in bad]
            done[k] = (text, endings)
        if problems:
            raise PatchError("Nothing written.\n  " + "\n  ".join(problems))
        report = []
        for k, (text, endings) in done.items():
            if not dry:
                out = text.replace("\n", "\r\n") if endings == "CRLF" else text
                open(self.paths[k], "wb").write(out.encode("utf-8"))
            report.append(f"{shown(self.paths[k], base)}: {len(self.edits[k])} edit(s), {endings} kept")
        return "\n".join(report) + ("\n(dry run: nothing written)" if dry else "")


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        sys.exit(__doc__)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")   # the Windows console is cp1252
    p = Patch()
    for path, pairs in json.load(open(args[0], encoding="utf-8")).items():
        for old, new in pairs:
            p.edit(path, old, new)
    print(p.apply(dry="--dry-run" in args))


if __name__ == "__main__":
    main()
