import os
import random
import shutil

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
    - shutil

    Example:
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

def run_tests():
    random.seed(42)
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def base(self, dir, n_files):
        # Create directory
        if not os.path.exists(dir):
            os.makedirs(dir)
        # Run function
        n = f_534(dir, n_files)
        # Check files
        self.assertEqual(n, n_files)
        for f in os.listdir(dir):
            self.assertTrue(f.endswith('.txt'))
            with open(os.path.join(dir, f), 'r') as file:
                self.assertEqual(len(file.read()), 1)
                file.seek(0)
        # Remove files
        shutil.rmtree(dir)

    def test_case_1(self):
        self.base('./directory', 5)

    def test_case_2(self):
        self.base('./dir', 10)

    def test_case_3(self):
        self.base('./d', 15)

    def test_case_4(self):
        self.base('./d', 20)

    def test_case_5(self):
        self.base('./directory', 25)

run_tests()
if __name__ == "__main__":
    run_tests()