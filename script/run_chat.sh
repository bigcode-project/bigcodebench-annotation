# python script/openeval_openai.py

MODELS=(m-a-p/OpenCodeInterpreter-DS-6.7B deepseek-ai/deepseek-coder-6.7b-instruct Qwen/CodeQwen1.5-7B-Chat)
for model in "${MODELS[@]}"; do
    python script/openeval_chat_osmodel.py "$model"
done