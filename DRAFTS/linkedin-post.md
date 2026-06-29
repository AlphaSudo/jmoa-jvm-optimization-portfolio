# LinkedIn Post Draft

I have published v1 of my JVM optimization portfolio: JMOA, a build-time Spring Boot memory optimization project.

The work validates JMOA across three service shapes:

- internal Spring Boot service with CDS/AppCDS-style runtime: ~4.2 MB median memory reduction
- internal fat-JAR/CDS service after plugin/runtime hardening: ~2.7 MB median PSS reduction
- public Spring PetClinic `customers-service` with no CDS/AppCDS/Leyden: ~4.6 MB median PSS reduction under the project's real exploded Boot / `JarLauncher` deployment

The biggest lesson: JVM memory optimization is not just bytecode rewriting. Candidate selection, artifact materialization, classloader visibility, runtime policy, and PSS/Private_Dirty measurement all decide whether fewer classes become lower container memory.

Repo: `<link>`
