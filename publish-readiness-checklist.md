# Publish Readiness Checklist

Generated: 2026-06-28

## Automated Draft Status

- [x] README exists and includes results table.
- [x] PetClinic public no-CDS case study exists.
- [x] Doctor case study exists and uses corrected ~2.7 MB claim.
- [x] Patient addendum exists and separates 31D-P2 from 31E.
- [x] Plugin/runtime hardening technical note exists.
- [x] Evidence inventory exists.
- [x] Evidence summaries exist.
- [x] Claim guardrails are documented.
- [x] LinkedIn draft exists.
- [x] CV bullet draft exists.
- [x] Job application paragraph draft exists.

## Human Review Required

- [ ] Confirm all private/internal service descriptions are acceptable.
- [ ] Confirm no credentials or internal URLs are present.
- [ ] Confirm no private patient/doctor data is present.
- [ ] Decide license or publication note.
- [ ] Decide whether to publish diagrams as Mermaid, rendered images, or both.
- [ ] Add actual GitHub repo URL to LinkedIn draft.
- [ ] Review generated PDF if/when exported.

## Claim Audit

- [x] Doctor -5.9 MB is not cited as final.
- [x] Doctor Phase 32I is not cited as final.
- [x] Patient 31D-P2 and 31E are not mixed.
- [x] PetClinic claim says no-CDS.
- [x] PetClinic claim says exploded Boot / `JarLauncher`.
- [x] PetClinic claim includes `MALLOC_ARENA_MAX=1`.
- [x] PetClinic fat-JAR result is described as a failure/negative control, not final.
- [x] JMOA is not described as always winning.

## Recommended Publish Order

1. Review this portfolio folder locally.
2. Create a public GitHub repo named `jmoa-jvm-optimization-portfolio`.
3. Copy or push this folder as the repo root.
4. Publish README and PetClinic case first.
5. Add Doctor and Patient sanitized case studies.
6. Post short LinkedIn summary with repo link.
7. Update CV/project section.
