#!/usr/bin/env python3
"""Validate the marketplace before pushing.

Checks that:
  - every plugin listed in marketplace.json exists and has a plugin.json
  - name, version and description match between the two files
  - every skill has a SKILL.md with frontmatter whose name matches its folder
Run from the repo root: python scripts/validate.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []


def frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
for entry in market.get("plugins", []):
    name = entry.get("name")
    plugin_dir = (ROOT / entry.get("source", "")).resolve()
    manifest = plugin_dir / ".claude-plugin/plugin.json"
    if not manifest.exists():
        errors.append(f"[{name}] missing {manifest.relative_to(ROOT)}")
        continue
    plugin = json.loads(manifest.read_text())
    for field in ("name", "version", "description"):
        if entry.get(field) != plugin.get(field):
            errors.append(f"[{name}] '{field}' differs between marketplace.json and plugin.json")

    skills_dir = plugin_dir / "skills"
    skills = sorted(p for p in skills_dir.iterdir() if p.is_dir()) if skills_dir.exists() else []
    for skill in skills:
        skill_md = skill / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"[{name}] {skill.name}/ has no SKILL.md")
            continue
        fm = frontmatter(skill_md.read_text())
        if fm.get("name") != skill.name:
            errors.append(f"[{name}] {skill.name}/SKILL.md name '{fm.get('name')}' must match folder name")
        if not fm.get("description"):
            errors.append(f"[{name}] {skill.name}/SKILL.md is missing a description")

if errors:
    print("Validation failed:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print(f"OK: {len(market.get('plugins', []))} plugin(s) validated.")
