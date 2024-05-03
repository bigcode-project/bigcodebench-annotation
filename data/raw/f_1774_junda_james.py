import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def f_1774(df, bins=20):
    """
    Draw a histogram of the last column of the DataFrame and return the plot.

    Parameters:
    - df (DataFrame): The input DataFrame, which must contain at least one column.
    - bins (int, optional): Number of bins for the histogram. Defaults to 20.

    Returns:
    - Axes: A Matplotlib Axes object representing the histogram of the last column. The histogram includes:
      - Title: 'Histogram of ' followed by the name of the last column.
      - X-axis label: 'Value'
      - Y-axis label: 'Frequency'

    Raises:
    - ValueError: If the input is not a DataFrame, or if the DataFrame is empty.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - numpy

    Example:
    >>> df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
    >>> ax = f_1774(df)
    >>> plt.show()
    """

    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("The input must be a non-empty pandas DataFrame.")

    last_col_name = df.columns[-1]
    fig, ax = plt.subplots()
    ax.hist(df[last_col_name], bins=bins)
    ax.set_title(f'Histogram of {last_col_name}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')

    return ax


import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        
    def test_return_type(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        ax = f_1774(df)
        self.assertIsInstance(ax, plt.Axes)

    def test_invalid_input_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_1774(pd.DataFrame())

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            f_1774("not a dataframe")

    def test_histogram_bins(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        ax = f_1774(df, bins=10)
        # plt.hist returns a tuple; to check the number of bins, we need to count the patches of the ax object
        self.assertEqual(len(ax.patches), 10)

    def test_plot_title_and_labels(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        ax = f_1774(df)
        self.assertIn('Histogram of ', ax.get_title())
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')

    def test_histogram_values(self):
        # Create a DataFrame with fixed values to ensure predictable histogram frequencies
        df = pd.DataFrame({'A': [1] * 10 + [2] * 20 + [3] * 30})
        ax = f_1774(df, bins=3)  # Bins set to 3 to match the distinct values in 'A'
        n, bins, patches = ax.hist(df['A'], bins=3)

        # Expected frequencies: 10 for '1', 20 for '2', 30 for '3'
        expected_frequencies = [10, 20, 30]
        actual_frequencies = [p.get_height() for p in patches]

        self.assertEqual(actual_frequencies, expected_frequencies)

def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()