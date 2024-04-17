import os
import openai
import jsonlines
import termcolor

from cdifflib import CSequenceMatcher
from camel_converter import to_snake
from datasets import load_dataset
from typing import List, Dict
from tqdm import tqdm

PROMPT = """\
# Choose the most suitable labels for the give program:
SQL
CSV
DataFrames
Time
JSON
XML
HTML
Image
Text
Built-in Data Structure
Analysis
Networking
Processing
Visualization
File Storage    
Encrytion
    
# You should output the suitable labels in a list format, such as ["CSV", "DataFrames"].
"""
def get_prompt(sample):
    return PROMPT + sample["prompt"] + sample["canonical_solution"]
    
class ChatWrapper:

    def __init__(self, model: str):
        self._model = model

    def __call__(self, prompt: str, n: int) -> str:
        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]
        while True:
            try:
                response = openai.ChatCompletion.create(
                    model=self._model,
                    messages=messages,
                    temperature=0.2,
                    top_p=0.95,
                    n=n
                )
                content_list = list()
                for i in range(n):
                    message = response["choices"][i]["message"]
                    assert message["role"] == "assistant"
                    content_list.append(message["content"])
                return content_list
            except Exception as e:
                print("API EXCEPTION:", e)
                
if __name__ == '__main__':
    TIMES = 1
    MODEL = "gpt-4-0613"
        
    with jsonlines.open("OpenEval_perturbed.jsonl") as f:
        samples = [line for line in f]
        
    chat_wrapper = ChatWrapper(MODEL)
    
    for idx, sample in enumerate(tqdm(samples)):
        prompt = get_prompt(sample)
        sample["labels"] = chat_wrapper(prompt, TIMES)
    
    results_filename = f"OpenEval_labeled.jsonl"
    with jsonlines.open(results_filename, "w") as writer:
        writer.write_all(samples)