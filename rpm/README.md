# RPM Packaging Demo

Demonstrates simple RPM packaging using a simple C++ project.

## Building

To compile the source code into the executable:

```bash
$ make clean all
```

Produces a single `hello` binary in `build/`.

## Packaging

To package the executable as an RPM for distribution:

```bash
$ make dist
```

The package version is dictated by the value in the `VERSION` file.

Constructs an RPM using the `example.spec` file and the build artifacts from `build/`.

During a pipeline run, the CI system can provide values for two variables:
- `CI_VERSION_QUALIFIER` - A qualifier appended to the version number to indicate a pre-release version
- `CI_BUILD` - Used to inform the RPM release number

For example:

```bash
$ CI_BUILD=57 make dist
```

Will construct an RPM named `example-1.0.0-57.el8.x86_64`.

Similarly, for a development build:

```bash
$ CI_VERSION_QUALIFIER=~363 CI_BUILD=5 make dist
```

Will construct an RPM named `example-1.0.0~363-5.el8.x86_64`.

## Testing

To execute unit tests:

```bash
$ make test
```

## Publishing

To publish the RPM(s) to the artifact repository:

```bash
$ make publish
```