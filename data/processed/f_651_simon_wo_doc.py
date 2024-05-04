import shutil
from pathlib import Path
from typing import List

def f_274(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    '''
    Move all files with certain extensions from one directory to another.

    Parameters:
    - source_dir (str): The directory containing the source files.
    - target_dir (str): The directory to which the files should be moved.
    - extensions (List[str]): The list of file extensions to be moved.

    Returns:
    int: The number of moved files.

    Raises:
    - ValueError: If source_dir or target_dir does not exist.

    Requirements:
    - shutil
    - pathlib.Path

    Example:
    >>> f_274('path/to/source/', 'path/to/target/', ['.jpg', '.png', '.gif'])
    15
    >>> f_274('path/to/source/', 'path/to/target/', ['.txt'])
    1
    '''
    if Path(source_dir).is_dir() == False:
        raise ValueError("source_dir does not exist.")
    if Path(target_dir).is_dir() == False:
        raise ValueError("target_dir does not exist.")
    count = 0
    for extension in extensions:
        for file_name in Path(source_dir).glob(f'*{extension}'):
            shutil.move(str(file_name), target_dir)
            count += 1
    return count

import unittest
import tempfile
import os
import shutil
def setup_test_environment(extensions, num_files_per_extension):
    # Create temporary directories
    source_dir = tempfile.mkdtemp()
    target_dir = tempfile.mkdtemp()
    file_list = []
    # Populate source_dir with files
    for ext in extensions:
        for i in range(num_files_per_extension):
            with open(os.path.join(source_dir, f"file_{i}{ext}"), "w") as f:
                f.write(f"This is a sample {ext} file.")
                file_list.append(f"file_{i}{ext}")
    return source_dir, target_dir, file_list
# Cleanup function to remove temporary directories after test
def cleanup_test_environment(source_dir, target_dir):
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)
# Define the test cases
class TestCases(unittest.TestCase):
    def test_case_dir(self):
        source_dir, target_dir, file_list = setup_test_environment(['.jpg', '.png', '.gif'], 3)
        self.assertRaises(Exception, f_274, 'non_existent', target_dir, ['.test'])
        self.assertRaises(Exception, f_274, source_dir, 'non_existent', ['.test'])
    
    def test_case_1(self):
        # Test basic functionality with jpg, png, and gif extensions
        source_dir, target_dir, file_list = setup_test_environment(['.jpg', '.png', '.gif'], 3)
        result = f_274(source_dir, target_dir, ['.jpg', '.png', '.gif'])
        self.assertEqual(result, 9)  # 3 files for each of the 3 extensions
        self.assertEqual(len(os.listdir(target_dir)), 9)
        self.assertCountEqual(file_list, os.listdir(target_dir))
        cleanup_test_environment(source_dir, target_dir)
    def test_case_2(self):
        # Test only one extension
        source_dir, target_dir, file_list = setup_test_environment(['.jpg', '.png', '.gif', '.txt'], 12)
        result = f_274(source_dir, target_dir, ['.jpg'])
        file_list = [file for file in file_list if file[-4:] == '.jpg']
        self.assertEqual(result, 12)  # Only jpg files should be moved
        self.assertEqual(len(os.listdir(target_dir)), 12)
        self.assertCountEqual(file_list, os.listdir(target_dir))
        cleanup_test_environment(source_dir, target_dir)
    def test_case_3(self):
        # Test with no files to move
        source_dir, target_dir, file_list = setup_test_environment(['.jpg'], 8)
        result = f_274(source_dir, target_dir, ['.png'])
        self.assertEqual(result, 0)  # No png files in source
        self.assertEqual(len(os.listdir(target_dir)), 0)
        self.assertCountEqual([], os.listdir(target_dir))
        cleanup_test_environment(source_dir, target_dir)
    def test_case_4(self):
        # Test with empty source directory
        source_dir = tempfile.mkdtemp()
        target_dir = tempfile.mkdtemp()
        result = f_274(source_dir, target_dir, ['.jpg', '.png', '.gif'])
        self.assertEqual(result, 0)  # No files to move
        self.assertEqual(len(os.listdir(target_dir)), 0)
        self.assertCountEqual([], os.listdir(target_dir))
        cleanup_test_environment(source_dir, target_dir)
    def test_case_5(self):
        # Test moving multiple extensions but not all
        source_dir, target_dir, file_list = setup_test_environment(['.jpg', '.txt', '.doc', 'png'], 5)
        result = f_274(source_dir, target_dir, ['.jpg', '.txt', '.doc'])
        file_list = [file for file in file_list if file[-4:] in ['.jpg', '.txt', '.doc']]
        self.assertEqual(result, 15)  # All files should be moved
        self.assertEqual(len(os.listdir(target_dir)), 15)
        self.assertCountEqual(file_list, os.listdir(target_dir))
        cleanup_test_environment(source_dir, target_dir)
