#!/usr/bin/env python3
"""Check file roles, formats, and active skill metadata against the Core inventory."""
import json
from pathlib import Path
import re
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []
schema = yaml.safe_load((ROOT / "index/document-schema.yaml").read_text())
inventory = json.loads((ROOT / "core-files.json").read_text())["files"]
registry = yaml.safe_load((ROOT / "index/SKILL_REGISTRY.yaml").read_text())["skills"]


def matches(pattern, path):
    expression = re.escape(pattern).replace(r"\*\*", "\0").replace(r"\*", "[^/]*").replace("\0", ".*")
    return re.fullmatch(expression, path) is not None


def check(paths=inventory):
    found = []
    roles = schema["roles"]
    rules = schema["rules"]
    if schema.get("default") != "reject" or schema.get("classification") != "first_matching_rule":
        found.append("schema must reject unclassified files")
    for path in paths:
        selected = next((rule for rule in rules if matches(rule["pattern"], path)), None)
        if selected is None:
            found.append(f"unclassified:{path}")
            continue
        role = selected["role"]
        if role not in roles:
            found.append(f"unknown_role:{path}:{role}")
            continue
        suffix = Path(path).suffix or "none"
        if suffix not in roles[role]["formats"]:
            found.append(f"format_mismatch:{path}:{role}:{suffix}")
        if role == "instruction_entrypoint" and not re.fullmatch(r"skills/[^/]+/SKILL\.md", path):
            found.append(f"nested_instruction_entrypoint:{path}")
    registered = {v["entrypoint"]: (k, v) for k, v in registry.items() if v.get("status") == "active"}
    classified = {p for p in paths if re.fullmatch(r"skills/[^/]+/SKILL\.md", p)}
    if registered.keys() != classified:
        found.append(f"skill_registry_mismatch:missing={sorted(registered.keys()-classified)} extra={sorted(classified-registered.keys())}")
    for path, (key, cfg) in registered.items():
        file = ROOT / path
        if not file.is_file():
            found.append(f"missing_skill:{path}")
            continue
        content = file.read_text()
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
        if not match:
            found.append(f"frontmatter_missing:{path}")
            continue
        try:
            metadata = yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            found.append(f"frontmatter_invalid:{path}")
            continue
        expected_name = cfg.get("frontmatter_name", key)
        if not isinstance(metadata, dict) or metadata.get("name") != expected_name or not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
            found.append(f"frontmatter_metadata:{path}")
        if not content[match.end():].strip():
            found.append(f"skill_body_empty:{path}")
    return found


if __name__ == "__main__":
    errors = check()
    if errors:
        print("DOCUMENT SCHEMA: FAIL", *errors, sep="\n- ")
        sys.exit(1)
    print(f"DOCUMENT SCHEMA: PASS files={len(inventory)} active_skills={len([s for s in registry.values() if s.get('status') == 'active'])}")
