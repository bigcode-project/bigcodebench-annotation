import sys
from pathlib import Path

# Constants
PATH_TO_APPEND = '/path/to/whatever'

def task_func(path_to_append=PATH_TO_APPEND):
    """
    Add a specific path to sys.path and create a directory in that path if it does not exist.

    Note:
    - The function uses a constant PATH_TO_APPEND which defaults to '/path/to/whatever'.

    Parameters:
    - path_to_append (str): The path to append to sys.path and to create a directory. Default is '/path/to/whatever'.

    Returns:
    - path_to_append (str): The path that was appended and where the directory was created.

    Requirements:
    - sys
    - pathlib
 
    Examples:
    >>> task_func("/new/path/to/append")
    "/new/path/to/append"

    >>> task_func()
    "/path/to/whatever"

    """

    Path(path_to_append).mkdir(parents=True, exist_ok=True)
    sys.path.append(path_to_append)
    return path_to_append

import tempfile
import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        # Creating a temporary directory
        self.temp_dir = tempfile.TemporaryDirectory()
        # Removing the appended path from sys.path for each test case
        if self.temp_dir.name + '/test/path' in sys.path:
            sys.path.remove(self.temp_dir.name + '/test/path')
        if self.temp_dir.name + '/another/test/path' in sys.path:
            sys.path.remove(self.temp_dir.name + '/another/test/path')
    def tearDown(self):
        # Cleaning up the temporary directory
        self.temp_dir.cleanup()
    def test_1(self):
        # Testing with the default path
        result = task_func(self.temp_dir.name + '/path/to/whatever')
        self.assertEqual(result, self.temp_dir.name + '/path/to/whatever')
        self.assertTrue(self.temp_dir.name + '/path/to/whatever' in sys.path)
        self.assertTrue(Path(self.temp_dir.name + '/path/to/whatever').exists())
    def test_2(self):
        # Testing with a custom path
        result = task_func(self.temp_dir.name + '/test/path')
        self.assertEqual(result, self.temp_dir.name + '/test/path')
        self.assertTrue(self.temp_dir.name + '/test/path' in sys.path)
        self.assertTrue(Path(self.temp_dir.name + '/test/path').exists())
    def test_3(self):
        # Testing if the directory is actually created
        task_func(self.temp_dir.name + '/another/test/path')
        self.assertTrue(Path(self.temp_dir.name + '/another/test/path').exists())
    def test_4(self):
        # Testing if the path is appended to sys.path
        task_func(self.temp_dir.name + '/test/path')
        self.assertTrue(self.temp_dir.name + '/test/path' in sys.path)
    def test_5(self):
        # Testing if the function returns the correct path
        result = task_func(self.temp_dir.name + '/test/path')
        self.assertEqual(result, self.temp_dir.name + '/test/path')
