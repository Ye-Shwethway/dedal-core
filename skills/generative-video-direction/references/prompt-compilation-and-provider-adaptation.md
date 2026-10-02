# Prompt Compilation and Provider Adaptation

The provider-neutral Motion Shot Spec is authoritative. Prompts, JSON, UI instructions, and parameter sets are compiled execution artifacts.

## Compilation order

1. Choose the provider mode/control surface.
2. Map authoritative references to supported input slots/roles.
3. Write only the temporal/visual information the provider still needs.
4. Add camera/timing/audio controls supported by the current mode.
5. Add preserve/change constraints only where the provider can use them meaningfully.
6. Keep unsupported controls out of the package or label them as approximations.

## Image-to-video rule

When the image fixes appearance, composition, lighting and style, prompt primarily:

- subject action;
- environmental motion;
- camera behavior;
- timing/pace;
- direction/speed;
- intended end state or change.

Do not redescribe the entire frame unless a visual transformation is actually intended.

## Provider-neutral first

A project may target several generators. Preserve one Motion Shot Spec and compile separate provider contracts rather than letting provider syntax become project truth.

## Complexity discipline

Start with the smallest wording/control package that expresses the important motion. If a take fails, add or change one material control at a time when practical so causality remains diagnosable.

## No capability hallucination

If a current provider feature has not been verified, mark it `unknown` and choose a supported alternative or request fresh research. Do not infer support from another model/version/product surface.
