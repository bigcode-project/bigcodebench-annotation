import os
from transformers import AutoModelForCausalLM, AutoTokenizer

import termcolor
import jsonlines
import sys

from cdifflib import CSequenceMatcher
from camel_converter import to_snake
# from datasets import load_dataset
from typing import List
from tqdm import tqdm
device = "cuda" # the device to load the model onto

_CITATION = """

}
"""

EOS = ["\ndef", "\nclass ", "\nimport ", "\nfrom ", "\nassert ", "\n# "]

def get_prompt_base(doc):
    return "Complete the following function:\n" + doc["prompt"]

def stop_at_stop_token(decoded_string, stop_tokens):
        """
        Produces the prefix of decoded_string that ends at the first occurrence of
        a stop_token.
        WARNING: the decoded_string *must not* include the prompt, which may have stop tokens
        itself.
        """
        min_stop_index = len(decoded_string)
        for stop_token in stop_tokens:
            stop_index = decoded_string.find(stop_token)
            if stop_index != -1 and stop_index < min_stop_index:
                min_stop_index = stop_index
        return decoded_string[:min_stop_index]

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
        if "### Response:\n" in content:
            content = content.split("### Response:\n")[1]
        if "```" in content:
            content = content.split("```")[1]
        # first parse with assumption that content has description
        matcher = CSequenceMatcher(None, prompt, content)
        tag, _, _, j1, j2 = matcher.get_opcodes()[-1]
        if tag == "insert":
            return stop_at_stop_token(content[j1:j2], EOS)
        # second parse content with assumption that model wrote code without description
        for entry_point in self._entry_point_variations(entry_point):
            if "def " + entry_point in content:                
                content = content.split(entry_point)[1]
                return stop_at_stop_token("".join(content.splitlines(keepends=True)[1:]), EOS)
        return stop_at_stop_token("".join(content.splitlines(keepends=True)[1:]), EOS)


class ChatWrapper:

    def __init__(self, model: str):
        
        self.model = AutoModelForCausalLM.from_pretrained(
                            model,
                            torch_dtype="auto",
                            device_map="auto"
                        )
        self.tokenizer = AutoTokenizer.from_pretrained(model)

    def __call__(self, prompt: str, max_new_tokens=1024, temperature=0, top_p=0.95, n=1) -> List[str]:
        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(device)

        if not temperature:
            generated_ids = self.model.generate(
                model_inputs.input_ids,
                do_sample=False,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                num_return_sequences=n,
            )
        else:
            generated_ids = self.model.generate(
                model_inputs.input_ids,
                do_sample=True,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                num_return_sequences=n,
            )

        content_list = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
        return content_list


if __name__ == '__main__':
    TIMES = 1
    VERBOSE = True
    TEMPERATURE = 0
    MODEL = sys.argv[1]
    input_file = "data/open-eval.jsonl"
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
        sample["raw_generation"] = chat_wrapper(prompt, temperature=TEMPERATURE, n=TIMES)
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

    results_filename = MODEL.split("/")[-1]+f"_completions_"+input_file.split("/")[-1].split(".")[0]+".jsonl"
    with jsonlines.open("results/"+results_filename, "w") as writer:
        writer.write_all(samples)
