import os
import random
import shutil
import json

def f_532(directory, n):
    """
    Create n random files in a directory with json content, and then reset the cursor to the beginning of each file.

    Parameters:
    - directory (str): The directory in which to generate the files.
    - n (int): The number of files to generate.

    Returns:
    - directory (str): The directory in which the files were generated.

    Requirements:
    - os
    - random
    - shutil
    - json

    Example:
    >>> f_532('/path/to/directory', 1)
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

def run_tests():
    random.seed(42)
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        directory = f_532('./source', 10)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 10)
        shutil.rmtree(directory)

    def test_case_2(self):
        directory = f_532('./src', 1)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 1)
        shutil.rmtree(directory)

    def test_case_3(self):
        directory = f_532('./s', 100)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 100)
        shutil.rmtree(directory)

    def test_case_4(self):
        directory = f_532('./s', 0)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 0)
        shutil.rmtree(directory)

    def test_case_5(self):
        directory = f_532('./source', 1)
        self.assertTrue(os.path.exists(directory))
        self.assertEqual(len(os.listdir(directory)), 1)
        shutil.rmtree(directory)

run_tests()
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # run_tests()