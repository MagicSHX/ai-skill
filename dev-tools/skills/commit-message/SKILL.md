---
name: commit-message
description: Write clear git commit messages in the Conventional Commits format. Use this skill whenever the user asks for a commit message, wants to describe staged changes, asks "what should I commit this as", pastes a git diff and wants it summarized, or is about to run git commit, even if they don't mention Conventional Commits by name.
---

# Commit Message Writer

Write commit messages that follow the Conventional Commits format so the
history stays readable and tools can generate changelogs from it.

## Workflow

1. Look at what changed. If you can run commands, use `git diff --staged`
   (or `git diff` if nothing is staged). Otherwise, use the diff or
   description the user gave you.
2. Pick the single best type from the table below. If the changes span
   several unrelated types, suggest splitting them into separate commits.
3. Write the message using the format below.
4. Check it with `python scripts/check_commit.py "<message>"` when you can
   run scripts, and fix anything it reports.

## Format

```
<type>(<optional scope>): <summary>

<optional body: what changed and why, wrapped at 72 characters>

<optional footer: BREAKING CHANGE: ..., Closes #123>
```

Rules for the summary line:
- Imperative mood ("add", not "added" or "adds")
- No more than 72 characters, no trailing period
- Lowercase after the colon

## Types

| Type | Use for |
|------|---------|
| feat | A new feature for the user |
| fix | A bug fix |
| docs | Documentation only |
| refactor | Code change that neither fixes a bug nor adds a feature |
| test | Adding or fixing tests |
| chore | Build process, tooling, dependencies |
| perf | Performance improvements |

For edge cases (breaking changes, reverts, multi-scope commits), read
`references/conventional-commits.md`.

## Example

Input: a diff that adds rate limiting to the login endpoint.

Output:
```
feat(auth): add rate limiting to login endpoint

Limit failed login attempts to 5 per minute per IP to slow down
credential-stuffing attacks.

Closes #42
```
