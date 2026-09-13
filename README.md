# DEDAL Core

**Dream Everything. Design Anything. Limitlessly.**

`dedal-core` is the public operational foundation for **DEDAL**, a persistent, personalized AI collaborator developed with the Creator.

This repository is not a model checkpoint and does not contain private memory. It defines the durable structures that make DEDAL more consistent, capable, auditable, and reusable across sessions, tools, projects, and model upgrades.

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

```text
.
├── AGENTS.md
├── SECURITY.md
├── docs/
│   ├── IDENTITY.md
│   ├── architecture/
│   │   └── FOUNDATION.md
│   ├── capabilities/
│   │   └── CURRENT_CAPABILITIES.md
│   ├── continuity/
│   │   └── CURRENT_CHECKPOINT.md
│   └── evolution/
│       └── IMPROVEMENT_PROTOCOL.md
├── state/
│   └── capability-registry.yaml
└── .github/
    └── workflows/
        └── repo-integrity.yml
```

## Public-Core Rule

This repository may contain public architecture, workflows, documentation, sanitized configuration, schemas, tests, and automation definitions.

It must **not** contain credentials, API tokens, passwords, private personal data, raw memory exports, confidential medical/hospital data, or other sensitive state.

Private state belongs in explicitly authorized external stores such as ChatGPT Memory/Library, private databases, connected services, or other secured infrastructure.

## Status

Foundation initialized: **2026-09-13**.

The current phase is deliberately minimal: establish identity, continuity, capability awareness, security boundaries, and an improvement protocol before adding more automation or infrastructure.
