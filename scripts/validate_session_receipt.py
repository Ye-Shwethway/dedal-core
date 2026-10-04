#!/usr/bin/env python3
"""Regression checks for receipt identity, source coverage, and conditions."""
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
profiles = {p["id"]: p for p in yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]}
now = datetime.now(timezone.utc).isoformat()
release = json.loads((ROOT / "state/release-manifest.json").read_text())
active = json.loads((ROOT / "state/active-release.json").read_text())

def make_read(path):
    record = {"path": path, "read_ref": "tool:read:case", "observed_at": now}
    if path.endswith("/"):
        record.update(kind="library_directory_list", item_count=2)
    else:
        record.update(kind="library_file_read", library_file_id="libfile_case", version_id="1",
                      content_sha256=release["files"].get(path, "0" * 64))
    return record

def run(profile_id, receipt):
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "receipt.json"
        path.write_text(json.dumps(receipt))
        result = subprocess.run([sys.executable, str(ROOT / "scripts/session_check.py"),
                                 "--profile", profile_id, "--task-id", "task-case", "--receipt", str(path)],
                                capture_output=True, text=True)
        return result.returncode, result.stdout + result.stderr

core = profiles["core-architecture-change"]
base = {
    "schema_version": 3,
    "task_id": "task-case",
    "task_started_at": now,
    "release_sha256": active["release_sha256"],
    "profile_id": core["id"],
    "source_reads": [make_read(p) for p in core["required_core"]],
    "gate_checks": [{"id": g, "evidence_ref": "validator:case", "passed": True, "observed_at": now} for g in core["execution_gates"]],
    "condition_results": {}
}
assert run(core["id"], base)[0] == 0
for change, expected in [
    ({"task_id": "prior-task"}, "identity"),
    ({"source_reads": base["source_reads"][:-1]}, "missing_sources"),
    ({"gate_checks": base["gate_checks"][:-1]}, "unsupported_gates"),
    ({"schema_version": 2}, "version"),
    ({"release_sha256": "0" * 64}, "release"),
    ({"gate_checks": [{**base["gate_checks"][0], "passed": False}, *base["gate_checks"][1:]]}, "gate evidence"),
    ({"source_reads": [{**base["source_reads"][0], "content_sha256": "0" * 64}, *base["source_reads"][1:]]}, "digest"),
    ({"source_reads": [{**base["source_reads"][0], "version_id": None}, *base["source_reads"][1:]]}, "source identity"),
    ({"task_started_at": (datetime.now(timezone.utc) - timedelta(hours=5)).isoformat()}, "task start time")
]:
    result = run(core["id"], {**base, **change})
    assert result[0] != 0 and expected in result[1], result
orison = profiles["dedal-orison-image-to-video"]
conditional = {**base, "profile_id": orison["id"],
               "source_reads": [make_read(p) for p in orison["required_core"] + orison["required_private"]],
               "gate_checks": [{"id": g, "evidence_ref": "tool:case", "passed": True, "observed_at": now} for g in orison["execution_gates"]]}
result = run(orison["id"], conditional)
assert result[0] != 0 and "unevaluated condition" in result[1], result
conditional["condition_results"] = {"character_is_darian": {"applies": True, "evidence_ref": "task:case"}}
result = run(orison["id"], conditional)
assert result[0] != 0 and "profiles/Darian" in result[1], result
conditional["source_reads"] += [make_read(p) for p in orison["conditional_private"][0]["sources"]]
assert run(orison["id"], conditional)[0] == 0
print("SESSION RECEIPT: PASS task identity, source/gate coverage, conditional private sources")
