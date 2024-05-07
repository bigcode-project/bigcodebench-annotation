import os
import random
import json

def f_26(directory, n):
    """
    Create n random files in a directory with json content with the key 'number' and a random integer value between 1 and 100, and then reset the cursor to the beginning of each file.

    Parameters:
    - directory (str): The directory in which to generate the files.
    - n (int): The number of files to generate.

    Returns:
    - directory (str): The directory in which the files were generated.

    Requirements:
    - os
    - random
    - json

    Example:
    >>> f_26('/path/to/directory', 1)
    '/path/to/directory'
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(n):
        filename = str(i) + ".json"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as file:
            json.dump({'number': random.randint(1, 100)}, file)
            file.seek(0)
    return directory

import unittest
import shutil
class TestCases(unittest.TestCase):
    def tearDown(self):
        shutil.rmtree('./source', ignore_errors=True)
        shutil.rmtree('./src', ignore_errors=True)
        shutil.rmtree('./s', ignore_errors=True)
    def test_case_1(self):
        random.seed(0)
        directory = f_26('./source', 10)
        self.assertTrue(os.path.exists(directory))
        read_data = []
        for file in sorted(os.listdir(directory)):
            with open(os.path.join(directory, file), 'r') as f:
                read_data.append(json.load(f))
        self.assertEqual(read_data, [{'number': 50}, {'number': 98}, {'number': 54}, {'number': 6}, {'number': 34}, {'number': 66}, {'number': 63}, {'number': 52}, {'number': 39}, {'number': 62}])
        shutil.rmtree(directory)
    def test_case_2(self):
        random.seed(1)
        directory = f_26('./src', 1)
        self.assertTrue(os.path.exists(directory))
        read_data = []
        for file in os.listdir(directory):
            with open(os.path.join(directory, file), 'r') as f:
                read_data.append(json.load(f))
        self.assertEqual(read_data, [{'number': 18}])
        shutil.rmtree(directory)
    def test_case_3(self):
        directory = f_26('./s', 100)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 100)
        shutil.rmtree(directory)
    def test_case_4(self):
        directory = f_26('./s', 0)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 0)
        shutil.rmtree(directory)
    def test_case_5(self):
        random.seed(2)
        directory = f_26('./source', 1)
        self.assertTrue(os.path.exists(directory))
        read_data = []
        for file in os.listdir(directory):
            with open(os.path.join(directory, file), 'r') as f:
                read_data.append(json.load(f))
        self.assertEqual(read_data, [{'number': 8}])
        shutil.rmtree(directory)
