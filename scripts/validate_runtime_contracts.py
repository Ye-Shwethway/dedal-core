#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "runtime"))

from github_mutation_guard import GuardViolation, load_policy, validate_trace  # noqa: E402


def validate_guard_cases() -> None:
    policy = load_policy(ROOT / "runtime" / "github-mutation-policy.json")
    contract = json.loads((ROOT / "evals" / "github-mutation-guard" / "contract-v1.json").read_text(encoding="utf-8"))
    for case in contract["cases"]:
        accepted = True
        complete = False
        try:
            guard = validate_trace(policy, case["mode"], case["tools"])
            complete = guard.complete
        except GuardViolation:
            accepted = False
        if accepted != case["accept"]:
            raise AssertionError(f"{case['id']}: expected accept={case['accept']} got {accepted}")
        if accepted and "complete" in case and complete != case["complete"]:
            raise AssertionError(f"{case['id']}: expected complete={case['complete']} got {complete}")


def validate_checkpoint() -> None:
    cp = json.loads((ROOT / "state" / "current-checkpoint.json").read_text(encoding="utf-8"))
    schema = json.loads((ROOT / "state" / "checkpoint.schema.json").read_text(encoding="utf-8"))
    required = set(schema.get("required", []))
    missing = sorted(required - set(cp))
    if missing:
        raise AssertionError(f"checkpoint missing required keys: {missing}")
    if not isinstance(cp["accepted_state"], list) or not cp["accepted_state"]:
        raise AssertionError("checkpoint accepted_state must be a non-empty list")
    if not isinstance(cp["evidence"], list):
        raise AssertionError("checkpoint evidence must be a list")
    if not isinstance(cp["unresolved_risks"], list):
        raise AssertionError("checkpoint unresolved_risks must be a list")
    nxt = cp["next_executable_step"]
    if not isinstance(nxt, dict) or not nxt.get("id") or not nxt.get("action"):
        raise AssertionError("checkpoint next_executable_step must contain id and action")
    rev = cp["last_verified_revision"]
    if not isinstance(rev, dict) or not rev.get("sha") or not rev.get("ref"):
        raise AssertionError("checkpoint last_verified_revision must contain ref and sha")
    if len(rev["sha"]) != 40 or any(c not in "0123456789abcdef" for c in rev["sha"]):
        raise AssertionError("checkpoint last_verified_revision.sha must be a lowercase 40-char git SHA")
    version_parts = cp["version"].split(".")
    if len(version_parts) != 3 or not all(part.isdigit() for part in version_parts):
        raise AssertionError("checkpoint version must be semantic X.Y.Z")


def live_skills() -> list[str]:
    return sorted(p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md"))


def validate_skill_consolidation() -> None:
    data = json.loads((ROOT / "state" / "skill-consolidation.json").read_text(encoding="utf-8"))
    allowed = {"KEEP", "TUNE", "MERGE", "REMOVE", "NEEDS_EVIDENCE"}
    entries = data.get("entries", [])
    names = [entry.get("skill") for entry in entries]
    if len(names) != len(set(names)):
        raise AssertionError("skill consolidation contains duplicate skill entries")
    live = live_skills()
    if sorted(names) != live:
        raise AssertionError(f"skill consolidation coverage mismatch: classified={sorted(names)} live={live}")
    for entry in entries:
        if entry.get("decision") not in allowed:
            raise AssertionError(f"invalid consolidation decision for {entry.get('skill')}: {entry.get('decision')}")
        if not entry.get("evidence_level") or not entry.get("overlap"):
            raise AssertionError(f"incomplete consolidation entry: {entry.get('skill')}")


def validate_routing_boundaries() -> None:
    data = json.loads((ROOT / "state" / "routing-boundaries.json").read_text(encoding="utf-8"))
    live = set(live_skills())
    clusters = data.get("clusters", [])
    ids = [cluster.get("id") for cluster in clusters]
    if not clusters or len(ids) != len(set(ids)):
        raise AssertionError("routing boundaries require non-empty unique cluster ids")
    referenced: set[str] = set()
    for cluster in clusters:
        owners = cluster.get("primary_owner_by_intent", {})
        if not owners or not cluster.get("rule"):
            raise AssertionError(f"incomplete routing cluster: {cluster.get('id')}")
        for owner in owners.values():
            if owner in live:
                referenced.add(owner)
            elif owner != "domain-owner-or-research":
                raise AssertionError(f"routing cluster {cluster.get('id')} references unknown owner: {owner}")
    required_overlap_owners = {
        "github", "software-development", "release-engineering", "agent-engineering",
        "ika", "knowledge-memory", "project-bootstrap", "data-operations",
        "medicine-store-assistant", "patient-report-assistant", "interface-design",
        "visual-direction", "research", "skill-acquisition", "writing-editorial"
    }
    missing = sorted(required_overlap_owners - referenced)
    if missing:
        raise AssertionError(f"routing boundary coverage missing overlap owners: {missing}")


def main() -> int:
    validate_guard_cases()
    validate_checkpoint()
    validate_skill_consolidation()
    validate_routing_boundaries()
    print("runtime contracts: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
