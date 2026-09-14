#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "evals" / "delegation-authority" / "contract-v1.json"


def _subset(child: list[str], parent: list[str]) -> bool:
    return set(child).issubset(set(parent))


def case_valid(case: dict) -> bool:
    parent = case.get("parent", {})
    child = case.get("child", {})
    returned = case.get("return", {})

    if not _subset(child.get("tools", []), parent.get("tools", [])):
        return False
    if not _subset(child.get("modes", []), parent.get("modes", [])):
        return False
    if not _subset(child.get("resources", []), parent.get("resources", [])):
        return False
    if not _subset(child.get("intents", []), parent.get("intents", [])):
        return False
    if child.get("can_redelegate", False) and not parent.get("can_redelegate", False):
        return False
    if not returned.get("provenance", False):
        return False
    return True


def main() -> int:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    ids = [case.get("id") for case in cases]
    if not cases or len(ids) != len(set(ids)):
        raise AssertionError("delegation authority contract requires non-empty unique case ids")

    for case in cases:
        actual = case_valid(case)
        expected = bool(case.get("accept"))
        if actual != expected:
            raise AssertionError(f"{case.get('id')}: expected accept={expected} got {actual}")

    print("delegation authority contract: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
