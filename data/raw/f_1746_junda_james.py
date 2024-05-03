import pandas as pd
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt

def f_1746(df):
    """
    Draw and return a heat map with temperature data from a pandas DataFrame.

    Parameters:
    df (DataFrame): A pandas DataFrame with 'Date', 'Time', and 'Temperature' columns.

    Returns:
    AxesSubplot: Seaborn heatmap object.

    Raises:
    ValueError: If 'df' is not a DataFrame or lacks 'Date', 'Time', or 'Temperature' columns.

    Requirements:
    - pandas
    - seaborn
    - numpy 
    - matplotlib.pyplot


    Example:
    >>> np.random.seed(42)
    >>> df = pd.DataFrame({
    ...     'Date': pd.date_range(start='1/1/2021', end='12/31/2021'),
    ...     'Time': ['12:00']*365,
    ...     'Temperature': np.random.randint(-10, 35, size=365)
    ... })
    >>> ax = f_1746(df)
    >>> ax.get_title()  # Expected: 'Temperature Heatmap'
    'Temperature Heatmap'
    """
    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['Date', 'Time', 'Temperature']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'Date', 'Time', and 'Temperature' columns.")

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    df_pivot = df.pivot("Month", "Day", "Temperature")
    ax = sns.heatmap(df_pivot)
    ax.set_title('Temperature Heatmap')
    return ax

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.df = pd.DataFrame({
            'Date': pd.date_range(start='1/1/2021', end='12/31/2021'),
            'Time': ['12:00'] * 365,
            'Temperature': np.random.randint(-10, 35, size=365)
        })
    def test_return_value(self):
        ax = f_1746(self.df)
        heatmap_data = ax.collections[0].get_array()
        heatmap_data[np.isnan(heatmap_data)] = 0
        heatmap_data = heatmap_data.flatten().tolist()
        expect = [28.0, 18.0, 4.0, 32.0, -3.0, 10.0, 28.0, 8.0, 12.0, 0.0, 0.0, 13.0, 25.0, 29.0, 13.0, -8.0, 11.0, -9.0, 13.0, 33.0, 19.0, 27.0, -9.0, 10.0, 22.0, 1.0, 11.0, 33.0, 14.0, 16.0, 31.0, 17.0, 5.0, 4.0, 33.0, -8.0, 26.0, -4.0, 10.0, -2.0, 28.0, 7.0, -7.0, 14.0, 3.0, -2.0, 15.0, -9.0, 9.0, 17.0, -4.0, 33.0, -3.0, 24.0, 3.0, 6.0, 25.0, 29.0, -7.0, None, None, None, -9.0, -5.0, 31.0, -7.0, 18.0, 7.0, 15.0, 33.0, 23.0, -1.0, 25.0, 3.0, 20.0, 4.0, -3.0, 3.0, 12.0, 29.0, 10.0, 5.0, 34.0, 7.0, 13.0, 15.0, 14.0, 34.0, 30.0, 18.0, 4.0, 34.0, -10.0, 14.0, -4.0, -2.0, 13.0, -10.0, 33.0, -3.0, 13.0, 0.0, 6.0, -3.0, 24.0, 24.0, 22.0, -6.0, 31.0, 28.0, 30.0, 17.0, -4.0, -2.0, -3.0, 1.0, 23.0, 22.0, 12.0, 13.0, 26.0, 24.0, 33.0, None, 29.0, 11.0, 16.0, 24.0, -10.0, 24.0, 26.0, 3.0, -8.0, -10.0, -6.0, 15.0, 3.0, 28.0, 16.0, -2.0, 4.0, 4.0, 15.0, 31.0, 2.0, 21.0, 28.0, 21.0, -7.0, 19.0, 26.0, 12.0, 28.0, 34.0, 4.0, 32.0, 18.0, 25.0, 2.0, 21.0, -4.0, 11.0, 17.0, -9.0, 31.0, 34.0, -5.0, 17.0, 17.0, 33.0, 33.0, 9.0, 19.0, 0.0, 17.0, 14.0, 28.0, 22.0, -10.0, 16.0, 2.0, 30.0, -8.0, 28.0, -5.0, None, -3.0, 16.0, -2.0, 26.0, 22.0, 31.0, 33.0, 13.0, 4.0, 21.0, 21.0, 13.0, 30.0, 1.0, 28.0, -9.0, -8.0, 26.0, 6.0, -9.0, -9.0, 17.0, 12.0, 26.0, 21.0, 22.0, -10.0, 8.0, -9.0, 33.0, 15.0, 21.0, -5.0, 21.0, -7.0, 0.0, 6.0, 27.0, 13.0, -6.0, 23.0, -5.0, 11.0, 0.0, 5.0, 22.0, -2.0, -5.0, 5.0, 18.0, -8.0, 9.0, 25.0, 8.0, 15.0, -8.0, 8.0, 9.0, 21.0, -4.0, 30.0, 22.0, 29.0, 28.0, 7.0, 29.0, -10.0, 0.0, 17.0, 14.0, 12.0, 20.0, 19.0, 31.0, 24.0, -4.0, 5.0, 15.0, -9.0, -10.0, 1.0, -6.0, 26.0, 21.0, -2.0, 30.0, 24.0, 8.0, 5.0, -8.0, 9.0, 13.0, None, 22.0, 13.0, 0.0, -3.0, 25.0, 27.0, 29.0, 9.0, 24.0, 14.0, 24.0, 14.0, 18.0, 7.0, 7.0, -9.0, 24.0, 5.0, 30.0, 25.0, 22.0, -7.0, 22.0, 3.0, 10.0, 9.0, -3.0, -4.0, -8.0, 6.0, 22.0, 1.0, 11.0, 11.0, 19.0, 27.0, 27.0, 34.0, -3.0, 16.0, 16.0, 23.0, 10.0, 19.0, 22.0, 17.0, 22.0, -6.0, 8.0, -7.0, 24.0, 6.0, 33.0, 17.0, 19.0, 18.0, -5.0, 24.0, 30.0, 26.0, 13.0, None, 18.0, 20.0, 24.0, 22.0, 10.0, 21.0, 12.0, 22.0, -8.0, 7.0, 14.0, 31.0, 20.0, -8.0, 29.0, 13.0, 21.0, 11.0, 12.0, -9.0, 16.0, 31.0, -9.0, 15.0, 6.0, 29.0, 22.0, -2.0, 32.0, 28.0, 18.0]
        self.assertListEqual(heatmap_data, expect, "DataFrame contents should match the expected output")
    
    def test_return_type1(self):
        ax = f_1746(self.df)
        self.assertIsInstance(ax, plt.Axes)
    

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            f_1746(pd.DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}))

    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_1746(pd.DataFrame({'Date': [], 'Time': [], 'Temperature': []}))

    def test_plot_title(self):
        ax = f_1746(self.df)
        self.assertTrue('Temperature Heatmap' in ax.get_title())

    def test_date_conversion(self):
        df_with_string_dates = self.df.copy()
        df_with_string_dates['Date'] = df_with_string_dates['Date'].dt.strftime('%Y-%m-%d')
        ax = f_1746(df_with_string_dates)
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