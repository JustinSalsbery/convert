# author: Justin Salsbery

# File settings:
FILE := convert
INSTALL_DIR := /usr/local/bin

# Make settings:
.ONESHELL:
.SILENT:

install:
	cp ${FILE}.py ${INSTALL_DIR}/${FILE}
	chmod +x ${INSTALL_DIR}/${FILE}

uninstall:
	rm -f ${INSTALL_DIR}/${FILE}
