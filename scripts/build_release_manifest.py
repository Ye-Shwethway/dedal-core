#!/usr/bin/env python3
"""Generate deterministic digests, then activate the release pointer last."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"state/release-manifest.json", "state/active-release.json"}
inventory = json.loads((ROOT / "core-files.json").read_text())
version = (ROOT / "VERSION").read_text().strip()
assert "core_version" not in inventory, "inventory is release-independent"
files = inventory["files"]
actual = sorted(str(p.relative_to(ROOT)) for p in ROOT.rglob("*") if p.is_file()
                and "__pycache__" not in p.parts and ".git" not in p.parts)
assert files == actual, "inventory must be complete and sorted before release generation"
hashes = {path: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for path in files if path not in EXCLUDED}
release = {"schema_version": 1, "core_version": version, "algorithm": "sha256", "files": hashes}
data = (json.dumps(release, indent=2, ensure_ascii=False) + "\n").encode()
(ROOT / "state/release-manifest.json").write_bytes(data)
active = {"schema_version": 1, "core_version": version,
          "release_manifest": "state/release-manifest.json",
          "release_sha256": hashlib.sha256(data).hexdigest()}
(ROOT / "state/active-release.json").write_text(json.dumps(active, indent=2) + "\n")
print(f"release activated: {version} files={len(files)} sha256={active['release_sha256']}")
