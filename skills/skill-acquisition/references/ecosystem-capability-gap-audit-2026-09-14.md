# Ecosystem Capability-Gap Audit — 2026-09-14

## Purpose

Survey the current public Agent Skills ecosystem for capability areas that materially improve DEDAL, without turning the Core into a skill collection. The question is not how many skills exist; it is which missing faculties or reference packs improve real Creator workflows.

## Decision rule

Classify candidates as:

- **TOP-LEVEL CANDIDATE** — distinct recurring ownership domain that may deserve an independently routable faculty after evidence.
- **REFERENCE-PACK FIRST** — useful specialist knowledge that should remain under an existing owner until recurring outcomes justify promotion.
- **LATER / HIGH BAR** — potentially valuable, but risk, evidence, or workflow maturity is insufficient.
- **REJECT AS TOP-LEVEL** — execution surfaces, thin wrappers, duplicate ownership, or weakly grounded skill collections.

Popularity, stars, marketplace counts, or a vendor label are discovery signals only.

## High-signal sources reviewed

### Cloudflare

- Source: `cloudflare/skills`
- Pinned commit: `b052c32bab7dd493513260228a36c88294f343f1`
- First-party corpus spanning Workers, Pages, KV/D1/R2, Durable Objects, Wrangler, networking, security, observability, Agents SDK, and MCP workflows.
- Strong pattern: current-doc bias plus contextual auto-loading rather than static product knowledge.

### Flutter

- Source: `flutter/agent-plugins`
- Pinned commit: `7cdb7d3c33679ef14a7a7584cec1d5ecb8752586`
- First-party Flutter team corpus combining skills, persistent rules, MCP live analysis/test tools, and specialist agents.
- Strong pattern: use procedural skills for known model failure modes; use live analyzer/test state for project truth.

### Android

- Source: `android/skills`
- Pinned commit: `bac232fd02b0855df9275281a2a7a47643768719`
- First-party Android skills explicitly prioritize workflows where evaluations show LLM underperformance instead of documenting everything.
- Strong pattern: evidence-targeted reference packaging.

### HashiCorp

- Source: `hashicorp/agent-skills`
- Pinned commit: `c2d65dfe492f74d360d35b859b88932222470bd8`
- First-party Terraform/Packer corpus with explicit lifecycle states and independently installable specialist skills.
- Strong pattern: product-specific procedural packs should not automatically become broad top-level faculties.

### Postgres / backend

- Source: `neondatabase/postgres-skills`
- Pinned commit: `27fe45e0f71ea89a6eaf9ea4d2e4068957c81c26`
- Also reviewed: Neon and Supabase agent-skill corpora.
- Useful coverage: schema design, indexing, query optimization, migrations, pooling, concurrency, branching, RLS, monitoring.

### Quality engineering

- Reviewed community QA skill collections and Playwright-specific operating contracts.
- Useful recurring concepts: independent acceptance evidence, E2E, exploratory testing, regression, robust behavioral locators, boundary mocking, visual/accessibility checks, post-deploy drift checks.
- Evidence quality is mixed because no single first-party cross-framework QA corpus dominates; adaptation should synthesize methodology and prefer framework primary docs where possible.

### Observability / SRE

- Reviewed Sentry official AI skill direction and vendor-neutral OpenTelemetry community skills.
- Useful pattern: source-of-truth indexes and bounded traces/metrics/log retrieval rather than copying fast-changing telemetry docs into prompts.

### Healthcare / life sciences

- Reviewed `awslabs/hcls-agent-skills` and NVIDIA Digital Health examples.
- The ecosystem is substantial, but generic clinical reasoning is not a safe acquisition target. DEDAL should prefer bounded clinical-informatics, documentation, interoperability, data, research, or coding workflows with current authoritative sources.

## Classification

### 1. Quality Engineering — TOP-LEVEL CANDIDATE, priority 1

Why it may deserve its own owner:

- Software Development owns implementation/debug/testing mechanics, but it should not grade its own work by default.
- Release Engineering owns artifact/source/deployment evidence, not product-behavior test strategy.
- Interface Design owns UX direction, not independent visual regression or accessibility verification.
- DEDAL repeatedly benefits from acceptance criteria, regression design, E2E checks, exploratory testing, visual verification, test oracles, and failure evidence across projects.

Proposed ownership boundary if promoted:

> Independent product-quality strategy and verification: acceptance criteria, test planning, exploratory testing, E2E/integration strategy, regression, visual/accessibility checks, reliability checks, and evidence-based readiness verdicts.

Do not let it replace implementation tests, release provenance, or Creator acceptance.

Next action: deep audit QA methodology and representative tool-specific corpora, then baseline on real DEDAL project flows before promotion.

### 2. Cloudflare Platform — TOP-LEVEL CANDIDATE, priority 2

Why it may deserve its own owner:

- Creator workflows repeatedly span Workers, Pages, D1, Access, Tunnel, DNS/networking, Wrangler, storage, and AI-agent infrastructure.
- The platform crosses Software Development, Release Engineering, Security Engineering, and infrastructure boundaries often enough that routing becomes fragmented.
- A specialist Cloudflare owner can preserve product semantics while pairing with generic owners for implementation/security/release layers.

Promotion condition: adapt first-party knowledge into DEDAL with live-doc freshness and no external runtime dependency. Do not copy the whole vendor corpus into always-loaded context.

### 3. Database Engineering — TOP-LEVEL CANDIDATE, priority 3

Distinct potential ownership:

- schema and relational design;
- indexes/query plans/performance;
- migrations and backward compatibility;
- transactions, isolation, locks, concurrency;
- connection pooling and operational database behavior.

This is not Data Operations, which owns record identity, reconciliation, staging, formulas, deterministic transforms, and promotion mechanics.

Start as reference packs. Promote only after recurring database work demonstrates routing value.

## Reference-pack-first areas

### Flutter / Mobile

Use the official Flutter corpus under Software Development, with Interface Design and Release Engineering paired only when the subgoal requires them. Current evidence does not justify a separate Flutter personality/faculty.

### Android native / Play-facing engineering

Use official Android skill guidance on demand. Treat framework/platform facts as fresh technical references, not permanent Core rules.

### Postgres / Supabase / Neon

Use as database reference packs and as evidence toward a future Database Engineering owner. Vendor-specific workflows remain subordinate to project truth.

### Terraform / IaC

Keep under Release Engineering + Security Engineering + Software Development for now. Promote infrastructure/SRE only if repeated work shows a stable ownership gap.

### Observability / SRE

Reference-pack first. Useful topics include structured logs, traces, metrics, alert evidence, incident timelines, production diagnosis, rollback signals, and post-deploy checks. Ownership currently overlaps Release, Software, and Security.

### Browser / Computer Automation

Treat as an execution surface. Browser skills may package efficient actions or test recipes, but browser control itself is not a top-level faculty. QA, Research, or Automations should own intent.

## Later / high-bar area

### Healthcare / Clinical Informatics

Potentially high value because the Creator is a physician and DEDAL supports hospital workflows, but the acquisition target must remain bounded.

Good future targets:

- FHIR/HL7/clinical interoperability;
- evidence-grounded medical literature workflows;
- coding/terminology mapping;
- clinical documentation structure;
- de-identified clinical data engineering;
- guideline retrieval with freshness/provenance controls.

Do not create a generic `doctor` or autonomous clinical-decision skill from community prompts. High-stakes medical conclusions still require current authoritative sources and appropriate uncertainty.

## Reject as top-level

- marketplace-scale bulk imports;
- site-specific browser action collections;
- thin vendor wrappers already covered by an existing faculty plus reference pack;
- generic medical/persona skills with weak provenance;
- skills duplicating Cognitive Runtime invariants;
- skills whose main value is exposing a tool rather than teaching a distinct reasoning/workflow domain.

## Campaign order

1. Deep-audit **Quality Engineering** and decide whether it clears the top-level promotion gate.
2. Deep-audit **Cloudflare Platform** against the Creator's real Cloudflare workflows.
3. Build **database reference packs**, then reassess Database Engineering promotion.
4. Add Flutter/Android, observability, and IaC references opportunistically when real tasks exercise them.
5. Keep healthcare acquisition bounded and evidence-heavy; revisit after lower-risk capability work.

## Evidence boundary

This audit establishes discovery and architectural classification only. It does not prove that any candidate improves DEDAL outcomes. Promotion requires representative task evidence and regression review.
