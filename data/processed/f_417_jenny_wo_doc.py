from collections import Counter
import random
import matplotlib.pyplot as plt


def f_99(num_rolls, num_dice, plot_path=None, random_seed=0):
    """Simulate rolling a certain number of a standard six-sided dice several times, then
    identify and display the distribution of the sums of the dice rolls in a bar plot.

    Parameters:
    - num_rolls (int): The number of times to roll the dice.
    - num_dice (int): The number of dice to roll each time.
    - plot_path (str, optional): Path to save the generated plot. If not provided, plot is not saved.
    - random_seed (int): Random seed for reproducibility. Defaults to 0.

    Returns:
    tuple: A tuple containing the following elements:
        - Counter: A Counter object with the count of each possible sum.
        - Axes: A matplotlib Axes object representing the bar plot of the Distribution of Dice Roll Sums,
                with Sum of Dice Roll on the x-axis and count on the y-axis.

    Requirements:
    - collections.Counter
    - random
    - matplotlib.pyplot

    Example:
    >>> result, ax = f_99(10000, 2, 'output.png')
    >>> type(result)
    <class 'collections.Counter'>
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    POSSIBLE_VALUES = list(range(1, 7))

    random.seed(random_seed)

    sums = []
    for _ in range(num_rolls):
        roll = [random.choice(POSSIBLE_VALUES) for _ in range(num_dice)]
        sums.append(sum(roll))

    sums_counter = Counter(sums)

    labels, values = zip(*sums_counter.items())

    plt.bar(labels, values)
    plt.xlabel("Sum of Dice Roll")
    plt.ylabel("Count")
    plt.title("Distribution of Dice Roll Sums")
    ax = plt.gca()
    if plot_path:
        plt.savefig(plot_path)

    return sums_counter, ax

import unittest
import os
from collections import Counter
import tempfile
import shutil
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to store plots
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Close matplotlib plots and remove temporary directory
        plt.close("all")
        shutil.rmtree(self.test_dir)
    def test_case_1(self):
        # Test basic functionality with 100 rolls and 2 dice
        result, ax = f_99(100, 2, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_2(self):
        # Test plot saving functionality
        plot_path = os.path.join(self.test_dir, "test_plot.png")
        result, ax = f_99(1000, 1, plot_path, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(os.path.exists(plot_path))
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_3(self):
        # Test with a larger number of dice
        result, ax = f_99(500, 5, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(isinstance(ax, plt.Axes))
    def test_case_4(self):
        # Test with the minimum possible inputs
        result, ax = f_99(1, 1, random_seed=42)
        self.assertIsInstance(result, Counter)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(len(result), 1)  # Only one possible sum with 1 roll of 1 die
    def test_case_5(self):
        # Test the effect of different random seeds on the result consistency
        result1, _ = f_99(100, 2, random_seed=42)
        result2, _ = f_99(100, 2, random_seed=43)
        self.assertNotEqual(
            result1, result2, "Results should differ with different seeds"
        )
    def test_case_6(self):
        # Test plot detail correctness (labels, title)
        plot_path = os.path.join(self.test_dir, "test_plot_detail.png")
        _, ax = f_99(10, 2, plot_path, random_seed=42)
        self.assertTrue(
            "sum of dice roll" in ax.get_xlabel().lower(), "X-axis label is incorrect"
        )
        self.assertEqual(ax.get_ylabel(), "Count", "Y-axis label is incorrect")
        self.assertTrue(
            "distribution of dice roll sums" in ax.get_title().lower(),
            "Plot title is incorrect",
        )
    def test_case_7(self):
        # Test data correctness with a manually calculated example
        result, _ = f_99(2, 1, random_seed=42)
        expected = Counter({6: 1, 1: 1})
        self.assertEqual(
            result, expected, "Data distribution does not match expected outcome"
        )
    def tearDown(self):
        plt.close("all")
