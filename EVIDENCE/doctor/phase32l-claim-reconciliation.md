# Doctor Phase 32L Claim Reconciliation

## Final Claim

Doctor-service D2-fixed is a confirmed modest memory win:

```text
~2.7 MB median PSS reduction
~1.8 MB median Private_Dirty reduction
3/3 paired wins
corrected Spring Boot fat JAR
per-candidate CDS
no runtime javaagent
```

## Do Not Cite

- Phase 32I as a final result
- the mistaken -5.9 MB median
- the broken pre-substitution fat JAR as a valid optimized artifact

## What Changed

Phase 32I was invalid because optimized dependency JARs existed on disk but were not packaged into `BOOT-INF/lib`.

The corrected path:

```text
discover broken materialization
fix fat-JAR substitution
fix PACKAGE_SAM multi-root adapter placement
add AdapterReferenceValidator
retrain CDS
rerun confirmation
audit median calculation
publish corrected ~2.7 MB result
```

## Portfolio Wording

Use:

```text
Doctor-service confirmed a modest ~2.7 MB median PSS reduction after correcting fat-JAR materialization and adapter placement defects.
```

Avoid:

```text
Doctor-service achieved a ~5.9 MB median reduction.
```
