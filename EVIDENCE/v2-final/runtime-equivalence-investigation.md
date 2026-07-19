# Runtime-Equivalence Investigation

Status: `RECONCILIATION_GATES_BLOCKED`.

The direct product matrix was frozen and audited before any new three-arm
measurement. Exact historical scripts, artifacts, image identities, launch
policies, and current accepted artifact hashes were recovered from the local
engineering archive rather than reconstructed from portfolio prose.

## Findings

| Service | Lineage | Replay or screen finding | Qualification result |
|---|---|---|---|
| PetClinic | Strict B0, V1, and V2 share one source universe | Frozen Phase 33M replay changed from 3/3 and -4,758 KB PSS to 0/3 and +8,647 KB | Historical replay drift blocks a new campaign |
| Doctor | Strict B0, D2, and final V2 share one source universe | Direct B0 to V2 remains confirmed at 3/3 and -5,809 KB PSS | Retrospective same-B0 control exceeds 1 MiB; dedicated qualification remains required |
| Patient | Strict B0, accepted V1, and accepted corrected V2 share one source universe | Direct screens measured `FB4E...`, not accepted V2 `4CFC...` | Artifact mismatch and noisy retrospective control block a verdict |

The PetClinic replay used the original runner, frozen image IDs, artifact
hashes, exploded-Boot mode, `-Xshare:off`, `MALLOC_ARENA_MAX=1`, warmup,
settle, and workload. Loaded classes still fell by about 154, but heap page
residency changed direction. This is runtime drift, not a missing optimizer
transformation.

## Decision

No rotated B0/V1/V2 block was launched because its predeclared admission gates
failed. The public source repository now contains an audited command wrapper,
runtime fingerprint capture, artifact-lineage proof, noise analyzer, gated
three-arm runner, and public evaluation entry point. Raw private evidence and
machine paths are not published here.
