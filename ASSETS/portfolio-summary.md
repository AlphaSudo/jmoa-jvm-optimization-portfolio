# JMOA Portfolio One-Page Summary

## JMOA: Build-Time JVM Memory Optimization For Spring Boot

JMOA is a build-time Java bytecode optimization project for Spring Boot services. It targets selected lambda and adapter patterns before runtime, then verifies that the optimized artifact is actually loaded under the intended deployment mode.

## Problem

Spring Boot container memory is affected by more than Java heap size. Lambda bytecode, adapter classes, class metadata, Spring Boot packaging, classloader visibility, CDS/no-CDS mode, allocator behavior, and runtime launch shape can all affect PSS and Private_Dirty.

## Approach

```text
profile workload
-> select candidate sites
-> rewrite bytecode at build time
-> consolidate PACKAGE_SAM adapters
-> materialize runtime artifact
-> verify runtime origins
-> measure PSS / Private_Dirty / memory.current
```

## Confirmed Results

| Service | Mode | Result |
| --- | --- | ---: |
| Patient-service | expanded classpath + CDS | ~4.2-4.4 MB median memory reduction |
| Doctor-service | corrected fat JAR + CDS | ~2.7 MB median PSS reduction |
| Spring PetClinic `customers-service` | exploded Boot + no-CDS | ~4.6 MB median PSS reduction |

## Public Centerpiece

Spring PetClinic `customers-service`:

- public open-source service
- no CDS/AppCDS/Leyden
- no runtime javaagent
- real exploded Boot / `JarLauncher` deployment
- `MALLOC_ARENA_MAX=1`
- runtime origins verified
- 3/3 paired wins

## Key Technical Lesson

JMOA is not only a bytecode optimizer. It is a JVM deployment optimizer.

The confirmed PetClinic win required:

```text
candidate selection
+ bytecode correctness
+ adapter placement
+ artifact materialization
+ actual deployment-shape alignment
+ runtime policy
+ runtime-origin verification
+ paired measurement
```

## Skills Demonstrated

- JVM memory analysis
- Java bytecode rewriting
- Spring Boot packaging internals
- CDS/no-CDS validation
- PSS, Private_Dirty, cgroup, NMT, smaps analysis
- runtime class-origin verification
- rigorous claim reconciliation
