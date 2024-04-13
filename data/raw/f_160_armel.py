import re
import os
import json


# Constants
PATTERN = r'\b\d{4}\b'

def f_160(dir_path):
    """
    Extract 4-digit numbers (assumed years) from all text files within a directory and its subdirectories. Results are saved in a JSON file in the same directory.
    - Make use of the regex PATTERN.
    - The output json file should be named "extracted_years".
        - It should be form from a directory which keys are the relative path to each file in the directory and its subdirectories.
        - The value associated to a key is the list of 4-digit numbers found it the corresponding file.
    
    Parameters:
    dir_path (str): The path of the directory.
    
    Returns:
    str: The path of the JSON file with the results.
    
    Requirements:
    - re
    - os
    - json
        
    Example:
    >>> f_160("/path/to/directory")
    "/path/to/directory/extracted_years.json"

    The JSON file will have a structure similar to:
    {
        "file1.txt": ["2023", "1998"],
        "file2.txt": ["2022", "2050", "2100"],
        "sub_dir/file3.txt": ["2077"]
    }
    """
    result = {}
    file_paths = [os.path.join(root, file) for root, _, files in os.walk(dir_path) for file in files if file.endswith('.txt')]

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
        matches = re.findall(PATTERN, content)
        if matches:
            result[os.path.relpath(file_path, dir_path)] = matches

    output_path = os.path.join(dir_path, 'extracted_years.json')
    with open(output_path, 'w') as output_file:
        json.dump(result, output_file, indent=4)

    return output_path

import unittest
import os
import json
import re

class TestCases(unittest.TestCase):
    """Test cases for the f_160 function."""
    def setUp(self):
        self.test_dir = "data/f_160"
        os.makedirs(self.test_dir, exist_ok=True)

        self.d_1 = os.path.join(self.test_dir, "dir_1")
        os.makedirs(self.d_1, exist_ok=True)
        
        with open(os.path.join(self.d_1, "txt_1.txt"), "w") as f :
            f.write("The WWII started in 1939 and ended in 1945")
        
        self.d_2 = os.path.join(self.test_dir, "dir_2")
        os.makedirs(self.d_2, exist_ok=True)
        with open(os.path.join(self.d_2, "txt_1.txt"), "w") as f :
            f.write("Alice was born in 2008. In 2013, she was 5. She died in 2021.") 
        with open(os.path.join(self.d_2, "txt_2.txt"), "w") as f :
            f.write("Bob will graduate in 2015.")    
        with open(os.path.join(self.d_2, "txt_2.txt"), "w") as f :
            f.write("Arthur went to Germany in 1980 and came back in 1999.") 

        self.d_3 = os.path.join(self.test_dir, "dir_3")
        os.makedirs(self.d_3, exist_ok=True)
        with open(os.path.join(self.d_3, "txt_1.txt"), "w") as f :
            f.write("I was born in 2003.") 

        self.d_4 = os.path.join(self.test_dir, "dir_4")
        os.makedirs(self.d_4, exist_ok=True)
        with open(os.path.join(self.d_4, "txt_1.txt"), "w") as f :
            f.write("I was born in 2007.") 

        self.d_5 = os.path.join(self.test_dir, "dir_5")
        os.makedirs(self.d_5, exist_ok=True)

        self.d_6 = os.path.join(self.test_dir, "dir_6")
        os.makedirs(self.d_6, exist_ok=True)
        with open(os.path.join(self.d_6, "txt_1.txt"), "w") as f :
            f.write("A1 was born in 2007.")
        with open(os.path.join(self.d_6, "txt_2.txt"), "w") as f :
            f.write("A2 was born in 2009.")
        os.makedirs(os.path.join(self.d_6, "dir_6_1"))
        with open(os.path.join(self.d_6, "dir_6_1/txt_1.txt"), "w") as f :
            f.write("B1 was born in 2007. He was 5 in 2012.")
        with open(os.path.join(self.d_6, "dir_6_1/txt_2.txt"), "w") as f :
            f.write("B2 was born in 1745. He died in 1800.")
        os.makedirs(os.path.join(self.d_6, "dir_6_2"))
        with open(os.path.join(self.d_6, "dir_6_2/txt_1.txt"), "w") as f :
            f.write("B4 went to Spain in 1933.")
    
    def tearDown(self):
        import shutil
        try:
            shutil.rmtree(self.test_dir)
        except OSError as e:
            print(e)
        
    def test_case_1(self):
        self.helper_test_extracted_years(self.d_1)
    
    def test_case_2(self):
        self.helper_test_extracted_years(self.d_2)
        
    def test_case_3(self):
        self.helper_test_extracted_years(self.d_3)
        
    def test_case_4(self):
        self.helper_test_extracted_years(self.d_4)
    
    def test_case_5(self):
        self.helper_test_extracted_years(self.d_5)

    def test_case_6(self):
        output_path = f_160(self.d_6)
        with open(output_path, 'r') as json_file:
            data = json.load(json_file)
        self.assertDictEqual(
            data,
            {
                'txt_2.txt': ['2009'], 
                'txt_1.txt': ['2007'], 
                'dir_6_2/txt_1.txt': ['1933'], 
                'dir_6_1/txt_2.txt': ['1745', '1800'], 
                'dir_6_1/txt_1.txt': ['2007', '2012']
            }
        )
        
    def helper_test_extracted_years(self, test_dir):
        '''Helper function to test extracted years from the text files.'''
        output_path = f_160(test_dir)
        
        # Check if the output file exists
        self.assertTrue(output_path.endswith("extracted_years.json"))
        self.assertTrue(os.path.exists(output_path), 'Output JSON file does not exist.')
        
        # Read the JSON file and check its content
        with open(output_path, 'r') as json_file:
            data = json.load(json_file)
        
        for file, years in data.items():
            # Check if the extracted years are actually 4-digit numbers
            self.assertTrue(all([re.match(PATTERN, year) for year in years]), f'Invalid year detected in {file}.')


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()    