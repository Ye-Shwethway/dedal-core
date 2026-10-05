#!/usr/bin/env python3
"""Protected local outcome probes. Unsupported baseline checks are never failures.

Freeze this grader outside the candidate before running. No model or live-service
quality inference is made from fixture outcomes.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import yaml


def tree_hash(root):
    files = json.loads((root / "core-files.json").read_text())["files"]
    return hashlib.sha256(json.dumps({p: hashlib.sha256((root/p).read_bytes()).hexdigest() for p in files}, sort_keys=True).encode()).hexdigest()


def probe(root, case, td):
    root = root.resolve()
    method = case["method"]
    if method in {"values_export", "stock_delta", "retry_allowed", "handoff"}:
        script = root / "scripts/outcome_properties.py"
        if not script.exists():
            return {"status": "unsupported", "reason": "baseline_has_no_owned_deterministic_oracle"}
        input_file = td / "input.json"
        input_file.write_text(json.dumps(case["input"]))
        command = [sys.executable, str(script), method, "--input", str(input_file)]
        if method == "handoff":
            command += ["--artifact-root", str(td)]
        r = subprocess.run(command, capture_output=True, timeout=60)
        actual = r.returncode == 0
    elif method == "context":
        profiles = yaml.safe_load((root / "index/task-profiles.yaml").read_text())["profiles"]
        profile = next(p for p in profiles if p["id"] == "core-architecture-change")
        actual = all((root/p).is_file() for p in profile["required_core"])
        full_bytes = sum((root/p).stat().st_size for p in profile["required_core"])
        machine_bytes = sum((root/p).stat().st_size for p in profile.get("required_machine", []))
        return {"status": "pass" if actual else "fail", "full_content_bytes": full_bytes, "machine_bytes": machine_bytes}
    elif method == "receipt":
        # Build current-release fixtures under each implementation's own receipt schema.
        from datetime import datetime, timezone, timedelta
        now = datetime.now(timezone.utc)
        stamp = now.isoformat()
        profiles = yaml.safe_load((root / "index/task-profiles.yaml").read_text())["profiles"]
        profile = next(p for p in profiles if p["id"] == "core-architecture-change")
        active = json.loads((root/"state/active-release.json").read_text())
        task = b"Review DEDAL Core schema"
        route = {"schema_version": 1, "task_id": "protected-case", "task_sha256": hashlib.sha256(task).hexdigest(),
                 "release_sha256": active["release_sha256"], "lexical_candidates": [profile["id"]],
                 "decision": "select_profile", "selected_profile": profile["id"], "basis": "lexical_confirmation",
                 "rationale": "Core refinement is the current task.", "reviewed_at": stamp}
        route_bytes = json.dumps(route).encode()
        schema = json.loads((root/"state/hydration-receipt.schema.json").read_text())["properties"]["schema_version"]["const"]
        reads, events = [], []
        for i, path in enumerate(profile["required_core"]):
            observed = (now-timedelta(seconds=1)).isoformat() if case["variant"] == "early_hydration" and i == 0 else stamp
            raw = (root/path).read_bytes()
            name = f"source-{i}"
            (td/name).write_bytes(raw)
            record = {"path": path, "kind": "library_file_read", "read_ref": name, "observed_at": observed,
                      "library_file_id": "libfile_fixture", "version_id": None, "version_status": "unavailable", "content_sha256": hashlib.sha256(raw).hexdigest()}
            if schema >= 6:
                record["read_class"] = "hydration"
            reads.append(record)
            events.append({**record, "id": name, "kind": "source_read", "artifact": name, "full_read": True, "size_bytes": len(raw)})
        gates = [{"id": g, "evidence_ref": g, "passed": True, "observed_at": stamp} for g in profile["phase_gates"]["execute"]]
        (td/"rollback.json").write_text(json.dumps({"ordered_write_set": [{"path": "fixture"}], "rollback_rule": "Restore exact baseline"}))
        for g in gates:
            event = {"id": g["id"], "kind": "gate", "gate_id": g["id"], "observed_at": stamp}
            if g["id"] == "validator_green":
                event.update(method="command", command="validators/validate_core.py")
            else:
                event.update(method="artifact", artifact="rollback.json", sha256=hashlib.sha256((td/"rollback.json").read_bytes()).hexdigest())
                if case["variant"] == "missing_evidence":
                    event["artifact"] = "missing.json"
                if case["variant"] == "digest_corruption":
                    event["sha256"] = "0" * 64
            events.append(event)
        bundle = {"schema_version": 1, "task_id": "protected-case", "release_sha256": active["release_sha256"], "events": events}
        bundle_bytes = json.dumps(bundle).encode()
        receipt = {"schema_version": schema, "task_id": "protected-case", "task_started_at": (now-timedelta(seconds=2)).isoformat(),
                   "profile_id": profile["id"], "operation": "change", "phase": "execute", "source_reads": reads,
                   "gate_checks": gates, "condition_results": {}, "release_sha256": active["release_sha256"],
                   "task_sha256": hashlib.sha256(task).hexdigest(), "routing_decision_sha256": hashlib.sha256(route_bytes).hexdigest()}
        if schema >= 6:
            receipt.update(evidence_mode="local_artifacts", evidence_bundle_sha256=hashlib.sha256(bundle_bytes).hexdigest())
        (td/"task.txt").write_bytes(task)
        (td/"route.json").write_bytes(route_bytes)
        (td/"receipt.json").write_text(json.dumps(receipt))
        (td/"events.json").write_bytes(bundle_bytes)
        command = [sys.executable, str(root/"scripts/session_check.py"), "--profile", profile["id"], "--operation", "change", "--phase", "execute",
                   "--task-id", "protected-case", "--task-file", str(td/"task.txt"), "--route-decision", str(td/"route.json"), "--receipt", str(td/"receipt.json")]
        if schema >= 6:
            command += ["--evidence-bundle", str(td/"events.json"), "--artifact-root", str(td)]
        r = subprocess.run(command, capture_output=True, timeout=60)
        actual = r.returncode == 0
    else:
        raise ValueError("unknown protected case")
    return {"status": "pass" if actual == case["expected"] else "fail", "accepted": actual,
            "output_sha256": hashlib.sha256(r.stdout+r.stderr).hexdigest(),
            "output": (r.stdout+r.stderr).decode(errors="replace")[:1500]}


def run(baseline, candidate, suite, trials):
    before = {"baseline": tree_hash(baseline), "candidate": tree_hash(candidate)}
    results = []
    for case in suite["cases"]:
        for trial in range(trials):
            for name, root in [("baseline", baseline), ("candidate", candidate)]:
                with tempfile.TemporaryDirectory() as directory:
                    td = Path(directory)
                    for filename, content in suite.get("artifacts", {}).items():
                        (td/filename).write_text(content)
                    started = time.perf_counter()
                    result = probe(root, case, td)
                    result.update(case=case["id"], family=case["family"], trial=trial+1, implementation=name,
                                  local_elapsed_ms=round((time.perf_counter()-started)*1000, 3))
                    results.append(result)
    assert before == {"baseline": tree_hash(baseline), "candidate": tree_hash(candidate)}, "implementation mutated during evaluation"
    return {"kind": "controlled_contract_and_artifact_outcome_comparison", "frozen_tree_hashes": before,
            "grader_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "suite_sha256": hashlib.sha256(json.dumps(suite, sort_keys=True).encode()).hexdigest(),
            "trials_per_case": trials, "results": results, "model_trials": "unavailable",
            "model_corrections": None, "tokens": None, "cost": None, "visual_quality": "not_evaluated",
            "live_side_effects": "none", "general_performance_gain": "not_established",
            "unsupported_baseline_checks": "reported_separately_never_counted_as_failures"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--suite", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--trials", type=int, default=2)
    args = parser.parse_args()
    if args.trials < 1 or args.output.resolve().is_relative_to(args.candidate.resolve()):
        parser.error("positive trials and output outside candidate required")
    args.output.write_text(json.dumps(run(args.baseline, args.candidate, json.loads(args.suite.read_text()), args.trials), indent=2)+"\n")
