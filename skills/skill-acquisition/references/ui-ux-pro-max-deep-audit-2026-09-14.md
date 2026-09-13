# UI/UX Pro Max Deep Audit — 2026-09-14

Source: `nextlevelbuilder/ui-ux-pro-max-skill`
Pinned commit: `7f69fed6a2717900085f1bc3b263721f8ba025e2`
Verified license: MIT

## Why this source matters

UI/UX Pro Max is not merely a long prompt. Its main transferable architecture is a searchable local design-intelligence system: categorized UI/UX knowledge, BM25-style retrieval, domain and stack-specific searches, design-system aggregation, persistence, explicit no-match handling, and relevance/evaluation scripts.

At the pinned snapshot the project advertises a broad catalog covering styles, palettes, font pairings, UX guidance, charts, icons/motion, and many implementation stacks. Popularity/install counts were used only as discovery signals, never as trust or correctness proof.

## Adopt / Adapt / Merge / Reject

### Adapt

1. **Scoped design-intelligence retrieval**
   - Search only the domain relevant to the current design question.
   - Separate semantic UX concerns from stack/platform implementation guidance.
   - Inspect result identity/category and applicability before using it.

2. **Explicit miss semantics**
   - A zero-result or weak result is not a recommendation.
   - Retry once with narrower scope, then label general guidance as fallback.
   - Never fabricate a database/catalog match.

3. **Design-system aggregation**
   - For new product/page direction, synthesize a small complementary evidence set (product/surface pattern, visual family, semantic color, typography, interaction/accessibility, platform constraints) rather than asking one generic style query to decide everything.

4. **Master + surface override persistence**
   - Preserve global design truth separately from surface/page-specific exceptions.
   - Read existing master before regeneration.
   - Do not silently overwrite accepted direction.

5. **Retrieval quality / calibration mindset**
   - Search systems need relevance tests, thresholds, domain identity checks, and regression fixtures; raw lexical ranking alone is not proof of good routing.

6. **Freshness-aware stack knowledge**
   - Technical design guidance should carry version/review metadata and be verified when framework/API/platform drift can change implementation.

### Merge into existing `interface-design`

- The above patterns extend Interface Design's evidence layer; they do not justify a second competing UI skill.
- Existing brief inference, surface-mode framing, refinement-vs-redesign rules, accessibility floor, and bounded rendered verification remain the primary reasoning workflow.

### Reject from durable Core

- Vendoring the upstream CSV catalog wholesale.
- Treating upstream style/product rankings as universal taste truth.
- Provider-specific Claude/plugin path assumptions.
- Installing or auto-updating the upstream CLI as a DEDAL dependency.
- External logo-generation APIs/services as default interface-design capability.
- Fixed current framework versions embedded as permanent Core truth.
- Numeric variance/motion/density dials as mandatory design ontology.
- `--force`-style overwrite behavior without owner/project authority.
- Any assumption that popularity, catalog size, or a successful search proves current correctness.

## Security and authority notes

The upstream project contains executable CLI/scripts and optional external-service integrations. DEDAL inspected source but did not install or execute the package. Public Core keeps only rewritten methodology and provenance.

Catalog/query text must not become a path for leaking private project data to third-party services. Project-local/private evidence remains inside the correct trust boundary.

## DEDAL outcome

DEDAL Interface Design gains two new progressive references:
- `design-intelligence-retrieval.md`
- `design-system-persistence.md`

The skill now treats design intelligence as scoped evidence with explicit confidence/fallback semantics and persists durable design truth using safe master + surface precedence.
