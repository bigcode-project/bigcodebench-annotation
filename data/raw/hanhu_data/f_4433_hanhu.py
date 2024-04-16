import ctypes
import hashlib
import binascii

def f_4435(filepath):
    """
    Loads a DLL file from a given filepath, calculates its MD5 and SHA256 hashes,
    and prints these hashes in hexadecimal format. This function is a demonstration
    of file handling, usage of the hashlib library for hash calculations, and binascii
    for hexadecimal conversion. Note that the actual operations performed on the loaded
    DLL are limited to hash calculation.

    Parameters:
    filepath (str): The path of the DLL file.

    Returns:
    str: The name of the loaded DLL file.

    Requirements:
    - ctypes
    - hashlib
    - binascii

    Examples:
    >>> isinstance(f_4435('libc.so.6'), str) # Example output will vary based on system and DLL file availability.
    True
    >>> 'libc.so.6' in f_4435('libc.so.6')
    True
    """
    lib = ctypes.CDLL(filepath)

    with open(filepath, 'rb') as f:
        data = f.read()

    md5_hash = hashlib.md5(data).digest()
    print(f'MD5 Hash: {binascii.hexlify(md5_hash).decode()}')

    sha256_hash = hashlib.sha256(data).digest()
    print(f'SHA256 Hash: {binascii.hexlify(sha256_hash).decode()}')

    return lib._name

import unittest
from unittest.mock import patch
import tempfile
import os
import sys
from io import StringIO
import binascii

class TestF4435(unittest.TestCase):

    def setUp(self):
        # Create a temporary DLL file
        self.temp_file = tempfile.NamedTemporaryFile(suffix='.dll', delete=False)
        self.filepath = self.temp_file.name
        # Redirect stdout to capture print statements
        self.original_stdout = sys.stdout
        sys.stdout = StringIO()

    def test_file_existence(self):
        self.assertTrue(os.path.exists(self.filepath))

    def test_invalid_file_path(self):
        with self.assertRaises(OSError):
            f_4435('invalid_path.dll')

    @patch('ctypes.CDLL')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data=b'test data')
    @patch('hashlib.md5')
    @patch('hashlib.sha256')
    def test_dll_name_returned(self, mock_sha256, mock_md5, mock_open, mock_cdll):
        """Test if the function returns the name of the loaded DLL file."""
        mock_md5.return_value.digest.return_value = b'\x93\x15\x98\x3f\xcd\xb4\xcc\xcb\x28\x7b\xcc\xdb\xdd\x4e\x8a\x45'  # Mock MD5 digest
        mock_sha256.return_value.digest.return_value = b'\xd7\xa8\xfb\x48\xd2\x8d\x1d\x73\xa0\x34\x6b\xbf\x40\x41\xdf\x98\xc2\x50\x1d\x4a\xe4\x88\x9b\x93\x4f\xaa\x63\xf7\xaf\x67\xe9\xb1'  # Mock SHA256 digest
        mock_cdll.return_value._name = 'test.dll'
        dll_name = f_4435(self.filepath)  # Replace 'f_4435_module.f_4435' with the actual path to your f_4435 function
        self.assertEqual(dll_name, 'test.dll')

    @patch('ctypes.CDLL')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data=b'test data')
    @patch('hashlib.md5')
    def test_md5_hash_printed(self, mock_md5, mock_open, mock_cdll):
        """Test if the MD5 hash is correctly calculated and printed."""
        expected_hash = b'\x93\x15\x98\x3f\xcd\xb4\xcc\xcb\x28\x7b\xcc\xdb\xdd\x4e\x8a\x45'
        mock_md5.return_value.digest.return_value = expected_hash

        with patch('builtins.print') as mock_print:
            f_4435('path/to/test.dll')
            expected_md5_output = f'MD5 Hash: {binascii.hexlify(expected_hash).decode()}'
            mock_print.assert_any_call(expected_md5_output)

    @patch('ctypes.CDLL')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data=b'test data')
    @patch('hashlib.sha256')
    def test_sha256_hash_printed(self, mock_sha256, mock_open, mock_cdll):
        """Test if the SHA256 hash is correctly calculated and printed."""
        expected_hash = b'\xd7\xa8\xfb\x48\xd2\x8d\x1d\x73\xa0\x34\x6b\xbf\x40\x41\xdf\x98\xc2\x50\x1d\x4a\xe4\x88\x9b\x93\x4f\xaa\x63\xf7\xaf\x67\xe9\xb1'
        mock_sha256.return_value.digest.return_value = expected_hash

        with patch('builtins.print') as mock_print:
            f_4435('path/to/test.dll')
            expected_sha256_output = f'SHA256 Hash: {binascii.hexlify(expected_hash).decode()}'
            mock_print.assert_any_call(expected_sha256_output)

    def tearDown(self):
        os.remove(self.filepath)
        sys.stdout = self.original_stdout


if __name__ == '__main__':
    unittest.main()
