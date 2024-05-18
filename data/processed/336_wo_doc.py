import re
import os
import glob
from pathlib import Path


def task_func(pattern, directory, extensions):
    """
    Find all files in a specific directory that contain a regex pattern in their contents in a case insensitive manner.
    
    Parameters:
    pattern (str): The regex pattern to match.
    directory (str): The directory to search in.
    extensions (list): The file extensions to consider. 
    
    Returns:
    list: A list of absolute file paths that contain the pattern.
    
    Requirements:
    - os
    - glob
    - pathlib
    - re

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()
    >>> with open(os.path.join(temp_dir, 'hello.txt'), 'w') as f:
    ...     _ = f.write('Hello, this is a test file.')
    >>> with open(os.path.join(temp_dir, 'hello.md'), 'w') as f:
    ...     _ = f.write('# Notes')
    >>> matches = task_func('Hello', temp_dir, ['*.txt', '*.md'])
    >>> str(matches[0]).endswith('hello.txt')
    True
    """
    matched_files = []
    for ext in extensions:
        files = glob.glob(os.path.join(directory, ext))
        for file in files:
            with open(file, 'r') as f:
                content = f.read().lower()
                if re.search(pattern.lower(), content):
                    matched_files.append(Path(file).resolve())
    return matched_files

import unittest
import shutil
import doctest
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.extensions = ['*.txt', '*.md', '*.csv']
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_directory = f"{self.base_tmp_dir}/test/"
        os.makedirs(self.test_directory, exist_ok=True)
        # Sample data to be written to files
        sample_files_data = {
            "sample1.txt": "Hello, this is a test file.\nContains some text.",
            "sample2.md": "# Markdown File\n\nThis is a markdown hello file.\n",
            "sample3.csv": "Name,Age\nAlice,25\nBob,hello\nCharlie,30",
            "sample4.txt": "Just another random text file.",
            "sample5.md": "Hello world! This is a markdown file."
        }
        # Write the sample data to files
        for filename, content in sample_files_data.items():
            with (
                    open(os.path.join(self.test_directory, filename), 'w')
                    if os.path.exists(os.path.join(self.test_directory, filename))
                    else open(os.path.join(self.test_directory, filename), 'x')
            ) as file:
                file.write(content)
    def tearDown(self):
        if os.path.exists(self.test_directory):
            shutil.rmtree(self.test_directory)
    def test_case_1(self):
        matched_files = task_func('.*hello.*', self.test_directory, self.extensions)
        matched_files = [Path(file).name for file in matched_files]
        expected_files = ['sample1.txt', 'sample2.md', 'sample3.csv', 'sample5.md']
        self.assertCountEqual(matched_files, expected_files)
    def test_case_2(self):
        matched_files = task_func('alice', self.test_directory, self.extensions)
        matched_files = [Path(file).name for file in matched_files]
        expected_files = ['sample3.csv']
        self.assertCountEqual(matched_files, expected_files)
    def test_case_3(self):
        matched_files = task_func('random', self.test_directory, self.extensions)
        matched_files = [Path(file).name for file in matched_files]
        expected_files = ['sample4.txt']
        self.assertCountEqual(matched_files, expected_files)
    def test_case_4(self):
        matched_files = task_func('\#', self.test_directory, self.extensions)
        matched_files = [Path(file).name for file in matched_files]
        expected_files = ['sample2.md']
        self.assertCountEqual(matched_files, expected_files)
    def test_case_5(self):
        matched_files = task_func('world', self.test_directory, self.extensions)
        matched_files = [Path(file).name for file in matched_files]
        expected_files = ['sample5.md']
        self.assertCountEqual(matched_files, expected_files)
