import os
import re

def f_671(directory):
    """
    Finds all files in the specified directory whose names contain any type of 
    bracket (round, curly, or square).

    Uses an internal constant BRACKET_PATTERN = '[(){}\\[\\]]', which specifies
    the brackets that are looked for.

    
    Parameters:
    directory (str): The directory path to search in.
    
    Returns:
    list[str]: A list of file paths that contain brackets in their names.
    
    Requirements:
    - re
    - os
    
    Example:
    >>> f_671('./some_directory/')
    ['./some_directory/file(1).txt', './some_directory/folder/file[2].jpg']
    
    >>> f_671('./another_directory/')
    ['./another_directory/file{3}.png']
    """
    BRACKET_PATTERN = '[(){}\\[\\]]'  # Corrected pattern to match any type of bracket
    
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(BRACKET_PATTERN, file):
                file_list.append(os.path.join(root, file))
    return file_list

import unittest
import os
from pathlib import Path
import shutil
class TestCases(unittest.TestCase):
    # Function to create the mock directory structure and files
    def create_test_files(self, base_path, file_dict):
        for name, content in file_dict.items():
            path = Path(base_path) / name
            if isinstance(content, dict):  # it's a directory
                path.mkdir()
                self.create_test_files(path, content)
            else:  # it's a file
                path.write_text(content)
    # Define a directory structure with files containing brackets and without brackets
    test_files = {
        'file1.txt': '',  # without brackets
        'file(2).txt': '',  # with round brackets
        'file[3].png': '',  # with square brackets
        'file{4}.jpg': '',  # with curly brackets
        'folder1': {
            'file(5).jpg': '',  # with round brackets
            'file6.csv': '',  # without brackets
            'folder2': {
                'file[7].csv': '',  # with square brackets
                'file{8}.png': ''  # with curly brackets
            }
        }
    }
# Create a temporary directory structure for testing
    temp_dir = ''
    def setUp(self):
        self.temp_dir = os.path.join(os.getcwd(), 'temp_test_dir')
        if not os.path.exists(self.temp_dir):
            os.mkdir(self.temp_dir)
        self.create_test_files(self.temp_dir, self.test_files)
    
    def test_case_1(self):
        # Test with the root directory
        result = f_671(self.temp_dir)
        self.assertIn(os.path.join(self.temp_dir, 'file(2).txt'), result)
        self.assertIn(os.path.join(self.temp_dir, 'file[3].png'), result)
        self.assertIn(os.path.join(self.temp_dir, 'file{4}.jpg'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'file(5).jpg'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file[7].csv'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file{8}.png'), result)
        self.assertEqual(len(result), 6)
        
    def test_case_2(self):
        # Test with a sub-directory
        result = f_671(os.path.join(self.temp_dir, 'folder1'))
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'file(5).jpg'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file[7].csv'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file{8}.png'), result)
        self.assertEqual(len(result), 3)
        
    def test_case_3(self):
        # Test with a deeper sub-directory
        result = f_671(os.path.join(self.temp_dir, 'folder1', 'folder2'))
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file[7].csv'), result)
        self.assertIn(os.path.join(self.temp_dir, 'folder1', 'folder2', 'file{8}.png'), result)
        self.assertEqual(len(result), 2)
    def test_case_4(self):
        # Test with an empty directory
        empty_dir = os.path.join(self.temp_dir, 'empty_folder')
        os.mkdir(empty_dir)
        result = f_671(empty_dir)
        self.assertEqual(result, [])
    def test_case_5(self):
        # Test with directory containing files without brackets
        no_bracket_dir = os.path.join(self.temp_dir, 'no_bracket_folder')
        os.mkdir(no_bracket_dir)
        open(os.path.join(no_bracket_dir, 'file9.txt'), 'w').close()
        open(os.path.join(no_bracket_dir, 'file10.jpg'), 'w').close()
        result = f_671(no_bracket_dir)
        self.assertEqual(result, [])
    def tearDown(self):
        shutil.rmtree('temp_test_dir')
