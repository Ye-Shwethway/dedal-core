#!/usr/bin/env python3
"""Reject stale, mismatched, and unreviewed route claims."""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json

import yaml

from profile_probe import probe
from validate_route_decision import ROOT, validate

profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
active = json.loads((ROOT / "state/active-release.json").read_text())
task = "Review DEDAL Core schema".encode()
base = {"schema_version": 1, "task_id": "task-case", "task_sha256": hashlib.sha256(task).hexdigest(),
        "release_sha256": active["release_sha256"], "lexical_candidates": probe(task.decode(), profiles)["profiles"],
        "decision": "select_profile", "selected_profile": "core-architecture-change",
        "basis": "lexical_confirmation", "rationale": "This task changes the DEDAL Core schema and its routing contracts.",
        "reviewed_at": datetime.now(timezone.utc).isoformat()}
assert validate(base, task, "task-case", profiles, active["release_sha256"]) == []


def rejects(change, expected):
    value = deepcopy(base)
    value.update(change)
    errors = validate(value, task, "task-case", profiles, active["release_sha256"])
    assert expected in errors, errors


rejects({"task_sha256": "0" * 64}, "decision_identity")
rejects({"lexical_candidates": []}, "candidate_drift")
rejects({"selected_profile": "visual-narrative-production"}, "invalid_profile_selection")
rejects({"rationale": "yes"}, "rationale_missing")
rejects({"decision": "no_profile", "selected_profile": "core-architecture-change"}, "invalid_exclusion")
negated = "Do not make a visual novel; reconcile medicine stock".encode()
claim = {**base, "task_sha256": hashlib.sha256(negated).hexdigest(),
         "lexical_candidates": probe(negated.decode(), profiles)["profiles"],
         "decision": "no_profile", "selected_profile": None, "basis": "semantic_exclusion",
         "rationale": "The visual-novel words are negated; the requested work concerns stock."}
assert claim["lexical_candidates"] == ["recurring-character-image-sequence"]
assert validate(claim, negated, "task-case", profiles, active["release_sha256"]) == []
burmese = "စနစ်ရဲ့ အဓိကတည်ဆောက်ပုံကို ပြန်စစ်ပါ".encode()
override = {**base, "task_sha256": hashlib.sha256(burmese).hexdigest(),
            "lexical_candidates": [], "basis": "semantic_override",
            "rationale": "The Burmese request asks to inspect the system's core architecture."}
assert validate(override, burmese, "task-case", profiles, active["release_sha256"]) == []
print("ROUTE DECISION NEGATIVES: PASS mismatches, negation exclusion, semantic override")
