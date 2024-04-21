import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def f_823(df):
    """
    Plots the correlation matrix from numeric columns in a DataFrame and returns a DataFrame
    where the numeric columns are standardized to have mean 0 and variance 1.

    Parameters:
    df (pandas.DataFrame): Input DataFrame with columns of numeric data.

    Returns:
    pandas.DataFrame: Standardized DataFrame.
    matplotlib.figure.Figure: Figure object containing the heatmap of the correlation matrix.

    Requirements:
    - pandas
    - numpy
    - seaborn
    - matplotlib
    - sklearn

    Raises:
    - ValueError: If the DataFrame is empty or if no numeric columns are present.

    Notes:
    - Only numeric columns are considered for the heatmap. Non-numeric columns are ignored.

    Examples:
    >>> import pandas as pd
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    >>> standardized_df, fig = f_823(df)
    >>> standardized_df
              A         B
    0 -1.224745 -1.224745
    1  0.000000  0.000000
    2  1.224745  1.224745
    >>> type(fig)
    <class 'matplotlib.figure.Figure'>
    """
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.empty:
        raise ValueError("No numeric columns present")

    correlation = numeric_df.corr()
    fig, ax = plt.subplots()
    sns.heatmap(correlation, ax=ax)

    numeric_cols = numeric_df.columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df, fig


import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case with integer values
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        standardized_df, fig = f_823(df)

        self.assertTrue(np.allclose(standardized_df.mean(), 0))
        self.assertTrue(np.allclose(standardized_df.std(ddof=0), 1))
        self.assertTrue(isinstance(fig, plt.Figure))

    def test_case_2(self):
        # Test case with float values
        df = pd.DataFrame({"X": [1.1, 2.2, 3.3], "Y": [4.4, 5.5, 6.6]})
        standardized_df, fig = f_823(df)
        self.assertTrue(np.allclose(standardized_df.mean(), 0))
        self.assertTrue(np.allclose(standardized_df.std(ddof=0), 1))
        self.assertTrue(isinstance(fig, plt.Figure))

    def test_case_3(self):
        # Test case with negative values
        df = pd.DataFrame({"A": [-1, -2, -3], "B": [-4, -5, -6]})
        standardized_df, fig = f_823(df)
        self.assertTrue(np.allclose(standardized_df.mean(), 0))
        self.assertTrue(np.allclose(standardized_df.std(ddof=0), 1))
        self.assertTrue(isinstance(fig, plt.Figure))

    def test_case_4(self):
        # Test case with single column
        df = pd.DataFrame({"A": [1, 2, 3]})
        standardized_df, fig = f_823(df)
        self.assertTrue(np.allclose(standardized_df.mean(), 0))
        self.assertTrue(np.allclose(standardized_df.std(ddof=0), 1))
        self.assertTrue(isinstance(fig, plt.Figure))

    def test_case_5(self):
        # Test proper exception handling - no numeric columns
        df = pd.DataFrame({"A": ["apple", "banana", "cherry"]})
        with self.assertRaises(ValueError):
            f_823(df)

    def test_case_6(self):
        # Test proper exception handling - empty dataframe
        df = pd.DataFrame()
        with self.assertRaises(ValueError):
            f_823(df)

    def test_case_7(self):
        # Test ignoring non-numeric columns
        df = pd.DataFrame({"A": [1, 2, 3], "B": ["x", "y", "z"], "C": [4.5, 5.5, 6.5]})
        standardized_df, fig = f_823(df)
        self.assertTrue("B" in standardized_df.columns)
        self.assertTrue(np.allclose(standardized_df[["A", "C"]].mean(), 0))
        self.assertTrue(np.allclose(standardized_df[["A", "C"]].std(ddof=0), 1))
        self.assertIsInstance(fig, plt.Figure)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
