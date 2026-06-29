# PetClinic Phase 33M Summary

## Status

```text
verdict: confirmed-public-nocds-win
service: Spring PetClinic customers-service
candidate: full P2
launch mode: EXPLODED_BOOT_APP
runtime policy: NO_CDS_LOW_DIRTY
paired wins: 3/3
```

## Runtime Contract

- No CDS
- No AppCDS
- No Leyden
- No runtime javaagent
- `MALLOC_ARENA_MAX=1`
- Spring Boot exploded app
- `JarLauncher`
- optimized dependency layer
- dynamic runtime-origin proof passed

## Final Median Result

| Metric | Baseline median | Full P2 median | Delta |
| --- | ---: | ---: | ---: |
| PSS | 351779 KB | 344178 KB | -4.6 MB |
| Private_Dirty | 342604 KB | 334968 KB | -4.8 MB |
| `memory.current` | 356163584 bytes | 351313920 bytes | -4.6 MB |
| heap PSS | 105084 KB | 95828 KB | -7.0 MB |
| loaded classes | 24404 | 24250 | -154 |
| startup | 16.866 s | 16.900 s | +0.034 s |

## Pair Results

| Pair | PSS | Private_Dirty | `memory.current` | Result |
| --- | ---: | ---: | ---: | --- |
| 1 | -10.1 MB | -10.5 MB | -23.4 MB | pass |
| 2 | -1.0 MB | -1.1 MB | -1.3 MB | pass |
| 3 | -4.6 MB | -4.8 MB | -4.6 MB | pass |

## Interpretation

Phase 33M confirms a public open-source no-CDS JMOA win only under the real exploded Boot deployment shape. This summary should be cited together with the launch-mode caveat: fat-JAR full P2 was negative.
