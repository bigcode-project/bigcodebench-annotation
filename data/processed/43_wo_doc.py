import os
import shutil
import random


def task_func(num_files, source_dir='./source_dir/', dest_dir='./dest_dir/', file_ext='.txt', seed=0):
    """
    Moves a specified number of random files with a given extension from a source directory to a target directory.
    
    Parameters:
    - num_files (int): The number of files to move.
    - source_dir (str, optional): The directory from where the files will be moved. Defaults to './source_dir/'.
    - dest_dir (str, optional): The directory to which the files will be moved. Defaults to './dest_dir/'.
    - file_ext (str, optional): The extension of the files to move. Defaults to '.txt'.
    - seed (int, optional): The seed for the random number generator. Defaults to 0.
    
    Returns:
    - list: A list of filenames that were moved.

    Requirements:
    - os
    - shutil
    - random

    Example:
    >>> import tempfile
    >>> import os
    >>> source_dir = tempfile.mkdtemp()
    >>> dest_dir = tempfile.mkdtemp()
    >>> for i in range(10):
    ...     with open(f"{source_dir}/file{i}.txt", 'w') as file:
    ...         _ = file.write(f"This is file {i}")
    >>> task_func(5, source_dir, dest_dir, '.txt')
    ['file7.txt', 'file9.txt', 'file2.txt', 'file1.txt', 'file4.txt']
    """
    random.seed(seed)
    files = [f for f in os.listdir(source_dir) if f.endswith(file_ext)]
    num_files = min(num_files, len(files))
    random_files = random.sample(files, num_files)
    for file in random_files:
        shutil.move(os.path.join(source_dir, file), dest_dir)
    return random_files

import unittest
import shutil
import doctest
import tempfile
# Create the source and destination directories for testing
base_tmp_dir = tempfile.mkdtemp()
source_dir = f"{base_tmp_dir}/test/test_source_dir/"
dest_dir = f"{base_tmp_dir}/test/test_dest_dir/"
class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        # Create the directories if they don't exist
        if not os.path.exists(source_dir):
            os.makedirs(source_dir)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        # Generate 10 dummy .txt files in the source directory for testing
        for i in range(10):
            with (
                open(os.path.join(source_dir, f"file{i}.txt"), "w")
                if os.path.exists(os.path.join(source_dir, f"file{i}.txt"))
                else open(os.path.join(source_dir, f"file{i}.txt"), "x") 
            ) as f:
                f.write(f"This is file {i}")
        return super().setUp()
    
    def tearDown(self) -> None:
        shutil.rmtree(base_tmp_dir)
        return super().tearDown()
    def test_case_1(self):
        # Test the case where 5 files are moved
        moved_files = task_func(5, source_dir, dest_dir, '.txt')
        self.assertEqual(len(moved_files), 5)
        for file in moved_files:
            self.assertTrue(os.path.exists(os.path.join(dest_dir, file)))
            self.assertFalse(os.path.exists(os.path.join(source_dir, file)))
        # Test the names of the moved files
        self.assertSetEqual(set(moved_files), set([f"file{i}.txt" for i in [6, 8, 2, 9, 0]]))
    def test_case_2(self):
        # Test the case where no files are moved
        moved_files = task_func(0, source_dir, dest_dir, '.txt')
        self.assertEqual(len(moved_files), 0)
        for file in moved_files:
            self.assertFalse(os.path.exists(os.path.join(source_dir, file)))
    def test_case_3(self):
        # Test the case where all files are moved
        moved_files = task_func(10, source_dir, dest_dir, '.txt')
        self.assertEqual(len(moved_files), 10)
        for file in moved_files:
            self.assertTrue(os.path.exists(os.path.join(dest_dir, file)))
            self.assertFalse(os.path.exists(os.path.join(source_dir, file)))
    def test_case_4(self):
        # Test the case for roustness to an invalid number of files (greater than the files present)
        moved_files = task_func(15, source_dir, dest_dir, '.txt')
        self.assertEqual(len(moved_files), 10)
        for file in moved_files:
            self.assertTrue(os.path.exists(os.path.join(dest_dir, file)))
        # Test the names of the moved files
        self.assertSetEqual(set(moved_files), set([f"file{i}.txt" for i in range(10)]))
    def test_case_5(self):
        # Test the case with a different file extension (no files should be moved)
        moved_files = task_func(5, source_dir, dest_dir, '.jpeg')
        self.assertEqual(len(moved_files), 0)
        for file in moved_files:
            self.assertFalse(os.path.exists(os.path.join(source_dir, file)))
