# Evidence index

## Current publications

| Release | Records | Scope |
| --- | --- | --- |
| Stable 2.1 | [PetClinic summary](v2.1/petclinic-direct-ram-win.md), [JSON](v2.1/petclinic-direct-ram-win.json) | Accepted 14.88 MiB PSS / 16.24 MiB cgroup deployment saving; packaging-inclusive; bounded CPU/startup costs |
| Provisional 2.15 | [Patient benchmark](v2.15/patient-scoped-ram-benchmark.md), [JSON](v2.15/patient-scoped-ram-benchmark.json) | 8.38 MiB median stopped PSS; conditional lower bound 8.19 MiB; original calibration failed with approved exception; performance bounds unqualified or failed; no new Maven binaries |

Patient startup/cache warmth, production parity and uploaded-binary parity are
unqualified. Its complete pair/cost/identity record is copied from the source
publication; raw inputs remain private and inspection is not external replication.

## Historical research

The `doctor`, `patient`, `petclinic` and `v2-final` folders preserve earlier
protocol-specific investigations. Their values are unchanged and labeled
historical. They explain product hardening and rejected hypotheses; they do
not replace or add to current release results.

- [Historical direct product matrix](v2-final/direct-product-matrix.md)
- [Historical incremental three-service matrix](v2-final/three-service-matrix.md)
- [Historical runtime reconciliation](v2-final/runtime-equivalence-investigation.md)

Use [case studies](../CASE-STUDIES/README.md) for the engineering narrative and
the source [release boundaries](https://github.com/AlphaSudo/jmoa/blob/main/docs/releases/current-state.md)
for distribution and claim status.
