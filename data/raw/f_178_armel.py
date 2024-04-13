import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def f_178(rows=100, columns=['A', 'B', 'C', 'D', 'E']):
    """
    Generate a pandas DataFrame with random values and then visualize the correlation matrix of this DataFrame using the seaborn heatmap.
    
    Parameters:
    - rows (int): Number of rows for the DataFrame. Default is 100.
    - columns (list): List of column names for the DataFrame. Default is ['A', 'B', 'C', 'D', 'E'].
    
    Returns:
    tuple: A tuple containing:
        - DataFrame: The generated DataFrame.
        - matplotlib.axes._axes.Axes: The seaborn heatmap Axes object.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - seaborn
    - numpy

    Example:
    >>> df, ax = f_178(rows=5, columns=['X', 'Y', 'Z'])
    >>> print(df)
          X         Y         Z
    0  0.42345  0.98234  0.23423
    1  0.89234  0.12345  0.56432
    2  0.12345  0.65432  0.34561
    3  0.67890  0.23456  0.23456
    4  0.78901  0.34567  0.56789
    """
    df = pd.DataFrame(np.random.rand(rows, len(columns)), columns=columns)
    corr_matrix = df.corr()
    plt.figure()
    ax = sns.heatmap(corr_matrix, annot=True)
    return df, ax

import unittest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    """Test cases for the f_178 function."""
    def test_case_1(self):
        df, ax = f_178()
        self.assertEqual(df.shape, (100, 5))
        self.assertListEqual(list(df.columns), ['A', 'B', 'C', 'D', 'E'])
        
    def test_case_2(self):
        df, ax = f_178(rows=10, columns=['X', 'Y'])
        self.assertEqual(df.shape, (10, 2))
        self.assertListEqual(list(df.columns), ['X', 'Y'])
        
    def test_case_3(self):
        df, ax = f_178(rows=5, columns=['P', 'Q', 'R'])
        self.assertEqual(df.shape, (5, 3))
        self.assertListEqual(list(df.columns), ['P', 'Q', 'R'])
        
    def test_case_4(self):
        df, ax = f_178(rows=50, columns=['M', 'N', 'O', 'P'])
        self.assertEqual(df.shape, (50, 4))
        self.assertListEqual(list(df.columns), ['M', 'N', 'O', 'P'])
        
    def test_case_5(self):
        df, ax = f_178(rows=1, columns=['Z'])
        self.assertEqual(df.shape, (1, 1))
        self.assertListEqual(list(df.columns), ['Z'])

if __name__ == "__main__" :
    run_tests()