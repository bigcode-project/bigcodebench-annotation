import shutil
import pandas as pd
import numpy as np
from random import choice
import os
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
current_directory_path = os.path.join(os.getcwd(), os.path.splitext(os.path.basename(__file__))[0])
if not os.path.exists(current_directory_path):
    os.makedirs(current_directory_path)


def f_464(file_path):
    """
    Create a CSV file with a 2D matrix filled with random lowercase letters.
    
    Parameters:
    - file_path (str): The path of the CSV file to be created.
    
    Returns:
    None: Writes a CSV file to the specified path.
    
    Requirements:
    - pandas
    - numpy
    - random

    Example:
    >>> f_464('random_matrix.csv')
    """
    matrix = pd.DataFrame(np.random.choice(LETTERS, (10, 10)))
    matrix.to_csv(file_path, sep='\t', header=False, index=False)

    return None

import unittest
import pandas as pd


class TestGenerateRandomMatrix(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        """Clean up any files created during the tests."""
        # Check and remove the expected file if it exists
        # if os.path.exists(FILE_PATH):
        #     os.remove(FILE_PATH)
        if os.path.exists(current_directory_path):
            shutil.rmtree(current_directory_path)

    def test_case_1(self):
        # Testing with a sample file path
        file_path = os.path.join(current_directory_path, 'test_output_1.csv')
        f_464(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        self.assertEqual(df.shape, (10, 10), "Matrix shape should be 10x10")

    def test_case_2(self):
        # Testing if the generated matrix contains only lowercase letters
        file_path = os.path.join(current_directory_path, 'test_output_2.csv')
        f_464(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        all_lower = df.applymap(str.islower).all().all()
        self.assertTrue(all_lower, "All elements should be lowercase letters")

    def test_case_3(self):
        # Testing if the generated matrix contains only letters from the alphabet
        file_path = os.path.join(current_directory_path, 'test_output_3.csv')
        f_464(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        all_alpha = df.applymap(str.isalpha).all().all()
        self.assertTrue(all_alpha, "All elements should be alphabetic")

    def test_case_4(self):
        # Testing if the generated matrix contains different letters
        file_path = os.path.join(current_directory_path, 'test_output_4.csv')
        f_464(file_path)
        df = pd.read_csv(file_path, sep='\t', header=None)
        unique_elements = df.nunique().sum()
        self.assertTrue(unique_elements > 10, "Matrix should have more than 10 unique elements")

    def test_case_5(self):
        # Testing if the function overwrites existing files
        file_path = os.path.join(current_directory_path, 'test_output_5.csv')
        with open(file_path, 'w') as f:
            f.write("test")
        f_464(file_path)
        with open(file_path, 'r') as f:
            content = f.read()
        self.assertNotEqual(content, "test", "Function should overwrite existing content")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGenerateRandomMatrix))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()