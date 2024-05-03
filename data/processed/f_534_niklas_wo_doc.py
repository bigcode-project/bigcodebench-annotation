import os
import random

def f_144(directory, n_files):
    """
    Create n random txt files in a specific directory, write only a single digit random integer into each file, and then reset the cursor to the beginning of each file.
    The file names start from 'file_1.txt' and increment by 1 for each file.
    
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
    >>> f_144('/path/to/directory', 5)
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
        n = f_144(dir, n_files)
        # Check files
        self.assertEqual(n, n_files)
        read_data = []
        for f in sorted(os.listdir(dir)):
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
        self.base('./directory', 5, ['1', '0', '4', '3', '3'])
    def test_case_2(self):
        self.base('./dir', 10, ['1', '9', '0', '4', '3', '3', '2', '1', '8', '1'])
    def test_case_3(self):
        self.base('./d', 15, ['1', '9', '6', '0', '0', '1', '3', '0', '4', '3', '3', '2', '1', '8', '1'])
    def test_case_4(self):
        self.base('./d', 20, ['1', '9', '6', '0', '0', '1', '3', '3', '8', '9', '0', '0', '8', '4', '3', '3', '2', '1', '8', '1'])
    def test_case_5(self):
        self.base('./directory', 25, ['1', '9', '6', '0', '0', '1', '3', '3', '8', '9', '0', '0', '8', '3', '8', '6', '3', '7', '4', '3', '3', '2', '1', '8', '1'])
