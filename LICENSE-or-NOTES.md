# License And Publication Notes

This portfolio is a public-facing technical summary of JMOA optimization experiments.

## Recommended Publication Mode

Use this repository as a portfolio / case-study repository, not as a raw evidence dump.

Recommended before publishing:

- Review all private/internal service references.
- Keep raw local evidence out of the public repository.
- Publish sanitized summaries, not container logs or private project paths.
- Add a license only after deciding whether the portfolio is documentation-only or also includes reusable code.

## Suggested License Choices

For documentation only:

```text
CC BY 4.0
```

For code plus documentation:

```text
MIT
```

## Privacy Notes

Patient-service and doctor-service are internal/private case studies and should remain sanitized. The public reproducible centerpiece is the Spring PetClinic `customers-service` case study.

## Evidence Boundary

This repo should include:

- claim summaries
- sanitized case studies
- methodology
- tables
- diagrams
- public-safe evidence indexes

This repo should not include:

- private source code
- credentials or secrets
- local machine paths
- raw JARs or CDS archives
- raw smaps/NMT/class-histogram dumps unless sanitized and intentionally published
