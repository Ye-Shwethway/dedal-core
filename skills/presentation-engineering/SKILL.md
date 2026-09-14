---
name: presentation-engineering
description: Design, build, edit, and verify professional slide decks and PPTX artifacts with strong narrative, evidence, visual hierarchy, editability, and presentation-specific QA.
---

# Presentation Engineering

Own the presentation-production layer: how an audience, objective, evidence set, and speaking context become a coherent deck and reusable presentation artifact.

## Use when

- creating or editing PowerPoint/PPTX, meeting decks, CME/clinical talks, annual reports, board/management decks, lectures, scientific/lab presentations, pitch decks, or training slides;
- turning source documents/data/research into a slide narrative;
- redesigning an existing deck while preserving meaning/editability;
- deciding slide roles, charts, diagrams, imagery, speaker notes, pacing, and template use;
- verifying slide readability, overflow, visual hierarchy, evidence placement, and rendered output.

## Ownership boundary

Presentation Engineering owns audience/objective framing, narrative spine, slide-role architecture, action titles, evidence-to-slide mapping, presentation visual hierarchy, chart/diagram choice, speaker notes, template fidelity, editability strategy, and deck-specific render QA.

It does **not** replace:
- Research or a domain owner for factual authority;
- Writing/Editorial for prose and translation quality;
- Data Operations for source-table integrity;
- Visual Direction for custom visual asset continuity;
- Quality Engineering for independent readiness when required;
- the platform-native slide/PPTX execution tool.

## Workflow

1. **Frame the talk.** Audience, decision/learning goal, duration, venue/display constraints, presenter role, language, and required source/template.
2. **Build the argument.** Define thesis, narrative arc, sections, and slide roles before styling individual slides.
3. **Map evidence.** Claims, data, citations, figures, screenshots, tables, and unresolved assumptions belong to explicit slide/evidence slots.
4. **Choose a visual system.** Establish hierarchy, typography, palette, spacing, motif and layout grammar appropriate to the topic and context.
5. **Build editable artifacts.** Prefer native text, shapes, charts and tables where practical; use images when the source visual or complexity makes raster/vector placement more truthful.
6. **Add presenter support.** Speaker notes, transitions between sections, timing cues, and appendix/source slides when useful.
7. **Render and inspect.** Validate the file, render slides, inspect montage/full-size slides, and fix overflow, collisions, tiny text, orphaned placeholders, poor chart labeling, inconsistent spacing and weak hierarchy.
8. **Deliver sourcefully.** Preserve template/source/workspace or authoring code when future revision matters.

## Durable rules

- A deck is not a document split into rectangles. Each slide has a role in an argument or teaching sequence.
- Prefer conclusion/action-oriented titles when the audience should understand the point before reading the body.
- One slide may contain multiple elements, but it should have one dominant communicative purpose.
- Native editability is valuable, but not at the cost of misrepresenting evidence or rebuilding complex source figures inaccurately.
- Every material number/claim should retain a traceable evidence path when the context requires it.
- Avoid repetitive title-plus-bullets layouts; vary structure according to content, not decoration.
- Rendered visual QA is mandatory for serious deck production; source code/XML validity alone cannot prove layout quality.
- Template inheritance and requested brand constraints outrank generic design taste.
- Current PPTX library/tool limitations, font availability, rendering differences and platform behavior are runtime facts; verify when material.

## Progressive references

- `references/story-evidence-and-slide-architecture.md`
- `references/pptx-production-and-qa.md`
