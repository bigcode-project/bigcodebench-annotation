NAMES=(chien jenny wenhao niklas hanhu ratna simon xiaoheng zhihan ming)

for name in "${NAMES[@]}"; do
    if [[ "$name" == "zhihan" ]]; then
        # Copy only files in the range 981-1031 for zhihan
        for file in data/raw/*"$name"*py; do
            # if f_ID where ID is between 981 and 1031
            if [[ "$file" == *"f_"* ]]; then
                id=$(echo "$file" | grep -oP '(?<=f_)\d+')
                if [[ "$id" -ge 981 && "$id" -le 1031 ]]; then
                    cp "$file" data/clean/
                fi
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
