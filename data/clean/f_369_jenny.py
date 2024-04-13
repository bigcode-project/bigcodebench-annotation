import matplotlib.pyplot as plt
import numpy as np


def f_369(myList):
    """
    Draws a histogram of the values in a list and returns the plot's Axes.

    For visualization:
      - Bin edges are adjusted to align with integer values in `myList`.
      - Histogram bars are outlined in black.
      - X-axis label: 'Value'
      - Y-axis label: 'Frequency'
      - Plot title: 'Histogram of Values'

    Parameters:
    - myList (list): List of numerical values to plot.

    Returns:
    - ax (matplotlib.axes._axes.Axes): Axes object of the histogram plot.

    Requirements:
    - matplotlib.pyplot
    - numpy

    Example:
    >>> myList = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    >>> ax = f_369(myList)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(0.0, 0, '0.0'), Text(0.5, 0, '0.5'), Text(1.0, 0, '1.0'), Text(1.5, 0, '1.5'), Text(2.0, 0, '2.0'), Text(2.5, 0, '2.5'), Text(3.0, 0, '3.0'), Text(3.5, 0, '3.5'), Text(4.0, 0, '4.0'), Text(4.5, 0, '4.5'), Text(5.0, 0, '5.0')]
    """
    _, ax = plt.subplots()
    ax.hist(
        myList, bins=np.arange(min(myList), max(myList) + 2) - 0.5, edgecolor="black"
    )
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Values")
    return ax


import unittest
import numpy as np
import matplotlib.pyplot as plt


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        myList = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        ax = f_369(myList)
        heights, _, _ = ax.hist(
            myList,
            bins=np.arange(min(myList), max(myList) + 2) - 0.5,
            edgecolor="black",
        )
        self.assertIsInstance(ax, plt.Axes)
        self.assertListEqual(list(heights), [1, 2, 3, 4])
        self.assertEqual(ax.get_title(), "Histogram of Values")
        self.assertEqual(ax.get_xlabel(), "Value")
        self.assertEqual(ax.get_ylabel(), "Frequency")

    def test_case_2(self):
        # Test with empty list
        with self.assertRaises(ValueError):
            f_369([])

    def test_case_3(self):
        # Test with single element
        myList = [100]
        ax = f_369(myList)
        heights, _, _ = ax.hist(myList)
        self.assertEqual(heights.max(), 1)

    def test_case_4(self):
        # Test with negative values
        myList = [-5, -4, -3, -3, -2, -2, -2, -1]
        ax = f_369(myList)
        heights, _, _ = ax.hist(myList)
        self.assertGreaterEqual(len(heights), 1)

    def test_case_5(self):
        # Test with floats
        myList = [1.1, 1.2, 2.5, 2.5, 3.75, 4.25]
        ax = f_369(myList)
        heights, _, _ = ax.hist(myList)
        self.assertGreaterEqual(len(heights), 1)

    def test_case_6(self):
        # Test handling non-numeric values
        myList = ["a", "b", "c"]
        with self.assertRaises(TypeError):
            f_369(myList)

    def tearDown(self):
        plt.close("all")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
