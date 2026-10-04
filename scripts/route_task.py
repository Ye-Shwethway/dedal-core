#!/usr/bin/env python3
"""Resolve an explicit task profile without guessing on ambiguity or semantic gaps."""
import argparse
import json
from pathlib import Path

import yaml

from profile_probe import probe

ROOT = Path(__file__).resolve().parents[1]


def route(task, profiles):
    result = probe(task, profiles)
    if result["status"] != "matched":
        return {**result, "primary": None, "supporting": [],
                "next": "semantic_review" if result["status"] == "ambiguous" else "bounded_skill_search_or_semantic_review"}
    profile = next(p for p in profiles if p["id"] == result["profiles"][0])
    return {**result, "primary": profile["primary"],
            "supporting": profile.get("supporting", []),
            "required_core": profile.get("required_core", []),
            "required_private": profile.get("required_private", []),
            "execution_gates": profile.get("execution_gates", []),
            "next": "hydrate_and_verify"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True)
    args = parser.parse_args()
    profiles = yaml.safe_load((ROOT / "index/task-profiles.yaml").read_text())["profiles"]
    print(json.dumps(route(args.task, profiles), ensure_ascii=False))
