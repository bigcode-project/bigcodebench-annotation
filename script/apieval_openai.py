"""Testing
from datasets import load_dataset

ds = load_dataset("bigcode/humaneval-x-bugs", "python")["test"]
idx = 0

def get_prompt_base(doc, language="python"):
    # See 
    # https://github.com/roG0d/CodeGeeX/blob/f66205b5f615a4eead9c26d7ec297e14738ea18d/codegeex/benchmark/evaluate_humaneval_x.py#L78
    # https://github.com/THUDM/CodeGeeX/pull/76#issuecomment-1500653190
    if language == "rust":
        main = "fn main(){}\n"
        prompt_base = main + doc["declaration"] + doc["prompt"]
    else:
        prompt_base = doc["prompt"]
    return prompt_base

prompt_base = get_prompt_base(ds[idx], language="python")
    
messages = [
    {
        "role": "user",
        "content": ds[idx]["instruction"],
    },
    {
        "role": "assistant",
        "content": prompt_base,
    },
]

gpt-4-0613
response = openai.ChatCompletion.create(
model="gpt-4-0613",
messages=messages
)
"""

import os
import openai
from openai import OpenAI
import termcolor
import jsonlines
import sys

from cdifflib import CSequenceMatcher
from camel_converter import to_snake
# from datasets import load_dataset
from typing import List
from tqdm import tqdm
client = OpenAI()

_CITATION = """

}
"""

def get_prompt_base(doc):
    return "Complete the following function:\n" + doc["prompt"]



class ParseError(Exception):
    pass

class ContentParser:

    @staticmethod
    def _entry_point_variations(entry_point: str) -> List[str]:
        # NOTE: workaround dataset's bug with entry point naming
        return [
            entry_point,
            to_snake(entry_point),
            entry_point[0].lower() + entry_point[1:],
        ]

    def __call__(self, prompt: str, content: str, entry_point: str):
        # NOTE: Model doesn't follow instructions directly:
        # adds description of change and sometimes fixes
        # typos, or other "bugs" in description.
        if "```" in content:
            content = content.split("```")[1]
        # first parse with assumption that content has description
        matcher = CSequenceMatcher(None, prompt, content)
        tag, _, _, j1, j2 = matcher.get_opcodes()[-1]
        if tag == "insert":
            return content[j1:j2]
        # second parse content with assumption that model wrote code without description
        for entry_point in self._entry_point_variations(entry_point):
            if entry_point in content:
                content = content.split(entry_point)[-1]
                return "".join(content.splitlines(keepends=True)[1:])
        raise ParseError(f"Prompt is not in content:\n{content}")


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
        # while True:
        # try:
        response = client.chat.completions.create(
            model=self._model,
            messages=messages,
            temperature=0.2,
            top_p=0.95,
            n=n
        )
        content_list = list()
        for i in range(n):
            message = response.choices[i].message
            assert message.role == "assistant"
            content_list.append(message.content)
        return content_list
        # except Exception as e:
        #     print("API EXCEPTION:", e)


if __name__ == '__main__':
    TIMES = 1
    VERBOSE = True
    MODEL = "gpt-4"
    input_file = sys.argv[1]
    # make test directory
    if not os.path.exists("results"):
        os.makedirs("results")
    
    # Load descriptions

    samples = []
    with jsonlines.open(input_file) as f:
        for s in f:
            samples.append(s)

    chat_wrapper = ChatWrapper(MODEL)
    parse_errors = 0
    parser = ContentParser()
    for idx, sample in enumerate(tqdm(samples)):
        prompt = get_prompt_base(sample)
        
        if VERBOSE:
            print(f"Processing {sample['task_id']} ({idx + 1}/{len(samples)}))...")
        sample["raw_generation"] = chat_wrapper(prompt, TIMES)
        try:
            sample["generation"] = [parser(prompt, generation_item, sample["task_id"]) for generation_item in sample["raw_generation"]]
        except ParseError as e:
            parse_errors += 1
            print("PARSE EXCEPTION:", e)
            sample["generation"] = [""]
        if VERBOSE:
            for i in range(TIMES):
                print(termcolor.colored(sample["task_id"], "yellow", attrs=["bold"]))
                print(termcolor.colored(prompt, "yellow"))
                print(termcolor.colored(sample["canonical_solution"], "red"))
                print(termcolor.colored(sample["generation"][i], "green")+"\n\n")
    if VERBOSE:
        print("parse error rate:", parse_errors / len(samples))

    results_filename = MODEL+f"_completions_"+input_file.split("/")[-1].split(".")[0]+".jsonl"
    with jsonlines.open("results/"+results_filename, "w") as writer:
        writer.write_all(samples)
