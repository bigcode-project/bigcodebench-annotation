import os
import hashlib
import re
import json

# Constants
FILE_EXTENSION = '.txt'
DIRECTORY = '/home/user/data/'

def f_979(directory_path=DIRECTORY):
    '''
    Generates checksums for all files with a specific extension (.txt by default) 
    in a given directory and stores them in a JSON file.
    
    Args:
    - directory_path (str): The path to the directory where the files are located. 
                            Default is '/home/user/data/'.
                            
    Returns:
    - dict: A dictionary where keys are filenames and values are their respective MD5 checksums.
    
    Requirements:
    - os
    - hashlib
    - re
    - json
    
    Example:
    >>> f_979("/path/to/directory")
    {{
        "file1.txt": "d41d8cd98f00b204e9800998ecf8427e",
        "file2.txt": "e99a18c428cb38d5f260853678922e03",
        ...
    }}
    '''
    checksums = {}

    for file in os.listdir(directory_path):
        if re.search(FILE_EXTENSION + '$', file):
            with open(os.path.join(directory_path, file), 'rb') as f:
                checksums[file] = hashlib.md5(f.read()).hexdigest()

    with open(os.path.join(directory_path, 'checksums.json'), 'w') as f:
        json.dump(checksums, f)

    return checksums
    

import unittest
import os
import re
import json
import hashlib

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # We'll skip this test since the default directory doesn't exist in this context
        pass
    
    def test_case_2(self):
        # Test with the temporary directory containing .txt files
        result = f_979(temp_dir)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 3)  # Expecting 3 txt files
        self.assertIn("file1.txt", result)
        self.assertIn("file2.txt", result)
        self.assertIn("file3.txt", result)
        self.assertNotIn("image.jpg", result)
        
        # Checking if checksums.json was created
        self.assertTrue(os.path.exists(os.path.join(temp_dir, 'checksums.json')))
        
        # Verifying the content of checksums.json
        with open(os.path.join(temp_dir, 'checksums.json'), 'r') as f:
            json_content = json.load(f)
            self.assertEqual(json_content, result)
    
    def test_case_3(self):
        # Test with an invalid directory path
        with self.assertRaises(FileNotFoundError):
            f_979("/invalid/path")
            
    def test_case_4(self):
        # Test with a directory that doesn't contain .txt files
        empty_dir = tempfile.mkdtemp()
        result = f_979(empty_dir)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 0)
        
    def test_case_5(self):
        # Test with a directory containing large .txt files
        large_dir = tempfile.mkdtemp()
        large_content = "A" * 10**6  # 1 MB of content
        with open(os.path.join(large_dir, "large_file.txt"), 'w') as f:
            f.write(large_content)
        
        result = f_979(large_dir)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 1)
        self.assertIn("large_file.txt", result)
if __name__ == "__main__":
    run_tests()