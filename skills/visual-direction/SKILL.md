---
name: visual-direction
description: Plan, generate, edit, review, and refine image-production work with reference authority, identity/trait consistency, composition control, drift detection, and bounded visual QA.
---

# Visual Direction / Image Production

Use this skill when image quality depends on preserving a subject, style, composition, or canonical visual state across generations/edits rather than merely asking for a one-off picture.

## Core lifecycle

`define purpose -> establish reference hierarchy -> lock canonical traits -> plan shot/set -> generate/edit -> inspect visually -> classify drift -> revise narrowly -> accept/reject -> persist durable visual truth`

## Rules

1. **Reference authority before prompting** — identify which image(s) control identity, body/shape, hairstyle/grooming, wardrobe, composition, style, and environment. One image need not control every dimension.
2. **Canonical traits are explicit** — write down the few traits that must survive variation; separate them from intentionally variable traits.
3. **Small reference sets beat ambiguous piles** — use the smallest reference set that establishes the needed constraints; explain each reference's role.
4. **Separate identity from art direction** — subject identity, pose/composition, wardrobe, environment, lighting, and style are distinct control dimensions. Do not let a style reference silently redefine identity.
5. **Plan before batch generation** — define shot purpose, framing, camera relation, pose/action, environment, wardrobe, lighting/mood, and what must remain invariant.
6. **Edit locally when the problem is local** — if one trait or region is wrong, prefer targeted correction over re-generating unrelated content.
7. **Drift is a defect class** — detect identity drift, anatomy/proportion drift, wardrobe/prop drift, composition drift, style drift, age/grooming drift, and continuity drift separately.
8. **Visual inspection is required for visual claims** — prompt/source inspection alone is not evidence that the rendered result matches. Inspect the actual output before acceptance.
9. **Compare against canonical references, not memory** — when a stable character/subject matters, review against accepted reference images or a durable trait sheet.
10. **Acceptance is explicit** — accepted images may become canonical anchors; rejected experiments must not silently redefine the subject or style.
11. **Metrics are advisory** — automated similarity/reward scores may help triage but do not replace human/Creator visual acceptance, especially for identity and aesthetic quality.
12. **Persist only durable visual truth** — record canonical traits, reference roles, approved anchors, and accepted direction; do not persist every failed prompt.

## Production modes

- **Identity-first** — portraits/characters where facial/body/age/grooming continuity dominates.
- **Composition-first** — posters/product/scene work where layout and spatial relations dominate.
- **Style-first** — illustration/art-direction work where visual language dominates while subject truth remains bounded.
- **Edit-first** — preserve most existing pixels/content and change only specified elements.
- **Set/series** — multiple images must share a coherent subject, era, wardrobe logic, grade, and photographic/art direction.

## Pairing

Pair with image-generation/editing tools for execution, Interface Design when the image belongs to a UI/product surface, Writing/Editorial for embedded copy, and Files/Knowledge state when canonical references or approved anchors must persist.

Do not invent a user's physical traits from memory when an authoritative current reference is required. Do not claim identity consistency without inspecting the produced image.