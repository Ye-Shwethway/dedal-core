#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "evals" / "reliability-engineering-routing" / "contract-v1.json"


def main() -> int:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    if not cases:
        raise AssertionError("reliability routing contract requires cases")

    ids = [case.get("id") for case in cases]
    if len(ids) != len(set(ids)):
        raise AssertionError("reliability routing contract has duplicate ids")

    allowed_primary = {
        "reliability-engineering",
        "release-engineering",
        "software-development",
        "quality-engineering",
        "security-engineering",
    }
    allowed_support = {
        "reliability-engineering",
        "cloudflare-platform",
        "database-engineering",
    }

    for case in cases:
        if case.get("primary") not in allowed_primary:
            raise AssertionError(f"{case.get('id')}: invalid primary owner")
        supporting = case.get("supporting", [])
        if len(supporting) != len(set(supporting)):
            raise AssertionError(f"{case.get('id')}: duplicate supporting owners")
        if case.get("primary") in supporting:
            raise AssertionError(f"{case.get('id')}: primary repeated as supporting")
        if any(owner not in allowed_support for owner in supporting):
            raise AssertionError(f"{case.get('id')}: invalid supporting owner")

    expected = {
        "RE-01": ("reliability-engineering", True),
        "RE-02": ("reliability-engineering", True),
        "RE-03": ("release-engineering", True),
        "RE-04": ("software-development", True),
        "RE-05": ("quality-engineering", True),
        "RE-06": ("security-engineering", True),
        "RE-07": ("reliability-engineering", False),
        "RE-08": ("reliability-engineering", False),
        "RE-09": ("reliability-engineering", False),
        "RE-10": ("reliability-engineering", False),
    }
    by_id = {case["id"]: case for case in cases}
    if set(by_id) != set(expected):
        raise AssertionError("reliability routing contract case coverage mismatch")
    for cid, (primary, accept) in expected.items():
        case = by_id[cid]
        if case["primary"] != primary or bool(case["accept"]) != accept:
            raise AssertionError(f"{cid}: routing expectation mismatch")

    print("reliability engineering routing: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
