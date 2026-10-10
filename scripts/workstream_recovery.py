#!/usr/bin/env python3
"""Reconcile interrupted operations with task-bound current owner observations."""
from datetime import datetime, timezone, timedelta


def timestamp(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("recovery timestamp requires timezone")
    return result


def reconcile(checkpoint, observations):
    if checkpoint.get("schema_version") != 1 or not checkpoint.get("task_id"):
        raise ValueError("recovery checkpoint identity missing")
    updated = timestamp(checkpoint["updated_at"])
    if updated > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise ValueError("recovery checkpoint is future dated")
    operations = checkpoint.get("pending_operations")
    if not isinstance(operations, list):
        raise ValueError("pending operations must be explicit")
    by_id = {}
    for observation in observations:
        key = observation.get("operation_id")
        if not key or key in by_id:
            raise ValueError("duplicate/invalid recovery observation")
        by_id[key] = observation
    decisions, seen = [], set()
    for operation in operations:
        key = operation.get("id")
        if (not key or key in seen or not operation.get("owner") or not operation.get("target")
                or not isinstance(operation.get("expected_result"), dict) or not operation["expected_result"]):
            raise ValueError("operation identity/owner missing")
        seen.add(key)
        observation = by_id.get(key)
        action = "read_authoritative_owner"
        if observation:
            if (observation.get("task_id") != checkpoint["task_id"]
                    or observation.get("owner") != operation["owner"]
                    or observation.get("target") != operation["target"]
                    or not observation.get("evidence_ref")
                    or not updated <= timestamp(observation["observed_at"]) <= datetime.now(timezone.utc) + timedelta(minutes=5)):
                raise ValueError("stale or mismatched recovery observation: " + key)
            outcome = observation.get("outcome")
            if outcome == "expected_result_present":
                if observation.get("actual_result") != operation["expected_result"]:
                    raise ValueError("observed result differs from expected target: " + key)
                action = "accept_observed_result_no_replay"
            elif outcome == "confirmed_no_effect":
                action = "retry_after_current_authority_check" if operation.get("retry_safe") is True else "review_retry_safety"
            elif outcome == "conflict":
                action = "reconcile_conflict_no_replay"
            elif outcome != "unknown":
                raise ValueError("unknown recovery outcome: " + str(outcome))
        decisions.append({"operation_id": key, "action": action})
    if set(by_id) - seen:
        raise ValueError("observation outside interrupted work unit")
    return {"task_id": checkpoint["task_id"], "decisions": decisions,
            "external_truth": "requires_authoritative_tool_evidence",
            "authority": "checkpoint_does_not_grant_new_permissions"}
