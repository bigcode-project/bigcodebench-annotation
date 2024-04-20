# python script/openeval_openai.py

MODELS=(codellama/CodeLlama-7b-hf bigcode/starcoder2-3b bigcode/starcoder2-7b bigcode/starcoder2-15b)
for model in "${MODELS[@]}"; do
    python script/openeval_code_osmodel.py "$model"
done