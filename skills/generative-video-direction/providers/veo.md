# Veo — current adapter notes

_Last reviewed: 2026-10-02. Verify first-party Google documentation at execution time._

Observed high-value control patterns in Veo 3.1 guidance:

- image-to-video;
- consistent-element/reference-image workflows ("ingredients to video");
- first+last-frame transitions;
- synchronous audio/dialogue in supported modes;
- staged workflows that create visual anchors first, then animate them.

DEDAL implication: use first/end visual states when terminal geometry/camera transition matters; do not force all scene truth into one text prompt. Exact limits and mode availability are volatile.
