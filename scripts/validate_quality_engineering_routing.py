#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "evals" / "quality-engineering-routing" / "contract-v1.json"


def main() -> None:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    assert data["faculty"] == "quality-engineering"
    cases = {case["id"]: case for case in data["cases"]}
    required = {f"QE-{i:02d}" for i in range(1, 9)}
    assert required == set(cases), f"missing/unexpected cases: {set(cases) ^ required}"

    assert cases["QE-01"]["expected_primary"] == "software-development"
    assert cases["QE-02"]["expected_primary"] == "quality-engineering"
    assert "release-engineering" in cases["QE-02"]["expected_supporting"]
    assert cases["QE-03"]["expected_primary"] == "interface-design"
    assert cases["QE-04"]["expected_primary"] == "quality-engineering"
    assert "interface-design" in cases["QE-04"]["expected_supporting"]
    assert cases["QE-05"]["expected_primary"] == "quality-engineering"
    assert cases["QE-05"]["execution_surface"] == "playwright-or-browser-tool"
    assert cases["QE-06"]["expected_primary"] == "security-engineering"
    assert cases["QE-07"]["expected_outcome"] == "reject"
    assert cases["QE-08"]["expected_outcome"] == "reject"

    for case in data["cases"]:
        assert case.get("rule"), f"{case['id']} lacks rule"

    print("quality-engineering routing contract: PASS")


if __name__ == "__main__":
    main()
