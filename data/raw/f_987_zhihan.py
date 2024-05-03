import os
import re
import hashlib

def f_987(path=FILE_PATH, delimiter=SPLIT_PATTERN):
    """
    Divide a file path by a specific delimiter, leaving the delimiter in the result.
    The function also computes the hash of the file if the path is a file.
    
    Parameters:
    path (str): The file path to split. Default is 'Docs/src/Scripts/temp'.
    delimiter (str): The delimiter to use for splitting the path. Default is '/'.

    Returns:
    list[tuple]: A list of tuples, where each tuple contains a path component and its hash (if it's a file).
                 If the component is not a file, its hash will be None.

    Requirements:
    - os
    - re
    - hashlib

    Example:
    >>> f_987("Docs/src/file.txt", "/")
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

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = f_987("Docs/src/", "/")
        expected = [('Docs', None), ('/', None), ('src', None), ('/', None)]
        self.assertEqual(result, expected)

    def test_case_2(self):
        result = f_987("Docs/src/file.txt", "/")
        expected = [('Docs', None), ('/', None), ('src', None), ('/', None), ('file.txt', None)]
        self.assertEqual(result, expected)

    def test_case_3(self):
        result = f_987("Dir1/file1/Dir2/file2.txt", "/")
        expected = [('Dir1', None), ('/', None), ('file1', None), ('/', None), ('Dir2', None), ('/', None), ('file2.txt', None)]
        self.assertEqual(result, expected)

    def test_case_4(self):
        result = f_987("Dir1-file1-Dir2-file2.txt", "-")
        expected = [('Dir1', None), ('-', None), ('file1', None), ('-', None), ('Dir2', None), ('-', None), ('file2.txt', None)]
        self.assertEqual(result, expected)

    def test_case_5(self):
        result = f_987("", "/")
        expected = []
        self.assertEqual(result, expected)

if __name__ == "__main__":
    run_tests()