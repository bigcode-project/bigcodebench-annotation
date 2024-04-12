import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f_445(array_length=100):
    '''
    Generate two arrays of random numbers of a given length, calculate their mean, median, and standard deviation, 
    and draw a bar chart to compare these statistics.

    Args:
    - array_length (int, optional): The length of the arrays to be generated. Default is 100.

    Returns:
    - DataFrame: A pandas DataFrame with the statistics of the arrays.
    - Axes: The bar chart plot comparing the statistics.

    Requirements:
    - numpy
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df, ax = f_445(50)
    '''
    array1 = np.random.rand(array_length)
    array2 = np.random.rand(array_length)

    statistics = {
        'Array1': [np.mean(array1), np.median(array1), np.std(array1)],
        'Array2': [np.mean(array2), np.median(array2), np.std(array2)]
    }

    df = pd.DataFrame(statistics, index=['Mean', 'Median', 'Standard Deviation'])
    ax = df.plot(kind='bar')

    return df, ax
    

import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestArrayStatistics))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestArrayStatistics(unittest.TestCase):
    
    def test_default_length(self):
        df, ax = f_445()
        self.assertEqual(df.shape, (3, 2))
        self.assertTrue(all(df.index == ['Mean', 'Median', 'Standard Deviation']))
        self.assertTrue(all(df.columns == ['Array1', 'Array2']))
        self.assertIsInstance(ax, plt.Axes)
    
    def test_custom_length(self):
        df, ax = f_445(200)
        self.assertEqual(df.shape, (3, 2))
        self.assertTrue(all(df.index == ['Mean', 'Median', 'Standard Deviation']))
        self.assertTrue(all(df.columns == ['Array1', 'Array2']))
        self.assertIsInstance(ax, plt.Axes)
    
    def test_statistics_values(self):
        np.random.seed(42)  # Setting seed for reproducibility
        df, _ = f_445(1000)
        self.assertAlmostEqual(df['Array1']['Mean'], 0.4903, places=3)
        self.assertAlmostEqual(df['Array2']['Mean'], 0.5068, places=3)
        self.assertAlmostEqual(df['Array1']['Median'], 0.4968, places=3)
        self.assertAlmostEqual(df['Array2']['Median'], 0.5187, places=3)
        self.assertAlmostEqual(df['Array1']['Standard Deviation'], 0.2920, places=3)
        self.assertAlmostEqual(df['Array2']['Standard Deviation'], 0.2921, places=3)
    
    def test_negative_length(self):
        with self.assertRaises(ValueError):
            f_445(-50)
    
    def test_zero_length(self):
        df, ax = f_445(0)
        self.assertEqual(df.shape, (3, 2))
        self.assertTrue(all(df.index == ['Mean', 'Median', 'Standard Deviation']))
        self.assertTrue(all(df.columns == ['Array1', 'Array2']))
        self.assertIsInstance(ax, plt.Axes)


if __name__ == '__main__':
    run_tests()