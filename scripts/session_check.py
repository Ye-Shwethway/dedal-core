#!/usr/bin/env python3
"""Check Core structure and traceable profile hydration coverage."""
import argparse
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--profile", help="Matched task profile id")
parser.add_argument("--receipt", type=Path, help="Session-specific source and gate evidence")
parser.add_argument("--task-id", help="Current work unit id; prevents receipt reuse across tasks")
args = parser.parse_args()

result = subprocess.run([sys.executable, str(ROOT / "validators/validate_core.py")],
                        capture_output=True, text=True)
if result.returncode:
    print("STRUCTURAL READINESS: FAIL")
    print(result.stdout, end="")
    print(result.stderr, end="", file=sys.stderr)
    sys.exit(result.returncode)
if not any((args.profile, args.receipt, args.task_id)):
    print("STRUCTURAL READINESS: PASS")
    print("EXECUTION PREFLIGHT: UNVERIFIED (profile receipt not supplied)")
    sys.exit(0)
if not all((args.profile, args.receipt, args.task_id)):
    parser.error("--profile, --receipt, and --task-id must be supplied together")

profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
profile = next((p for p in profiles if p["id"] == args.profile), None)
if profile is None:
    raise SystemExit(f"EXECUTION PREFLIGHT: FAIL unknown profile {args.profile}")
try:
    receipt = json.loads(args.receipt.read_text())
except (OSError, ValueError) as exc:
    raise SystemExit(f"EXECUTION PREFLIGHT: FAIL receipt unavailable: {exc}")
if (receipt.get("schema_version") != 2 or receipt.get("task_id") != args.task_id
        or receipt.get("profile_id") != args.profile):
    raise SystemExit("EXECUTION PREFLIGHT: FAIL receipt version or task/profile identity")

reads = receipt.get("source_reads")
checks = receipt.get("gate_checks")
conditions = receipt.get("condition_results")
if not isinstance(reads, list) or not isinstance(checks, list) or not isinstance(conditions, dict):
    raise SystemExit("EXECUTION PREFLIGHT: FAIL receipt shape")
read_paths = set()
for record in reads:
    if not isinstance(record, dict):
        raise SystemExit("EXECUTION PREFLIGHT: FAIL source record shape")
    path, kind = record.get("path"), record.get("kind")
    if not isinstance(path, str) or path in read_paths or not record.get("read_ref"):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL duplicate or unreferenced source {path}")
    expected_kind = "library_directory_list" if path.endswith("/") else "library_file_read"
    if kind != expected_kind:
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL source kind {path}")
    if kind == "library_file_read" and (not str(record.get("library_file_id", "")).startswith("libfile_")
                                        or "version_id" not in record
                                        or record["version_id"] is not None and not isinstance(record["version_id"], str)):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL source identity {path}")
    if kind == "library_directory_list" and (type(record.get("item_count")) is not int or record["item_count"] < 1):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL empty source collection {path}")
    try:
        observed = datetime.fromisoformat(record["observed_at"].replace("Z", "+00:00"))
        if observed.tzinfo is None or observed > datetime.now(timezone.utc) + timedelta(minutes=5):
            raise ValueError("timestamp")
    except (KeyError, ValueError, AttributeError):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL observation time {path}")
    read_paths.add(path)

required = set(profile.get("required_core", [])) | set(profile.get("required_private", []))
for branch in profile.get("conditional_private", []):
    name = branch["when"]
    result = conditions.get(name)
    if not isinstance(result, dict) or type(result.get("applies")) is not bool or not result.get("evidence_ref"):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL unevaluated condition {name}")
    if result["applies"]:
        required.update(branch.get("sources", []))
missing = required - read_paths
gate_ids = set()
for check in checks:
    if not isinstance(check, dict) or not check.get("id") or not check.get("evidence_ref") or check["id"] in gate_ids:
        raise SystemExit("EXECUTION PREFLIGHT: FAIL gate evidence shape")
    gate_ids.add(check["id"])
unsatisfied = set(profile.get("execution_gates", [])) - gate_ids
if missing or unsatisfied:
    raise SystemExit(f"EXECUTION PREFLIGHT: FAIL missing_sources={sorted(missing)} unsupported_gates={sorted(unsatisfied)}")
print(f"STRUCTURAL READINESS: PASS\nEXECUTION PREFLIGHT: RECEIPT COVERAGE PASS profile={args.profile} task={args.task_id}")
print("SOURCE TRUTH: references require direct tool readback; receipt fields alone are not proof of content use")
