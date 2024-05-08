import json
from collections import Counter
import random

def f_560(my_dict, keys):
    """
    Updates a given dictionary by adding 10 random elements based on the 'keys' parameter,
    with values as random integers from 1 to 100. It saves the JSON representation of the
    updated dictionary to a file and the counts of each key to a separate text file.

    Parameters:
        my_dict (dict): The dictionary to be updated.
        keys (list of str): A list of keys to be added to the dictionary.

    Returns:
        tuple: The dictionary, path to the JSON file, and path to the text file.

    Raises:
        ValueError: If 'keys' does not contain exactly 10 unique elements.

    Note:
        This function modifies the input dictionary in place.
        The filename of the json is 'updated_dictionary.json'
        The filename of the txt file is 'key_frequencies.txt'

    Requirements:
    - json
    - collections.Counter
    - random

    Examples:
    >>> result, json_path, txt_path = f_560({'first_key': 1, 'second_key': 2}, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    >>> isinstance(result, dict)
    True
    >>> len(result) > 2  # Checking if more keys have been added
    True
    """
    if len(set(keys)) != 10:
        raise ValueError("keys parameter must contain exactly 10 unique elements")
    for key in keys:
        my_dict[key] = random.randint(1, 100)
    json_filename = "updated_dictionary.json"
    txt_filename = "key_frequencies.txt"
    with open(json_filename, 'w') as json_file:
        json.dump(my_dict, json_file, indent=4)
    key_counts = Counter(my_dict.keys())
    with open(txt_filename, 'w') as txt_file:
        for key, count in key_counts.items():
            txt_file.write(f"{key}: {count}\n")
    return my_dict, json_filename, txt_filename

import unittest
from unittest.mock import patch
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    def tearDown(self):
        json_filename = "updated_dictionary.json"
        txt_filename = "key_frequencies.txt"
        if os.path.exists(json_filename):
            os.remove(json_filename)
        if os.path.exists(txt_filename):
            os.remove(txt_filename)
        
    def test_return_type(self):
        """Test that the function returns the correct tuple types."""
        result, json_path, txt_path = f_560({}, self.keys)
        self.assertIsInstance(result, dict)
        self.assertIsInstance(json_path, str)
        self.assertIsInstance(txt_path, str)
    def test_new_keys_added(self):
        """Test that new keys are added to the dictionary."""
        result, _, _ = f_560({}, self.keys)
        for key in self.keys:
            self.assertIn(key, result)
    def test_original_keys_preserved(self):
        """Test that original keys in the dictionary are preserved."""
        original_dict = {'x': 200, 'y': 300}
        result, _, _ = f_560(original_dict.copy(), self.keys)
        self.assertIn('x', result)
        self.assertIn('y', result)
    def test_values_within_range(self):
        """Test that all values are within the specified range 1-100."""
        result, _, _ = f_560({}, self.keys)
        for value in result.values():
            self.assertTrue(1 <= value <= 100)
    def test_dictionary_length_update(self):
        """Test that the dictionary length is correctly updated."""
        original_dict = {'x': 200, 'y': 300}
        expected_length = len(original_dict) + len(self.keys)
        result, _, _ = f_560(original_dict.copy(), self.keys)
        self.assertEqual(len(result), expected_length)
    def test_files_created(self):
        """Test that JSON and TXT files are created."""
        _, json_path, txt_path = f_560({}, self.keys)
        self.assertTrue(os.path.exists(json_path))
        self.assertTrue(os.path.exists(txt_path))
    def test_value_error_raised_for_invalid_keys(self):
        """Test that a ValueError is raised if 'keys' does not contain exactly 10 unique elements."""
        with self.assertRaises(ValueError):
            f_560({}, ['a', 'b'])  # Not enough keys
    @patch('random.randint', return_value=50)
    def test_mock_random(self, mock_randint):
        """Test the function with a mock of the random.randint function."""
        result, _, _ = f_560({}, self.keys)
        mock_randint.assert_called()
        for key in self.keys:
            self.assertEqual(result[key], 50)
