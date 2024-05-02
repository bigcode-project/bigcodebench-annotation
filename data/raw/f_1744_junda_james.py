import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def f_1744(df):
    """
    Draw and return the daily turnover line chart from a pandas DataFrame.

    Parameters:
    df (DataFrame): A pandas DataFrame with 'Date' and 'Sales' columns.

    Returns:
    Axes: Matplotlib Axes object with the line chart.

    Raises:
    ValueError: If 'df' is not a DataFrame or lacks 'Date' or 'Sales' columns, or has no data to plot.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - numpy

    Example:
    >>> df = pd.DataFrame({
    ...     'Date': pd.date_range(start='1/1/2021', end='12/31/2021'),
    ...     'Sales': np.random.randint(100, 2000, size=365)
    ... })
    >>> ax = f_1744(df)
    >>> ax.get_title()  # Expected: 'Daily Turnover'
    'Daily Turnover'
    >>> ax.get_ylabel()  # Expected: 'Sales'
    'Sales'
    """
    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['Date', 'Sales']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'Date' and 'Sales' columns.")

    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    resampled_df = df.resample('D').sum()

    if resampled_df.empty or resampled_df['Sales'].sum() == 0:
        raise ValueError("No data available to plot after resampling.")

    ax = resampled_df.plot(y='Sales')
    ax.set_title('Daily Turnover')
    ax.set_ylabel('Sales')

    return ax

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.df = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2021', periods=10),
            'Sales': np.random.randint(100, 2000, size=10)
        })

    def test_return_type(self):
    # Adjusted to include more data points
        np.random.seed(42)
        large_df = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2021', periods=30),
            'Sales': np.random.randint(100, 2000, size=30)
        })
        ax = f_1744(large_df)
        self.assertIsInstance(ax, plt.Axes)
        
    def test_value(self):
        # Adjusted to include more data points
        ax = f_1744(self.df)
        # Retrieve the line plot data
        # Assuming 'ax' is the Axes object returned by your function 'f_1744'

        # Retrieve the line plot data
        line = ax.get_lines()[0]  # Get the first (and likely only) line plot
        sales = line.get_ydata()
        actual_sales = [str(int(sale)) for sale in sales]

        expect = ['1226', '1559', '960', '1394', '1230', '1195', '1824', '1144', '1738', '221']
        self.assertEqual(actual_sales, expect, "DataFrame contents should match the expected output")
        

    def test_plot_title_and_labels(self):
        # Adjusted to include more data points
        np.random.seed(42)
        large_df = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2021', periods=30),
            'Sales': np.random.randint(100, 2000, size=30)
        })
        ax = f_1744(large_df)
        self.assertEqual(ax.get_title(), 'Daily Turnover')
        self.assertEqual(ax.get_ylabel(), 'Sales')

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            f_1744(pd.DataFrame({'a': [1, 2], 'b': [3, 4]}))

    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_1744(pd.DataFrame({'Date': [], 'Sales': []}))

    def test_date_conversion(self):
        df_with_string_dates = self.df.copy()
        df_with_string_dates['Date'] = df_with_string_dates['Date'].dt.strftime('%Y-%m-%d')
        ax = f_1744(df_with_string_dates)
        self.assertIsInstance(ax, plt.Axes)

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