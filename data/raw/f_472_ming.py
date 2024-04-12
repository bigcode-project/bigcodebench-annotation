import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import sample
import unittest

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def f_472(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on values of multiple columns, 
    and then create n random line plots of two columns against each other.

    Parameters:
    - df (pd.DataFrame): The input pandas DataFrame.
    - tuples (list of tuple): A list of tuples, each tuple represents values in a row to be removed.
    - n_plots (int): The number of line plots to generate.

    Returns:
    - (pd.DataFrame, list): A tuple containing the modified DataFrame and a list of plot details.
      Each entry in the plot details list is a tuple containing the two columns plotted against each other.

    Requirements:
    - pandas for DataFrame manipulation.
    - numpy for array operations.
    - matplotlib.pyplot for plotting.
    - random for selecting random elements.

    Example:
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plot_details = f_472(df, tuples, 3)
    """
    mask = df.apply(tuple, axis=1).isin(tuples)
    df = df[~mask]

    plot_details = []
    for _ in range(min(n_plots, len(df))):
        selected_columns = sample(COLUMNS, 2)
        df.plot(x=selected_columns[0], y=selected_columns[1], kind='line')
        plot_details.append((selected_columns[0], selected_columns[1]))

    plt.show()

    return df, plot_details

# Unit test class
class TestF472(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))
        self.tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]

    def test_basic_functionality(self):
        modified_df, plot_details = f_472(self.df, self.tuples, 3)

        # Convert DataFrame rows to tuples for comparison
        df_tuples = set([tuple(x) for x in modified_df.to_numpy()])

        # Convert list of tuples to a set for efficient searching
        tuples_to_remove = set(self.tuples)

        # Check that none of the tuples to remove are in the modified DataFrame
        intersection = df_tuples.intersection(tuples_to_remove)
        self.assertTrue(len(intersection) == 0, f"Removed tuples found in the modified DataFrame: {intersection}")

    def test_empty_dataframe(self):
        empty_df = pd.DataFrame(columns=list('ABCDE'))
        modified_df, plot_details = f_472(empty_df, [], 1)
        self.assertTrue(modified_df.empty)

    def test_zero_plots(self):
        modified_df, plot_details = f_472(self.df, [], 0)
        self.assertEqual(len(plot_details), 0)

    def test_more_plots_than_data(self):
        modified_df, plot_details = f_472(self.df.iloc[:5], [], 10)
        self.assertTrue(len(plot_details) <= 5)

    def test_plot_details(self):
        _, plot_details = f_472(self.df, [], 3)
        self.assertEqual(len(plot_details), 3)
        all_columns = all(c[0] in COLUMNS and c[1] in COLUMNS for c in plot_details)
        self.assertTrue(all_columns)

if __name__ == '__main__':
    unittest.main()
