#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def valid_record(policy: dict, rec: dict) -> bool:
    durability = rec.get("durability")
    if durability not in policy["durability_values"]:
        return False
    decision = rec.get("decision")
    if decision not in policy["decisions"]:
        return False
    if durability == "transient":
        return decision == "transient_close" and bool(str(rec.get("no_promotion_reason", "")).strip())
    if any(k not in rec for k in policy["durable_required_fields"]):
        return False
    if decision != "retain":
        return True
    repair = rec.get("repair") or {}
    if policy.get("require_runtime_repair_verification") and not (repair.get("status") == "fixed" and repair.get("verified") is True):
        return False
    sync = rec.get("canonical_sync") or {}
    if policy.get("require_canonical_sync_for_durable_retain") and sync.get("status") not in {"synced", "not_applicable"}:
        return False
    guard = rec.get("regression_guard") or {}
    if policy.get("require_regression_guard_or_not_testable_reason"):
        if guard.get("status") not in {"added", "existing", "not_testable"}:
            return False
        if guard.get("status") == "not_testable" and not str(guard.get("reason", "")).strip():
            return False
    learning = rec.get("learning") or {}
    if policy.get("require_durable_learning_sink") and learning.get("status") != "captured":
        return False
    verification = rec.get("verification") or {}
    if policy.get("require_independent_verification") and verification.get("independent") is not True:
        return False
    if policy.get("require_empty_debt_for_durable_retain") and rec.get("unresolved_debt") != []:
        return False
    return True

def main() -> int:
    data=json.loads((ROOT/"evals"/"self-improvement"/"closure-contract-v2.json").read_text(encoding="utf-8"))
    policy=data["policy"]
    cases=data.get("cases",[])
    ids=[c.get("id") for c in cases]
    if not cases or len(ids)!=len(set(ids)):
        raise AssertionError("self-improvement closure contract requires unique cases")
    for case in cases:
        actual=valid_record(policy,case.get("record",{}))
        expected=bool(case.get("accept"))
        if actual!=expected:
            raise AssertionError(f"{case.get('id')}: expected accept={expected} got {actual}")
    print(f"self-improvement closure contract: valid ({len(cases)} cases)")
    return 0
if __name__=="__main__":
    raise SystemExit(main())
