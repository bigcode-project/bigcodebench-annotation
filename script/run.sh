# NAMES=(indraneil chien jenny wenhao niklas hanhu ratna simon ming zhihan james xiaoheng armel)
# rm -rf data/clean/*
# mkdir -p data/clean
# for name in "${NAMES[@]}"; do
#     # Copy all files for other names
#     cp data/raw/*"$name"*py data/clean/
# done

# flake8 data/clean/*.py --select=E9,F63,F7,F82 --show-source --statistics
# python script/parse.py

# gzip data/BigCodeBench.jsonl > data/BigCodeBench.jsonl.gz

# # used for BigCodeBench evaluation
# pip install -U bigcodebench
# python script/eval.py --samples data/BigCodeBench.jsonl

# for file in data/processed/*wo_doc.py; do
    
#     if ! pytest "$file"; then
#         echo "Pytest failed on $file, stopping..."
#         exit 1
#     fi
# done

# for file in data/processed/*w_doc.py; do
    
#     if [[ "$file" == *"189_"* ]]; then
#         continue
#     fi

#     if ! pytest --doctest-modules "$file"; then
#         echo "Pytest failed on $file, stopping..."
#         exit 1
#     fi
# done
