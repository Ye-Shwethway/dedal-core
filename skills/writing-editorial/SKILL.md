---
name: writing-editorial
description: Design, draft, rewrite, translate, edit, and quality-check user-facing prose while preserving intent, factual grounding, audience fit, terminology, voice, and multilingual fidelity.
---

# Writing / Editorial Engineering

Use this skill when the main deliverable is prose whose quality depends on preserving meaning while improving structure, clarity, tone, consistency, or cross-language fidelity.

## Core lifecycle

`establish intent/audience -> separate facts from expression -> choose structure -> draft/transform -> terminology/voice pass -> fidelity/grounding pass -> polish -> final QA`

## Rules

1. **Intent before prose** — determine what the text must accomplish, who will read it, what action or understanding it should produce, and any format/channel constraints.
2. **Project/user style outranks generic style** — explicit Creator instructions, accepted terminology, brand/project voice, legal/medical/domain conventions, and target-language norms take priority over general style-guide preferences.
3. **Facts and style are separate layers** — editing wording must not silently add, remove, strengthen, weaken, or reinterpret factual claims. If a material claim changes, verify it or flag it as an editorial/content decision.
4. **Preserve semantic invariants** — for rewrites/translations identify non-negotiable meaning, dates, quantities, names, obligations, negation, uncertainty, and scope before changing phrasing.
5. **Structure serves reader tasks** — order information by reader need and decision/action flow, not by the source text's accidental order. Preserve source order only when sequence itself carries meaning.
6. **Prefer clarity over ornament** — use precise, direct wording appropriate to the audience. Avoid unnecessary jargon, ambiguity, decorative complexity, and filler unless voice or genre deliberately requires them.
7. **Terminology is state** — use one preferred term per concept unless variation is intentional. Maintain capitalization, abbreviations, labels, names, and translated equivalents consistently across the artifact.
8. **Voice is a controlled variable** — distinguish formality, warmth, directness, technical density, persuasion, humor, and emotional intensity rather than treating “tone” as one vague dial.
9. **Revision should have a target** — make passes for structure, correctness/fidelity, terminology, voice, and surface polish separately when the artifact is consequential. Do not endlessly rewrite without a defect signal or requested direction.
10. **Multilingual work protects meaning first** — translate intent and function, not surface word order. Preserve critical entities/units/numbers; account for target-language naturalness and cultural/contextual fit; expose genuinely ambiguous source wording.
11. **Global-facing text minimizes translation traps** — favor unambiguous sentence structure and stable terminology; avoid unnecessary idioms, culture-specific metaphors, and wordplay when downstream translation/localization matters.
12. **Publication QA is proportional to risk** — for consequential text check factual claims, omissions, dates/numbers, names/links, terminology, requested format, accessibility/readability, and channel constraints before declaring it ready.

## Editing modes

- **Transform** — rewrite/shorten/expand/reformat while preserving semantic invariants.
- **Draft** — create new prose from goals, facts, constraints, and audience.
- **Translate/localize** — preserve meaning while producing natural target-language text and required formatting.
- **Editorial review** — diagnose structure, clarity, terminology, tone, factual-risk, and publication defects without automatically replacing the whole artifact.
- **Style-system work** — establish or apply durable terminology/voice/style rules; use executable lint/checks when they materially reduce repeat defects.

## Grounding rule

When prose contains externally verifiable or time-sensitive claims, pair with Research and cite/verify those claims before polishing them into authoritative-sounding language. Editorial confidence must not exceed source confidence.

## Pairing

Pair with Research for factual grounding, Files/Docs for artifact mechanics, Interface Design for UX copy embedded in product surfaces, and domain skills for specialized terminology and policy. This skill owns editorial mechanics, not domain truth.
