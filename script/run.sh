#!/bin/bash
cp data/raw/hanhu_data/*.py data/clean
python script/parse.py
for file in data/processed/*hanhu*.py; do
    echo "Running pytest on $file..."
    if [[ "$file" == *"_w_doc.py"* ]]; then
        pytest --doctest-modules "$file"
    elif [[ "$file" == *"_wo_doc.py"* ]]; then
        pytest "$file"
    fi

    if [ $? -ne 0 ]; then
        echo "Pytest failed on $file, stopping..."
        # exit 1
    fi
done