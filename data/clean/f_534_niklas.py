import os
import random

def f_534(directory, n_files):
    """
    Create n random txt files in a specific directory, write only a single digit random integer into each file, and then reset the cursor to the beginning of each file.

    Parameters:
    - directory (str): The directory in which to generate the files.
    - n_files (int): The number of files to generate.

    Returns:
    - n_files (int): The number of files generated.

    Requirements:
    - os
    - random

    Example:
    >>> random.seed(2)
    >>> f_534('/path/to/directory', 5)
    5
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")

        with open(filename, 'w') as file:
            file.write(str(random.randint(0, 9)))
            file.seek(0)

    return n_files

import unittest
import shutil

class TestCases(unittest.TestCase):
    def base(self, dir, n_files, contents):
        random.seed(42)
        # Create directory
        if not os.path.exists(dir):
            os.makedirs(dir)
        # Run function
        n = f_534(dir, n_files)
        # Check files
        self.assertEqual(n, n_files)
        read_data = []
        for f in os.listdir(dir):
            self.assertTrue(f.endswith('.txt'))
            with open(os.path.join(dir, f), 'r') as file:
                read_data.append(file.read())
                file.seek(0)
        self.assertEqual(read_data, contents)

    def tearDown(self):
        shutil.rmtree('./directory', ignore_errors=True)
        shutil.rmtree('./dir', ignore_errors=True)
        shutil.rmtree('./d', ignore_errors=True)

    def test_case_1(self):
        self.base('./directory', 5, ['1', '4', '0', '3', '3'])

    def test_case_2(self):
        self.base('./dir', 10, ['9', '1', '2', '1', '1', '8', '4', '0', '3', '3'])

    def test_case_3(self):
        self.base('./d', 15, ['9', '1', '3', '2', '1', '1', '8', '4', '0', '0', '3', '1', '3', '6', '0'])

    def test_case_4(self):
        self.base('./d', 20, ['9', '1', '3', '8', '2', '1', '1', '8', '8', '4', '0', '3', '0', '3', '1', '3', '0', '9', '6', '0'])

    def test_case_5(self):
        self.base('./directory', 25, ['6', '9', '1', '3', '8', '8', '2', '7', '1', '3', '1', '8', '8', '3', '4', '0', '3', '0', '3', '1', '3', '0', '9', '6', '0'])
