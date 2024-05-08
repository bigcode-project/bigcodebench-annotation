import argparse
import os
import json
from tqdm import tqdm
from wildcode.gen.util import trusted_exec
from wildcode.eval.utils import (
    create_tempdir,
    reliability_guard,
)
def get_groundtruth(problems):
    print("\nAsserting the groundtruth...")
    if os.path.exists("checkpoint.txt"):
        with open("checkpoint.txt", "r") as f:
            checkpoint = int(f.read())
    else:
        checkpoint = 0
    for i, problem in tqdm(enumerate(problems[checkpoint:]), total=len(problems[checkpoint:])):
        task_id = problem["task_id"]
        try:
            with create_tempdir():
                maximum_memory_bytes = 32 * 1024 * 1024 * 1024
                reliability_guard(maximum_memory_bytes=maximum_memory_bytes)
                trusted_exec(
                    problem["prompt"] + "\n" + problem["clean_canonical_solution"],
                    problem["test"],
                    problem["entry_point"],
                )
        except:
            if i > 0:
                with open("checkpoint.txt", "w") as f:
                    f.write(str(i+checkpoint))
            raise Exception(f"Error in task data/raw/{task_id}")
    

def read_problems(jsonl_file):
    with open(jsonl_file, "r") as f:
        problems = []
        for line in f:
            data = json.loads(line)
            problems.append(data)
    return problems


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=str, help="Path to the samples")
    flags = parser.parse_args()

    problems = read_problems(flags.samples)
    get_groundtruth(problems)
if __name__ == "__main__":
    main()