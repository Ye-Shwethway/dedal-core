# Artifact Identity and Provenance

Release evidence should connect an artifact to the source and build process that produced it.

## Minimum attribution

For releasable binaries/packages/images, record as appropriate:
- source repository;
- exact commit/ref;
- release version/channel;
- workflow/build run;
- artifact filename/package/image identity;
- cryptographic hash/digest;
- build/runtime/toolchain versions when they affect reproducibility;
- provenance/attestation identity when available.

## Evidence strength

From weaker to stronger:
1. filename/version label;
2. CI artifact linked to a run;
3. hash/digest linked to exact source commit;
4. signed provenance/attestation linking source, workflow, identity, and artifact digest;
5. policy verification at consumption/deployment time.

Do not claim a stronger level from weaker evidence.

## Attestations

Artifact attestations are useful when consumers or deployment policy actually verify them. Generation without verification adds traceability but does not by itself enforce trust.

Treat provenance as an answer to `where/how did this artifact come from?`, not `is this artifact bug-free or non-malicious?`.

## Supply-chain checks

For higher-risk releases consider:
- pinned workflow actions/dependencies;
- trusted build runners/reusable workflows;
- minimal workflow permissions;
- SBOM generation where dependency visibility matters;
- signing/attestation;
- dependency/source provenance;
- verification before promotion/deployment.

Choose controls proportionate to project risk rather than maximizing ceremony.
