import os
import shutil
import fnmatch
import time

def f_975(days):
    """
    Move all .txt files in a specific folder older than a certain number of days to an archive folder.

    Parameters:
    days (int): The number of days to use as a threshold.

    Requirements:
    - os
    - shutil
    - fnmatch
    - time

    Constants:
    - FOLDER_PATH: Path to the source folder containing the files.
    - ARCHIVE_PATH: Path to the destination archive folder.
    - FILE_PATTERN: File pattern to look for in the source folder.

    Returns:
    list: A list of filenames that were moved to the archive.

    Example:
    >>> f_975(30)
    ['file1.txt', 'file2.txt']
    """
    FOLDER_PATH = './files/'
    ARCHIVE_PATH = './archive/'
    FILE_PATTERN = '*.txt'
    
    current_time = time.time()
    moved_files = []

    for filename in os.listdir(FOLDER_PATH):
        if fnmatch.fnmatch(filename, FILE_PATTERN):
            file_path = os.path.join(FOLDER_PATH, filename)
            file_time = os.path.getmtime(file_path)
            file_age_days = (current_time - file_time) / (60 * 60 * 24)
            if file_age_days > days:
                shutil.move(file_path, ARCHIVE_PATH)
                moved_files.append(filename)

    return moved_files

import unittest
import os
import shutil

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        # Reset the files and archive before each test
        for file in os.listdir("./archive"):
            shutil.move(os.path.join("./archive", file), "./files")

    def test_case_1(self):
        # Test with files older than 30 days
        moved_files = f_975(30)
        self.assertListEqual(moved_files, ['file1.txt', 'file3.txt', 'file5.txt'])
        self.assertListEqual(os.listdir("./archive"), ['file1.txt', 'file3.txt', 'file5.txt'])
        self.assertListEqual(os.listdir("./files"), ['file2.txt', 'file4.txt'])

    def test_case_2(self):
        # Test with files older than 10 days
        moved_files = f_975(10)
        self.assertListEqual(moved_files, ['file1.txt', 'file3.txt', 'file5.txt', 'file2.txt', 'file4.txt'])
        self.assertListEqual(os.listdir("./archive"), ['file1.txt', 'file3.txt', 'file5.txt', 'file2.txt', 'file4.txt'])
        self.assertEqual(os.listdir("./files"), [])

    def test_case_3(self):
        # Test with files older than 40 days (no files should be moved)
        moved_files = f_975(40)
        self.assertEqual(moved_files, [])
        self.assertEqual(os.listdir("./archive"), [])
        self.assertListEqual(os.listdir("./files"), ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt', 'file5.txt'])

    def test_case_4(self):
        # Test with files older than 35 days (only file1, file3, file5 should be moved)
        moved_files = f_975(35)
        self.assertListEqual(moved_files, ['file1.txt', 'file3.txt', 'file5.txt'])
        self.assertListEqual(os.listdir("./archive"), ['file1.txt', 'file3.txt', 'file5.txt'])
        self.assertListEqual(os.listdir("./files"), ['file2.txt', 'file4.txt'])

    def test_case_5(self):
        # Test with files older than 5 days (all files should be moved)
        moved_files = f_975(5)
        self.assertListEqual(moved_files, ['file1.txt', 'file3.txt', 'file5.txt', 'file2.txt', 'file4.txt'])
        self.assertListEqual(os.listdir("./archive"), ['file1.txt', 'file3.txt', 'file5.txt', 'file2.txt', 'file4.txt'])
        self.assertEqual(os.listdir("./files"), [])
if __name__ == "__main__":
    run_tests()