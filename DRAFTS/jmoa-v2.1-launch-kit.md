# JMOA 2.1 Launch Kit

## One-line description

JMOA is an evidence-gated build-time JVM optimizer that connects bytecode
transformation, Spring Boot packaging, runtime-origin proof, and Linux memory
measurement.

## Single X post

I built JMOA 2.1 to answer a harder question than “can I shrink a JAR?”: can I
prove the deployed JVM service actually uses less RAM?

On Spring PetClinic, exact R41F reduced process PSS by 14.88 MiB and cgroup RAM
by 16.24 MiB vs the documented strict no-JMOA exploded deployment—12/12
held-out blocks, p=0.000488.

The honest boundary: this is packaging-inclusive, and CPU increased 14.71%.
Paper, source, negative results, and evidence:
https://github.com/AlphaSudo/jmoa/releases/tag/v2.1.0

## Five-post technical thread

1. JVM optimization is not complete when bytecode changes. The final Spring
   Boot artifact can load different classes, packaging can dominate residency,
   and one clean RSS snapshot can disappear under cold-start variance. I built
   JMOA to own that full path.

2. JMOA profiles real execution, admits bounded lambda/adapter rewrites,
   performs audited LVT/LVTT reduction, materializes fat/exploded Boot
   deployments, proves runtime origins, and then runs paired PSS+cgroup
   confirmation. Unsafe or non-economic candidates are rejected.

3. JMOA 2.1's PetClinic result: -15,241.5 KiB process PSS and -17,033,216 B
   `memory.current`, with 12/12 favorable held-out blocks and exact
   p=0.00048828125. The campaign completed 81/81 sessions with no reused
   observations.

4. The result is not benchmark theater. Median lifecycle CPU increased 14.71%,
   and the four-arm factorial showed packaging was the dominant main effect.
   So the claim is explicitly packaging-inclusive—not “metadata removal saved
   15 MiB.”

5. This project spans ASM bytecode work, Maven plugins, Spring Boot packaging,
   cgroup/smaps/NMT attribution, experimental design, failure-preserving
   automation, and release engineering. Source + technical paper:
   https://github.com/AlphaSudo/jmoa/releases/tag/v2.1.0

## LinkedIn / recruiter summary

I released JMOA 2.1, an evidence-gated JVM footprint optimization system for
Spring Boot. The project goes beyond bytecode transformation: it profiles
runtime behavior, applies conservative build-time rewrites, audits classfile
changes, materializes the real deployment, proves runtime origins, and validates
memory using paired Linux PSS and cgroup evidence.

The published PetClinic campaign completed 81/81 sessions. The accepted JMOA
deployment reduced median process PSS by 14.88 MiB and target-cgroup RAM by
16.24 MiB across 12/12 favorable held-out blocks. The report also discloses a
14.71% lifecycle-CPU tradeoff and shows through a four-arm factorial that
packaging was the dominant measured contributor.

The work demonstrates JVM bytecode engineering, Maven plugin development,
Spring Boot packaging, Linux memory attribution, statistical experiment design,
failure analysis, and public release engineering.

## Claim language to preserve

Say:

> Exact R41F reduced PetClinic process PSS by 14.88 MiB and target-cgroup RAM
> by 16.24 MiB versus the documented strict no-JMOA B0 exploded deployment.
> The result is packaging-inclusive and service-specific.

Do not say:

- “JMOA always saves 15 MiB.”
- “Metadata removal saved 15 MiB.”
- “Fat JARs always use less memory.”
- “There is no performance cost.”
