import os
import glob
import hashlib

def task_func(source_dir, target_dir, prefix='#Hash: '):
    """
    Computes the MD5 hash of each file's content in the specified `source_dir`, prepends the hash along with a prefix 
    to the original content, and writes the modified content to new files in the `target_dir`. 
    Existing files with the same name in `target_dir` are overwritten.

    Parameters:
    - source_dir (str): The directory containing the files to be processed. Must exist.
    - target_dir (str): The directory where the processed files will be written. Created if it does not exist.
    - prefix (str): The prefix to prepend before the hash in each new file. Default is '#Hash: '.

    Returns:
    - list: A list of paths to the newly created files in the `target_dir`, each with the hash prepended.

    Requirements:
    - os
    - glob
    - hashlib

    Raises:
    FileNotFoundError if the source directory does not exist.

    Example:
    >>> task_func(source_dir='samples', target_dir='hashed_samples', prefix='#MD5: ')
    ['hashed_samples/file1.txt', 'hashed_samples/file2.txt']
    """

    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    new_files = []
    for file_path in glob.glob(os.path.join(source_dir, '*')):
        with open(file_path, 'r') as infile:
            content = infile.read()
        hash_object = hashlib.md5(content.encode())
        new_file_path = os.path.join(target_dir, os.path.basename(file_path))
        with open(new_file_path, 'w') as outfile:
            outfile.write(f"{prefix}{hash_object.hexdigest()}\n{content}")
        new_files.append(new_file_path)
    return new_files

import unittest
import os
import shutil
import tempfile
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create temporary directories for source and target
        self.source_dir = tempfile.mkdtemp()
        self.target_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Clean up the directories after tests
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.target_dir)
    def test_default_directories_and_prefix(self):
        # Create some sample files in source_dir
        sample_files = ['file1.txt', 'file2.txt', 'file3.txt']
        for file_name in sample_files:
            with open(os.path.join(self.source_dir, file_name), 'w') as f:
                f.write("Sample content for " + file_name)
        
        result = task_func(source_dir=self.source_dir, target_dir=self.target_dir)
        expected_files = [os.path.join(self.target_dir, file_name) for file_name in sample_files]
        self.assertListEqual(sorted(result), sorted(expected_files))
        for file in expected_files:
            with open(file, 'r') as f:
                lines = f.readlines()
                self.assertTrue(lines[0].startswith('#Hash: '))
                self.assertIn("Sample content for", ''.join(lines[1:]))
    def test_custom_prefix(self):
        # Testing with a custom prefix
        custom_prefix = "MD5Hash: "
        with open(os.path.join(self.source_dir, "file.txt"), 'w') as f:
            f.write("Sample content")
        
        result = task_func(source_dir=self.source_dir, target_dir=self.target_dir, prefix=custom_prefix)
        for file in result:
            with open(file, 'r') as f:
                lines = f.readlines()
                self.assertTrue(lines[0].startswith(custom_prefix))
    def test_empty_directory(self):
        # Testing with an empty source directory
        result = task_func(source_dir=self.source_dir, target_dir=self.target_dir)
        self.assertEqual(result, [])
    def test_non_existing_source_directory(self):
        # Using a non-existing source directory should raise FileNotFoundError
        non_existing_dir = "/path/to/nonexistent/dir"
        with self.assertRaises(FileNotFoundError):
            task_func(source_dir=non_existing_dir, target_dir=self.target_dir)
    def test_overwriting_existing_files(self):
        # Overwriting existing files in the target directory
        file_path = os.path.join(self.target_dir, "file1.txt")
        with open(file_path, 'w') as f:
            f.write("Initial content.")
        
        with open(os.path.join(self.source_dir, "file1.txt"), 'w') as f:
            f.write("New content.")
        
        task_func(source_dir=self.source_dir, target_dir=self.target_dir)
        with open(file_path, 'r') as f:
            self.assertNotEqual(f.read(), "Initial content.")
