# Runway — current adapter notes

_Last reviewed: 2026-10-04. Verify Runway first-party documentation at execution time._

Current Runway guidance separates several control surfaces:

- image-to-video, where the input image establishes the initial composition/subject/light/style and text focuses on motion/camera progression;
- reusable image/media references for character, object, scene, and style control;
- keyframe/edit workflows in current Apps/Edit Studio surfaces;
- video-to-video / modification workflows for preserving or changing existing motion.

DEDAL implication: do not assume every Runway video model accepts an arbitrary ordered keyframe stack. Compile the canonical source sequence to the specific verified mode. When I2V is used, keep prompts motion-focused and avoid simultaneously demanding large subject and camera changes from one start image.
