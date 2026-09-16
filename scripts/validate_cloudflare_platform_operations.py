#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "evals" / "cloudflare-platform-operations" / "contract-v1.json"
REF = ROOT / "skills" / "cloudflare-platform" / "references" / "worker-deployment-and-connector-recovery.md"
SKILL = ROOT / "skills" / "cloudflare-platform" / "SKILL.md"


def main() -> int:
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    if len(cases) != 8:
        raise AssertionError("cloudflare operations contract requires 8 cases")
    ids = [case.get("id") for case in cases]
    if ids != [f"CFOP-{i:02d}" for i in range(1, 9)]:
        raise AssertionError("cloudflare operations contract case coverage/order mismatch")
    for case in cases:
        expect = case.get("expect", [])
        if not case.get("intent") or len(expect) < 3 or len(expect) != len(set(expect)):
            raise AssertionError(f"{case.get('id')}: incomplete/duplicate expectations")

    ref = REF.read_text(encoding="utf-8")
    skill = SKILL.read_text(encoding="utf-8")
    required_ref_phrases = [
        "Do not assume they are byte-identical",
        "manual source editing is especially a last resort",
        "do **not** blindly retry",
        "bounded chunk retrieval",
        "remote MCP/Gateway as the source of tool semantics",
    ]
    for phrase in required_ref_phrases:
        if phrase not in ref:
            raise AssertionError(f"missing Cloudflare operational rule: {phrase}")
    required_skill_phrases = [
        "Verify execution-surface fidelity",
        "Automate before delegating manual edits",
        "Never overwrite a newer live Worker with stale repository source",
    ]
    for phrase in required_skill_phrases:
        if phrase not in skill:
            raise AssertionError(f"missing Cloudflare skill rule: {phrase}")

    print("cloudflare platform operations: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
