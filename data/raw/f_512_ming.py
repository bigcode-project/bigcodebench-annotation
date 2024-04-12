import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def f_512(dataframe, target_value):
    '''
    Searches a given DataFrame for rows with cells equal to the provided target value.
    It then plots the count of such rows per column.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame to be searched.
    - target_value (str): The target value to be searched in the DataFrame.

    Returns:
    tuple: A tuple containing:
        - A pandas Series with counts of the target value per column.
        - A matplotlib Axes object representing the plot (None if dataframe is empty).

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame({
            'Column1': ['0', 'a', '332', '33'],
            'Column2': ['1', 'bb', '33', '22'],
            'Column3': ['2', 'ccc', '2', '332']
        })
    >>> series, ax = f_512(df, '332')
    '''
    # Convert dataframe to string type for uniform comparison
    dataframe = dataframe.astype(str)
    
    counts = dataframe.apply(lambda x: (x == target_value).sum())

    # Check if DataFrame is empty
    if not dataframe.empty:
        ax = counts.plot(kind='bar')
    else:
        ax = None

    return counts, ax
    

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test case with default example data
        df = pd.DataFrame({
            'Column1': ['0', 'a', '332', '33'],
            'Column2': ['1', 'bb', '33', '22'],
            'Column3': ['2', 'ccc', '2', '332']
        })
        counts, ax = f_512(df, '332')
        self.assertEqual(counts['Column1'], 1)
        self.assertEqual(counts['Column2'], 0)
        self.assertEqual(counts['Column3'], 1)

    def test_case_2(self):
        # Test case with no occurrences of the target value
        df = pd.DataFrame({
            'Column1': ['0', 'a', '331', '33'],
            'Column2': ['1', 'bb', '33', '22'],
            'Column3': ['2', 'ccc', '2', '331']
        })
        counts, ax = f_512(df, '332')
        self.assertEqual(counts['Column1'], 0)
        self.assertEqual(counts['Column2'], 0)
        self.assertEqual(counts['Column3'], 0)

    def test_case_3(self):
        # Test case with multiple occurrences of the target value in a single column
        df = pd.DataFrame({
            'Column1': ['332', 'a', '332', '33'],
            'Column2': ['1', '332', '332', '22'],
            'Column3': ['2', '332', '2', '332']
        })
        counts, ax = f_512(df, '332')
        self.assertEqual(counts['Column1'], 2)
        self.assertEqual(counts['Column2'], 2)
        self.assertEqual(counts['Column3'], 2)

    def test_case_4(self):
        # Test case with an empty DataFrame
        df = pd.DataFrame()
        counts, ax = f_512(df, '332')
        self.assertEqual(len(counts), 0)

    def test_case_5(self):
        # Test case with different data types in the DataFrame
        df = pd.DataFrame({
            'Column1': [0, 'a', 332, '33'],
            'Column2': [1.0, 'bb', 33.0, 22.2],
            'Column3': [2, 'ccc', 2, 332]
        })
        counts, ax = f_512(df, '332')
        self.assertEqual(counts['Column1'], 1)
        self.assertEqual(counts['Column2'], 0)
        self.assertEqual(counts['Column3'], 1)


if __name__ == '__main__':
    run_tests()
