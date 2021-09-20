LATEST ?= 0
NAME := avojak/example
# Base version is defined in the VERSION file
VERSION := `cat VERSION`
# If CI_BUILD is provided, append .CI_BUILD
VERSION := $(if $(CI_BUILD),$(VERSION).$(CI_BUILD),$(VERSION))
# If CI_VERSION_QUALIFIER is provided, append -CI_VERSION_QUALIFIER
VERSION := $(if $(CI_VERSION_QUALIFIER),$(VERSION)-$(CI_VERSION_QUALIFIER),$(VERSION))
# Use a tag list in case we want to tag multiple platforms, architectures, etc.
TAGLIST := -t $(NAME):$(VERSION)
# Tag as latest if the LATEST variable is passed as 1
ifeq ($(LATEST),1)
	TAGLIST += -t $(NAME):latest
endif
DOCKER_BUILD_CMD = docker build $(TAGLIST) .

.PHONY: all image

all: image

image:
	$(DOCKER_BUILD_CMD)