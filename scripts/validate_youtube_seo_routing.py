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
    "skills/youtube-seo/SKILL.md",
    "skills/youtube-seo/ADAPTATION_NOTES.md",
    "skills/youtube-seo/references/evidence-and-opportunity-model.md",
    "skills/youtube-seo/references/mvp-workflows.md",
    "evals/youtube-seo/contract-v1.json",
]:
    if not (ROOT / path).exists():
        errors.append(f"missing {path}")

require("index/MASTER_INDEX.md", "YouTube SEO", "master index")
require("index/SKILL_REGISTRY.yaml", "youtube-seo:", "machine registry")
require("state/routing-boundaries.json", '"youtube-discovery-boundary"', "routing boundary")
require("skills/youtube-publishing/SKILL.md", "YouTube SEO owns", "publishing boundary")
require("skills/youtube-seo/SKILL.md", "Do not turn missing data into fake precision", "truth gate")
require("skills/youtube-seo/SKILL.md", "OWNED_FIRST_PARTY", "evidence classes")
require("skills/youtube-seo/SKILL.md", "Search, Browse, Suggested", "surface model")

contract = json.loads((ROOT / "evals/youtube-seo/contract-v1.json").read_text(encoding="utf-8"))
if len(contract.get("cases", [])) < 8:
    errors.append("youtube-seo contract must contain at least 8 cases")

# Public/private leakage is enforced repo-wide by validate_public_repo_privacy.py.
# This validator checks YouTube-SEO structure/ownership only, avoiding private sentinel values in public source.

if errors:
    print("FAIL")
    for err in errors:
        print("-", err)
    raise SystemExit(1)
print(f"PASS: youtube-seo routing contract; {len(contract['cases'])} cases")
