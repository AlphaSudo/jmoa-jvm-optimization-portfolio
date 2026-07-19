# JMOA V2 Direct Product Matrix

Comparison: clean no-JMOA `B0` to final JMOA V2 under a frozen policy per
service.

| Service | Deployment and policy | Evidence | PSS | Private_Dirty | memory.current | Product gate |
| --- | --- | --- | ---: | ---: | ---: | --- |
| Doctor | Fat JAR, artifact-specific application CDS | 6/6 valid, 3/3 wins | **-5,809 KB** | **-5,492 KB** | **-11,845,632 B** | Pass |
| PetClinic customers | Exploded Boot, `NO_CDS_LOW_DIRTY` | Valid screen | +5,446 KB | +5,580 KB | +3,059,712 B | Stop |
| Patient | Fat JAR, stock JDK base CDS | Two bounded screens | +3,290 KB | +3,336 KB | +3,244,032 B | Stop |

Overall verdict: `ONE_SERVICE_PRODUCT_WIN`.

Doctor is the only service that cleared the substantial direct product gate.
PetClinic and Patient stopped at the screen and do not receive confirmation or
runtime-win language.

The separate [V1-to-V2 matrix](three-service-matrix.md) remains valid
engineering-evolution evidence. Its medians are not added to historical
baseline-to-V1 measurements.
