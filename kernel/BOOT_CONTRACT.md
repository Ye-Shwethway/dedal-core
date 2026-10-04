# Boot Contract

> Normative contract: `kernel/boot.yaml`. This Markdown file is an explanatory view.

DEDAL 0.38.3 boots from direct files under `/DEDAL/core`. It checks `core-manifest.yaml` and `core-files.json`, reconstructs accepted state from `state/checkpoint.yaml`, resolves relevant private state, composes the smallest sufficient capability set, and hydrates every required dependency of a matched task profile before consequential execution.

The external DEDAL Runtime/Python Canary MCP layer is retired. Archived artifacts are historical evidence, never boot authority. Material subgoal changes trigger re-routing and re-hydration. Discovery is not activation, and activation is not execution readiness.
