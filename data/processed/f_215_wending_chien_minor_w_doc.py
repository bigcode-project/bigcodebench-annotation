import pandas as pd
import matplotlib.pyplot as plt
from random import randint


def f_215(num_types=5, integer_range=(0, 100)):
    """
    Generate a DataFrame containing random integer values across a specified number of categories,
    and visualize these data as a horizontal stacked bar chart.

    Parameters:
    num_types (int, optional): The number of distinct categories for which data will be generated. Defaults to 5.
    integer_range (tuple, optional): The inclusive range from which random integers are drawn. Defaults to (0, 100).

    Returns:
    tuple: A tuple containing a matplotlib Figure and Axes objects for the generated plot.

    Requirements:
    pandas, matplotlib.pyplot, random

    Note:
    The plot displays categories on the y-axis and their corresponding values on the x-axis, with
    data segmented by category.

    Example:
    >>> fig, ax = f_215(3, (0, 50))
    >>> plt.show()  # This will display the plot.
    """
    LABELS = [f'Type{i + 1}' for i in range(num_types)]
    data = pd.DataFrame({label: [randint(*integer_range) for _ in range(num_types)] for label in LABELS})

    fig, ax = plt.subplots()
    data.plot(kind='barh', stacked=True, ax=ax)

    return fig, ax

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        fig, ax = f_215()
        self.assertEqual(len(ax.patches), 25)
    def test_case_2(self):
        fig, ax = f_215(3, (0, 50))
        self.assertEqual(len(ax.patches), 9)
    def test_case_3(self):
        fig, ax = f_215(10)
        self.assertEqual(len(ax.patches), 100)
    def test_case_4(self):
        fig, ax = f_215(1, (10, 20))
        self.assertEqual(len(ax.patches), 1)
    def test_case_5(self):
        fig, ax = f_215(2, (5, 15))
        self.assertEqual(len(ax.patches), 4)
