import json
import os
import hashlib
import base64
import time

def task_func(file_path, unknown_key):
    """
    Reads a JSON file, extracts a value specified by an 'unknown_key' within a nested structure, hashes this value using SHA256,
    and writes the base64-encoded hash to a new file with a timestamp in its name. The JSON should contain a specific 
    structure where the value to be hashed is under 'A' -> [unknown_key] -> 'maindata' -> [index 0] -> 'Info'.

    Parameters:
    - file_path (str): The file path to read the JSON data from.
    - unknown_key (str): The key to look for in the nested JSON structure under the top-level key 'A'. This key should 
                         lead to a list of dictionaries under 'maindata', with the first dictionary containing the 'Info' key.

    Returns:
    str: The absolute file path of the newly created file containing the hashed value.
    
    Requirements:
    - json
    - os
    - hashlib
    - base64
    - time
    
    Example:
    >>> json_file = '/path/to/file.json'
    >>> new_file = task_func(json_file, 'B')
    >>> print(f"Hashed data saved at: {new_file}")
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    value = data['A'][unknown_key]["maindata"][0]["Info"]
    hashed_value = hashlib.sha256(value.encode()).digest()
    hashed_str = base64.b64encode(hashed_value).decode()
    new_file_name = f"{unknown_key}_hashed_{int(time.time())}.txt"
    new_file_path = os.path.join(os.getcwd(), new_file_name)
    with open(new_file_path, 'w') as f:
        f.write(hashed_str)
    return new_file_path

import unittest
import os
import json
import hashlib
import base64
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup temporary directory for tests
        self.temp_dir = tempfile.mkdtemp()
        # Create sample JSON data for the tests
        self.path_1 = os.path.join(self.temp_dir, 'test1.json')
        self.path_2 = os.path.join(self.temp_dir, 'test2.json')
        sample_data_1 = {
            'A': {
                'B': {
                    'maindata': [{'Info': 'hello world'}],
                },
                'C': {
                    'maindata': [{'Info': 'goodbye world'}],
                }
            }
        }
        sample_data_2 = {
            'A': {
                'D': {
                    'maindata': [{'Info': 'another world'}],
                },
                'E': {
                    'maindata': [{'Info': 'yet another world'}],
                }
            }
        }
        # Write sample data to files
        with open(self.path_1, 'w') as f:
            json.dump(sample_data_1, f)
        with open(self.path_2, 'w') as f:
            json.dump(sample_data_2, f)
    def tearDown(self):
        # Clean up the temporary directory
        os.remove(self.path_1)
        os.remove(self.path_2)
        os.rmdir(self.temp_dir)
    def test_hash_length_for_key_B(self):
        # Check the length of the base64-encoded SHA-256 hash for key B
        result = task_func(self.path_1, 'B')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)
        os.remove(result)
    def test_hash_length_for_key_C(self):
        # Check the length of the base64-encoded SHA-256 hash for key C
        result = task_func(self.path_1, 'C')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)
        os.remove(result)
    def test_hash_length_for_key_D(self):
        # Check the length of the base64-encoded SHA-256 hash for key D
        result = task_func(self.path_2, 'D')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)
        os.remove(result)
    def test_hash_length_for_key_E(self):
        # Check the length of the base64-encoded SHA-256 hash for key E
        result = task_func(self.path_2, 'E')
        self.assertTrue(os.path.exists(result))
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(len(hashed_value), 44)
        os.remove(result)
    def test_hash_value_for_key_B(self):
        # Verify the hash value for key B is correctly computed and encoded
        result = task_func(self.path_1, 'B')
        expected_info = 'hello world'
        expected_hash = hashlib.sha256(expected_info.encode()).digest()
        expected_base64 = base64.b64encode(expected_hash).decode()
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(hashed_value, expected_base64)
        os.remove(result)
    def test_hash_value_for_key_C(self):
        # Verify the hash value for key C is correctly computed and encoded
        result = task_func(self.path_1, 'C')
        expected_info = 'goodbye world'
        expected_hash = hashlib.sha256(expected_info.encode()).digest()
        expected_base64 = base64.b64encode(expected_hash).decode()
        with open(result, 'r') as f:
            hashed_value = f.read()
        self.assertEqual(hashed_value, expected_base64)
        os.remove(result)
    def test_invalid_key_error(self):
        # Test handling of invalid key
        with self.assertRaises(KeyError):
            task_func(self.path_1, 'Z')
# Define this function only if needed to run tests manually
