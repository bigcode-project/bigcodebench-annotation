import matplotlib
# Check and set the backend
print("Current backend:", matplotlib.get_backend())  # Optional: Check the current backend
matplotlib.use('Agg')  # Set to 'Agg' to avoid GUI-related issues
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def f_439(a, b, columns=['A', 'B']):
    """
    Standardize two lists of numbers using the StandardScaler from sklearn and visualize the standardized values using a bar plot.

    Parameters:
        a (list): A list of numbers.
        b (list): Another list of numbers.
        columns (list, optional): Column names for the resulting DataFrame. Defaults to ['A', 'B'].

    Returns:
        pd.DataFrame: A DataFrame containing the standardized values.
        matplotlib.axes.Axes: Axes object of the displayed bar plot.

    Requirements:
        - numpy
        - pandas
        - sklearn.preprocessing
        - matplotlib

    Example:
        >>> df, ax = f_439([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
        >>> isinstance(df, pd.DataFrame) and isinstance(ax, matplotlib.axes.Axes)
        True
    """
    # Handle empty input lists by returning an empty DataFrame and Axes object
    if len(a) == 0 or len(b) == 0:
        fig, ax = plt.subplots()
        plt.close(fig)  # Prevent empty plot from displaying
        return pd.DataFrame(), ax

    scaler = StandardScaler()
    standardized_values = scaler.fit_transform(np.array([a, b]).T)
    df = pd.DataFrame(standardized_values, columns=columns)

    ax = df.plot(kind='bar')
    plt.show()
    return df, ax


import unittest
import pandas as pd
import matplotlib


class TestCases(unittest.TestCase):
    def test_standard_case(self):
        """Test the function with non-empty lists."""
        df, ax = f_439([1, 2, 3], [4, 5, 6])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (3, 2))
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_empty_lists(self):
        """Test the function with empty lists."""
        df, ax = f_439([], [])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.empty, True)
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_unequal_length_lists(self):
        """Test the function with lists of unequal length. Expecting an exception."""
        with self.assertRaises(ValueError):
            f_439([1, 2, 3], [4, 5])

    def test_single_value_lists(self):
        """Test the function with single-value lists."""
        df, ax = f_439([1], [1])
        self.assertEqual(df.shape, (1, 2))
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_large_lists(self):
        """Test the function with large lists."""
        df, ax = f_439(list(range(100)), list(range(100, 200)))
        self.assertEqual(df.shape, (100, 2))
        self.assertIsInstance(ax, matplotlib.axes.Axes)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
