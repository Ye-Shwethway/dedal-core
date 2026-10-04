#!/usr/bin/env python3
"""Conservative lexical probe; unresolved tasks require semantic profile review."""
import argparse
import json
from pathlib import Path
import re
import unicodedata

import yaml

ROOT = Path(__file__).resolve().parents[1]

def normalize(value):
    value = unicodedata.normalize("NFKC", value).casefold()
    value = re.sub(r"[-_→–—/]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()

def contains(task, phrase):
    term = normalize(phrase)
    return bool(re.search(r"(?<!\w)" + re.escape(term) + r"(?!\w)", task))

def probe(task, profiles):
    normalized = normalize(task)
    matches = []
    for profile in profiles:
        rule = profile.get("match", {})
        every = rule.get("all", [])
        some = rule.get("any", [])
        if (all(contains(normalized, term) for term in every)
                and (not some or any(contains(normalized, term) for term in some))):
            matches.append(profile["id"])
    status = "unresolved" if not matches else ("ambiguous" if len(matches) > 1 else "matched")
    return {"status": status, "profiles": matches, "scope": "lexical_probe_only"}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True)
    args = parser.parse_args()
    profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
    print(json.dumps(probe(args.task, profiles), ensure_ascii=False))
