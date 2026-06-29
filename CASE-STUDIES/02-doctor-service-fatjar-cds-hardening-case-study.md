# Doctor-Service Fat-JAR/CDS Hardening Case Study

## Executive Summary

Doctor-service is the systems debugging case study. It started as an apparent failure, exposed invalid measurement and packaging defects, drove product hardening in JMOA, and ended as a corrected modest memory win.

Final audited result:

```text
median PSS reduction: ~2.7 MB
median Private_Dirty reduction: ~1.8 MB
paired PSS wins: 3/3
runtime mode: corrected Spring Boot fat JAR
CDS: per-candidate
runtime javaagent: absent
```

The important story is not "we got a bigger number." It is:

```text
we found invalid evidence,
root-caused why it was invalid,
fixed product invariants,
then accepted the smaller audited number.
```

## Service Profile

Doctor-service is a Spring Boot/JPA/JWT microservice from a private/internal HMS project. Public documentation should keep this service sanitized and should not expose private source paths, URLs, credentials, or domain data.

Public-safe shape:

- Spring Boot service
- JPA/Hibernate
- PostgreSQL
- OAuth2/JWT resource-server style security
- Spring Boot fat-JAR deployment
- CDS-style runtime measurement

## Initial Discovery And Candidate Shaping

JMOA discovery found a large lambda and adapter surface. The selected candidate was:

```text
D2_WARMED_ADAPTER_REUSE
MODE_C
PACKAGE_SAM
```

Build-time shape:

- 618 rewritten classes
- 134 logical adapters
- optimized dependency JARs generated
- no failed classes in the optimized build

## Initial Measurement Failure

The initial Phase 32I measurement did not confirm a memory win. That result was not accepted as a final JMOA result because later investigation showed the measured fat JAR was not actually using the optimized dependencies.

Invalid evidence must remain documented, but not cited as a final claim.

## Phase 32J Root Cause: Optimized JARs Not In `BOOT-INF/lib`

Root cause:

```text
JMOA generated optimized dependency JARs,
but the Spring Boot fat JAR still contained original dependency JARs in BOOT-INF/lib.
```

That meant the runtime was mostly loading original dependencies even though optimized files existed elsewhere.

This is a product-level lesson:

```text
optimized files on disk are not enough.
The runtime classloader must actually see them.
```

## PACKAGE_SAM Multi-Root Adapter Placement Bug

The correction pass found a second product issue. PACKAGE_SAM adapter buckets can span multiple class roots. The original placement logic emitted adapters to a first matching root, leaving rewritten classes in other roots with dangling adapter references.

Fix:

```text
emit adapters to all required output roots
```

## Post-Weave Self-Heal

A third issue appeared around generated Spring/AOT classes. Some classes were rewritten after initial adapter placement, creating new references to adapters that had not been emitted into that root.

Fix:

```text
post-weave self-heal scans rewritten output and fans out missing referenced adapters
```

## AdapterReferenceValidator

JMOA added a build-time validator that scans rewritten output class constant pools for `JmoaPkgAdapters` references and verifies the referenced adapter class exists in the corresponding runtime root.

This turns a future runtime `ClassNotFoundException` into a build failure.

Final plugin hardening facts:

- 118/118 tests passed
- missing adapter references: 0
- duplicate adapter entries: 0
- logical adapters: 134
- physical adapters after fan-out/self-heal: 175

## Java Fat-JAR Substitution Fix

The fat-JAR substitution step also had to preserve Spring Boot nested-JAR semantics. A prior Zip implementation corrupted nested-JAR metadata.

The corrected approach used Java `java.util.zip` and preserved Spring Boot-compatible nested entries.

Product invariant:

```text
Spring Boot fat-JAR materialization must replace BOOT-INF/lib originals with optimized JARs without corrupting nested-JAR headers.
```

## Patient Regression Gate

Because plugin hardening changed adapter emission and validation behavior, the known patient-service candidate was used as a regression gate.

Result:

- optimization decision counts stable
- eligible sites stable
- planned sites stable
- rewritten classes stable
- logical adapters stable
- runtime smoke passed
- CDS mapped
- no class-loading errors

The patient historical memory claim remained unchanged; this was a correctness regression gate, not a new patient memory measurement.

## Corrected CDS And Runtime Validation

After fat-JAR substitution and adapter placement fixes:

- corrected baseline and D2-fixed artifacts were built
- per-candidate CDS archives were retrained
- runtime health passed
- workload passed
- no runtime javaagent was present
- no CNF/NCDF classloading errors occurred

## Corrected Final Measurement

The initial script reported a mistaken -5.9 MB median because it selected the wrong array element. Phase 32L audited the data and corrected the median.

Correct final Doctor claim:

| Metric | Result |
| --- | ---: |
| Median PSS reduction | ~2.7 MB |
| Median Private_Dirty reduction | ~1.8 MB |
| Paired-delta median | ~2.0 MB |
| Paired PSS wins | 3/3 |
| Workload errors | 0 |
| Runtime javaagent | absent |

The corrected number is smaller than the mistaken one, but it is the number that should be published.

## Lessons For JVM Productization

Doctor-service hardened JMOA in ways that matter beyond one benchmark:

1. Fat-JAR packaging must be explicitly materialized.
2. Build success does not prove runtime classpath correctness.
3. PACKAGE_SAM adapter placement must handle multiple roots.
4. Runtime errors should be caught by build-time validation.
5. Statistical audits matter as much as bytecode audits.
6. Smaller honest claims are stronger than inflated invalid claims.

## Final Claim

Doctor-service D2-fixed is a confirmed modest memory win under corrected Spring Boot fat-JAR/CDS deployment:

```text
~2.7 MB median PSS reduction
~1.8 MB median Private_Dirty reduction
3/3 paired wins
after fat-JAR substitution and PACKAGE_SAM adapter placement fixes
```

Do not cite Phase 32I or the mistaken -5.9 MB median as final.
