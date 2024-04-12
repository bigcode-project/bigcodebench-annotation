import re
import os
import zipfile

# Constants
ZIP_DIR = '/zip/dir'
ZIP_PATTERN = re.compile(r'^(.*?)-\d+\.zip$')

def f_661():
    """
    Unzip all zip files in a directory whose name matches a certain pattern by splitting the filename the last time "-" occurs and using the prefix part of the filename as the directory to extract.
    
    Parameters:
    - None    

    Requirements:
    - os
    - re
    - zipfile

    Example:
    >>> f_661()
    """
    for filename in os.listdir(ZIP_DIR):
        match = ZIP_PATTERN.match(filename)
        if match is not None:
            prefix = match.group(1)
            with zipfile.ZipFile(os.path.join(ZIP_DIR, filename), 'r') as zip_ref:
                zip_ref.extractall(os.path.join(ZIP_DIR, prefix))

import unittest
import os

TEST_DIR = "/mnt/data/test_zip_dir"

class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Test with default pattern
        # We expect three directories (sample, test_data, data_test) to be created 
        # when using the default pattern.
        extracted_dirs = f_661(TEST_DIR)
        self.assertEqual(len(extracted_dirs), 3)
        self.assertIn(os.path.join(TEST_DIR, "sample"), extracted_dirs)
        self.assertIn(os.path.join(TEST_DIR, "test_data"), extracted_dirs)
        self.assertIn(os.path.join(TEST_DIR, "data_test"), extracted_dirs)

    def test_case_2(self):
        # Test with a custom pattern that matches filenames like "test_data-<number>.zip".
        # We expect only the "test_data" directory to be created.
        pattern = r'^(test_data)-\d+\.zip$'
        extracted_dirs = f_661(TEST_DIR, pattern=pattern)
        self.assertEqual(len(extracted_dirs), 1)
        self.assertIn(os.path.join(TEST_DIR, "test_data"), extracted_dirs)

    def test_case_3(self):
        # Test with another custom pattern that matches filenames like "data_test-<number>.zip".
        # We expect only the "data_test" directory to be created.
        pattern = r'^(data_test)-\d+\.zip$'
        extracted_dirs = f_661(TEST_DIR, pattern=pattern)
        self.assertEqual(len(extracted_dirs), 1)
        self.assertIn(os.path.join(TEST_DIR, "data_test"), extracted_dirs)

    def test_case_4(self):
        # Test with a pattern that doesn't match any file in the directory.
        # We expect no directories to be created.
        pattern = r'^non_existent-\d+\.zip$'
        extracted_dirs = f_661(TEST_DIR, pattern=pattern)
        self.assertEqual(len(extracted_dirs), 0)

    def test_case_5(self):
        # Test with a more complex pattern that matches filenames like "test-<number>_data.zip".
        # We expect only the "test" directory to be created.
        pattern = r'^(test)-\d+_data\.zip$'
        extracted_dirs = f_661(TEST_DIR, pattern=pattern)
        self.assertEqual(len(extracted_dirs), 1)
        self.assertIn(os.path.join(TEST_DIR, "test"), extracted_dirs)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()