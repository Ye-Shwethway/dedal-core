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
from evidence import verify as verify_evidence, digest
from selected_sources import verify_selected
from validate_core_contracts import validate_selection

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--full", action="store_true", help="Explicit development/release audit of the complete Core")
parser.add_argument("--profile", help="Matched task profile id")
parser.add_argument("--receipt", type=Path, help="Session-specific source and gate evidence")
parser.add_argument("--task-id", help="Current work unit id; prevents receipt reuse across tasks")
parser.add_argument("--task-file", type=Path, help="Exact UTF-8 task text bound to semantic routing")
parser.add_argument("--route-decision", type=Path, help="Task-bound semantic route claim")
parser.add_argument("--operation", help="Profile operation, such as audit or change")
parser.add_argument("--phase", choices=("inspect", "execute", "close"), help="Current phase; closure never authorizes execution")
parser.add_argument("--evidence-bundle", type=Path, help="Bound local source/gate event artifacts")
parser.add_argument("--artifact-root", type=Path, help="Root of full source and evidence artifacts")
parser.add_argument("--media-state", type=Path, help="Exact asset-bound review/approval/publication record")
args = parser.parse_args()

try:
    boot_sources = ["core-manifest.yaml", "kernel/boot.yaml", "kernel/kernel.yaml", "kernel/session.yaml",
                    "kernel/response.yaml", "index/routing.yaml", "state/checkpoint.yaml",
                    "scripts/session_check.py", "scripts/selected_sources.py", "scripts/validate_core_contracts.py",
                    "scripts/validate_route_decision.py", "scripts/profile_probe.py", "scripts/evidence.py"]
    verify_selected(ROOT, boot_sources)
    routing_errors = validate_selection(yaml.safe_load((ROOT / "index/routing.yaml").read_text()))
    if routing_errors:
        raise ValueError(str(routing_errors))
except (OSError, ValueError, KeyError, TypeError) as exc:
    print("STRUCTURAL READINESS: FAIL " + str(exc))
    sys.exit(1)
if args.full:
    result = subprocess.run([sys.executable, str(ROOT / "validators/validate_core.py")],
                            capture_output=True, text=True)
    if result.returncode:
        print("STRUCTURAL READINESS: FAIL")
        print(result.stdout, end="")
        print(result.stderr, end="", file=sys.stderr)
        sys.exit(result.returncode)
    print("FULL INVENTORY INTEGRITY: PASS")
else:
    print("SELECTED SOURCE INTEGRITY: PASS; full inventory not checked")
if not any((args.profile, args.receipt, args.task_id, args.task_file, args.route_decision, args.operation, args.phase, args.media_state)):
    print("STRUCTURAL READINESS: PASS")
    print("EXECUTION PREFLIGHT: UNVERIFIED (profile receipt not supplied)")
    sys.exit(0)
if not all((args.profile, args.receipt, args.task_id, args.task_file, args.route_decision, args.operation, args.phase)):
    parser.error("--profile, --receipt, --task-id, --task-file, --route-decision, --operation and --phase must be supplied together")

try:
    verify_selected(ROOT, ["index/task-profiles.yaml"])
    profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
except (OSError, ValueError, KeyError, TypeError) as exc:
    raise SystemExit("EXECUTION PREFLIGHT: FAIL " + str(exc))
profile = next((p for p in profiles if p["id"] == args.profile), None)
if profile is None:
    raise SystemExit(f"EXECUTION PREFLIGHT: FAIL unknown profile {args.profile}")
if args.phase not in profile.get("operations", {}).get(args.operation, []):
    raise SystemExit("EXECUTION PREFLIGHT: FAIL operation/phase not allowed")
try:
    verify_selected(ROOT, [*profile.get("required_core", []), *profile.get("required_machine", [])])
except (OSError, ValueError, KeyError, TypeError) as exc:
    raise SystemExit("EXECUTION PREFLIGHT: FAIL " + str(exc))
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
if (not isinstance(receipt, dict) or receipt.get("schema_version") != 6 or receipt.get("task_id") != args.task_id
        or receipt.get("release_sha256") != active["release_sha256"]
        or receipt.get("task_sha256") != hashlib.sha256(task_bytes).hexdigest()
        or receipt.get("routing_decision_sha256") != hashlib.sha256(decision_bytes).hexdigest()
        or receipt.get("profile_id") != args.profile
        or receipt.get("operation") != args.operation or receipt.get("phase") != args.phase):
    raise SystemExit("EXECUTION PREFLIGHT: FAIL receipt version, release, or task/profile identity")
if set(receipt) != {"schema_version", "task_id", "profile_id", "operation", "phase", "release_sha256", "task_sha256", "routing_decision_sha256", "task_started_at", "source_reads", "gate_checks", "condition_results", "evidence_mode", "evidence_bundle_sha256"}:
    raise SystemExit("EXECUTION PREFLIGHT: FAIL unknown or missing receipt field")

if receipt["evidence_mode"] not in {"coverage", "local_artifacts"}:
    raise SystemExit("EXECUTION PREFLIGHT: FAIL evidence mode")
if receipt["evidence_mode"] == "coverage" and (receipt["evidence_bundle_sha256"] is not None or args.evidence_bundle or args.artifact_root):
    raise SystemExit("EXECUTION PREFLIGHT: FAIL coverage cannot imply verified evidence")
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
    if set(record) - {"path", "kind", "read_ref", "observed_at", "library_file_id", "version_id", "version_status", "item_count", "content_sha256", "read_class", "activated_at", "reuse_reason"}:
        raise SystemExit("EXECUTION PREFLIGHT: FAIL source record unknown field")
    path, kind = record.get("path"), record.get("kind")
    if record.get("read_class") not in {"boot", "discovery", "hydration", "reused"}:
        raise SystemExit("EXECUTION PREFLIGHT: FAIL read class")
    if not isinstance(path, str) or path in read_paths or not record.get("read_ref"):
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL duplicate or unreferenced source {path}")
    expected_kind = "library_directory_list" if path.endswith("/") else "library_file_read"
    if kind != expected_kind:
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL source kind {path}")
    version_status, version_id = record.get("version_status"), record.get("version_id")
    valid_version = (version_status == "available" and isinstance(version_id, str) and bool(version_id)) or (version_status == "unavailable" and "version_id" in record and version_id is None)
    if kind == "library_file_read" and (not str(record.get("library_file_id", "")).startswith("libfile_")
                                        or not valid_version
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
        route_time = datetime.fromisoformat(decision["reviewed_at"].replace("Z", "+00:00"))
        if record["read_class"] == "hydration" and read_times[-1] < route_time:
            raise ValueError("hydration before route")
        if record["read_class"] == "reused":
            activated = datetime.fromisoformat(record["activated_at"].replace("Z", "+00:00"))
            if not record.get("reuse_reason") or not within_task(record["activated_at"]) or activated < max(route_time, read_times[-1]):
                raise ValueError("reuse activation")
            read_times.append(activated)
        elif "activated_at" in record or "reuse_reason" in record:
            raise ValueError("reuse metadata belongs only to reused reads")
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
expected_gates = set(profile["phase_gates"][args.phase])
unsatisfied = expected_gates - gate_ids
if gate_ids - expected_gates:
    raise SystemExit("EXECUTION PREFLIGHT: FAIL gate belongs to another phase")
if missing or unsatisfied:
    raise SystemExit(f"EXECUTION PREFLIGHT: FAIL missing_sources={sorted(missing)} unsupported_gates={sorted(unsatisfied)}")
media_action = profile.get("media_workflow", {}).get(args.phase, {}).get(args.operation)
if media_action:
    if not args.media_state:
        raise SystemExit("MEDIA WORKFLOW: FAIL --media-state required")
    try:
        from media_workflow import validate as validate_media
        media_bytes = args.media_state.read_bytes()
        check = next(c for c in checks if c["id"] == "media_workflow_ready")
        if check["evidence_ref"] != "sha256:" + hashlib.sha256(media_bytes).hexdigest():
            raise ValueError("receipt is not bound to current media state")
        validate_media(json.loads(media_bytes), media_action, args.task_id)
    except (OSError, ValueError, KeyError, TypeError, StopIteration, subprocess.SubprocessError) as exc:
        raise SystemExit("MEDIA WORKFLOW: FAIL " + str(exc))
    print("MEDIA WORKFLOW: LOCAL PROPERTIES PASS; external refs require authoritative evidence")
elif args.media_state:
    raise SystemExit("MEDIA WORKFLOW: FAIL state supplied to a non-media operation")
verification = None
if receipt["evidence_mode"] == "local_artifacts":
    if not args.evidence_bundle or not args.artifact_root:
        raise SystemExit("EXECUTION PREFLIGHT: FAIL evidence bundle/root required")
    try:
        bundle_bytes = args.evidence_bundle.read_bytes()
        if digest(bundle_bytes) != receipt["evidence_bundle_sha256"]:
            raise ValueError("evidence bundle digest")
        verification = verify_evidence(json.loads(bundle_bytes), receipt, args.artifact_root, ROOT)
    except (OSError, ValueError, KeyError, TypeError, subprocess.TimeoutExpired) as exc:
        raise SystemExit(f"EXECUTION PREFLIGHT: FAIL local evidence {exc}")
    if verification["unresolved_gates"]:
        raise SystemExit("LOCAL EVIDENCE: INCOMPLETE judgment/readback acceptance required " + str(verification["unresolved_gates"]))
    print("LOCAL ARTIFACT PROPERTIES: PASS; host authentication unavailable; model content use unproven")
print(f"STRUCTURAL READINESS: PASS\nPHASE RECEIPT: COVERAGE PASS profile={args.profile} operation={args.operation} phase={args.phase} task={args.task_id}")
print("SOURCE TRUTH: references require direct tool readback; receipt fields alone are not proof of content use")
