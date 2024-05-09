import pandas as pd
import numpy as np

DEFAULT_COLUMNS = ['Element', 'Count']


def f_201(elements, include_index=False):
    """
    Constructs a DataFrame that enumerates the character counts of each string in a provided list of elements. This
    function can optionally include an index column for each row in the DataFrame.

    Parameters:
    elements (List[str]): A list of strings whose character counts are to be calculated.
    include_index (bool): Flag to decide whether to add an index column in the resulting DataFrame.

    Returns: DataFrame: Returns a pandas DataFrame with columns for elements and their respective character counts.
    Includes an 'Index' column if requested.

    Requirements:
    - pandas
    - numpy

    Note:
    The order of columns in the returned DataFrame will be ['Index', 'Element', 'Count'] if the index is included.

    Example:
    >>> result = f_201(['abc', 'def'], include_index=True)
    >>> print(result.to_string(index=False))
     Index Element  Count
         0     abc      3
         1     def      3
    """
    elements_series = pd.Series(elements)
    count_series = elements_series.apply(lambda x: len(x))
    data_dict = {'Element': elements_series, 'Count': count_series}
    if include_index:
        data_dict['Index'] = np.arange(len(elements))
    count_df = pd.DataFrame(data_dict)
    if include_index:
        count_df = count_df[['Index', 'Element', 'Count']]  # Reordering columns to put 'Index' first
    return count_df


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_case_1(self):
        result = f_201(['hello'])
        expected = pd.DataFrame({'Element': ['hello'], 'Count': [5]})
        pd.testing.assert_frame_equal(result, expected)

    def test_case_2(self):
        result = f_201(['a', 'bc', 'def'])
        expected = pd.DataFrame({'Element': ['a', 'bc', 'def'], 'Count': [1, 2, 3]})
        pd.testing.assert_frame_equal(result, expected)

    def test_case_3(self):
        result = f_201(['zzz', 'zzz'])
        expected = pd.DataFrame({'Element': ['zzz', 'zzz'], 'Count': [3, 3]})
        pd.testing.assert_frame_equal(result, expected)

    def test_case_4(self):
        result = f_201(['hello world', 'open ai'])
        expected = pd.DataFrame({'Element': ['hello world', 'open ai'], 'Count': [11, 7]})
        pd.testing.assert_frame_equal(result, expected)

    def test_case_5(self):
        result = f_201(['hello', 'world'], include_index=True)
        expected = pd.DataFrame({'Index': np.array([0, 1], dtype='int64'), 'Element': ['hello', 'world'], 'Count': [5, 5]})
        pd.testing.assert_frame_equal(result, expected)


if __name__ == "__main__":
    run_tests()
