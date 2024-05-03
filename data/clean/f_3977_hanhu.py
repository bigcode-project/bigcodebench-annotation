import hashlib
import rsa
import base64


def f_3979(file_path):
    """
    Generates a signed hash of a file's contents using RSA encryption. The file's contents are hashed using SHA-256,
    and then the hash is signed with a private RSA key stored in 'private.pem'. The signed hash is encoded in base64.

    Parameters:
    file_path (str): The path to the file whose contents are to be signed.

    Returns:
    str: The base64 encoded signed hash of the file.

    Requirements:
    - hashlib
    - rsa
    - base64

    Examples:
    Assuming 'example.txt' contains some text and a valid 'private.pem' is present,
    >>> len(f_3979('example.txt')) > 0
    True

    Assuming 'empty.txt' is an empty file and a valid 'private.pem' is present,
    >>> len(f_3979('empty.txt')) > 0
    True
    """
    with open(file_path, 'rb') as f:
        content = f.read()

    hash_output = hashlib.sha256(content).digest()

    with open('private.pem', 'rb') as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())
    signature = rsa.sign(hash_output, private_key, 'SHA-256')

    return base64.b64encode(signature).decode('utf-8')

import unittest
import os
import rsa
import base64
from unittest.mock import patch

class TestCases(unittest.TestCase):

    @classmethod
    def setUp(self):
        """Set up test environment: create necessary files with mock content."""
        with open('example.txt', 'w') as f:
            f.write('This is a test file.')
        with open('empty.txt', 'w') as f:
            f.write('')  # Empty file

        # Generate a test RSA key pair
        (pub_key, priv_key) = rsa.newkeys(512)
        with open('private.pem', 'wb') as f:
            f.write(priv_key.save_pkcs1('PEM'))
        
        # Create an intentionally invalid private key file
        with open('invalid_private.pem', 'w') as f:
            f.write('Invalid key content')

    def tearDown(self):
        """Clean up by removing the files created for the test."""
        for filename in ['example.txt', 'empty.txt', 'private.pem', 'invalid_private.pem']:
            if os.path.exists(filename):
                os.remove(filename)

    def test_signed_hash_of_file(self):
        """Ensure a non-empty signature is produced for a file with content."""
        result = f_3979('example.txt')
        self.assertTrue(len(result) > 0)

    def test_signed_hash_of_empty_file(self):
        """Ensure a non-empty signature is produced for an empty file."""
        result = f_3979('empty.txt')
        self.assertTrue(len(result) > 0)

    def test_file_not_exist(self):
        """Verify FileNotFoundError is raised for non-existent file paths."""
        with self.assertRaises(FileNotFoundError):
            f_3979('nonexistent.txt')

    def test_invalid_private_key_format(self):
        """Test that an invalid private key format raises ValueError."""
        # Temporarily replace the valid key with an invalid one for this test
        os.rename('private.pem', 'temp_private.pem')
        os.rename('invalid_private.pem', 'private.pem')
        try:
            with self.assertRaises(ValueError):
                f_3979('example.txt')
        finally:
            # Ensure cleanup happens correctly
            os.rename('private.pem', 'invalid_private.pem')
            os.rename('temp_private.pem', 'private.pem')

    def test_different_files_same_key(self):
        """Ensure different files produce different signatures using the same key."""
        # Assuming another_example.txt exists and contains different content
        if os.path.exists('another_example.txt'):
            hash1 = f_3979('example.txt')
            hash2 = f_3979('another_example.txt')
            self.assertNotEqual(hash1, hash2)

    @patch('rsa.sign', side_effect=rsa.pkcs1.VerificationError("Mocked verification error"))
    def test_rsa_verification_error_handling(self, mock_sign):
        """Test that rsa.pkcs1.VerificationError is correctly handled within the signing process."""
        with self.assertRaises(rsa.pkcs1.VerificationError):
            f_3979('example.txt')


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
