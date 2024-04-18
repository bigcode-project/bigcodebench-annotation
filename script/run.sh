#!/bin/bash
cp data/raw/hanhu_data/*.py data/clean
python script/parse.py
for file in data/processed/*hanhu*w_doc*; do
    echo "Running pytest on $file..."
    pytest --doctest-modules "$file"    
    if [ $? -ne 0 ]; then
        echo "Pytest failed on $file, stopping..."
        # exit 1
    fi
done

for file in data/processed/*hanhu*wo_doc*; do
    echo "Running pytest on $file..."
    pytest "$file"    
    if [ $? -ne 0 ]; then
        echo "Pytest failed on $file, stopping..."
        # exit 1
    fi
done