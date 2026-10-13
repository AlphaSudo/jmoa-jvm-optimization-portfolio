# JMOA: current portfolio summary

## Evidence-gated JVM footprint engineering

JMOA combines representative profiling, bounded lambda/adapter transformation,
audited classfile metadata reduction, Spring Boot materialization, runtime-origin
proof, semantic workloads and paired Linux memory evidence.

| Publication | Observation | Qualification |
| --- | --- | --- |
| Stable 2.1 PetClinic | 14.88 MiB lower process PSS; 16.24 MiB lower target-cgroup RAM | 12 held-out blocks; accepted packaging-inclusive deployment result; lifecycle CPU +14.71%, startup +1.652 s within frozen gates |
| Provisional 2.15 Patient | 8.38 MiB lower median stopped PSS; conditional lower bound 8.19 MiB | 12 paired Java 26/Leyden blocks; original calibration failed with approved post-observation exception; performance bounds unqualified or failed |

Patient startup/cache warmth and production/uploaded-binary parity remain
unqualified. JMOA 2.15 publishes evidence only, with no new Maven binaries;
stable plugin/runtime coordinates remain 2.1.0. These are distinct service and
runtime studies, not a version-improvement comparison.

## Engineering demonstrated

- JVM bytecode analysis, conservative admission, adapter generation and validation.
- Raw LVT/LVTT reduction with non-target preservation and signed/MR/sealed exclusions.
- Fat-JAR/exploded-Boot materialization, SHA-256 lineage and loaded-origin proof.
- smaps/PSS, cgroup v2, NMT, heap, class/metaspace, JIT and fault investigation.
- Frozen paired designs, controls, held-out confirmation, failed-attempt accounting.
- Explicit cost, calibration, observability and reproducibility limitations.

The PetClinic build/smoke workflow needs frozen input prerequisites and does
not alone reproduce the memory campaign. Private Patient raw source and
measurements are not distributed. See the [evidence index](../EVIDENCE/README.md).

- [Stable 2.1 release](https://github.com/AlphaSudo/jmoa/releases/tag/v2.1.0)
- [Provisional 2.15 release](https://github.com/AlphaSudo/jmoa/releases/tag/v2.15)
- [Source repository](https://github.com/AlphaSudo/jmoa)
