#!/bin/bash

INSTALL_FOLDER="script_maker"

SCRIPTMAKER_PATH="${PWD}"

if [[ $* == *-u* ]]; then
	echo "uninstalling the scriptmaker"
	rm -rf ${HOME}/.local/bin/scriptmaker
else
	echo "installing the scriptmaker"
	if [[ $INSTALL_FOLDER == "$(basename $PWD)" ]]; then
		echo "you are in the correct folder"
	else
		echo "you need the full instalaltion"
		git clone https://github.com/MihaiBlebea/python-script-maker "${INSTALL_FOLDER}" && \
		cd "${INSTALL_FOLDER}"
	fi
	sed 's?__PATH__?'`pwd`'?' ./scriptmaker.tmp > scriptmaker && \
	chmod +x scriptmaker && \
	mv -f ./scriptmaker ${HOME}/.local/bin/scriptmaker
fi
