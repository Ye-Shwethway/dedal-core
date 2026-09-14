#!/usr/bin/env python3
"""Fail-closed GitHub mutation-mode guard for DEDAL harness adapters.

This module does not intercept provider tools by itself. A host must call check()
before a mutation and record_success() only after that mutation succeeds.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable


class GuardViolation(RuntimeError):
    pass


class MutationGuard:
    def __init__(self, policy: dict, mode: str):
        self.policy = policy
        self.mode = mode
        self.completed: list[str] = []
        if mode not in policy.get("modes", {}):
            raise GuardViolation(f"unknown mutation mode: {mode}")

    @property
    def mode_policy(self) -> dict:
        return self.policy["modes"][self.mode]

    def check(self, tool: str, *, is_mutation: bool = True) -> None:
        if not is_mutation:
            return

        known = set(self.policy.get("known_mutators", []))
        if tool not in known:
            raise GuardViolation(f"unknown mutation tool rejected fail-closed: {tool}")

        allowed = set(self.mode_policy.get("allowed_mutators", []))
        if tool not in allowed:
            raise GuardViolation(f"tool {tool} is forbidden while mode {self.mode} is locked")

        if self.mode == "direct-single-file":
            limit = int(self.mode_policy.get("max_successful_mutations", 1))
            if len(self.completed) >= limit:
                raise GuardViolation("direct-single-file work unit already consumed its mutation")
            return

        if self.mode == "atomic-multi-file":
            self._check_atomic_sequence(tool)
            return

        raise GuardViolation(f"mode has no executable guard implementation: {self.mode}")

    def _check_atomic_sequence(self, tool: str) -> None:
        phases = self.mode_policy["ordered_phases"]
        repeatable = set(self.mode_policy.get("repeatable", []))

        if not self.completed:
            allowed_phases = [0]
        else:
            last = self.completed[-1]
            phase_for_last = next(i for i, phase in enumerate(phases) if last in phase)
            if last in repeatable:
                allowed_phases = [phase_for_last]
                if phase_for_last + 1 < len(phases):
                    allowed_phases.append(phase_for_last + 1)
            else:
                allowed_phases = [phase_for_last + 1]

        allowed_phases = [i for i in allowed_phases if i < len(phases)]
        if not allowed_phases:
            raise GuardViolation("atomic work unit is already complete")

        if not any(tool in phases[i] for i in allowed_phases):
            expected = " or ".join(", ".join(phases[i]) for i in allowed_phases)
            raise GuardViolation(
                f"atomic sequence violation: got {tool}; expected: {expected}"
            )

    def record_success(self, tool: str, *, is_mutation: bool = True) -> None:
        self.check(tool, is_mutation=is_mutation)
        if is_mutation:
            self.completed.append(tool)

    @property
    def complete(self) -> bool:
        if self.mode == "direct-single-file":
            return len(self.completed) == int(self.mode_policy.get("max_successful_mutations", 1))
        if self.mode == "atomic-multi-file":
            return bool(self.completed) and self.completed[-1] == "update_ref"
        return False


def load_policy(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def validate_trace(policy: dict, mode: str, tools: Iterable[str]) -> MutationGuard:
    guard = MutationGuard(policy, mode)
    for tool in tools:
        guard.record_success(tool)
    return guard


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy", type=Path, default=Path(__file__).with_name("github-mutation-policy.json"))
    parser.add_argument("--mode", required=True)
    parser.add_argument("tools", nargs="+")
    args = parser.parse_args()

    try:
        guard = validate_trace(load_policy(args.policy), args.mode, args.tools)
    except GuardViolation as exc:
        print(f"REJECTED: {exc}")
        return 2

    print(json.dumps({"accepted": True, "mode": args.mode, "completed": guard.completed, "complete": guard.complete}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
