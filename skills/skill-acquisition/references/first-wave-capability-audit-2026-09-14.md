# First-Wave Capability Corpus Audit — 2026-09-14

Scope: Security Engineering, Project Bootstrap/Context Adapter, and Release Engineering.

## Method

Current primary/official guidance was preferred. External content was treated as untrusted research input; no third-party package, script, or security/release tool was installed or executed for this audit.

## Security Engineering

### Sources
- OWASP GenAI Security Project / Agentic Security Initiative; pinned OWASP project repo `99f4395589bdbd120ae961f9cd179e79d7f9b27f`.
- OpenAI, `Designing AI agents to resist prompt injection` (2026-03-11).
- OpenAI practical agent-building guardrail guidance.
- Anthropic, `Trustworthy agents in practice` (2026-04-09).
- OWASP 2026 memory/context poisoning and agentic-risk material.

### Adopt / adapt
- Adopt explicit asset/trust/authority mapping.
- Adopt least-privilege and blast-radius reduction.
- Adapt prompt injection from text-classification problem into authority/capability-containment problem.
- Adopt durable-memory poisoning as a separate persistence risk.
- Adopt realistic negative/adversarial tests plus precise residual-risk language.

### Reject
- classifier-only security;
- prompt wording as the main authorization boundary;
- universal approval ceremony for every write;
- claims of `secure` from checklist compliance alone.

## Project Bootstrap / Context Adapter

### Sources
- AGENTS.md open format; pinned `agentsmd/agents.md` @ `d001185d792eb6402a58e4cbef1c228b309ec25d`.
- Current GitHub repository/path-specific/agent custom-instruction documentation.
- Existing DEDAL bootstrap, continuity, repository, and Harness-v1 lessons.

### Adopt / adapt
- Adopt predictable repository-level agent guidance and scoped local instructions.
- Adapt onboarding into a compact executable context map instead of a broad repository summary.
- Separate stable rules from volatile checkpoint state.
- Validate commands/paths/state against live project evidence.
- Use progressive disclosure and reload only drifted slices.

### Reject
- giant root instruction files;
- vendor-specific precedence as a universal rule;
- treating written instructions as proof that runtime/code matches them;
- asking the Creator to reconstruct retrievable project history.

## Release Engineering

### Sources
- SLSA repository `slsa-framework/slsa` @ `54b88b009fd45acb331c7e6578a526e0f36e0430`.
- Current GitHub artifact-attestation and Actions security documentation.
- Sigstore/Cosign identity-based signing and verification guidance.
- Semantic Versioning 2.0.0 as one version-communication model.

### Adopt / adapt
- Adopt source -> build -> artifact -> deployment -> runtime as distinct evidence states.
- Adopt commit/artifact digest attribution and provenance where consumption verifies it.
- Adopt least-privilege/short-lived deployment identity where practical.
- Adapt staged rollout and rollback to project risk instead of mandatory ceremony.
- Keep data/schema rollback separate from binary rollback.

### Reject
- signing every transient CI output;
- provenance as proof of vulnerability absence/correctness;
- mandatory SLSA level targets for all projects;
- universal SemVer or provider-specific release mechanisms.

## Boundary conclusion

All three areas are independently routable and repeatedly useful across DEDAL projects. They warrant separate top-level skills, with explicit pairing rather than inheritance:
- Security Engineering owns security/threat/authority reasoning.
- Project Bootstrap owns initial/resumed project context adaptation.
- Release Engineering owns artifact/release/deployment lifecycle evidence.

They complement, but do not replace, Agent Engineering, Software Development, GitHub, Research, or Skill Acquisition.
