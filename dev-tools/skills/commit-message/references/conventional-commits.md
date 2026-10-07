# Conventional Commits: edge cases

Read this only when the main SKILL.md doesn't cover the situation.

## Breaking changes

Add `!` after the type/scope AND a `BREAKING CHANGE:` footer:

```
feat(api)!: remove v1 endpoints

BREAKING CHANGE: /v1/* routes are gone. Migrate to /v2.
```

## Reverts

```
revert: feat(auth): add rate limiting to login endpoint

This reverts commit a1b2c3d.
```

## Changes touching several areas

Omit the scope rather than listing several: `refactor: rename config loader`.
If the areas are truly unrelated, recommend separate commits instead.

## Full spec

https://www.conventionalcommits.org/en/v1.0.0/
