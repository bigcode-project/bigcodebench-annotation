# python script/openeval_openai.py

MODELS=(gpt-3.5-turbo-0125 gpt-4-turbo-2024-04-09)
for model in "${MODELS[@]}"; do
    python script/openeval_openai.py "$model"
done