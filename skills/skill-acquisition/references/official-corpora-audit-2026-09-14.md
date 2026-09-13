# Official Corpus Audit — Anthropic, Vercel, Microsoft

_Date: 2026-09-14_

This audit studies three high-signal first-party/public skill corpora as design inputs for DEDAL. It records patterns and provenance; it does not import their packages or runtime assumptions.

## Pinned sources

### Anthropic
- Repository: `anthropics/skills`
- Commit: `34040c9c568585f6929bedeaad110ad08f079624`
- Primary material: `skills/skill-creator/SKILL.md`
- License note: the repository does not expose one uniform root license at this snapshot; individual skills may carry their own license terms. DEDAL therefore uses conceptual synthesis only unless a specific file's license is separately verified.

Useful patterns:
- skill creation as an iterative draft -> realistic test prompts -> with-skill vs baseline -> qualitative/quantitative evaluation -> rewrite loop;
- explicit evaluation of triggering quality, not only output quality;
- progressive disclosure: metadata -> SKILL.md -> bundled resources;
- realistic test prompts and objective assertions only when the output is objectively verifiable;
- compare improved skills against the old version, not merely against no skill.

Rejected/generalized:
- Claude-specific subagent, viewer, and task-notification mechanics;
- deliberately pushy triggering as a universal rule. DEDAL prefers accurate triggering plus explicit aliases and smallest-sufficient routing.

### Vercel Labs
- Repository: `vercel-labs/agent-skills`
- Commit: `063bee94c3f4df8453406c830b0a7df0f2860278`
- Primary material: `skills/react-best-practices/SKILL.md`, repository build/test infrastructure.
- License note: the inspected React skill declares MIT in frontmatter; no root LICENSE file was found at the pinned snapshot. Reuse therefore remains pattern-level unless a specific source file's terms are verified.

Useful patterns:
- large knowledge sets compiled into a concise skill entrypoint plus granular rule files;
- rules grouped and ordered by impact, so high-value checks run before low-value polish;
- build-time validation and test extraction rather than trusting hand-maintained generated guidance;
- dedicated test packages for complex operational skills.

Rejected/generalized:
- React/Vercel-specific rules as global engineering law;
- generated output treated as trustworthy without source/version validation.

### Microsoft
- Repository: `microsoft/skills`
- Commit: `903dc62b1e4c833235b54db918a9a51cb6d3cc8f`
- Primary material: `.github/skills/skill-creator/SKILL.md`
- Root license: MIT.

Useful patterns:
- every instruction must justify its context-token cost;
- "degrees of freedom": use broad guidance when many approaches are valid, exact scripts/contracts when precision is required;
- freshness-first behavior for fast-changing SDK/API knowledge;
- 80/20 hero-scenario discipline: keep dominant workflows in the entrypoint, move less-common variants to references;
- do not demote a genuinely co-equal workflow merely to keep the main skill short;
- explicit generated-at/freshness metadata for generated knowledge skills.

Rejected/generalized:
- Azure-specific authentication/runtime rules outside Azure tasks;
- rigid token budgets as a universal constraint. DEDAL keeps the principle of compact entrypoints without assuming one numeric budget fits every domain.

## Adopt / Adapt / Merge / Reject matrix

| Pattern | Decision | DEDAL destination |
|---|---|---|
| Progressive disclosure | Adopt | Skill Acquisition authoring contract |
| With-skill vs baseline / old-skill eval | Adopt | `authoring-and-evals.md` |
| Trigger-quality evaluation | Adapt | `authoring-and-evals.md` |
| Objective assertions + human qualitative review | Adopt | `authoring-and-evals.md` |
| Impact-ranked rule catalogs | Adopt | `knowledge-packaging-and-freshness.md` |
| Build/validate generated rule packs | Adapt | `knowledge-packaging-and-freshness.md` |
| Degrees of freedom | Adopt | `authoring-and-evals.md` |
| 80/20 hero workflow split | Adapt | `knowledge-packaging-and-freshness.md` |
| Generated-at / freshness review | Adopt | `knowledge-packaging-and-freshness.md` |
| Provider-specific subagent/CLI mechanics | Reject | none |
| Vendor/domain rules as universal DEDAL rules | Reject | none |

## Conclusion

The strongest cross-corpus lesson is that a professional skill system must optimize four things separately: **routing accuracy, context efficiency, task performance, and freshness**. A skill can be well-written yet fail by triggering badly, loading too much context, becoming stale, or producing no measurable improvement. DEDAL should evaluate all four dimensions when materially revising a skill.