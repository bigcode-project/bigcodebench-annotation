from datetime import datetime
import pandas as pd
from itertools import product

# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]


def f_36(date_str):
    """
    Generate a Pandas DataFrame containing a series of dates for a predefined list of employees.

    Parameters:
    - date_str (str): A date string in the "yyyy-mm-dd" format to define the starting date.

    Returns:
    - DataFrame: A pandas DataFrame with 'Employee' and 'Date' columns, listing the next 10 days for each employee.

    Requirements:
    - datetime.datetime
    - pandas
    - itertools

    Example:
    >>> df = f_36('2023-06-15')
    >>> print(df)
       Employee       Date
    0      John 2023-06-15
    1      John 2023-06-16
    ...
    49     Dave 2023-06-24
    """
    start_date = datetime.strptime(date_str, "%Y-%m-%d")
    dates = pd.date_range(start_date, periods=10).tolist()
    df = pd.DataFrame(list(product(EMPLOYEES, dates)), columns=["Employee", "Date"])
    return df

import unittest
import pandas as pd
from datetime import datetime, timedelta
class TestCases(unittest.TestCase):
    """Test cases for the function."""
    def test_return_type(self):
        """Test if the function returns a Pandas DataFrame."""
        df_test = f_36("2023-01-01")
        self.assertIsInstance(df_test, pd.DataFrame)
    def test_correct_columns(self):
        """Test if the DataFrame has the correct columns: 'Employee' and 'Date'."""
        df_test = f_36("2023-01-01")
        self.assertListEqual(df_test.columns.tolist(), ["Employee", "Date"])
    def test_date_range(self):
        """Test if the function generates the correct date range for 10 days."""
        start_date = "2023-01-01"
        df_test = f_36(start_date)
        end_date = (
            datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=9)
        ).date()
        self.assertTrue(all(df_test["Date"] <= pd.Timestamp(end_date)))
    def test_number_of_rows(self):
        """Test if the DataFrame has the correct number of rows (10 days * number of employees)."""
        df_test = f_36("2023-01-01")
        expected_rows = 10 * len(EMPLOYEES)  # 10 days for each employee
        self.assertEqual(len(df_test), expected_rows)
    def test_leap_year(self):
        """Test if the function correctly handles the date range for a leap year."""
        df_test = f_36("2024-02-28")
        leap_year_end_date = (
            datetime.strptime("2024-02-28", "%Y-%m-%d") + timedelta(days=9)
        ).date()
        self.assertIn(pd.Timestamp(leap_year_end_date), df_test["Date"].values)
