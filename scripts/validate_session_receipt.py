#!/usr/bin/env python3
"""Regression checks for task-bound route, release, source, and gate chronology."""
from datetime import datetime, timezone, timedelta
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import yaml

from profile_probe import probe

ROOT = Path(__file__).resolve().parents[1]
profiles = {p["id"]: p for p in yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]}
release = json.loads((ROOT / "state/release-manifest.json").read_text())
active = json.loads((ROOT / "state/active-release.json").read_text())
expected_hashes = {**release["files"], "state/release-manifest.json": active["release_sha256"],
                   "state/active-release.json": hashlib.sha256((ROOT / "state/active-release.json").read_bytes()).hexdigest()}
now = datetime.now(timezone.utc).isoformat()
core_task = "Review DEDAL Core schema"
orison_task = "Orison image-to-video source sequence"


def route_bytes(profile_id, task, *, decision="select_profile", basis="lexical_confirmation"):
    obj = {"schema_version": 1, "task_id": "task-case", "task_sha256": hashlib.sha256(task.encode()).hexdigest(),
           "release_sha256": active["release_sha256"], "lexical_candidates": probe(task, list(profiles.values()))["profiles"],
           "decision": decision, "selected_profile": profile_id if decision == "select_profile" else None,
           "basis": basis, "rationale": "The current task intent requires this profile and its resources.",
           "reviewed_at": now}
    return json.dumps(obj).encode()


def make_read(path):
    record = {"path": path, "read_ref": "tool:read:case", "observed_at": now, "read_class": "hydration"}
    if path.endswith("/"):
        record.update(kind="library_directory_list", item_count=2)
    else:
        record.update(kind="library_file_read", library_file_id="libfile_case", version_id="1", version_status="available", read_class="hydration",
                      content_sha256=expected_hashes.get(path, "0" * 64))
    return record


def base_receipt(profile, task):
    routes = route_bytes(profile["id"], task)
    operation = "change" if profile["id"] == "core-architecture-change" else "handoff"
    return {"schema_version": 6, "task_id": "task-case", "task_started_at": now,
            "operation": operation, "phase": "execute",
            "task_sha256": hashlib.sha256(task.encode()).hexdigest(),
            "routing_decision_sha256": hashlib.sha256(routes).hexdigest(),
            "release_sha256": active["release_sha256"], "profile_id": profile["id"],
            "evidence_mode": "coverage", "evidence_bundle_sha256": None,
            "source_reads": [make_read(p) for p in profile["required_core"] + profile.get("required_private", [])],
            "gate_checks": [{"id": g, "evidence_ref": "validator:case", "passed": True, "observed_at": now}
                            for g in profile["phase_gates"]["execute"]], "condition_results": {}}


def run(profile_id, receipt, task, routes=None):
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        files = {"receipt.json": json.dumps(receipt), "task.txt": task,
                 "route.json": (routes or route_bytes(profile_id, task)).decode()}
        for name, content in files.items():
            (root / name).write_text(content)
        result = subprocess.run([sys.executable, str(ROOT / "scripts/session_check.py"),
                                 "--profile", profile_id, "--task-id", "task-case",
                                 "--task-file", str(root / "task.txt"),
                                 "--route-decision", str(root / "route.json"),
                                 "--operation", receipt["operation"], "--phase", receipt["phase"],
                                 "--receipt", str(root / "receipt.json")],
                                capture_output=True, text=True)
        return result.returncode, result.stdout + result.stderr


core = profiles["core-architecture-change"]
base = base_receipt(core, core_task)
assert run(core["id"], base, core_task)[0] == 0
for change, expected in [
    ({"task_id": "prior-task"}, "identity"),
    ({"source_reads": base["source_reads"][:-1]}, "missing_sources"),
    ({"gate_checks": base["gate_checks"][:-1]}, "unsupported_gates"),
    ({"schema_version": 4}, "version"),
    ({"schema_version": 5}, "version"),
    ({"release_sha256": "0" * 64}, "release"),
    ({"routing_decision_sha256": "0" * 64}, "identity"),
    ({"gate_checks": [{**base["gate_checks"][0], "passed": False}, *base["gate_checks"][1:]]}, "gate evidence"),
    ({"source_reads": [{**base["source_reads"][0], "content_sha256": "0" * 64}, *base["source_reads"][1:]]}, "digest"),
    ({"source_reads": [{**base["source_reads"][0], "version_id": None}, *base["source_reads"][1:]]}, "source identity"),
    ({"source_reads": [{**base["source_reads"][0], "version_status": "unavailable"}, *base["source_reads"][1:]]}, "source identity"),
    ({"phase": "unknown"}, "invalid choice"),
    ({"operation": "audit"}, "operation/phase"),
    ({"source_reads": [{**base["source_reads"][0], "observed_at": (datetime.now(timezone.utc) + timedelta(seconds=1)).isoformat()}, *base["source_reads"][1:]]}, "gate observation"),
    ({"task_started_at": (datetime.now(timezone.utc) - timedelta(hours=5)).isoformat()}, "task start time")
]:
    result = run(core["id"], {**base, **change}, core_task)
    assert result[0] != 0 and expected in result[1], result

unavailable = {**base, "source_reads": [{**base["source_reads"][0], "version_id": None, "version_status": "unavailable"}, *base["source_reads"][1:]]}
assert run(core["id"], unavailable, core_task)[0] == 0
assert base["gate_checks"] and "checkpoint_updated" not in {x["id"] for x in base["gate_checks"]}
audit = {**base, "operation": "audit", "phase": "inspect", "gate_checks": [base["gate_checks"][0]]}
assert run(core["id"], audit, core_task)[0] == 0
closing = {**base, "phase": "close", "gate_checks": [{"id": g, "evidence_ref": "validator:case", "passed": True, "observed_at": now} for g in core["phase_gates"]["close"]]}
assert run(core["id"], closing, core_task)[0] == 0
missing_checkpoint = {**closing, "gate_checks": [g for g in closing["gate_checks"] if g["id"] != "checkpoint_updated"]}
assert run(core["id"], missing_checkpoint, core_task)[0] != 0
assert run(core["id"], {**base, "gate_checks": closing["gate_checks"]}, core_task)[0] != 0

orison = profiles["dedal-orison-image-to-video"]
conditional = base_receipt(orison, orison_task)
result = run(orison["id"], conditional, orison_task)
assert result[0] != 0 and "unevaluated condition" in result[1], result
conditional["condition_results"] = {"character_is_darian": {"applies": True, "evidence_ref": "task:case", "observed_at": now}}
result = run(orison["id"], conditional, orison_task)
assert result[0] != 0 and "profiles/Darian" in result[1], result
conditional["source_reads"] += [make_read(p) for p in orison["conditional_private"][0]["sources"]]
assert run(orison["id"], conditional, orison_task)[0] == 0
early = (datetime.fromisoformat(now) - timedelta(seconds=2)).isoformat()
prior_start = (datetime.fromisoformat(now) - timedelta(seconds=3)).isoformat()
before_route = {**base, "task_started_at": prior_start, "source_reads": [{**base["source_reads"][0], "observed_at": early}, *base["source_reads"][1:]]}
assert run(core["id"], before_route, core_task)[0] != 0
boot = {**before_route, "source_reads": [{**before_route["source_reads"][0], "read_class": "boot"}, *base["source_reads"][1:]]}
assert run(core["id"], boot, core_task)[0] == 0
reuse = {**before_route, "source_reads": [{**before_route["source_reads"][0], "read_class": "reused", "activated_at": now, "reuse_reason": "Current same-release bytes reactivated after semantic routing"}, *base["source_reads"][1:]]}
assert run(core["id"], reuse, core_task)[0] == 0
assert run(core["id"], {**reuse, "source_reads": [{**reuse["source_reads"][0], "activated_at": early}, *base["source_reads"][1:]]}, core_task)[0] != 0
print("SESSION RECEIPT: PASS task/release/route binding, phase gates, observed unavailable versions, conditions")
