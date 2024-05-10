import os
import shutil
import string

# Constants
INVALID_CHARACTERS = string.punctuation + string.whitespace

def task_func(directory_path):
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
    >>> task_func('path_to_directory')
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
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_dir_1 = os.path.join(self.temp_dir, 'test_dir_1')
        self.empty_dir = os.path.join(self.temp_dir, 'empty_dir')
        os.mkdir(self.test_dir_1)
        os.mkdir(self.empty_dir)
        self.create_test_files(self.test_dir_1, ['test1.pdf', 'data.csv', 'image.jpg', 'invalid file name.jpg'])
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    def create_test_files(self, directory, filenames):
        for filename in filenames:
            path = os.path.join(directory, filename)
            with open(path, 'w') as f:
                f.write("Dummy content")
    def test_file_moves(self):
        task_func(self.test_dir_1)
        invalid_dir = os.path.join(self.test_dir_1, 'Invalid')
        self.assertTrue(os.path.exists(invalid_dir))
        self.assertEqual(len(os.listdir(invalid_dir)), 4)
    def test_empty_directory(self):
        summary = task_func(self.empty_dir)
        self.assertEqual(summary, {})
    def test_basic_functionality(self):
        # Test basic functionality
        summary = task_func(self.test_dir_1)
        expected = {'Invalid': 4}
        self.assertEqual(summary, expected)
        
    def test_invalid_path(self):
        # Test with an invalid directory path
        with self.assertRaises(FileNotFoundError):
            task_func('invalid_path')
    def test_summary_content(self):
        # Test the summary content details
        summary = task_func(self.test_dir_1)
        
        # Check if the summary contains keys for all unique extensions and "Invalid"
        self.assertTrue(all(key in ['pdf', 'csv', 'jpg', 'Invalid'] for key in summary.keys()))
