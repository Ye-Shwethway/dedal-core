#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate_contract() -> None:
    contract_path = ROOT / "evals" / "medicine-store-assistant" / "master-data-archive-contract-v1.json"
    data = json.loads(contract_path.read_text(encoding="utf-8"))
    cases = data.get("cases", [])
    ids = [case.get("id") for case in cases]
    required = {
        "archive-role-not-operational",
        "values-only-snapshot",
        "archive-before-cleanup",
        "append-existing-archive",
        "explicit-projection-map",
        "schema-evolution-no-invention",
        "duplicate-month-guard",
        "explicit-amendment",
        "month-boundary-structural",
        "history-no-double-count",
        "desktop-gate-only-when-unreconciled",
    }
    if not cases or len(ids) != len(set(ids)):
        raise AssertionError("MSA Master Data contract requires non-empty unique case ids")
    missing = sorted(required - set(ids))
    if missing:
        raise AssertionError(f"MSA Master Data contract missing required cases: {missing}")
    if any(not case.get("expect") for case in cases):
        raise AssertionError("every MSA Master Data contract case requires expected behavior")

    skill = (ROOT / "skills" / "medicine-store-assistant" / "SKILL.md").read_text(encoding="utf-8")
    system = (ROOT / "skills" / "medicine-store-assistant" / "references" / "system-contract.md").read_text(encoding="utf-8")
    close = (ROOT / "skills" / "medicine-store-assistant" / "references" / "month-close-archive-and-cleanup.md").read_text(encoding="utf-8")
    archive = (ROOT / "skills" / "medicine-store-assistant" / "references" / "master-data-archive-contract.md").read_text(encoding="utf-8")
    reorder = (ROOT / "skills" / "medicine-store-assistant" / "references" / "reorder-intelligence-and-owner-review.md").read_text(encoding="utf-8")

    required_snippets = [
        (skill, "master-data-archive-contract.md"),
        (system, "not** a fifth operating surface"),
        (archive, "values/text, not live formulas"),
        (archive, "Do not treat `Master Data` as a fifth compatibility-locked operational sheet."),
        (archive, "fail closed on ambiguity instead of appending a second copy"),
        (archive, "The mere existence of a legacy desktop workbook does not automatically block Google-side month close."),
        (close, "closing fingerprint"),
        (close, "contains no live formulas/dependencies"),
        (reorder, "Do not double-count one month"),
    ]
    for text, snippet in required_snippets:
        if snippet not in text:
            raise AssertionError(f"missing MSA Master Data archive contract snippet: {snippet}")


def main() -> int:
    validate_contract()
    print("MSA Master Data archive contract: valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
