import re
import os
import shutil

def f_678(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    """
    Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, write these file paths to a configuration file.

    Parameters:
    - source_dir (str): The path to the source directory.
    - target_dir (str): The path to the target directory.
    - file_pattern (str, optional): The regular expression pattern that filenames must match in order
                                   to be moved. Default is r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b',
                                   which matches filenames that consist of alphanumeric characters
                                   and have extensions txt, doc, or docx.

    Returns:
    - str: Path to the created configuration file.

    Requirements:
    - re
    - os
    - shtuil

    Example:
    >>> f_678('/path/to/source', '/path/to/target')
    3
    """
    if not os.path.exists(source_dir):
        raise FileNotFoundError("The source directory does not exist.")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    moved_files_count = 0
    for filename in os.listdir(source_dir):
        if re.match(file_pattern, filename):
            shutil.move(os.path.join(source_dir, filename), os.path.join(target_dir, filename))
            moved_files_count += 1
    return moved_files_count

import unittest
import os
import tempfile
import configparser
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for source and target
        self.source_dir = tempfile.mkdtemp()
        self.target_dir = tempfile.mkdtemp()
        # Files that should match the pattern and be moved
        self.valid_files = ['test1.txt', 'document1.doc', 'file1.docx', 'test2.txt', 'notes1.docx']
        for file in self.valid_files:
            with open(os.path.join(self.source_dir, file), 'w') as f:
                f.write("Dummy content")
        # Files that should not match the pattern and remain
        self.invalid_files = ['image1.png', 'script.js', 'data.csv', 'test.tmp', 'archive.zip']
        for file in self.invalid_files:
            with open(os.path.join(self.source_dir, file), 'w') as f:
                f.write("Dummy content")
    def tearDown(self):
        # Clean up by removing directories
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.target_dir)
    def test_valid_files_moved(self):
        # Test that all valid files are moved
        moved_files_count = f_678(self.source_dir, self.target_dir)
        self.assertEqual(moved_files_count, len(self.valid_files), "Not all valid files were moved.")
    def test_invalid_files_not_moved(self):
        # Test that invalid files are not moved
        f_678(self.source_dir, self.target_dir)
        remaining_files = os.listdir(self.source_dir)
        self.assertListEqual(sorted(remaining_files), sorted(self.invalid_files), "Invalid files were moved.")
    def test_no_files_to_move(self):
        # Test with no files matching the pattern
        # Clean source directory from valid files
        for file in self.valid_files:
            os.remove(os.path.join(self.source_dir, file))
        moved_files_count = f_678(self.source_dir, self.target_dir)
        self.assertEqual(moved_files_count, 0, "Files were moved when none should have.")
    def test_pattern_specificity(self):
        # Test with a more specific pattern that should only match .docx files
        moved_files_count = f_678(self.source_dir, self.target_dir, r'\b[A-Za-z0-9]+\.(docx)\b')
        expected_count = sum(1 for f in self.valid_files if f.endswith('.docx'))
        self.assertEqual(moved_files_count, expected_count, "Pattern did not correctly filter files.")
    def test_target_directory_creation(self):
        # Test that the target directory is created if it does not exist
        shutil.rmtree(self.target_dir)  # Ensure target directory is deleted
        moved_files_count = f_678(self.source_dir, self.target_dir)
        self.assertTrue(os.path.exists(self.target_dir), "Target directory was not created.")
        self.assertEqual(moved_files_count, len(self.valid_files), "Files were not moved correctly when target directory was initially absent.")
