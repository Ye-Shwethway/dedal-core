# Infrastructure Change Safety and Recovery

Use this reference for high-impact infrastructure changes, partial applies, recovery, provider boundaries, and machine-image workflows.

## Risk model

Raise scrutiny when changes can destroy or replace persistent resources, alter identity/addressing, change trust/network boundaries, rotate credentials, modify state backends, or fan out across many dependent resources.

## Partial apply

Infrastructure operations can succeed for some resources and fail for others. Do not describe this as rollback unless the tool/provider actually reversed effects. Re-inspect live resources and state, then choose retry, compensating change, preserve-partial, or escalation according to the Cognitive Runtime recovery contract.

## State/backend safety

- Protect remote state and locking according to the actual backend/provider model.
- Treat direct state edits, force-unlock, backend migration, and state replacement as elevated operations.
- Backups/snapshots improve recovery options but do not prove semantic reversibility.
- Never expose state contents casually; state can contain sensitive provider/resource data.

## Provider boundary

Infrastructure Engineering owns lifecycle/reconciliation semantics. Provider-specific architecture remains with the relevant platform owner or current first-party docs. For example, Cloudflare product topology belongs to Cloudflare Platform even when Terraform manages it.

## Machine images / Packer

Image builds are infrastructure supply-chain artifacts. Preserve source/template/plugin provenance and verify the resulting image where risk warrants it. Building an image successfully does not prove instances launched from it are healthy; runtime health belongs to Reliability Engineering.

## Verification ladder

1. configuration validates/formats as appropriate;
2. plan/change preview is reviewed;
3. apply/build/import operation completes as observed;
4. state and provider reality reconcile as intended;
5. downstream service/runtime behavior is verified by the appropriate owner.

Never collapse these layers into one success claim.
