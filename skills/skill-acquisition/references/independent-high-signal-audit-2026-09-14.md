# Independent High-Signal Corpus Audit — 2026-09-14

Purpose: inspect popular independent skills for genuine DEDAL capability gaps, not popularity-driven copying.

## Discovery signal

skills.sh all-time leaderboard was used only as a discovery surface. At review time it showed strong adoption signals for `obra/superpowers` brainstorming, `Leonxlnx/taste-skill`, `lllllllama/RigorPilot-Skills`, and `pbakaus/impeccable`. Install counts are not trust or quality proof.

## Pinned sources

| Source | Commit | License | DEDAL decision |
|---|---|---|---|
| `obra/superpowers` | `b36e0829c6d0140e93cfef2ca599b1b07d4a7797` | MIT | Merge selected process-sizing ideas |
| `Leonxlnx/taste-skill` | `ccbc15639c97057cbfcf32ecebc38ef716e4bb37` | MIT | Adapt selected interface-design ideas |
| `lllllllama/RigorPilot-Skills` | `bd91195ad73199b95e24532b581ff12c07dcce09` | MIT | Merge research-governance patterns |
| `pbakaus/impeccable` | `cb56ed6c19a07329a9fa0cd4e657bee040156593` | Apache-2.0 | Adapt selected interface-design ideas |

No third-party package or script was installed or executed.

## 1. obra/superpowers

### Useful patterns
- Classify design/development work by process weight instead of one ceremony level for everything.
- A cheap feasibility spike, a bounded existing-flow change, and an architectural change deserve different artifacts.
- Hidden complexity can upgrade the process path mid-task; the workflow should not silently stay under-scoped.
- Explore current project context before design proposals.

### DEDAL adaptation
Merge the sizing/escalation concept into `decision-design` and normal Software Development judgment.

### Rejected
- Mandatory invocation before all creative work.
- Universal explicit approval gate before every implementation action.
- Provider-specific skill transitions and fixed document paths.

Reason: DEDAL already has Creator authority boundaries, project-local rules, and anti-ceremony requirements. Routine reversible work should not be blocked by ritual.

## 2. Leonxlnx/taste-skill

### Useful patterns
- Infer page/surface type, audience, reference signals, existing brand assets, and quiet constraints before choosing aesthetics.
- Distinguish real design systems from aesthetic inspiration and use official systems honestly when appropriate.
- Treat common model aesthetics as defaults to justify, not automatic choices.
- Redesign should inspect incumbent truth first.

### DEDAL adaptation
Promote a new provider-neutral `interface-design` skill together with Impeccable-derived patterns.

### Rejected
- Fixed numeric design/motion/density dials as universal controls.
- Hardcoded font/icon/library preferences.
- One frontend stack as a durable DEDAL default.
- Absolute bans whose validity depends on the brief.

## 3. llllllllama/RigorPilot-Skills

### Useful patterns
- Separate exploratory candidates from trusted reproduction or established truth.
- Freeze comparison anchors such as task, dataset/benchmark, evaluation source, reference, and budget when running an experiment campaign.
- Use an outer governance loop and an inner bounded experiment loop.
- Rank pre-execution candidates by expected value/cost/risk/rollback and post-execution candidates by observed evidence.
- Never turn exploratory gains into novelty/SOTA proof without the required literature contrast and fair-comparison evidence.

### DEDAL adaptation
Merge general scientific/exploratory evidence discipline into `research`; keep deep-learning-specific orchestration outside Core until a repeated DEDAL research workflow needs it.

## 4. pbakaus/impeccable

### Useful patterns
- The brief wins over generic taste.
- Missing DESIGN.md does not make an existing product greenfield; incumbent rendered/code truth matters.
- Distinguish surface jobs: Persuade, Operate, Read, Experience.
- Refinement preserves identity; redesign can replace visual language while preserving product truth.
- Visual QA should be evidence-backed and bounded rather than an open-ended self-polish loop.
- Durable design documentation should reflect what shipped, not abandoned intent.

### DEDAL adaptation
Combine these patterns with taste-skill influences in the new `interface-design` package.

### Rejected
- Bundled runtime launcher/binary and provider-specific hooks/agents.
- Universal maximalist aesthetic instruction.
- Command namespace and fixed project artifact conventions.

## Promotion summary

**Adopt/Adapt:** new `interface-design` skill.

**Merge:** process sizing into Decision Design; exploratory/trusted evidence separation into Research.

**Reject:** mandatory global invocation, universal approval ceremony, provider-specific runtimes, hardcoded aesthetic stacks, and popularity as trust.

## Future evaluation

Interface Design is a strong candidate for task-based qualitative evaluation because visual quality is partly subjective. Use representative surfaces with explicit briefs, compare against baseline behavior, and preserve Creator review rather than inventing pseudo-objective aesthetic metrics. Accessibility/responsiveness/runtime checks can remain objective where tooling supports them.
