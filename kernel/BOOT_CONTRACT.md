# Boot Contract

> Normative contract: `kernel/boot.yaml`. This Markdown file is an explanatory view.

DEDAL 0.39.1 boots from direct files under `/DEDAL/core`. It checks `core-manifest.yaml` and `core-files.json`, reconstructs accepted state from `state/checkpoint.yaml`, resolves relevant private state, composes the smallest sufficient capability set, and hydrates every required dependency of a semantically selected task profile before consequential execution. Lexical matches are candidates only; receipt v6 binds the decision to the task and verifies read-before-gate chronology.

The external DEDAL Runtime/Python Canary MCP layer is retired. Archived artifacts are historical evidence, never boot authority. Material subgoal changes trigger re-routing and re-hydration. Discovery is not activation, and activation is not execution readiness.

Essential readiness uses `validators/validate_core.py`, including document/schema, routing/profile and release checks. Profile receipts require an explicit operation and phase. Audits use inspect gates; execution uses preconditions; close uses postconditions. Null Library versions are represented as unavailable with the observed identity and digest. Coverage-mode receipts prove coverage only. Local-artifact mode verifies specific byte/command properties; authoritative tool results and actual reviewer acceptance remain necessary for external judgments.
