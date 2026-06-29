# Publish Evidence Inventory

Generated: 2026-06-28

This inventory separates public-safe claims from local/private/raw evidence. It is designed for the Week 1 portfolio publishing pass.

## Final Accepted Claims

| Case | Final public-safe claim | Evidence status |
| --- | --- | --- |
| Patient-service | Internal Spring Boot service, expanded classpath with per-candidate CDS, official Phase 31D-P2 median memory reduction ~4.2-4.4 MB, 9/9 individual wins | confirmed, private/sanitized |
| Doctor-service | Internal Spring Boot/JPA/JWT service, corrected Spring Boot fat JAR with CDS, audited median PSS reduction ~2.7 MB, median Private_Dirty reduction ~1.8 MB, 3/3 paired wins | confirmed, private/sanitized |
| Spring PetClinic `customers-service` | Public OSS Spring Boot service, no CDS/AppCDS/Leyden, no runtime javaagent, real exploded Boot / `JarLauncher` deployment, `MALLOC_ARENA_MAX=1`, median PSS reduction ~4.6 MB, 3/3 paired wins | confirmed, public centerpiece |

## Do Cite

- Patient Phase 31D-P2 official median: ~4.2-4.4 MB container memory reduction.
- Patient Phase 31E: independent evidence at ~2.7-2.9 MB, separate from the official claim.
- Doctor Phase 32K/32L corrected audit: ~2.7 MB median PSS reduction, ~1.8 MB median Private_Dirty reduction.
- PetClinic Phase 33M: ~4.6 MB median PSS reduction, ~4.8 MB median Private_Dirty reduction, ~4.6 MB median `memory.current` reduction.
- PetClinic 33L/33M deployment correction: exploded Boot was the real source deployment shape and fat-JAR was the negative/artificial measurement shape.

## Do Not Cite As Final

- Doctor Phase 32I as a final result.
- Doctor mistaken -5.9 MB median.
- PetClinic fat-JAR full P2 as a win.
- PetClinic early single-screen ablation wins as final.
- PetClinic `p2-no-spring-core` as a promoted candidate.
- `MALLOC_ARENA_MAX=1` as a complete solution by itself.

## Local Raw Evidence Categories

The following local source evidence exists and is useful, but should not be copied directly into a public repository without review:

| Category | Sanitized location | Publication guidance |
| --- | --- | --- |
| Phase 31 patient outputs | `<workspace>/v3.3/phase31-warmed-production-reprofile/out/` | Summarize only; private service |
| Phase 32 doctor outputs | `<workspace>/v3.3/phase32-doctor-service/out/` | Summarize only; private service |
| Phase 33 PetClinic outputs | `<workspace>/v3.3/phase33-petclinic/out/` | Publish summaries; raw logs optional only after path review |
| JARs and CDS archives | `<workspace>/v3.3/**/out/**/*.jar`, `<workspace>/v3.3/**/out/**/*.jsa` | Do not publish by default |
| smaps/NMT/class histogram dumps | `<workspace>/v3.3/**/out/**/*smaps*`, `<workspace>/v3.3/**/out/**/*nmt*`, `<workspace>/v3.3/**/out/**/*class-histogram*` | Do not publish without sanitization |
| container and workload logs | `<workspace>/v3.3/**/out/**/*.log` | Do not publish by default |

## Files Suitable For Public Repo

| File | Status |
| --- | --- |
| `README.md` | public-safe |
| `CASE-STUDIES/01-petclinic-public-nocds-case-study.md` | public-safe |
| `CASE-STUDIES/02-doctor-service-fatjar-cds-hardening-case-study.md` | sanitized private case |
| `CASE-STUDIES/03-patient-service-confirmation-addendum.md` | sanitized private case |
| `CASE-STUDIES/04-jmoa-plugin-runtime-hardening-technical-note.md` | public-safe technical note |
| `EVIDENCE/petclinic/*.md` | public-safe summaries |
| `EVIDENCE/doctor/*.md` | sanitized summaries |
| `EVIDENCE/patient/*.md` | sanitized summaries |
| `ASSETS/*.md` and `ASSETS/**/*.mmd` | public-safe |
| `DRAFTS/*.md` | public-safe drafts after personal review |

## Files Needing Manual Human Review

- Any file copied from raw `out/` phase directories.
- Any file containing local paths, hostnames, database details, JWT/security configuration, or private service internals.
- Any generated PDF before upload.
- Any chart labels or screenshots that mention private project names.

## Public-Safe Tables

### Portfolio Results

| Service | Source | Runtime mode | CDS? | Result | Status |
| --- | --- | --- | --- | --- | --- |
| Patient-service | private/internal | expanded classpath | yes | ~4.2-4.4 MB median | confirmed |
| Doctor-service | private/internal | corrected fat JAR | yes | ~2.7 MB median PSS | confirmed |
| Spring PetClinic `customers-service` | public OSS | exploded Boot / `JarLauncher` | no | ~4.6 MB median PSS | confirmed |

### PetClinic Final No-CDS Result

| Metric | Median delta |
| --- | ---: |
| PSS | -4.6 MB |
| Private_Dirty | -4.8 MB |
| `memory.current` | -4.6 MB |
| heap PSS | -7.0 MB |
| loaded classes | -154 |
| paired wins | 3/3 |

## Publishing Risk Notes

- Patient and Doctor are valuable portfolio cases, but they are private/internal. Keep them sanitized and avoid source-level details.
- PetClinic is the public trust anchor. Keep its claim precise: no-CDS, exploded Boot, `MALLOC_ARENA_MAX=1`, dynamic origins verified.
- The strongest technical narrative is not "JMOA always wins." It is "JMOA wins when bytecode, packaging, runtime policy, and verification are aligned."
