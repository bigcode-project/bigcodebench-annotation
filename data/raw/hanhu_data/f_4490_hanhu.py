import os
import pathlib
from hashlib import md5
import unicodedata

def f_4492(directory):
    """
    Processes all files within the specified directory, normalizes their filenames to ASCII,
    calculates their MD5 hashes, and retrieves their sizes. It returns a dictionary where
    each key is the normalized file name and each value is another dictionary with the file's size
    and MD5 hash. This method is useful for file integrity checks and file organization tasks.

    Parameters:
    directory (str): The directory path whose files are to be analyzed.

    Returns:
    dict: A dictionary where each key is a normalized file name, and the value is a dictionary
          containing the 'Size' (in bytes) and 'MD5 Hash' of the file.

    Requirements:
    - os
    - pathlib
    - hashlib.md5
    - unicodedata

    Examples:
    >>> info = f_4492('test')
    >>> type(info) == dict
    True
    >>> 'test.txt' in info
    True
    """
    files_info = {}

    for file_path in pathlib.Path(directory).iterdir():
        if file_path.is_file():
            normalized_file_name = unicodedata.normalize('NFKD', file_path.name).encode('ascii', 'ignore').decode()

            with open(file_path, 'rb') as file:
                file_content = file.read()
                file_hash = md5(file_content).hexdigest()

            files_info[normalized_file_name] = {'Size': os.path.getsize(file_path), 'MD5 Hash': file_hash}

    return files_info

import unittest
import os
import tempfile
import hashlib

class TestF4492(unittest.TestCase):

    def setUp(self):
        # Setup a temporary directory with files for testing
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file_path = os.path.join(self.temp_dir.name, "tést.txt")
        with open(self.test_file_path, "w") as file:
            file.write("Hello World")

    def test_return_type(self):
        result = f_4492(self.temp_dir.name)
        self.assertIsInstance(result, dict)

    def test_file_presence(self):
        result = f_4492(self.temp_dir.name)
        self.assertIn("test.txt", result)

    def test_file_size(self):
        result = f_4492(self.temp_dir.name)
        self.assertEqual(result["test.txt"]["Size"], 11)

    def test_file_hash(self):
        # This test could check the MD5 hash of a known file content
        expected_hash = hashlib.md5("Hello World".encode()).hexdigest()
        result = f_4492(self.temp_dir.name)
        normalized_file_name = "test.txt"
        self.assertEqual(result[normalized_file_name]["MD5 Hash"], expected_hash)

    def test_normalized_filename(self):
        # This test could check for filename normalization (ASCII conversion)
        result = f_4492(self.temp_dir.name)
        expected_name = "test.txt"
        self.assertIn(expected_name, result)
        self.assertNotIn("tést.txt", result)

    def tearDown(self):
        self.temp_dir.cleanup()


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestF4492)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
