#!/bin/bash

NAMES=(
    chien
    jenny
    wenhao
    ratna
    niklas
)
for name in "${NAMES[@]}"; do
    cp data/raw/*"$name"*py data/clean
done
python script/parse.py
for file in data/processed/*wo_doc.py; do
    if ! pytest "$file"; then
        echo "Pytest failed on $file, stopping..."
        exit 1
    fi
done

for file in data/processed/*w_doc.py; do
    if ! pytest --doctest-modules "$file"; then
        echo "Pytest failed on $file, stopping..."
        exit 1
    fi
done