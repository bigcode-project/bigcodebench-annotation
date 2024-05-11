import codecs
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS):
    """
    Generate a random float number from a list of hex strings and then encode the float number in utf-8.

    Parameters:
    hex_keys (list of str): A list of hexadecimal strings to choose from.
    
    Returns:
    bytes: The utf-8 encoded float number.

    Requirements:
    - struct
    - codecs
    - random

    Example:
    >>> random.seed(42)
    >>> task_func()
    b'36806.078125'
    """
    hex_key = random.choice(hex_keys)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    encoded_float = codecs.encode(str(float_num), 'utf-8')
    return encoded_float

import unittest
class TestCases(unittest.TestCase):
    def test_default_functionality(self):
        """Test the function with default parameters."""
        result = task_func()
        self.assertIsInstance(result, bytes)  # Check if output is correctly encoded in UTF-8
    def test_custom_hex_keys(self):
        """Test the function with a custom list of hexadecimal keys."""
        custom_keys = ['1A2FC614', '1B0FC614', '1C9FC614']
        result = task_func(hex_keys=custom_keys)
        self.assertIsInstance(result, bytes)
    def test_empty_list(self):
        """Test the function with an empty list."""
        with self.assertRaises(IndexError):  # Assuming random.choice will raise IndexError on empty list
            task_func(hex_keys=[])
    def test_consistency_of_output(self):
        """Ensure that the output is consistent with a fixed seed."""
        random.seed(42)  # Set the seed for predictability
        first_result = task_func()
        random.seed(42)  # Reset seed to ensure same choice is made
        second_result = task_func()
        self.assertEqual(first_result, second_result)
    def test_invalid_hex_key(self):
        """Test with an invalid hex key."""
        invalid_keys = ['ZZZZZZZZ', 'XXXX']
        with self.assertRaises(ValueError):
            task_func(hex_keys=invalid_keys)
