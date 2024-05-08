import numpy as np
import seaborn as sns


def f_806(arr):
    """
    Plots a heatmap of a given 2D numerical array and prints the sum of each row.
    The heatmap's color range is set based on the minimum and maximum values in the array.

    Parameters:
    arr (numpy.array): A 2D numpy array of numerical values.

    Returns:
    ax (matplotlib.axes.Axes): The Axes object with the plotted heatmap.

    Requirements:
    - numpy
    - seaborn

    Note:
    The function calculates the sum of each row and prints these values.
    The heatmap is plotted based on the original array with its color range set from the minimum to the maximum value in the array.

    Example:
    >>> arr = np.array([[i + j for i in range(3)] for j in range(5)])
    >>> ax = f_806(arr)
    >>> ax.get_title()
    'Heatmap of the 2D Array'
    """
    row_sums = arr.sum(axis=1)
    vmax = np.max(arr)  # Set vmax to the maximum value in the array
    vmin = np.min(arr)  # Set vmin to the minimum value in the array
    ax = sns.heatmap(
        arr, annot=True, vmax=vmax, vmin=vmin
    )  # Include both vmin and vmax in the heatmap call
    ax.set_title("Heatmap of the 2D Array")
    return ax

import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for the function f_806."""
    def tearDown(self):
        plt.clf()
    def test_scenario_1(self):
        """Scenario 1: Testing with a 2D array created by adding row and column indices."""
        arr = np.array([[i + j for i in range(3)] for j in range(5)])
        expected_vmax = np.max(arr)  # Calculate the expected vmax
        ax = f_806(arr)
        self.assertEqual(ax.get_title(), "Heatmap of the 2D Array")
        self.assertEqual(ax.collections[0].colorbar.vmax, expected_vmax)
    def test_scenario_2(self):
        """Scenario 2: Testing with a 2D array where each column has identical values based on the column index."""
        arr = np.array([[i for i in range(3)] for j in range(5)])
        expected_vmax = np.max(arr)  # Calculate the expected vmax
        ax = f_806(arr)
        self.assertEqual(ax.get_title(), "Heatmap of the 2D Array")
        self.assertEqual(ax.collections[0].colorbar.vmax, expected_vmax)
    def test_scenario_3(self):
        """Scenario 3: Testing with a 2D array where each row has identical values based on the row index."""
        arr = np.array([[j for i in range(3)] for j in range(5)])
        expected_vmax = np.max(arr)  # Calculate the expected vmax
        ax = f_806(arr)
        self.assertEqual(ax.get_title(), "Heatmap of the 2D Array")
        self.assertEqual(ax.collections[0].colorbar.vmax, expected_vmax)
    def test_scenario_4(self):
        """Scenario 4: Testing with a 2D array of zeros."""
        arr = np.zeros((5, 3))
        expected_vmax = np.max(arr)  # Calculate the expected vmax
        ax = f_806(arr)
        self.assertEqual(ax.get_title(), "Heatmap of the 2D Array")
        self.assertAlmostEqual(
            ax.collections[0].colorbar.vmax, expected_vmax, delta=0.2
        )
    def test_scenario_5(self):
        """Scenario 5: Testing with a 2D array of ones."""
        arr = np.ones((5, 3))
        expected_vmax = np.max(arr)  # Calculate the expected vmax
        ax = f_806(arr)
        self.assertEqual(ax.get_title(), "Heatmap of the 2D Array")
        self.assertAlmostEqual(
            ax.collections[0].colorbar.vmax, expected_vmax, delta=0.2
        )
