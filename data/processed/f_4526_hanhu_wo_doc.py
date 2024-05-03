import rsa
import os
import zipfile
from base64 import b64encode

def f_412(directory):
    """
    Generates RSA public and private keys, encrypts all files in the specified directory using the public key,
    and saves the encrypted files into a zip file. It returns the public key and the name of the zip file.

    Note: This method directly encrypts file data with RSA, which is not recommended for large files or
    production use. Typically, RSA is used to encrypt a symmetric key (like AES), which is then used to
    encrypt the actual data.

    Parameters:
    directory (str): The directory containing the files to be encrypted.

    Returns:
    rsa.PublicKey: The RSA public key.
    str: The filename of the zip file containing the encrypted files.

    Requirements:
    - rsa
    - os
    - zipfile
    - base64.b64encode

    Examples:
    >>> pub_key, zipfile_name = f_412('./')
    >>> isinstance(pub_key, rsa.PublicKey)
    'True'
    >>> isinstance(zipfile_name, str)
    'True'
    """
    (pub_key, priv_key) = rsa.newkeys(512)
    zipfile_name = 'encrypted_files.zip'

    with zipfile.ZipFile(zipfile_name, 'w') as zipf:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'rb') as f:
                    data = f.read()
                    encrypted_data = rsa.encrypt(data, pub_key)
                    zipf.writestr(filename, b64encode(encrypted_data).decode('utf-8'))

    return pub_key, zipfile_name

import rsa
import os
import zipfile
from base64 import b64encode
import unittest
import tempfile
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)
        # Remove created zip file
        if os.path.exists('encrypted_files.zip'):
            os.remove('encrypted_files.zip')
    def test_return_type(self):
        # Creating test files
        for i in range(2):
            with open(os.path.join(self.test_dir, f"file{i}.txt"), 'w') as f:
                f.write("Sample content")
        pub_key, zipfile_name = f_412(self.test_dir)
        self.assertIsInstance(pub_key, rsa.PublicKey)
        self.assertIsInstance(zipfile_name, str)
    def test_zipfile_creation(self):
        # Creating test files
        for i in range(2):
            with open(os.path.join(self.test_dir, f"file{i}.txt"), 'w') as f:
                f.write("Sample content")
        _, zipfile_name = f_412(self.test_dir)
        self.assertTrue(os.path.exists(zipfile_name))
        with zipfile.ZipFile(zipfile_name, 'r') as zipf:
            self.assertEqual(len(zipf.namelist()), 2)
    def test_empty_directory(self):
        # No files created in the setup for this test
        _, zipfile_name = f_412(self.test_dir)
        with zipfile.ZipFile(zipfile_name, 'r') as zipf:
            self.assertEqual(len(zipf.namelist()), 0)
    def test_file_encryption_contents(self):
        # Creating a single test file
        test_file_path = os.path.join(self.test_dir, "test_file.txt")
        with open(test_file_path, 'w') as f:
            f.write("Sample content")
        pub_key, zipfile_name = f_412(self.test_dir)
        with zipfile.ZipFile(zipfile_name, 'r') as zipf:
            encrypted_content = zipf.read(os.path.basename(test_file_path))
            # Read the content to ensure it is encrypted and not plain text
            self.assertNotEqual(b64encode(b"Sample content").decode('utf-8'), encrypted_content)
