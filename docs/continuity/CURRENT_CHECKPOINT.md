# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.12.0`
- Purpose: durable public operational core for DEDAL

## Active skills

Domain: `$msa`, `$pra`, `$ika`.

Generic/meta: GitHub, Files & Artifacts, Research, Software Development, Decision Design, Interface Design, Agent Engineering, **Security Engineering**, **Project Bootstrap**, **Release Engineering**, Automations, Skill Acquisition.

## Capability expansion roadmap

Roadmap: `docs/evolution/CAPABILITY_EXPANSION_ROADMAP.md`.

Eight planned areas are locked into the campaign:
1. Security Engineering — active;
2. Project Bootstrap / Context Adapter — active;
3. Release / Deployment Engineering — active;
4. Data / Spreadsheet / Operational Workflow Engineering — planned;
5. Writing / Editorial Engineering — planned;
6. Visual Direction / Image Production — planned;
7. Decision / Planning Intelligence v2 — planned;
8. Knowledge / Memory Architecture — planned.

Promotion remains gap-driven: an area may become a new skill, merge into an existing skill, or be rejected if evidence does not justify independent routing.

## First-wave corpus and boundaries

Audit: `skills/skill-acquisition/references/first-wave-capability-audit-2026-09-14.md`.

### Security Engineering

Primary corpus includes OWASP Agentic/GenAI security material, OpenAI prompt-injection/agent guardrail guidance, Anthropic trustworthy-agent guidance, and the pinned OWASP project repository `99f4395589bdbd120ae961f9cd179e79d7f9b27f`.

Core contract: map assets/trust/authority -> enumerate abuse paths -> constrain capability/blast radius -> verify controls -> report residual risk. Prompt injection is treated as an authority/capability-containment problem, not merely a string-classification problem. Persistent memory/context is treated as an attack surface.

### Project Bootstrap

Primary corpus includes AGENTS.md (`agentsmd/agents.md` @ `d001185d792eb6402a58e4cbef1c228b309ec25d`), current GitHub repository/path-specific instruction guidance, and DEDAL's own bootstrap/continuity evidence.

Core contract: build a minimal executable project model from authoritative state, separate stable rules from volatile checkpoint state, use scoped/progressive instructions, and avoid asking the Creator to reconstruct retrievable context.

### Release Engineering

Primary corpus includes SLSA (`slsa-framework/slsa` @ `54b88b009fd45acb331c7e6578a526e0f36e0430`), GitHub artifact-attestation/Actions security guidance, Sigstore/Cosign verification patterns, and SemVer as one compatibility model.

Core contract: verified source -> attributable build/artifact -> deliberate promotion -> deployment/runtime verification -> rollback/release evidence. Build success, artifact existence, deployment and runtime health remain separate evidence levels.

No third-party package, script, signing tool, or security scanner was installed or executed for this research/adaptation.

## Harness benchmark

Harness v1 remains active. Current compact benchmark evidence:
- GH-01: latest clean rerun PASS after mutation-mode/tool-allowlist hardening;
- GH-02: PASS;
- RS-01 / RS-02: await suitable real research work;
- LH-01 / LH-02: await suitable real multi-session/new-chat work.

Do not manufacture large artificial tasks merely to complete the scorecard.

## Verification target for v0.12.0

Repo Integrity must validate:
- the three new skill entrypoints and adaptation notes;
- minimum focused-reference counts;
- first-wave corpus audit and eight-area roadmap;
- pinned OWASP / AGENTS.md / SLSA provenance identifiers;
- existing foundational/kernel/skill checks;
- semantic VERSION format.

## Next executable phase

1. Exercise the new skills on real DEDAL/project work and capture regressions only when meaningful.
2. Continue Wave 2 with **Data / Operational Workflow Engineering** unless a higher-priority real gap emerges.
3. Then evaluate Writing/Editorial, Visual Direction, Decision Intelligence v2, and Knowledge/Memory Architecture in roadmap order, merging rather than multiplying skills where independence is weak.
4. Keep security/release facts that drift tied to current authoritative sources rather than freezing temporary platform syntax into Core.
