# PPTX Production and QA

Use this reference for editable PowerPoint production, template adaptation, slide rendering, and deck-specific QA.

## Production lanes

Choose according to the runtime and user need:
- native slide-generation capability when available;
- PptxGenJS or equivalent for programmatic editable decks;
- template-preserving OOXML/package editing for narrow structural edits when necessary;
- python-pptx for inspection or compatible limited operations when it is the appropriate runtime.

Do not assume one library is universally best. Prefer the platform's native supported slide tooling when it is stronger and follow its instructions.

## Source-first principle

For serious or recurring decks, preserve a rebuildable representation: outline/content plan, evidence/asset plan, template, authoring source, or equivalent workspace. Fix the source, then rebuild; avoid accumulating manual patches only in the final binary.

## Editability

Prefer editable text, simple diagrams, shapes, tables, and native charts when practical. Use source figures/screenshots/complex diagrams as images when redrawing would reduce fidelity or evidence integrity.

## Template work

Inspect the template visually before filling it. Respect masters/layouts/brand assets. Remove unused placeholders/groups rather than leaving empty shells. Preserve intended hierarchy instead of forcing every content block into a title-and-bullets slide.

## Render QA

A valid PPTX package can still be a bad deck. Before delivery:
1. validate/openability where tooling permits;
2. render slides to images/PDF;
3. inspect a montage for rhythm/consistency;
4. inspect dense or important slides full-size;
5. check clipping, overlap, overflow, tiny text, missing images/fonts, chart labels, contrast, stray placeholders, citations and speaker-note expectations;
6. fix source and re-render.

Font substitution can make sandbox renders differ from PowerPoint. Use known-compatible fonts when fit is critical or leave enough slack and state the limitation when the requested font cannot be verified locally.

## Upstream patterns reviewed

- `siril9/presentation-skill@311e29920c7c7ab37a93c12676bab7baecc0f4a6` (MIT): source-first workspaces, explicit content/evidence/asset plans, editable PPTX, role/layout grammars, render and delivery QA, scientific/clinical/data-heavy deck workflows.
- `anthropics/skills` PPTX skill at reviewed corpus commit `34040c9c568585f6929bedeaad110ad08f079624`: strong create/edit/template/render/validate patterns, but its PPTX materials are proprietary. DEDAL uses it only as comparative design evidence and does not copy or derive protected material.
- Other public PptxGenJS agent skills corroborate editable-native objects plus render/overflow/font QA as a durable workflow.
