import seaborn as sns
import matplotlib.pyplot as plt
import random


def f_280(list_of_lists, seed=0):
    """
    Create a histogram from the data in a list of lists. If any sublist is empty, 
    it will be filled with 5 random integers ranging from 0 to 100 (both inclusive)
    The histogram will then be constructed using the combined data from all sublists.
    
    Parameters:
    list_of_lists (list): A list containing multiple sublists with integers.
    seed (int, Optional): Seed value for random number generation. Default is 0.
    
    Returns:
    matplotlib.axes._subplots.AxesSubplot: The histogram plot object.
    
    Requirements:
    - random
    - seaborn
    - matplotlib.pyplot
    
    Example:
    >>> plot = f_280([[1, 2, 3], [], [4, 5, 6]])
    >>> type(plot)
    <class 'matplotlib.axes._axes.Axes'>
    """
    random.seed(seed)
    data = []
    # Initialize a fresh plot
    plt.figure()
    for list_ in list_of_lists:
        if list_:
            data += list_
        else:
            data += [random.randint(0, 100) for _ in range(5)]

    plot = sns.histplot(data)
    return plot


import unittest
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input: Two non-empty sublists and one empty sublist
        plot = f_280([[1, 2, 3], [], [4, 5, 6]])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
        # Test the number of bars in the histogram
        self.assertEqual(len(plot.patches), 5)

    def test_case_2(self):
        # Input: All empty sublists
        plot = f_280([[], [], []])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")

    def test_case_3(self):
        # Input: Single non-empty sublist
        plot = f_280([[1, 2, 3, 4, 5]], 77)
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")
        # Test the number of bars in the histogram
        self.assertEqual(len(plot.patches), 4)

    def test_case_4(self):
        # Input: Single empty sublist
        plot = f_280([[]])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")

    def test_case_5(self):
        # Input: Mixed empty and non-empty sublists
        plot = f_280([[10, 20], [], [30, 40, 50], []])
        self.assertEqual(str(type(plot)), "<class 'matplotlib.axes._axes.Axes'>")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    doctest.testmod()
    run_tests()