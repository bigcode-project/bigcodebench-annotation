NAMES=(chien jenny wenhao niklas hanhu ratna simon ming zhihan james xiaoheng)

for name in "${NAMES[@]}"; do
    # Copy all files for other names
    cp data/raw/*"$name"*py data/clean/
done

flake8 data/clean/*.py --select=E9,F63,F7,F82 --show-source --statistics
python script/parse.py

gzip -c data/open-eval.jsonl > data/open-eval.jsonl.gz

# # used for WildCode evaluation
# pip install -U wild-code
# python script/eval.py --samples data/open-eval.jsonl

for name in "${NAMES[@]}"; do

    for file in data/processed/*"$name"*wo_doc.py; do
        
        if ! pytest "$file"; then
            echo "Pytest failed on $file, stopping..."
            exit 1
        fi
    done

    for file in data/processed/*"$name"*w_doc.py; do
        
        if [[ "$file" == *"f_2248_hanhu"* ]]; then
            continue
        fi

        if ! pytest --doctest-modules "$file"; then
            echo "Pytest failed on $file, stopping..."
            exit 1
        fi
    done
done
