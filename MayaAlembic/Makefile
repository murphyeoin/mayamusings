LIB_A = AbcImport
LIB_B = AbcExport

MY_TARGETS = $(LIB_A) $(LIB_B)

.PHONY: all $(MY_TARGETS)
all: $(MY_TARGETS)

$(MY_TARGETS):
	@$(MAKE) -C $@;

