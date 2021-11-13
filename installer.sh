#!/bin/bash

INSTALL_FOLDER="script_maker"

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
	cp -f ./scriptmaker ${HOME}/.local/bin/scriptmaker
	# git clone https://github.com/MihaiBlebea/python-script-maker && \
	# mv -f ./python-script-maker/ ${HOME}/.local/bin/_scriptmaker/ && \
	# python3 -m venv ${HOME}/.local/bin/_scriptmaker/virtualenv && \
	# ln -s ${HOME}/.local/bin/_scriptmaker/execute.sh ${HOME}/.local/bin/scriptmaker
fi
