#!/usr/bin/env python3
"""Reconcile resumable single-root publication from fresh identity/hash snapshots.

This coordinator emits guarded requests. Library transport and fresh readback are
explicit adapters; no remote atomicity or always-on host hook is assumed.
"""
import argparse
import hashlib
import json
from pathlib import Path
import os
import tempfile


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(dir=path.parent, prefix=".journal-")
    try:
        with os.fdopen(fd, "w") as handle:
            json.dump(value, handle, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        if Path(name).exists():
            Path(name).unlink()


def prepare(before, after, metadata):
    before, after = Path(before).resolve(), Path(after).resolve()
    old = json.loads((before / "core-files.json").read_text())["files"]
    new = json.loads((after / "core-files.json").read_text())["files"]
    if set(old) - set(new):
        raise ValueError("removal requires an explicit archival migration")
    by_path = {m["path"].removeprefix("/DEDAL/core/"): m for m in metadata}
    entries = []
    for p in new:
        prior = sha(before / p) if p in old else None
        candidate = sha(after / p)
        if prior == candidate:
            continue
        if p in old and p not in by_path:
            raise ValueError("existing identity missing")
        m = by_path.get(p, {})
        entries.append({"path": p, "library_file_id": m.get("library_file_id"),
                        "prior_version": m.get("version_id"), "prior_sha256": prior,
                        "candidate_sha256": candidate, "candidate_path": str(after / p),
                        "prior_path": str(before / p) if prior else None})
    entries.sort(key=lambda e: (e["path"] == "state/active-release.json", e["path"] == "state/release-manifest.json", e["path"]))
    return {"schema_version": 1, "status": "update_in_progress", "from_version": (before / "VERSION").read_text().strip(),
            "to_version": (after / "VERSION").read_text().strip(), "ordered_write_set": entries,
            "outcomes": [], "rollback_rule": "Fresh snapshot, prior source bytes, prior manifest, prior pointer last; archive newly created canonical nodes by their observed identities before accepting rollback.",
            "authority": "single_direct_core_tree", "atomic": False}


def reconcile(journal, snapshot, direction="forward"):
    if direction not in {"forward", "rollback"} or not isinstance(snapshot, dict):
        raise ValueError("invalid direction/snapshot")
    pending, done, conflicts = [], [], []
    created = {o["path"]: o.get("library_file_id") for o in journal["outcomes"] if o.get("status") == "succeeded"}
    for e in journal["ordered_write_set"]:
        actual = snapshot.get(e["path"])
        expected_id = e["library_file_id"] or created.get(e["path"])
        if actual and expected_id and actual.get("library_file_id") != expected_id:
            conflicts.append(e["path"])
            continue
        # Unknown-success creates must be rediscovered and independently reconciled.
        if actual and not expected_id:
            conflicts.append(e["path"])
            continue
        current = actual.get("sha256") if actual else None
        target = e["candidate_sha256"] if direction == "forward" else e["prior_sha256"]
        other = e["prior_sha256"] if direction == "forward" else e["candidate_sha256"]
        if current == target:
            done.append(e["path"])
        elif current == other:
            pending.append(e["path"])
        else:
            conflicts.append(e["path"])
    return {"done": done, "pending": pending, "conflicts": conflicts,
            "status": "conflict" if conflicts else ("bytes_complete" if not pending else "update_in_progress")}


def request(journal, snapshot, stage, direction="forward", directory_ids=None):
    state = reconcile(journal, snapshot, direction)
    if state["conflicts"]:
        raise ValueError("publication conflict: " + repr(state["conflicts"]))
    groups = {"source": [e for e in journal["ordered_write_set"] if e["path"] not in {"state/release-manifest.json", "state/active-release.json"}],
              "manifest": [e for e in journal["ordered_write_set"] if e["path"] == "state/release-manifest.json"],
              "pointer": [e for e in journal["ordered_write_set"] if e["path"] == "state/active-release.json"]}
    order = ["source", "manifest", "pointer"]
    if stage not in order:
        raise ValueError("unknown stage")
    previous = [e["path"] for s in order[:order.index(stage)] for e in groups[s]]
    if set(previous) - set(state["done"]):
        raise ValueError("earlier stage requires fresh verified readback")
    uploads, archives = [], []
    for e in groups[stage]:
        if e["path"] not in state["pending"]:
            continue
        actual = snapshot.get(e["path"])
        if direction == "rollback" and e["prior_sha256"] is None:
            archives.append({"path": e["path"], "library_file_id": actual["library_file_id"], "operation": "archive_created_node_outside_canonical_root"})
            continue
        local_path = e["candidate_path"] if direction == "forward" else e["prior_path"]
        wanted = e["candidate_sha256"] if direction == "forward" else e["prior_sha256"]
        if sha(local_path) != wanted:
            raise ValueError("frozen local bytes changed")
        item = {"local_path": local_path, "purpose": "replace_library_file" if actual else "create_library_file"}
        if actual:
            item["library_file_id"] = actual["library_file_id"]
            if actual.get("version_id") is not None:
                item["expected_current_version"] = int(actual["version_id"])
            item["version_reason"] = "DEDAL reconciled publication " + direction
        else:
            parent = str(Path(e["path"]).parent)
            if not directory_ids or parent not in directory_ids:
                raise ValueError("new file requires resolved destination folder")
            item["directory_id"] = directory_ids[parent]
            item["library_artifact_type"] = "other"
        uploads.append(item)
    return {"uploads": uploads, "archives": archives, "direction": direction, "stage": stage,
            "weaker_concurrency": [e["path"] for e in groups[stage] if snapshot.get(e["path"], {}).get("version_id") is None and e["path"] in state["pending"]]}


def record(journal, results):
    by_local = {e["candidate_path"]: e for e in journal["ordered_write_set"]}
    by_local.update({e["prior_path"]: e for e in journal["ordered_write_set"] if e["prior_path"]})
    failed = False
    for result in results:
        entry = by_local.get(result.get("local_path"))
        if not entry:
            raise ValueError("unmatched transport result")
        journal["outcomes"].append({"path": entry["path"], "status": result.get("status", "unknown"),
                                    "library_file_id": result.get("library_file_id"), "version_id": result.get("current_version_number")})
        if result.get("status") != "succeeded":
            failed = True
    journal["status"] = "readback_required_after_failure" if failed else "readback_required"
    return not failed


def adopt_created(journal, snapshot, path):
    """Adopt an explicitly resolved unique canonical identity after unknown create success."""
    entry = next(e for e in journal["ordered_write_set"] if e["path"] == path)
    actual = snapshot.get(path)
    if entry["prior_sha256"] is not None or entry["library_file_id"] is not None or not actual or not actual.get("library_file_id") or actual.get("sha256") != entry["candidate_sha256"]:
        raise ValueError("create adoption lacks exact identity/content readback")
    journal["outcomes"].append({"path": path, "status": "succeeded", "library_file_id": actual["library_file_id"],
                                "version_id": actual.get("version_id"), "origin": "explicit_unique_readback_reconciliation_not_transport_ack"})
    journal["status"] = "readback_required"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("prepare", "reconcile", "request", "record", "adopt"))
    parser.add_argument("--journal", type=Path, required=True)
    parser.add_argument("--before", type=Path)
    parser.add_argument("--after", type=Path)
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--results", type=Path)
    parser.add_argument("--directories", type=Path)
    parser.add_argument("--stage", choices=("source", "manifest", "pointer"))
    parser.add_argument("--direction", choices=("forward", "rollback"), default="forward")
    parser.add_argument("--path", help="Exact newly created canonical path resolved uniquely from current metadata")
    args = parser.parse_args()
    load = lambda p: json.loads(p.read_text())
    try:
        if args.action == "prepare":
            save(args.journal, prepare(args.before, args.after, load(args.metadata)))
        else:
            journal = load(args.journal)
            if args.action == "adopt":
                adopt_created(journal, load(args.snapshot), args.path)
                save(args.journal, journal)
            elif args.action == "record":
                ok = record(journal, load(args.results)["results"])
                save(args.journal, journal)
                if not ok:
                    raise ValueError("transport failed; stop and obtain fresh readback")
            elif args.action == "reconcile":
                print(json.dumps(reconcile(journal, load(args.snapshot), args.direction), indent=2))
            else:
                print(json.dumps(request(journal, load(args.snapshot), args.stage, args.direction,
                                         load(args.directories) if args.directories else None), indent=2))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.exit(1, str(exc) + "\n")
