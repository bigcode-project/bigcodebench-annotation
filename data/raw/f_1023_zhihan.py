import base64
import hashlib
import os


# Constants
SALT_LENGTH = 32

def f_1023(password):
    """
    Hash a password with the PBKDF2 algorithm and encode both the salt and the hashed password with base64.

    Parameters:
    password (str): The password to be hashed.

    Returns:
    tuple: A tuple containing the base64 encoded salt and hashed password.

    Requirements:
    - base64
    - hashlib
    - os
    - binascii

    Example:
    >>> salt, hashed_password = f_1023('my_password')
    >>> print(salt, hashed_password)
    """
    salt = os.urandom(SALT_LENGTH)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return base64.b64encode(salt), base64.b64encode(hashed_password)

import unittest
import base64
import hashlib

# Load the refined function for testing
exec(open('/mnt/data/refined_function.py').read())

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Testing with a simple password
        salt, hashed_password = f_1023('password123')
        self.assertTrue(isinstance(salt, bytes))
        self.assertTrue(isinstance(hashed_password, bytes))
        # Ensure it's a valid base64 encoded string
        decoded_salt = base64.b64decode(salt)
        decoded_hashed_password = base64.b64decode(hashed_password)
        # Verify that the hashed password matches when regenerated
        regenerated_hashed_password = hashlib.pbkdf2_hmac('sha256', 'password123'.encode(), decoded_salt, 100000)
        self.assertEqual(regenerated_hashed_password, decoded_hashed_password)

    def test_case_2(self):
        # Testing with a password containing special characters
        salt, hashed_password = f_1023('p@ssw0rd$%^&*')
        self.assertTrue(isinstance(salt, bytes))
        self.assertTrue(isinstance(hashed_password, bytes))
        decoded_salt = base64.b64decode(salt)
        decoded_hashed_password = base64.b64decode(hashed_password)
        regenerated_hashed_password = hashlib.pbkdf2_hmac('sha256', 'p@ssw0rd$%^&*'.encode(), decoded_salt, 100000)
        self.assertEqual(regenerated_hashed_password, decoded_hashed_password)

    def test_case_3(self):
        # Testing with a long password
        long_password = 'a' * 1000
        salt, hashed_password = f_1023(long_password)
        self.assertTrue(isinstance(salt, bytes))
        self.assertTrue(isinstance(hashed_password, bytes))
        decoded_salt = base64.b64decode(salt)
        decoded_hashed_password = base64.b64decode(hashed_password)
        regenerated_hashed_password = hashlib.pbkdf2_hmac('sha256', long_password.encode(), decoded_salt, 100000)
        self.assertEqual(regenerated_hashed_password, decoded_hashed_password)

    def test_case_4(self):
        # Testing with a short password
        short_password = 'a'
        salt, hashed_password = f_1023(short_password)
        self.assertTrue(isinstance(salt, bytes))
        self.assertTrue(isinstance(hashed_password, bytes))
        decoded_salt = base64.b64decode(salt)
        decoded_hashed_password = base64.b64decode(hashed_password)
        regenerated_hashed_password = hashlib.pbkdf2_hmac('sha256', short_password.encode(), decoded_salt, 100000)
        self.assertEqual(regenerated_hashed_password, decoded_hashed_password)

    def test_case_5(self):
        # Testing with a password that is a number
        number_password = '1234567890'
        salt, hashed_password = f_1023(number_password)
        self.assertTrue(isinstance(salt, bytes))
        self.assertTrue(isinstance(hashed_password, bytes))
        decoded_salt = base64.b64decode(salt)
        decoded_hashed_password = base64.b64decode(hashed_password)
        regenerated_hashed_password = hashlib.pbkdf2_hmac('sha256', number_password.encode(), decoded_salt, 100000)
        self.assertEqual(regenerated_hashed_password, decoded_hashed_password)
if __name__ == "__main__":
    run_tests()