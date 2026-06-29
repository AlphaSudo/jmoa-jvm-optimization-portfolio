# JMOA Plugin And Runtime Hardening Technical Note

## Executive Summary

The strongest lesson across the JMOA case studies is that build-time bytecode optimization is only one part of the product.

The product boundary is:

```text
candidate selection
+ bytecode rewriting
+ adapter placement
+ artifact materialization
+ runtime policy
+ runtime-origin verification
+ measured confirmation
```

If any link is wrong, fewer classes may not become lower memory.

## Why Build Success Is Not Runtime Success

A JMOA build can produce optimized dependency JARs and still fail as a runtime optimization if:

- optimized JARs are not in the actual runtime classpath
- original JARs shadow optimized JARs
- adapters are emitted to the wrong root
- Spring Boot nested-JAR metadata is corrupted
- the selected deployment mode does not match the service's real launch shape
- runtime policy causes allocator or heap page behavior to hide the savings

Doctor-service and PetClinic both exposed this.

## Fat-JAR Substitution Bug

Doctor-service generated optimized dependency JARs, but the measured Spring Boot fat JAR still contained original dependencies under `BOOT-INF/lib`.

Product rule:

```text
For fat-JAR deployment, JMOA must substitute optimized dependencies into BOOT-INF/lib and verify the result.
```

## Multi-Root PACKAGE_SAM Adapter Placement Bug

PACKAGE_SAM adapter buckets can be referenced from multiple output roots. Emitting the adapter only to a first root can leave rewritten classes in other roots with unresolved adapter references.

Product rule:

```text
Adapter emission must fan out to every root that contains rewritten references.
```

## Post-Weave Adapter Self-Heal

Some Spring-generated classes can be rewritten after initial adapter placement. JMOA added a post-weave self-heal pass to detect referenced-but-missing adapters and emit them into the needed roots.

Product rule:

```text
adapter validation must run after weaving, not only before it.
```

## AdapterReferenceValidator

The validator scans rewritten class constant pools for `JmoaPkgAdapters` references and confirms each referenced adapter class exists in the corresponding runtime root.

This converts runtime classloading failures into build failures.

Final fixed-plugin facts:

- 118/118 tests passed
- missing adapter references: 0
- duplicate adapter entries: 0
- multi-root emission supported
- post-weave self-heal supported

## Runtime-Origin Verification

Static packaging inspection is necessary but not sufficient. Runtime-origin proof answers:

```text
Did the JVM actually load optimized classes from the intended origin?
```

PetClinic used `-Xlog:class+load` to prove sampled Spring Boot/Data/Beans/Web/WebMVC/Actuator classes and JMOA runtime classes loaded from optimized exploded Boot origins.

Product rule:

```text
Every public memory claim needs either dynamic origin proof or an equivalent runtime-origin gate.
```

## Deployment-Mode Classifier

The PetClinic breakthrough came from classifying the real source deployment mode:

```text
source Dockerfile: EXPLODED_BOOT_APP
old measured mode: SPRING_BOOT_FAT_JAR
```

The measured mode was not the source project's real launch shape. Once JMOA was materialized into exploded Boot layers, full P2 confirmed.

Deployment modes JMOA must distinguish:

- Spring Boot fat JAR
- Spring Boot layered/exploded app
- expanded classpath
- custom classpath
- unknown/manual

## Materialization Modes

### Fat JAR

Required invariants:

- optimized JARs replace originals under `BOOT-INF/lib`
- nested-JAR metadata remains Spring Boot compatible
- `jmoa-runtime-lib` is present when required
- no original JAR shadows optimized JARs
- adapter references validate

### Exploded Boot

Required invariants:

- layertools extraction matches source launch shape
- optimized JARs are placed in the dependency layer
- `JarLauncher` sees optimized dependencies
- runtime origins are dynamically verified

### Expanded Classpath

Required invariants:

- optimized classpath is generated
- optimized JARs precede originals
- no duplicate shadowing breaks runtime behavior
- classpath can be audited directly

## Runtime Policy

JMOA needs separate policies for different product modes:

### CDS

- train per-candidate archive
- verify archive maps
- verify no archive degradation
- measure with the same archive policy for baseline and optimized

### No-CDS

- disable CDS/AppCDS/Leyden
- ensure no runtime javaagent
- use service-specific low-dirty policy when accepted
- for PetClinic, the accepted policy includes `MALLOC_ARENA_MAX=1`

### Diagnostic

- enable NMT
- capture smaps and smaps_rollup
- capture class histograms
- capture runtime class origins
- separate diagnostic logging runs from clean memory confirmation when logging could perturb memory

## Final Product Boundary

The final product boundary is:

```text
JMOA success = candidate + bytecode + packaging + runtime policy + verification.
```

The three case studies demonstrate this across:

- expanded classpath + CDS
- corrected fat JAR + CDS
- exploded Boot + no-CDS

The PetClinic result is the clearest version of the lesson:

```text
the same candidate failed under artificial fat-JAR launch,
then passed under the real exploded Boot deployment shape.
```
