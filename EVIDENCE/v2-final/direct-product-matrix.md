# JMOA V2 Direct Product Matrix

Status: `DIRECT_PRODUCT_MATRIX_UNDER_RECONCILIATION`.

Comparison: clean no-JMOA `B0` to final JMOA V2 under a frozen policy per
service.

| Service | Deployment and policy | Evidence | PSS | Private_Dirty | memory.current | Product gate |
| --- | --- | --- | ---: | ---: | ---: | --- |
| Doctor | Fat JAR, artifact-specific application CDS | 6/6 valid, 3/3 wins | **-5,809 KB** | **-5,492 KB** | **-11,845,632 B** | Pass |
| PetClinic customers | Exploded Boot, `NO_CDS_LOW_DIRTY` | Valid screen; historical replay drift | +5,446 KB | +5,580 KB | +3,059,712 B | Stop |
| Patient | Fat JAR, stock JDK base CDS | Two screens on non-accepted V2 SHA | +3,290 KB | +3,336 KB | +3,244,032 B | Stop |

Previous provisional verdict: `ONE_SERVICE_PRODUCT_WIN`.

Doctor retains its confirmed measured result. PetClinic's frozen Phase 33M
replay reversed from the accepted 3/3 win to 0/3 under the current runtime.
Patient's screens used `FB4E...`, while the accepted corrected V2 is `4CFC...`.
The aggregate adoption verdict remains under reconciliation; a new three-arm
campaign was blocked by replay and same-artifact variance gates.

The separate [V1-to-V2 matrix](three-service-matrix.md) remains valid
engineering-evolution evidence. Its medians are not added to historical
baseline-to-V1 measurements.
