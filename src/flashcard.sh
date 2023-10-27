#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
    echo 'Python3 not downlaoded , Please dowload to run.' >&2
    exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py $1
deactivate