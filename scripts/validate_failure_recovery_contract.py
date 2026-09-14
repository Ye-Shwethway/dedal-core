#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "evals" / "failure-recovery" / "contract-v1.json"


def case_valid(case):
    decision = case.get("decision")
    if decision not in {"retry", "compensate", "preserve_partial", "escalate"}:
        return False

    failed = case.get("failed_step")
    if decision == "retry":
        if not failed or failed.get("status") != "failed":
            return False
        return bool(failed.get("idempotent") or failed.get("safe_retry"))

    steps = case.get("steps", [])
    if decision == "compensate":
        if case.get("claims_full_rollback"):
            if any(s.get("status") == "succeeded" and not s.get("reversible", False) for s in steps):
                return False
        succeeded_reversible = [s["id"] for s in steps if s.get("status") == "succeeded" and s.get("reversible", False)]
        order = case.get("compensation_order")
        if order is not None and order != list(reversed(succeeded_reversible)):
            return False
        if any(s.get("compensation_status") == "failed" for s in steps):
            return case.get("final_state") == "manual_required"
        return True

    if decision == "preserve_partial":
        return (
            case.get("final_state") == "partial"
            and bool(case.get("residual_effects"))
            and bool(case.get("blocked_actions"))
        )

    if decision == "escalate":
        return (
            case.get("final_state") == "manual_required"
            and bool(case.get("residual_effects"))
            and bool(case.get("blocked_actions"))
        )

    return False


def main():
    data = json.loads(CONTRACT.read_text())
    cases = data.get("cases", [])
    assert cases, "failure-recovery contract must contain cases"
    seen = set()
    for case in cases:
        cid = case.get("id")
        assert cid and cid not in seen, f"invalid/duplicate case id: {cid}"
        seen.add(cid)
        actual = case_valid(case)
        expected = case.get("expect") == "accept"
        assert actual == expected, f"{cid}: expected {case.get('expect')}, got {'accept' if actual else 'reject'}"
    print(f"failure-recovery contract OK: {len(cases)} cases")


if __name__ == "__main__":
    main()
