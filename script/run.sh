NAMES=(chien jenny wenhao ratna niklas hanhu ming)
for name in "${NAMES[@]}"; do
    cp data/raw/*"$name"*py data/clean
done
python script/parse.py
for file in data/processed/*ming*wo_doc.py; do
    if [[ $file == *"f_855"* ]]; then
        continue
    fi

    if ! pytest "$file"; then
        echo "Pytest failed on $file, stopping..."
        exit 1
    fi
done

for file in data/processed/*ming*w_doc.py; do
    if [[ $file == *"ratna"* ]]; then
        continue
    fi

    if ! pytest --doctest-modules "$file"; then
        echo "Pytest failed on $file, stopping..."
        exit 1
    fi
done