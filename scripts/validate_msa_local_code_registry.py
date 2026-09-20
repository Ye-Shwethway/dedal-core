#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def validate_contract() -> None:
    data = json.loads((ROOT / "evals" / "medicine-store-assistant" / "local-code-registry-v1.json").read_text(encoding="utf-8"))
    ids = [c.get("id") for c in data.get("cases", [])]
    required = {"not-row-id","same-identity-multi-lot","different-identity-unique","monotonic-no-reuse","registry-before-new-code","not-cms-evidence","cms-replacement-lineage","historical-snapshot-preserved","checkpoint-audit-readback"}
    if not ids or len(ids) != len(set(ids)) or required - set(ids):
        raise AssertionError("MSA local-code contract cases invalid")
    skill = (ROOT / "skills" / "medicine-store-assistant" / "SKILL.md").read_text(encoding="utf-8")
    system = (ROOT / "skills" / "medicine-store-assistant" / "references" / "system-contract.md").read_text(encoding="utf-8")
    cms = (ROOT / "skills" / "medicine-store-assistant" / "references" / "cms-price-and-matching.md").read_text(encoding="utf-8")
    local = (ROOT / "skills" / "medicine-store-assistant" / "references" / "local-code-registry.md").read_text(encoding="utf-8")
    archive = (ROOT / "skills" / "medicine-store-assistant" / "references" / "master-data-archive-contract.md").read_text(encoding="utf-8")
    for text, snippet in [
        (skill,"local-code-registry.md"),
        (system,"Local fallback identifiers are not CMS identities"),
        (cms,"persistent local fallback identifier"),
        (local,"One local code = one local identity for life."),
        (local,"never reassigned to another identity"),
        (local,"REPLACED_BY_CMS"),
        (local,"does not prove CMS catalogue identity"),
        (archive,"do not retroactively rewrite the older closed-month snapshot")
    ]:
        if snippet not in text:
            raise AssertionError(f"missing MSA local-code snippet: {snippet}")

def main() -> int:
    validate_contract()
    print("MSA local-code registry contract: valid")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
