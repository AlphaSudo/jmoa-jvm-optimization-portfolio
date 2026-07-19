# JMOA V2 Final Three-Service Matrix

This is the V1-to-final-V2 engineering-evolution matrix. For the direct clean
no-JMOA comparison, use the [direct product matrix](direct-product-matrix.md).

Comparison: accepted V1 artifact to final V2 artifact under a frozen runtime
policy per service.

| Service | Deployment | Confirmed policy | Valid runs | Wins | Median PSS | Median Private_Dirty | Median memory.current |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| PetClinic customers | Exploded Boot / `JarLauncher` | `NO_CDS_LOW_DIRTY` | 6/6 | 2/3 | -6,012 KB | -5,708 KB | -8,081,408 B |
| Doctor | Corrected Spring Boot fat JAR | `APPLICATION_CDS` | 6/6 | 3/3 | -5,156 KB | -5,212 KB | -6,975,488 B |
| Patient | Corrected Spring Boot fat JAR | `JDK_BASE_CDS_LOW_DIRTY` | 6/6 | 3/3 | -8,279 KB | -8,444 KB | -8,523,776 B |

Every row has zero workload errors, V2-C `CONFIRMED_WIN`, and V2-D
attribution. Patient no-CDS is independently confirmed at -8,903 KB median
PSS. Dynamic Patient application CDS remains blocked for the tested
single-replica deployment.

These results are protocol-specific. They do not establish one universally
optimal CDS mode, packaging shape, or allocator policy.
