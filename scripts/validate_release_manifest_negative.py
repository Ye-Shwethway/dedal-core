#!/usr/bin/env python3
"""Ensure digest drift and pointer tampering fail before boot readiness."""
from pathlib import Path
import shutil
import tempfile

from validate_release_manifest import ROOT, validate

assert validate(ROOT) == []
with tempfile.TemporaryDirectory() as directory:
    copy = Path(directory) / "core"
    shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns("__pycache__"))
    target = copy / "index/routing.yaml"
    target.write_text(target.read_text() + "\n# drift\n")
    assert any(e.startswith("release_digest_mismatch:index/routing.yaml") for e in validate(copy))
    shutil.copy2(ROOT / "index/routing.yaml", target)
    pointer = copy / "state/active-release.json"
    pointer.write_text(pointer.read_text().replace("release_sha256", "wrong_key"))
    assert "release_identity_or_pointer_mismatch" in validate(copy)
print("RELEASE NEGATIVES: PASS drift and pointer tampering rejected")
