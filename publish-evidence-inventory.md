# V2 Publish Evidence Inventory

Updated: 2026-07-18

This inventory separates the current V2 release claims from historical V1
evidence and private raw captures.

## Current Public-Safe Claims

| Case | Confirmed V2 claim | Evidence status |
| --- | --- | --- |
| PetClinic customers | Exploded Boot, `NO_CDS_LOW_DIRTY`, median PSS -6,012 KB, 2/3 wins | public, 6/6 valid, V2-C/V2-D |
| Doctor | Corrected fat JAR, `APPLICATION_CDS`, median PSS -5,156 KB, 3/3 wins | private/sanitized, 6/6 valid, V2-C/V2-D |
| Patient | Corrected fat JAR, `JDK_BASE_CDS_LOW_DIRTY`, median PSS -8,279 KB, 3/3 wins | private/sanitized, 6/6 valid, V2-C/V2-D |

Patient `NO_CDS_LOW_DIRTY` is independently confirmed at -8,903 KB median
PSS. Dynamic Patient application CDS remains blocked.

## Historical Evidence

Phase 31-33 summaries document the original V1 validation and hardening work:

- Patient Phase 31D-P2: approximately 4.2-4.4 MB.
- Doctor corrected Phase 32K/32L audit: approximately 2.7 MB PSS.
- PetClinic Phase 33M full-P2 result: approximately 4.6 MB PSS.

These are retained for provenance and must not replace the current V2 matrix.

## Do Not Cite As Current V2

- Doctor Phase 32I or the mistaken -5.9 MB median.
- Patient Phase 31 medians as the final V2 result.
- PetClinic Phase 33M as the final incremental V1-to-V2 result.
- PetClinic fat-JAR full P2 as a win.
- Single-screen, invalid, mixed, or diagnostic-only results.
- `MALLOC_ARENA_MAX=1` as a complete solution by itself.

## Publication Boundary

Public-safe:

- source and architecture links;
- final sanitized matrix and case studies;
- historical sanitized summaries;
- rendered diagrams, chart, one-page PDF, and hiring drafts.

Excluded:

- Doctor and Patient source, configuration, database assets, or raw captures;
- JARs, CDS archives, images, dumps, logs, credentials, and machine paths;
- any sanitized Markdown summary used as a substitute for raw evidence replay.

PetClinic remains the public reproduction bridge. Doctor and Patient remain
sanitized private-service studies.
