#!/bin/bash

# Loop through all python files in the current directory
for file in data/processed/*.py; do
    pytest "$file"
    if [ $? -ne 0 ]; then
        echo "Pytest failed on $file, stopping..."
        exit 1
    fi
done