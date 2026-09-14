#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def case_is_valid(policy: dict, items: list[dict], operations: list[dict]) -> bool:
    allowed_ops = set(policy["operators"])
    protected = set(policy["protected_classes"])
    volatile = set(policy["volatile_classes"])
    item_map = {item.get("id"): dict(item) for item in items}
    if not item_map or None in item_map or len(item_map) != len(items):
        return False

    for operation in operations:
        op = operation.get("op")
        item_id = operation.get("item")
        if op not in allowed_ops or item_id not in item_map:
            return False
        item = item_map[item_id]
        klass = item.get("class")

        if op == "refresh":
            if klass not in volatile:
                return False
            item["fresh"] = True
        elif op == "select":
            if operation.get("mode") not in {"full", "summary", "reference"}:
                return False
            if klass in volatile and not item.get("fresh"):
                return False
        elif op == "compress":
            if klass in protected and (
                not operation.get("preserves_anchor") or not operation.get("source_ref")
            ):
                return False
        elif op == "drop":
            if klass in protected:
                return False
        elif op == "isolate":
            if not operation.get("purpose"):
                return False
            if operation.get("return_mode") != "compact_evidence_with_refs":
                return False
        elif op == "write":
            if not operation.get("scope") or not operation.get("source_ref"):
                return False

    return True


def main() -> int:
    data = json.loads(
        (ROOT / "evals" / "context-engineering" / "contract-v1.json").read_text(encoding="utf-8")
    )
    policy = data.get("policy", {})
    required = {"operators", "protected_classes", "volatile_classes", "ephemeral_classes"}
    if not required.issubset(policy):
        raise AssertionError("context-engineering policy missing required keys")

    cases = data.get("cases", [])
    ids = [case.get("id") for case in cases]
    if not cases or len(ids) != len(set(ids)):
        raise AssertionError("context-engineering contract requires non-empty unique case ids")

    for case in cases:
        actual = case_is_valid(policy, case.get("items", []), case.get("operations", []))
        expected = bool(case.get("accept"))
        if actual != expected:
            raise AssertionError(f"{case.get('id')}: expected accept={expected} got {actual}")

    print("context-engineering contract: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
