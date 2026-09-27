# PetClinic: From Memory Noise to a Claimable JMOA 2.1 Result

## The outcome

The accepted JMOA R41F deployment reduced process PSS by **14.88 MiB** and
target-cgroup RAM by **16.24 MiB** versus the documented strict no-JMOA B0
exploded deployment. All 12 held-out blocks favored R41F.

That one sentence took far more than one benchmark run. The engineering problem
was to distinguish a real deployment effect from JVM lifecycle variance,
allocator retention, file charge, packaging, and capture defects.

## Why the earlier numbers disagreed

Earlier PetClinic studies answered different questions:

- accepted V1 versus V2 measured engineering evolution;
- R4.87 measured exact R41F versus accepted V2E;
- T7R measured R41F versus B0 under symmetric fat packaging and failed its
  frozen 4 MiB PSS endpoint;
- T7R2 established a smaller but claimable target-cgroup benefit under that
  symmetric comparison;
- T7R23 finally measured both content and packaging roles in one four-arm
  held-out design.

Those deltas were never arithmetically additive. Each had its own comparator,
packaging, endpoint, and claim boundary.

## The defects that had to be eliminated

The investigation found and fixed several measurement-path failures before the
successful campaign:

- cgroup file charge could reverse an otherwise favorable PSS result;
- same-artifact anonymous/native variance exceeded early gates;
- suspend/hibernate broke continuous control epochs;
- two sequential views of a live process could disagree;
- post-claim native trim exposed residual reclaim;
- a boundary audit sampled the wrong instant;
- one PowerShell helper lost fields when shaping command results;
- a workload child ledger could be semantically complete but structurally
  incomplete for the reducer.

Failed campaigns remained failed evidence. Their observations were not recycled
into the successful result.

## The final design

The final campaign used five role qualifications, ten same-artifact control
pairs, four direct screen pairs, and twelve held-out four-arm blocks. The four
arms crossed strict B0/R41 content with exploded/fat packaging. Claim frames
were captured from stopped processes under a frozen Java 17/SerialGC tuple,
with swap, reclaim, workload, trim, process identity, and teardown evidence.

The campaign executed 81 sessions without replacement. PSS, Private Dirty,
cgroup anonymous/file/kernel memory, CPU, startup, latency, faults, and
semantic outcomes were reduced under a predeclared estimator.

## Result and interpretation

The primary R41F-minus-B0E process-PSS median was -15,241.5 KiB, with
12/12 favorable blocks and exact sign-test `p=0.00048828125`. The bootstrap
95% interval was [-16,109.5, -15,052.5] KiB. `memory.current` corroborated the
result at -17,033,216 bytes median.

The factorial matters. Packaging contributed the dominant -12,715.25 KiB main
effect; content contributed -2,465 KiB; their interaction was +3,801.5 KiB.
The result is therefore a claim about the exact JMOA deployment—not a claim
that metadata removal alone saved 15 MiB.

Native process-heap PSS increased 2,972 KiB even while total PSS fell. That
adverse component is retained in the public record. Java-heap PSS fell 15,092
KiB and cgroup anonymous, file, and kernel components all moved favorably.

## Engineering lesson

The most important lesson is that JVM memory optimization must own the whole
path from bytecode decision to deployed measurement. Transformation safety,
packaging, runtime origins, lifecycle state, kernel accounting, statistics, and
product costs are one system.

JMOA's value is not merely that one artifact won. It is that the system rejected
dozens of attractive but invalid stories until an exact deployment survived
all of those layers.

## Links

- [JMOA 2.1 technical paper](https://github.com/AlphaSudo/jmoa/blob/main/docs/paper/jmoa-v2.1-petclinic-memory-engineering.md)
- [Authoritative result](https://github.com/AlphaSudo/jmoa/blob/main/docs/product-evidence/petclinic-r41f-b0-t7r23-result.md)
- [JMOA source](https://github.com/AlphaSudo/jmoa)
- [JMOA 2.1 release](https://github.com/AlphaSudo/jmoa/releases/tag/v2.1.0)
