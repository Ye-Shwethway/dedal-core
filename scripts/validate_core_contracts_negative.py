#!/usr/bin/env python3
"""Mutation probes for contract validation; valid baseline must stay green."""
from copy import deepcopy
import json
from pathlib import Path

import yaml

from validate_core_contracts import ROOT, validate

load = lambda path: yaml.safe_load((ROOT / path).read_text())
base = [load("index/task-profiles.yaml"), load("index/routing.yaml"),
        load("index/SKILL_REGISTRY.yaml"), load("index/document-schema.yaml"),
        set(json.loads((ROOT / "core-files.json").read_text())["files"])]
assert validate(*base) == []


def rejected(mutate, expected):
    copy = deepcopy(base)
    mutate(copy)
    errors = validate(*copy)
    assert any(e.startswith(expected) for e in errors), errors


rejected(lambda x: x[0]["profiles"][0].update(primary=["generative-video-direction", "visual-narrative-production"]), "invalid_skill_composition")
rejected(lambda x: x[0]["profiles"][2]["supporting"].append("nonexistent"), "invalid_skill_composition")
rejected(lambda x: x[0]["profiles"][2]["required_core"].remove("skills/self-improvement/SKILL.md"), "missing_skill_entrypoint_dependency")
rejected(lambda x: x[0]["profiles"][2]["required_core"].append("../private"), "invalid_required_core")
rejected(lambda x: x[1]["steps"][3].update(max_primary=2), "routing_selection_policy")
rejected(lambda x: x[3]["rules"].append(dict(x[3]["rules"][0])), "invalid_or_duplicate_document_rule")
print("CORE CONTRACT NEGATIVES: PASS six invalid states rejected")
