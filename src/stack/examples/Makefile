# @SI_Copyright@
# @SI_Copyright@
#

ROLLROOT	= ../../..
DEPENDS.DIRS	= spreadsheets
include $(STACKBUILD)/etc/CCRules.mk

ifeq ($(ROLLVERSION),)
ROLLVERSION = $(RPM_PACKAGE_VERSION)
endif


build:
	echo "Building sample spreadsheets"

install::
	env
	mkdir -p $(ROOT)/opt/stack/share/examples/spreadsheets/
	(cd spreadsheets/partition ; \
	for x in *.csv; do	\
		$(INSTALL) -m444 $$x $(ROOT)/opt/stack/share/examples/spreadsheets/$(ROLL)-$(ROLLVERSION)-partition-$$x ; \
	done)
	(cd spreadsheets/controller ; \
	for x in *.csv; do	\
		$(INSTALL) -m444 $$x $(ROOT)/opt/stack/share/examples/spreadsheets/$(ROLL)-$(ROLLVERSION)-controller-$$x ; \
	done)
	(cd spreadsheets/network ; \
	for x in *.csv; do	\
		$(INSTALL) -m444 $$x $(ROOT)/opt/stack/share/examples/spreadsheets/$(ROLL)-$(ROLLVERSION)-network-$$x ; \
	done)

