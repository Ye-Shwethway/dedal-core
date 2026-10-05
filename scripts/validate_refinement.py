#!/usr/bin/env python3
"""Fault injection and negative checks for evidence, publication and disclosure."""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import tempfile
import yaml
from evidence import verify, digest
from context_plan import plan, lifecycle
from publication import prepare, reconcile, request, record, save, adopt_created
from outcome_properties import values_export, stock_delta, retry_allowed, handoff

ROOT = Path(__file__).resolve().parents[1]


def rejects(call):
    try:
        call()
    except (ValueError, KeyError, OSError):
        return
    raise AssertionError("invalid state accepted")


def evidence_cases():
    now = datetime.now(timezone.utc).isoformat()
    with tempfile.TemporaryDirectory() as td:
        p = Path(td)
        (p / "source.txt").write_text("complete current source")
        raw = (p / "source.txt").read_bytes()
        source = {"path": "example", "kind": "library_file_read", "read_ref": "source", "library_file_id": "libfile_test",
                  "version_id": None, "version_status": "unavailable", "content_sha256": digest(raw), "observed_at": now}
        event = {**source, "id": "source", "kind": "source_read", "artifact": "source.txt", "full_read": True, "size_bytes": len(raw)}
        receipt = {"task_id": "test", "release_sha256": "a" * 64, "source_reads": [source], "gate_checks": [], "condition_results": {}}
        bundle = {"schema_version": 1, "task_id": "test", "release_sha256": "a" * 64, "events": [event]}
        assert verify(bundle, receipt, p, ROOT)["host_authentication"] == "unavailable"
        for change in [{"artifact": "missing"}, {"artifact": "../outside"}, {"full_read": False}, {"size_bytes": len(raw)-1}, {"version_id": "1"}, {"path": "other"}]:
            rejects(lambda: verify({**bundle, "events": [{**event, **change}]}, receipt, p, ROOT))
        rejects(lambda: verify({**bundle, "events": [event, event]}, receipt, p, ROOT))
        check = {"id": "creator_publishing_authority_confirmed", "evidence_ref": "gate", "passed": True, "observed_at": now}
        gate = {"id": "gate", "kind": "gate", "gate_id": check["id"], "method": "creator_acceptance", "artifact": "source.txt", "observed_at": now}
        r = {**receipt, "gate_checks": [check]}
        b = {**bundle, "events": [event, gate]}
        assert verify(b, r, p, ROOT)["unresolved_gates"]
        rejects(lambda: verify({**b, "events": [event, {**gate, "method": "command", "command": "scripts/build_release_manifest.py"}]}, r, p, ROOT))
        rejects(lambda: verify({**b, "events": [event]}, r, p, ROOT))
        print("Evidence: full/null reads, six corruptions, duplicates, missing refs and forged authority rejected")


def publication_cases():
    with tempfile.TemporaryDirectory() as td:
        p = Path(td)
        before, after = p / "before", p / "after"
        files = ["a.txt", "b.txt", "core-files.json", "state/release-manifest.json", "state/active-release.json", "VERSION"]
        for root, value in [(before, "old"), (after, "new")]:
            (root / "state").mkdir(parents=True)
            for f in files:
                (root / f).write_text(value)
            (root / "core-files.json").write_text(json.dumps({"files": files}))
        metadata = [{"path": "/DEDAL/core/" + f, "library_file_id": "libfile_" + str(i), "version_id": "1"} for i, f in enumerate(files)]
        journal = prepare(before, after, metadata)
        entries = journal["ordered_write_set"]
        snapshot = {e["path"]: {"library_file_id": e["library_file_id"], "version_id": "1", "sha256": e["prior_sha256"]} for e in entries}
        rejects(lambda: request(journal, snapshot, "pointer"))
        # Crash both before and after every mutation. Readback drives progress, not acknowledgements.
        trials = 0
        for cut in range(len(entries) + 1):
            for lose_ack in (False, True):
                snap = deepcopy(snapshot)
                j = deepcopy(journal)
                for e in entries[:cut]:
                    snap[e["path"]]["sha256"] = e["candidate_sha256"]
                    snap[e["path"]]["version_id"] = "2"
                    if not lose_ack:
                        record(j, [{"local_path": e["candidate_path"], "status": "succeeded", "library_file_id": e["library_file_id"], "current_version_number": 2}])
                state = reconcile(j, snap)
                assert len(state["done"]) == cut and not state["conflicts"]
                for stage in ("source", "manifest", "pointer"):
                    req = request(j, snap, stage)
                    for u in req["uploads"]:
                        e = next(e for e in entries if e["candidate_path"] == u["local_path"])
                        snap[e["path"]]["sha256"] = e["candidate_sha256"]
                assert reconcile(j, snap)["status"] == "bytes_complete"
                for stage in ("source", "manifest", "pointer"):
                    req = request(j, snap, stage, "rollback")
                    for u in req["uploads"]:
                        e = next(e for e in entries if e["prior_path"] == u["local_path"])
                        snap[e["path"]]["sha256"] = e["prior_sha256"]
                assert reconcile(j, snap, "rollback")["status"] == "bytes_complete"
                trials += 1
        corrupted = deepcopy(snapshot)
        first = entries[0]
        corrupted[first["path"]]["sha256"] = "f" * 64
        rejects(lambda: request(journal, corrupted, "source"))
        corrupted[first["path"]]["sha256"] = first["prior_sha256"]
        corrupted[first["path"]]["library_file_id"] = "libfile_other"
        rejects(lambda: request(journal, corrupted, "source"))
        assert not record(journal, [{"local_path": first["candidate_path"], "status": "failed"}])
        rejects(lambda: request(journal, snapshot, "pointer"))
        save(p / "journal.json", journal)
        assert json.loads((p / "journal.json").read_text())["status"] == "readback_required_after_failure"
        (after / "new.txt").write_text("new owned file")
        (after / "core-files.json").write_text(json.dumps({"files": files + ["new.txt"]}))
        create_journal = prepare(before, after, metadata)
        new_entry = next(e for e in create_journal["ordered_write_set"] if e["path"] == "new.txt")
        original = {e["path"]: {"library_file_id": e["library_file_id"], "version_id": "1", "sha256": e["prior_sha256"]} for e in create_journal["ordered_write_set"] if e["prior_sha256"] is not None}
        dirs = {".": "resolved-test-folder"}
        created_request = request(create_journal, original, "source", directory_ids=dirs)
        assert any(u["purpose"] == "create_library_file" for u in created_request["uploads"])
        original["new.txt"] = {"library_file_id": "libfile_created", "version_id": "0", "sha256": new_entry["candidate_sha256"]}
        assert reconcile(create_journal, original)["conflicts"] == ["new.txt"]
        adopt_created(create_journal, original, "new.txt")
        assert "new.txt" in reconcile(create_journal, original)["done"]
        rollback = request(create_journal, original, "source", "rollback")
        assert rollback["archives"][0]["library_file_id"] == "libfile_created"
        print(f"Publication: {trials} crash/ack-loss resume+rollback trials; drift/identity/early-pointer rejected")


def context_cases():
    profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
    registry = yaml.safe_load((ROOT / "index/SKILL_REGISTRY.yaml").read_text())["skills"]
    for profile in profiles:
        p = plan(profile["id"])
        assert p["full_integrity"] == "pass" and p["tokens"] is None and p["cost"] is None
        assert registry[profile["primary"]]["entrypoint"] in p["read_full"]
        assert not set(p["read_full"]) & set(p["machine_verified"])
    result = lifecycle([{"path": "current", "lifecycle": "current"}, {"path": "old", "lifecycle": "retired"}, {"path": "unknown"}], ["current", "old", "unknown", "missing"])
    assert result == {"active": ["current"], "blocked": ["old"], "review_required": ["unknown", "missing"]}
    print("Context: seven full-entrypoint plans; retired/unknown lifecycle filtered without cache claims")


if __name__ == "__main__":
    evidence_cases()
    publication_cases()
    context_cases()
    print("REFINEMENT: PASS")
