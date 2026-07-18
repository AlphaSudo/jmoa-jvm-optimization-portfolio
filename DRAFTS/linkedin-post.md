# LinkedIn Post Draft

I have published JMOA V2, an evidence-driven build-time JVM footprint optimizer for Spring Boot.

V2 delivered confirmed incremental median PSS reductions over V1 across three service surfaces:

- Spring PetClinic customers-service, no-CDS low-dirty policy: -6,012 KB
- Doctor service, application CDS: -5,156 KB
- Patient service, stock JDK base-CDS low-dirty policy: -8,279 KB

Every result used three paired runs, six valid runs, zero workload errors, V2-C evidence validation, and V2-D memory attribution. The runtime policy was selected per service; JMOA does not claim that one CDS mode wins everywhere.

The engineering lesson was bigger than bytecode rewriting. A credible JVM optimizer also needs artifact auditing, Spring Boot materialization, runtime-origin proof, measurement validation, negative-result retention, and memory attribution.

Source: https://github.com/AlphaSudo/jmoa

Case studies: https://github.com/AlphaSudo/jmoa-jvm-optimization-portfolio
