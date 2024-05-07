NAMES=(
    zhihan
)
for name in "${NAMES[@]}"; do
    cp data/raw/*"$name"*py data/clean
done
flake8 data/clean/*refined*.py --select=E9,F63,F7,F82 --show-source --statistics
python script/parse.py

for name in "${NAMES[@]}"; do
    for file in data/processed/*"$name"*refined*wo_doc.py; do
        if pytest "$file"; then
            # Increment the count on successful pytest
            count=$((count + 1))
        else
            echo "Pytest failed on $file, stopping..."
            exit 1
        fi
    done

    for file in data/processed/*"$name"*refined*w_doc.py; do
        if pytest --doctest-modules "$file"; then
            # Increment the count on successful pytest
            count=$((count + 1))
        else
            echo "Pytest failed on $file, stopping..."
            exit 1
        fi
    done
done

# Print the total count of successful pytest executions
echo "Total successful pytest executions: $count"
