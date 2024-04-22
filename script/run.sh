NAMES=(chien jenny wenhao niklas hanhu)
for name in "${NAMES[@]}"; do
    cp data/raw/*"$name"*py data/clean
done
python script/parse.py

for name in "${NAMES[@]}"; do
    for file in data/processed/*"$name"*wo_doc.py; do
        if [[ $file == *"f_855"* ]]; then
            continue
        fi

        if ! coverage run -m pytest "$file"; then
            echo "Pytest failed on $file, stopping..."
            exit 1
        fi
    done

    for file in data/processed/*"$name"*w_doc.py; do
        if ! coverage run -m pytest --doctest-modules "$file"; then
            echo "Pytest failed on $file, stopping..."
            exit 1
        fi
    done
done
