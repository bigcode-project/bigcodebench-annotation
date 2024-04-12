import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def f_500(num_samples=100, num_features=5):
    """
    Generate a Pandas DataFrame with random values, representing a dataset with multiple features. 
    Calculate the correlation between the features and visualize this information using a heatmap.
    
    Parameters:
    - num_samples (int): The number of samples to generate. Default is 100.
    - num_features (int): The number of features to generate. Default is 5.
    
    Returns:
    - DataFrame: The generated DataFrame with random values.
    - Axes: The heatmap visualization of the correlation matrix.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot
    - seaborn
    
    Example:
    >>> df, ax = f_500(10, 3)
    >>> print(df)
    >>> ax.figure.show()
    """
    FEATURES = ['Feature' + str(i) for i in range(1, num_features + 1)]
    SAMPLES = ['Sample' + str(i) for i in range(1, num_samples + 1)]
    
    data = np.random.rand(len(SAMPLES), len(FEATURES))
    df = pd.DataFrame(data, index=SAMPLES, columns=FEATURES)
    
    corr_matrix = df.corr()
    ax = sns.heatmap(corr_matrix, annot=True)
    
    return df, ax

import unittest
import pandas as pd
import matplotlib.pyplot as plt

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        df, ax = f_500()
        self.assertEqual(df.shape, (100, 5))
        self.assertIsInstance(ax, plt.Axes)
        
    def test_case_2(self):
        df, ax = f_500(10, 3)
        self.assertEqual(df.shape, (10, 3))
        self.assertIsInstance(ax, plt.Axes)

    def test_case_3(self):
        df, ax = f_500(50, 2)
        self.assertEqual(df.shape, (50, 2))
        self.assertIsInstance(ax, plt.Axes)
        
    def test_case_4(self):
        df, ax = f_500(150, 6)
        self.assertEqual(df.shape, (150, 6))
        self.assertIsInstance(ax, plt.Axes)
        
    def test_case_5(self):
        df, ax = f_500(5, 10)
        self.assertEqual(df.shape, (5, 10))
        self.assertIsInstance(ax, plt.Axes)


if __name__ == "__main__":
    run_tests()