import numpy as np
import pandas as pd
from datetime import datetime

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

def f_650(result):
    """
    Calculate the mean, median, min, max, and standard deviation of the "from_user" values in "result" 
    and add the current date and time in the format YYYY-mm-dd HHL:MM:SS to the summary.
    The global constant DATE_FORMAT is used to transform the currnet date and time into this format.

    Parameters:
    result (list of dict): A list of dictionaries containing the key "from_user" whose numeric values are to be analyzed.

    Returns:
    Series: A pandas Series with the statistical summary, including 'mean', 'median', 'min', 'max', 'std', and 'current_time'.

    Data Structures:
    - Uses numpy arrays for efficient statistical computations.

    Raises:
    - ValueError: If the "from_user" values are not numeric.

    Requirements:
    - numpy
    - pandas
    - datetime

    Example:
    >>> result = [{"hi": 7, "bye": 4, "from_user": 0}, {"from_user": 0}, {"from_user": 1}]
    >>> f_650(result)
    mean                  0.333333
    median                0.0
    min                   0.0
    max                   1.0
    std                   0.471405
    current_time          2023-10-10 12:23:45  # Note: This time will vary based on when the function is run
    dtype: object

    >>> result = [{"test": 7, "hallo": 4, "from_user": 1.3},
    >>>           {"from_user": 2},
    >>>           {"from_user": 4.6},
    >>>           {"from_user": -2.3, "b": 1},
    >>>           {"a": "test", "from_user": 12.12},
    >>>          ]
    >>> summary = f_650(result)
    >>> summary
    mean                          3.544
    median                          2.0
    min                            -2.3
    max                           12.12
    std                        4.821508
    current_time    2023-11-28 13:21:07
    dtype: object
    """
    from_user_values = np.array([d['from_user'] for d in result if 'from_user' in d])
    # Handle edge case of empty array
    if len(from_user_values) == 0:
        summary = {
            'mean': np.nan,
            'median': np.nan,
            'min': np.nan,
            'max': np.nan,
            'std': np.nan,
            'current_time': datetime.now().strftime(DATE_FORMAT)
        }
    
    elif not np.issubdtype(from_user_values.dtype, np.number):
         raise ValueError("from_user values should be numeric only.")


    else:
        summary = {
            'mean': np.mean(from_user_values),
            'median': np.median(from_user_values),
            'min': np.min(from_user_values),
            'max': np.max(from_user_values),
            'std': np.std(from_user_values),
            'current_time': datetime.now().strftime(DATE_FORMAT)
        }

    summary_series = pd.Series(summary)
    return summary_series

import unittest
import numpy as np

class TestCases(unittest.TestCase):

    def test_case_non_numeric(self):
        result = [{'from_user': 'a'}, {'from_user': 1}]
        self.assertRaises(Exception, f_650, result)

    def test_case_1(self):
        result = [{"hi": 7, "bye": 4, "from_user": 0}, {"from_user": 0}, {"from_user": 1}]
        summary = f_650(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertAlmostEqual(summary['mean'], 0.333333, places=5)
        self.assertEqual(summary['median'], 0.0)
        self.assertEqual(summary['min'], 0.0)
        self.assertEqual(summary['max'], 1.0)
        self.assertAlmostEqual(summary['std'], 0.471405, places=5)

    def test_case_2(self):
        result = [{"from_user": 1}, {"from_user": 2}, {"from_user": 3}]
        summary = f_650(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertEqual(summary['mean'], 2.0)
        self.assertEqual(summary['median'], 2.0)
        self.assertEqual(summary['min'], 1.0)
        self.assertEqual(summary['max'], 3.0)
        self.assertAlmostEqual(summary['std'], 0.816497, places=5)

    def test_case_3(self):
        result = [{"from_user": 5}]
        summary = f_650(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertEqual(summary['mean'], 5.0)
        self.assertEqual(summary['median'], 5.0)
        self.assertEqual(summary['min'], 5.0)
        self.assertEqual(summary['max'], 5.0)
        self.assertEqual(summary['std'], 0.0)

    def test_case_4(self):
        result = [{"hello": 2}, {"world": 3}]
        summary = f_650(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertTrue(np.isnan(summary['mean']))
        self.assertTrue(np.isnan(summary['median']))
        self.assertTrue(np.isnan(summary['min']))
        self.assertTrue(np.isnan(summary['max']))
        self.assertTrue(np.isnan(summary['std']))

    def test_case_5(self):
        'empty list'
        result = []
        summary = f_650(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertTrue(np.isnan(summary['mean']))
        self.assertTrue(np.isnan(summary['median']))
        self.assertTrue(np.isnan(summary['min']))
        self.assertTrue(np.isnan(summary['max']))
        self.assertTrue(np.isnan(summary['std']))
    
    
    def test_case_6(self):
        'float'
        result = [{"hi": 7, "bye": 4, "from_user": 0.3},
                  {"from_user": 0.1},
                  {"from_user": 15.6},
                  {"from_user": -2.3},
                  {"from_user": 12.12},
                  {"from_user": -25.234},
                  {"from_user": 124.2},
                  ]
        summary = f_650(result)
        current_time = datetime.now().strftime(DATE_FORMAT)[:-3]
        self.assertEqual(summary['current_time'][:-3], current_time)
        self.assertAlmostEqual(summary['mean'], 17.826571, places=5)
        self.assertEqual(summary['median'], 0.3)
        self.assertEqual(summary['min'], -25.234)
        self.assertEqual(summary['max'], 124.2)
        self.assertAlmostEqual(summary['std'], 45.092813, places=5)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()