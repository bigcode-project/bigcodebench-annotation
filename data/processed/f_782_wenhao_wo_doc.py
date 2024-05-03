import re
import os
import glob

def f_438(dir_path: str) -> list:
    """
    Rename all files in the specified directory by removing all special characters,
    punctuation marks, and spaces, using regular expressions. The function keeps
    alphanumeric characters and removes the rest.

    Requirements:
    - re
    - os
    - glob

    Parameters:
    dir_path (str): The path to the directory containing the files to be renamed.

    Returns:
    list[str]: A list containing the new names of all files after rena.

    Example:
    >>> f_438('path/to/directory')
    ['file1', 'file2', 'file3']
    >>> f_438('another/directory/path')
    ['anotherFile1', 'anotherFile2']
    """
    new_names = []
    for file_path in glob.glob(os.path.join(dir_path, '*')):
        base_name = os.path.basename(file_path)
        new_name = re.sub('[^A-Za-z0-9]+', '', base_name)
        new_path = os.path.join(dir_path, new_name)
        os.rename(file_path, new_path)
        new_names.append(new_name)
    return new_names

import unittest
from pathlib import Path
import shutil
class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.temp_dir = Path("temp_test_dir")
        self.temp_dir.mkdir(parents=True, exist_ok=True)
    
    def tearDown(self):
        shutil.rmtree(self.temp_dir)
    
    def test_special_characters_removal(self):
        test_files = ["file@1.txt", "file_#2.txt", "file$ 3.txt"]
        for file_name in test_files:
            (self.temp_dir / file_name).touch()
        
        expected_names = ["file1txt", "file2txt", "file3txt"]
        new_file_names = f_438(str(self.temp_dir))
        
        self.assertListEqual(sorted(new_file_names), sorted(expected_names))
    
    def test_alphanumeric_names(self):
        test_files = ["file1.txt", "file2.txt", "file3.txt"]
        for file_name in test_files:
            (self.temp_dir / file_name).touch()
        
        expected_names = ["file1txt", "file2txt", "file3txt"]
        new_file_names = f_438(str(self.temp_dir))
        
        self.assertListEqual(sorted(new_file_names), sorted(expected_names))
    
    def test_empty_directory(self):
        expected_names = []
        new_file_names = f_438(str(self.temp_dir))
        
        self.assertListEqual(new_file_names, expected_names)
    
    def test_only_special_characters(self):
        test_files = ["@@@.txt", "###.txt", "$$$ .txt"]
        for file_name in test_files:
            (self.temp_dir / file_name).touch()
        
        expected_names = ["txt", "txt", "txt"]
        new_file_names = f_438(str(self.temp_dir))
        
        self.assertListEqual(sorted(new_file_names), sorted(expected_names))
    
    def test_mixed_characters(self):
        test_files = ["f@ile_1.txt", "file# 2.txt", "fi$le 3.txt"]
        for file_name in test_files:
            (self.temp_dir / file_name).touch()
        
        expected_names = ["file1txt", "file2txt", "file3txt"]
        new_file_names = f_438(str(self.temp_dir))
        
        self.assertListEqual(sorted(new_file_names), sorted(expected_names))
