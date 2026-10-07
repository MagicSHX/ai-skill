#!/usr/bin/env python3
"""Check a commit message against the basic Conventional Commits rules.

Usage: python check_commit.py "feat(auth): add rate limiting"
Exits 0 if valid, 1 with a list of problems otherwise.
"""
import re
import sys

TYPES = {"feat", "fix", "docs", "refactor", "test", "chore", "perf",
         "style", "build", "ci", "revert"}
HEADER = re.compile(r"^(?P<type>[a-z]+)(\((?P<scope>[^)]+)\))?(?P<bang>!)?: (?P<summary>.+)$")


def check(message: str) -> list[str]:
    problems = []
    lines = message.strip().splitlines()
    if not lines:
        return ["Message is empty."]
    header = lines[0]
    m = HEADER.match(header)
    if not m:
        return ["Header must look like 'type(scope): summary'."]
    if m["type"] not in TYPES:
        problems.append(f"Unknown type '{m['type']}'. Use one of: {', '.join(sorted(TYPES))}.")
    if len(header) > 72:
        problems.append(f"Header is {len(header)} characters; keep it to 72 or fewer.")
    if m["summary"].endswith("."):
        problems.append("Remove the trailing period from the summary.")
    if m["summary"][0].isupper():
        problems.append("Start the summary with a lowercase letter.")
    if len(lines) > 1 and lines[1].strip():
        problems.append("Leave a blank line between the header and the body.")
    return problems


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    issues = check(sys.argv[1])
    if issues:
        print("Problems found:")
        for issue in issues:
            print(f"  - {issue}")
        sys.exit(1)
    print("Looks good.")
