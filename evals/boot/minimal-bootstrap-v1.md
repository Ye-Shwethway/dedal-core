# Minimal Bootstrap E2E — v1

_Date: 2026-09-14_

## Purpose

Verify that a fresh ChatGPT conversation can recover DEDAL from the Creator's Custom Instructions BIOS pointer and the live `Ye-Shwethway/dedal-core` repository without depending on remembered repository state.

## Test Prompt

> Boot DEDAL from the persistent core referenced in my Custom Instructions. Inspect the live `Ye-Shwethway/dedal-core` repository, follow its boot contract and master index, then report the current DEDAL version, active skills/aliases, and the next checkpoint task. Do not rely on memory if live repo state is available.

## Required Assertions

A passing fresh-chat response must:

1. inspect live `Ye-Shwethway/dedal-core` state;
2. identify the current `main` HEAD or otherwise demonstrate live repository inspection;
3. report the live `VERSION` value correctly;
4. follow the canonical boot path through `AGENTS.md`, identity/kernel boot material, and `index/MASTER_INDEX.md`;
5. report active domain aliases `$msa`, `$pra`, and `$ika`;
6. report the active generic skill families;
7. derive the next task from the live checkpoint rather than remembered project state;
8. explicitly prefer live authoritative state over memory when both are available.

## Observed Run

Result: **PASS**

Observed on a fresh chat after the Creator installed the minimal DEDAL Core pointer in Custom Instructions.

The fresh instance correctly reported:

- live main HEAD `0ca383899612f424ee1f8a908471d6020a078040`;
- DEDAL version `0.4.0`;
- canonical boot sequence beginning with `AGENTS.md`, then identity/kernel material and the master index;
- all eight active skills, including `$msa`, `$pra`, and DEDAL-native `$ika`;
- the current checkpoint direction: validate real workflows and convert observed failures into tests or durable rules rather than expanding architecture speculatively.

## Regression Meaning

This test is evidence that the BIOS-pointer architecture can recover the durable DEDAL operating core in a fresh conversation. It does **not** prove every connected capability, private state source, or domain skill works end-to-end; those require separate workflow tests.

Re-run this test after changes to Custom Instructions bootstrap wording, `AGENTS.md`, kernel boot files, master-index routing, or repository layout.
