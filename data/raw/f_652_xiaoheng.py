import os
import shutil
import fnmatch

def f_652(source_directory, destination_directory, file_pattern):
    """
    Moves all files that match a particular pattern from one directory to another.
    
    Functionality:
    - Moves files from 'source_directory' to 'destination_directory' based on a filename pattern 'file_pattern'.
    
    Input:
    - source_directory (str): The path to the source directory from which files will be moved.
    - destination_directory (str): The path to the destination directory to which files will be moved.
    - file_pattern (str): The file pattern to match (e.g., '*.txt' for all text files).
    
    Output:
    - Returns a list of filenames that were moved.
    
    Requirements:
    - os
    - shutil
    - fnmatch
    
    Example:
    >>> f_652('/path/to/source', '/path/to/destination', '*.txt')
    ['f_652_data_xiaoheng/file1.txt', 'f_652_data_xiaoheng/file2.txt']
    """
    moved_files = []
    for path, dirs, files in os.walk(source_directory):
        for filename in fnmatch.filter(files, file_pattern):
            shutil.move(os.path.join(path, filename), os.path.join(destination_directory, filename))
            moved_files.append(filename)
    return moved_files

import unittest
import os
import shutil

class TestCases(unittest.TestCase):
    def setUp(self):
        self.source_directory = "/mnt/data/source_directory"
        self.destination_directory = "/mnt/data/destination_directory"
        
        # Create some txt files and a jpg file in the source directory
        self.file_names = ['f_652_data_xiaoheng/file1.txt', 'f_652_data_xiaoheng/file2.txt', 'f_652_data_xiaoheng/file3.jpg']
        for file_name in self.file_names:
            with open(os.path.join(self.source_directory, file_name), 'w') as f:
                f.write(f"This is {file_name}")

    def tearDown(self):
        # Clean up the directories after each test
        for directory in [self.source_directory, self.destination_directory]:
            if os.path.exists(directory):
                shutil.rmtree(directory)
        os.makedirs(self.source_directory, exist_ok=True)
        os.makedirs(self.destination_directory, exist_ok=True)
    
    def test_move_txt_files(self):
        moved_files = f_652(self.source_directory, self.destination_directory, '*.txt')
        self.assertEqual(sorted(moved_files), ['f_652_data_xiaoheng/file1.txt', 'f_652_data_xiaoheng/file2.txt'])
        self.assertFalse(os.path.exists(os.path.join(self.source_directory, 'f_652_data_xiaoheng/file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.destination_directory, 'f_652_data_xiaoheng/file1.txt')))

    def test_move_jpg_files(self):
        moved_files = f_652(self.source_directory, self.destination_directory, '*.jpg')
        self.assertEqual(moved_files, ['f_652_data_xiaoheng/file3.jpg'])
        self.assertFalse(os.path.exists(os.path.join(self.source_directory, 'f_652_data_xiaoheng/file3.jpg')))
        self.assertTrue(os.path.exists(os.path.join(self.destination_directory, 'f_652_data_xiaoheng/file3.jpg')))

    def test_no_matching_files(self):
        moved_files = f_652(self.source_directory, self.destination_directory, '*.png')
        self.assertEqual(moved_files, [])
        
    def test_return_moved_files(self):
        moved_files = f_652(self.source_directory, self.destination_directory, '*.txt')
        self.assertEqual(sorted(moved_files), ['f_652_data_xiaoheng/file1.txt', 'f_652_data_xiaoheng/file2.txt'])

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()