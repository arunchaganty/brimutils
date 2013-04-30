SHELL=bash
BIN_DIRS=\
	bin \
	ext/bitly/data_hacks
BINS=$(BIN_DIRS:=/*)

ifndef PREFIX
	PREFIX=out/bin
endif

# This is sort of awful
define file_not_exists
	([ ! -f $(1) ] || (echo "File already exists: $(1)" && false))
endef

default: update build

build: build-bins

install: install-check install-bins

update:
	@echo ""
	@echo "-- Updating submodules."
	@echo ""
	git submodule init
	git submodule update

build-bins:
	@echo ""
	@echo "-- Making binaries."
	@echo ""

install-check:
	@echo ""
	@echo "-- Preparing to install."
	@echo ""
ifdef CAREFUL
	@$(foreach F, $(shell ls ${BINS}), \
	   $(call file_not_exists, ${PREFIX}/$(shell basename $F)) &&) true
endif

install-bins:
	@echo ""
	@echo "-- Installing binaries into ${PREFIX}."
	@echo ""
	mkdir -p ${PREFIX}
	cp -p ${BINS} ${PREFIX}/
	$(foreach F, $(shell ls ${BINS}), \
	  chmod +x ${PREFIX}/$(shell basename $F);) true
