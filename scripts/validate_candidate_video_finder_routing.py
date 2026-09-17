#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
errors = []


def require(path, needle, label):
    text = (ROOT / path).read_text(encoding="utf-8")
    if needle not in text:
        errors.append(f"{label}: missing {needle!r} in {path}")


for path in [
    "skills/candidate-video-finder/SKILL.md",
    "skills/candidate-video-finder/ADAPTATION_NOTES.md",
    "skills/candidate-video-finder/references/candidate-record-and-gates.md",
    "skills/candidate-video-finder/references/discovery-evidence-and-risk.md",
    "skills/candidate-video-finder/references/handoffs-and-learning.md",
    "evals/candidate-video-finder/contract-v1.json",
]:
    if not (ROOT / path).exists():
        errors.append(f"missing {path}")

require("index/MASTER_INDEX.md", "Candidate Video Finder", "master index")
require("index/SKILL_REGISTRY.yaml", "candidate-video-finder:", "machine registry")
require("state/routing-boundaries.json", '"candidate-video-boundary"', "routing boundary")
require("skills/candidate-video-finder/SKILL.md", "specific bounded scene", "candidate atom")
require("skills/candidate-video-finder/SKILL.md", "Creator selection", "creator authority")
require("skills/candidate-video-finder/SKILL.md", "Candidate Finder has no publication or channel-mutation authority", "mutation boundary")
require("skills/candidate-video-finder/SKILL.md", "copyright safe", "risk certainty guard")
require("skills/candidate-video-finder/SKILL.md", "private operational overlay", "private learning boundary")
require("skills/video-production/references/scene-and-action-boundary-extraction.md", "locator evidence, not canonical cut authority", "production cut boundary")
require("skills/youtube-seo/SKILL.md", "YouTube SEO owns discovery research", "seo downstream boundary")
require("skills/youtube-publishing/SKILL.md", "YouTube SEO owns", "publishing ownership boundary")

contract = json.loads((ROOT / "evals/candidate-video-finder/contract-v1.json").read_text(encoding="utf-8"))
if len(contract.get("cases", [])) < 10:
    errors.append("candidate-video-finder contract must contain at least 10 cases")
ids = [c.get("id") for c in contract.get("cases", [])]
if len(ids) != len(set(ids)):
    errors.append("candidate-video-finder contract has duplicate case ids")

if errors:
    print("FAIL")
    for err in errors:
        print("-", err)
    raise SystemExit(1)
print(f"PASS: candidate-video-finder routing contract; {len(contract['cases'])} cases")
