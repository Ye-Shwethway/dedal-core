# Current Checkpoint

_Date: 2026-09-14_

## Repository

- Repository: `Ye-Shwethway/dedal-core`
- Visibility: public
- Default branch: `main`
- Current version: `0.18.0`
- Purpose: durable public operational core for DEDAL

## Operating phase

The initial eight-area capability expansion campaign is complete. DEDAL is now in **hardening + consolidation + outcome validation** mode, not default skill-expansion mode.

The consolidation efficiency baseline remains valid as preliminary evidence only. Numeric claims must continue to use directly observable counts or be labeled structural proxies.

## Hardening campaign state

### 1. GitHub mutation guardrails

Added an executable fail-closed mutation guard under `runtime/` plus positive/negative contract cases under `evals/github-mutation-guard/`.

The guard enforces the locked work-unit mode:
- direct mode permits one direct contents mutation and rejects atomic Git-data mutation tools;
- atomic mode permits `create_blob(s) -> create_tree -> create_commit -> update_ref`, rejects direct contents writes, rejects out-of-order transitions, and rejects mutation tools unknown to the current policy when the host marks them as mutations.

Important residual risk: the public Core repository cannot intercept native provider GitHub tools by itself. Actual platform-level prevention requires a host/tool dispatcher to route mutation calls through the guard. Until then, this is **executable contract enforcement available for integration**, not universal native-tool interception.

The v0.15 wrong-tool regression remains preserved as evidence of why instruction-only safeguards are insufficient.

### 2. Skill overlap / routing consolidation

`state/skill-consolidation.json` now classifies every live skill entrypoint with one of KEEP / TUNE / MERGE / REMOVE / NEEDS_EVIDENCE and records the primary overlap boundary.

Current classification counts:
- KEEP: 10
- TUNE: 1 (`skill-acquisition`, because the expansion campaign is complete and acquisition should now be gap-driven)
- NEEDS_EVIDENCE: 8
- MERGE: 0
- REMOVE: 0

No skill was merged or removed without representative outcome evidence.

### 3. Executable continuity checkpoint

`state/checkpoint.schema.json` and `state/current-checkpoint.json` now provide a machine-readable checkpoint carrying:
- accepted state;
- evidence;
- unresolved risks;
- next executable step;
- owner;
- last verified revision.

`python3 scripts/validate_runtime_contracts.py` validates this checkpoint shape, skill-classification coverage, and GitHub mutation-guard cases in CI.

## Consolidation / benchmark evidence

Existing benchmark evidence is preserved rather than normalized away:
- GH-01: clean atomic milestones exist, while v0.15 remains regression evidence;
- GH-02: PASS;
- RS-01: PARTIAL;
- RS-02: PASS;
- LH-01 / LH-02: still need representative continuity/recovery work;
- several expanded skills remain contract-validated but not outcome-validated.

No new universal efficiency percentage is claimed by this hardening release.

## Next executable phase

1. Integrate the mutation guard into any controllable GitHub tool dispatcher / harness surface so a locked mode can actually block disallowed provider calls before execution.
2. Shadow-score ordinary real work for the eight `NEEDS_EVIDENCE` skills and update classifications only from observed outcomes.
3. Tune Skill Acquisition routing so it activates for explicit acquisition work or a demonstrated capability gap, not roadmap momentum.
4. Exercise the machine-readable checkpoint during a real new-chat/resume cycle for LH-01/LH-02 evidence.
5. Keep MERGE/REMOVE at zero until evidence shows duplicated ownership or context/process cost that exceeds value.
