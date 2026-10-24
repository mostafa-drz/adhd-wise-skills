#!/usr/bin/env python3
"""Fail on skills that would mis-load, break the house rules, or make health claims.

Claude Code fails soft on bad frontmatter: the skill still answers to its name while
automatic matching silently stops. This check is where those problems surface.
"""
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^(?!-)(?!.*--)[a-z0-9-]{1,64}(?<!-)$")
# Treatment language turns a productivity tool into a health claim (FTC, FDA, EU MDR).
CLAIMS_RE = re.compile(
    r"\b(treats?|treatment|cures?|reduces? symptoms|clinically proven|therapy|diagnos\w*)\b",
    re.IGNORECASE,
)


def frontmatter(md: Path):
    raw = md.read_text()
    if not raw.startswith("---\n"):
        raise ValueError("frontmatter must start on line 1")
    parsed = yaml.safe_load(raw.split("---\n", 2)[1])
    if not isinstance(parsed, dict):
        raise ValueError("frontmatter is not a YAML mapping")
    return parsed


def check_plugin(plugin: Path, problems: list) -> None:
    rel = plugin.relative_to(ROOT)
    if (plugin / "bin").exists():
        problems.append(f"{rel}: has a top-level bin/, which claude.ai and Cowork refuse")
    manifest = json.loads((plugin / ".claude-plugin" / "plugin.json").read_text())
    if "claude" in manifest.get("name", "").lower():
        problems.append(f"{rel}: plugin name contains 'claude'")
    if not manifest.get("version"):
        problems.append(f"{rel}: plugin.json has no version, so buyers never get updates")
    if CLAIMS_RE.search(manifest.get("description", "")):
        problems.append(f"{rel}: plugin description uses treatment language")

    for md in sorted(plugin.glob("skills/*/SKILL.md")):
        srel, folder = md.relative_to(ROOT), md.parent.name
        try:
            fm = frontmatter(md)
        except (ValueError, yaml.YAMLError) as exc:
            problems.append(f"{srel}: {str(exc).splitlines()[0]}")
            continue
        name = str(fm.get("name") or "").strip()
        desc = str(fm.get("description") or "").strip()
        if name != folder:
            problems.append(f"{srel}: name '{name}' != folder '{folder}'")
        if not NAME_RE.match(folder) or "claude" in folder:
            problems.append(f"{srel}: folder name breaks the naming rules")
        if not desc:
            problems.append(f"{srel}: no description, so Claude cannot match this skill")
        elif len(desc) > 1024:
            problems.append(f"{srel}: description is {len(desc)} chars, the cap is 1024")
        if CLAIMS_RE.search(desc):
            problems.append(f"{srel}: description uses treatment language")
        if "side_effects" not in (fm.get("metadata") or {}):
            problems.append(f"{srel}: metadata.side_effects is missing")
        evals = md.parent / "evals" / "evals.json"
        if not evals.exists():
            problems.append(f"{srel}: no evals/evals.json")
        elif len(json.loads(evals.read_text())) < 2:
            problems.append(f"{srel}: evals.json needs at least two cases")


def main() -> int:
    problems: list = []
    plugins = sorted(p.parent.parent for p in ROOT.glob("plugins/*/.claude-plugin/plugin.json"))
    if not plugins:
        problems.append("no plugins found under plugins/")
    for plugin in plugins:
        check_plugin(plugin, problems)
    readme = ROOT / "README.md"
    if readme.exists():
        for line in readme.read_text().splitlines():
            if CLAIMS_RE.search(line) and "not medical advice" not in line.lower():
                problems.append(f"README.md: treatment language: {line.strip()[:80]}")
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print(f"skills OK across {len(plugins)} plugin(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
