import os
from datetime import datetime

def f_644(filepath: str) -> dict:
    """
    Determine the size and date of the last modification of a file.

    Parameters:
    - filepath (str): The path to the file.

    Returns:
    - dict: A dictionary containing the size (in bytes) and last modification 
          date of the file in the format '%Y-%m-%d %H:%M:%S'.

    Requirements:
    - os
    - datetime

    Example:
    >>> f_644('/path/to/file.txt')
    {'size': '1024 bytes', 'last_modified': '2022-01-01 12:30:45'}
    """
    try:
        size = os.path.getsize(filepath)
        mtime = os.path.getmtime(filepath)
        mtime = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    except OSError as e:
        raise Exception(f"Error: {e}")
    return {'size': f"{size} bytes", 'last_modified': mtime}

import unittest
import os
from datetime import datetime
from unittest.mock import patch
import errno
def create_test_files(base_path):
    os.makedirs(base_path, exist_ok=True)
    with open(os.path.join(base_path, "empty_file.txt"), 'w') as f:
        pass
    with open(os.path.join(base_path, "large_file.txt"), 'w') as f:
        f.write("A" * 10**6)  # 1MB file
class TestCases(unittest.TestCase):
    def setUp(self):
        self.base_path = "f_644_data_xiaoheng"
        create_test_files(self.base_path)
    def tearDown(self):
        for item in os.listdir(self.base_path):
            os.remove(os.path.join(self.base_path, item))
        os.rmdir(self.base_path)
    def test_file_properties(self):
        file_path = os.path.join(self.base_path, "large_file.txt")
        result = f_644(file_path)
        expected_size = os.path.getsize(file_path)
        expected_mtime = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        self.assertEqual(result['size'], f"{expected_size} bytes")
        self.assertEqual(result['last_modified'], expected_mtime)
    def test_empty_file(self):
        file_path = os.path.join(self.base_path, "empty_file.txt")
        result = f_644(file_path)
        self.assertEqual(result['size'], "0 bytes")
    def test_file_not_found(self):
        file_path = os.path.join(self.base_path, "nonexistent.txt")
        with self.assertRaises(Exception) as context:
            f_644(file_path)
        self.assertIn("No such file or directory", str(context.exception))
    @patch('os.path.getsize')
    @patch('os.path.getmtime')
    def test_permission_error(self, mock_getmtime, mock_getsize):
        mock_getsize.side_effect = OSError(errno.EACCES, "Permission denied")
        mock_getmtime.side_effect = OSError(errno.EACCES, "Permission denied")
        
        with self.assertRaises(Exception) as context:
            f_644("fakepath/file.txt")
        self.assertIn("Permission denied", str(context.exception))
    def test_large_file(self):
        file_path = os.path.join(self.base_path, "large_file.txt")
        result = f_644(file_path)
        self.assertTrue(int(result['size'].replace(' bytes', '')) > 0)
