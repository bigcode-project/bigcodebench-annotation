import pandas as pd
import matplotlib.pyplot as plt
from random import randint


def f_142(num_rows=5, rand_range=(0, 100)):
    """
    Create a DataFrame containing random integer values within a specified range for categories 'A' through 'E',
    and visualize this data with a stacked bar chart.

    Parameters:
    num_rows (int): Specifies the number of rows in the DataFrame.
    rand_range (tuple): Defines the lower and upper bounds for the random number generation, inclusive.

    Returns:
    matplotlib.figure.Figure: The matplotlib Figure object containing the plotted data.

    Requirements:
    - pandas
    - matplotlib
    - random

    Example:
    >>> fig = f_142(num_rows=3, rand_range=(10, 50))
    >>> type(fig)
    <class 'matplotlib.figure.Figure'>
    """
    labels = ['A', 'B', 'C', 'D', 'E']
    data = pd.DataFrame({label: [randint(rand_range[0], rand_range[1]) for _ in range(num_rows)] for label in labels})
    fig, ax = plt.subplots()
    data.plot(kind='bar', stacked=True, ax=ax)
    return fig

import unittest
import pandas as pd
from matplotlib.figure import Figure
LABELS = ['A', 'B', 'C', 'D', 'E']
class TestCases(unittest.TestCase):
    def test_case_1(self):
        fig = f_142()
        self.assertIsInstance(fig, Figure)
        ax = fig.axes[0]
        self.assertEqual(len(ax.patches), 5 * len(LABELS))  # 5 bars for each category
    def test_case_2(self):
        fig = f_142(num_rows=10)
        self.assertIsInstance(fig, Figure)
        ax = fig.axes[0]
        self.assertEqual(len(ax.patches), 10 * len(LABELS))  # 10 bars for each category
    def test_case_3(self):
        fig = f_142(rand_range=(10, 50))
        self.assertIsInstance(fig, Figure)
        ax = fig.axes[0]
        for bar in ax.patches:
            self.assertTrue(10 <= bar.get_height() <= 50)
    def test_case_4(self):
        fig = f_142(num_rows=3, rand_range=(20, 30))
        self.assertIsInstance(fig, Figure)
        ax = fig.axes[0]
        self.assertEqual(len(ax.patches), 3 * len(LABELS))  # 3 bars for each category
        for bar in ax.patches:
            self.assertTrue(20 <= bar.get_height() <= 30)
    def test_case_5(self):
        fig = f_142(num_rows=7, rand_range=(5, 15))
        self.assertIsInstance(fig, Figure)
        ax = fig.axes[0]
        self.assertEqual(len(ax.patches), 7 * len(LABELS))  # 7 bars for each category
        for bar in ax.patches:
            self.assertTrue(5 <= bar.get_height() <= 15)
