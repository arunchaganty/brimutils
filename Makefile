SHELL=bash
ALIASES_SRC="aliases.sh"
BIN_DIRS=\
	bin \
	ext/bitly/data_hacks
BINS=$(BIN_DIRS:=/*)

ifndef PREFIX
	PREFIX=out/bin
endif

ifndef ALIASES
	ALIASES=out/bash_aliases
endif

# This is sort of awful
define file_not_exists
	([ ! -f $(1) ] || (echo "File already exists: $(1)" && false))
endef

default: update build

build: build-bins build-aliases

install: install-check install-bins install-aliases

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

build-aliases:
	@echo ""
	@echo "-- Making alias commands."
	@echo ""

install-check:
	@echo ""
	@echo "-- Preparing to install."
	@echo ""
	@$(foreach F, $(shell ls ${BINS}), \
	   $(call file_not_exists, ${PREFIX}/$(shell basename $F)) &&) true

install-bins:
	@echo ""
	@echo "-- Installing binaries into ${PREFIX}."
	@echo ""
	mkdir -p ${PREFIX}
	cp -p ${BINS} ${PREFIX}/
	$(foreach F, $(shell ls ${BINS}), \
	  chmod +x ${PREFIX}/$(shell basename $F);) true

install-aliases:
ifndef NO_ALIASES
	@echo ""
	@echo "-- Installing aliases into ${ALIASES}."
	@echo ""
	mkdir -p $(shell dirname ${ALIASES})
	echo "" >> ${ALIASES}
	echo "" >> ${ALIASES}
	echo "# Added by exoutils." >> ${ALIASES}
	cat ${ALIASES_SRC} >> ${ALIASES}
else
	@echo ""
	@echo "-- Not installing aliases."
	@echo ""
endif
