import pandas as pd
import numpy as np


def f_358(days, random_seed=0):
    """
    Generates a spending report DataFrame for the given number of days.

    This function takes a number of days as input and populates a pandas DataFrame
    with fake expenditure data indexed by date. Each day on or after '2023-01-01'
    has its own row. The DataFrame has five columns: Groceries, Entertainment, Rent,
    Utilities, and Miscellaneous, with their integer values independently randomly
    sampled from 0 to 100.

    Parameters:
    - days (int): Number of days for which the report is to be generated.
                  This is used to generate dates starting from '2023-01-01'.
                  For example, a 'days' of 2 will generate data for '2023-01-01',
                  '2023-01-02'.
                  If 0, this function will return a DataFrame with the expected
                  columns that is otherwise empty.
    - random_seed (int): Numpy random seed for reproducibility. Defaults to 0.

    Returns:
    - pd.DataFrame: A DataFrame containing spending details for specified days,
                    with shape (num_days, 5).

    Requirements:
    - pandas
    - numpy

    Example:
    >>> df = f_358(5, random_seed=42)
    >>> type(df)
    <class 'pandas.core.frame.DataFrame'>
    >>> df.head(2)
                Groceries  Entertainment  Rent  Utilities  Miscellaneous
    date                                                                
    2023-01-01         51             20    87         52              1
    2023-01-02         92             82    99          1             63
    """
    np.random.seed(random_seed)
    date_rng = pd.date_range(start="2023-01-01", periods=days, freq="D")
    df = pd.DataFrame(date_rng, columns=["date"])
    df.set_index("date", inplace=True)
    categories = ["Groceries", "Entertainment", "Rent", "Utilities", "Miscellaneous"]
    for category in categories:
        df[category] = np.random.randint(0, 100, size=(days))
    return df

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    report_columns = [
        "Groceries",
        "Entertainment",
        "Rent",
        "Utilities",
        "Miscellaneous",
    ]
    start_date = pd.to_datetime(["2023-01-01"]).day
    def _test_report_structure(self, report, days):
        self.assertIsInstance(report, pd.DataFrame)
        self.assertEqual(report.shape[0], days)
        self.assertEqual(report.shape[1], len(self.report_columns))
        self.assertEqual(list(report.columns), self.report_columns)
    def _test_report_data(self, report):
        self.assertFalse(report.isnull().values.any())
        self.assertTrue(pd.api.types.is_datetime64_ns_dtype(report.index))
        self.assertTrue(report.index.day.map(lambda d: d >= self.start_date).all())
        for col in report:
            self.assertTrue((report[col] >= 0).all() and (report[col] <= 100).all())
    def _test_report(self, report, days):
        self._test_report_structure(report, days)
        self._test_report_data(report)
    def test_case_1(self):
        # Test basic case with default parameters
        days = 7
        report = f_358(days)
        self._test_report(report, days)
    def test_case_2(self):
        # Test handling 0 days
        days = 0
        report = f_358(days)
        self._test_report(report, days)
    def test_case_3(self):
        # Test handling larger number of days
        days = 1000
        report = f_358(days)
        self._test_report(report, days)
    def test_case_4(self):
        # Test handling invalid inputs
        with self.assertRaises(ValueError):
            f_358(-1)
        with self.assertRaises(ValueError):
            f_358(None)
        with self.assertRaises(TypeError):
            f_358("-1")
    def test_case_5(self):
        # Test random seed reproducibility
        days = 100
        report1 = f_358(days, random_seed=42)
        report2 = f_358(days, random_seed=42)
        self.assertTrue(report1.equals(report2))
        self._test_report(report1, days)
        self._test_report(report2, days)
    def test_case_6(self):
        # Test random seed variation
        days = 100
        report1 = f_358(days, random_seed=24)
        report2 = f_358(days, random_seed=42)
        self.assertFalse(report1.equals(report2))
        self._test_report(report1, days)
        self._test_report(report2, days)
