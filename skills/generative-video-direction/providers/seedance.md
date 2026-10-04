# Seedance — current adapter notes

_Last reviewed: 2026-10-04. Verify ByteDance/BytePlus first-party documentation at execution time._

Current Seedance 2.5 / ModelArk guidance describes multiple distinct temporal-control paths:

- strict first-frame and first+last-frame image-to-video;
- ordered independent keyframes in reference workflows, with stronger visual alignment than a single multi-panel storyboard;
- timestamped or shot-numbered visual timelines;
- large reference sets and video/audio references in supported modes;
- extension/editing and seamless-transition workflows.

The docs explicitly distinguish a multi-panel storyboard (high-level plot guidance) from multiple independent keyframe images (closer visual alignment), and recommend identifying ordered keyframe images in the prompt. First/last-frame mode strictly locks those endpoints; reference-mode keyframes are more flexible but not equivalent to exact endpoint locking.

DEDAL implication: when dense source anchors exist, choose between strict adjacent-pair interpolation and ordered keyframe/reference mode based on whether exact endpoint fidelity or multi-state trajectory control matters more. Keep aspect ratios consistent. Do not assume that more references always increase stability; verify current limits and mode behavior.
