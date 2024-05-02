import hashlib
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']


def f_329(hex_keys=KEYS, seed=42):
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
    >>> f_329(['1a2b3c4d', '5e6f7g8h'])
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
    def test_case_1(self):
        result = f_329(['1a2b3c4d', '5e6f7g8h'])
        self.assertEqual(result, '426614caa490f2c185aebf58f1d4adac')
    def test_case_2(self):
        result = f_329()
        self.assertEqual(result, 'aa1f8c53e0aee57fccd07b90a902579a')
    def test_case_3(self):
        result = f_329(['12121212', '34343434'])
        self.assertEqual(result, 'b523721fccb8fe2e7bf999e74e25056f')
    def test_case_4(self):
        result = f_329(['1VVVVVVV', '3VVVVVVV', 'F3fF3fF3'])
        self.assertEqual(result, 'fae7b34f299d23a584fbc19c2fcdf865')
    def test_case_5(self):
        # test error message
        with self.assertRaises(ValueError):
            f_329(['1a2b3c4d', '5e6f7g8h', 'invalid_hex'])
