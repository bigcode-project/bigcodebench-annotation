from datetime import datetime
import os
from pathlib import Path

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def f_954(file_path):
    """
    Determine the creation time of a file and convert it to a formatted string '% Y-% m-% d% H:% M:% S'.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    str: The creation time of the file in the format '%Y-%m-%d %H:%M:%S'.
    
    Requirements:
    - datetime
    - os
    - pathlib.Path
    
    Example:
    
    Example:
    >>> f_954('/path/to/file.txt')
    '2023-09-28 12:30:45'
    
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"No such file or directory: '{file_path}'")

    creation_time = os.path.getctime(file_path)
    formatted_time = datetime.fromtimestamp(creation_time).strftime(DATE_FORMAT)
    
    return formatted_time

import unittest
from datetime import datetime
import os
from pathlib import Path

def create_dummy_file(filename):
    """Creates a dummy file and returns its creation time."""
    with open(filename, 'w') as f:
        f.write("This is a dummy file.")
    return os.path.getctime(filename)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def setUp(self):
        """Setup function to create dummy files for testing."""
        self.file1 = "dummy1.txt"
        self.file2 = "dummy2.txt"
        self.file3 = "dummy3.txt"
        self.creation_time1 = create_dummy_file(self.file1)
        self.creation_time2 = create_dummy_file(self.file2)
        self.creation_time3 = create_dummy_file(self.file3)
    
    def tearDown(self):
        """Cleanup function to remove dummy files after testing."""
        os.remove(self.file1)
        os.remove(self.file2)
        os.remove(self.file3)

    def test_case_1(self):
        expected_output = datetime.fromtimestamp(self.creation_time1).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(f_954(self.file1), expected_output)
        
    def test_case_2(self):
        expected_output = datetime.fromtimestamp(self.creation_time2).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(f_954(self.file2), expected_output)
        
    def test_case_3(self):
        expected_output = datetime.fromtimestamp(self.creation_time3).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(f_954(self.file3), expected_output)
        
    def test_case_4(self):
        # Test for non-existing file
        with self.assertRaises(FileNotFoundError):
            f_954("non_existing_file.txt")
    
    def test_case_5(self):
        # Test for a directory
        os.mkdir("test_dir")
        dir_creation_time = os.path.getctime("test_dir")
        expected_output = datetime.fromtimestamp(dir_creation_time).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(f_954("test_dir"), expected_output)
        os.rmdir("test_dir")
if __name__ == "__main__":
    run_tests()