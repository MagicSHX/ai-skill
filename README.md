# my-skills

A shared collection of Claude skills, packaged as Claude Code plugins.

## Install (Claude Code)

```
/plugin marketplace add YOUR-GITHUB-USERNAME/my-skills
/plugin install dev-tools@my-skills
```

To get updates later, run `/plugin marketplace update my-skills`.

## Install (Claude.ai)

Zip a single skill folder (for example `dev-tools/skills/commit-message`)
and upload it in **Settings → Capabilities → Skills**.

## Available plugins

| Plugin | Skills | Description |
|--------|--------|-------------|
| dev-tools | commit-message | Write Conventional Commits messages |

## Repo layout

```
.claude-plugin/marketplace.json   # catalog of every plugin in this repo
dev-tools/                        # one plugin
  .claude-plugin/plugin.json      # plugin name, version, description
  skills/commit-message/
    SKILL.md                      # instructions Claude reads
    references/                   # extra docs, loaded only when needed
    scripts/                      # helper scripts the skill can run
scripts/validate.py               # checks the repo is consistent
.github/workflows/validate.yml    # runs validate.py on every PR
```

## Contributing

1. Add a skill folder under an existing plugin's `skills/`, or create a new
   plugin folder and register it in `.claude-plugin/marketplace.json`.
2. Make sure the `name` in `SKILL.md` matches the folder name.
3. When you change a plugin, bump `version` in both `plugin.json` and
   `marketplace.json`.
4. Test locally: `claude --plugin-dir ./dev-tools`
5. Run `python scripts/validate.py` before opening a PR.

## License

MIT
