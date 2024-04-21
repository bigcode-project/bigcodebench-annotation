import numpy as np
import pandas as pd


def f_212(rows=5, cols=5):
    """
    Generates a DataFrame with random numerical data and visualizes this data in a stacked bar chart for
    specified categories.

    Parameters:
    rows (int, optional): Number of rows for the DataFrame. Defaults to 5.
    cols (int, optional): Number of columns for the DataFrame, corresponding to the number of categories.
    Defaults to 5, with a maximum of 5 categories ("A", "B", "C", "D", "E").

    Returns:
    matplotlib.axes._subplots.AxesSubplot: The Axes object displaying the stacked bar chart.

    Requirements:
    numpy, pandas, matplotlib.pyplot

    Raises:
    ValueError: If the number of columns exceeds the number of available categories.

    Example:
    >>> import matplotlib
    >>> ax = f_212(3, 3)  # Generates a 3x3 DataFrame and plots it
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """
    np.random.seed(0)
    categories = ['A', 'B', 'C', 'D', 'E']
    if cols > len(categories):
        raise ValueError(f"Maximum number of columns allowed is {len(categories)}")

    data = pd.DataFrame(np.random.rand(rows, cols) * 100, columns=categories[:cols])

    ax = data.plot(kind='bar', stacked=True, figsize=(10, 6))
    ax.set_ylabel('Value')
    ax.set_title('Stacked Bar Chart')

    return ax


import unittest
import matplotlib.pyplot as plt

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def tearDown(self):
        # Cleanup any opened figures in matplotlib
        plt.close('all')

    def test_case_1(self):
        ax = f_212(5, 5)
        self.assertEqual(len(ax.patches), 25)  # 5 bars with 5 segments each, each segment represents a stacked part

    def test_case_2(self):
        ax = f_212(7, 3)
        self.assertEqual(len(ax.patches), 21)  # 7 bars with 3 segments each

    def test_case_3(self):
        ax = f_212(10, 2)
        self.assertEqual(len(ax.patches), 20)  # 10 bars with 2 segments each

    def test_case_4(self):
        with self.assertRaises(ValueError):  # Testing for more columns than categories
            ax = f_212(5, 6)

    def test_case_5(self):
        ax = f_212(3, 1)
        self.assertEqual(len(ax.patches), 3)  # 3 bars with 1 segment each


if __name__ == "__main__":
    run_tests()
