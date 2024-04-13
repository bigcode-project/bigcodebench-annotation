import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def f_173(df):
    """
    For a given DataFrame df with 3 columns "A", "B" and "C", select rows in which the values in column "B" are greater than 50 and in column "C" equal 900. Standardize the values from column "A" for the selected rows and plot the distribution.

    Parameters:
    df (DataFrame): The input pandas DataFrame.

    Returns:
    numpy.ndarray : Array of standardized values.
    Axes object: The distribution plot of standardized values.

    Requirements:
    - pandas
    - sklearn.preprocessing
    - seaborn

    Example:
    >>> df = pd.DataFrame(
            {
                'A': np.random.randint(0, 100, 1000),
                'B': np.random.randint(0, 100, 1000),
                'C': np.random.choice([900, 800, 700, 600], 1000)
            }
        )
    >>> f_173(df)
    """
    selected = df['A'][(df['B'] > 50) & (df['C'] == 900)]
    standardized = StandardScaler().fit_transform(selected.values.reshape(-1, 1))
    plt.figure()
    sns.distplot(standardized)
    plot = sns.distplot(standardized)
    return standardized, plot

import unittest
import numpy as np

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    """Test cases for the f_173 function."""
    def test_case_1(self):
        df = pd.DataFrame(
            {
                'A': np.random.randint(0, 100, 100),
                'B': np.random.randint(0, 100, 100),
                'C': np.random.choice([900, 800, 700, 600], 100)}
            )
        standardized, result = f_173(df)
        self.assertTrue(isinstance(result, plt.Axes))
        self.assertAlmostEqual(standardized.mean(), 0, places=1)
        self.assertAlmostEqual(standardized.std(), 1, places=1)
    
    def test_case_2(self):
        df = pd.DataFrame(
            {
                'A': np.random.randint(0, 200, 200),
                'B': np.random.randint(50, 150, 200),
                'C': [900] * 200
            }
        )
        standardized, result = f_173(df)
        self.assertTrue(isinstance(result, plt.Axes))
        self.assertAlmostEqual(standardized.mean(), 0, places=1)
        self.assertAlmostEqual(standardized.std(), 1, places=1)
    
    def test_case_3(self):
        df = pd.DataFrame(
            {
                'A': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
                'B': [55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
                'C': [900, 900, 800, 700, 600, 500, 400, 300, 200, 100]
            }
        )
        standardized, result = f_173(df)
        self.assertTrue(isinstance(result, plt.Axes))
        self.assertAlmostEqual(standardized.mean(), 0, places=1)
        self.assertAlmostEqual(standardized.std(), 1, places=1)
    
    def test_case_4(self):
        df = pd.DataFrame(
            {
                "A" : [10, 20, 30, 40, 50, 60, 70, 80, 90],
                "B" : [20, 70, 10, 80, 35, 95, 15, 100, 17],
                "C" : [900, 900, 100, 900, 300, 900, 400, 900, 1000]
            }
        )
        standardized, result = f_173(df)
        self.assertTrue(isinstance(result, plt.Axes))
        self.assertAlmostEqual(standardized.mean(), 0, places=1)
        self.assertAlmostEqual(standardized.std(), 1, places=1)
        self.assertTrue(np.allclose(standardized[:,0], np.array([-1.34164079, -0.4472136, 0.4472136, 1.34164079]), atol=1e-6))
    
    def test_case_5(self):
        df = pd.DataFrame(
            {
                "A" : [10, 20],
                "B" : [60, 70],
                "C" : [900, 900]
            }
        )
        standardized, result = f_173(df)
        self.assertTrue(isinstance(result, plt.Axes))
        self.assertAlmostEqual(standardized.mean(), 0, places=1)
        self.assertAlmostEqual(standardized.std(), 1, places=1)
        self.assertTrue(np.allclose(standardized[:,0], np.array([-1.0, 1.0]), atol=1e-6))

if __name__ == "__main__" :
    run_tests()