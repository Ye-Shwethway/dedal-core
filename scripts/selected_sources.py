#!/usr/bin/env python3
"""Verify a release pointer and a selected working set without scanning the tree."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re


def safe_name(name):
    if (not isinstance(name, str) or not name or "\\" in name
            or PurePosixPath(name).is_absolute() or ".." in PurePosixPath(name).parts
            or str(PurePosixPath(name)) != name):
        raise ValueError("invalid Core source path: " + repr(name))


def safe_path(root, name):
    safe_name(name)
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError("Core source escapes root: " + name)
    return path


def release_identity(root):
    root = Path(root)
    active_bytes = (root / "state/active-release.json").read_bytes()
    active = json.loads(active_bytes)
    data = (root / "state/release-manifest.json").read_bytes()
    release = json.loads(data)
    if (not isinstance(active, dict) or not isinstance(release, dict)
            or active.get("schema_version") != 1 or release.get("schema_version") != 1
            or active.get("release_manifest") != "state/release-manifest.json"
            or release.get("algorithm") != "sha256"
            or not re.fullmatch(r"\d+\.\d+\.\d+", str(active.get("core_version", "")))
            or release.get("core_version") != active["core_version"]
            or hashlib.sha256(data).hexdigest() != active.get("release_sha256")):
        raise ValueError("release identity or pointer mismatch")
    hashes = release.get("files")
    if not isinstance(hashes, dict) or not hashes:
        raise ValueError("release source digest map missing")
    for name, digest in hashes.items():
        safe_name(name)
        if not re.fullmatch(r"[0-9a-f]{64}", str(digest)):
            raise ValueError("invalid source digest: " + name)
    expected = {**hashes, "state/release-manifest.json": active["release_sha256"],
                "state/active-release.json": hashlib.sha256(active_bytes).hexdigest()}
    version = root / "VERSION"
    if ("VERSION" not in hashes or hashlib.sha256(version.read_bytes()).hexdigest() != hashes["VERSION"]
            or version.read_text().strip() != active["core_version"]):
        raise ValueError("release VERSION mismatch")
    return active, expected


class ReleaseSnapshot:
    """One operation only; verified bytes are not a cross-task or persistent cache."""
    def __init__(self, root):
        self.root = Path(root)
        self.active, self.expected = release_identity(self.root)
        self.contents = {}

    def verify(self, paths):
        verified = {}
        for name in dict.fromkeys(paths):
            path = safe_path(self.root, name)
            if name not in self.expected:
                raise ValueError("source outside accepted release: " + name)
            try:
                data = path.read_bytes()
            except OSError as exc:
                raise ValueError("required source unavailable: " + name) from exc
            if hashlib.sha256(data).hexdigest() != self.expected[name]:
                raise ValueError("selected source digest mismatch: " + name)
            self.contents[name] = data
            verified[name] = len(data)
        return {"release_sha256": self.active["release_sha256"],
                "core_version": self.active["core_version"], "verified": verified,
                "integrity_scope": "selected_sources", "full_integrity": "not_checked"}

    def assert_current(self):
        active, expected = release_identity(self.root)
        if active != self.active or expected != self.expected:
            raise ValueError("release changed during selected-source operation")


def verify_selected(root, paths):
    """Hash only selected files; absent/unrelated development sources are irrelevant."""
    snapshot = ReleaseSnapshot(root)
    result = snapshot.verify(paths)
    snapshot.assert_current()
    return result
