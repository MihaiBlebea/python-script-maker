#!/bin/bash

GIT_URL=$(git config --get remote.origin.url)

if [[ $* == *-u* ]]; then
	echo "uninstalling the scriptmaker"
	unlink ${HOME}/.local/bin/scriptmaker && \
	rm -rf ${HOME}/.local/bin/_scriptmaker
else
	echo "installing the scriptmaker"
	git clone ${GIT_URL} && \
	cp -r ./python-script-maker/ ${HOME}/.local/bin/_scriptmaker/ && \
	python3 -m venv ${HOME}/.local/bin/_scriptmaker/virtualenv && \
	ln -s ${HOME}/.local/bin/_scriptmaker/execute.sh ${HOME}/.local/bin/scriptmaker
fi
