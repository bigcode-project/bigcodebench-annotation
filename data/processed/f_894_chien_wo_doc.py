import os
import hashlib

# Constants
DIRECTORY = "./hashed_files"


def f_539(input_string):
    """
    Hash each non-empty line of a multi-line string using SHA256 and save the hashes to files.
    The filename is the first 10 characters of the hash, with a '.txt' extension.

    Parameters:
    - input_string (str): A multi-line string to be processed.

    Returns:
    - list[str]: A list of file paths where the hashes of non-empty lines are saved.

    Requirements:
    - os
    - hashlib

    Notes:
    - If the DIRECTORY does not exist, it is created.
    - Empty lines in the input string are ignored.

    Example:
    >>> file_paths = f_539('line a\nfollows by line b\n\n...bye\n')
    >>> print(file_paths)
    ['./hashed_files/489fe1fa6c.txt', './hashed_files/67009597fe.txt', './hashed_files/eab4758603.txt']
    """
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    file_paths = []
    lines = input_string.split("\n")
    for line in lines:
        if line:  # Check if line is not empty
            line_hash = hashlib.sha256(line.encode()).hexdigest()
            filename = line_hash[:10] + ".txt"
            filepath = os.path.join(DIRECTORY, filename)
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(line_hash)
            file_paths.append(filepath)

    return file_paths

import unittest
import os
import hashlib
import shutil
class TestCases(unittest.TestCase):
    """Tests for the function f_539."""
    def setUp(self):
        """Set up a temporary directory for test files."""
        self.temp_directory = "./temp_test_files"
        os.makedirs(self.temp_directory, exist_ok=True)
    def tearDown(self):
        """Clean up by removing the temporary directory after tests."""
        shutil.rmtree(self.temp_directory)
        dirs_to_remove = ["hashed_files"]
        for dir_path in dirs_to_remove:
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)
    def test_single_line(self):
        """Test with a single line input."""
        input_string = "Hello world"
        expected = [os.path.join("./hashed_files", "64ec88ca00.txt")]
        result = f_539(input_string)
        self.assertEqual(result, expected)
    def test_multi_line(self):
        """Test with a multi-line input."""
        input_string = "First line\nSecond line\nThird line"
        expected = [
            os.path.join("./hashed_files", "2361df1018.txt"),
            os.path.join("./hashed_files", "c8b588f708.txt"),
            os.path.join("./hashed_files", "3195807ae4.txt"),
        ]
        result = f_539(input_string)
        self.assertEqual(result, expected)
    def test_empty_input(self):
        """Test with an empty string."""
        input_string = ""
        expected = []
        result = f_539(input_string)
        self.assertEqual(result, expected)
    def test_input_with_empty_lines(self):
        """Test input string containing empty lines."""
        input_string = "Line one\n\nLine two\n"
        expected = [
            os.path.join("./hashed_files", "209f4c0be3.txt"),
            os.path.join("./hashed_files", "1ae5466eb8.txt"),
        ]
        result = f_539(input_string)
        self.assertEqual(result, expected)
    def test_no_newline_at_end(self):
        """Test input string without a newline at the end."""
        input_string = "Line with no newline at end"
        expected = [os.path.join("./hashed_files", "901dd863e9.txt")]
        result = f_539(input_string)
        self.assertEqual(result, expected)
    def test_directory_creation(self):
        """
        Test if the function creates the directory if it does not exist.
        """
        # Assert that the DIRECTORY does not exist before calling the function
        self.assertFalse(os.path.exists(DIRECTORY))
        # Call the function with any string
        f_539("Test for directory creation")
        # Check if the DIRECTORY has been created
        self.assertTrue(os.path.exists(DIRECTORY))
        # Optionally, clean up by removing the created directory after the test
        if os.path.exists(DIRECTORY):
            shutil.rmtree(DIRECTORY)
