import re
from pathlib import Path
import shutil
import tarfile

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"

def f_679():
    """
    Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, archive these files in a tar file.

    Parameters:
    - None

    Returns:
    - str: Path to the created tar file.

    Requirements:
    - re
    - pathlib
    - shutil
    - tarfile

    Example:
    >>> f_679()
    """
    tar_path = Path(DIRECTORY) / 'archive.tar'
    with tarfile.open(tar_path, 'w') as tar:
        for path in Path(DIRECTORY).rglob('*'):
            if re.search(PATTERN, str(path)):
                tar.add(path)
    return str(tar_path)

import unittest
import tempfile
import os
import tarfile
from pathlib import Path

class TestCases(unittest.TestCase):
    def setUp(self):
        # Creating a temporary directory to store test files
        self.test_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.test_dir.cleanup)  # Ensure cleanup
    
    def create_test_files(self, files):
        """
        Helper function to create test files in the temporary directory.
        """
        for file_name, content in files.items():
            with open(os.path.join(self.test_dir.name, file_name), 'w') as f:
                f.write(content)
    
    def test_case_1(self):
        """
        Test Case 1: Archive files that match a simple pattern in a directory without subdirectories.
        - Files 'test1.txt' and 'test2.txt' should be archived as they match the pattern 'test\d\.txt'.
        - File 'sample.txt' should not be archived as it does not match the pattern.
        """
        files = {
            'test1.txt': 'Hello World',
            'test2.txt': 'Python is great',
            'sample.txt': 'This is a sample file'
        }
        self.create_test_files(files)
        
        # Run the function
        pattern = r'test\d\.txt'
        tar_file = f_679(self.test_dir.name, pattern)
        
        # Check that the tar file contains the correct files
        with tarfile.open(tar_file, 'r') as tar:
            self.assertEqual(sorted(tar.getnames()), sorted(['test1.txt', 'test2.txt']))
    
    def test_case_2(self):
        """
        Test Case 2: Archive files that match a pattern with special characters in a directory without subdirectories.
        - Files 'test_1.txt', 'test_2.txt', and 'test-3.txt' should all be archived as they match the pattern 'test[\-_]\d\.txt'.
        """
        files = {
            'test_1.txt': 'Hello World',
            'test_2.txt': 'Python is great',
            'test-3.txt': 'This is a test file'
        }
        self.create_test_files(files)
        
        # Run the function
        pattern = r'test[\-_]\d\.txt'
        tar_file = f_679(self.test_dir.name, pattern)
        
        # Check that the tar file contains the correct files
        with tarfile.open(tar_file, 'r') as tar:
            self.assertEqual(sorted(tar.getnames()), sorted(['test_1.txt', 'test_2.txt', 'test-3.txt']))
    
    def test_case_3(self):
        """
        Test Case 3: Archive files from subdirectories.
        - All files 'test1.txt', 'test2.txt', and 'test3.txt' should be archived as they match the pattern 'test\d\.txt'.
        - The files should be archived with their relative paths from the search directory.
        """
        files = {
            'subdir/test1.txt': 'File in subdir',
            'subdir/test2.txt': 'Another file in subdir',
            'test3.txt': 'File in root dir'
        }
        for file_name in files:
            file_path = os.path.join(self.test_dir.name, file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(files[file_name])
        
        # Run the function
        pattern = r'test\d\.txt'
        tar_file = f_679(self.test_dir.name, pattern)
        
        # Check that the tar file contains the correct files
        with tarfile.open(tar_file, 'r') as tar:
            self.assertEqual(sorted(tar.getnames()), sorted(['subdir/test1.txt', 'subdir/test2.txt', 'test3.txt']))
    
    def test_case_4(self):
        """
        Test Case 4: No files match the pattern.
        - There are two files 'file1.txt' and 'file2.txt' in the directory, but neither matches the pattern 'nonmatchingpattern'.
        - The tar file should be empty.
        """
        files = {
            'file1.txt': 'Hello World',
            'file2.txt': 'Python is great'
        }
        self.create_test_files(files)
        
        # Run the function
        pattern = r'nonmatchingpattern'
        tar_file = f_679(self.test_dir.name, pattern)
        
        # Check that the tar file contains no files
        with tarfile.open(tar_file, 'r') as tar:
            self.assertEqual(tar.getnames(), [])
    
    def test_case_5(self):
        """
        Test Case 5: Directory does not exist.
        - Attempting to run the function with a non-existing directory should raise a FileNotFoundError.
        """
        # Run the function with a non-existing directory
        pattern = r'.*'
        with self.assertRaises(FileNotFoundError):
            f_679('/non/existing/directory', pattern)

# Defining the run_tests function
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()