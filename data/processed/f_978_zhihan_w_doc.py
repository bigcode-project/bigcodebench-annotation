import codecs
import random
import string
import hashlib

def f_785(password_length=10, salt="salty"):
    """
    Generate a random password of a specified length, including Latin characters, numbers, and symbols. 
    Then, hash the password using the SHA256 algorithm after mixing it with a specified salt.
    
    Parameters:
    - password_length (int, optional): Length of the generated password. Defaults to 10.
    - salt (str, optional): Salt to be added to the password before hashing. Defaults to "salty".
    
    Returns:
    str: The hashed password.
    
    Requirements:
    - codecs
    - random
    - string
    - hashlib
    
    Example:
    >>> random.seed(0)
    >>> hashed_password = f_785(12, "my_salt")
    >>> print(hashed_password)
    a706478dc5969e90dcfc2fbaffff0b9f8e7f2b006002edac13cb17f5bf9ba941
    """
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for i in range(password_length))
    password = codecs.encode(password, 'latin-1').decode('utf-8')
    salted_password = (password + salt).encode('utf-8')
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return hashed_password

import unittest
import codecs
import random
import string
import hashlib
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with default parameters
        random.seed(0)
        hashed_password = f_785()
        self.assertEqual(len(hashed_password), 64)  # SHA256 produces a 64-character long hash
    def test_case_2(self):
        # Testing with custom password length but default salt
        random.seed(0)
        hashed_password = f_785(15)
        self.assertEqual(len(hashed_password), 64)
    def test_case_3(self):
        # Testing with default password length but custom salt
        random.seed(0)
        hashed_password = f_785(salt="custom_salt")
        self.assertEqual(len(hashed_password), 64)
    def test_case_4(self):
        # Testing with both custom password length and salt
        random.seed(0)
        hashed_password = f_785(20, "another_salt")
        self.assertEqual(len(hashed_password), 64)
    def test_case_5(self):
        # Testing with edge value for password length (e.g., very small value)
        random.seed(0)
        hashed_password = f_785(1)
        self.assertEqual(len(hashed_password), 64)
