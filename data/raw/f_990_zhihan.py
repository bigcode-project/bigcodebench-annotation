import os
import hashlib
import json
from pathlib import Path

def f_990(directory: str) -> str:
    """
    Create SHA256 hashes for all files in the given directory and save the hashes in a JSON file.
    
    Parameters:
    - directory (str): The path to the directory containing files to be hashed.
    
    Returns:
    str: The path of the JSON file containing the hashes.
    
    Requirements:
    - os
    - hashlib
    - json
    - pathlib.Path
    
    Example:
    >>> json_file = f_990("/path/to/directory")
    >>> print(f"Hashes saved at: {json_file}")
    """
    hash_dict = {}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            with open(file_path, 'rb') as f:
                bytes = f.read()  # read entire file as bytes
                readable_hash = hashlib.sha256(bytes).hexdigest()
                hash_dict[str(file_path)] = readable_hash
                
    # Save to JSON file
    json_file = Path(directory) / 'hashes.json'
    with open(json_file, 'w') as f:
        json.dump(hash_dict, f)
        
    return str(json_file)

import unittest
import os
import json
import hashlib
from pathlib import Path

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def setUp(self):
        # Creating a temporary directory for testing
        self.test_dir = "/mnt/data/tmp_test_dir"
        Path(self.test_dir).mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        # Cleaning up the temporary directory
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_case_1(self):
        # Testing with an empty directory
        json_file = f_990(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {})

    def test_case_2(self):
        # Testing with a directory containing a single file
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write("Hello, world!")
        json_file = f_990(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertIn('file1.txt', data.keys())

    def test_case_3(self):
        # Testing with a directory containing multiple files
        files_content = {
            'file2.txt': "Hello again!",
            'file3.txt': "Goodbye!"
        }
        for filename, content in files_content.items():
            with open(os.path.join(self.test_dir, filename), 'w') as f:
                f.write(content)
        json_file = f_990(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            for filename in files_content.keys():
                self.assertIn(filename, data.keys())

    def test_case_4(self):
        # Testing with a directory containing nested subdirectories and files
        sub_dir = os.path.join(self.test_dir, 'sub_dir')
        Path(sub_dir).mkdir(parents=True, exist_ok=True)
        with open(os.path.join(sub_dir, 'file4.txt'), 'w') as f:
            f.write("Nested file content!")
        json_file = f_990(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertIn('sub_dir/file4.txt', data.keys())

    def test_case_5(self):
        # Testing if the computed hash is correct
        with open(os.path.join(self.test_dir, 'file5.txt'), 'w') as f:
            f.write("Check hash!")
        json_file = f_990(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(os.path.join(self.test_dir, 'file5.txt'), 'rb') as f:
            bytes = f.read()
            expected_hash = hashlib.sha256(bytes).hexdigest()
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data['file5.txt'], expected_hash)
if __name__ == "__main__":
    run_tests()