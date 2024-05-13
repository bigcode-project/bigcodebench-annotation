import struct
import random

# Constants
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_key=None):
    """
    Generate a random float number from a list of hexadecimal strings and then round the float number to 2 decimal places.

    Parameters:
    - None

    Returns:
    - rounded_float (float): The rounded float number.

    Requirements:
    - struct
    - random

    Example:
    >>> random.seed(42)
    >>> print(repr(f"{task_func():.1f}"))
    '36806.1'

    """

    if hex_key is None:
        hex_key = random.choice(KEYS)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    rounded_float = round(float_num, 2)
    return rounded_float

import unittest
class TestCases(unittest.TestCase):
    
    def test_return_type(self):
        result = task_func()
        self.assertIsInstance(result, float)
    def test_rounded_two_decimal(self):
        result = task_func()
        decimal_part = str(result).split('.')[1]
        self.assertTrue(len(decimal_part) <= 2)
    def test_randomness(self):
        random.seed()  # Reset the seed to ensure randomness
        results = {task_func() for _ in range(100)}
        self.assertTrue(len(results) > 1)
    def test_specific_hex_keys(self):
        for hex_key in KEYS:
            expected_result = round(struct.unpack('!f', bytes.fromhex(hex_key))[0], 2)
            result = task_func(hex_key)
            self.assertEqual(result, expected_result)
    def test_no_seed(self):
        random.seed()  # Reset the random seed
        results = {task_func() for _ in range(100)}
        self.assertTrue(len(results) > 1)
