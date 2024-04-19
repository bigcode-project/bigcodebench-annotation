#!/bin/bash

NAME=$1
cp data/raw/*ratna*.py data/clean
python script/parse.py
for file in data/processed/*wo_doc.py; do
    pytest "$file"
    if [ $? -ne 0 ]; then
        echo "Pytest failed on $file, stopping..."
        exit 1
    fi
done

for file in data/processed/*w_doc.py; do
    pytest --doctest-modules "$file"
    if [ $? -ne 0 ]; then
        echo "Pytest failed on $file, stopping..."
        exit 1
    fi
done