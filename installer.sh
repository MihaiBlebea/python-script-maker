#!/bin/bash

if [[ $* == *-u* ]]; then
	echo "uninstalling the scriptmaker"
	unlink ${HOME}/.local/bin/scriptmaker && \
	rm -rf ${HOME}/.local/bin/_scriptmaker
else
	echo "installing the scriptmaker"
	git clone https://github.com/MihaiBlebea/python-script-maker && \
	cp -r ./python-script-maker/ ${HOME}/.local/bin/_scriptmaker/ && \
	rm -rf ./python-script-maker && \
	python3 -m venv ${HOME}/.local/bin/_scriptmaker/virtualenv && \
	ln -s ${HOME}/.local/bin/_scriptmaker/execute.sh ${HOME}/.local/bin/scriptmaker
fi
