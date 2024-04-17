#!/bin/bash

cp data/raw/*ratan*.py data/clean
python script/parse.py
for file in data/processed/*.py; do
    # pytest --doctest-modules "$file"
    pytest "$file"
    if [ $? -ne 0 ]; then
        echo "Pytest failed on $file, stopping..."
        # exit 1
    fi
done