NAMES=(chien jenny wenhao niklas hanhu ming)
for name in "${NAMES[@]}"; do
    cp data/raw/*"$name"*py data/clean
done
python script/parse.py

# pytest data/processed/f_359*.py
for name in "${NAMES[@]}"; do
    for file in data/processed/*"$name"*wo_doc.py; do
        if [[ $file == *"f_855"* ]]; then
            continue
        fi

        if ! pytest "$file"; then
            echo "Pytest failed on $file, stopping..."
            exit 1
        fi
    done

    for file in data/processed/*"$name"*w_doc.py; do
        if ! pytest --doctest-modules "$file"; then
            echo "Pytest failed on $file, stopping..."
            exit 1
        fi
    done
done