import os
import logging

def task_func(directory):
    """
    Removes all jQuery files (JavaScript files containing 'jquery' in their name) from a specified directory.

    Parameters:
    directory (str): The directory path.

    Returns:
    tuple: A tuple containing two elements:
        - int: The number of files removed.
        - list: The names of the removed files.

    Raises:
    - If the specified directory does not exist the code would raise FileNotFoundError.
    
    Note:
    - Removed files are logged in 'jquery_removal.log' file.

    Requirements:
    - os
    - logging


    Example:
    >>> task_func("/path/to/directory")
    (3, ['jquery-1.js', 'jquery-2.js', 'jquery-ui.js'])  # Assuming 3 jQuery files were removed
    """

    logging.basicConfig(filename='jquery_removal.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")
    files = os.listdir(directory)
    removed_files = 0
    removed_file_names = []
    for file in files:
        if 'jquery' in file and file.endswith('.js'):
            try:
                os.remove(os.path.join(directory, file))
                removed_files += 1
                removed_file_names.append(file)
                logging.info(f"Removed jQuery file: {file}")
            except Exception as e:
                logging.error(f"Error while removing file {file}: {e}")
    return removed_files, removed_file_names

import unittest
from unittest.mock import MagicMock, patch
class TestCases(unittest.TestCase):
    @patch('os.path.exists')
    @patch('os.listdir')
    @patch('os.remove')
    def test_remove_jquery_files(self, mock_remove, mock_listdir, mock_exists):
        mock_exists.return_value = True
        mock_listdir.return_value = ['jquery-1.js', 'jquery-2.js', 'jquery-ui.js', 'otherfile.txt', 'example.js']
        removed_count, removed_files = task_func('/fake/directory')
        self.assertEqual(removed_count, 3)
        self.assertListEqual(removed_files, ['jquery-1.js', 'jquery-2.js', 'jquery-ui.js'])
    @patch('os.path.exists')
    @patch('os.listdir')
    def test_empty_directory(self, mock_listdir, mock_exists):
        mock_exists.return_value = True
        mock_listdir.return_value = []
        removed_count, removed_files = task_func('/fake/empty/directory')
        self.assertEqual(removed_count, 0)
        self.assertListEqual(removed_files, [])
    @patch('os.path.exists')
    def test_nonexistent_directory(self, mock_exists):
        mock_exists.return_value = False
        with self.assertRaises(FileNotFoundError):
            task_func('/fake/nonexistent/directory')
    @patch('os.path.exists', return_value=True)
    @patch('os.listdir', return_value=['jquery-1.js', 'jquery-2.min.js', 'jquery-ui.css'])
    @patch('os.remove')
    def test_remove_jquery_files_not_js(self, mock_remove, mock_listdir, mock_exists):
        removed_count, removed_files = task_func('/fake/directory')
        self.assertEqual(removed_count, 2)
        self.assertListEqual(removed_files, ['jquery-1.js', 'jquery-2.min.js'])
    @patch('os.path.exists', return_value=True)
    @patch('os.listdir', return_value=['subdir', 'jquery-1.js'])
    @patch('os.remove')
    def test_remove_jquery_files_subdirectory(self, mock_remove, mock_listdir, mock_exists):
        removed_count, removed_files = task_func('/fake/directory')
        self.assertEqual(removed_count, 1)
        self.assertListEqual(removed_files, ['jquery-1.js'])
    @patch('os.path.exists', return_value=True)
    @patch('os.listdir', return_value=['jquery-1.js', 'jquery-2.js', 'jquery-ui.js'])
    @patch('os.remove', side_effect=OSError("Permission denied"))
    def test_remove_jquery_files_error(self, mock_remove, mock_listdir, mock_exists):
        removed_count, removed_files = task_func('/fake/directory')
        self.assertEqual(removed_count, 0)
        self.assertListEqual(removed_files, [])
    @patch('os.path.exists', return_value=True)
    @patch('os.listdir', return_value=['jquery-1.js', 'jquery-2.min.js', 'jquery-ui.css'])
    @patch('os.remove')
    def test_logging(self, mock_remove, mock_listdir, mock_exists):
        """Test if logging works as expected."""
        with patch('logging.info') as mock_info, \
             patch('logging.error') as mock_error:
            task_func('/fake/directory')
            mock_info.assert_called()
            mock_error.assert_not_called()  # Ensure that no error message is logged
    def tearDown(self):
        """Remove the generated log file after each test."""
        log_file = 'jquery_removal.log'
        if os.path.exists(log_file):
            logging.shutdown()  # Manually close the logging file handler
            os.remove(log_file)
