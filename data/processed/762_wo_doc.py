import codecs
import os
import zipfile


def task_func(directory_name="latin_files",
          content='Sopetón',
          file_names=['file1.txt', 'file2.txt', 'file3.txt'],
          encoding="latin-1"):
    '''
    Create a directory with the given name, create specified .txt files. Encode
    the content using the specified encoding and write it into all .txt files, 
    then zip the directory. 

    Args:
    directory_name (str): The name of the directory to be created.
    content (str, optional): The content which should be written to each .txt file.
                             Defaults to 'Sopetón'.
    file_names (list): List of .txt file names to be created.
                       Defaults to ['file1.txt', 'file2.txt', 'file3.txt'].
    encoding (str): The encoding type for the files. Default is 'latin-1'.

    Returns:
    str: The zipped file name.

    Requirements:
    - codecs
    - os
    - zipfile

    Example:
    >>> zipped_file = task_func("latin_files", "test", ["file1.txt", "file2.txt", "file3.txt"])
    >>> print(zipped_file)
    latin_files.zip

    >>> zipped_file = task_func(directory_name="directorio", content='hi', file_names=["custom1.txt", "custom2.txt"], encoding='utf-8')
    >>> print(zipped_file)
    directorio.zip
    '''

    os.makedirs(directory_name, exist_ok=True)
    for file_name in file_names:
        with open(os.path.join(directory_name, file_name), 'wb') as f:
            f.write(codecs.encode(content, encoding))
    zipped_file = directory_name + '.zip'
    with zipfile.ZipFile(zipped_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory_name):
            for file in files:
                zipf.write(os.path.join(root, file))
    return zipped_file 

import unittest
import os
import shutil
from zipfile import ZipFile
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test default parameters
        zipped_file = task_func()
        self.assertEqual(zipped_file, "latin_files.zip")
        self.assertTrue(os.path.exists(zipped_file))
        
        # Extract the zipped file and check contents
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("test_case_1")
        self.assertTrue(os.path.exists(os.path.join("latin_files", "file1.txt")))
        self.assertTrue(os.path.exists(os.path.join("latin_files", "file2.txt")))
        self.assertTrue(os.path.exists(os.path.join("latin_files", "file3.txt")))
        for i in range(1,4):
            with open(os.path.join("latin_files", f'file{i}.txt'), encoding='latin-1') as file:
                self.assertEqual(file.read(), 'Sopetón')
        shutil.rmtree("test_case_1")
        os.remove(zipped_file)
        shutil.rmtree("latin_files")
    def test_case_2(self):
        # Test with custom directory and file names
        zipped_file = task_func(directory_name="custom_directory", content='test', file_names=["custom1.txt", "custom2.txt"], encoding='utf-8')
        self.assertEqual(zipped_file, "custom_directory.zip")
        self.assertTrue(os.path.exists(zipped_file))
        
        # Extract the zipped file and check contents
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("test_case_2")
        self.assertTrue(os.path.exists(os.path.join("test_case_2", "custom_directory", "custom1.txt")))
        self.assertTrue(os.path.exists(os.path.join("test_case_2", "custom_directory", "custom2.txt")))
        for i in range(1,3):
            with open(os.path.join("custom_directory", f'custom{i}.txt'), encoding='latin-1') as file:
                self.assertEqual(file.read(), 'test')    
    
        shutil.rmtree("test_case_2")
        os.remove(zipped_file)
        shutil.rmtree("custom_directory")
    def test_case_3(self):
        # Test with custom encoding
        zipped_file = task_func(encoding="utf-8")
        self.assertEqual(zipped_file, "latin_files.zip")
        self.assertTrue(os.path.exists(zipped_file))
        
        # Extract the zipped file and check contents
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("test_case_3")
        with open(os.path.join("test_case_3", "latin_files", "file1.txt"), 'r') as file:
            content = file.read()
        self.assertEqual(content, 'Sopetón')  # Since we used utf-8 encoding, the content should match
        shutil.rmtree("test_case_3")
        os.remove(zipped_file)
        shutil.rmtree("latin_files")
    def test_case_4(self):
        # Test with all custom parameters
        zipped_file = task_func(directory_name="all_custom", file_names=["all1.txt", "all2.txt"], encoding="utf-8")
        self.assertEqual(zipped_file, "all_custom.zip")
        self.assertTrue(os.path.exists(zipped_file))
        
        # Extract the zipped file and check contents
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("test_case_4")
        with open(os.path.join("test_case_4", "all_custom", "all1.txt"), 'r') as file:
            content = file.read()
        self.assertEqual(content, 'Sopetón')  # Since we used utf-8 encoding, the content should match
        shutil.rmtree("test_case_4")
        os.remove(zipped_file)
        shutil.rmtree("all_custom")
    def test_case_5(self):
        # Test with a single file and default encoding
        zipped_file = task_func(directory_name="single_file_dir", file_names=["single.txt"])
        self.assertEqual(zipped_file, "single_file_dir.zip")
        self.assertTrue(os.path.exists(zipped_file))
        
        # Extract the zipped file and check contents
        with ZipFile(zipped_file, 'r') as zip_ref:
            zip_ref.extractall("test_case_5")
        self.assertTrue(os.path.exists(os.path.join("test_case_5", "single_file_dir", "single.txt")))
        shutil.rmtree("test_case_5")
        shutil.rmtree("single_file_dir")
        os.remove(zipped_file)
