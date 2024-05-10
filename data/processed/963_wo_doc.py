import os
import glob
from collections import Counter


def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    """
    Traverses a given directory recursively to count files by specified extensions.

    Parameters:
    - directory (str): The path of the directory to search.
    - extensions (list of str): File extensions to count. Defaults to ['.txt', '.docx', '.xlsx', '.csv'].
    - keep_zero (bool): Whether to include extensions with zero counts. Defaults to True.

    Returns:
    - Counter: An object containing counts of files for each of the specified extensions.

    Raises:
    - OSError: If the specified directory does not exist.

    Requirements:
    - os
    - glob
    - collections

    Note:
    - This function counts files in a case-sensitive manner.

    Examples:
    >>> task_func('/path/to/documents')
    Counter({'.txt': 5, '.docx': 2, '.xlsx': 1, '.csv': 0})
    >>> task_func('/path/to/documents', keep_zero=False)
    Counter({'.txt': 5, '.docx': 2, '.xlsx': 1})
    >>> task_func('/path/to/documents', extensions=['.txt'], keep_zero=False)
    Counter({'.txt': 5})
    """
    if not os.path.exists(directory):
        raise OSError("directory must exist.")
    counter = Counter()
    for suffix in extensions:
        count = len(
            glob.glob(os.path.join(directory, "**", "*" + suffix), recursive=True)
        )
        if count:
            counter[suffix] += count
        else:
            if keep_zero:
                counter[suffix] += count
    return counter

import unittest
from collections import Counter
from tempfile import TemporaryDirectory
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
    def tearDown(self):
        self.temp_dir.cleanup()
    def create_test_files(self, directory, file_list):
        for file_name in file_list:
            with open(os.path.join(directory, file_name), "w") as f:
                f.write("Test")
    def test_case_1(self):
        # Test basic case with default extensions
        file_names = ["file1.txt", "file2.docx", "file3.xlsx", "file4.csv", "file5.txt"]
        self.create_test_files(self.temp_dir.name, file_names)
        result = task_func(self.temp_dir.name)
        expected = Counter({".txt": 2, ".docx": 1, ".xlsx": 1, ".csv": 1})
        self.assertEqual(result, expected)
    def test_case_2(self):
        # Test empty directory
        result = task_func(self.temp_dir.name)
        expected = Counter({".txt": 0, ".docx": 0, ".xlsx": 0, ".csv": 0})
        self.assertEqual(result, expected)
    def test_case_3(self):
        # Test error handling - non-existent directory
        with self.assertRaises(OSError):
            task_func("/path/to/nonexistent/directory")
    def test_case_4(self):
        # Test ignoring unspecified extensions
        file_names = ["file1.pdf", "file2.png", "file3.txt"]
        self.create_test_files(self.temp_dir.name, file_names)
        result = task_func(self.temp_dir.name)
        expected = Counter({".txt": 1, ".docx": 0, ".xlsx": 0, ".csv": 0})
        self.assertEqual(result, expected)
    def test_case_5(self):
        # Test nested folders
        nested_dir_path = os.path.join(self.temp_dir.name, "nested")
        os.makedirs(nested_dir_path)
        file_names = ["nested_file1.txt", "nested_file2.xlsx"]
        self.create_test_files(nested_dir_path, file_names)
        result = task_func(self.temp_dir.name)
        expected = Counter({".txt": 1, ".xlsx": 1, ".docx": 0, ".csv": 0})
        self.assertEqual(result, expected)
    def test_case_6(self):
        # Test custom extensions
        file_names = ["image.jpeg", "video.mp4", "document.pdf"]
        self.create_test_files(self.temp_dir.name, file_names)
        result = task_func(
            self.temp_dir.name, extensions=[".jpeg", ".mp4"], keep_zero=False
        )
        expected = Counter({".jpeg": 1, ".mp4": 1})
        self.assertEqual(result, expected)
    def test_case_7(self):
        # Test custom extensions
        file_names = ["file1.txt", "file2.docx"]
        self.create_test_files(self.temp_dir.name, file_names)
        result = task_func(self.temp_dir.name, keep_zero=False)
        expected = Counter(
            {".txt": 1, ".docx": 1}
        )  # .xlsx and .csv are omitted because their count is 0 and keep_zero is False
        self.assertEqual(result, expected)
    def test_case_8(self):
        # Test case sensitivity
        file_names = ["file1.txt", "file1.tXt", "fiLE.txt", "fiLE.TXt"]
        self.create_test_files(self.temp_dir.name, file_names)
        result = task_func(self.temp_dir.name, extensions=[".txt"])
        expected = Counter({".txt": 2})
        self.assertEqual(result, expected)
