import os
import random

def f_122(directory, n_files):
    """
    Create n random text files in a specific directory, write a random string to each file, and then reset the cursor to the beginning of each file.

    Parameters:
    - directory (str): The directory in which to generate the files.
    - n_files (int): The number of files to generate.

    Returns:
    - directory (str): The directory in which the files were generated.

    Requirements:
    - os
    - random

    Example:
    >>> f_122('/path/to/directory', 5)
    '/path/to/directory'
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")

        with open(filename, 'w') as file:
            file.write(str(random.randint(1, 100)))
            file.seek(0)

    return directory

import unittest
import shutil
class TestCases(unittest.TestCase):
    def setUp(self):
        random.seed(42)
        
    def tearDown(self):
        shutil.rmtree('./source', ignore_errors=True)
        shutil.rmtree('./src', ignore_errors=True)
        shutil.rmtree('./s', ignore_errors=True)
    
    def test_case_1(self):
        directory = f_122('./source', 10)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 10)
        for file in os.listdir(directory):
            self.assertEqual(file.split('.')[-1], 'txt')
        
    def test_case_2(self):
        directory = f_122('./src', 1)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 1)
        for file in os.listdir(directory):
            self.assertEqual(file.split('.')[-1], 'txt')        
        
    def test_case_3(self):
        directory = f_122('./s', 100)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 100)
        for file in os.listdir(directory):
            self.assertEqual(file.split('.')[-1], 'txt')        
        
    def test_case_4(self):
        directory = f_122('./s', 0)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 0)
        for file in os.listdir(directory):
            self.assertEqual(file.split('.')[-1], 'txt')        
        
    def test_case_5(self):
        directory = f_122('./source', 1)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 1)
        for file in os.listdir(directory):
            self.assertEqual(file.split('.')[-1], 'txt')
