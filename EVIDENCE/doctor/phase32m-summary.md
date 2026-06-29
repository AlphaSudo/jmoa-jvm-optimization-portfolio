# Doctor-Service Phase 32M Summary

## Status

```text
case: doctor-service
source: private/internal
runtime mode: corrected Spring Boot fat JAR
CDS: per-candidate
candidate: D2-fixed
status: confirmed modest win
```

## Final Audited Result

| Metric | Result |
| --- | ---: |
| Median PSS reduction | ~2.7 MB |
| Median Private_Dirty reduction | ~1.8 MB |
| Paired-delta median | ~2.0 MB |
| Paired PSS wins | 3/3 |
| Workload errors | 0 |
| Runtime javaagent | absent |

## Important Correction

The initially reported -5.9 MB Doctor median was incorrect. The final audited median is ~2.7 MB PSS reduction.

## Technical Lesson

Doctor-service proved that JMOA must own fat-JAR materialization. Optimized dependency JARs outside `BOOT-INF/lib` are not enough; Spring Boot must load the optimized nested JARs at runtime.

## Product Hardening From This Case

- fat-JAR substitution fix
- PACKAGE_SAM multi-root adapter emission
- post-weave adapter self-heal
- `AdapterReferenceValidator`
- corrected median audit
