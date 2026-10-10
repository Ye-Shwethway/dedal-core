#!/usr/bin/env python3
"""Derive intent metadata from active skill sources; provenance stays in the registry."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def build(root=ROOT):
    root = Path(root)
    registry = yaml.safe_load((root / "index/SKILL_REGISTRY.yaml").read_text())["skills"]
    skills = {}
    for name, entry in registry.items():
        if entry.get("status") != "active":
            continue
        body = (root / entry["entrypoint"]).read_text()
        if not body.startswith("---\n"):
            raise ValueError("skill frontmatter missing: " + name)
        front = yaml.safe_load(body.split("---", 2)[1])
        description = front.get("description")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("skill trigger missing: " + name)
        skills[name] = {"use_when": description, "aliases": entry.get("aliases", []),
                        "entrypoint": entry["entrypoint"], "status": "registered"}
    return {"schema_version": 1, "availability": "resolve_current_tools_and_dependencies_per_task",
            "activation": "metadata_is_not_content_read_or_execution_readiness", "skills": skills}


if __name__ == "__main__":
    target = ROOT / "index/skill-catalog.yaml"
    target.write_text(yaml.safe_dump(build(), sort_keys=False, allow_unicode=True, width=110))
    print("skill catalog generated")
