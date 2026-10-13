# Patient: provisional Java 26/Leyden memory benchmark in JMOA 2.15

## Outcome and qualification

The exact tested Patient configuration showed **8.38 MiB lower median
stopped-process PSS** across twelve fresh paired blocks. Its **conditional
lower saving bound was 8.19 MiB**. **Original calibration failed and used an
approved post-observation exception; performance bounds remain unqualified or
failed.** Startup/cache warmth, production parity and uploaded-binary parity
remain unqualified. The release contains no new Maven binaries.

## The engineering question

The Patient workload retains Java 26/Leyden caches and the intended service
behavior. The comparison is direct clean B0 versus the frozen composed JMOA
candidate; each artifact has its own cache. Historical baseline/UTF8 and
incremental metadata medians were not added to manufacture a total.

The audited artifact contains 788 rewritten static call sites: 455 Tier 1 and
333 Tier 2 across 498 owners, with 192 logical and 195 physical helpers.
Those are static identities, not invocation counts or proof every site executed.
The final process uses no JMOA optimization javaagent.

## Measurement and interpretation

Twenty-four fresh confirmation units form twelve adjacent, balanced-order
pairs. Median saving is 8,586 KiB. Eleven of twelve pairs strictly exceed
8 MiB; one saves 8,096 KiB. The third-smallest saving is 8,384 KiB, giving the
conditional order-statistic bound under independent, exchangeable, stable
pairs. Those assumptions are not proved. Process PSS, cgroup file charge,
artifact bytes and AOT-cache file size remain distinct measurements.

The original eight-control block exceeded its frozen precision limits:
540 KiB maximum difference versus 512 KiB, and 176 KiB absolute median bias
versus 128 KiB. The human admitted that exact observed block before untouched
fresh confirmation. Original calibration remains failed.

## Costs and remaining limits

All 82 cost metrics are published. Five confirmation margin tests failed:
startup, early read-user, early actuator-prometheus, early stroke-low and
repeated delete. Cost calibration and stationarity/assessability are unqualified.
Passing numerical rows therefore do not establish passing performance bounds.

Both arms share the allocator and native trimming policy. The composed candidate
reduces dependency line-number observability, a cost not enabled by the stable
2.1 raw LVT/LVTT reducer. A finite synthetic stroke fixture is not live ML
equivalence; ConfigClient is absent. Private raw inputs are not distributed.

The tested producer is an admitted compatibility port. Equality with uploaded
stable 2.1 plugin/runtime binaries is unresolved, so 2.15 is an evidence release
and does not replace stable Maven version 2.1.0.

## Relation to PetClinic

PetClinic 2.1 has an accepted 14.88 MiB process-PSS deployment saving with
packaging as the dominant factorial main effect and passing frozen cost gates.
Patient's different JDK, service, cache policy and provisional acceptance state
prevent interpreting 8.38 MiB as a version-to-version regression or speedup.

## Evidence

- [Patient pairs, identities, costs and limitations](../EVIDENCE/v2.15/patient-scoped-ram-benchmark.md)
- [Machine-readable record](../EVIDENCE/v2.15/patient-scoped-ram-benchmark.json)
- [2.15 companion paper](https://github.com/AlphaSudo/jmoa/blob/main/docs/paper/jmoa-v2.15-patient-leyden-memory-evidence.md)
- [2.15 release](https://github.com/AlphaSudo/jmoa/releases/tag/v2.15)
