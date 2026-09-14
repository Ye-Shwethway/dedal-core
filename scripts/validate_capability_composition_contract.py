#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "runtime" / "capability-composition-policy.json"
CONTRACT = ROOT / "evals" / "capability-composition" / "contract-v1.json"

ROLES = {"RUNTIME", "PRIMARY", "SUPPORTING", "EXECUTION", "DORMANT"}


def load(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def evaluate(case):
    errors = []
    comp = case.get("composition", {})

    if set(comp) != ROLES:
        errors.append("composition must define exactly RUNTIME/PRIMARY/SUPPORTING/EXECUTION/DORMANT")

    runtime = comp.get("RUNTIME", [])
    primary = comp.get("PRIMARY", [])
    supporting = comp.get("SUPPORTING", [])
    execution = comp.get("EXECUTION", [])
    dormant = comp.get("DORMANT", [])

    if "cognitive-runtime" not in runtime:
        errors.append("cognitive-runtime must remain active")

    all_loaded = runtime + primary + supporting + execution
    if len(all_loaded) != len(set(all_loaded)):
        errors.append("a capability cannot occupy multiple active roles")
    if set(dormant) & set(all_loaded):
        errors.append("dormant capabilities cannot also be active")

    explicit = case.get("explicit_skill")
    if explicit and explicit not in primary:
        errors.append("explicit skill/alias owner must be primary")

    rationale = case.get("supporting_rationale", {})
    for skill in supporting:
        if not str(rationale.get(skill, "")).strip():
            errors.append(f"supporting capability lacks distinct rationale: {skill}")

    # A deliberately broad supporting set without explicit rationale is a load-all smell.
    if len(supporting) > 4:
        errors.append("supporting set is broader than a smallest-sufficient composition")

    return errors


def main():
    policy = load(POLICY)
    contract = load(CONTRACT)

    assert policy["architecture"] == "persistent-cognitive-runtime"
    assert "RUNTIME" in policy["roles"]
    assert "PRIMARY" in policy["roles"]
    assert "SUPPORTING" in policy["roles"]
    assert "EXECUTION" in policy["roles"]
    assert "DORMANT" in policy["roles"]
    assert "no-load-all-skills-default" in policy["principles"]
    assert policy["host_boundary"]["universal_host_interception_claim_forbidden"] is True

    seen = set()
    for case in contract["cases"]:
        cid = case["id"]
        assert cid not in seen, f"duplicate case id: {cid}"
        seen.add(cid)
        actual_accept = not evaluate(case)
        expected_accept = case["expect"] == "accept"
        if actual_accept != expected_accept:
            raise AssertionError(
                f"{cid}: expected {case['expect']}, got {'accept' if actual_accept else 'reject'}; "
                f"errors={evaluate(case)}"
            )

    required = {f"CC-{i:02d}" for i in range(1, 9)}
    assert required.issubset(seen), f"missing required cases: {sorted(required - seen)}"
    print(f"capability composition contract: {len(seen)} cases passed")


if __name__ == "__main__":
    main()
