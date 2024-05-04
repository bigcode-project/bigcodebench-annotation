import pandas as pd
import numpy as np

def f_508(d):
    """
    Calculate mean, sum, max, min and standard deviation for the keys "x," "y" and "z" from a list of dictionaries "d."
    
    Parameters:
    d (list): A list of dictionaries.

    Returns:
    dict: A dictionary with keys as 'x', 'y', and 'z' and values as dictionaries of statistics.

    Raises:
    - ValueError: If input is not a list of dictionaries.

    Requirements:
    - pandas
    - numpy

    Examples:
    >>> data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
    >>> f_508(data)
    {'x': {'mean': 2.0, 'sum': 6, 'max': 3, 'min': 1, 'std': 0.816496580927726}, 'y': {'mean': 8.666666666666666, 'sum': 26, 'max': 15, 'min': 1, 'std': 5.792715732327589}, 'z': {'mean': 6.0, 'sum': 18, 'max': 7, 'min': 5, 'std': 0.816496580927726}}
    >>> f_508([])
    {'x': None, 'y': None, 'z': None}
    >>> f_508([{'a': 1}])
    {'x': None, 'y': None, 'z': None}
    """
    if not isinstance(d, list) or any(not isinstance(item, dict) for item in d):
        raise ValueError("Input must be a list of dictionaries.")
    if not d:
        return {key: None for key in ['x', 'y', 'z']}
    df = pd.DataFrame(d).fillna(0)  # Replace missing values with 0 to allow computations
    stats = {}
    for key in ['x', 'y', 'z']:
        if key in df.columns:
            stats[key] = {
                'mean': np.mean(df[key]),
                'sum': np.sum(df[key]),
                'max': np.max(df[key]),
                'min': np.min(df[key]),
                'std': np.std(df[key], ddof=0)  # Population standard deviation
            }
        else:
            stats[key] = None
    return stats

# Test suite
import unittest
class TestCases(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(f_508([]), {'x': None, 'y': None, 'z': None})
    def test_valid_input(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        result = f_508(data)
        self.assertAlmostEqual(result['x']['mean'], 2.0)
        self.assertAlmostEqual(result['y']['mean'], 8.666666666666666)
        self.assertAlmostEqual(result['z']['mean'], 6.0)
    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            f_508("not a list")
    def test_partial_keys(self):
        data = [{'x': 1, 'y': 2}, {'y': 3, 'z': 4}]
        result = f_508(data)
        self.assertIsNotNone(result['x'])
        self.assertIsNotNone(result['y'])
        self.assertIsNotNone(result['z'])
    def test_all_keys_missing(self):
        data = [{'a': 1}, {'b': 2}]
        self.assertEqual(f_508(data), {'x': None, 'y': None, 'z': None})
