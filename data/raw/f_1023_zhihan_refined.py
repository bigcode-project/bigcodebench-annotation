import base64
import hashlib
import os

def f_1023(password, SALT_LENGTH = 32):
    """
    Hashes a password using the PBKDF2 HMAC algorithm with SHA-256 as the hashing algorithm, 
    combined with a randomly generated salt, and returns both the salt and the hashed password, 
    each base64-encoded.

    Parameters:
    password (str): The password to be hashed.
    SALT_LENGTH (int): the length of the randomly generated salt.

    Returns:
    tuple[bytes, bytes]: A tuple containing the base64-encoded salt and the base64-encoded hashed password as byte strings.

    Raises:
    ValueError if the password is None or empty

    Requirements:
    - base64
    - hashlib
    - os

    Example:
    >>> salt, hashed_password = f_1023('my_password')
    >>> isinstance(salt, bytes)
    True
    >>> isinstance(hashed_password, bytes)
    True
    """
    if not password:
        raise ValueError
    salt = os.urandom(SALT_LENGTH)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return base64.b64encode(salt), base64.b64encode(hashed_password)

import unittest
import base64
import hashlib
import os

class TestCases(unittest.TestCase):

    def decode_and_regenerate_password(self, encoded_salt, encoded_hashed_password, original_password):
        """ Helper function to decode base64 encoded salt and password, and regenerate the hashed password. """
        decoded_salt = base64.b64decode(encoded_salt)
        decoded_hashed_password = base64.b64decode(encoded_hashed_password)
        regenerated_hashed_password = hashlib.pbkdf2_hmac('sha256', original_password.encode(), decoded_salt, 100000)
        return regenerated_hashed_password, decoded_hashed_password

    def test_case_1(self):
        """ Testing with a simple password """
        salt, hashed_password = f_1023('password123')
        self.assertTrue(isinstance(salt, bytes) and isinstance(hashed_password, bytes))
        regenerated, original = self.decode_and_regenerate_password(salt, hashed_password, 'password123')
        self.assertEqual(regenerated, original)

    def test_case_2(self):
        """ Testing with a password containing special characters """
        salt, hashed_password = f_1023('p@ssw0rd$%^&*')
        self.assertTrue(isinstance(salt, bytes) and isinstance(hashed_password, bytes))
        regenerated, original = self.decode_and_regenerate_password(salt, hashed_password, 'p@ssw0rd$%^&*')
        self.assertEqual(regenerated, original)

    def test_case_3(self):
        """ Testing with a long password """
        long_password = 'a' * 1000
        salt, hashed_password = f_1023(long_password)
        self.assertTrue(isinstance(salt, bytes) and isinstance(hashed_password, bytes))
        regenerated, original = self.decode_and_regenerate_password(salt, hashed_password, long_password)
        self.assertEqual(regenerated, original)

    def test_case_4(self):
        """ Testing with a short password """
        short_password = 'a'
        salt, hashed_password = f_1023(short_password)
        self.assertTrue(isinstance(salt, bytes) and isinstance(hashed_password, bytes))
        regenerated, original = self.decode_and_regenerate_password(salt, hashed_password, short_password)
        self.assertEqual(regenerated, original)

    def test_case_5(self):
        """ Testing with a password that is a number """
        number_password = '1234567890'
        salt, hashed_password = f_1023(number_password)
        self.assertTrue(isinstance(salt, bytes) and isinstance(hashed_password, bytes))
        regenerated, original = self.decode_and_regenerate_password(salt, hashed_password, number_password)
        self.assertEqual(regenerated, original)

    def test_invalid_input(self):
        """ Testing with invalid input such as None or empty string """
        with self.assertRaises(ValueError):
            f_1023(None)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()