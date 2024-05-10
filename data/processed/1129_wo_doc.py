import os
import re
import hashlib

def task_func(path, delimiter):
    """
    Splits a file path by a specified delimiter, retaining the delimiter in the output, and computes the hash of each component if it is a file.
    
    Parameters:
    path (str): The file path to split.
    delimiter (str): The delimiter to use for splitting the path.

    Returns:
    list[tuple]: A list of tuples, where each tuple contains a path component and its hash (if it's a file).
                 If the component is not a file, its hash will be None.

    Requirements:
    - os
    - re
    - hashlib

    Example:
    >>> task_func("Docs/src/file.txt", "/")
    [('Docs', None), ('/', None), ('src', None), ('/', None), ('file.txt', 'hash_value')]
    """
    path_components = re.split(f'({delimiter})', path)
    hashes = []
    for component in path_components:
        if not component:  # Remove empty components
            continue
        if component != delimiter and os.path.isfile(component):
            with open(component, 'rb') as f:
                hashes.append(hashlib.sha256(f.read()).hexdigest())
        else:
            hashes.append(None)
    return list(zip(path_components, hashes))

import unittest
import os
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory and files for testing
        self.test_dir = tempfile.mkdtemp()
        self.test_file1 = os.path.join(self.test_dir, 'file1.txt')
        self.test_file2 = os.path.join(self.test_dir, 'file2.txt')
        with open(self.test_file1, 'w') as f:
            f.write('Hello World')
        with open(self.test_file2, 'w') as f:
            f.write('Goodbye World')
    def tearDown(self):
        # Remove temporary files and directory after testing
        os.remove(self.test_file1)
        os.remove(self.test_file2)
        os.rmdir(self.test_dir)
    def test_simple_path_without_files(self):
        # Test splitting a path without any files
        result = task_func("Docs/src/", "/")
        expected = [('Docs', None), ('/', None), ('src', None), ('/', None)]
        self.assertEqual(result, expected)
    def test_path_with_file_but_no_hashing(self):
        # Test splitting a path with a file, assuming file does not exist for hashing
        result = task_func("Docs/src/file.txt", "/")
        expected = [('Docs', None), ('/', None), ('src', None), ('/', None), ('file.txt', None)]
        self.assertEqual(result, expected)
    def test_complex_path_with_no_files(self):
        # Test a more complex path with multiple directories and no files
        result = task_func("Dir1/file1/Dir2/file2.txt", "/")
        expected = [('Dir1', None), ('/', None), ('file1', None), ('/', None), ('Dir2', None), ('/', None), ('file2.txt', None)]
        self.assertEqual(result, expected)
    def test_path_with_non_standard_delimiter(self):
        # Test path splitting using a non-standard delimiter
        result = task_func(f"Dir1-file1-{self.test_file1}-file2.txt", "-")
        expected = [('Dir1', None), ('-', None), ('file1', None), ('-', None), (self.test_file1, hashlib.sha256(open(self.test_file1, 'rb').read()).hexdigest()), ('-', None), ('file2.txt', None)]
        self.assertEqual(result, expected)
    def test_empty_path(self):
        # Test an empty path string
        result = task_func("", "/")
        expected = []
        self.assertEqual(result, expected)
    def test_path_with_existing_files(self):
        # Test a path with existing files to check hashing
        path = f"{self.test_file1}####{self.test_file2}"
        result = task_func(path, "####")
        expected = [(self.test_file1, hashlib.sha256(open(self.test_file1, 'rb').read()).hexdigest()),
                    ('####', None),
                    (self.test_file2, hashlib.sha256(open(self.test_file2, 'rb').read()).hexdigest())]
        print(result)
        print(expected)
        self.assertEqual(result, expected)
