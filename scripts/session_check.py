#!/usr/bin/env python3
"""Check Core structure and traceable profile hydration coverage."""
import argparse
from datetime import datetime, timezone, timedelta
import hashlib
import json
import re
from pathlib import Path
import subprocess
import sys

import yaml

from validate_route_decision import validate as validate_route_decision

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--profile", help="Matched task profile id")
parser.add_argument("--receipt", type=Path, help="Session-specific source and gate evidence")
parser.add_argument("--task-id", help="Current work unit id; prevents receipt reuse across tasks")
parser.add_argument("--task-file", type=Path, help="Exact UTF-8 task text bound to semantic routing")
parser.add_argument("--route-decision", type=Path, help="Task-bound semantic route claim")
args = parser.parse_args()

result = subprocess.run([sys.executable, str(ROOT / "validators/validate_core.py")],
                        capture_output=True, text=True)
if result.returncode:
    print("STRUCTURAL READINESS: FAIL")
    print(result.stdout, end="")
    print(result.stderr, end="", file=sys.stderr)
    sys.exit(result.returncode)
if not any((args.profile, args.receipt, args.task_id, args.task_file, args.route_decision)):
    print("STRUCTURAL READINESS: PASS")
    print("EXECUTION PREFLIGHT: UNVERIFIED (profile receipt not supplied)")
    sys.exit(0)
if not all((args.profile, args.receipt, args.task_id, args.task_file, args.route_decision)):
    parser.error("--profile, --receipt, --task-id, --task-file, and --route-decision must be supplied together")

profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
profile = next((p for p in profiles if p["id"] == args.profile), None)
if profile is None:
    raise SystemExit(f"EXECUTION PREFLIGHT: FAIL unknown profile {args.profile}")
try:
    receipt = json.loads(args.receipt.read_text())
    task_bytes = args.task_file.read_bytes()
    decision_bytes = args.route_decision.read_bytes()
    decision = json.loads(decision_bytes)
except (OSError, ValueError) as exc:
    raise SystemExit(f"EXECUTION PREFLIGHT: FAIL receipt or routing input unavailable: {exc}")
active = json.loads((ROOT / "state/active-release.json").read_text())
release = json.loads((ROOT / "state/release-manifest.json").read_text())
expected_hashes = {**release["files"],
                   "state/release-manifest.json": active["release_sha256"],
                   "state/active-release.json": hashlib.sha256((ROOT / "state/active-release.json").read_bytes()).hexdigest()}
if (receipt.get("schema_version") != 4 or receipt.get("task_id") != args.task_id
        or receipt.get("release_sha256") != active["release_sha256"]
        or receipt.get("task_sha256") != hashlib.sha256(task_bytes).hexdigest()
        or receipt.get("routing_decision_sha256") != hashlib.sha256(decision_bytes).hexdigest()
        or receipt.get("profile_id") != args.profile):
    raise SystemExit("EXECUTION PREFLIGHT: FAIL receipt version, release, or task/profile identity")
if set(receipt) != {"schema_version", "task_id", "profile_id", "release_sha256", "task_sha256", "routing_decision_sha256", "task_started_at", "source_reads", "gate_checks", "condition_results"}:
    raise SystemExit("EXECUTION PREFLIGHT: FAIL unknown or missing receipt field")

now = datetime.now(timezone.utc)
try:
    started = datetime.fromisoformat(receipt["task_started_at"].replace("Z", "+00:00"))
    if started.tzinfo is None or not (now - timedelta(hours=4) <= started <= now + timedelta(minutes=5)):
        raise ValueError("task start outside window")
except (KeyError, ValueError, AttributeError):
    raise SystemExit("EXECUTION PREFLIGHT: FAIL task start time")
route_errors = validate_route_decision(decision, task_bytes, args.task_id, profiles,
                                       active["release_sha256"], started=started, now=now)
if route_errors or decision.get("decision") != "select_profile" or decision.get("selected_profile") != args.profile:
    raise SystemExit(f"EXECUTION PREFLIGHT: FAIL semantic route decision {route_errors}")


def within_task(value):
    observed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return observed.tzinfo is not None and started <= observed <= now + timedelta(minutes=5)

reads = receipt.get("source_reads")
checks = receipt.get("gate_checks")
conditions = receipt.get("condition_results")
if not isinstance(reads, list) or not isinstance(checks, list) or not isinstance(conditions, dict):
    raise SystemExit("EXECUTION PREFLIGHT: FAIL receipt shape")
read_paths = set()
read_times = []
for record in reads:
    if not isinstance(record, dict):
        raise SystemExit("EXECUTION PREFLIGHT: FAIL source record shape")
    if set(record) - {"path", "kind", "read_ref", "observed_at", "library_file_id", "version_id", "item_count", "content_sha256"}:
        raise SystemExit("EXECUTION PREFLIGHT: FAIL source record unknown field")
    path, kind = record.get("path"), record.get("kind")
    if not isinstance(path, str) or path in read_paths or not record.get("read_ref"):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL duplicate or unreferenced source {path}")
    expected_kind = "library_directory_list" if path.endswith("/") else "library_file_read"
    if kind != expected_kind:
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL source kind {path}")
    if kind == "library_file_read" and (not str(record.get("library_file_id", "")).startswith("libfile_")
                                        or not isinstance(record.get("version_id"), str) or not record["version_id"]
                                        or not re.fullmatch(r"[0-9a-f]{64}", str(record.get("content_sha256", "")))):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL source identity {path}")
    if path in expected_hashes and record.get("content_sha256") != expected_hashes[path]:
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL release source digest {path}")
    if kind == "library_directory_list" and (type(record.get("item_count")) is not int or record["item_count"] < 1):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL empty source collection {path}")
    try:
        if not within_task(record["observed_at"]):
            raise ValueError("timestamp")
        read_times.append(datetime.fromisoformat(record["observed_at"].replace("Z", "+00:00")))
    except (KeyError, ValueError, AttributeError):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL observation time {path}")
    read_paths.add(path)

required = set(profile.get("required_core", [])) | set(profile.get("required_private", []))
condition_times = []
for branch in profile.get("conditional_private", []):
    name = branch["when"]
    result = conditions.get(name)
    if not isinstance(result, dict) or type(result.get("applies")) is not bool or not result.get("evidence_ref"):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL unevaluated condition {name}")
    try:
        if set(result) != {"applies", "evidence_ref", "observed_at"} or not within_task(result["observed_at"]):
            raise ValueError("condition timestamp")
        condition_times.append(datetime.fromisoformat(result["observed_at"].replace("Z", "+00:00")))
    except (KeyError, ValueError, AttributeError):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL condition observation time {name}")
    if result["applies"]:
        required.update(branch.get("sources", []))
if set(conditions) != {b["when"] for b in profile.get("conditional_private", [])}:
    raise SystemExit("EXECUTION PREFLIGHT: FAIL unknown condition")
missing = required - read_paths
gate_ids = set()
latest_dependency = max([started, datetime.fromisoformat(decision["reviewed_at"].replace("Z", "+00:00")),
                         *read_times, *condition_times])
for check in checks:
    if (not isinstance(check, dict) or not check.get("id") or not check.get("evidence_ref")
            or check.get("passed") is not True or check["id"] in gate_ids
            or set(check) != {"id", "evidence_ref", "passed", "observed_at"}):
        raise SystemExit("EXECUTION PREFLIGHT: FAIL gate evidence shape")
    try:
        if (not within_task(check["observed_at"])
                or datetime.fromisoformat(check["observed_at"].replace("Z", "+00:00")) < latest_dependency):
            raise ValueError("gate timestamp")
    except (KeyError, ValueError, AttributeError):
        raise SystemExit("EXECUTION PREFLIGHT: FAIL gate observation time")
    gate_ids.add(check["id"])
unsatisfied = set(profile.get("execution_gates", [])) - gate_ids
if missing or unsatisfied:
    raise SystemExit(f"EXECUTION PREFLIGHT: FAIL missing_sources={sorted(missing)} unsupported_gates={sorted(unsatisfied)}")
print(f"STRUCTURAL READINESS: PASS\nEXECUTION PREFLIGHT: RECEIPT COVERAGE PASS profile={args.profile} task={args.task_id}")
print("SOURCE TRUTH: references require direct tool readback; receipt fields alone are not proof of content use")
