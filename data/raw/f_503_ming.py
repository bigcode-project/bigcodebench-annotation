import re
import os
import hashlib
import binascii
# Set DATA_DIR to the 'data' subdirectory in the current script's directory
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

def f_503(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    """
    Searches for files within the specified directory matching a given regex pattern
    and computes a SHA256 hash of each file's content.

    Parameters:
    - directory (str): Directory to search for files.
    - pattern (str): Regex pattern that filenames must match. Default pattern matches 'AcroTray.exe'.

    Returns:
    - dict: A dictionary with file paths as keys and their SHA256 hashes as values.

    Requirements:
    - re: For regex matching.
    - os: For walking through the directory.
    - hashlib: For computing SHA256 hashes.
    - binascii: For converting hash bytes to hexadecimal string.

    Example:
    >>> f_503("/path/to/directory")
    {'/path/to/directory/AcroTray.exe': 'abc123...'}
    """
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if re.search(pattern, file):
                path = os.path.join(root, file)
                with open(path, 'rb') as f:
                    data = f.read()
                    hash_digest = hashlib.sha256(data).digest()
                    hashes[path] = binascii.hexlify(hash_digest).decode()
    return hashes


import unittest
import tempfile
import shutil
import os

class TestF503(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_dir = DATA_DIR
        if not os.path.exists(cls.test_dir):
            os.makedirs(cls.test_dir)

        # Create a test file within the test_dir
        cls.test_file = os.path.join(cls.test_dir, "AcroTray.exe")
        with open(cls.test_file, 'wb') as f:
            f.write(b"Dummy content for testing.")

    @classmethod
    def tearDownClass(cls):
        # Clean up by removing the test directory and its contents
        shutil.rmtree(cls.test_dir, ignore_errors=True)

    def test_matching_file(self):
        """Ensure the method correctly identifies and hashes a matching file."""
        # Use the directory, not the file path, and adjust the pattern if necessary.
        result = f_503(self.test_dir, r"AcroTray\.exe$")

        # Verify that the file's full path is included in the results
        self.assertIn(self.test_file, result.keys(), "The file should be found and hashed.")

        # Optionally, verify the correctness of the hash value for added robustness.
        # Compute the expected hash for comparison
        with open(self.test_file, 'rb') as file:
            data = file.read()
            expected_hash = hashlib.sha256(data).hexdigest()

        self.assertEqual(result[self.test_file], expected_hash, "The hash value should match the expected hash.")

    def test_no_matching_file(self):
        """Test directory with no files matching the pattern."""
        no_match_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, no_match_dir)  # Ensure cleanup
        result = f_503(no_match_dir)
        self.assertEqual(len(result), 0)

    def test_empty_directory(self):
        """Test an empty directory."""
        empty_dir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, empty_dir)  # Ensure cleanup
        result = f_503(empty_dir)
        self.assertEqual(len(result), 0)

    def test_hash_correctness(self):
        """Verify that the SHA256 hash is correctly computed."""
        # Adjust the call to search within the test directory and specify a pattern that matches the test file
        pattern = "AcroTray\.exe$"  # Simplified pattern to match the filename directly
        result = f_503(self.test_dir, pattern)

        # Construct the expected key as it would appear in the result
        expected_key = self.test_file

        # Ensure the file was matched and the hash is present in the results
        self.assertIn(expected_key, result)

        hash_value = result[expected_key]
        # Compute the expected hash for comparison
        with open(self.test_file, 'rb') as f:
            data = f.read()
            expected_hash = hashlib.sha256(data).hexdigest()

        self.assertEqual(hash_value, expected_hash)

    def test_custom_pattern(self):
        """Test functionality with a custom pattern that does not match any file."""
        custom_pattern = r"non_matching_pattern\.exe$"
        result = f_503(self.test_file, custom_pattern)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
