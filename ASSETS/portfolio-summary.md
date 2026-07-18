# JMOA V2 Portfolio One-Page Summary

## Evidence-Driven JVM Footprint Optimization For Spring Boot

JMOA combines build-time lambda/adapter transformation, raw dependency
classfile-metadata reduction, artifact auditing, Spring Boot materialization,
runtime-origin proof, paired evidence validation, and memory attribution.

## Final V2 Result

| Service | Deployment and policy | Median PSS, V1 to V2 | Wins |
| --- | --- | ---: | ---: |
| PetClinic customers | Exploded Boot, `NO_CDS_LOW_DIRTY` | -6,012 KB | 2/3 |
| Doctor | Fat JAR, `APPLICATION_CDS` | -5,156 KB | 3/3 |
| Patient | Fat JAR, `JDK_BASE_CDS_LOW_DIRTY` | -8,279 KB | 3/3 |

All three comparisons have 6/6 valid runs, zero workload errors, V2-C
`CONFIRMED_WIN`, and V2-D attribution.

## Engineering Pipeline

```text
analyze artifact and workload
-> admit bounded candidates
-> transform bytecode at build time
-> audit non-target classfile structures
-> materialize the real Spring Boot deployment
-> prove artifact identity and runtime origins
-> execute the semantic workload
-> run paired confirmation
-> validate evidence and attribute memory movement
```

## Runtime Policy Is Part Of The Product

- PetClinic: no-CDS confirmed.
- Doctor: application CDS confirmed with artifact-specific archives.
- Patient: stock JDK base CDS confirmed; no-CDS also independently confirmed.
- Patient dynamic application CDS: rejected for the tested deployment.

JMOA does not claim that one CDS mode, launch shape, or allocator policy is
universally optimal.

## Why The Evidence Is Credible

- PSS and Private_Dirty are primary process-memory metrics.
- `memory.current`, NMT, smaps regions, heap, histograms, classes, and metaspace
  support attribution.
- Single runs are screens; final claims use three balanced pairs.
- Invalid runs and losing pairs remain visible.
- Runtime javaagents are absent from final service claims.
- Negative candidates are rejected rather than promoted from artifact savings.

## Public Reproduction Bridge

Spring PetClinic customers-service is the public reference: clean-clone build
and semantic-smoke workflow, exploded Boot / `JarLauncher`, no CDS/AppCDS/
Leyden, and no runtime javaagent. Frozen measurement inputs remain explicit
prerequisites rather than hidden release assets.

Source: https://github.com/AlphaSudo/jmoa

Portfolio: https://github.com/AlphaSudo/jmoa-jvm-optimization-portfolio
