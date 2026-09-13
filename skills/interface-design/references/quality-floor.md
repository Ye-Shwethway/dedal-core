# Quality Floor

Use this as a compact review lens, not a universal style preset.

## Hierarchy and content
- The primary task or message should be obvious without scanning every element.
- Group related content; separate unrelated decisions.
- Labels and actions should describe outcomes, not implementation jargon.
- Empty, loading, error, disabled, success, and destructive states should be coherent where relevant.

## Layout and responsiveness
- Prefer structural layout primitives over fragile pixel/flex arithmetic.
- Check narrow and wide widths; avoid desktop-only assumptions.
- Preserve touch targets, readable measure, stable viewport behavior, and sensible overflow.
- Repeated patterns should share spacing/alignment logic rather than drift instance by instance.

## Typography and color
- Typography should create hierarchy and rhythm before decorative effects do.
- Maintain readable line length, line-height, and contrast.
- Accent color should carry meaning or brand intent, not compensate for weak hierarchy.
- Existing brand/type choices win unless redesign scope explicitly changes them.

## Interaction and motion
- Motion should clarify causality, hierarchy, feedback, or spatial change.
- Respect reduced-motion preferences where applicable.
- Hover-only meaning is insufficient on touch devices.
- Focus/keyboard states must remain visible for interactive web surfaces.

## Accessibility and resilience
- Use semantic controls and labels before custom interaction hacks.
- Verify contrast, focus order, accessible names, and state announcements when material.
- Preserve localization room and avoid layouts that depend on one string length.
- Do not hide failures behind visual polish: error recovery and product truth outrank aesthetics.

## Anti-template check

Before shipping, ask: which choices came from the brief/product and which came from model habit? Replace only the habit-driven choices that weaken coherence. Distinctiveness is a means to fit, not an obligation to be loud.
