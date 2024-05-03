import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def f_1781(df):
    """
    Draw the correlation matrix of the numerical columns of a DataFrame and return the heatmap plot.

    Parameters:
    df (DataFrame): The DataFrame.

    Returns:
    Axes: A Matplotlib Axes object representing the heatmap of the correlation matrix.

    Raises:
    ValueError: If the input is not a DataFrame, if the DataFrame is empty, or if there are no numeric columns.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot
    - seaborn

    Example:
    >>> df = pd.DataFrame({'A': np.random.normal(0, 1, 1000), 'B': np.random.exponential(1, 1000), 'C': np.random.uniform(-1, 1, 1000)})
    >>> ax = f_1781(df)
    >>> plt.show()
    """
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("The input must be a non-empty pandas DataFrame.")

    numeric_cols = df.select_dtypes(include=np.number).columns
    if not numeric_cols.size:
        raise ValueError("DataFrame contains no numeric columns.")

    corr_matrix = df[numeric_cols].corr()
    ax = sns.heatmap(corr_matrix, annot=True)
    ax.set_title('Correlation Matrix Heatmap')

    return ax

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from f_1781 import f_1781  # Assuming f_1781 is defined in a separate module

class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)  # Set seed for reproducibility
        self.df = pd.DataFrame({
            'A': np.random.normal(0, 1, 1000),
            'B': np.random.exponential(1, 1000),
            'C': np.random.uniform(-1, 1, 1000)
        })

    def test_return_type(self):
        ax = f_1781(self.df)
        self.assertIsInstance(ax, plt.Axes)

    def test_invalid_input_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_1781(pd.DataFrame())

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            f_1781("not a dataframe")

    def test_no_numeric_columns(self):
        df = pd.DataFrame({'D': ['text'] * 1000})
        with self.assertRaises(ValueError):
            f_1781(df)

    def test_correlation_values(self):
        ax = f_1781(self.df)
        heatmap_data = ax.collections[0].get_array().data
        expected_corr_matrix = self.df.corr().values
        np.testing.assert_array_almost_equal(heatmap_data, expected_corr_matrix)

    def test_plot_title(self):
        ax = f_1781(self.df)
        self.assertEqual(ax.get_title(), 'Correlation Matrix Heatmap')

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