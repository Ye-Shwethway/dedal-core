#!/usr/bin/env python3
"""Regression cases for conservative task-profile phrase routing."""
import json
from pathlib import Path
import sys

import yaml
from profile_probe import probe
from route_task import route

ROOT = Path(__file__).resolve().parents[1]
profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
cases = json.loads((ROOT / "evals/profile-routing/cases-v1.json").read_text())
errors = []
for case in cases["cases"]:
    result = probe(case["task"], profiles)
    if result["status"] != case["status"] or result["profiles"] != case["profiles"]:
        errors.append(f"{case['id']}: {result}")
    resolved = route(case["task"], profiles)
    if case["status"] == "matched":
        profile = next(p for p in profiles if p["id"] == case["profiles"][0])
        if (resolved["primary"] != profile["primary"] or resolved["supporting"] != profile.get("supporting", [])
                or resolved["next"] != "hydrate_and_verify"):
            errors.append(f"{case['id']}: composition {resolved}")
    elif resolved["primary"] is not None or resolved["next"] == "hydrate_and_verify":
        errors.append(f"{case['id']}: forced match {resolved}")
for case in cases["transitions"]:
    before, after = probe(case["from"], profiles), probe(case["to"], profiles)
    if before["profiles"] != case["from_profiles"] or after["profiles"] != case["to_profiles"]:
        errors.append(f"transition: {before} -> {after}")
if errors:
    print("PROFILE PROBE: FAIL", *errors, sep="\n- ")
    sys.exit(1)
print(f"PROFILE PROBE: PASS cases={len(cases['cases'])} transitions={len(cases['transitions'])}")
