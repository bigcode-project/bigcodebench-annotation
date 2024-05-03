import pandas as pd
import matplotlib.pyplot as plt


def f_451(data_list):
    """
    Visualizes the scores of students over multiple tests using a line plot.

    The function takes in a list of dictionaries. Each dictionary contains the name of a student (key)
    and their score (value). It combines these dictionaries into a pandas DataFrame and plots a line graph
    of student scores over tests, where the x-axis represents the test number and the y-axis represents the score.
    Each student's scores are plotted as separate lines. Missing scores are handled by not plotting
    those specific data points, allowing for discontinuous lines where data is missing.

    Parameters:
    - data_list (list of dict): A list of dictionaries with student names as keys and their scores as values.

    Returns:
    - ax (matplotlib.axes._axes.Axes): The Axes object with the plotted data.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> data = [{'John': 5, 'Jane': 10}, {'John': 6, 'Jane': 8}, {'John': 5, 'Jane': 9}]
    >>> ax = f_451(data)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(-0.25, 0, '−0.25'), Text(0.0, 0, '0.00'), Text(0.25, 0, '0.25'), Text(0.5, 0, '0.50'), Text(0.75, 0, '0.75'), Text(1.0, 0, '1.00'), Text(1.25, 0, '1.25'), Text(1.5, 0, '1.50'), Text(1.75, 0, '1.75'), Text(2.0, 0, '2.00'), Text(2.25, 0, '2.25')]
    """
    df = pd.DataFrame(data_list)
    fig, ax = plt.subplots()
    for column in df:
        ax.plot(df[column], label=column)
    ax.set_title("Student Scores over Tests")
    ax.set_xlabel("Test Number")
    ax.set_ylabel("Score")

    return ax

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data = [
            {"John": 5, "Jane": 10, "Joe": 7},
            {"John": 6, "Jane": 8, "Joe": 10},
            {"John": 5, "Jane": 9, "Joe": 8},
            {"John": 7, "Jane": 10, "Joe": 9},
        ]
        self.validate_plot(data)
    def test_case_2(self):
        data = [{"John": 3}, {"John": 4}, {"John": 5}, {"John": 6}]
        self.validate_plot(data)
    def test_case_3(self):
        data = [
            {"John": 3, "Jane": 2},
            {"John": 4, "Jane": 3},
            {"John": 5, "Jane": 4},
            {"John": 6, "Jane": 5},
        ]
        self.validate_plot(data)
    def test_case_4(self):
        data = [
            {"John": 10, "Jane": 20, "Joe": 15, "Jack": 25},
            {"John": 12, "Jane": 18, "Joe": 14, "Jack": 24},
            {"John": 11, "Jane": 19, "Joe": 13, "Jack": 23},
            {"John": 13, "Jane": 21, "Joe": 16, "Jack": 22},
        ]
        self.validate_plot(data)
    def test_case_5(self):
        data = [
            {"John": 7, "Jane": 8},
            {"John": 8, "Jane": 7},
            {"John": 7, "Jane": 8},
            {"John": 8, "Jane": 7},
        ]
        self.validate_plot(data)
    def test_case_6(self):
        data = []
        self.validate_plot(data)
    def test_case_7(self):
        # Floats
        data = [{"John": 5.5, "Jane": 10.1}, {"John": 6.75, "Jane": 8.25}]
        self.validate_plot(data)
    def test_case_8(self):
        # Missing scores
        data = [{"John": 5, "Jane": 10}, {"Jane": 8, "Joe": 7}, {"John": 6}]
        self.validate_plot(data)
    def validate_plot(self, data):
        ax = f_451(data)
        self.assertIsInstance(ax, plt.Axes)
        df = pd.DataFrame(data)
        for idx, column in enumerate(df):
            plotted_data_y = ax.lines[idx].get_ydata()
            expected_data_y = df[column].values.astype(float)
            # Handle float comparisons
            np.testing.assert_allclose(
                plotted_data_y, expected_data_y, rtol=1e-5, atol=1e-8, equal_nan=True
            )
            plotted_data_x = ax.lines[idx].get_xdata().astype(int)
            expected_data_x = np.arange(len(df[column].values))
            self.assertTrue(
                np.array_equal(plotted_data_x, expected_data_x),
                msg=f"X-data Mismatch for {column}. Plotted: {plotted_data_x}, Expected: {expected_data_x}",
            )
    def tearDown(self):
        plt.close("all")
