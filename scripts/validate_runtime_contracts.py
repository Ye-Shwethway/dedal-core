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


def _trajectory_case_is_valid(policy: dict, events: list[dict]) -> bool:
    event_types = set(policy["event_types"])
    statuses = set(policy["statuses"])
    forbidden_fields = set(policy["forbidden_event_fields"])
    max_retries = int(policy["max_retries_per_failed_event"])

    if not events:
        return False
    for expected_seq, event in enumerate(events, start=1):
        if event.get("seq") != expected_seq:
            return False
        if event.get("type") not in event_types or event.get("status") not in statuses:
            return False
        if not event.get("name"):
            return False
        if forbidden_fields.intersection(event):
            return False

    by_seq = {event["seq"]: event for event in events}

    retry_counts: dict[int, int] = {}
    for event in events:
        if event["type"] == "retry":
            target = event.get("for_event_seq")
            failed = by_seq.get(target)
            if failed is None or failed.get("status") != "failed" or target >= event["seq"]:
                return False
            retry_counts[target] = retry_counts.get(target, 0) + 1
            if retry_counts[target] > max_retries:
                return False

    successful_verifications = [
        event for event in events
        if event["type"] == "verification" and event["status"] == "succeeded"
    ]

    for event in events:
        if event["type"] == "tool_call" and event.get("mutation") is True and event["status"] == "succeeded":
            if not any(
                verification.get("for_event_seq") == event["seq"] and verification["seq"] > event["seq"]
                for verification in successful_verifications
            ):
                return False

        if event["type"] == "state_transition" and event.get("accepted") is True:
            evidence_ref = event.get("evidence_ref")
            if not evidence_ref:
                return False
            if not any(
                verification.get("evidence_ref") == evidence_ref and verification["seq"] < event["seq"]
                for verification in successful_verifications
            ):
                return False

    return True


def validate_trajectory_contract() -> None:
    data = json.loads((ROOT / "evals" / "trajectory" / "contract-v1.json").read_text(encoding="utf-8"))
    policy = data.get("policy", {})
    required_policy = {"event_types", "statuses", "forbidden_event_fields", "max_retries_per_failed_event"}
    if not required_policy.issubset(policy):
        raise AssertionError("trajectory policy missing required keys")
    cases = data.get("cases", [])
    ids = [case.get("id") for case in cases]
    if not cases or len(ids) != len(set(ids)):
        raise AssertionError("trajectory contract requires non-empty unique case ids")
    for case in cases:
        actual = _trajectory_case_is_valid(policy, case.get("events", []))
        expected = bool(case.get("accept"))
        if actual != expected:
            raise AssertionError(f"{case.get('id')}: expected accept={expected} got {actual}")


def main() -> int:
    validate_guard_cases()
    validate_checkpoint()
    validate_skill_consolidation()
    validate_routing_boundaries()
    validate_trajectory_contract()
    print("runtime contracts: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
