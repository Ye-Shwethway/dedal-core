# Adaptation Notes — Release Engineering

DEDAL Release Engineering synthesizes current supply-chain and deployment guidance into a project-agnostic release contract.

## Primary influences reviewed 2026-09-14

- SLSA framework repository `slsa-framework/slsa` @ `54b88b009fd45acb331c7e6578a526e0f36e0430` and current SLSA provenance/build guidance.
- Current GitHub Actions artifact-attestation documentation: provenance binds repository, workflow, environment/event and commit to an artifact; verification is required for security benefit.
- GitHub Actions security guidance for OIDC/cloud authentication and least-privilege workflows.
- Sigstore/Cosign documentation for identity-based signing, short-lived certificates, transparency-log evidence and verification.
- Semantic Versioning 2.0.0 as a compatibility-communication model, not a universal ecosystem mandate.

## Adopted

- source-to-artifact attribution as a first-class release property;
- separation of build, artifact, deploy and runtime evidence;
- signed provenance/attestation when useful and actually verified;
- staged promotion proportional to risk;
- explicit rollback/forward-fix planning;
- short-lived identity-based deployment credentials where supported;
- supply-chain controls as part of release engineering rather than post-hoc security theater.

## Rejected / generalized

- requiring SLSA level targets for every small project;
- signing every CI output regardless of consumption;
- treating attestation as proof that software is secure/correct;
- universal SemVer when platform/ecosystem versioning differs;
- provider-specific GitHub/Sigstore mechanics as the only valid implementation.

Release platform syntax, current action versions and deployment semantics must be verified live before production changes.
