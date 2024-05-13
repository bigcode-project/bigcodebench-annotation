import os
import glob
import shutil
import time

# Constants
FILE_EXTENSIONS = ['.txt', '.csv', '.xlsx', '.docx', '.pdf']

def task_func(my_path: str, days_old: int) -> str:
    """
    Archive files that were changed older than a specified number of days in a given directory. This function searches for files with specific extensions (.txt, .csv, .xlsx, .docx, .pdf) in the given directory.
    Files older than 'days_old' are moved to an 'archive' subdirectory within the specified directory.

    Parameters:
    my_path (str): The path of the directory to search.
    days_old (int): The age of files to archive, in days.

    Returns:
    str: The path of the archive subdirectory where files are moved.

    Requirements:
    - os
    - glob
    - shutil
    - time

    Example:
    >>> task_func('/usr/my_directory', 30)
    '/usr/my_directory/archive'
    """

    archive_dir = os.path.join(my_path, 'archive')
    os.makedirs(archive_dir, exist_ok=True)
    for ext in FILE_EXTENSIONS:
        files = glob.glob(os.path.join(my_path, '*' + ext))
        for file in files:
            if os.path.isfile(file) and os.path.getmtime(file) < time.time() - days_old * 86400:
                shutil.move(file, archive_dir)
    return archive_dir

import tempfile
import unittest
class TestCases(unittest.TestCase):
    def create_test_file(self, directory, filename, age_days):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'w') as f:
            f.write('Test content')
        # Set the last modified time to 'age_days' days ago
        old_time = time.time() - (age_days * 86400)
        os.utime(file_path, (old_time, old_time))
        return file_path
    def test_empty_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            archive_dir = task_func(tmpdir, 30)
            self.assertTrue(os.path.isdir(archive_dir), 'Archive directory not created')
            self.assertEqual(len(os.listdir(archive_dir)), 0, 'Archive directory is not empty')
    def test_no_old_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            self.create_test_file(tmpdir, 'test1.txt', 10)
            archive_dir = task_func(tmpdir, 30)
            self.assertTrue(os.path.isdir(archive_dir), 'Archive directory not created')
            self.assertEqual(len(os.listdir(archive_dir)), 0, 'Old files incorrectly archived')
    def test_old_files_archived(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            old_file = self.create_test_file(tmpdir, 'test2.txt', 40)
            archive_dir = task_func(tmpdir, 30)
            self.assertTrue(os.path.isfile(os.path.join(archive_dir, 'test2.txt')), 'Old file not archived')
    def test_mixed_file_ages(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            self.create_test_file(tmpdir, 'recent.txt', 10)
            old_file = self.create_test_file(tmpdir, 'old.txt', 40)
            archive_dir = task_func(tmpdir, 30)
            self.assertTrue(os.path.isfile(os.path.join(archive_dir, 'old.txt')), 'Old file not archived')
            self.assertFalse(os.path.isfile(os.path.join(archive_dir, 'recent.txt')), 'Recent file incorrectly archived')
    def test_different_extensions(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            self.create_test_file(tmpdir, 'test.pdf', 40)
            self.create_test_file(tmpdir, 'test.xlsx', 50)
            archive_dir = task_func(tmpdir, 30)
            self.assertTrue(os.path.isfile(os.path.join(archive_dir, 'test.pdf')), 'PDF file not archived')
            self.assertTrue(os.path.isfile(os.path.join(archive_dir, 'test.xlsx')), 'XLSX file not archived')
