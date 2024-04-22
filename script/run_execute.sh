# gpt-4-turbo-2024-04-09
# gpt-3.5-turbo-0125
# OpenCodeInterpreter-DS-6.7B 
# deepseek-coder-6.7b-instruct
# CodeQwen1.5-7B-Chat
# CodeLlama-7b-hf 
# starcoder2-3b 
# starcoder2-7b 
# starcoder2-15b
MODELS=(deepseek-coder-6.7b-instruct)
for model in "${MODELS[@]}"; do
    python script/execute_output.py results/"$model"_completions_open-eval.jsonl
done