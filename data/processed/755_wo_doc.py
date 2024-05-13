import os
import glob

def task_func(directory_path):
    """
    Reverse the order of words in all the filenames of a directory, where words are separated by periods.
    
    Parameters:
    - directory_path (str): The path to the directory.

    Returns:
    - new_filenames (list[str]): A list of new filenames after renaming.

    Requirements:
    - os
    - glob

    Example:
    Given filenames in directory: ["hello.world.txt", "sample.data.csv"]
    >>> task_func('/path/to/directory')
    ["txt.world.hello", "csv.data.sample"]
    """

    new_filenames = []
    for filename in glob.glob(os.path.join(directory_path, '*')):
        base_name = os.path.basename(filename)
        new_base_name = '.'.join(base_name.split('.')[::-1])
        os.rename(filename, os.path.join(directory_path, new_base_name))
        new_filenames.append(new_base_name)
    return new_filenames

import unittest
import shutil
import tempfile
class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    def test_single_file(self):
        open(os.path.join(self.test_dir, "hello.world.txt"), 'a').close()
        new_filenames = task_func(self.test_dir)
        self.assertEqual(new_filenames, ["txt.world.hello"])
    def test_multiple_files(self):
        open(os.path.join(self.test_dir, "sample.data.csv"), 'a').close()
        open(os.path.join(self.test_dir, "test.file.name.jpg"), 'a').close()
        new_filenames = task_func(self.test_dir)
        expected_filenames = ["csv.data.sample", "jpg.name.file.test"]
        self.assertCountEqual(new_filenames, expected_filenames)
    def test_empty_directory(self):
        new_filenames = task_func(self.test_dir)
        self.assertEqual(new_filenames, [])
    def test_files_without_extension(self):
        open(os.path.join(self.test_dir, "file1"), 'a').close()
        open(os.path.join(self.test_dir, "file2.txt"), 'a').close()
        new_filenames = task_func(self.test_dir)
        expected_filenames = ["file1", "txt.file2"]
        self.assertCountEqual(new_filenames, expected_filenames)
    def test_files_with_multiple_extensions(self):
        open(os.path.join(self.test_dir, "file.tar.gz"), 'a').close()
        open(os.path.join(self.test_dir, "archive.zip.001"), 'a').close()
        new_filenames = task_func(self.test_dir)
        expected_filenames = ["gz.tar.file", "001.zip.archive"]
        self.assertCountEqual(new_filenames, expected_filenames)
