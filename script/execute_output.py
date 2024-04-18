import subprocess
import jsonlines
from tqdm import tqdm
import sys
import os
import termcolor

if __name__ == '__main__':
    jsonl_file = sys.argv[1]
    outputs = []
    ref_ids = []
    with jsonlines.open(jsonl_file) as f:
        for s in f:
            outputs.append(s)
    pass_count = 0
    count = 0
    with open(f"{jsonl_file.replace('.jsonl', '.py')}","w") as fp:
        for output in tqdm(outputs):
            if output["generation"][0]:
                with open("test.py","w") as f:
                    f.write(output["prompt"] + "\n" + output["generation"][0] + "\n\n" + output["test"])
            else:
                with open("test.py","w") as f:
                    f.write(output["raw_generation"][0] + "\n\n" + output["test"])
            # Run the script and capture the output
            try:
                result = subprocess.run(["pytest", "test.py"], capture_output=True, text=True, timeout=50)
                # Output and error messages
                error_message = result.stdout
                if "failed" not in error_message:
                    pass_count += 1
                else:
                    fp.write(output["prompt"] + "\n" + output["generation"][0] + "\n\n" + output["test"])
                    fp.write("\n\n"+error_message+"\n\n##################################################\n\n")
            except:
                fp.write(output["prompt"] + "\n" + output["generation"][0] + "\n\n" + output["test"])
                fp.write("\n\n\"\"\"\n\n"+"TIMEOUT"+"\n\n\"\"\"\n\n##################################################\n\n")
            count+=1
    # remove test.py
    os.remove("test.py")
    print("Pass rate:", pass_count / count)
        