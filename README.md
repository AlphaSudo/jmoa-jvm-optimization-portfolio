<p align="center">
  <img src="ASSETS/jmoa-portfolio-hero.png" alt="JMOA build-time JVM memory optimization portfolio overview" width="100%">
</p>

# JMOA JVM Optimization Portfolio

JMOA is an evidence-driven, build-time JVM footprint optimization system for Spring Boot. It combines admitted lambda/adapter rewriting, raw dependency metadata reduction, byte-preservation auditing, deployment materialization, runtime-origin proof, paired evidence validation, and memory attribution.

This portfolio summarizes three confirmed case studies across different service shapes and deployment modes, with Spring PetClinic as the public no-CDS centerpiece.

## Source Code

The public JMOA source release lives in a separate repository:

- [AlphaSudo/jmoa](https://github.com/AlphaSudo/jmoa) contains the Maven plugin, runtime library, materialization and origin-proof tooling, evidence/attribution engines, and the clean-clone-qualified PetClinic build and semantic-smoke workflow.

This repository remains the evidence and case-study portfolio. The source repo is intentionally separate so private HMS evidence can stay sanitized while the public tooling has its own clean build surface.

## V2 Case Studies

| Public reproducibility | Private fat-JAR/CDS | Runtime-policy selection |
| --- | --- | --- |
| **PetClinic customers**<br>Exploded Boot, `NO_CDS_LOW_DIRTY`<br>V1 to V2: **-6,012 KB median PSS**, 2/3 wins<br>[Case study](CASE-STUDIES/01-petclinic-public-nocds-case-study.md) | **Doctor service**<br>Corrected fat JAR, application CDS<br>D2 to D2R: **-5,156 KB median PSS**, 3/3 wins<br>[Case study](CASE-STUDIES/02-doctor-service-fatjar-cds-hardening-case-study.md) | **Patient service**<br>Corrected fat JAR, stock JDK base CDS<br>V1 to V2: **-8,279 KB median PSS**, 3/3 wins<br>[Case study](CASE-STUDIES/03-patient-service-confirmation-addendum.md) |

All three final comparisons have 6/6 valid runs, zero workload errors, V2-C `CONFIRMED_WIN`, and V2-D attribution. Patient no-CDS is also independently confirmed at -8,903 KB median PSS. Dynamic Patient application CDS remains rejected for the tested single-replica deployment.

These are protocol-specific results. They do not establish universal benefit from CDS, no-CDS, a packaging shape, or one allocator policy.

## What JMOA Does

JMOA analyzes Java bytecode and workload profiles, identifies lambda and adapter patterns with favorable memory ROI, rewrites selected sites at build time, and materializes optimized artifacts for the target runtime shape.

The work here focuses on:

- MODE_C bytecode optimization
- PACKAGE_SAM adapter consolidation
- Spring Boot fat-JAR and exploded-Boot materialization
- Runtime-origin verification
- CDS and no-CDS measurement protocols
- Container memory measurement with PSS, Private_Dirty, cgroup `memory.current`, NMT, class histograms, and smaps

<p align="center">
  <img src="ASSETS/diagrams/jmoa-pipeline.png" alt="JMOA product pipeline from workload profiling through runtime-origin verification and PSS measurement" width="100%">
</p>

## Why Build-Time Instead Of Runtime Javaagent

Runtime javaagents are useful for diagnostics, but they complicate production memory claims. This portfolio uses build-time transformation so the measured process runs without a JMOA runtime javaagent.

That matters because the memory claim should belong to the optimized artifact and deployment shape, not to a live instrumentation layer.

## Detailed Records

- [Spring PetClinic public no-CDS case study](CASE-STUDIES/01-petclinic-public-nocds-case-study.md)
- [Doctor-service fat-JAR/CDS hardening case study](CASE-STUDIES/02-doctor-service-fatjar-cds-hardening-case-study.md)
- [Patient-service confirmation addendum](CASE-STUDIES/03-patient-service-confirmation-addendum.md)
- [JMOA plugin and runtime hardening technical note](CASE-STUDIES/04-jmoa-plugin-runtime-hardening-technical-note.md)

## Key Engineering Lessons

1. Candidate selection is necessary but not sufficient.
2. Build success is not runtime success.
3. Spring Boot packaging mode can decide whether an optimization wins or loses.
4. Runtime-origin proof is a product requirement, not a nice-to-have.
5. PSS and Private_Dirty are more useful than RSS for JVM container memory claims.
6. CDS and no-CDS are different product modes with different economics.
7. Invalid measurements are valuable when they expose product invariants.

<p align="center">
  <img src="ASSETS/diagrams/runtime-modes.svg" alt="Runtime shapes used by the JMOA portfolio: expanded classpath, corrected fat JAR, and exploded Boot app" width="100%">
</p>

## Measurement Methodology

Primary memory metrics:

- smaps PSS
- smaps Private_Dirty
- cgroup `memory.current`

Supporting diagnostics:

- Native Memory Tracking
- `GC.class_histogram`
- `VM.metaspace`
- loaded class counts
- smaps region breakdown
- startup timing
- workload error counts
- dynamic class-load origin logs

The case studies distinguish measured facts from hypotheses. Invalid intermediate phases are documented as lessons but not cited as final wins.

## Diagram Policy

The README publishes rendered images because they are easier to scan on GitHub and in recruiter/reviewer contexts. Mermaid sources are kept beside the rendered assets under [ASSETS](ASSETS/) so the diagrams remain editable and auditable.

## Claim Integrity Rules

- Do not cite invalid Doctor Phase 32I or old portfolio medians as V2 results.
- Use Doctor D2-to-D2R `-5,156 KB`, not the superseded V1-era `~2.7 MB` figure.
- Use Patient stock-base-CDS `-8,279 KB` for the primary final matrix; keep its independent no-CDS result separate.
- Do not describe Patient stock base CDS as Patient application CDS.
- Do not transfer PetClinic's exploded-Boot result to fat-JAR mode.
- Do not claim `MALLOC_ARENA_MAX=1` alone solved PetClinic no-CDS memory.
- Do not claim JMOA always wins.

## Skills Demonstrated

- JVM memory analysis
- Java bytecode transformation
- Spring Boot packaging internals
- AppCDS/CDS and no-CDS runtime measurement
- Container memory profiling
- `smaps`, PSS, Private_Dirty, cgroup, and NMT interpretation
- Runtime class-origin verification
- Experimental design and claim reconciliation
- Debugging invalid measurements into product hardening

## Evidence

Publish-safe summaries are under [EVIDENCE](EVIDENCE/). Raw local experiment outputs are intentionally not copied into this portfolio because they may contain local paths, bulky artifacts, or private environment details.
