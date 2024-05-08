import os
import hashlib
import base64

def f_652(password, PREFIX="ME", SALT_LENGTH=16):
    """
    Generates a hashed password by concatenating a given password with a prefix and a generated salt,
    and then hashing the combined string using SHA256. The hashed result is then encoded in base64.

    Parameters:
    - password (str): The password string to hash.
    - PREFIX (str): A prefix added to the password before hashing. Defaults to "ME".
    - SALT_LENGTH (int): The byte length of the random salt to be generated. Defaults to 16.

    Returns:
    - str: The base64 encoded SHA256 hash of the password concatenated with the prefix and salt.

    Raises:
    ValueError if the SALT_LENGTH is negative

    Requirements:
    - os
    - hashlib
    - base64

    Example:
    >>> hashed_password = f_652('password123', 'ME', 16)
    >>> isinstance(hashed_password, str)
    True
    """
    if SALT_LENGTH < 0:
        raise ValueError
    salt = os.urandom(SALT_LENGTH)
    salted_password = PREFIX + password + salt.hex()
    hashed_password = hashlib.sha256(salted_password.encode()).digest()
    return base64.b64encode(hashed_password).decode()

import unittest
from unittest.mock import patch
import base64
import hashlib
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a predictable random generator for consistent testing
        self.expected_salt = bytes([i%256 for i in range(16)])  # a repeatable "random" byte sequence
        self.patcher = patch('os.urandom', return_value=self.expected_salt)
        self.mock_urandom = self.patcher.start()
    def tearDown(self):
        # Stop patching 'os.urandom'
        self.patcher.stop()
    def test_consistent_hashing(self):
        password = "consistent"
        hashed_password1 = f_652(password, "ME", 16)
        hashed_password2 = f_652(password, "ME", 16)
        self.assertEqual(hashed_password1, hashed_password2)
    def test_different_prefix_and_salt_length(self):
        """ Test hashing with different prefixes and salt lengths """
        password = "password123"
        prefix1 = "ME"
        prefix2 = "YOU"
        hashed_password1 = f_652(password, prefix1, 16)
        hashed_password2 = f_652(password, prefix2, 32)
        self.assertNotEqual(hashed_password1, hashed_password2)
    def test_hash_length(self):
        """ Ensure the hashed password is always 44 characters """
        password = "variableLength"
        hashed_password = f_652(password)
        self.assertEqual(len(hashed_password), 44)
        self.assertIsInstance(hashed_password, str)
    def test_invalid_inputs(self):
        """ Test function behavior with invalid inputs """
        with self.assertRaises(TypeError):
            f_652(None)  # Passing None as password
        with self.assertRaises(TypeError):
            f_652("password", PREFIX=123)  # Non-string prefix
        with self.assertRaises(ValueError):
            f_652("password", SALT_LENGTH=-1)  # Invalid salt length
    def test_empty_password(self):
        """ Test hashing an empty string """
        hashed_password = f_652("", "ME", 16)
        expected_hash = hashlib.sha256(("ME" + "" + self.expected_salt.hex()).encode()).digest()
        expected_output = base64.b64encode(expected_hash).decode()
        self.assertEqual(hashed_password, expected_output)
    def test_special_characters_in_password(self):
        """ Test passwords that include special characters """
        special_password = "!@#$%^&*()_+{}:>?<"
        hashed_password = f_652(special_password, "ME", 16)
        expected_hash = hashlib.sha256(("ME" + special_password + self.expected_salt.hex()).encode()).digest()
        expected_output = base64.b64encode(expected_hash).decode()
        self.assertEqual(hashed_password, expected_output)
    def test_long_password(self):
        """ Test with an unusually long password """
        long_password = "x" * 1000  # A very long password
        hashed_password = f_652(long_password, "ME", 16)
        expected_hash = hashlib.sha256(("ME" + long_password + self.expected_salt.hex()).encode()).digest()
        expected_output = base64.b64encode(expected_hash).decode()
        self.assertEqual(hashed_password, expected_output)
    def test_hash_with_different_salts(self):
        """ Ensure different salts result in different hashes """
        password = "password"
        salt1 = bytes([i%256 for i in range(16)])
        salt2 = bytes([(i+1)%256 for i in range(16)])  # Slightly different salt
        with patch('os.urandom', return_value=salt1):
            hashed1 = f_652(password, "ME", 16)
        with patch('os.urandom', return_value=salt2):
            hashed2 = f_652(password, "ME", 16)
        self.assertNotEqual(hashed1, hashed2, "Different salts should result in different hashes")
    def test_deterministic_output_with_fixed_salt(self):
        """ Verify that the same salt and input always produces the same hash """
        password = "consistentOutput"
        prefix = "ME"
        hashed_password = f_652(password, prefix, 16)
        expected_hash = hashlib.sha256((prefix + password + self.expected_salt.hex()).encode()).digest()
        expected_output = base64.b64encode(expected_hash).decode()
        self.assertEqual(hashed_password, expected_output)
