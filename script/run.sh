NAMES=(jenny)
for name in "${NAMES[@]}"; do
    cp data/raw/*"$name"*py data/clean
done
python script/parse.py

# coverage run -a -m pytest data/processed/f_328_jenny_wo_doc.py
# coverage run -a -m pytest --doctest-modules data/processed/f_333_jenny_w_doc.py
# coverage report -m

for name in "${NAMES[@]}"; do
    for file in data/processed/*"$name"*wo_doc.py; do
        if [[ $file != *"f_855"* ]]; then
            continue
        fi

        if ! coverage run -a -m pytest "$file"; then
            echo "Pytest failed on $file, stopping..."
            exit 1
        fi
    done

    for file in data/processed/*"$name"*w_doc.py; do
        if ! coverage run -a -m pytest --doctest-modules "$file"; then
            echo "Pytest failed on $file, stopping..."
            exit 1
        fi
    done
done
