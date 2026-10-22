#!/usr/bin/env python3
"""Plan disclosure after verifying only metadata and the selected source closure."""
import argparse
import json
from pathlib import Path
import time
import yaml
from selected_sources import ReleaseSnapshot

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"retired", "retired_historical", "historical", "historical_closed", "archived", "superseded", "duplicate", "trash", "legacy_unclassified"}


def lifecycle(resources, selected):
    def normalize(path):
        return path.removeprefix("/DEDAL/private-overlay/")
    by_path = {}
    for record in resources:
        path = normalize(record["path"])
        if path in by_path:
            raise ValueError("duplicate private resource identity: " + path)
        by_path[path] = record
    active, blocked, review = [], [], []
    for path in selected:
        record = by_path.get(normalize(path))
        status = record.get("lifecycle") if record else None
        if status in EXCLUDED:
            blocked.append(path)
        elif status in {"active", "current"}:
            active.append(path)
        else:
            review.append(path)
    return {"active": active, "blocked": blocked, "review_required": review}


def plan(profile_id, root=ROOT, phase="execute", conditions=None):
    started = time.perf_counter()
    root = Path(root)
    snapshot = ReleaseSnapshot(root)
    snapshot.verify(["index/task-profiles.yaml", "context/budgets.yaml", "index/skill-catalog.yaml",
                           "scripts/context_plan.py", "scripts/selected_sources.py"])
    profiles = yaml.safe_load(snapshot.contents["index/task-profiles.yaml"])["profiles"]
    profile = next((p for p in profiles if p["id"] == profile_id), None)
    if profile is None:
        raise ValueError("unknown task profile")
    if phase not in profile["phase_gates"]:
        raise ValueError("unknown phase")
    branches = profile.get("conditional_core", [])
    names = {b["when"] for b in branches}
    if conditions is not None and (set(conditions) != names or any(type(v) is not bool for v in conditions.values())):
        raise ValueError("all conditional Core branches require explicit boolean decisions")
    read_paths = list(profile["required_core"])
    if conditions is not None:
        read_paths += [s for b in branches if conditions[b["when"]] for s in b["sources"]]
    read_paths = list(dict.fromkeys(read_paths))
    machine_paths = profile.get("required_machine", [])
    catalog = yaml.safe_load(snapshot.contents["index/skill-catalog.yaml"])["skills"]
    for skill in [profile["primary"], *profile.get("supporting", [])]:
        if skill not in catalog or catalog[skill]["entrypoint"] not in read_paths:
            raise ValueError("selected skill missing from catalog/dependency closure: " + skill)
    integrity = snapshot.verify([*read_paths, *machine_paths])
    snapshot.assert_current()
    sizes = {p: len(snapshot.contents[p]) for p in read_paths}
    budget = yaml.safe_load(snapshot.contents["context/budgets.yaml"])["observable_limits"]["profile_content_bytes"]
    result = {"schema_version": 1, "profile_id": profile_id, "phase": phase,
            "release_sha256": snapshot.active["release_sha256"], "read_full": sizes,
            "machine_verified": machine_paths, "required_private": profile.get("required_private", []),
            "conditional_private": profile.get("conditional_private", []),
            "conditional_core": profile.get("conditional_core", []),
            "conditional_resolution": "pending" if names and conditions is None else "resolved_declarations",
            "phase_gates": profile["phase_gates"][phase], "content_bytes": sum(sizes.values()),
            "machine_file_bytes": sum(len(snapshot.contents[p]) for p in machine_paths),
            "byte_budget": budget, "budget_status": "within" if sum(sizes.values()) <= budget else "exception_reason_required",
            "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
            "tokens": None, "cost": None, "full_integrity": "not_checked",
            "integrity_scope": integrity["integrity_scope"], "selected_integrity": "pass",
            "boundary": "read_full remains mandatory; machine verification is not a content-read claim"}
    return measure_disclosure(result)


def measure_disclosure(result):
    """Budget full source bodies plus this canonical compact UTF-8 envelope."""
    result["plan_bytes"] = 0
    result["disclosure_bytes"] = 0
    for _ in range(20):
        size = len(json.dumps(result, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
        total = result["content_bytes"] + size
        status = "within" if total <= result["byte_budget"] else "exception_reason_required"
        if (result["plan_bytes"], result["disclosure_bytes"], result["budget_status"]) == (size, total, status):
            return result
        result.update(plan_bytes=size, disclosure_bytes=total, budget_status=status)
    raise ValueError("disclosure measurement did not converge")


def skill_plan(skill_id, root=ROOT):
    root = Path(root)
    snapshot = ReleaseSnapshot(root)
    snapshot.verify(["index/skill-catalog.yaml", "scripts/context_plan.py", "scripts/selected_sources.py"])
    catalog = yaml.safe_load(snapshot.contents["index/skill-catalog.yaml"])["skills"]
    if skill_id not in catalog:
        raise ValueError("unknown registered skill")
    paths = [catalog[skill_id]["entrypoint"], "kernel/execution.yaml"]
    result = snapshot.verify(paths)
    snapshot.assert_current()
    return {"skill_id": skill_id, "read_full": result["verified"], "selected_integrity": "pass",
            "execution_readiness": "unverified_resolve_task_references_and_domain_gates",
            "full_integrity": "not_checked"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--profile")
    choice.add_argument("--skill")
    parser.add_argument("--phase", choices=("inspect", "execute", "close"), default="execute")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--budget-reason", help="Concrete correctness reason when mandatory full reads exceed observable byte limit")
    parser.add_argument("--private-manifest", type=Path)
    parser.add_argument("--private-path", action="append", default=[])
    parser.add_argument("--conditions", type=Path, help="JSON boolean decisions for every conditional Core branch")
    args = parser.parse_args()
    if args.skill:
        if args.private_path:
            parser.error("resolve skill-private context through the current owner")
        print(json.dumps(skill_plan(args.skill), indent=2))
        raise SystemExit(0)
    result = plan(args.profile, phase=args.phase, conditions=json.loads(args.conditions.read_text()) if args.conditions else None)
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
    result = measure_disclosure(result)
    if result["budget_status"] != "within" and not args.budget_reason:
        parser.exit(1, "Mandatory disclosure budget exceeded; provide a correctness reason\n")
    data = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(data)
    else:
        print(data, end="")
