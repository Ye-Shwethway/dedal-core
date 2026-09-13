# Harness Benchmark Scorecard

## Per-case result

Use one primary result:
- **PASS** — all primary assertions observed; no material regression.
- **PARTIAL** — goal mostly met but one assertion is unverified or one non-critical regression occurred.
- **FAIL** — correctness/evidence/authority failed, or a listed regression materially occurred.

## Diagnostic dimensions

Record only when observable:
- correctness: 0/1
- verification: 0/1
- recovery: 0/1 or N/A
- context discipline: 0/1
- tool efficiency: 0/1
- authority/safety: 0/1
- continuity: 0/1 or N/A

These are diagnostics, not a fake precision score. Missing observability is `N/A`, not zero.

## Promotion rule

Harness v1 may be called **outcome-validated on the smoke suite** only when:
1. all six cases have been exercised on representative real or controlled tasks;
2. no correctness, authority, or completion-evidence regression is observed;
3. at least one previously observed harness failure is demonstrably avoided or recovered better;
4. efficiency improvements are not purchased by weaker correctness or verification.

Until then, describe status as **contract-validated with accumulating outcome evidence**.

## Creator role

Creator feedback records product acceptance, friction, unwanted questions, and intent mismatch. It is valuable but is not required to adjudicate low-level technical correctness when tests/readback/authoritative sources can do so.
