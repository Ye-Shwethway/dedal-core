#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
contract = json.loads((ROOT / "evals/infrastructure-engineering-routing/contract-v1.json").read_text())

expected = {
    "IE-01": "infrastructure-engineering",
    "IE-02": "infrastructure-engineering",
    "IE-03": "software-development",
    "IE-04": "release-engineering",
    "IE-05": "reliability-engineering",
    "IE-06": "cloudflare-platform",
    "IE-07": "security-engineering",
    "IE-08": "database-engineering",
}

cases = {c["id"]: c for c in contract["cases"]}
for cid, primary in expected.items():
    assert cases[cid]["expect_primary"] == primary, (cid, cases[cid])

for cid in ["IE-N1", "IE-N2", "IE-N3", "IE-N4", "IE-N5", "IE-N6"]:
    assert cases[cid].get("reject") is True, cid

assert "infrastructure-engineering" in cases["IE-02"].get("expect_primary", "")
assert "security-engineering" in cases["IE-02"].get("expect_supporting", [])
assert "infrastructure-engineering" in cases["IE-07"].get("expect_supporting", [])

skill = (ROOT / "skills/infrastructure-engineering/SKILL.md").read_text()
for phrase in [
    "configuration, state, and live provider reality",
    "A speculative plan is not an applied change",
    "auto-approve",
    "Direct state mutation",
    "reliability-engineering",
    "cloudflare-platform",
]:
    assert phrase in skill, phrase

print("Infrastructure Engineering routing contract: OK")
