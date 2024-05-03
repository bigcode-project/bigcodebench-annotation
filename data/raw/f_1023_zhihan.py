import base64
import hashlib
import os


def f_1023(password, salt_length=32):
    """
    Generates a secure hash for a given password using the PBKDF2 (Password-Based Key Derivation Function 2) hashing algorithm,
    along with a randomly generated salt. Both the salt and the hashed password are then encoded using base64 for safe storage or transmission.

    The PBKDF2 algorithm is designed to be computationally intensive, making it difficult to perform brute-force attacks on the hashed password.
    This function uses the SHA-256 hash function as part of the PBKDF2 algorithm to provide a secure way of storing or verifying passwords.

    Parameters:
    - password (str): The plaintext password to hash.
    - salt_length (int, optional): The length of the salt in bytes. Defaults to 32.

    Returns:
    - tuple of (bytes, bytes): A tuple containing two base64 encoded bytes objects:
        1. The randomly generated salt.
        2. The hashed password.

    Requirements:
    - base64
    - hashlib
    - os
    - binascii

    Example:
    >>> salt, hashed_password = f_1023('my_password')
    >>> print(salt.decode(), hashed_password.decode())
    hRzZgbVhR3z0dismVQYOexLZsPR3Gj90pD949nWXTMA= zbO14FBUGA7OSRj3zlxzaFqZpLYaejPeaOGxEOi9FVk=
    >>> salt, hashed_password = f_1023('1234', 4)
    >>> print(salt.decode(), hashed_password.decode())
    hn1Diw== PAuFwOR4yId72mMU55wdPV25SacA3sUAzXQcfZHGz6Y=
    """
    salt = os.urandom(salt_length)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return base64.b64encode(salt), base64.b64encode(hashed_password)


import unittest
import base64
import hashlib


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
