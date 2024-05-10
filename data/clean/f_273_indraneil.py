import itertools
import numpy as np
import matplotlib.pyplot as plt


def f_273(elements, subset_size):
    """
    Generate all subsets of a given size from a tuple and draw a histogram of the sums of the subsets. Additionally,
    return the Axes object of the plotted histogram and the combinations of the subsets and their sums.

    Parameters:
    - elements (tuple): A tuple of integers for which subsets will be generated.
    - subset_size (int): Size of the subsets to be generated.

    Returns:
    - matplotlib.axes.Axes: Axes object of the plotted histogram.
    - list: List of all the combinations of subsets.
    - list: List of the sums of all the subsets.

    Requirements:
    - itertools
    - numpy
    - matplotlib

    Example:
    >>> ax, combs, sums = f_273((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> len(combs)
    45
    >>> len(sums)
    45
    """
    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations]
    ax = plt.hist(sums, bins=np.arange(min(sums), max(sums) + 2) - 0.5, rwidth=0.8, align='left')
    return plt.gca(), combinations, sums


import unittest
import doctest


class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Testing with a tuple of size 10 and subset size 2
        ax, combs, sums = f_273((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 2)
        self.assertIsInstance(ax, plt.Axes)  # Check if the return type is correct
        # Test the combinations and sums
        self.assertEqual(len(combs), 45)
        self.assertEqual(len(sums), 45)

    def test_case_2(self):
        # Testing with a tuple of size 5 and subset size 3
        ax, combs, sums = f_273((2, 4, 6, 8, 10), 3)
        self.assertIsInstance(ax, plt.Axes)
        # Test the combinations and sums
        self.assertEqual(len(combs), 10)
        self.assertEqual(len(sums), 10)

    def test_case_3(self):
        # Testing with an empty tuple
        ax, combs, sums = f_273((), 0)
        self.assertIsInstance(ax, plt.Axes)

    def test_case_4(self):
        # Testing with negative numbers in the tuple
        ax, combs, sums = f_273((-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5), 2)
        self.assertIsInstance(ax, plt.Axes)

    def test_case_5(self):
        # Testing with a subset size of 0
        ax, combs, sums = f_273((1, 2, 3, 4, 5), 2)
        self.assertIsInstance(ax, plt.Axes)
        # Test the combinations and sums
        self.assertEqual(combs, [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)])
        self.assertEqual(sums, [3, 4, 5, 6, 5, 6, 7, 7, 8, 9])


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
