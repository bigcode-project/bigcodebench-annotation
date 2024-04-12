import os
import shutil
import string

# Constants
INVALID_CHARACTERS = string.punctuation + string.whitespace

def f_700(directory_path):
    """
    Scan a directory and organize the files according to their endings. Files with invalid characters in the name will be moved to a new directory called "Invalid."
    
    The invalid characters are defined by the constant INVALID_CHARACTERS, which includes all punctuation and whitespace characters.

    Parameters:
    - directory_path (str): The path to the directory.

    Returns:
    - summary (dict): A summary dictionary containing the count of files moved to each directory.

    Requirements:
    - os
    - shutil
    - string

    Example:
    >>> f_700('path_to_directory')
    {'txt': 2, 'jpg': 1, 'Invalid': 1}
    """
    summary = {}
    for filename in os.listdir(directory_path):
        if any(char in INVALID_CHARACTERS for char in filename):
            if not os.path.exists(os.path.join(directory_path, 'Invalid')):
                os.mkdir(os.path.join(directory_path, 'Invalid'))
            shutil.move(os.path.join(directory_path, filename), os.path.join(directory_path, 'Invalid'))
            summary['Invalid'] = summary.get('Invalid', 0) + 1
        else:
            extension = os.path.splitext(filename)[-1].strip('.')
            if not os.path.exists(os.path.join(directory_path, extension)):
                os.mkdir(os.path.join(directory_path, extension))
            shutil.move(os.path.join(directory_path, filename), os.path.join(directory_path, extension))
            summary[extension] = summary.get(extension, 0) + 1
    return summary

import unittest
import os
import shutil

class TestCases(unittest.TestCase):
    def setUp(self):
        # Create test directories and files
        self.test_dir_1 = '/mnt/data/test_dir_1'
        self.test_dir_2 = '/mnt/data/test_dir_2'
        self.empty_dir = '/mnt/data/empty_dir'
        os.mkdir(self.empty_dir)

    def tearDown(self):
        # Delete test directories
        shutil.rmtree(self.test_dir_1)
        shutil.rmtree(self.test_dir_2)
        shutil.rmtree(self.empty_dir)

    def test_basic_functionality(self):
        # Test basic functionality
        summary_1 = f_700(self.test_dir_1)
        summary_2 = f_700(self.test_dir_2)
        
        # Check if the summary dictionary is accurate
        self.assertEqual(summary_1, {'pdf': 1, 'csv': 1, 'jpg': 3, 'Invalid': 1})
        self.assertEqual(summary_2, {'png': 2, 'txt': 2, 'csv': 1, 'Invalid': 1})

    def test_empty_directory(self):
        # Test empty directory
        summary = f_700(self.empty_dir)
        
        # Check if the summary dictionary is empty
        self.assertEqual(summary, {})
        
    def test_invalid_path(self):
        # Test with an invalid directory path
        with self.assertRaises(FileNotFoundError):
            f_700('invalid_path')

    def test_summary_content(self):
        # Test the summary content details
        summary = f_700(self.test_dir_1)
        
        # Check if the summary contains keys for all unique extensions and "Invalid"
        self.assertTrue(all(key in ['pdf', 'csv', 'jpg', 'Invalid'] for key in summary.keys()))
        
    def test_file_moves(self):
        # Test if the files are actually moved to the correct folders
        f_700(self.test_dir_1)
        
        # Check if the 'Invalid' directory exists and contains the correct number of files
        self.assertTrue(os.path.exists(os.path.join(self.test_dir_1, 'Invalid')))
        self.assertEqual(len(os.listdir(os.path.join(self.test_dir_1, 'Invalid'))), 1)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
    run_tests()