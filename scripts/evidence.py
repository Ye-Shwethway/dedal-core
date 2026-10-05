#!/usr/bin/env python3
"""Verify local evidence properties; never authenticate self-authored observations."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def digest(data):
    return hashlib.sha256(data).hexdigest()


def resolve(root, name):
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise ValueError("artifact path must be relative")
    root = Path(root).resolve()
    path = (root / name).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise ValueError("missing or escaped artifact")
    return path


def verify(bundle, receipt, artifact_root, core_root):
    """Return verifiable local properties and explicit unresolved judgment gates."""
    if (not isinstance(bundle, dict) or set(bundle) != {"schema_version", "task_id", "release_sha256", "events"}
            or bundle.get("schema_version") != 1 or bundle.get("task_id") != receipt["task_id"]
            or bundle.get("release_sha256") != receipt["release_sha256"] or not isinstance(bundle.get("events"), list)):
        raise ValueError("evidence bundle identity/shape")
    events = {}
    for event in bundle["events"]:
        if not isinstance(event, dict) or not isinstance(event.get("id"), str) or event["id"] in events:
            raise ValueError("duplicate or invalid event")
        events[event["id"]] = event
    properties, unresolved, used = [], [], set()
    for record in receipt["source_reads"]:
        event = events.get(record["read_ref"])
        if not event or event.get("kind") != "source_read" or event.get("path") != record["path"]:
            raise ValueError("source event missing or path mismatch")
        used.add(event["id"])
        if record["kind"] != "library_file_read":
            raise ValueError("directory coverage is not full-content verification")
        raw = resolve(artifact_root, event.get("artifact")).read_bytes()
        if event.get("full_read") is not True or event.get("size_bytes") != len(raw) or digest(raw) != record["content_sha256"]:
            raise ValueError("source content incomplete or digest mismatch")
        for key in ("library_file_id", "version_id", "version_status", "observed_at"):
            if key not in event or event[key] != record[key]:
                raise ValueError("source observation metadata mismatch")
        properties.append({"id": event["id"], "property": "complete_local_bytes_match_receipt", "origin": "unattested_observation"})
    for check in receipt["gate_checks"]:
        event = events.get(check["evidence_ref"])
        if not event or event.get("kind") != "gate" or event.get("gate_id") != check["id"] or event.get("observed_at") != check["observed_at"]:
            raise ValueError("gate event missing or binding mismatch")
        used.add(event["id"])
        method = event.get("method")
        if method == "command":
            # Only pure validation commands. No shell, arbitrary argv, or mutators.
            name = event.get("command")
            allowed = {"validators/validate_core.py", "scripts/validate_release_manifest.py", "scripts/validate_core_contracts.py"}
            if name not in allowed or check["id"] != "validator_green":
                raise ValueError("command does not verify this gate")
            result = subprocess.run([sys.executable, str(Path(core_root) / name)], cwd=core_root,
                                    capture_output=True, timeout=60)
            if result.returncode:
                raise ValueError("validator command failed")
            properties.append({"id": event["id"], "property": "current_validator_exit_zero", "output_sha256": digest(result.stdout + result.stderr)})
        elif method == "artifact":
            raw = resolve(artifact_root, event.get("artifact")).read_bytes()
            if digest(raw) != event.get("sha256"):
                raise ValueError("gate artifact digest mismatch")
            if check["id"] == "rollback_path_recorded":
                obj = json.loads(raw)
                if not isinstance(obj.get("ordered_write_set"), list) or not obj["ordered_write_set"] or not obj.get("rollback_rule"):
                    raise ValueError("rollback plan missing")
                property_name = "rollback_plan_record_present"
            elif check["id"] == "checkpoint_updated":
                expected = Path(core_root) / "state/checkpoint.yaml"
                if raw != expected.read_bytes():
                    raise ValueError("checkpoint does not match current Core")
                property_name = "current_checkpoint_bytes_match"
            else:
                # A manifest or picture's existence does not establish its truth.
                unresolved.append({"id": check["id"], "reason": "artifact_presence_does_not_verify_domain_property"})
                continue
            properties.append({"id": event["id"], "property": property_name})
        elif method in {"authoritative_readback", "visual_review", "creator_acceptance"}:
            # The host exposes no authenticated event adapter. Preserve the observation.
            resolve(artifact_root, event.get("artifact"))
            unresolved.append({"id": check["id"], "reason": "requires_authoritative_tool_or_reviewer_acceptance"})
        else:
            raise ValueError("unknown evidence method")
    for name, condition in receipt.get("condition_results", {}).items():
        event = events.get(condition["evidence_ref"])
        if not event or event.get("kind") != "condition" or event.get("condition") != name or event.get("applies") != condition["applies"] or event.get("observed_at") != condition["observed_at"]:
            raise ValueError("condition event missing or binding mismatch")
        used.add(event["id"])
        resolve(artifact_root, event.get("artifact"))
        unresolved.append({"id": name, "reason": "condition_semantics_require_current_task_review"})
    if set(events) != used:
        raise ValueError("unused evidence event")
    return {"properties": properties, "unresolved_gates": unresolved,
            "host_authentication": "unavailable", "model_content_use": "not_proven"}
