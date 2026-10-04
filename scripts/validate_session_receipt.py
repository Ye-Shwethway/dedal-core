#!/usr/bin/env python3
"""Regression checks for receipt identity, source coverage, and conditions."""
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
profiles = {p["id"]: p for p in yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]}
now = datetime.now(timezone.utc).isoformat()

def make_read(path):
    record = {"path": path, "read_ref": "tool:read:case", "observed_at": now}
    if path.endswith("/"):
        record.update(kind="library_directory_list", item_count=2)
    else:
        record.update(kind="library_file_read", library_file_id="libfile_case", version_id=None)
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
    "schema_version": 2,
    "task_id": "task-case",
    "profile_id": core["id"],
    "source_reads": [make_read(p) for p in core["required_core"]],
    "gate_checks": [{"id": g, "evidence_ref": "validator:case"} for g in core["execution_gates"]],
    "condition_results": {}
}
assert run(core["id"], base)[0] == 0
for change, expected in [
    ({"task_id": "prior-task"}, "identity"),
    ({"source_reads": base["source_reads"][:-1]}, "missing_sources"),
    ({"gate_checks": base["gate_checks"][:-1]}, "unsupported_gates"),
    ({"schema_version": 1}, "version")
]:
    result = run(core["id"], {**base, **change})
    assert result[0] != 0 and expected in result[1], result
orison = profiles["dedal-orison-image-to-video"]
conditional = {**base, "profile_id": orison["id"],
               "source_reads": [make_read(p) for p in orison["required_core"] + orison["required_private"]],
               "gate_checks": [{"id": g, "evidence_ref": "tool:case"} for g in orison["execution_gates"]]}
result = run(orison["id"], conditional)
assert result[0] != 0 and "unevaluated condition" in result[1], result
conditional["condition_results"] = {"character_is_darian": {"applies": True, "evidence_ref": "task:case"}}
result = run(orison["id"], conditional)
assert result[0] != 0 and "profiles/Darian" in result[1], result
conditional["source_reads"] += [make_read(p) for p in orison["conditional_private"][0]["sources"]]
assert run(orison["id"], conditional)[0] == 0
print("SESSION RECEIPT: PASS task identity, source/gate coverage, conditional private sources")
