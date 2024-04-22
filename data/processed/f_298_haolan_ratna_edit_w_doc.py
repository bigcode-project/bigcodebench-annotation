import pandas as pd
import seaborn as sns

def f_298(df, col1, col2):
    """
    Draw a scatter plot with a regression line for two columns from a DataFrame.

    Parameters:
    df (DataFrame): Input DataFrame.
    col1 (str): Name of the first column.
    col2 (str): Name of the second column.

    Returns:
    Axes: A seaborn axes object.

    Requirements:
    - pandas
    - seaborn

    Raises:
    - Raise ValueError if the input df is not a DataFrame, empty, or does not contain the specified columns.
    - Raise TypeError if df use non-numeric data

    Example:
    >>> import matplotlib.pyplot as plt
    >>> df = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [2, 4, 6, 8, 10]})
    >>> plot = f_298(df, 'X', 'Y')
    >>> len(plot.collections[0].get_offsets().data)
    5
    >>> plt.close()
    """
    # Ensure that the df is DataFrame, not empty and the specified column exists
    if not isinstance(df, pd.DataFrame) or df.empty or col1 not in df.columns or col2 not in df.columns:
        raise ValueError("The DataFrame is empty or the specified column does not exist.")
    
    ax = sns.regplot(x=col1, y=col2, data=df)

    return ax

import unittest
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_numeric_data(self):
        # Create a DataFrame with numeric data
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [5, 4, 3, 2, 1]
        })
        # Call the function with the DataFrame
        ax = f_298(df, 'A', 'B')
        
        # Assertions to validate the output
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes, "The returned object should be a seaborn FacetGrid.")
        plt.close()
    def test_non_numeric_data(self):
        # Create a DataFrame with non-numeric data
        df = pd.DataFrame({
            'A': ['one', 'two', 'three', 'four', 'five'],
            'B': ['five', 'four', 'three', 'two', 'one']
        })
        # We expect a TypeError because non-numeric data can't be used to plot a regression line
        with self.assertRaises(TypeError, msg="The function should raise a TypeError for non-numeric data."):
            f_298(df, 'A', 'B')
        plt.close()
    def test_missing_data(self):
        # Create a DataFrame with missing data
        df = pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': [5, None, 3, 2, 1]
        })
        # Call the function with the DataFrame
        ax = f_298(df, 'A', 'B')
        # Assertions to validate the output
        # We expect the function to handle missing data according to seaborn's default behavior
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes, "The returned object should be a seaborn FacetGrid.")
        # Check if the data plotted is the same length as the original minus the NaNs
        non_na_length = df.dropna().shape[0]
        self.assertEqual(len(ax.collections[0].get_offsets().data), non_na_length)  # Check if there's only one data point in the collection
        plt.close()
    def test_large_dataset(self):
        # Create a large DataFrame
        df = pd.DataFrame({
            'A': range(10000),
            'B': range(10000, 20000)
        })
        # Call the function with the DataFrame
        ax = f_298(df, 'A', 'B')
        # Assertions to validate the output
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes, "The returned object should be a seaborn FacetGrid.")
        plt.close()
    def test_single_data_point(self):
        # Create a DataFrame with a single data point
        df = pd.DataFrame({
            'A': [1],
            'B': [1]
        })
        # Call the function with the DataFrame
        ax = f_298(df, 'A', 'B')
        # Assertions to validate the output
        self.assertIsInstance(ax, matplotlib.axes._axes.Axes, "The returned object should be a seaborn FacetGrid.")
        self.assertEqual(len(ax.collections), 1)  # Check if there's only one collection of points in the plot
        self.assertEqual(len(ax.collections[0].get_offsets()), 1)  # Check if there's only one data point in the collection
        plt.close()
    
    def test_non_df(self):
        with self.assertRaises(ValueError):
            f_298("non_df", 'A', 'B')
    
    def test_empty_df(self):
        with self.assertRaises(ValueError):
            f_298(pd.DataFrame(), 'A', 'B')
    def test_column_df(self):
        with self.assertRaises(ValueError):
            f_298(pd.DataFrame({'A': [1]}), 'A', 'B')
