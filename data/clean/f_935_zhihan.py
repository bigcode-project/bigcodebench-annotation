import ast
import os
import glob

# Constants
DIRECTORY = 'data'

def f_935(directory):
    """
    Convert all Unicode string representations of dictionaries in all text files 
    in the specified directory to Python dictionaries.

    Parameters:
    directory (str): The path to the directory containing the text files.

    Returns:
    list: A list of dictionaries extracted from the text files.

    Requirements:
    - ast
    - os
    - glob

    Example:
    >>> f_935("sample_directory/")
    [{'key1': 'value1'}, {'key2': 'value2'}]

    Note:
    Ensure that the text files in the directory contain valid Unicode string representations of dictionaries.

    Raises:
    - The function would raise a ValueError if there are text file(s) that have invalid dictionary representation
    """
    path = os.path.join(directory, '*.txt')
    files = glob.glob(path)

    results = []
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                results.append(ast.literal_eval(line.strip()))

    return results

import unittest
import os
import ast
import shutil


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'testdir_f_935/'
        os.makedirs(self.test_dir, exist_ok=True)
        self.sample_directory = 'testdir_f_935/sample_directory'
        os.makedirs(self.sample_directory, exist_ok=True)
        f = open(self.sample_directory+"/1.txt","w")
        f.write("{'key1': 'value1'}")
        f.close()
        f = open(self.sample_directory+"/2.txt","w")
        f.write("{'key2': 'value2', 'key3': 'value3'}")
        f.close()
        f = open(self.sample_directory+"/3.txt","w")
        f.write("{'key4': 'value4'}")
        f.close()
        f = open(self.sample_directory+"/4.txt","w")
        f.write("{'key5': 'value5', 'key6': 'value6', 'key7': 'value7'}")
        f.close()
        f = open(self.sample_directory+"/5.txt","w")
        f.write("{'key8': 'value8'}")
        f.close()
        self.empty_directory = "testdir_f_935/empty_directory"
        os.makedirs(self.empty_directory, exist_ok=True)
        self.multi_line_directory = "testdir_f_935/multi_line_directory"
        os.makedirs(self.multi_line_directory, exist_ok=True)
        f = open(self.multi_line_directory+"/1.txt","w")
        f.write("{'key1': 'value1'}\n{'key2': 'value2'}")
        f.close()
        self.mixed_directory = "testdir_f_935/mixed_directory"
        os.makedirs(self.mixed_directory, exist_ok=True)
        f = open(self.mixed_directory+"/1.txt","w")
        f.write("invalid")
        f.close()
        self.invalid_directory = "testdir_f_935/invalid_directory"
        os.makedirs(self.invalid_directory, exist_ok=True)
        f = open(self.invalid_directory+"/1.txt","w")
        f.write("invalid")
        f.close()
        f = open(self.invalid_directory+"/2.txt","w")
        f.write("{'key1': 'value1'}")
        f.close()


    def tearDown(self):
        # Clean up the test directory
        shutil.rmtree(self.test_dir)

    def test_case_1(self):
        # Test with the sample directory
        result = f_935(self.sample_directory)
        expected_result = [
            {'key1': 'value1'},
            {'key2': 'value2', 'key3': 'value3'},
            {'key4': 'value4'},
            {'key5': 'value5', 'key6': 'value6', 'key7': 'value7'},
            {'key8': 'value8'}
        ]
        self.assertEqual(result, expected_result)
        
    def test_case_2(self):
        # Test with an empty directory
        result = f_935(self.empty_directory)
        self.assertEqual(result, [])
        
    def test_case_3(self):
        # Test with a directory containing a text file without valid dictionary representation
        with self.assertRaises(ValueError):
            f_935(self.invalid_directory)
            
    def test_case_4(self):
        # Test with a directory containing multiple text files, some of which are invalid
        with self.assertRaises(ValueError):
            f_935(self.mixed_directory)
            
    def test_case_5(self):
        # Test with a directory containing a text file with multiple valid dictionary representations
        result = f_935(self.multi_line_directory)
        expected_result = [
            {'key1': 'value1'},
            {'key2': 'value2'}
        ]
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    run_tests()