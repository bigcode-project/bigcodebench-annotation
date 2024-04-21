import pandas as pd
import matplotlib.pyplot as plt

def f_242(df, dct, columns=None, plot_histograms=False):
    '''
    Replace values in a DataFrame with a dictionary mapping and optionally record histograms for specified columns.
    
    Parameters:
    df (DataFrame): The input DataFrame.
    dct (dict): A dictionary for replacing values in df.
    columns (list of str, optional): List of column names to plot histograms. If None, no histograms are plotted.
    plot_histograms (bool): If True, plots histograms for specified columns.

    Returns:
    DataFrame: The DataFrame with replaced values.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame({'column1': [1, 2, 3, 4, 5], 'column2': [6, 7, 8, 9, 10]})
    >>> dct = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'v', 7: 'w', 8: 'x', 9: 'y', 10: 'z'}
    >>> modified_df = f_242(df, dct, ['column1', 'column2'], True)
    >>> print(modified_df)
    DataFrame with replaced values and histograms plotted for 'column1' and 'column2'.
    '''
    
    # Replace values using dictionary mapping
    df_replaced = df.replace(dct)
    
    # Plot a histogram for each specified column
    if plot_histograms and columns:
        for column in columns:
            if column in df_replaced:
                df_replaced[column].plot.hist(bins=50)
                plt.title(column)

    return df_replaced

import pandas as pd
import unittest
class TestCases(unittest.TestCase):
    def test_basic_functionality(self):
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        dct = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
        expected_df = pd.DataFrame({'col1': ['a', 'b'], 'col2': ['c', 'd']})
        result_df = f_242(df, dct)
        pd.testing.assert_frame_equal(result_df, expected_df)
    def test_complex_dataframe(self):
        df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8], 'col3': [9, 10, 11, 12]})
        dct = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l'}
        expected_df = pd.DataFrame({'col1': ['a', 'b', 'c', 'd'], 'col2': ['e', 'f', 'g', 'h'], 'col3': ['i', 'j', 'k', 'l']})
        result_df = f_242(df, dct)
        pd.testing.assert_frame_equal(result_df, expected_df)
    def test_empty_dataframe(self):
        df = pd.DataFrame()
        dct = {1: 'a', 2: 'b'}
        result_df = f_242(df, dct)
        pd.testing.assert_frame_equal(result_df, df)
    def test_columns_not_in_dataframe(self):
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        dct = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
        result_df = f_242(df, dct, columns=['col3', 'col4'], plot_histograms=True)
        pd.testing.assert_frame_equal(result_df, df.replace(dct))
    def test_histogram_plotting(self):
        df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        dct = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
        result_df = f_242(df, dct, columns=['col3', 'col4'], plot_histograms=True)
        # Since actual plot inspection is not feasible, assume histograms are correctly plotted if no errors are raised
        pd.testing.assert_frame_equal(result_df, df.replace(dct))
