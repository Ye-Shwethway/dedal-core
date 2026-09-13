# Instruction Hierarchy and Drift

Agent-facing project instructions should route behavior without becoming a stale duplicate documentation system.

## Hierarchy

Common layers include:
- Creator/session instructions;
- repository-wide agent instructions such as root `AGENTS.md`;
- path/module-specific `AGENTS.md` or equivalent scoped instructions;
- architecture/ADR and contribution documentation;
- current checkpoint/status artifacts;
- task-specific live state.

When multiple applicable instructions exist, use the platform/project's defined precedence and surface material conflicts. Do not silently choose the most convenient rule.

## Scope

Keep global instructions limited to rules that truly apply across the project. Put language/framework/module-specific rules near their scope when the execution surface supports that structure.

## Drift controls

Instructions become stale when they duplicate volatile facts such as:
- dependency versions;
- branch heads;
- temporary paths;
- current issue status;
- release numbers;
- one-off workarounds.

For volatile facts, point to the authoritative manifest/checkpoint/service instead of embedding a copy unless the snapshot itself is intentionally durable.

## Bootstrap verification

Before treating a context adapter as adequate, verify:
- referenced paths exist;
- commands are grounded in manifests/workflows/docs or were actually observed;
- branch/release claims match live state when available;
- accepted decisions are distinguished from proposals;
- the next step is executable without reconstructing hidden chat history.
