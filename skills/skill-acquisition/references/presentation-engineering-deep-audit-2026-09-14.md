# Presentation Engineering Deep Audit — 2026-09-14

## Gap

DEDAL could write prose, research facts, generate visuals, and manipulate files, but had no owner for professional presentation narrative, slide-role architecture, deck visual hierarchy, editability strategy, speaker notes, template fidelity, or rendered PPTX QA. The Creator regularly needs meeting, CME, annual and other presentation decks, so the gap is recurring and concrete.

## Sources reviewed

### Anthropic PPTX skill
- `anthropics/skills@34040c9c568585f6929bedeaad110ad08f079624` includes a substantial PPTX skill covering create/edit/read, templates, PptxGenJS, package manipulation, native charts, notes, rendering and validation.
- Its PPTX `LICENSE.txt` is proprietary and explicitly restricts extraction, copying and derivative works. DEDAL therefore uses it only as comparative evidence that the workflow class is mature; no text/code/assets are imported or derived.

### Open-source source-first presentation systems
- `siril9/presentation-skill@311e29920c7c7ab37a93c12676bab7baecc0f4a6`, MIT: mature source-first PPTX workflow with design/content/evidence/asset plans, editable decks, role-layout grammars, data/figure workflows, render QA, readability checks and scientific/clinical/report use cases.
- Tanght/other public PptxGenJS skills corroborate editable-native authoring, render inspection, overflow testing, font detection and reproducible source as durable production practices.
- Consulting/scientific presentation skills independently converge on audience/decision framing, answer-first or teaching-aware story structure, evidence traceability, native editability and slide-by-slide QA.

## Durable findings

1. A deck is a presentation argument/teaching sequence, not a document split into slides.
2. Audience shift and narrative spine should be defined before slide styling.
3. Slide roles should vary with purpose; repeating title-and-bullets layouts is a quality failure, not a neutral default.
4. Evidence planning must remain separate from visual polish; citations and material claims retain traceability.
5. Editable native elements are preferred where practical, but source evidence should not be inaccurately redrawn merely for editability.
6. Serious PPTX production needs rendered visual QA in addition to package validity/source correctness.
7. Source-first/rebuildable workspaces substantially improve iteration, auditing and recurring annual/CME/report workflows.
8. Font/rendering/library differences are runtime facts and must be verified or given layout slack.

## Ownership test

- Writing/Editorial owns prose quality, not deck architecture.
- Interface Design owns software UI/UX, not projected slide communication.
- Visual Direction owns image assets/continuity, not deck narrative.
- Research/domain skills own factual truth, not presentation assembly.
- Quality Engineering may independently verify a high-stakes deck but does not own its creative construction.

Presentation Engineering is therefore independently routable and recurring.

## Decision

**PROMOTE — Presentation Engineering as a top-level faculty.**

Platform-native slide/PPTX tooling, PptxGenJS, OOXML editors and renderers remain execution surfaces beneath it. Preserve higher-priority host instructions whenever the runtime provides a dedicated slide-generation workflow.
