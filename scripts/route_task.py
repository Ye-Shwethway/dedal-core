#!/usr/bin/env python3
"""Propose lexical candidates; a separate task-bound semantic decision activates one."""
import argparse
import json
from pathlib import Path

import yaml

from profile_probe import probe

ROOT = Path(__file__).resolve().parents[1]


def route(task, profiles):
    result = probe(task, profiles)
    candidates = [p for p in profiles if p["id"] in result["profiles"]]
    return {**result, "candidate_compositions": [
                {"profile_id": p["id"], "primary": p["primary"], "supporting": p.get("supporting", [])}
                for p in candidates],
            "primary": None, "supporting": [], "activation": "blocked_until_semantic_decision",
            "next": "semantic_review"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True)
    args = parser.parse_args()
    profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
    print(json.dumps(route(args.task, profiles), ensure_ascii=False))
