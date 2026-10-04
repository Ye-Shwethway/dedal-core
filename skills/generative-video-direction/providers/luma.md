# Luma Dream Machine — current adapter notes

_Last reviewed: 2026-10-04. Verify Luma first-party documentation at execution time._

Current Dream Machine guidance supports:

- start/end keyframes for keyframe-to-keyframe generation;
- extension toward an image keyframe;
- video-to-video Modify workflows;
- Ray3 Modify combinations of input video, start/end keyframes, and character reference in supported modes.

DEDAL implication: for a dense source sequence, pairwise keyframe segments are a natural compilation path. When an already-good motion path exists, Modify/video-reference workflows may preserve motion more reliably than reconstructing it from sparse stills.
