import os
import hashlib
import json
from pathlib import Path

def f_994(directory: str) -> str:
    """
    Create SHA256 hashes for all files in the specified directory, including files in subdirectories, 
    and save these hashes in a JSON file named 'hashes.json' in the given directory.

    Parameters:
    - directory (str): The path to the directory containing files to be hashed.
    
    Returns:
    str: The absolute path of the JSON file ('hashes.json') containing the hashes.
    
    Requirements:
    - os
    - hashlib
    - json
    - pathlib.Path

    Example:
    >>> json_file = f_994("/path/to/directory")
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
    json_file = Path(directory) / 'hashes.json'
    with open(json_file, 'w') as f:
        json.dump(hash_dict, f)
    return str(json_file)

import unittest
import os
import hashlib
import json
from pathlib import Path
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Creating a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Cleaning up the temporary directory
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)
    def test_empty_directory(self):
        # Testing with an empty directory
        json_file = f_994(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {})
    def test_single_file(self):
        # Testing with a directory containing a single file
        filepath = os.path.join(self.test_dir, 'file1.txt')
        with open(filepath, 'w') as f:
            f.write("Hello, world!")
        json_file = f_994(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertIn(filepath, data.keys())
    def test_multiple_files(self):
        # Testing with a directory containing multiple files
        files_content = {'file2.txt': "Hello again!", 'file3.txt': "Goodbye!"}
        filepaths = {}
        for filename, content in files_content.items():
            filepath = os.path.join(self.test_dir, filename)
            filepaths[filepath] = content
            with open(filepath, 'w') as f:
                f.write(content)
        json_file = f_994(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            for filepath in filepaths.keys():
                self.assertIn(filepath, data.keys())
    def test_nested_directories(self):
        # Testing with a directory containing nested subdirectories and files
        sub_dir = os.path.join(self.test_dir, 'sub_dir')
        filepath = os.path.join(sub_dir, 'file4.txt')
        Path(sub_dir).mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            f.write("Nested file content!")
        json_file = f_994(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertIn(filepath, data.keys())
    def test_correct_hash(self):
        # Testing if the computed hash is correct
        filepath = os.path.join(self.test_dir, 'file5.txt')
        with open(filepath, 'w') as f:
            f.write("Check hash!")
        json_file = f_994(self.test_dir)
        self.assertTrue(os.path.exists(json_file))
        with open(filepath, 'rb') as f:
            bytes = f.read()
            expected_hash = hashlib.sha256(bytes).hexdigest()
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(data[filepath], expected_hash)
