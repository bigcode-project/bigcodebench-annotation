import sys
import json
import subprocess
from tqdm import tqdm
from numpy import mean, median
from matplotlib import pyplot as plt
def get_pypi_stats(package_name):
    """
    Function to get PyPI download stats for a given package using pypinfo.
    """
    try:
        # Constructing the command to call pypinfo
        command = f"pypinfo --json {package_name}"
        
        # Running the command and capturing the output
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Print the output
        print(result.stdout)
        parsed_result = json.loads(result.stdout)

        return parsed_result["rows"][0]["download_count"]
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}", file=sys.stderr)
        return None

if __name__ == "__main__":
    with open("analysis/lib2domain.json") as f:
        lib2domain = json.load(f)
    
    with open("analysis/standard_lib.json") as f:
        standard_lib = json.load(f)

    with open("analysis/used_std_libs.json","w") as f:
        libs = []
        for lib in lib2domain.keys():
            if lib in standard_lib:
                libs.append(lib)
        json.dump(libs,f,indent=4)
    # with open("analysis/3rd_party_libs.json","w") as f:
    #     libs = []
    #     for lib in lib2domain.keys():
    #         if lib not in standard_lib:
    #             libs.append(lib)
    #     json.dump(libs,f,indent=4)
    
    # with open("analysis/3rd_party_libs.json") as f:
    #     libs = json.load(f)

    # download_stats = {}
    # for lib in tqdm(list(libs.values())[:]):
    #     print(f"Getting download stats for {lib}")
    #     download_stats[lib] = get_pypi_stats(lib)
    #     sorted_download_stats = dict(sorted(download_stats.items(), key=lambda x: x[1], reverse=True))
        
    # with open("analysis/download_stats.json", "w") as f:
    #     json.dump(sorted_download_stats, f, indent=4)
        
    with open("analysis/download_stats.json") as f:
        download_stats = json.load(f)
        # get mean and median download stats
        print(f"Mean download stats: {mean(list(download_stats.values()))}")
        print(f"Median download stats: {median(list(download_stats.values()))}")
        # plot the download stats with curve fitting
        plt.hist(list(download_stats.values()), bins=50, color='blue', edgecolor='black')
        plt.xlabel("Download Stats")
        plt.ylabel("Frequency")
        plt.title("Distribution of Download Stats")
        plt.savefig("analysis/download_stats.png")
        
        
    
