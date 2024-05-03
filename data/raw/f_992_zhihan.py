import os
import hashlib
import base64

# Constants
PREFIX = 'ME'
SALT_LENGTH = 16

def f_992(password):
    """
    Generate a hashed password from a given string by concatenating it with the prefix "ME," salt it and hash it with SHA256.

    Parameters:
    password (str): The password string.

    Returns:
    str: The hashed password.
    
    Requirements:
    - os
    - hashlib
    - base64

    Example:
    >>> hashed_password = f_992('password')
    >>> print(hashed_password)
    
    Note:
    The function uses the following constants:
    - PREFIX: "ME"
    - SALT_LENGTH: 16
    """
    salt = os.urandom(SALT_LENGTH)
    salted_password = PREFIX + password + salt.hex()
    
    hashed_password = hashlib.sha256(salted_password.encode()).digest()

    return base64.b64encode(hashed_password).decode()

import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        password = "password123"
        hashed_password = f_992(password)
        self.assertNotEqual(password, hashed_password)
        self.assertEqual(len(hashed_password), 44)  # Base64 encoded SHA256 hash is always 44 characters

    def test_case_2(self):
        password = "admin"
        hashed_password = f_992(password)
        self.assertNotEqual(password, hashed_password)
        self.assertEqual(len(hashed_password), 44)

    def test_case_3(self):
        password = "root"
        hashed_password = f_992(password)
        self.assertNotEqual(password, hashed_password)
        self.assertEqual(len(hashed_password), 44)

    def test_case_4(self):
        password = "secret"
        hashed_password = f_992(password)
        self.assertNotEqual(password, hashed_password)
        self.assertEqual(len(hashed_password), 44)

    def test_case_5(self):
        password = "letmein"
        hashed_password = f_992(password)
        self.assertNotEqual(password, hashed_password)
        self.assertEqual(len(hashed_password), 44)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()