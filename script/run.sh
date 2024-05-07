NAMES=(zhihan)

for name in "${NAMES[@]}"; do
    if [[ "$name" == "zhihan" ]]; then
        # Copy only files in the range 981-1031 for zhihan
        for file in data/raw/*"$name"*py; do
            if [[ "$file" =~ .*[[:digit:]]{4}_(981|98[2-9]|99[0-9]|100[0-9]|101[0-9]|102[0-9]|1031)_zhihan.*py ]]; then
                cp "$file" data/clean/
            fi
        done
    else
        # Copy all files for other names
        cp data/raw/*"$name"*py data/clean/
    fi
done

flake8 data/clean/*.py --select=E9,F63,F7,F82 --show-source --statistics
python script/parse.py

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
