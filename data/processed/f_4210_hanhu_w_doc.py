import numpy as np
import secrets
import hashlib
import base64

def f_396(num, from_base, to_base, alphabet):
    """
    Converts a number from one base to another, adds a random salt, hashes the result using SHA-256,
    and then encodes the hash in base64 using a custom alphabet. The function also returns the used salt.

    Parameters:
    num (str): The number to be converted, represented as a string.
    from_base (int): The base of the number to be converted.
    to_base (int): The base to convert the number to.
    alphabet (str): The custom alphabet to be used for base64 encoding. Each character in the provided alphabet
        represents a value in the base64 encoding scheme. For example, the standard base64 alphabet is:
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".
        The function uses this alphabet to encode the hash of the converted number. The length of the alphabet
        determines the possible characters in the resulting base64-encoded hash.

    Returns:
    tuple: A tuple containing the base64-encoded hash of the converted number and the used salt.

    Raises:
    ValueError: If `from_base` or `to_base` is less than 2, indicating an invalid base for conversion.
    ValueError: If the `num` string contains characters not valid in the `from_base` specified, indicating an invalid number format for conversion.

    Requirements:
    - numpy
    - secrets
    - hashlib
    - base64

    Examples:
    Convert a hexadecimal number to octal, hash it using SHA-256, and return the base64-encoded hash and salt using a custom alphabet.
    >>> alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    >>> encoded, salt = f_396('A1', 16, 8, alphabet)
    >>> isinstance(encoded, str) and isinstance(salt, str)
    True

    Verify that different invocations produce different results due to the random salt.
    >>> result1, salt1 = f_396('FF', 16, 8, alphabet)
    >>> result2, salt2 = f_396('FF', 16, 8, alphabet)
    >>> result1 != result2
    True
    """
    base64_table = np.array(list(alphabet))
    n = int(num, from_base)
    new_num = ''
    if to_base < 2:
        raise ValueError("to_base must be >= 2.")
    while n > 0:
        n, m = divmod(n, to_base)
        new_num += base64_table[m]
    num = new_num[::-1]
    salt = secrets.token_hex(16)
    hashed_num = hashlib.pbkdf2_hmac('sha256', bytes(num, 'utf-8'), bytes(salt, 'utf-8'), 100000)
    base64_encoded = base64.b64encode(hashed_num)
    return base64_encoded.decode(), salt

import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        # Define the alphabet in the setUp method to be reused in all tests
        self.alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    
    def test_base_conversion_and_hashing(self):
        encoded, salt = f_396('A1', 16, 8, self.alphabet)
        self.assertTrue(isinstance(encoded, str))
        self.assertTrue(isinstance(salt, str))
    def test_different_salts_different_hashes(self):
        result1, salt1 = f_396('FF', 16, 8, self.alphabet)
        result2, salt2 = f_396('FF', 16, 8, self.alphabet)
        self.assertNotEqual(result1, result2)
    def test_invalid_number_format(self):
        with self.assertRaises(ValueError):
            f_396('G', 16, 8, self.alphabet)
    def test_invalid_from_base(self):
        with self.assertRaises(ValueError):
            f_396('10', 1, 8, self.alphabet)
    def test_invalid_to_base(self):
        with self.assertRaises(ValueError):
            f_396('10', 10, 1, self.alphabet)
