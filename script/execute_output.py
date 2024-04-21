import subprocess
import jsonlines
from tqdm import tqdm
import sys
import os
import termcolor
import json
import tempfile

if __name__ == '__main__':
    jsonl_file = sys.argv[1]
    outputs = []
    ref_ids = []
    with jsonlines.open(jsonl_file) as f:
        for s in f:
            outputs.append(s)
    pass_count = 0
    task_record = dict()
    original_dir = os.getcwd()
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(f"{jsonl_file.replace('.jsonl', '.py')}","w") as fp:
            os.chdir(temp_dir)
            for output in tqdm(outputs):
                if not output["generation"][0]:
                    continue
                temp_script = os.path.join(temp_dir, "test_temp.py")
                if output["generation"][0]:
                    with open(temp_script,"w") as f:
                        f.write(output["prompt"] + "\n" + output["generation"][0] + "\n\n" + output["test"])
                else:
                    with open(temp_script,"w") as f:
                        f.write(output["raw_generation"][0] + "\n\n" + output["test"])
                # Run the script and capture the output
                try:
                    result = subprocess.run(["pytest", temp_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=50)
                    # Output and error messages
                    error_message = result.stdout
                    if result.returncode == 0:
                        pass_count += 1
                        task_record[output["task_id"]] = True
                    else:
                        fp.write(output["prompt"] + "\n" + output["generation"][0] + "\n\n" + output["test"])
                        fp.write("\n\n"+error_message+"\n\n##################################################\n\n")
                        task_record[output["task_id"]] = False
                except:
                    fp.write(output["prompt"] + "\n" + output["generation"][0] + "\n\n" + output["test"])
                    fp.write("\n\n\"\"\"\n\n"+"TIMEOUT"+"\n\n\"\"\"\n\n##################################################\n\n")
                    task_record[output["task_id"]] = False

    jsonl_file_name = jsonl_file.split("/")[-1]
    with open(f"{original_dir}/results/record_{jsonl_file_name}","w") as f:
        json.dump(task_record, f)
    print("Pass rate:", pass_count / len(outputs))
        