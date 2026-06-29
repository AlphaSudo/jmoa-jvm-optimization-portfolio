# Spring PetClinic Public No-CDS Case Study

## Executive Summary

JMOA full P2 produced a confirmed non-CDS memory win on the public Spring PetClinic microservices `customers-service` when the optimized artifact was materialized into the project's real exploded Spring Boot / `JarLauncher` deployment shape and run with the `NO_CDS_LOW_DIRTY` runtime policy.

Final Phase 33M result:

| Metric | Median delta |
| --- | ---: |
| PSS | -4.6 MB |
| Private_Dirty | -4.8 MB |
| cgroup `memory.current` | -4.6 MB |
| heap PSS | -7.0 MB |
| loaded classes | -154 |
| paired wins | 3/3 |
| workload errors | 0 |

Runtime constraints:

- No CDS
- No AppCDS
- No Leyden
- No runtime javaagent
- `MALLOC_ARENA_MAX=1`
- Exploded Boot / `JarLauncher`
- Dynamic runtime origins verified

## Why PetClinic `customers-service`

The PetClinic service is the public case because it avoids the trust problem of private/internal services. It is a recognizable Spring Boot microservice with real framework dependencies and a deployment shape that can be discussed publicly.

The objective was narrow:

```text
Can JMOA produce a confirmed memory win on a public Spring Boot service without CDS, AppCDS, Leyden, or a runtime javaagent?
```

Phase 33M answered yes, but only after correcting the deployment shape.

## Non-CDS Requirement

The target result had to avoid:

- CDS
- AppCDS
- Leyden
- runtime javaagent

That constraint mattered because earlier JMOA wins used CDS-style runtimes. PetClinic validates a different product mode: no-CDS artifact optimization plus explicit runtime policy.

## Initial Wrong Path: Fat-JAR Measurement Failed

Early PetClinic no-CDS measurements used a Spring Boot fat-JAR launch shape. Under that shape, full P2 reduced loaded classes but regressed memory.

The allocator-controlled fat-JAR confirmation failed:

```text
paired wins: 0/3
median PSS: +8.7 MB
Private_Dirty: +8.9 MB
memory.current: +9.0 MB
heap PSS: +8.5 MB
loaded classes: -153
```

That result was clean, but it did not match the source project deployment shape.

## Root Cause: Source Deployment Is Exploded Boot

Phase 33L found that the source PetClinic Dockerfile uses Spring Boot layertools extraction:

```text
java -Djarmode=layertools -jar application.jar extract
java org.springframework.boot.loader.launch.JarLauncher
```

So the real deployment shape is:

```text
EXPLODED_BOOT_APP
```

not:

```text
SPRING_BOOT_FAT_JAR
```

Launch-mode comparison showed this was decisive:

| Launch mode | Full P2 result |
| --- | --- |
| Fat JAR no-CDS | memory regression |
| Exploded Boot no-CDS | memory win |

Single-screen launch comparison:

| Launch mode | PSS | Private_Dirty | `memory.current` | heap PSS | loaded classes |
| --- | ---: | ---: | ---: | ---: | ---: |
| fat JAR | +7.3 MB | +7.6 MB | +7.8 MB | +6.4 MB | -155 |
| exploded Boot | -3.9 MB | -4.0 MB | -1.0 MB | -6.0 MB | -154 |

## Materialization Into Exploded Boot Layers

Phase 33L.7 materialized the optimized artifact into the extracted Spring Boot structure:

```text
dependencies/
spring-boot-loader/
snapshot-dependencies/
application/
```

The materializer verified:

- all expected layers existed
- optimized dependency JARs were present in the dependency layer
- `jmoa-runtime-lib` was present
- `JmoaPkgAdapters` classes were present
- 25 same-name dependency JARs changed from baseline to optimized
- 1 runtime library was added
- no new static duplicate/shadowing risk was introduced

## Runtime-Origin Proof

Phase 33L.8 captured runtime class-load proof using `-Xlog:class+load`.

The run produced:

```text
class-load records: 22538
sample classes found: 8/8
sample classes accepted: 8/8
dynamic origin proven: true
```

Sample classes verified from `/application/BOOT-INF/lib`:

- `jmoa.runtime.JmoaRuntimeSupport`
- `org.springframework.boot.SpringApplication`
- `org.springframework.boot.DefaultApplicationContextFactory`
- `org.springframework.data.core.ClassTypeInformation`
- `org.springframework.beans.factory.BeanFactoryUtils`
- `org.springframework.web.accept.ContentNegotiationManager`
- `org.springframework.web.servlet.config.annotation.WebMvcConfigurationSupport`
- `org.springframework.boot.actuate.autoconfigure.endpoint.condition.OnAvailableEndpointCondition`

This proves the measurement used optimized runtime origins, not merely optimized files sitting unused on disk.

## Phase 33M 3-Pair Confirmation

Phase 33M then ran paired baseline vs. full P2 confirmation under the selected product contract:

```text
candidate: full P2
launch mode: EXPLODED_BOOT_APP
runtime policy: NO_CDS_LOW_DIRTY
allocator policy: MALLOC_ARENA_MAX=1
CDS/AppCDS/Leyden: disabled
runtime javaagent: absent
```

Pair results:

| Pair | PSS | Private_Dirty | `memory.current` | heap PSS | loaded classes | Pass |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | -10.1 MB | -10.5 MB | -23.4 MB | -12.9 MB | -154 | yes |
| 2 | -1.0 MB | -1.1 MB | -1.3 MB | -0.8 MB | -153 | yes |
| 3 | -4.6 MB | -4.8 MB | -4.6 MB | -7.0 MB | -155 | yes |

The tightest pair still cleared the PSS, Private_Dirty, and `memory.current` gates.

## What Was Actually Saved

The most visible final savings were in container-level memory:

- PSS down ~4.6 MB
- Private_Dirty down ~4.8 MB
- cgroup `memory.current` down ~4.6 MB
- heap PSS down ~7.0 MB
- loaded classes down 154

The result is not explained by live heap bytes shrinking significantly. It is a deployment-aligned runtime memory result: fewer loaded classes and changed runtime/classloader behavior translated into lower dirty and proportional resident pages under the real launch mode.

## Why This Result Is Credible

The case is credible because it includes both positive and negative evidence:

- fat-JAR full P2 failed
- exploded Boot full P2 won
- runtime origins were dynamically verified
- no CDS or runtime javaagent was present
- workload errors were zero
- artifact materialization was checked
- the result passed 3 paired confirmation runs
- disallowed claims are documented

The strongest finding is not just that JMOA won. It is that the win required aligning bytecode, packaging, launch mode, runtime policy, and verification.

## Caveats

This case study does not claim:

- JMOA wins under every PetClinic packaging mode
- full P2 is universally no-CDS-safe
- `MALLOC_ARENA_MAX=1` alone solves no-CDS memory
- fat-JAR full P2 is positive
- all Spring Boot services will see this magnitude of improvement

The confirmed claim applies to:

```text
Spring PetClinic customers-service
+ full P2
+ exploded Boot / JarLauncher
+ NO_CDS_LOW_DIRTY
+ MALLOC_ARENA_MAX=1
+ verified optimized origins
```

## Reproducibility Notes

The public-safe reproduction contract is:

1. Build baseline and full P2 artifacts.
2. Extract with Spring Boot layertools.
3. Place optimized dependencies and `jmoa-runtime-lib` into the extracted dependency layer.
4. Launch with `JarLauncher`.
5. Run with no CDS/AppCDS/Leyden and no runtime javaagent.
6. Set `MALLOC_ARENA_MAX=1`.
7. Verify sampled runtime class origins.
8. Measure PSS, Private_Dirty, `memory.current`, heap PSS, loaded classes, startup, and workload errors.

Raw local evidence is intentionally not copied into this portfolio; the evidence summary files preserve the accepted metrics and claim boundaries.

## Final Claim

JMOA full P2 achieved a confirmed public open-source no-CDS memory win on Spring PetClinic `customers-service` under the project's actual exploded Boot deployment shape, with median PSS -4.6 MB, Private_Dirty -4.8 MB, and cgroup `memory.current` -4.6 MB across 3 paired confirmation runs.
