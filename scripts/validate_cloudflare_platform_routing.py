#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "evals" / "cloudflare-platform-routing" / "contract-v1.json"


def main() -> int:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    if not cases:
        raise AssertionError("cloudflare routing contract requires cases")
    ids = [case.get("id") for case in cases]
    if len(ids) != len(set(ids)):
        raise AssertionError("cloudflare routing contract has duplicate ids")

    allowed_primary = {
        "cloudflare-platform",
        "software-development",
        "release-engineering",
        "security-engineering",
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
        if case.get("accept") is False and case.get("requires_live_docs") is True:
            if "frozen Core" not in case.get("intent", ""):
                raise AssertionError(f"{case.get('id')}: live-doc rejection must target frozen fact use")

    expected = {
        "CF-01": ("software-development", True),
        "CF-02": ("cloudflare-platform", True),
        "CF-03": ("release-engineering", True),
        "CF-04": ("security-engineering", True),
        "CF-05": ("quality-engineering", True),
        "CF-06": ("cloudflare-platform", False),
        "CF-07": ("cloudflare-platform", False),
        "CF-08": ("cloudflare-platform", False),
        "CF-09": ("cloudflare-platform", False),
    }
    by_id = {case["id"]: case for case in cases}
    if set(by_id) != set(expected):
        raise AssertionError("cloudflare routing contract case coverage mismatch")
    for cid, (primary, accept) in expected.items():
        case = by_id[cid]
        if case["primary"] != primary or bool(case["accept"]) != accept:
            raise AssertionError(f"{cid}: routing expectation mismatch")

    print("cloudflare platform routing: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
