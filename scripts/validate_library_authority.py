#!/usr/bin/env python3
"""Validate direct Core authority and optional private routing metadata."""
import argparse
import json
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--overlay-manifest", type=Path)
parser.add_argument("--state-registry", type=Path)
parser.add_argument("--repo-manifest", type=Path)
args = parser.parse_args()
errors = []
manifest = yaml.safe_load((ROOT / "core-manifest.yaml").read_text())
checkpoint = yaml.safe_load((ROOT / "state/checkpoint.yaml").read_text())
inventory = json.loads((ROOT / "core-files.json").read_text())
version = (ROOT / "VERSION").read_text().strip()
if (manifest.get("canonical_root") != "/DEDAL/core" or checkpoint.get("accepted", {}).get("canonical_core") != "/DEDAL/core"
        or manifest.get("core_version") != version or inventory.get("core_version") != version):
    errors.append("core authority/version drift")
if checkpoint.get("accepted", {}).get("migration_status") != "direct_tree_verified":
    errors.append("migration status not verified")
if args.overlay_manifest:
    overlay = json.loads(args.overlay_manifest.read_text())
    boot = overlay.get("boot", {})
    if (boot.get("core_root") != "/DEDAL/core"
            or boot.get("core_manifest") != "/DEDAL/core/core-manifest.yaml"
            or "/DEDAL/repo-mirror/" in json.dumps(boot)):
        errors.append("overlay boot points outside direct Core")
if args.state_registry:
    registry = json.loads(args.state_registry.read_text())
    policy = registry.get("root_policy", {})
    if (registry.get("canonical_roots", {}).get("core") != "/DEDAL/core/"
            or any(k in policy for k in ("canonical_core_zip", "canonical_snapshot", "canonical_repo_manifest"))):
        errors.append("registry active root/sync metadata drift")
if args.repo_manifest:
    mirror = json.loads(args.repo_manifest.read_text())
    if (mirror.get("direct_core_root") != "/DEDAL/core" or mirror.get("core_version") != version
            or mirror.get("file_count") != len(inventory["files"])
            or mirror.get("expected_github_head") != manifest.get("recorded_github_base")):
        errors.append("Git sync metadata contradicts direct Core")
if errors:
    print("LIBRARY AUTHORITY: FAIL", *errors, sep="\n- ")
    sys.exit(1)
print("LIBRARY AUTHORITY: PASS direct Core and supplied metadata")
