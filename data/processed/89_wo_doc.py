import os
import glob
import shutil

def task_func(directory, archive_dir='archive'):
    """
    Archive all JSON files in a given directory by moving them to a specified archive directory.

    Parameters:
    directory (str): The directory where the JSON files are located.
    archive_dir (str): The directory to which the JSON files will be archived. Defaults to 'archive'.

    Returns:
    tuple: A tuple containing a boolean value and a list of error messages.
           The boolean is True if all files are successfully moved, and False otherwise.
           The list contains error messages for each file that failed to move.

    Requirements:
    - os
    - glob
    - shutil

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()
    >>> files = ['file1.json', 'file2.json', 'file3.json']
    >>> for file in files:
    ...     with open(os.path.join(temp_dir, file), 'w') as f:
    ...         _ = f.write("Dummy content for testing.")
    >>> backup_dir = tempfile.mkdtemp()
    >>> task_func(temp_dir, backup_dir)
    (True, [])
    """
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    json_files = glob.glob(os.path.join(directory, '*.json'))
    error_messages = []
    for json_file in json_files:
        try:
            shutil.move(json_file, archive_dir)
        except Exception as e:
            error_message = f'Unable to move {json_file} due to {str(e)}'
            error_messages.append(error_message)
    return (len(error_messages) == 0, error_messages)

import unittest
import doctest
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a test directory with some JSON files and some other file types
        os.makedirs('test_data', exist_ok=True)
        with open('test_data/test1.json', 'w') as f:
            f.write('{}')
        with open('test_data/test2.json', 'w') as f:
            f.write('{}')
        with open('test_data/test.txt', 'w') as f:
            f.write('Hello')
        # Create a different archive directory for one of the tests
        os.makedirs('custom_archive', exist_ok=True)
        os.makedirs('archive', exist_ok=True)
    def tearDown(self):
        # Clean up test directories and files
        shutil.rmtree('test_data')
        shutil.rmtree('archive')
        shutil.rmtree('custom_archive')
    def test_case_1(self):
        """Test archiving JSON files with the default archive directory."""
        success, errors = task_func('test_data')
        self.assertTrue(success)
        self.assertEqual(len(errors), 0)
        self.assertTrue(os.path.exists('archive/test1.json'))
        self.assertTrue(os.path.exists('archive/test2.json'))
    def test_case_2(self):
        """Test archiving with a custom archive directory."""
        success, errors = task_func('test_data', 'custom_archive')
        self.assertTrue(success)
        self.assertEqual(len(errors), 0)
        self.assertTrue(os.path.exists('custom_archive/test1.json'))
        self.assertTrue(os.path.exists('custom_archive/test2.json'))
    def test_case_3(self):
        """Test with a nonexistent source directory."""
        success, errors = task_func('nonexistent_directory')
        self.assertTrue(success)
        self.assertEqual(len(errors), 0)
    def test_case_4(self):
        """Test with an empty directory."""
        os.makedirs('empty_directory', exist_ok=True)
        success, errors = task_func('empty_directory')
        self.assertTrue(success)
        self.assertEqual(len(errors), 0)
        shutil.rmtree('empty_directory')
    def test_case_5(self):
        """Test that non-JSON files are not archived."""
        success, errors = task_func('test_data')
        self.assertTrue(success)
        self.assertEqual(len(errors), 0)
        self.assertFalse(os.path.exists('archive/test.txt'))
