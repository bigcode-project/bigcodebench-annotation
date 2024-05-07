import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def f_349(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    """
    Generates and plots a sales forecast starting from a given date, for a specified number of periods and frequency.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot
    
    Parameters:
    - start_date (str): Start date for the forecast in 'YYYY-MM-DD' format.
    - periods (int): Number of periods to forecast.
    - freq (str): Frequency of the forecast (e.g., 'WOM-2FRI' for the second Friday of each month, 'M' for monthly).
    - random_seed (int, optional): Seed for the random number generator to ensure reproducibility.

    Returns:
    - A tuple containing:
        1. A DataFrame with columns ['Date', 'Sales'], where 'Date' is the forecast date and 'Sales' are the forecasted sales.
        2. A matplotlib Axes object for the sales forecast plot.

    Examples:
    >>> df, ax = f_349('2021-01-01', 5, 'WOM-2FRI')
    >>> print(df)
                Sales
    Date             
    2021-01-08    272
    2021-02-12    147
    2021-03-12    217
    2021-04-09    292
    2021-05-14    423
    >>> df, ax = f_349('2022-02-01', 3, 'M', random_seed=42)
    >>> print(df)
                Sales
    Date             
    2022-02-28    202
    2022-03-31    448
    2022-04-30    370
    """
    np.random.seed(random_seed)
    date_range = pd.date_range(start_date, periods=periods, freq=freq)
    sales_forecast = np.random.randint(100, 500, size=periods)
    forecast_df = pd.DataFrame({'Date': date_range, 'Sales': sales_forecast}).set_index('Date')
    fig, ax = plt.subplots()
    forecast_df['Sales'].plot(ax=ax, marker='o')
    ax.set_title('Sales Forecast')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.grid(True)
    return forecast_df, ax

import unittest
class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.random_seed = 42
    def test_basic_forecast(self):
        df, ax = f_349('2021-01-01', 5, 'WOM-2FRI', self.random_seed)
        self.assertEqual(len(df), 5)
        self.assertTrue(all(df.columns == ['Sales']))
        self.assertEqual(ax.get_title(), 'Sales Forecast')
    def test_monthly_forecast(self):
        df, ax = f_349('2022-01-01', 3, 'M', self.random_seed)
        self.assertEqual(len(df), 3)
        self.assertTrue(all(df.columns == ['Sales']))
    def test_quarterly_forecast(self):
        df, ax = f_349('2020-01-01', 4, 'Q', self.random_seed)
        self.assertEqual(len(df), 4)
        self.assertTrue(all(df.columns == ['Sales']))
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            f_349('2021-13-01', 5, 'M', self.random_seed)
    def test_negative_periods(self):
        with self.assertRaises(ValueError):
            f_349('2021-01-01', -5, 'M', self.random_seed)
