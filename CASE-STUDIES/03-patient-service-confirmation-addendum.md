# Patient-Service Confirmation Addendum

## Purpose

This addendum summarizes the confirmed patient-service win without exposing private/internal source details. Patient-service is the first JMOA service win and remains the baseline internal case.

## Official Claim

Official production claim:

```text
Phase 31D-P2
Candidate: C2
Runtime mode: expanded classpath
CDS: per-candidate trained archives
Runtime javaagent: absent
Result: ~4.2-4.4 MB median container memory reduction
Individual wins: 9/9
```

Official median table:

| Metric | Baseline median | C2 median | Delta |
| --- | ---: | ---: | ---: |
| PSS | 330.9 MB | 326.7 MB | -4.2 MB |
| Private_Dirty | 288.1 MB | 283.8 MB | -4.3 MB |
| `memory.current` | 419.5 MB | 415.1 MB | -4.4 MB |
| startup | 27.7 s | 34.0 s | +6.3 s |

The startup cost was documented and accepted as a tradeoff for a long-running service profile.

## Independent Evidence Run

Phase 31E produced independent evidence with smaller but consistent container-level savings:

| Metric | Baseline | C2 | Delta |
| --- | ---: | ---: | ---: |
| PSS | 328.0 MB | 325.3 MB | -2.7 MB |
| Private_Dirty | 285.5 MB | 283.0 MB | -2.6 MB |
| `memory.current` | 417.3 MB | 414.4 MB | -2.9 MB |
| RSS | 307.4 MB | 304.5 MB | -2.9 MB |

Phase 31E is supporting evidence, not the official median claim. Do not mix the two.

## Runtime Shape

Patient-service used expanded classpath mode:

```text
java @jvm-flags -cp @optimized-classpath <application-main>
```

This made optimized dependency ordering easy to verify and avoided Spring Boot fat-JAR substitution risk.

## Candidate Shape

Public-safe candidate summary:

- MODE_C
- PACKAGE_SAM
- warmed adapter-reuse policy
- 330 eligible sites
- 317 planned sites
- 168 rewritten classes
- 95 logical adapters
- failed classes: 0
- workload errors: 0

## Fixed-Plugin Regression Status

Later plugin fixes from the Doctor-service path changed adapter placement and validation behavior. Patient-service was smoke-tested under the fixed plugin as a correctness regression gate.

Stable invariants:

- eligible sites: 330
- planned sites: 317
- rewritten classes: 168
- logical adapters: 95
- missing adapter references: 0
- runtime smoke: passed
- CDS mapped: true
- warmup: passed

This proved correctness safety under the fixed plugin, but it was not a new full patient memory remeasurement.

## Claim Integrity

Use:

```text
Patient-service official claim is Phase 31D-P2: ~4.2-4.4 MB median memory reduction, 9/9 individual wins.
```

Also acceptable:

```text
Phase 31E independently reproduced the direction with ~2.7-2.9 MB container memory savings.
```

Do not say:

```text
Phase 31E replaces the official Phase 31D-P2 claim.
The fixed-plugin smoke is a new memory confirmation.
```

## Final Claim

Patient-service confirms JMOA C2 as an internal expanded-classpath/CDS win:

```text
~4.2-4.4 MB official median memory reduction
9/9 individual memory wins
no runtime javaagent
per-candidate CDS archives
startup tradeoff documented
```
