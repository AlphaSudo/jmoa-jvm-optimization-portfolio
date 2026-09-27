# JMOA 2.1 PetClinic Direct RAM Evidence

Terminal decision: `T7R23_R487_SCALE_DIRECT_RAM_WIN`

Exact R41F JMOA fat-JAR versus documented strict no-JMOA B0 exploded Boot:

| Metric | Median delta | Favorable blocks | 95% bootstrap interval |
| --- | ---: | ---: | ---: |
| Process PSS | -15,241.5 KiB | 12/12 | [-16,109.5, -15,052.5] KiB |
| `memory.current` | -17,033,216 B | 12/12 | [-17,842,176, -16,713,728] B |
| Private Dirty | -15,252 KiB | 12/12 | [-16,062, -14,880] KiB |
| Cgroup anonymous | -15,616,000 B | 12/12 | [-16,445,440, -15,243,264] B |
| Cgroup file | -411,648 B | 12/12 | [-450,560, -362,496] B |

Exact paired sign-test `p=0.00048828125`. The campaign completed 81/81
sessions with zero predecessor observations reused. Median lifecycle CPU was
+14.7073%; median startup was +1,652 ms. All frozen product gates passed.

Claim boundary: packaging-inclusive and service-specific. Packaging main
effect was -12,715.25 KiB PSS; content main effect was -2,465 KiB; interaction
was +3,801.5 KiB.

Authoritative source result:

- https://github.com/AlphaSudo/jmoa/blob/main/docs/product-evidence/petclinic-r41f-b0-t7r23-result.md
- https://github.com/AlphaSudo/jmoa/blob/main/docs/product-evidence/petclinic-r41f-b0-t7r23-result.json
- https://github.com/AlphaSudo/jmoa/blob/main/docs/paper/jmoa-v2.1-petclinic-memory-engineering.md
