#!/bin/bash

BIN_PATH="${HOME}/.local/bin/_scriptmaker"
eval "${BIN_PATH}/virtualenv/bin/python3 ${BIN_PATH}/project.py \"${@}\""