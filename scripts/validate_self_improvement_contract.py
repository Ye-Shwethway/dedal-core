#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def valid_experiment(policy: dict, exp: dict) -> bool:
    if not exp or any(field not in exp for field in policy["required_fields"]):
        return False
    if exp.get("decision") not in policy["decisions"]:
        return False
    baseline = exp.get("baseline")
    candidate = exp.get("candidate")
    eval_set = exp.get("eval_set")
    if policy.get("require_comparable_baseline") and not isinstance(baseline, dict):
        return False
    if not isinstance(candidate, dict) or not candidate.get("revision"):
        return False
    if not isinstance(eval_set, dict):
        return False
    held_in = eval_set.get("held_in", [])
    held_out = eval_set.get("held_out", [])
    if not held_in or not held_out:
        return False
    if policy.get("protected_eval") and eval_set.get("modified_by_candidate") is not False:
        return False
    if policy.get("forbid_task_specific_benchmaxxing"):
        scope = candidate.get("change_scope", [])
        if any(str(item).startswith("task:") for item in scope):
            return False
    regressions = exp.get("regressions", [])
    if policy.get("require_regression_check") and not isinstance(regressions, list):
        return False
    if exp["decision"] == "retain" and regressions:
        return False
    return True


def main() -> int:
    data = json.loads((ROOT / "evals" / "self-improvement" / "contract-v1.json").read_text(encoding="utf-8"))
    policy = data["policy"]
    cases = data.get("cases", [])
    ids = [case.get("id") for case in cases]
    if not cases or len(ids) != len(set(ids)):
        raise AssertionError("self-improvement contract requires unique cases")
    for case in cases:
        actual = valid_experiment(policy, case.get("experiment", {}))
        expected = bool(case.get("accept"))
        if actual != expected:
            raise AssertionError(f"{case.get('id')}: expected accept={expected} got {actual}")
    print("self-improvement contract: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
