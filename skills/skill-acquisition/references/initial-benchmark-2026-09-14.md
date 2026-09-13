# Initial Skill Ecosystem Benchmark — 2026-09-14

This is the first DEDAL external-skill survey. It records ideas adopted or rejected; it is not a claim that any surveyed package is globally safe or best-in-class.

## Surveyed source classes

### Agent Skills open standard

- `https://github.com/agentskills/agentskills`
- Key useful pattern: progressive disclosure — discovery metadata first, full `SKILL.md` on activation, deeper scripts/references only when needed.
- License observed at survey time: Apache-2.0 for code, CC-BY-4.0 for documentation.

### OpenAI public plugin/skill examples

- `https://github.com/openai/plugins`
- Useful pattern: explicit skill invocation and focused reusable workflows.
- Rejected as a DEDAL-wide rule: overly aggressive mandatory invocation based on tiny probability of relevance. DEDAL keeps smallest-sufficient routing instead.

### Production engineering/community repositories

Examples inspected include:

- `https://github.com/kk-agent/skill.md`
- `https://github.com/buildpad-ai/skills`
- `https://github.com/dotnet/skills`

Useful patterns:

- phase separation such as define/specify -> plan -> build -> verify -> review -> ship;
- root-cause-first debugging;
- dedicated validation before declaring completion;
- tests and review gates tied to concrete changes rather than generic ceremony.

### Research-oriented skills

Examples inspected include:

- `https://github.com/PracticalSwan/agent-skills`
- `https://github.com/nousresearch/hermes-agent`
- `https://github.com/firecrawl/web-agent`

Useful patterns:

- primary-source preference;
- explicit source provenance captured during retrieval rather than reconstructed afterward;
- triangulation and visible disagreement;
- confidence/evidence gaps surfaced rather than smoothed over;
- citation verification as a separate completion gate for evidence-heavy deliverables.

DEDAL adaptation: preserve these principles without requiring one specific citation-ledger script or a fixed number of sources for every task.

### Public registries / discovery hubs

Examples: ClawHub and skills.sh.

Useful pattern: broad discovery across many publishers and categories.

Security lesson: registry scanning, static analysis, reputation, stars, install counts, and malware telemetry are signals only. ClawHub security reports demonstrate that a package can be malware/static-scan clean while still being flagged for semantic privacy, persistence, broad-trigger, or excessive-agency risks. DEDAL therefore requires instruction-level and data-boundary review before adoption.

## First accepted changes to DEDAL generic skills

### Software Development

Adopt:

- explicit understand/plan/implement/verify/review/ship lifecycle scaled to task size;
- root-cause-first debugging;
- fresh-evidence completion gate;
- inspect final diff/artifact rather than trusting tool exit alone.

### GitHub

Adopt:

- separate read/plan/write/verify phases;
- refetch before writes when concurrent state may matter;
- inspect exact diff and final branch/commit after mutation;
- never equate a queued/running workflow with success.

### Research

Adopt:

- search strategy proportional to claim importance;
- capture source identity/provenance while researching;
- primary-source preference plus independent corroboration for important contested claims;
- explicit unsupported/conflicting evidence state;
- citation/evidence coverage review for evidence-heavy outputs.

## Deliberately rejected patterns

- global "always invoke skills" rules that override DEDAL routing judgment;
- automatic installation/execution of discovered third-party packages;
- fixed worker/subagent requirements when the runtime may not support them;
- treating popularity, registry badges, or security scanners as trust;
- rigid source-count rules for trivial or uniquely authoritative facts;
- copying provider-specific tool syntax into DEDAL's durable skill layer when a provider-agnostic contract works.

## Next survey direction

Continue ecosystem research only against concrete capability gaps. Near-term candidates should be selected from repeated DEDAL work rather than by catalog size.