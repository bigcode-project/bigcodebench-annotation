import os
import json
import re
import shutil

# Constants
SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def f_659():
    """
    Move all json files in a source directory to a target directory and rename them by splitting the filename the last time "-" occurs and keeping the prefix part of the filename.
    
    Parameters:
    - None

    Requirements:
    - os
    - json
    - re
    - shutil

    Example:
    >>> f_659()
    """
    for filename in os.listdir(SOURCE_DIR):
        match = FILE_PATTERN.match(filename)
        if match is not None:
            prefix = match.group(1)
            new_filename = f'{prefix}.json'
            shutil.move(os.path.join(SOURCE_DIR, filename), os.path.join(TARGET_DIR, new_filename))

import unittest
import os

source_dirs = ["/mnt/data/test_data/source_0", "/mnt/data/test_data/source_1", "/mnt/data/test_data/source_2", "/mnt/data/test_data/source_3", "/mnt/data/test_data/source_4"]
target_dirs = ["/mnt/data/test_data/target_0", "/mnt/data/test_data/target_1", "/mnt/data/test_data/target_2", "/mnt/data/test_data/target_3", "/mnt/data/test_data/target_4"]

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        # This method will be run before each test case to reset the test data
        for s_dir, t_dir in zip(source_dirs, target_dirs):
            for file in os.listdir(t_dir):
                os.remove(os.path.join(t_dir, file))
            for j, file_name in enumerate(os.listdir(s_dir)):
                new_file_name = f"{os.path.splitext(file_name)[0].split('-')[0]}-{j}.json"
                os.rename(os.path.join(s_dir, file_name), os.path.join(s_dir, new_file_name))

    def test_case_1(self):
        # Test with source_0 and target_0 directories.
        # Expect 5 files to be moved and renamed correctly in target_0 directory.
        result = f_659(source_dirs[0], target_dirs[0])
        self.assertEqual(result["moved_files"], 5)
        self.assertTrue(all([file.endswith(".json") for file in result["new_filenames"]]))

    def test_case_2(self):
        # Test with source_1 and target_1 directories.
        # Expect 5 files to be moved and renamed correctly in target_1 directory.
        result = f_659(source_dirs[1], target_dirs[1])
        self.assertEqual(result["moved_files"], 5)
        self.assertTrue(all([file.endswith(".json") for file in result["new_filenames"]]))

    def test_case_3(self):
        # Test with source_2 and target_2 directories.
        # Expect 5 files to be moved and renamed correctly in target_2 directory.
        result = f_659(source_dirs[2], target_dirs[2])
        self.assertEqual(result["moved_files"], 5)
        self.assertTrue(all([file.endswith(".json") for file in result["new_filenames"]]))

    def test_case_4(self):
        # Test with source_3 and target_3 directories.
        # Expect 5 files to be moved and renamed correctly in target_3 directory.
        result = f_659(source_dirs[3], target_dirs[3])
        self.assertEqual(result["moved_files"], 5)
        self.assertTrue(all([file.endswith(".json") for file in result["new_filenames"]]))

    def test_case_5(self):
        # Test with source_4 and target_4 directories.
        # Expect 5 files to be moved and renamed correctly in target_4 directory.
        result = f_659(source_dirs[4], target_dirs[4])
        self.assertEqual(result["moved_files"], 5)
        self.assertTrue(all([file.endswith(".json") for file in result["new_filenames"]]))


if __name__ == "__main__":
    run_tests()