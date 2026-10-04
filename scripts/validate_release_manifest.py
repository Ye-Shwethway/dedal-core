#!/usr/bin/env python3
"""Validate the active direct-tree release and every inventoried file digest."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"state/release-manifest.json", "state/active-release.json"}


def validate(root=ROOT):
    errors = []
    active = json.loads((root / "state/active-release.json").read_text())
    release_bytes = (root / "state/release-manifest.json").read_bytes()
    release = json.loads(release_bytes)
    inventory = json.loads((root / "core-files.json").read_text())
    actual = {str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()
              and "__pycache__" not in p.parts and ".git" not in p.parts}
    expected = set(inventory["files"])
    hashes = release.get("files", {})
    digest = hashlib.sha256(release_bytes).hexdigest()
    version = (root / "VERSION").read_text().strip()
    if (active.get("schema_version") != 1 or release.get("schema_version") != 1
            or active.get("core_version") != version or release.get("core_version") != version
            or active.get("release_sha256") != digest or active.get("release_manifest") != "state/release-manifest.json"
            or release.get("algorithm") != "sha256"):
        errors.append("release_identity_or_pointer_mismatch")
    if expected != actual or set(hashes) != expected - EXCLUDED:
        errors.append("release_file_set_mismatch")
    for path, sha in hashes.items():
        file = root / path
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != sha:
            errors.append(f"release_digest_mismatch:{path}")
    return errors


if __name__ == "__main__":
    try:
        errors = validate()
    except (OSError, ValueError, KeyError) as exc:
        errors = [f"release_unavailable:{exc}"]
    if errors:
        print("RELEASE CONSISTENCY: FAIL", *errors, sep="\n- ")
        sys.exit(1)
    print("RELEASE CONSISTENCY: PASS all inventoried file digests and active pointer")
