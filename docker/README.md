# Docker Packaging Demo

Demonstrates simple Docker image packaging.

## Building

```bash
$ make all
```

Produces a single Docker image tagged with the version from the `VERSION` file.

During a pipeline run, the CI system can provide values for three variables:
- `CI_VERSION_QUALIFIER` - A qualifier appended to the version number to indicate a pre-release version
- `CI_BUILD` - Used to inform the RPM release number
- `LATEST` - Used to inform the build whether or not to also tag the build as `latest`

For example:

```bash
$ CI_BUILD=57 make image
```

Will tag an image named `example:1.0.0.57`.

Similarly, for a development build:

```bash
$ CI_VERSION_QUALIFIER=CICD-363 make image
```

Will tag an image named `example:1.0.0-CICD-363`.

```bash
$ LATEST=1 CI_BUILD=57 make image
```

Will tag an image twice:
- `example:1.0.0.57`
- `example:latest`