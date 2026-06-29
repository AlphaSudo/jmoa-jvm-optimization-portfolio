# Patient-Service Phase 31 Summary

## Status

```text
case: patient-service
source: private/internal
candidate: C2
runtime mode: expanded classpath
CDS: per-candidate trained archives
runtime javaagent: absent
status: confirmed
```

## Official Phase 31D-P2 Claim

| Metric | Baseline median | C2 median | Delta |
| --- | ---: | ---: | ---: |
| PSS | 330.9 MB | 326.7 MB | -4.2 MB |
| Private_Dirty | 288.1 MB | 283.8 MB | -4.3 MB |
| `memory.current` | 419.5 MB | 415.1 MB | -4.4 MB |
| startup | 27.7 s | 34.0 s | +6.3 s |

Additional claim:

```text
9/9 individual post-workload memory measurements favored C2.
```

## Phase 31E Independent Evidence

| Metric | Delta |
| --- | ---: |
| PSS | -2.7 MB |
| Private_Dirty | -2.6 MB |
| `memory.current` | -2.9 MB |
| RSS | -2.9 MB |

Phase 31E is supporting evidence. It does not replace the official Phase 31D-P2 claim.

## Claim Boundary

Use:

```text
Patient-service official claim is ~4.2-4.4 MB median memory reduction under expanded classpath with per-candidate CDS, with 9/9 individual wins.
```

Do not mix:

```text
31D-P2 medians
31E independent evidence
fixed-plugin smoke validation
```
