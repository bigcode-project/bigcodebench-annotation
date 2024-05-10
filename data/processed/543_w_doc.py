import hashlib
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']


def task_func(hex_keys=KEYS, seed=42):
    """
    Given a list of hexadecimal string keys, this function selects one at random,
    converts it into a floating-point number, and then computes its MD5 hash. An optional
    seed parameter allows for deterministic random choices for testing purposes.

    Parameters:
    hex_keys (list of str): A list of hexadecimal strings to choose from.
    seed (int, optional): A seed for the random number generator to ensure deterministic behavior.

    Returns:
    str: The MD5 hash of the floating-point number derived from the randomly selected hexadecimal string.

    Raises:
    ValueError: If contains invalid hexadecimal strings.

    Requirements:
    - struct
    - hashlib
    - random

    Example:
    >>> task_func(['1a2b3c4d', '5e6f7g8h'])
    '426614caa490f2c185aebf58f1d4adac'
    """
    random.seed(seed)
    hex_key = random.choice(hex_keys)
    try:
        float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    except ValueError as e:
        raise ValueError("Invalid hexadecimal string in hex_keys.") from e
    hashed_float = hashlib.md5(str(float_num).encode()).hexdigest()
    return hashed_float

import unittest
class TestCases(unittest.TestCase):
    def test_normal_functionality(self):
        """Test the function with default parameters."""
        result = task_func()
        self.assertIsInstance(result, str)
    def test_custom_keys_list(self):
        """Test the function with a custom list of hexadecimal keys."""
        custom_keys = ['1A2FC614', '1B0FC614', '1C9FC614']
        result = task_func(hex_keys=custom_keys)
        self.assertIsInstance(result, str)
    def test_empty_key_list(self):
        """Test the function with an empty list to check for error handling."""
        with self.assertRaises(IndexError):
            task_func(hex_keys=[])
    def test_invalid_hexadecimal(self):
        """Test the function with an invalid hexadecimal string."""
        invalid_keys = ['ZZZ', '4A0FC614']
        with self.assertRaises(ValueError):
            task_func(hex_keys=invalid_keys)
    def test_consistent_output_with_same_seed(self):
        """Test that the same seed returns the same result."""
        result1 = task_func(seed=99)
        result2 = task_func(seed=99)
        self.assertEqual(result1, result2)
