import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def f_827(df, x_column, y_column):
    """
    Draws a scatter plot for the specified columns from a pandas DataFrame and fits a linear regression model to the data.

    Parameters:
    df (DataFrame): The input pandas DataFrame.
    x_column (str): The column name for the x-axis. Data contained in column must be numeric.
    y_column (str): The column name for the y-axis. Data contained in column must be numeric.

    Returns:
    matplotlib.axes._subplots.AxesSubplot: The Axes object containing the scatter plot and the linear regression line.

    Requirements:
    - pandas
    - numpy
    - matplotlib
    - sklearn

    Notes:
    - After plotting the scatterplot, this function overlays the predicted regression line on top in red on the same Axes.

    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]})
    >>> ax = f_827(df, 'A', 'B')
    >>> type(ax)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    """
    X = df[x_column].values.reshape(-1, 1)
    Y = df[y_column].values
    reg = LinearRegression().fit(X, Y)
    Y_pred = reg.predict(X)

    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.plot(X, Y_pred, color="red")

    return ax


import unittest
import pandas as pd
import numpy as np
from matplotlib.axes import Axes


class TestCases(unittest.TestCase):
    def helper_assert_line_correctness(self, ax, expected_slope, expected_intercept):
        # Helper function to check if linear regression predictions are correct

        tolerance = 1e-6

        # Extract line data
        line = ax.lines[0]
        x_data, y_data = line.get_xdata(), line.get_ydata()

        # Calculate slope and intercept of the line plot
        calculated_slope = (y_data[-1] - y_data[0]) / (x_data[-1] - x_data[0])
        calculated_intercept = y_data[0] - calculated_slope * x_data[0]

        # Assert slope and intercept
        self.assertAlmostEqual(
            calculated_slope,
            expected_slope,
            delta=tolerance,
            msg="Slope did not match expected value",
        )
        self.assertAlmostEqual(
            calculated_intercept,
            expected_intercept,
            delta=tolerance,
            msg="Intercept did not match expected value",
        )

    def test_plot_attributes(self):
        # Basic case to test plot is correct
        df = pd.DataFrame({"X": [1, 2, 3, 4], "Y": [1, 2, 3, 4]})
        ax = f_827(df, "X", "Y")
        self.assertIsInstance(ax, Axes)
        self.assertEqual(len(ax.lines), 1)
        self.assertEqual(len(ax.collections), 1)

    def test_linear_positive_slope(self):
        # Testing with a dataset that should produce a positive slope
        df = pd.DataFrame({"X": [1, 2, 3, 4], "Y": [2, 4, 6, 8]})
        ax = f_827(df, "X", "Y")
        self.helper_assert_line_correctness(ax, expected_slope=2, expected_intercept=0)

    def test_linear_negative_slope(self):
        # Testing with a dataset that should produce a negative slope
        df = pd.DataFrame({"X": [1, 2, 3, 4], "Y": [8, 6, 4, 2]})
        ax = f_827(df, "X", "Y")
        self.helper_assert_line_correctness(
            ax, expected_slope=-2, expected_intercept=10
        )

    def test_linear_zero_slope(self):
        # Testing with a dataset that should produce a zero slope
        df = pd.DataFrame({"X": [1, 2, 3, 4], "Y": [5, 5, 5, 5]})
        ax = f_827(df, "X", "Y")
        self.helper_assert_line_correctness(ax, expected_slope=0, expected_intercept=5)

    def test_single_data_point(self):
        # Testing with a DataFrame having a single data point
        df = pd.DataFrame({"X": [1], "Y": [1]})
        ax = f_827(df, "X", "Y")

        self.assertIsInstance(ax, Axes)
        self.assertEqual(len(ax.lines), 1)
        self.assertEqual(len(ax.collections), 1)

    def test_missing_values(self):
        # Testing with missing values in the DataFrame
        df = pd.DataFrame({"X": [1, 2, np.nan, 4], "Y": [1, np.nan, 3, 4]})
        with self.assertRaises(ValueError):
            f_827(df, "X", "Y")

    def test_with_categorical_data(self):
        # Testing with categorical data to ensure it fails
        df = pd.DataFrame({"X": ["a", "b", "c"], "Y": ["d", "e", "f"]})
        with self.assertRaises(ValueError):
            f_827(df, "X", "Y")

    def test_incorrect_column_names(self):
        # Testing with incorrect column names
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        with self.assertRaises(KeyError):
            f_827(df, "X", "Y")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
