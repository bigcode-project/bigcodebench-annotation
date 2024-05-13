import json
import base64
import unicodedata

def task_func(json_file: str) -> dict:
    """
    This function reads a JSON file where each key is a unique identifier, and the corresponding value is a base64 encoded string.
    After decoding, it applies Unicode normalization form C (NFC) to each decoded string to ensure the canonical composition of characters.
    The function returns a dictionary where the keys are preserved, and the values are the normalized, decoded strings. Decoding is performed using the UTF-8 encoding scheme.

    Parameters:
    - json_file (str): The path to the JSON file.

    Returns:
    - dict: A dictionary where each key is mapped to a normalized, decoded string from the base64 encoded value in the input file.

    Requirements:
    - unicodedata
    - json
    - base64

    Examples:
    Given a file 'example.json' with the content:
    {"key1": "SGVsbG8gV29ybGQ=", "key2": "UHl0aG9uIENvZGUgUmVmaW5lcg=="}

    >>> task_func('example.json')
    {'key1': 'Hello World', 'key2': 'Python Code Refiner'}

    Given a file 'empty.json' with the content:
    {}

    >>> task_func('empty.json')
    {}
    """
    ENCODING = 'utf-8'
    with open(json_file, 'r') as f:
        data = json.load(f)
    decoded_data = {k: unicodedata.normalize('NFC', base64.b64decode(v).decode(ENCODING)) for k, v in data.items()}
    return decoded_data

import unittest
from unittest.mock import mock_open, patch
import json
class TestCases(unittest.TestCase):
    def setUp(self):
        # Initialize test data and expected results
        self.mock_data = '{"key1": "SGVsbG8gV29ybGQ=", "key2": "UHl0aG9uIENvZGUgUmVmaW5lcg=="}'
        self.expected_output = {'key1': 'Hello World', 'key2': 'Python Code Refiner'}
    def test_decode_base64(self):
        # Test decoding base64 encoded strings from a mock JSON file
        with patch('builtins.open', mock_open(read_data=self.mock_data)):
            result = task_func('dummy_file.json')
            self.assertEqual(result, self.expected_output)
    def test_empty_json(self):
        # Test handling of an empty JSON file
        with patch('builtins.open', mock_open(read_data='{}')):
            result = task_func('dummy_file.json')
            self.assertEqual(result, {})
    def test_non_json_content(self):
        # Test error handling for non-JSON content
        with patch('builtins.open', mock_open(read_data='Not a JSON')):
            with self.assertRaises(json.JSONDecodeError):
                task_func('dummy_file.json')
    def test_file_not_found(self):
        # Test error handling for a non-existent file
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_file.json')
    def test_invalid_base64(self):
        # Test error handling for invalid base64 encoding
        with patch('builtins.open', mock_open(read_data='{"key1": "Invalid base64"}')):
            with self.assertRaises(ValueError):
                task_func('dummy_file.json')
    def test_unicode_normalization(self):
        # Properly encode a Unicode string 'è' to base64
        unicode_string = 'è'
        encoded_unicode_string = base64.b64encode(unicode_string.encode('utf-8')).decode('ascii')
        mock_data_with_unicode = f'{{"key1": "{encoded_unicode_string}"}}'  # Encoded mock data
        expected_normalized_output = {'key1': 'è'}  # Expected result after normalization
        with patch('builtins.open', mock_open(read_data=mock_data_with_unicode)):
            result = task_func('dummy_file_unicode.json')
            self.assertEqual(result, expected_normalized_output)
