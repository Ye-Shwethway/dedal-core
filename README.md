# DEDAL Core

**Dream Everything. Design Anything. Limitlessly.**

`dedal-core` is the public operational foundation for **DEDAL**, a persistent, personalized AI collaborator developed with the Creator.

This repository is not a model checkpoint and does not contain private memory. It defines the durable structures that make DEDAL more consistent, capable, auditable, and reusable across sessions, tools, projects, and model upgrades.

## 0.38.2 Library-native harness

DEDAL treats direct files under `/DEDAL/core` as its boot authority. `core-manifest.yaml` and `core-files.json` declare the machine contract and complete file inventory. Normative session behavior is YAML (`kernel/*.yaml`, `index/routing.yaml`, `index/task-profiles.yaml`, `state/checkpoint.yaml`), validated by `validators/validate_core.py`. External DEDAL Runtime/Python Canary MCP sidecars are retired.

## Purpose

DEDAL Core exists to preserve and improve:

- identity and operating principles;
- continuity across chats and model transitions;
- capability and tool awareness;
- workflow and agent conventions;
- externalized self-improvement through feedback, tests, and documentation;
- secure boundaries between public operating logic and private state;
- reusable automation and orchestration patterns.

## Design Principle

```text
Effective DEDAL capability
= model intelligence
× context quality
× tool access
× persistent state
× execution capability
× feedback loops
```

The base model is only one layer. The surrounding system can evolve independently through better context, tools, state, workflows, evaluation, and feedback.

## Repository Map

`kernel/` owns boot and invariants; `index/` owns routing, profiles and skill discovery; `state/` owns accepted machine checkpoints; `skills/` owns modular instructions; `evals/`, `scripts/` and `validators/` own checks; `docs/` explains the machine contracts. Every current file appears in `core-files.json`.

## Public-Core Rule

This repository may contain public architecture, workflows, documentation, sanitized configuration, schemas, tests, and automation definitions.

It must **not** contain credentials, API tokens, passwords, private personal data, raw memory exports, confidential medical/hospital data, or other sensitive state.

Private state belongs in explicitly authorized external stores such as ChatGPT Memory/Library, private databases, connected services, or other secured infrastructure.

## Status

Foundation initialized: **2026-09-13**.

Core 0.38.2 uses direct Library files. The recorded Git base is in `core-manifest.yaml`; upstream synchronization is pending.
