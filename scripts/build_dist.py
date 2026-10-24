#!/usr/bin/env python3
"""Build the files buyers install, one set per plugin, into dist/.

  <plugin>-<version>.zip               Claude Desktop / claude.ai / Cowork: Upload plugin
  <plugin>-<version>-agents-skills.zip Codex, Cursor, Copilot, Gemini: unzip into ~/.agents/skills/
  skills/<skill>.zip                   claude.ai: upload a single skill (folder at the zip root)
"""
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
# Evals are for us, not for buyers.
SKIP = {".DS_Store", "__pycache__", "evals"}


def add_tree(zf: zipfile.ZipFile, src: Path, prefix: str) -> None:
    for path in sorted(src.rglob("*")):
        if path.is_file() and not SKIP.intersection(path.relative_to(src).parts):
            zf.write(path, f"{prefix}{path.relative_to(src).as_posix()}")


def main() -> int:
    shutil.rmtree(DIST, ignore_errors=True)
    (DIST / "skills").mkdir(parents=True)
    for manifest in sorted(ROOT.glob("plugins/*/.claude-plugin/plugin.json")):
        plugin = manifest.parent.parent
        meta = json.loads(manifest.read_text())
        stem = f"{meta['name']}-{meta['version']}"
        skills = [s for s in sorted((plugin / "skills").iterdir()) if (s / "SKILL.md").exists()]

        with zipfile.ZipFile(DIST / f"{stem}.zip", "w", zipfile.ZIP_DEFLATED) as zf:
            add_tree(zf, plugin / ".claude-plugin", ".claude-plugin/")
            for skill in skills:
                add_tree(zf, skill, f"skills/{skill.name}/")
        with zipfile.ZipFile(DIST / f"{stem}-agents-skills.zip", "w", zipfile.ZIP_DEFLATED) as zf:
            for skill in skills:
                add_tree(zf, skill, f"{skill.name}/")
        for skill in skills:
            with zipfile.ZipFile(DIST / "skills" / f"{skill.name}.zip", "w", zipfile.ZIP_DEFLATED) as zf:
                add_tree(zf, skill, f"{skill.name}/")
        print(f"built {stem}: {len(skills)} skill(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
