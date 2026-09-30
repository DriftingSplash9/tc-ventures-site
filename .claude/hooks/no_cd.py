"""PreToolUse hook: refuse a Bash command that starts with `cd` (INFRA-14a).

The Bash tool resets its working directory after a `cd`, and a leading `cd`
has been the most repeated harmless miss in this repo's handoffs. Ruled
"A: yes, for this repo only" in handoff-025-decisions.xlsx (2026-09-29).

Reads the hook's JSON on stdin. Exit 2 blocks the call and shows stderr to
the agent; exit 0 lets it through. `cd` inside a command (after && or ;) is
allowed: only the first word is checked.
"""
import json
import re
import sys

try:
    data = json.load(sys.stdin)
except ValueError:
    sys.exit(0)

command = (data.get("tool_input") or {}).get("command") or ""
if re.match(r"\s*cd(\s|;|&|$)", command):
    sys.stderr.write(
        "Refused by .claude/hooks/no_cd.py (INFRA-14a): don't start a Bash "
        "command with cd. Use absolute paths, or git -C / a script's own "
        "path argument.\n"
    )
    sys.exit(2)
sys.exit(0)
