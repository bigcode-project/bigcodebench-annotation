import hashlib
import base64


def f_35(filename, data, password):
    """
    Encrypt a string with a password, then write the encrypted string to a file. 
    If the file does not exist, create it.

    Parameters:
    filename (str): The name of the file to write to.
    data (str): The string to encrypt and write to the file.
    password (str): The password to use for encryption.

    Returns:
    str: The encrypted string.

    Requirements:
    - hashlib
    - base64

    Example:
    >>> f_35('test.txt', 'Hello, World!', 'password')
    'Fu0k9LUEJCY+ookLrA=='
    """
    try:
        open(filename, 'x').close()
    except FileExistsError:
        pass
    key = hashlib.sha256(password.encode()).digest()
    encrypted_bytes = [byte ^ key[i % len(key)] for i, byte in enumerate(data.encode())]
    encrypted = base64.b64encode(bytes(encrypted_bytes)).decode()
    with open(filename, 'w') as f:
        f.write(encrypted)
    return encrypted

import unittest
import os
import shutil
output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
class TestCases(unittest.TestCase):
    def tearDown(self):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        # if os.path.exists(FILE_PATH):
        #     os.remove(FILE_PATH)
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir)
    def test_case_1(self):
        # Testing basic encryption and file write
        file1 = os.path.join(output_dir, 'test1.txt')
        encrypted = f_35(file1, 'Hello, World!', 'password123')
        with open(file1, 'r') as f:
            file_content = f.read()
        self.assertEqual(encrypted, file_content)
        
    def test_case_2(self):
        # Testing with different data and password
        file2 = os.path.join(output_dir, 'test2.txt')
        encrypted = f_35(file2, 'OpenAI', 'secret')
        with open(file2, 'r') as f:
            file_content = f.read()
        self.assertEqual(encrypted, file_content)
        
    def test_case_3(self):
        # Testing with special characters in data and password
        file3 = os.path.join(output_dir, 'test3.txt')
        data = '!@#$%^&*()_+'
        password = 'special_chars'
        encrypted = f_35(file3, data, password)
        with open(file3, 'r') as f:
            file_content = f.read()
        self.assertEqual(encrypted, file_content)
        
    def test_case_4(self):
        # Testing file creation if it doesn't exist
        file4 = os.path.join(output_dir, 'nonexistent_file.txt')
        if os.path.exists(file4):
            os.remove(file4)
        encrypted = f_35(file4, 'Test Data', 'pwd')
        self.assertTrue(os.path.exists(file4))
        
    def test_case_5(self):
        # Testing decryption to ensure encryption is reversible
        file5 = os.path.join(output_dir, 'test5.txt')
        data = 'Decryption Test'
        password = 'decrypt_pwd'
        encrypted = f_35(file5, data, password)
        
        # Decryption logic (reverse of encryption)
        key = hashlib.sha256(password.encode()).digest()
        decrypted_bytes = [byte ^ key[i % len(key)] for i, byte in enumerate(base64.b64decode(encrypted))]
        decrypted = bytes(decrypted_bytes).decode()
        
        self.assertEqual(data, decrypted)
