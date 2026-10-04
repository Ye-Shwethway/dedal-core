#!/usr/bin/env python3
"""Validate the complete direct Library Core tree and its machine contracts."""
from pathlib import Path
import json
import subprocess
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
errors = []

def load(path):
    file = ROOT / path
    if not file.is_file():
        errors.append(f"missing:{path}")
        return {}
    try:
        return json.loads(file.read_text()) if file.suffix == ".json" else yaml.safe_load(file.read_text()) or {}
    except (ValueError, yaml.YAMLError) as exc:
        errors.append(f"parse:{path}:{exc}")
        return {}

version_file = ROOT / "VERSION"
version = version_file.read_text().strip() if version_file.is_file() else None
if not version:
    errors.append("missing:VERSION")
manifest = load("core-manifest.yaml")
paths = ["kernel/boot.yaml", "kernel/kernel.yaml", "kernel/session.yaml",
         "kernel/state-boundary.yaml", "index/routing.yaml",
         "index/task-profiles.yaml", "index/SKILL_REGISTRY.yaml",
         "index/document-schema.yaml",
         "state/checkpoint.yaml", "state/current-checkpoint.json",
         "context/budgets.yaml", "state/hydration-receipt.schema.json",
         "state/routing-decision.schema.json",
         "core-files.json"]
obj = {p: load(p) for p in paths}
boot, kernel, session = (obj[p] for p in ("kernel/boot.yaml", "kernel/kernel.yaml", "kernel/session.yaml"))
profiles = obj["index/task-profiles.yaml"]
registry = obj["index/SKILL_REGISTRY.yaml"]
checkpoint = obj["state/checkpoint.yaml"]
inventory = obj["core-files.json"]

for path, data in [("core-manifest.yaml", manifest), *obj.items()]:
    if path in ("core-files.json", "index/SKILL_REGISTRY.yaml"):
        continue
    if data.get("version", data.get("core_version")) not in (None, version):
        errors.append(f"version_drift:{path}")
if manifest.get("canonical_root") != "/DEDAL/core" or boot.get("canonical_root") != "/DEDAL/core":
    errors.append("canonical_root_drift")
if manifest.get("archive_boot") != "forbidden" or manifest.get("external_runtime_mcp") != "retired":
    errors.append("authority_policy_drift")
if checkpoint.get("accepted", {}).get("canonical_core") != "/DEDAL/core":
    errors.append("checkpoint_boot_drift")
if checkpoint.get("accepted", {}).get("boot_surface") != "ChatGPT Library direct tree":
    errors.append("checkpoint_surface_drift")
if obj["state/current-checkpoint.json"].get("version") != version:
    errors.append("machine_checkpoint_version_drift")
if not any(x.get("id") == "read_checkpoint" and x.get("required") for x in session.get("start", [])):
    errors.append("session_missing_checkpoint")
if session.get("execution_readiness", {}).get("no_receipt") != "fail_closed":
    errors.append("execution_receipt_guard_missing")
if session.get("execution_readiness", {}).get("route_decision_schema") != "state/routing-decision.schema.json":
    errors.append("session_route_decision_pointer_drift")
if manifest.get("hydration_receipt_schema") != "state/hydration-receipt.schema.json":
    errors.append("receipt_schema_pointer_drift")
if manifest.get("routing_decision_schema") != "state/routing-decision.schema.json":
    errors.append("route_decision_schema_pointer_drift")
if manifest.get("document_schema") != "index/document-schema.yaml":
    errors.append("document_schema_pointer_drift")
if manifest.get("active_release") != "state/active-release.json" or manifest.get("release_manifest") != "state/release-manifest.json":
    errors.append("release_pointer_drift")
allowed = {"verify_release", "load_sources", "load_checkpoint", "load_private_manifest", "resolve_state",
           "compose", "resolve_profile", "hydrate", "apply_rule"}
for step in boot.get("boot_sequence", []):
    if not step.get("id") or step.get("kind") not in allowed:
        errors.append(f"boot_step_invalid:{step}")
    for path in step.get("sources", []):
        if not (ROOT / path).is_file():
            errors.append(f"boot_missing_ref:{path}")
for ref in ("session_protocol", "kernel_contract", "routing_policy", "task_profiles", "checkpoint"):
    if not (ROOT / str(boot.get(ref, ""))).is_file():
        errors.append(f"boot_missing_ref:{ref}")
for entry in kernel.get("invariants", []):
    if not entry.get("id") or entry.get("enforce") not in ("reasoning", "validator") or not entry.get("spec"):
        errors.append(f"invalid_invariant:{entry}")

ids = set()
for profile in profiles.get("profiles", []):
    pid = profile.get("id")
    if not pid or pid in ids:
        errors.append(f"duplicate_profile:{pid}")
    ids.add(pid)
    match = profile.get("match", {})
    if not isinstance(match, dict) or not any(match.get(k) for k in ("all", "any")):
        errors.append(f"profile_match_missing:{pid}")
    for key in ("all", "any"):
        terms = match.get(key, [])
        if not isinstance(terms, list) or any(not isinstance(term, str) or not term.strip() for term in terms):
            errors.append(f"profile_match_invalid:{pid}:{key}")
    for path in profile.get("required_core", []):
        if not (ROOT / path).is_file():
            errors.append(f"profile_missing_ref:{pid}:{path}")
for name, skill in registry.get("skills", {}).items():
    if skill.get("status") == "active" and not (ROOT / skill.get("entrypoint", "")).is_file():
        errors.append(f"skill_missing_entrypoint:{name}")

files = inventory.get("files", [])
if inventory.get("schema_version") != 1 or not files or len(files) != len(set(files)):
    errors.append("inventory_invalid")
if inventory.get("core_version") != version:
    errors.append("inventory_version_drift")
for path in files:
    if path.startswith("/") or ".." in Path(path).parts or not (ROOT / path).is_file():
        errors.append(f"inventory_missing:{path}")
actual = {str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file()
          and "__pycache__" not in p.parts and ".git" not in p.parts}
if set(files) != actual:
    errors.append(f"inventory_mismatch:missing={len(set(files)-actual)} untracked={len(actual-set(files))}")
for path in ("kernel/boot.yaml", "kernel/kernel.yaml", "kernel/session.yaml",
             "index/routing.yaml", "index/task-profiles.yaml", "state/checkpoint.yaml"):
    text = (ROOT / path).read_text().lower() if (ROOT / path).is_file() else ""
    if "mcp__dedal_runtime" in text or "mcp__dedal_python_canary" in text:
        errors.append(f"external_runtime_dependency:{path}")
    if "/dedal/repo-mirror/dedal-core-current.zip" in text:
        errors.append(f"archive_boot_dependency:{path}")
if not errors:
    check = subprocess.run([sys.executable, str(ROOT / "scripts/validate_release_manifest.py")], capture_output=True, text=True)
    if check.returncode:
        errors.append("release_consistency:" + check.stdout.strip().replace("\n", "; "))
if errors:
    print("DEDAL CORE VALIDATION: FAIL")
    for error in errors:
        print("-", error)
    sys.exit(1)
print(f"DEDAL CORE VALIDATION: PASS version={version} files={len(files)} profiles={len(ids)}")
