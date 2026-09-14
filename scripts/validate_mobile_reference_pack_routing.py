#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "evals" / "mobile-reference-pack-routing" / "contract-v1.json"


def main() -> int:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    if not cases:
        raise AssertionError("mobile reference-pack routing requires cases")

    ids = [case.get("id") for case in cases]
    if len(ids) != len(set(ids)):
        raise AssertionError("duplicate mobile routing case ids")

    allowed_primary = {
        "software-development",
        "interface-design",
        "quality-engineering",
        "release-engineering",
        "database-engineering",
    }
    for case in cases:
        if case.get("primary") not in allowed_primary:
            raise AssertionError(f"{case.get('id')}: invalid primary owner")
        if case.get("reference_pack") != "mobile-flutter-android":
            raise AssertionError(f"{case.get('id')}: wrong reference pack")
        supporting = case.get("supporting", [])
        if len(supporting) != len(set(supporting)):
            raise AssertionError(f"{case.get('id')}: duplicate supporting owner")
        if case.get("primary") in supporting:
            raise AssertionError(f"{case.get('id')}: primary repeated as supporting")

    expected = {
        "MB-01": ("software-development", True),
        "MB-02": ("interface-design", True),
        "MB-03": ("quality-engineering", True),
        "MB-04": ("release-engineering", True),
        "MB-05": ("database-engineering", True),
        "MB-06": ("software-development", False),
        "MB-07": ("software-development", False),
        "MB-08": ("quality-engineering", False),
    }
    by_id = {case["id"]: case for case in cases}
    if set(by_id) != set(expected):
        raise AssertionError("mobile routing case coverage mismatch")

    for cid, (primary, accept) in expected.items():
        case = by_id[cid]
        if case["primary"] != primary or bool(case["accept"]) != accept:
            raise AssertionError(f"{cid}: routing expectation mismatch")

    if by_id["MB-07"].get("requires_live_docs") is not True:
        raise AssertionError("MB-07 must require live docs")

    print("mobile reference-pack routing: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
