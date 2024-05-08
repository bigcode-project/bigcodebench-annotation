# NAMES=(chien jenny wenhao niklas hanhu ratna simon ming)
NAMES=(zhihan)
# for name in "${NAMES[@]}"; do
#     cp data/raw/*"$name"*py data/clean
# done
for i in {933..981}
do
    if [ -e data/raw/f_"$i"_zhihan.py  ]
    then
        cp data/raw/f_"$i"_zhihan.py data/clean
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
        if ! pytest --doctest-modules "$file"; then
            echo "Pytest failed on $file, stopping..."
            exit 1
        fi
    done
done