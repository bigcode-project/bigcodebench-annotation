import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def f_1722(start_date, end_date, seed=42):
    """
    Generate random sales data for each day between a start and end date, inclusive.
    Returns the data and a plot of sales over time.

    Parameters:
    start_date (datetime): The start date.
    end_date (datetime): The end date.
    seed (int): Seed for the random number generator. Default is 42.

    Returns:
    DataFrame: A pandas DataFrame with columns 'Date' and 'Sales'.
    Axes: A matplotlib Axes object of the plot showing the sales overtime.
    
    sales ranges 0 to 500 and it is an integer

    Requirements:
    - numpy
    - pandas
    - datetime

    Example:
    >>> start_date = datetime(2021, 1, 1)
    >>> end_date = datetime(2021, 12, 31)
    >>> data, plot = f_1722(start_date, end_date)
    >>> print(data.head())
            Date  Sales
    0 2021-01-01    102
    1 2021-01-02    435
    2 2021-01-03    348
    3 2021-01-04    270
    4 2021-01-05    106
    """
    np.random.seed(seed)
    data = []
    date = start_date

    while date <= end_date:
        sales = np.random.randint(0, 500)
        data.append([date, sales])
        date += timedelta(days=1)

    df = pd.DataFrame(data, columns=["Date", "Sales"])
    ax = df.plot(x='Date', y='Sales')
    ax.set_ylabel("Sales")

    return df, ax

import unittest

class TestCases(unittest.TestCase):
    def setUp(self):
        self.start_date = datetime(2021, 1, 1)
        self.end_date = datetime(2021, 1, 10)

    def test_random_reproducibility(self):
        df1, _ = f_1722(self.start_date, self.end_date, 42)
        df2, _ = f_1722(self.start_date, self.end_date, 42)
        pd.testing.assert_frame_equal(df1, df2)

    def test_dataframe_structure(self):
        df, _ = f_1722(self.start_date, self.end_date)
        self.assertListEqual(list(df.columns), ["Date", "Sales"])
        self.assertEqual(len(df), (self.end_date - self.start_date).days + 1)

    def test_sales_values_range(self):
        df, _ = f_1722(self.start_date, self.end_date)
        self.assertTrue(df["Sales"].between(0, 500).all())

    def test_different_seeds_produce_different_data(self):
        df1, _ = f_1722(self.start_date, self.end_date, 42)
        df2, _ = f_1722(self.start_date, self.end_date, 43)
        self.assertFalse(df1.equals(df2))
    
    def test_values(self):
        df1, _ = f_1722(self.start_date, self.end_date, 42)
        df_list = df1.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        
        expect = ['2021-01-01 00:00:00,102', '2021-01-02 00:00:00,435', '2021-01-03 00:00:00,348', '2021-01-04 00:00:00,270', '2021-01-05 00:00:00,106', '2021-01-06 00:00:00,71', '2021-01-07 00:00:00,188', '2021-01-08 00:00:00,20', '2021-01-09 00:00:00,102', '2021-01-10 00:00:00,121']
        
        with open('df_contents.txt', 'w') as file:
            file.write(str(df_list))

        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")

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