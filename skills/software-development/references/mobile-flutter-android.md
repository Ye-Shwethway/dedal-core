# Mobile Flutter/Android Reference Pack

Use this reference only when the active task materially depends on Flutter or Android-specific implementation/toolchain behavior. It does not create a separate Mobile Engineering owner.

## Routing

- Flutter/Android application implementation, architecture refactor, plugin integration, Gradle/config edits -> **Software Development** primary.
- Mobile UI responsiveness/layout/design direction -> **Interface Design** primary, with Software Development supporting implementation.
- Widget/integration/E2E/device verification and regression coverage -> **Quality Engineering** primary when independent acceptance is the goal.
- APK/AAB signing, build provenance, Play distribution, rollout/rollback -> **Release Engineering** primary.
- Local SQLite/schema/query/transaction semantics -> **Database Engineering** primary.
- Framework/toolchain docs and commands are execution/reference knowledge, not ownership.

## Flutter patterns

Adapted from `flutter/agent-plugins@7cdb7d3c33679ef14a7a7584cec1d5ecb8752586`.

- Prefer clear separation of UI/presentation, application/domain logic, and data access. Preserve project-local architecture if already coherent; do not force MVVM/Repository patterns onto every app merely because an upstream example uses them.
- Keep widgets lean; move reusable state/logic behind explicit seams that are easy to test.
- For layout failures, reason from Flutter constraints and actual widget tree before adding arbitrary wrappers or fixed dimensions.
- Use responsive primitives such as `LayoutBuilder`, `MediaQuery`, flexible constraints, and breakpoint behavior deliberately rather than device-specific hard coding.
- Add widget tests for component rendering/interactions and integration tests for critical multi-screen flows when the risk justifies them.
- Prefer stable user-visible/testable hooks (`Key`, text, semantics) over fragile tree-position assumptions.
- Routing, localization, HTTP, serialization, and preview guidance should be loaded only when the task needs that concern.

## Android-native / build-system patterns

Adapted from `android/skills@bac232fd02b0855df9275281a2a7a47643768719`.

- Use official Android guidance first for AGP/Gradle/JDK/Kotlin compatibility, target/compile SDK behavior, platform migrations, Play requirements, R8/shrinker analysis, CameraX, edge-to-edge, and other version-sensitive workflows.
- Treat toolchain upgrades as migrations: inspect current versions, compatibility matrix, breaking changes, plugin constraints, generated code processors, and verification path before editing.
- Do not blindly copy fixed dependency versions from this reference pack. Current stable/recommended versions are drift-sensitive and must be verified from official Android/Flutter/Dart/Gradle sources when material.
- Preserve project-local Flutter-generated Android structure unless a platform-specific change actually requires native edits.
- Prefer targeted Gradle verification over ritual `clean` builds; inspect the failing layer before broad cache deletion.
- Platform migrations should carry explicit compatibility and rollback/recovery thinking when they can affect production builds.

## Testing and evidence

- A successful compile does not prove runtime behavior on representative devices.
- Emulator success does not automatically prove physical-device behavior, especially for camera, storage, notifications, background execution, biometrics, billing, permissions, graphics, and OEM-sensitive behavior.
- Framework unit/widget tests, integration tests, native instrumentation, build checks, and Creator/device acceptance are different evidence layers.
- When converting exploratory interactions into durable tests, preserve the behavior oracle rather than merely recording taps.

## Freshness boundary

Verify current official docs when the answer depends on:
- Flutter/Dart/Android/AGP/Gradle/Kotlin/JDK versions or compatibility;
- target/compile SDK requirements or Play policy deadlines;
- deprecated/replaced APIs, migration flags, plugin compatibility, or build commands;
- release/signing/billing/store requirements;
- tooling/MCP/CLI command surfaces.

Stable engineering principles may live here; fast-moving version facts should not.
