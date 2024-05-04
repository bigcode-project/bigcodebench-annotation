import os
import ctypes
from datetime import datetime
import pytz

def f_73(filepath):
    """
    Loads a DLL file from the specified filepath and returns its metadata, including creation time,
    modification time, and file size. The times are displayed in UTC format. This function
    demonstrates the use of ctypes for loading DLLs and os module for accessing file metadata.

    
    Parameters:
    filepath (str): The path of the DLL file.

    Returns:
    str: The name of the loaded DLL file.
    dict: A dictionary containing the metadata of the DLL file, including the keys 'Creation Time', 'Modification Time', and 'Size'.
    
    Requirements:
    - ctypes
    - os
    - datetime.datetime
    - pytz

    Examples:
    >>> isinstance(f_73('libc.so.6'), str) # Doctest will vary based on the system and DLL file availability.
    True
    >>> 'libc.so.6' in f_73('libc.so.6')
    True
    """
    metadata = dict()
    lib = ctypes.CDLL(filepath)
    file_stat = os.stat(filepath)
    creation_time = datetime.fromtimestamp(file_stat.st_ctime, pytz.UTC)
    modification_time = datetime.fromtimestamp(file_stat.st_mtime, pytz.UTC)
    file_size = file_stat.st_size
    metadata['Creation Time'] = creation_time
    metadata['Modification Time'] = modification_time
    metadata['Size'] = file_size
    return lib._name, metadata

import unittest
import os
import ctypes
from unittest.mock import patch
import tempfile
import sys
from datetime import datetime
import pytz
from io import StringIO
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary DLL file
        self.temp_file = tempfile.NamedTemporaryFile(suffix='.dll', delete=False)
        self.filepath = self.temp_file.name
    def test_file_existence(self):
        self.assertTrue(os.path.exists(self.filepath))
    def test_invalid_file_path(self):
        with self.assertRaises(OSError):
            f_73('invalid_path.dll')
    @patch('ctypes.CDLL')
    @patch('os.stat')
    def test_return_value(self, mock_stat, mock_cdll):
        """Verify that the function returns the name of the DLL file."""
        mock_cdll.return_value._name = 'test.dll'
        result, metadata = f_73('path/to/test.dll')
        self.assertEqual(result, 'test.dll')
        self.assertIsInstance(metadata, dict)
    @patch('ctypes.CDLL', side_effect=OSError("File not found"))
    def test_nonexistent_file(self, mock_cdll):
        """Ensure function handles nonexistent files appropriately."""
        with self.assertRaises(OSError) as context:
            f_73('path/to/nonexistent.dll')
        self.assertEqual(str(context.exception), "File not found")
    @patch('os.stat')
    @patch('ctypes.CDLL')
    def test_metadata_printing(self, mock_cdll, mock_stat):
        """Check if file metadata is correctly printed."""
        # Setup mock for os.stat to return specific file metadata
        mock_stat.return_value.st_ctime = 1609459200  # 2021-01-01 00:00:00 UTC
        mock_stat.return_value.st_mtime = 1609545600  # 2021-01-02 00:00:00 UTC
        mock_stat.return_value.st_size = 123456
        # Setup mock for CDLL to return a dummy name
        mock_cdll.return_value._name = 'test.dll'
        # Set the expected output dictionary
        expected_output = {
            'Creation Time': datetime(2021, 1, 1, 0, 0, 0, tzinfo=pytz.UTC),
            'Modification Time': datetime(2021, 1, 2, 0, 0, 0, tzinfo=pytz.UTC),
            'Size': 123456
        }
        # Call the function
        result, metadata = f_73('path/to/test.dll')
        # Check if the output matches the expected dictionary
        self.assertEqual(result, 'test.dll', expected_output)
        self.assertEqual(metadata, expected_output)
        
    def tearDown(self):
        os.remove(self.filepath)
