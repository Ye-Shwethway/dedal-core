# Veo — current adapter notes

_Last reviewed: 2026-10-04. Verify first-party Google documentation at execution time._

Current Veo 3.1 guidance documents:

- image-to-video;
- first+last-frame interpolation;
- up to three content reference images in supported Veo 3.1 workflows;
- video extension from previously generated Veo output;
- portrait/landscape generation and native audio in supported variants.

DEDAL implication: a dense canonical source sequence should normally be compiled into short overlapping first/last segments (`A->B`, `B->C`, ...), unless a different verified control surface is available. Use content references to reinforce identity/product appearance, not as a substitute for missing temporal bridge states.
