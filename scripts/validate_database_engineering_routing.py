#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "evals" / "database-engineering-routing" / "contract-v1.json"


def main() -> int:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    if not cases:
        raise AssertionError("database engineering routing contract requires cases")
    ids = [case.get("id") for case in cases]
    if len(ids) != len(set(ids)):
        raise AssertionError("database engineering routing contract has duplicate ids")

    allowed_primary = {
        "database-engineering",
        "software-development",
        "data-operations",
        "cloudflare-platform",
        "release-engineering",
        "quality-engineering",
    }
    for case in cases:
        if case.get("primary") not in allowed_primary:
            raise AssertionError(f"{case.get('id')}: invalid primary owner")
        supporting = case.get("supporting", [])
        if len(supporting) != len(set(supporting)):
            raise AssertionError(f"{case.get('id')}: duplicate supporting owners")
        if case.get("primary") in supporting:
            raise AssertionError(f"{case.get('id')}: primary repeated as supporting")

    expected = {
        "DB-01": ("software-development", True),
        "DB-02": ("database-engineering", True),
        "DB-03": ("data-operations", True),
        "DB-04": ("cloudflare-platform", True),
        "DB-05": ("release-engineering", True),
        "DB-06": ("quality-engineering", True),
        "DB-07": ("database-engineering", False),
        "DB-08": ("database-engineering", False),
        "DB-09": ("database-engineering", False),
        "DB-10": ("database-engineering", False),
    }
    by_id = {case["id"]: case for case in cases}
    if set(by_id) != set(expected):
        raise AssertionError("database engineering routing contract case coverage mismatch")
    for cid, (primary, accept) in expected.items():
        case = by_id[cid]
        if case["primary"] != primary or bool(case["accept"]) != accept:
            raise AssertionError(f"{cid}: routing expectation mismatch")

    print("database engineering routing: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
