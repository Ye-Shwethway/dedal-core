#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def allowed(policy: dict, grant: dict, action: dict) -> bool:
    trusted = set(policy["authority_sources"])
    modes = set(policy["capability_modes"])
    high_impact = set(policy["high_impact_modes"])

    if grant.get("authority_source") not in trusted:
        return False
    if grant.get("mode") not in modes or action.get("mode") not in modes:
        return False
    for key in ("tool", "mode", "resource", "intent"):
        if grant.get(key) != action.get(key):
            return False
    if action.get("mode") in high_impact and policy.get("require_confirmation_for_high_impact"):
        if action.get("confirmed") is not True:
            return False
    if grant.get("external_mcp") or action.get("external_mcp"):
        if not (grant.get("external_mcp") and action.get("external_mcp")):
            return False
        if policy.get("require_schema_pin_for_external_mcp"):
            pin = grant.get("schema_pin")
            if not pin or action.get("schema_pin") != pin:
                return False
    return True


def main() -> int:
    data = json.loads((ROOT / "evals" / "tool-authority" / "contract-v1.json").read_text(encoding="utf-8"))
    policy = data["policy"]
    cases = data["cases"]
    ids = [case.get("id") for case in cases]
    if not cases or len(ids) != len(set(ids)):
        raise AssertionError("tool-authority contract requires non-empty unique case ids")
    for case in cases:
        actual = allowed(policy, case["grant"], case["action"])
        expected = bool(case["accept"])
        if actual != expected:
            raise AssertionError(f"{case['id']}: expected accept={expected} got {actual}")
    print("tool authority contract: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
