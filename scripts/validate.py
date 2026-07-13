#!/usr/bin/env python3
"""Validate the career-copilot skill suite.

Checks (no external dependencies):
  1. Every skills/<dir>/ has a SKILL.md with YAML frontmatter.
  2. Frontmatter `name` matches the folder name, is kebab-case, <= 64 chars.
  3. Frontmatter `description` exists, is non-empty, <= 1024 chars.
  4. Every `references/....md` path mentioned in a skill file resolves
     (including cross-skill `../<skill>/references/....md` mentions).
  5. Every file in a skill's references/ dir is mentioned by its SKILL.md.
  6. .claude-plugin/plugin.json and marketplace.json parse and carry
     the required fields.
  7. Every skill folder is listed in the README.

Exit code 0 = clean, 1 = failures (warnings alone don't fail the build).
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

failures: list[str] = []
warnings: list[str] = []

REF_RE = re.compile(r"(?:\.\./)*(?:[a-z0-9\-]+/)*references/[A-Za-z0-9_\-.]+\.md")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm: dict[str, str] = {}
    key = None
    for line in text[3:end].strip().splitlines():
        if re.match(r"^[A-Za-z_-]+:", line):
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
        elif key:  # folded continuation line
            fm[key] += " " + line.strip()
    return fm


def check_skill(skill_dir: Path) -> None:
    name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        failures.append(f"{name}: missing SKILL.md")
        return

    text = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    if fm is None:
        failures.append(f"{name}: SKILL.md has no YAML frontmatter")
        return

    fm_name = fm.get("name", "")
    if not fm_name:
        failures.append(f"{name}: frontmatter has no `name`")
    elif fm_name != name:
        failures.append(f"{name}: frontmatter name `{fm_name}` != folder name")
    elif not NAME_RE.match(fm_name) or len(fm_name) > 64:
        failures.append(f"{name}: `{fm_name}` is not kebab-case or exceeds 64 chars")

    desc = fm.get("description", "")
    if not desc:
        failures.append(f"{name}: frontmatter has no `description`")
    elif len(desc) > 1024:
        failures.append(f"{name}: description is {len(desc)} chars (max 1024)")

    # Referenced paths resolve — from SKILL.md and from the reference files.
    mentioned: set[str] = set()
    for md in [skill_md, *sorted((skill_dir / "references").glob("*.md"))]:
        for ref in REF_RE.findall(md.read_text(encoding="utf-8")):
            target = (md.parent / ref).resolve()
            if not target.is_file():
                failures.append(f"{name}: {md.name} references missing file `{ref}`")
            if md == skill_md:
                mentioned.add(target.name)

    # Orphaned reference files (present but never mentioned by SKILL.md).
    refs_dir = skill_dir / "references"
    if refs_dir.is_dir():
        for ref_file in sorted(refs_dir.glob("*.md")):
            if ref_file.name not in mentioned:
                warnings.append(f"{name}: references/{ref_file.name} never mentioned in SKILL.md")


def check_plugin_manifests() -> None:
    plugin = ROOT / ".claude-plugin" / "plugin.json"
    marketplace = ROOT / ".claude-plugin" / "marketplace.json"
    for path, required in [(plugin, ["name"]), (marketplace, ["name", "owner", "plugins"])]:
        if not path.is_file():
            failures.append(f"missing {path.relative_to(ROOT)}")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            failures.append(f"{path.relative_to(ROOT)}: invalid JSON ({e})")
            continue
        for field in required:
            if field not in data:
                failures.append(f"{path.relative_to(ROOT)}: missing `{field}`")


def check_readme() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for skill_dir in sorted(SKILLS.iterdir()):
        if skill_dir.is_dir() and f"`{skill_dir.name}`" not in readme:
            warnings.append(f"README does not mention `{skill_dir.name}`")


def main() -> int:
    if not SKILLS.is_dir():
        print("FAIL: no skills/ directory")
        return 1
    for skill_dir in sorted(SKILLS.iterdir()):
        if skill_dir.is_dir():
            check_skill(skill_dir)
    check_plugin_manifests()
    check_readme()

    for w in warnings:
        print(f"WARN: {w}")
    for f in failures:
        print(f"FAIL: {f}")
    total = len([d for d in SKILLS.iterdir() if d.is_dir()])
    print(f"\n{total} skills checked — {len(failures)} failure(s), {len(warnings)} warning(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
