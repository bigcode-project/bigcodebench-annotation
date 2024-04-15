import os

def f_314(directory):
    """
    Removes all jQuery files (JavaScript files containing 'jquery' in their name) from a specified directory.

    Parameters:
    directory (str): The directory path.

    Returns:
    tuple: A tuple containing two elements:
        - int: The number of files removed.
        - list: The names of the removed files.

    Raises:
    FileNotFoundError: If the specified directory does not exist.

    Example:
    >>> f_280("/path/to/directory")
    (3, ['jquery-1.js', 'jquery-2.js', 'jquery-ui.js'])  # Assuming 3 jQuery files were removed
    """

    # Check if directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    # Get all files in the directory
    files = os.listdir(directory)

    # Remove jQuery files
    removed_files = 0
    removed_file_names = []
    for file in files:
        if 'jquery' in file and file.endswith('.js'):
            os.remove(os.path.join(directory, file))
            removed_files += 1
            removed_file_names.append(file)

    return removed_files, removed_file_names

import unittest
from unittest.mock import MagicMock, patch

class TestF1590(unittest.TestCase):

    @patch('os.path.exists')
    @patch('os.listdir')
    @patch('os.remove')
    def test_remove_jquery_files(self, mock_remove, mock_listdir, mock_exists):
        mock_exists.return_value = True
        mock_listdir.return_value = ['jquery-1.js', 'jquery-2.js', 'jquery-ui.js', 'otherfile.txt', 'example.js']
        removed_count, removed_files = f_314('/fake/directory')
        self.assertEqual(removed_count, 3)
        self.assertListEqual(removed_files, ['jquery-1.js', 'jquery-2.js', 'jquery-ui.js'])

    @patch('os.path.exists')
    @patch('os.listdir')
    def test_empty_directory(self, mock_listdir, mock_exists):
        mock_exists.return_value = True
        mock_listdir.return_value = []
        removed_count, removed_files = f_314('/fake/empty/directory')
        self.assertEqual(removed_count, 0)
        self.assertListEqual(removed_files, [])

    @patch('os.path.exists')
    def test_nonexistent_directory(self, mock_exists):
        mock_exists.return_value = False
        with self.assertRaises(FileNotFoundError):
            f_314('/fake/nonexistent/directory')

    # More tests can be added here

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestF1590))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    run_tests()