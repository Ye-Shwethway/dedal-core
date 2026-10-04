#!/usr/bin/env python3
"""Bind a semantic routing claim to exact task text, release, and lexical candidates."""
import argparse
from datetime import datetime, timezone, timedelta
import hashlib
import json
from pathlib import Path
import sys

import yaml

from profile_probe import probe

ROOT = Path(__file__).resolve().parents[1]


def validate(decision, task_bytes, task_id, profiles, release_sha, started=None, now=None):
    errors = []
    now = now or datetime.now(timezone.utc)
    try:
        task = task_bytes.decode("utf-8")
        if not task.strip():
            return ["empty_task"]
        candidates = probe(task, profiles)["profiles"]
    except (UnicodeDecodeError, TypeError):
        return ["task_encoding"]
    fields = {"schema_version", "task_id", "task_sha256", "release_sha256", "lexical_candidates",
              "decision", "selected_profile", "basis", "rationale", "reviewed_at"}
    if not isinstance(decision, dict) or set(decision) != fields:
        return ["decision_shape"]
    if (decision["schema_version"] != 1 or decision["task_id"] != task_id
            or decision["task_sha256"] != hashlib.sha256(task_bytes).hexdigest()
            or decision["release_sha256"] != release_sha):
        errors.append("decision_identity")
    if decision["lexical_candidates"] != candidates:
        errors.append("candidate_drift")
    if not isinstance(decision["rationale"], str) or len(decision["rationale"].strip()) < 10:
        errors.append("rationale_missing")
    try:
        reviewed = datetime.fromisoformat(decision["reviewed_at"].replace("Z", "+00:00"))
        if (reviewed.tzinfo is None or reviewed > now + timedelta(minutes=5)
                or reviewed < now - timedelta(hours=4) or started and reviewed < started):
            raise ValueError("review time")
    except (ValueError, AttributeError):
        errors.append("review_time")
    kind, selected, basis = decision["decision"], decision["selected_profile"], decision["basis"]
    known = {p["id"] for p in profiles}
    if kind == "select_profile":
        if (not isinstance(selected, str) or selected not in known
                or basis != ("lexical_confirmation" if selected in candidates else "semantic_override")):
            errors.append("invalid_profile_selection")
    elif kind == "no_profile":
        if selected is not None or basis != "semantic_exclusion":
            errors.append("invalid_exclusion")
    elif kind == "defer":
        if selected is not None or basis != "insufficient_context":
            errors.append("invalid_deferral")
    else:
        errors.append("unknown_decision")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--task-file", type=Path, required=True)
    parser.add_argument("--decision", type=Path, required=True)
    args = parser.parse_args()
    profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
    active = json.loads((ROOT / "state/active-release.json").read_text())
    try:
        errors = validate(json.loads(args.decision.read_text()), args.task_file.read_bytes(), args.task_id,
                          profiles, active["release_sha256"])
    except (OSError, ValueError) as exc:
        errors = [f"input_unavailable:{exc}"]
    if errors:
        print("ROUTE DECISION: FAIL", *errors, sep="\n- ")
        sys.exit(1)
    print("ROUTE DECISION: CLAIM VALIDATED; semantic truth requires review")
