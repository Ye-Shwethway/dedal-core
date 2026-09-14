# Mobile Engineering Reference Audit — 2026-09-14

## Decision

**Do not promote a top-level Mobile Engineering faculty at this checkpoint.**

Flutter and Android contain valuable specialist knowledge, but the audited workflows route cleanly through existing DEDAL owners. Promote a shared reference pack instead of another active owner.

## Sources

- `flutter/agent-plugins@7cdb7d3c33679ef14a7a7584cec1d5ecb8752586` — first-party Flutter team corpus.
- `android/skills@bac232fd02b0855df9275281a2a7a47643768719` — first-party Android team corpus, Apache-2.0.
- Current Flutter and Android developer documentation for freshness-sensitive concepts.

## Why not a new faculty

The Flutter corpus is organized around task recipes: architecture, widget/integration tests, responsive layouts, layout debugging, routing, localization, HTTP, serialization, and previews. These map directly onto Software Development, Interface Design, and Quality Engineering.

The Android corpus explicitly says it prioritizes workflows where evaluations show LLMs underperform rather than duplicating areas the model already handles well. Its strongest examples are targeted toolchain/platform recipes such as AGP migrations, R8 analysis, CameraX, and platform-specific changes. This strongly supports progressive references rather than a broad permanent Mobile owner.

A Mobile Engineering owner would currently duplicate four already-clear authorities:
- Software Development — app/framework implementation, architecture, Gradle/config code changes;
- Interface Design — responsive UX/UI direction;
- Quality Engineering — independent widget/integration/device/readiness verification;
- Release Engineering — APK/AAB/build/signing/store promotion and rollback.

Database Engineering continues to own SQLite/local database semantics; Security Engineering owns permissions/trust policy when security is primary.

## Adapted patterns

1. **Framework guidance is scoped, not constitutional.** Upstream MVVM/Repository or specific test recipes are useful defaults, not reasons to rewrite accepted project architecture.
2. **Version-sensitive mobile facts stay live.** AGP/Gradle/Kotlin/JDK/SDK/Play policy/plugin compatibility and tool commands drift quickly and require current official documentation when material.
3. **Build-tool upgrades are migrations.** Inspect compatibility matrices, breaking changes, generated-code processors/plugins, and explicit verification paths.
4. **Evidence is layered.** Compile/build success, emulator behavior, integration tests, physical-device behavior, and store acceptance are distinct evidence layers.
5. **Exploration can become durable tests.** Tool/MCP-driven exploratory interaction is useful when converted into an explicit behavior oracle, not merely replayed gestures.
6. **Mobile-specific debugging should remain targeted.** Layout constraints, R8/shrinker failures, camera/device behavior, OEM/permission/background behavior, and native build failures should load only the relevant reference.
7. **Do not install all vendor skills by default.** Pull the smallest task-specific reference needed.

## Promotion gate for a future Mobile Engineering owner

Reconsider only if representative work repeatedly shows a stable ownership layer that cannot be cleanly expressed as framework implementation + UI direction + QA + release. Evidence should show routing or outcome gains, not just frequent Flutter/Android usage.

Possible future signals include cross-platform lifecycle/background execution, platform channel architecture, mobile permissions/device capability coordination, store/runtime compatibility, or mobile-specific observability becoming a repeated multi-project reasoning domain with no clear existing owner.

## Result

Reference-pack promotion approved. Top-level Mobile Engineering promotion rejected for now.
