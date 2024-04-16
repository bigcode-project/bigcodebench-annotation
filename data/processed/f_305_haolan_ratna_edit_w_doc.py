import matplotlib.pyplot as plt
import random

# Constants
COLORS = ['#00bfbf', '#000000', '#0000ff']
def f_305(number_list, bins):
    """
    Create a histogram plot of a list of numbers.

    Parameters:
    - number_list (list): A list of numeric values to be plotted.
    - bins (int or sequence): If an integer, the number of histogram bins. 
      If a sequence, defines the bin edges.

    Returns:
    matplotlib.axes._axes.Axes: The axes object representing the histogram plot.

    Note:
    - This function generates a histogram plot using Matplotlib.
    - The plot title is set to 'Histogram'.
    - The x-axis label is set to 'Number'.
    - The y-axis label is set to 'Frequency'.
    - The color of the histogram bars is randomly selected from a predefined set of colors.


    Requirements:
    - matplotlib.pyplot: For creating the histogram plot.

    Example:
    >>> number_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    >>> bins = 5
    >>> ax = f_305(number_list, bins)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    fig, ax = plt.subplots()
    color = random.choice(COLORS)  # Randomly select color from the COLORS constant
    ax.hist(number_list, bins=bins, color=color)
    ax.set_title('Histogram')
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')
    return ax

import unittest
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
# Test data (this could be in a separate file or generated dynamically in real-world scenarios)
test_data = {'small_dataset': [8, 8, 10, 2, 6, 8, 10, 2, 6, 7], 'large_dataset': [4, 9, 42, 79, 5, 60, 27, 58, 34, 61, 44, 68, 1, 78, 93, 11, 100, 69, 89, 45, 43, 7, 54, 31, 75, 64, 20, 93, 93, 95, 33, 19, 2, 6, 49, 18, 95, 62, 36, 52, 48, 61, 78, 61, 48, 17, 79, 4, 54, 63, 64, 37, 79, 22, 3, 24, 42, 1, 59, 25, 15, 53, 81, 86, 2, 34, 71, 80, 11, 36, 90, 37, 80, 48, 35, 66, 13, 57, 13, 16, 32, 42, 48, 96, 92, 60, 4, 14, 45, 45, 52, 88, 49, 71, 91, 77, 17, 27, 34, 18, 88, 41, 18, 65, 58, 18, 62, 77, 2, 5, 22, 2, 47, 39, 5, 17, 87, 85, 54, 7, 97, 32, 62, 92, 10, 45, 66, 58, 61, 25, 46, 10, 70, 60, 41, 5, 78, 79, 64, 36, 71, 45, 9, 11, 85, 51, 53, 71, 47, 88, 45, 37, 92, 72, 35, 70, 66, 28, 76, 97, 34, 13, 36, 88, 80, 86, 41, 91, 23, 2, 51, 61, 44, 50, 37, 90, 76, 45, 45, 51, 6, 12, 92, 16, 30, 74, 55, 58, 57, 77, 15, 51, 17, 48, 96, 89, 79, 16, 66, 30, 86, 53, 13, 61, 12, 66, 13, 94, 98, 82, 58, 19, 75, 22, 32, 24, 5, 49, 75, 16, 58, 36, 33, 79, 7, 58, 100, 54, 42, 74, 30, 52, 8, 68, 43, 97, 28, 47, 6, 51, 54, 62, 82, 4, 18, 82, 43, 72, 64, 97, 62, 90, 54, 1, 60, 27, 27, 42, 83, 100, 85, 73, 13, 5, 2, 96, 65, 28, 51, 28, 17, 35, 36, 71, 14, 53, 18, 23, 71, 85, 6, 1, 61, 68, 52, 9, 66, 37, 70, 91, 65, 59, 91, 55, 34, 86, 4, 48, 56, 55, 31, 21, 88, 41, 27, 81, 13, 34, 30, 42, 35, 94, 50, 82, 54, 4, 70, 52, 19, 38, 57, 89, 9, 35, 77, 79, 98, 29, 73, 92, 54, 38, 14, 71, 49, 15, 70, 16, 25, 79, 74, 76, 70, 7, 37, 36, 92, 51, 92, 37, 57, 10, 51, 3, 20, 66, 38, 1, 56, 15, 8, 46, 47, 75, 89, 24, 18, 84, 78, 66, 16, 76, 36, 58, 22, 96, 56, 22, 64, 9, 24, 74, 87, 50, 82, 1, 7, 73, 96, 91, 31, 61, 59, 95, 82, 92, 3, 37, 24, 22, 3, 54, 29, 52, 32, 82, 87, 42, 45, 4, 26, 96, 59, 42, 69, 51, 74, 25, 70, 90, 52, 30, 51, 69, 21, 8, 8, 65, 86, 26, 19, 61, 37, 58, 3, 21, 100, 7, 59, 5, 69, 38, 30, 11, 48, 9, 11, 7, 20, 46, 86, 63, 98, 51, 82, 51, 22, 18, 10, 34, 98, 54, 22, 51, 46, 54, 14, 79, 74, 84, 38, 25, 16, 28, 19, 100, 94, 87, 54, 81, 7, 56, 7, 7, 6, 1, 81, 40, 99, 88, 21, 28, 79, 74, 67, 16, 89, 17, 87, 86, 39, 75, 91, 87, 33, 25, 68, 25, 58, 96, 61, 92, 39, 50, 36, 30, 23, 28, 82, 52, 28, 23, 92, 17, 46, 62, 69, 80, 14, 96, 44, 98, 77, 39, 92, 69, 7, 22, 50, 12, 25, 76, 26, 34, 35, 99, 66, 97, 44, 79, 41, 41, 41, 41, 28, 17, 49, 79, 47, 56, 77, 27, 50, 6, 41, 59, 19, 15, 27, 58, 25, 62, 51, 12, 57, 38, 81, 88, 67, 82, 37, 8, 94, 77, 92, 88, 98, 59, 25, 9, 38, 48, 43, 23, 51, 11, 92, 32, 45, 46, 38, 54, 32, 45, 22, 65, 5, 66, 80, 84, 6, 80, 65, 14, 81, 19, 77, 7, 24, 46, 34, 53, 36, 48, 46, 81, 72, 55, 33, 66, 68, 34, 5, 14, 91, 35, 59, 61, 51, 92, 87, 10, 24, 33, 9, 89, 8, 28, 99, 4, 41, 56, 39, 25, 27, 80, 35, 28, 86, 21, 61, 73, 19, 68, 98, 70, 40, 89, 12, 31, 55, 92, 4, 52, 14, 13, 5, 91, 41, 56, 36, 70, 39, 51, 51, 39, 42, 39, 32, 84, 77, 31, 42, 46, 36, 59, 20, 30, 87, 3, 71, 34, 3, 43, 31, 81, 75, 53, 65, 77, 43, 92, 77, 46, 62, 24, 71, 80, 33, 10, 72, 75, 24, 79, 9, 20, 9, 58, 9, 72, 17, 15, 49, 82, 20, 39, 39, 29, 81, 42, 72, 60, 91, 6, 81, 85, 15, 38, 79, 60, 24, 20, 58, 97, 100, 34, 74, 66, 56, 55, 8, 61, 79, 86, 94, 75, 23, 53, 60, 71, 95, 47, 82, 98, 45, 3, 16, 53, 15, 100, 42, 37, 76, 59, 19, 40, 88, 8, 9, 42, 53, 83, 37, 86, 84, 3, 37, 14, 3, 66, 43, 22, 22, 3, 21, 94, 29, 13, 49, 30, 4, 3, 4, 2, 83, 41, 92, 21, 64, 50, 66, 39, 88, 29, 81, 8, 19, 41, 46, 50, 53, 41, 50, 74, 32, 22, 50, 21, 37, 3, 78, 7, 37, 97, 5, 50, 64, 1, 17, 43, 52, 52, 82, 47, 20, 66, 16, 51, 63, 92, 83, 53, 61, 99, 61, 37, 41, 63, 7, 8, 93, 7, 45, 74, 2, 68, 16, 12, 93, 99, 32, 32, 68, 9, 39, 67, 81, 6, 23, 30, 67, 49, 40, 6, 29, 29, 95, 88, 64, 54, 24, 16, 80, 24, 26, 56, 44, 20, 35, 93, 49, 5, 33, 1, 40, 94, 18, 73, 44, 85, 98, 25, 24, 84, 75, 68, 48, 96, 5, 81, 13, 90, 37, 26, 9, 52, 31, 88, 46, 40, 8, 63, 65, 50, 74, 86, 100, 86, 66, 24, 35, 95, 80, 30, 49, 16, 57, 14, 80, 28, 13, 28, 71, 3, 2, 94, 24, 43, 8, 53, 86, 25, 75, 59, 59, 48, 71, 19, 34, 72, 4, 17, 2, 60, 51, 21, 9, 32, 29, 25, 81, 32, 37, 93, 93, 65, 52, 48, 96, 78], 'uniform_dataset': [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 'empty_dataset': [], 'mixed_dataset': [30, 40, 20, 1, 20, 50, 1, 50, 20, 20, 1, 50, 20, 50, 10, 10, 1, 20, 20, 20, 20, 20, 1, 1, 40, 30, 30, 30, 30, 50, 1, 10, 40, 1, 30, 20, 40, 30, 50, 20, 50, 30, 40, 20, 20, 10, 40, 10, 50, 20]}
class TestCases(unittest.TestCase):
    def test_case_1(self):
        ax = f_305(test_data["small_dataset"], 5)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Histogram")
        self.assertEqual(ax.get_xlabel(), "Number")
        self.assertEqual(ax.get_ylabel(), "Frequency")
        # Convert RGBA tuple to color code
        color_code = mcolors.rgb2hex(ax.patches[0].get_facecolor())
        # Check color
        self.assertIn(color_code, ['#00bfbf', '#000000', '#0000ff'])
        plt.close()
    def test_case_2(self):
        ax = f_305(test_data["large_dataset"], 10)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Histogram")
        self.assertEqual(ax.get_xlabel(), "Number")
        self.assertEqual(ax.get_ylabel(), "Frequency")
        plt.close()
    def test_case_3(self):
        ax = f_305(test_data["uniform_dataset"], 3)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Histogram")
        self.assertEqual(ax.get_xlabel(), "Number")
        self.assertEqual(ax.get_ylabel(), "Frequency")
        plt.close()
    def test_case_4(self):
        ax = f_305(test_data["empty_dataset"], 5)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Histogram")
        self.assertEqual(ax.get_xlabel(), "Number")
        self.assertEqual(ax.get_ylabel(), "Frequency")
        plt.close()
    def test_case_5(self):
        ax = f_305(test_data["mixed_dataset"], 6)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Histogram")
        self.assertEqual(ax.get_xlabel(), "Number")
        self.assertEqual(ax.get_ylabel(), "Frequency")
        plt.close()
