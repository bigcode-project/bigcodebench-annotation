import base64
import json
import zlib

def task_func(data_dict):
    """
    Serializes a dictionary to a JSON string, compresses it using zlib, and then encodes the compressed
    data with base64.

    Parameters:
    data_dict (dict): The dictionary to be compressed and encoded. The dictionary should only contain
                      data that can be serialized to JSON.

    Returns:
    str: A base64 encoded string that represents the zlib-compressed JSON string of the dictionary.

    Requirements:
    - base64
    - zlib
    - json
    
    Example:
    >>> data = {'key1': 'value1', 'key2': 'value2'}
    >>> encoded_data = task_func(data)
    >>> print(encoded_data)
    eJyrVspOrTRUslJQKkvMKU01VNJRAIkYwUWMlGoBw5sKmw==
    """

    json_str = json.dumps(data_dict)
    compressed = zlib.compress(json_str.encode())
    return base64.b64encode(compressed).decode()

import unittest
import json
import zlib
import base64
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a simple dictionary containing string values.
        data = {'key1': 'value1', 'key2': 'value2'}
        result = task_func(data)
        self.assertIsInstance(result, str)
        decompressed_data = json.loads(zlib.decompress(base64.b64decode(result)).decode())
        self.assertEqual(decompressed_data, data)
    def test_case_2(self):
        # Test with an empty dictionary.
        data = {}
        result = task_func(data)
        self.assertIsInstance(result, str)
        decompressed_data = json.loads(zlib.decompress(base64.b64decode(result)).decode())
        self.assertEqual(decompressed_data, data)
    def test_case_3(self):
        # Test with a dictionary containing mixed types (string and integers).
        data = {'name': 'John', 'age': 30, 'city': 'New York'}
        result = task_func(data)
        self.assertIsInstance(result, str)
        decompressed_data = json.loads(zlib.decompress(base64.b64decode(result)).decode())
        self.assertEqual(decompressed_data, data)
    def test_case_4(self):
        # Test with a nested dictionary containing lists of dictionaries.
        data = {'users': [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]}
        result = task_func(data)
        self.assertIsInstance(result, str)
        decompressed_data = json.loads(zlib.decompress(base64.b64decode(result)).decode())
        self.assertEqual(decompressed_data, data)
    def test_case_5(self):
        # Test with a dictionary containing multiple integer values.
        data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
        result = task_func(data)
        self.assertIsInstance(result, str)
        decompressed_data = json.loads(zlib.decompress(base64.b64decode(result)).decode())
        self.assertEqual(decompressed_data, data)
