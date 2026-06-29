# PetClinic Phase 33N Evidence Index

## Evidence Chain

```text
33K freeze
  -> full P2 artifact exists and hashes match
33L.7 materializer
  -> optimized dependency layer exists in exploded Boot shape
33L.8 dynamic origin proof
  -> optimized classes load from /application/BOOT-INF/lib
33L.9 launch comparison
  -> exploded Boot is positive, fat JAR is negative
33M confirmation
  -> full P2 exploded Boot passes 3-pair no-CDS win gate
33N freeze
  -> claim, caveats, and evidence boundaries are locked
```

## Public-Safe Evidence Summary

| Evidence | Status | Public-safe takeaway |
| --- | --- | --- |
| Artifact freeze | pass | Baseline and full P2 artifacts were fixed for confirmation |
| Exploded Boot materialization | pass | Optimized dependencies were placed into the real extracted dependency layer |
| Dynamic origin proof | pass | 8/8 sampled optimized/runtime classes loaded from expected origins |
| Launch-mode comparison | measured | fat-JAR failed, exploded Boot won |
| Phase 33M confirmation | pass | 3/3 paired wins, median PSS -4.6 MB |

## Dynamic Origin Samples

Accepted runtime-origin samples included:

- `jmoa.runtime.JmoaRuntimeSupport`
- `org.springframework.boot.SpringApplication`
- `org.springframework.boot.DefaultApplicationContextFactory`
- `org.springframework.data.core.ClassTypeInformation`
- `org.springframework.beans.factory.BeanFactoryUtils`
- `org.springframework.web.accept.ContentNegotiationManager`
- `org.springframework.web.servlet.config.annotation.WebMvcConfigurationSupport`
- `org.springframework.boot.actuate.autoconfigure.endpoint.condition.OnAvailableEndpointCondition`

## Claim Boundary

Supported:

```text
PetClinic customers-service full P2 wins under exploded Boot / JarLauncher with NO_CDS_LOW_DIRTY.
```

Not supported:

```text
PetClinic full P2 wins under fat-JAR mode.
JMOA no-CDS wins are launch-mode independent.
MALLOC_ARENA_MAX=1 alone is sufficient.
```
