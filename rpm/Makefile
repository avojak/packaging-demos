# Derive the package name from the .spec file
PACKAGE := $(shell basename *.spec .spec)
# Create the list of --define arguments to pass to rpmbuild, starting with override of _topdir to use our local rpmbuild directory
RPMBUILD_DEFINITIONS := --define "_topdir %(pwd)/rpmbuild"
# If CI_VERSION_QUALIFIER is provided, add a --define argument to pass along to rpmbuild
RPMBUILD_DEFINITIONS += $(if $(CI_VERSION_QUALIFIER),--define "_ci_version_qualifier $(CI_VERSION_QUALIFIER)")
# If CI_BUILD is provided, add a --define argument to pass along to rpmbuild
RPMBUILD_DEFINITIONS += $(if $(CI_BUILD),--define "_ci_build $(CI_BUILD)")
RPMBUILD_CMD := rpmbuild $(RPMBUILD_DEFINITIONS)

all: init
	g++ -Wall src/hello.cpp -o build/hello

init:
	mkdir -p build rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SRPMS}

clean:
	rm -rf rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SRPMS}/*
	rm -rf build/*

test:
	@echo "Placeholder for unit tests"

dist: all
	cp -r build/* rpmbuild/SOURCES/
	$(RPMBUILD_CMD) -ba $(PACKAGE).spec