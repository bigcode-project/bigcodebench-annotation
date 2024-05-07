import rsa
from cryptography.fernet import Fernet
from base64 import b64encode

def f_324(file_path):
    """
    Generates RSA public and private keys and uses Fernet symmetric encryption to encrypt the contents
    of a specified file. The Fernet key is then encrypted with the public RSA key. The encrypted file
    contents and the encrypted Fernet key are saved in separate files.

    This method demonstrates a hybrid encryption approach where symmetric encryption is used for the file
    contents and asymmetric encryption for the encryption key.

    Parameters:
    file_path (str): The path to the file to be encrypted.

    Returns:
    PublicKey: The RSA public key.
    str: The filename of the encrypted file.
    str: The filename of the file containing the encrypted Fernet key.

    Requirements:
    - rsa
    - cryptography.fernet.Fernet
    - base64.b64encode

    Examples:
    >>> pub_key, encrypted_file, encrypted_key_file = f_324('my_file.txt')
    >>> len(pub_key.save_pkcs1()) > 100
    True
    >>> encrypted_file.endswith('.encrypted')
    True
    >>> encrypted_key_file.endswith('.encrypted')
    True
    """
    (pub_key, priv_key) = rsa.newkeys(512)
    fernet_key = Fernet.generate_key()
    fernet = Fernet(fernet_key)
    with open(file_path, 'rb') as f:
        data = f.read()
        encrypted_data = fernet.encrypt(data)
    encrypted_file = file_path + '.encrypted'
    with open(encrypted_file, 'wb') as f:
        f.write(encrypted_data)
    encrypted_fernet_key = rsa.encrypt(fernet_key, pub_key)
    encrypted_key_file = 'fernet_key.encrypted'
    with open(encrypted_key_file, 'wb') as f:
        f.write(b64encode(encrypted_fernet_key))
    return pub_key, encrypted_file, encrypted_key_file

import unittest
from cryptography.fernet import Fernet
import os
import rsa
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a test file
        self.test_file = 'test_file.txt'
        with open(self.test_file, 'w') as f:
            f.write("This is a test file.")
    def test_file_encryption(self):
        pub_key, encrypted_file, _ = f_324(self.test_file)
        self.assertTrue(os.path.exists(encrypted_file))
    def test_encrypted_key_file_creation(self):
        pub_key, _, encrypted_key_file = f_324(self.test_file)
        self.assertTrue(os.path.exists(encrypted_key_file))
    def test_public_key_type(self):
        pub_key, _, _ = f_324(self.test_file)
        self.assertIsInstance(pub_key, rsa.PublicKey)
    def test_encrypted_file_size(self):
        _, encrypted_file, _ = f_324(self.test_file)
        original_size = os.path.getsize(self.test_file)
        encrypted_size = os.path.getsize(encrypted_file)
        self.assertTrue(encrypted_size > original_size)
    def test_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            f_324("non_existent_file.txt")
    def tearDown(self):
        # Clean up created files
        os.remove(self.test_file)
        encrypted_file = self.test_file + '.encrypted'
        if os.path.exists(encrypted_file):
            os.remove(encrypted_file)
        if os.path.exists('fernet_key.encrypted'):
            os.remove('fernet_key.encrypted')
