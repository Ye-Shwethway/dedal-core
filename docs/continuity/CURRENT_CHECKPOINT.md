# Current Checkpoint

_Date: 2026-09-13_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Purpose: durable public operational core for DEDAL

## Foundation Established

The initial foundation consists of:

- `README.md` — purpose and repository map;
- `AGENTS.md` — operating contract and source-of-truth hierarchy;
- `SECURITY.md` — public-repository security boundary;
- `docs/IDENTITY.md` — stable DEDAL identity definition;
- `docs/architecture/FOUNDATION.md` — layered system architecture;
- `docs/capabilities/CURRENT_CAPABILITIES.md` — current capability snapshot;
- `docs/evolution/IMPROVEMENT_PROTOCOL.md` — externalized self-improvement loop;
- `state/capability-registry.yaml` — machine-readable sanitized capability registry;
- `.github/workflows/repo-integrity.yml` — baseline structural validation;
- `.gitignore` — local/private artifact exclusions.

## Locked Principles

1. DEDAL Core is public architecture, not a private-memory dump.
2. Live authoritative state outranks remembered summaries.
3. Model weights are not treated as self-modifiable by DEDAL.
4. Improvement occurs through context, tools, persistent state, evaluations, workflows, and feedback loops.
5. Sensitive state remains external and explicitly authorized.
6. Work/cloud-computer capability is valuable but quota-expensive and is not a foundational always-on dependency.
7. Changes should remain inspectable, attributable, and reversible where practical.

## Immediate Next Phase

Do not rush into a large agent framework.

Next design work should identify the Creator's intended DEDAL evolution idea and then decide which of these layers are actually needed:

- persistent private state service;
- MCP/tool gateway;
- evaluation harness;
- workflow/skill registry;
- GitHub Actions execution runners;
- event/condition automation;
- cross-project continuity index.

Architecture should follow the actual use case rather than precede it.
