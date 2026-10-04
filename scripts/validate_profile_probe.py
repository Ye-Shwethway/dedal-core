#!/usr/bin/env python3
"""Regression cases for conservative task-profile phrase routing."""
import json
from pathlib import Path
import sys

import yaml
from profile_probe import probe

ROOT = Path(__file__).resolve().parents[1]
profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
cases = json.loads((ROOT / "evals/profile-routing/cases-v1.json").read_text())
errors = []
for case in cases["cases"]:
    result = probe(case["task"], profiles)
    if result["status"] != case["status"] or result["profiles"] != case["profiles"]:
        errors.append(f"{case['id']}: {result}")
for case in cases["transitions"]:
    before, after = probe(case["from"], profiles), probe(case["to"], profiles)
    if before["profiles"] != case["from_profiles"] or after["profiles"] != case["to_profiles"]:
        errors.append(f"transition: {before} -> {after}")
if errors:
    print("PROFILE PROBE: FAIL", *errors, sep="\n- ")
    sys.exit(1)
print(f"PROFILE PROBE: PASS cases={len(cases['cases'])} transitions={len(cases['transitions'])}")
