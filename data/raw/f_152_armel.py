import os
import random
import pandas as pd
from random import randint

# Constants
NUM_CATEGORIES = 5
NUM_SAMPLES = 100
CATEGORIES = ['Category {}'.format(i+1) for i in range(NUM_CATEGORIES)]

def f_152(save_dir="data/f_152"):
    """
    Create a dataframe with NUM_SAMPLES rows and NUM_CATEGORIES columns and save it as 'output.csv'. The column names should be formatted as in CATEGORIES
    - Do not include the index column when saving.
    - The dataframe values should be randomly sampled between 0 and 100 (both included)

    Parameters:
    - save_dir (str): The path to the directory.

    Returns:
    - pandas.DataFrame: The dataframe created.

    Requirements:
    - random
    - os
    - numpy
    - matplotlib.pyplot

    Example:
    >>> f_152()   
    
    """
    data = pd.DataFrame()
    for category in CATEGORIES:
        data[category] = [randint(0, 100) for _ in range(NUM_SAMPLES)]
    data.to_csv(os.path.join(save_dir, "output.csv"), index=False)
    return data

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_152 function."""
    def setUp(self) -> None:
        random.seed(0)
        self.test_dir = "data/f_152"
        os.makedirs(self.test_dir, exist_ok=True)
    
    def test_case_1(self):
        data = f_152(self.test_dir)
        self.assertEqual(data.shape, (100, 5))
        self.assertListEqual(list(data.columns), ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5'])
        for column in data.columns:
            self.assertTrue(data[column].between(0, 100).all())
        self.assertTrue(
            os.path.exists(
                os.path.join(self.test_dir, "output.csv")
            )
        )
        expected = pd.read_csv(os.path.join(self.test_dir, "output.csv"))
        pd.testing.assert_frame_equal(data, expected)

    def test_case_2(self):
        data1 = f_152(self.test_dir)
        data2 = f_152(self.test_dir)
        for column in data1.columns:
            diff = abs(data1[column].mean() - data2[column].mean())
            self.assertTrue(diff < 20)
    
    def test_case_3(self):
        data1 = f_152(self.test_dir)
        data2 = f_152(self.test_dir)
        self.assertFalse(data1.equals(data2))
        
    def test_case_4(self):
        data = f_152(self.test_dir)
        self.assertTrue(data.min().min() >= 0)
        self.assertTrue(data.max().max() <= 100)
        
    def test_case_5(self):
        data = f_152(self.test_dir)
        self.assertTrue(data.std().mean() > 10)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests() 