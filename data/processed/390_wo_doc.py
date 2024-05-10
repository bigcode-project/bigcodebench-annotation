import re
import os
import shutil


def task_func(directory):
    """
    Find the files with filenames that contain "like" or "what" in a directory, create a new subdirectory called "Interesting Files" 
    and move those files to the new subdirectory.

    Parameters:
    directory (str): The directory path.

    Returns:
    List of files moved

    Requirements:
    - re
    - os
    - shutil

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()
    >>> files = ['file_with_like.txt', 'another_file_with_what.doc', 'file_without_keywords.jpg', 'hidden_what_in_name.whatever']
    >>> for file in files:
    ...     with open(os.path.join(temp_dir, file), 'w') as f:
    ...         _ = f.write("Dummy content for testing.")
    >>> task_func(temp_dir)
    ['another_file_with_what.doc', 'hidden_what_in_name.whatever', 'file_with_like.txt']
    """
    pattern = re.compile(r'(like|what)', re.IGNORECASE)
    interesting_files = [file for file in os.listdir(directory) if pattern.search(file)]
    if not os.path.exists(os.path.join(directory, 'Interesting Files')):
        os.mkdir(os.path.join(directory, 'Interesting Files'))
    for file in interesting_files:
        shutil.move(os.path.join(directory, file), os.path.join(directory, 'Interesting Files'))
    return interesting_files

import doctest
import unittest
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a clean test environment before each test
        self.base_tmp_dir = tempfile.mkdtemp()
        self.test_directory = f"{self.base_tmp_dir}/test"
        if not os.path.exists(self.test_directory):
            os.makedirs(self.test_directory)
        self.test_files = [
            "file_with_like.txt",
            "another_file_with_what.doc",
            "file_without_keywords.jpg",
            "LIKE_in_caps.pdf",
            "hidden_what_in_name.whatever",
            "no_keyword.png"
        ]
        for file in self.test_files:
            with open(os.path.join(self.test_directory, file), 'w') as f:
                f.write("Dummy content for testing.")
        if os.path.exists(os.path.join(self.test_directory, "Interesting Files")):
            shutil.rmtree(os.path.join(self.test_directory, "Interesting Files"))
        super(TestCases, self).setUp()
    def tearDown(self):
        shutil.rmtree(self.test_directory)
        super(TestCases, self).tearDown()
    def test_caae_1(self):
        """Test if only files with 'like' or 'what' in their names are moved."""
        expected_files = ["file_with_like.txt", "another_file_with_what.doc", "LIKE_in_caps.pdf", "hidden_what_in_name.whatever"]
        moved_files = task_func(self.test_directory)
        self.assertCountEqual(moved_files, expected_files)
    def test_caae_2(self):
        """Test if 'Interesting Files' directory is created."""
        task_func(self.test_directory)
        self.assertTrue(os.path.exists(os.path.join(self.test_directory, "Interesting Files")))
    def test_caae_3(self):
        """Test that files without 'like' or 'what' in their names are not moved."""
        task_func(self.test_directory)
        remaining_files = os.listdir(self.test_directory)
        expected_remaining = ["file_without_keywords.jpg", "no_keyword.png"]
        self.assertCountEqual(remaining_files, expected_remaining + ["Interesting Files"])
    def test_caae_4(self):
        """Test the case insensitivity of the keyword matching."""
        expected_files = ["LIKE_in_caps.pdf"]
        moved_files = task_func(self.test_directory)
        self.assertIn("LIKE_in_caps.pdf", moved_files)
    def test_caae_5(self):
        """Test the function with an empty directory (should handle gracefully)."""
        empty_dir = os.path.join(self.test_directory, "empty_dir")
        os.makedirs(empty_dir, exist_ok=True)
        result = task_func(empty_dir)
        self.assertEqual(result, [])
