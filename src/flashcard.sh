#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
    echo 'Python3 not downlaoded' >&2
    exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r src/requirements.txt
python3 src/main.py $1
deactivate