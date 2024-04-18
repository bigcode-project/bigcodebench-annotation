#!/bin/bash

cp data/raw/*armel*.py data/clean

python script/parse.py

failed_pytests="failed_pytests.txt"
failed_doctests="failed_doctests.txt"

for file in data/processed/*armel*.py; do
    pytest "$file"
    if [ $? -ne 0 ]; then
        echo "$file" >> "$failed_pytests"
    fi
done

for file in data/processed/*armel_w_doc*.py; do
    pytest --doctest-modules "$file"
    if [ $? -ne 0 ]; then
        echo "$file" >> "$failed_doctests"
    fi
done