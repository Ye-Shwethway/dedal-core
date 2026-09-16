#!/usr/bin/env python3
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "evals/youtube-publishing-hardening/contract-v1.json"
SKILL = ROOT / "skills/youtube-publishing/SKILL.md"
REFERENCE = ROOT / "skills/youtube-publishing/references/mutation-hardening-and-recovery.md"
CHECKPOINT = ROOT / "skills/youtube-publishing/CURRENT_CHECKPOINT.md"
MACHINE = ROOT / "state/current-checkpoint.json"
VERSION = ROOT / "VERSION"

required_cases = {f"YT-HARD-{i:02d}" for i in range(1, 10)}
contract = json.loads(CONTRACT.read_text())
actual_cases = {case["id"] for case in contract["cases"]}
if actual_cases != required_cases:
    raise SystemExit(f"case coverage mismatch: {sorted(actual_cases)}")

combined = "\n".join(p.read_text() for p in [SKILL, REFERENCE, CHECKPOINT])
required_phrases = [
    "managed baseline",
    "delete -> insert",
    "rollback",
    "fail closed",
    "caption",
    "banner",
    "watermark",
    "stage-aware D1 mutation audit",
    "one bounded retry",
    "read back",
]
missing = [p for p in required_phrases if p.lower() not in combined.lower()]
if missing:
    raise SystemExit(f"missing hardening phrases: {missing}")

machine = json.loads(MACHINE.read_text())
version = VERSION.read_text().strip()
if machine.get("version") != version:
    raise SystemExit(f"checkpoint version {machine.get('version')} != VERSION {version}")

if machine["next_executable_step"]["id"] not in {"YOUTUBE-SOURCE-SYNC-01", "YOUTUBE-PUBLIC-SOURCE-OUTCOME-01"}:
    raise SystemExit("unexpected next checkpoint")

for path in [CONTRACT, SKILL, REFERENCE, CHECKPOINT, MACHINE]:
    text = path.read_text()
    banned_value_patterns = [
        r'Bearer\s+[A-Za-z0-9._~-]{20,}',
        r'AIza[0-9A-Za-z_-]{20,}',
        r'ya29\.[0-9A-Za-z._-]{20,}',
        r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    ]
    for pattern in banned_value_patterns:
        if re.search(pattern, text):
            raise SystemExit(f"possible secret material in {path}: {pattern}")

print("youtube publishing hardening contract: PASS")
print(f"cases: {len(actual_cases)}")
print(f"version: {version}")
