import os
import re

def f_749(pattern: str, replacement: str, directory: str) -> bool:
    """
    Renames all files in a directory that match a particular pattern with a given replacement string.
    
    Functionality:
        - Searches for files in the specified directory whose names contain the given pattern.
        - Renames those files by replacing the pattern with the given replacement string.
    
    Input:
        - pattern (str): The pattern to search for in the filenames.
        - replacement (str): The string to replace the pattern with.
        - directory (str): The directory in which to search for files.
        
    Output:
    - Returns a boolean value. True if the operation was successful, otherwise False.
    
    Requirements:
    - re
    - os

    Examples:
    >>> f_749('draft', 'final', '/home/user/documents')
    True
    >>> f_749('tmp', 'temp', '/home/user/downloads')
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
    
    def test_renaming_files(self):
        self.create_test_files(["draft1.txt", "draft2.txt", "draft3.txt"])
        result = f_749("draft", "final", self.test_dir)
        self.assertTrue(result)
        expected_files = sorted(["final1.txt", "final2.txt", "final3.txt"])
        actual_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(expected_files, actual_files)
        
    def test_no_matching_files(self):
        self.create_test_files(["file1.txt", "file2.txt", "file3.txt"])
        result = f_749("draft", "final", self.test_dir)
        self.assertTrue(result)
        expected_files = sorted(["file1.txt", "file2.txt", "file3.txt"])
        actual_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(expected_files, actual_files)
        
    def test_nonexistent_directory(self):
        result = f_749("draft", "final", "/nonexistent/directory")
        self.assertFalse(result)
        
    def test_empty_directory(self):
        result = f_749("draft", "final", self.test_dir)
        self.assertTrue(result)
        self.assertEqual([], os.listdir(self.test_dir))
        
    def test_complex_pattern_renaming(self):
        self.create_test_files(["draft_file1.txt", "file_draft2.txt", "draft3file.txt"])
        result = f_749("draft", "final", self.test_dir)
        self.assertTrue(result)
        expected_files = sorted(["final_file1.txt", "file_final2.txt", "final3file.txt"])
        actual_files = sorted(os.listdir(self.test_dir))
        self.assertEqual(expected_files, actual_files)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    run_tests()
