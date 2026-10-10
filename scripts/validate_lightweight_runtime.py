#!/usr/bin/env python3
"""Partial-workspace, selected-source tamper and interrupted-work regressions."""
from copy import deepcopy
from datetime import datetime, timezone, timedelta
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import yaml

from build_skill_catalog import build
from context_plan import plan, lifecycle
from selected_sources import verify_selected
from workstream_recovery import reconcile

ROOT = Path(__file__).resolve().parents[1]


def rejects(call):
    try:
        call()
    except (ValueError, KeyError, OSError):
        return
    raise AssertionError("invalid state accepted")


def copy_sources(root, names):
    for name in set(names):
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / name, target)


def partial_cases():
    catalog = yaml.safe_load((ROOT / "index/skill-catalog.yaml").read_text())
    assert catalog == build(ROOT), "catalog differs from active instruction metadata"
    assert all(s["status"] == "registered" for s in catalog["skills"].values())
    profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
    metadata = ["VERSION", "state/active-release.json", "state/release-manifest.json",
                "index/task-profiles.yaml", "context/budgets.yaml", "index/skill-catalog.yaml",
                "scripts/context_plan.py", "scripts/selected_sources.py"]
    count = 0
    for profile in profiles:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            names = metadata + profile["required_core"] + profile.get("required_machine", [])
            copy_sources(root, names)
            result = plan(profile["id"], root)
            assert result["selected_integrity"] == "pass" and result["full_integrity"] == "not_checked"
            assert len(list(root.rglob("*"))) < 100, "partial fixture became a full distribution"
            source = root / profile["required_core"][0]
            original = source.read_bytes()
            source.write_bytes(original + b"\nchanged")
            rejects(lambda: plan(profile["id"], root))
            source.unlink()
            rejects(lambda: plan(profile["id"], root))
            source.write_bytes(original)
            rejects(lambda: verify_selected(root, ["../escape"]))
            pointer = root / "state/active-release.json"
            data = json.loads(pointer.read_text())
            data["release_sha256"] = "0" * 64
            pointer.write_text(json.dumps(data))
            rejects(lambda: plan(profile["id"], root))
            count += 1
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        boot = ["VERSION", "state/active-release.json", "state/release-manifest.json",
                "core-manifest.yaml", "kernel/boot.yaml", "kernel/kernel.yaml", "kernel/session.yaml",
                "kernel/response.yaml", "index/routing.yaml", "state/checkpoint.yaml",
                "scripts/session_check.py", "scripts/selected_sources.py", "scripts/validate_core_contracts.py",
                "scripts/validate_route_decision.py", "scripts/profile_probe.py", "scripts/evidence.py"]
        copy_sources(root, boot)
        command = [sys.executable, str(root / "scripts/session_check.py")]
        result = subprocess.run(command, capture_output=True, text=True)
        assert result.returncode == 0 and "full inventory not checked" in result.stdout, result.stdout + result.stderr
        assert not (root / "validators").exists() and not (root / "skills").exists()
        (root / "kernel/session.yaml").write_text("tampered")
        result = subprocess.run(command, capture_output=True, text=True)
        assert result.returncode != 0 and "digest mismatch" in result.stdout + result.stderr, result.stdout + result.stderr
    normalized = lifecycle([{"path": "/DEDAL/private-overlay/lessons/example.md", "lifecycle": "active"}], ["lessons/example.md"])
    assert normalized["active"] == ["lessons/example.md"]
    rejects(lambda: lifecycle([{"path": "same"}, {"path": "/DEDAL/private-overlay/same"}], ["same"]))
    print(f"LIGHTWEIGHT: {count} partial profile workspaces pass; missing/tampered sources and pointer drift rejected; boot needs 16 files, not full tree")


def recovery_cases():
    now = datetime.now(timezone.utc)
    checkpoint = {"schema_version": 1, "task_id": "interrupted-unit", "updated_at": now.isoformat(),
                  "pending_operations": [{"id": "write-1", "owner": "fixture-owner", "target": "exact-object",
                                          "retry_safe": False, "expected_result": {"sha256": "a" * 64}}]}
    observation = {"operation_id": "write-1", "task_id": checkpoint["task_id"], "owner": "fixture-owner",
                   "target": "exact-object", "observed_at": now.isoformat(), "evidence_ref": "fixture-readback",
                   "outcome": "expected_result_present", "actual_result": {"sha256": "a" * 64}}
    action = lambda cp, obs: reconcile(cp, obs)["decisions"][0]["action"]
    assert action(checkpoint, [observation]) == "accept_observed_result_no_replay"
    assert action(checkpoint, []) == "read_authoritative_owner"
    assert action(checkpoint, [{**observation, "outcome": "unknown"}]) == "read_authoritative_owner"
    assert action(checkpoint, [{**observation, "outcome": "conflict"}]) == "reconcile_conflict_no_replay"
    assert action(checkpoint, [{**observation, "outcome": "confirmed_no_effect"}]) == "review_retry_safety"
    safe = deepcopy(checkpoint)
    safe["pending_operations"][0]["retry_safe"] = True
    assert action(safe, [{**observation, "outcome": "confirmed_no_effect"}]) == "retry_after_current_authority_check"
    for change in [{"task_id": "another-unit"}, {"target": "other"}, {"owner": "other"}, {"evidence_ref": ""},
                   {"observed_at": (now - timedelta(seconds=1)).isoformat()},
                   {"actual_result": {"sha256": "b" * 64}}, {"outcome": "claimed_success"}]:
        rejects(lambda: reconcile(checkpoint, [{**observation, **change}]))
    rejects(lambda: reconcile(checkpoint, [observation, observation]))
    print("RECOVERY: lost acknowledgement, absence, unknown/conflict, stale/wrong-task/target/owner/result and duplicate evidence cases pass")


if __name__ == "__main__":
    partial_cases()
    recovery_cases()
