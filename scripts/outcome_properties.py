#!/usr/bin/env python3
"""Pure fixture/artifact oracles. They verify data, not remote ownership/acceptance."""
from pathlib import Path
import json
import math


def values_export(source, exported):
    if set(source) != {"columns", "rows"} or set(exported) != {"columns", "rows"}:
        return False
    if source != exported or not isinstance(source["rows"], list) or not source["columns"]:
        return False
    width = len(source["columns"])
    return all(isinstance(row, list) and len(row) == width and all(
        cell is None or type(cell) in (bool, int) or
        (type(cell) is float and math.isfinite(cell)) or
        (isinstance(cell, str) and not cell.lstrip().startswith(("=", "+", "@")))
        for cell in row) for row in source["rows"])


def stock_delta(before, after, operation):
    """A chosen lot changes once by the authorized fixture quantity; siblings remain."""
    if set(before) != set(after) or not isinstance(operation, dict) or any(type(v) is not int or v < 0 for v in before.values()):
        return False
    key, qty = operation.get("lot_id"), operation.get("quantity")
    if key not in before or type(qty) is not int or qty <= 0 or type(before[key]) is not int or before[key] < qty:
        return False
    return all(type(after[k]) is int and after[k] == before[k] - (qty if k == key else 0) for k in before)


def retry_allowed(journal, operation_key):
    matches = [r for r in journal if r.get("operation_key") == operation_key]
    # Missing outcome is not permission to replay a non-idempotent action.
    return bool(matches) and all(r.get("status") == "confirmed_no_effect" for r in matches)


def handoff(manifest, root):
    frames = manifest.get("frames")
    if not isinstance(frames, list) or not frames:
        return False
    root = Path(root).resolve()
    paths, ids = set(), set()
    for frame in frames:
        if not isinstance(frame, dict) or set(frame) != {"id", "path", "accepted", "sha256"}:
            return False
        p = (root / frame["path"]).resolve()
        if (not p.is_relative_to(root) or not p.is_file() or frame["id"] in ids or p in paths
                or frame["accepted"] is not True):
            return False
        from hashlib import sha256
        if sha256(p.read_bytes()).hexdigest() != frame["sha256"]:
            return False
        paths.add(p)
        ids.add(frame["id"])
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("method", choices=("values_export", "stock_delta", "retry_allowed", "handoff"))
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--artifact-root", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    if args.method == "handoff":
        if not args.artifact_root:
            parser.error("handoff requires artifact root")
        ok = handoff(data, args.artifact_root)
    else:
        ok = globals()[args.method](**data)
    print(json.dumps({"property": args.method, "passed": ok, "remote_origin": "unattested", "visual_identity": "not_evaluated"}))
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
