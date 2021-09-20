LATEST ?= 0
NAME := avojak/example
VERSION := `cat VERSION`
VERSION := $(if $(CI_BUILD),$(VERSION).$(CI_BUILD),$(VERSION))
VERSION := $(if $(CI_VERSION_QUALIFIER),$(VERSION)-$(CI_VERSION_QUALIFIER),$(VERSION))
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