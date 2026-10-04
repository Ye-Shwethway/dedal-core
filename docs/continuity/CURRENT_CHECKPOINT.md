# Current Checkpoint

> Machine authority: `state/checkpoint.yaml` and `state/current-checkpoint.json`.

- Core version: `0.38.2`.
- Direct Library Core root: `/DEDAL/core`.
- GitHub public history base recorded in `core-manifest.yaml`; upstream 0.38.2 sync is pending.
- External DEDAL Runtime MCPs are retired.
- Active skill entrypoints and task-profile required references must exist in the complete `core-files.json` inventory.
- Run `validators/validate_core.py`, `scripts/validate_profile_probe.py`, `scripts/validate_session_receipt.py`, and `scripts/session_check.py` after Core changes. The latter reports structural readiness without a task receipt; receipt coverage is not independent proof of source use.

Domain-specific accepted state remains in the machine checkpoint, registered skills, and task-relevant private overlay. Older checkpoints and release notes are historical evidence.
