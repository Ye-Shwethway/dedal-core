#!/usr/bin/env python3
"""Build a small disclosure plan after full local release verification."""
import argparse
import json
from pathlib import Path
import time
import yaml
from validate_release_manifest import validate

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"retired", "retired_historical", "historical", "historical_closed", "archived", "superseded", "duplicate", "trash", "legacy_unclassified"}


def lifecycle(resources, selected):
    by_path = {r["path"]: r for r in resources}
    active, blocked, review = [], [], []
    for path in selected:
        record = by_path.get(path)
        status = record.get("lifecycle") if record else None
        if status in EXCLUDED:
            blocked.append(path)
        elif status in {"active", "current"}:
            active.append(path)
        else:
            review.append(path)
    return {"active": active, "blocked": blocked, "review_required": review}


def plan(profile_id, root=ROOT, phase="execute"):
    started = time.perf_counter()
    root = Path(root)
    errors = validate(root)
    if errors:
        raise ValueError("release verification failed: " + repr(errors))
    profiles = yaml.safe_load((root / "index/task-profiles.yaml").read_text())["profiles"]
    profile = next(p for p in profiles if p["id"] == profile_id)
    if phase not in profile["phase_gates"]:
        raise ValueError("unknown phase")
    read_paths = profile["required_core"]
    machine_paths = profile.get("required_machine", [])
    active = json.loads((root / "state/active-release.json").read_text())
    sizes = {p: (root / p).stat().st_size for p in read_paths}
    budget = yaml.safe_load((root / "context/budgets.yaml").read_text())["observable_limits"]["profile_content_bytes"]
    return {"schema_version": 1, "profile_id": profile_id, "phase": phase,
            "release_sha256": active["release_sha256"], "read_full": sizes,
            "machine_verified": machine_paths, "required_private": profile.get("required_private", []),
            "conditional_private": profile.get("conditional_private", []),
            "phase_gates": profile["phase_gates"][phase], "content_bytes": sum(sizes.values()),
            "machine_file_bytes": sum((root / p).stat().st_size for p in machine_paths),
            "byte_budget": budget, "budget_status": "within" if sum(sizes.values()) <= budget else "exception_reason_required",
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
            "tokens": None, "cost": None, "full_integrity": "pass",
            "boundary": "read_full remains mandatory; machine verification is not a content-read claim"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    parser.add_argument("--phase", choices=("inspect", "execute", "close"), default="execute")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--budget-reason", help="Concrete correctness reason when mandatory full reads exceed observable byte limit")
    parser.add_argument("--private-manifest", type=Path)
    parser.add_argument("--private-path", action="append", default=[])
    args = parser.parse_args()
    result = plan(args.profile, phase=args.phase)
    if result["budget_status"] == "exception_reason_required":
        if not args.budget_reason or not args.budget_reason.strip():
            parser.exit(1, "Mandatory read budget exceeded; provide a correctness reason without omitting sources\n")
        result["budget_exception_reason"] = args.budget_reason
    if args.private_path:
        if not args.private_manifest:
            parser.error("private selection requires authoritative current manifest")
        manifest = json.loads(args.private_manifest.read_text())
        selected = [p.removeprefix("/DEDAL/private-overlay/") for p in args.private_path]
        result["private_lifecycle"] = lifecycle(manifest["resources"], selected)
        if result["private_lifecycle"]["blocked"] or result["private_lifecycle"]["review_required"]:
            parser.exit(1, json.dumps(result["private_lifecycle"]) + "\n")
    data = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(data)
    else:
        print(data, end="")
