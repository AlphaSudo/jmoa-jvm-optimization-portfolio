# PetClinic Phase 33M Final Verdict

## Verdict

```text
CONFIRMED PUBLIC NO-CDS MEMORY WIN
```

## Claim

JMOA full P2 reduced Spring PetClinic `customers-service` memory under the project's real exploded Spring Boot / `JarLauncher` deployment shape, with no CDS/AppCDS/Leyden and no runtime javaagent.

## Final Numbers

```text
Median PSS:            -4.6 MB
Median Private_Dirty:  -4.8 MB
Median memory.current: -4.6 MB
Median heap PSS:       -7.0 MB
Loaded classes:        -154
Paired wins:           3/3
Workload errors:       0
```

## Required Caveat

The result depends on deployment shape. Fat-JAR full P2 regressed memory in the accepted evidence. The confirmed win applies to exploded Boot / `JarLauncher`.
