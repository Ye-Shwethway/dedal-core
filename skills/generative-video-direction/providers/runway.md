# Runway — current adapter notes

_Last reviewed: 2026-10-02. Verify Runway first-party documentation at execution time._

Current Gen-4.5 guidance emphasizes:

- image-to-video input establishes composition/subject/lighting/style;
- text should primarily describe motion, camera work and temporal progression;
- start simple and add detail strategically;
- current mode/duration/aspect/resolution support is model/version specific.

DEDAL implication: keep I2V prompts motion-focused and diagnose conflicts between implied motion in the input image and requested motion before adding prompt complexity.
