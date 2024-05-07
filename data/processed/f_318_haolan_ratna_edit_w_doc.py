import numpy as np
import matplotlib.pyplot as plt

# Constants
COLORS = ['r', 'g', 'b']

def f_520(df, group_col, value_col, group_name):
    """
    Create a bar subplot of a specific group from the input dataframe.

    Parameters:
    - df (DataFrame): The input DataFrame containing the data.
    - group_col (str): The name of the column to group the data by.
    - value_col (str): The name of the column containing the values to plot.
    - group_name (str): The name of the group to plot.

    Returns:
    - Axes: A matplotlib axes object with the bar chart.

    Requirements:
    - matplotlib.pyplot
    - numpy

    Note:
    - The title of the plot will be 'Bar chart of [value_col] for [group_name]'.
    - The x-axis label will be the name of the grouping column [group_col].
    - The y-axis label will be the name of the value column [value_col].

    Raises:
    - Raise ValueError if the group_name does not exist in df.

    Example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({'Group': ['A', 'B', 'C'], 'Value': [10, 20, 30]})
    >>> ax = f_520(df, 'Group', 'Value', 'B')
    >>> num_bars = len(ax.containers[0])  # Number of bars in the plot
    >>> num_bars == 1  # There should be 1 bar in the plot for group 'B'
    True
    >>> ax.containers[0][0].get_height() == 20 # The bar height of Group B should be 20
    True
    >>> plt.close()
    """
    group_data = df[df[group_col] == group_name]
    if group_data.empty:
        raise ValueError
    fig, ax = plt.subplots()
    num_bars = len(group_data)
    bar_width = 0.35
    index = np.arange(num_bars)
    bars = ax.bar(index, group_data[value_col], bar_width, color=COLORS[:num_bars])
    ax.set_xlabel(group_col)
    ax.set_ylabel(value_col)
    ax.set_title(f'Bar chart of {value_col} for {group_name}')
    ax.set_xticks(index)
    ax.set_xticklabels(group_data[group_col])
    return ax

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker
faker = Faker()
# Constants
COLORS = ['r', 'g', 'b']
class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'Group': ['A', 'B', 'C'], 'Value': [10, 20, 30]})
        
    def test_single_group_bar_chart(self):
        ax = f_520(self.df, 'Group', 'Value', 'B')
        num_bars = len(ax.containers[0])  # Number of bars in the plot
        self.assertEqual(num_bars, 1)  # There should be 1 bar in the plot for group 'B'
        plt.close()
    def test_missing_group(self):
        with self.assertRaises(ValueError):
            ax = f_520(self.df, 'Group', 'Value', 'D')  # Group 'D' does not exist in the DataFrame
        plt.close()
    def test_correct_labels(self):
        ax = f_520(self.df, 'Group', 'Value', 'B')
        self.assertEqual(ax.get_xlabel(), 'Group')  # x-axis label should be 'Group'
        self.assertEqual(ax.get_ylabel(), 'Value')  # y-axis label should be 'Value'
        plt.close()
    def test_inline_points(self):
        ax = f_520(self.df, 'Group', 'Value', 'B')
        bars = ax.containers[0]
        for bar in bars:
            self.assertAlmostEqual(bar.get_height(), 20, delta=0.01)  # Check if points are inline
        plt.close()
    
    
    def test_inline_points(self):
        ax = f_520(self.df, 'Group', 'Value', 'C')
        bars = ax.containers[0]
        for bar in bars:
            self.assertAlmostEqual(bar.get_height(), 30, delta=0.01)  # Check if points are inline
        plt.close()
def generate_complex_test_data(num_rows=100):
    """Generate a DataFrame with a mix of numeric and text data, including some potential outliers."""
    data = {
        'Group': [faker.random_element(elements=('A', 'B', 'C', 'D')) for _ in range(num_rows)],
        'Value': [faker.random_int(min=0, max=1000) for _ in range(num_rows)]
    }
    complex_df = pd.DataFrame(data)
    return complex_df
