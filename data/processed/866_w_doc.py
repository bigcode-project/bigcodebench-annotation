import pandas as pd
import numpy as np

def task_func(fruit_data):
    """
    Calculate and return the total and average counts for each type of fruit.

    This function takes a list of tuples, each containing a fruit name and its count, 
    then calculates the total count and the average count for each type of fruit. 
    The results are returned as a pandas DataFrame with each row representing a different fruit.

    If fruit_data is an empty list, an empty dataFrame is returned.

    Parameters:
    fruit_data (list of tuples): Each tuple contains a string representing the fruit name and an integer for the count.

    Returns:
    DataFrame: A pandas DataFrame with two columns: 'Total Count' and 'Average Count'. 
               Each row's index is the fruit name.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> fruit_list = [('apple', 5), ('banana', 3), ('apple', 6), ('banana', 4), ('cherry', 5), ('banana', 2), ('apple', 4), ('cherry', 5)]
    >>> report = task_func(fruit_list)
    >>> report.sort_index(inplace=True)
    >>> print(report)
            Total Count  Average Count
    apple            15            5.0
    banana            9            3.0
    cherry           10            5.0

    >>> fruit = [('apple', 1), ('orange', 25), ('apple', 111)]
    >>> df = task_func(fruit)
    >>> df.sort_index(inplace=True)
    >>> print(df)
            Total Count  Average Count
    apple           112           56.0
    orange           25           25.0
    """
    if len(fruit_data) == 0:
        return pd.DataFrame()
    fruits, counts = zip(*fruit_data)
    fruits = unique_values = list(set(fruits))
    total_counts = {fruit: np.sum([count for fruit_, count in fruit_data if fruit_ == fruit])
                  for fruit in fruits}
    avg_counts = {fruit: np.mean([count for fruit_, count in fruit_data if fruit_ == fruit])
                  for fruit in fruits}
    report_df = pd.DataFrame(list(zip(total_counts.values(), avg_counts.values())),
                             index=fruits,
                             columns=['Total Count', 'Average Count'])
    return report_df

import unittest
import pandas as pd
import numpy as np
class TestCases(unittest.TestCase):
    test_data_sets = [
        [('vote', 19), ('those', 15), ('recent', 4), ('manage', 12), ('again', 13), ('box', 16), ('box', 16), ('box', 16)],
        [('experience', 14), ('interesting', 8), ('firm', 13), ('enjoy', 19), ('area', 3), ('what', 12), ('along', 1)],
        [('our', 11), ('then', 2), ('imagine', 6), ('heavy', 17), ('low', 6), ('site', 12), ('nearly', 3), ('organization', 6), ('me', 14), ('eat', 17)],
        [('involve', 2), ('money', 11), ('use', 15), ('fish', 19), ('boy', 3), ('both', 10)], [('take', 16), ('activity', 12), ('tend', 10), ('take', 2)]
    ]
    def test_empty(self):
        report = task_func([])
        self.assertTrue(report.empty)
    def test_case_1(self):
        # Using the first set of test data
        report = task_func(self.test_data_sets[0])
        expected = pd.DataFrame(
            {
            'Total Count': {'vote': 19,
            'those': 15,
            'recent': 4,
            'manage': 12,
            'again': 13,
            'box': 48},
            'Average Count': {'vote': 19.0,
            'those': 15.0,
            'recent': 4.0,
            'manage': 12.0,
            'again': 13.0,
            'box': 16.0}
            }
        )
        # The report should be a DataFrame with the correct columns and index
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)
    def test_case_2(self):
        # Using the second set of test data
        report = task_func(self.test_data_sets[1])
        expected = pd.DataFrame(
            {'Total Count': {'experience': 14.0,
                'interesting': 8.0,
                'firm': 13.0,
                'enjoy': 19.0,
                'area': 3.0,
                'what': 12.0,
                'along': 1.0},
                'Average Count': {'experience': 14.0,
                'interesting': 8.0,
                'firm': 13.0,
                'enjoy': 19.0,
                'area': 3.0,
                'what': 12.0,
                'along': 1.0}}
        )
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        # The report should be a DataFrame with the correct columns and index
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)
    def test_case_3(self):
        # Using the third set of test data
        report = task_func(self.test_data_sets[2])
        expected = pd.DataFrame(
            {'Total Count': {'our': 11.0,
            'then': 2.0,
            'imagine': 6.0,
            'heavy': 17.0,
            'low': 6.0,
            'site': 12.0,
            'nearly': 3.0,
            'organization': 6.0,
            'me': 14.0,
            'eat': 17.0},
            'Average Count': {'our': 11.0,
            'then': 2.0,
            'imagine': 6.0,
            'heavy': 17.0,
            'low': 6.0,
            'site': 12.0,
            'nearly': 3.0,
            'organization': 6.0,
            'me': 14.0,
            'eat': 17.0}}
        )
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)
    def test_case_4(self):
        # Using the fourth set of test data
        report = task_func(self.test_data_sets[3])
        expected = pd.DataFrame(
            {'Total Count': {'involve': 2.0,
            'money': 11.0,
            'use': 15.0,
            'fish': 19.0,
            'boy': 3.0,
            'both': 10.0},
            'Average Count': {'involve': 2.0,
            'money': 11.0,
            'use': 15.0,
            'fish': 19.0,
            'boy': 3.0,
            'both': 10.0}}
        )
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)
    def test_case_5(self):
        # Using the fifth set of test data
        report = task_func(self.test_data_sets[4])
        expected = pd.DataFrame(
            {'Total Count': {'take': 18.0, 'activity': 12.0, 'tend': 10.0},
            'Average Count': {'take': 9.0, 'activity': 12.0, 'tend': 10.0}}
        )
        report.sort_index(inplace=True)
        expected.sort_index(inplace=True)
        self.assertIsInstance(report, pd.DataFrame)
        self.assertListEqual(list(report.columns), ['Total Count', 'Average Count'])
        pd.testing.assert_frame_equal(report, expected, check_dtype=False)
