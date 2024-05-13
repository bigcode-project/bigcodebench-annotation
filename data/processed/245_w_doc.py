import pandas as pd
import random
from scipy import stats

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    """
    Generate a random dataset of floating-point numbers within a specified range, 
    truncate each value to 3 decimal places, and calculate statistical measures (mean, median, mode) of the data.
    
    Parameters:
    n_data_points (int): Number of data points to generate. Default is 5000.
    min_value (float): Minimum value range for data points. Default is 0.0.
    max_value (float): Maximum value range for data points. Default is 10.0.

    Returns:
    dict: A dictionary with keys 'mean', 'median', 'mode' and their corresponding calculated values.
    
    Requirements:
    - pandas
    - random
    - scipy.stats

    Example:
    >>> random.seed(0)
    >>> stats = task_func(1000, 5.0, 5.0)
    >>> print(stats)
    {'mean': 5.0, 'median': 5.0, 'mode': 5.0}
    """

    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])
    mean = data_df['Value'].mean()
    median = data_df['Value'].median()
    mode = stats.mode(data_df['Value'].values)[0][0]
    return {'mean': mean, 'median': median, 'mode': mode}

import unittest
import random
class TestCases(unittest.TestCase):
    def test_default_parameters(self):
        random.seed(0)
        result = task_func()
        self.assertIn('mean', result)
        self.assertIn('median', result)
        self.assertIn('mode', result)
    def test_custom_range(self):
        random.seed(0)
        result = task_func(1000, 1.0, 5.0)
        self.assertGreaterEqual(result['mean'], 1.0)
        self.assertLessEqual(result['mean'], 5.0)
        self.assertGreaterEqual(result['median'], 1.0)
        self.assertLessEqual(result['median'], 5.0)
        self.assertGreaterEqual(result['mode'], 1.0)
        self.assertLessEqual(result['mode'], 5.0)
    def test_small_dataset(self):
        random.seed(0)
        result = task_func(10, 2.0, 2.0)
        self.assertEqual(result['mean'], 2.0)
        self.assertEqual(result['median'], 2.0)
        self.assertEqual(result['mode'], 2.0)
    def test_large_dataset(self):
        random.seed(0)
        result = task_func(10000, 0.0, 100.0)
        self.assertTrue(0.0 <= result['mean'] <= 100.0)
        self.assertTrue(0.0 <= result['median'] <= 100.0)
        self.assertTrue(0.0 <= result['mode'] <= 100.0)
    def test_single_value_range(self):
        random.seed(0)
        result = task_func(100, 5.0, 5.0)
        self.assertEqual(result['mean'], 5.0)
        self.assertEqual(result['median'], 5.0)
        self.assertEqual(result['mode'], 5.0)
