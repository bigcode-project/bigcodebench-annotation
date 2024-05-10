import os
import re

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    """
    Renames all files in a directory that match a particular pattern with a given replacement string.
    
    Parameters:
        - pattern (str): The pattern to search for in the filenames.
        - replacement (str): The string to replace the pattern with.
        - directory (str): The directory in which to search for files.
        
    Returns:
    - Returns a boolean value. True if the operation was successful, otherwise False.
    
    Requirements:
    - re
    - os

    Examples:
    >>> task_func('draft', 'final', '/home/user/documents')
    True
    >>> task_func('tmp', 'temp', '/home/user/downloads')
    False
    """
    try:
        for file in os.listdir(directory):
            if re.search(pattern, file):
                new_filename = re.sub(pattern, replacement, file)
                os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))
        return True
    except Exception as e:
        return False

import unittest
import tempfile
import shutil
from pathlib import Path
class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def create_test_files(self, filenames):
        for filename in filenames:
            Path(f"{self.test_dir}/{filename}").touch()
    
    def test_renafiles(self):
        self.create_test_files(["draft1.txt", "draft2.txt", "draft3.txt"])
        result = task_func("draft", "final", self.test_dir)
        self.assertTrue(result)
        expected_files = sorted(["final1.txt", "final2.txt", "final3.txt"])
        actual_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(expected_files, actual_files)
        
    def test_no_matching_files(self):
        self.create_test_files(["file1.txt", "file2.txt", "file3.txt"])
        result = task_func("draft", "final", self.test_dir)
        self.assertTrue(result)
        expected_files = sorted(["file1.txt", "file2.txt", "file3.txt"])
        actual_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(expected_files, actual_files)
        
    def test_nonexistent_directory(self):
        result = task_func("draft", "final", "/nonexistent/directory")
        self.assertFalse(result)
        
    def test_empty_directory(self):
        result = task_func("draft", "final", self.test_dir)
        self.assertTrue(result)
        self.assertEqual([], os.listdir(self.test_dir))
        
    def test_complex_pattern_renaming(self):
        self.create_test_files(["draft_file1.txt", "file_draft2.txt", "draft3file.txt"])
        result = task_func("draft", "final", self.test_dir)
        self.assertTrue(result)
        expected_files = sorted(["final_file1.txt", "file_final2.txt", "final3file.txt"])
        actual_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(expected_files, actual_files)
