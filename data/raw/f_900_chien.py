import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list(range(1, 27))


def f_900(n_pairs=26):
    """
    This function generates and displays a bar chart representing random letter-number pairs.
    Each bar corresponds to a unique pair, formed by combining a letter from 'a' to 'z' with a number
    from 1 to 26. The function randomly shuffles these pairs and assigns a random count to each.

    Parameters:
    - n_pairs (int, optional): The number of letter-number pairs to display in the bar chart.
      The value must be an integer between 1 and 26, inclusive. The default value is 26, which
      includes one pair for each letter in the alphabet.

    Returns:
    - matplotlib.container.BarContainer: This object represents the bar chart created by the function.
      Each bar in the chart is labeled with its corresponding letter-number pair (e.g., 'a:1', 'b:2').
      The title of the chart is "Random Letter:Number Pairs Chart", the x-axis label is "Letter:Number Pairs",
      and the y-axis label is "Counts".

    Raises:
    - ValueError: If 'n_pairs' is outside the range of 1 to 26, inclusive. This ensures that the function
      operates within the bounds of the predefined letters ('a' to 'z') and numbers (1 to 26).

    Requirements:
    - numpy
    - matplotlib
    - random

    Notes:
    - Each call to this function will likely produce a different chart because it shuffles the order
      of the pairs and assigns random counts to them.
    - The random counts assigned to each pair range from 1 to 9.

    Example:
    >>> ax = f_900(5)
    >>> [bar.get_label() for bar in ax]
    ['d:4', 'b:2', 'c:3', 'e:5', 'a:1']
    """
    if n_pairs > 26 or n_pairs < 1:
        raise ValueError("n_pairs should be between 1 and 26")

    pairs = [f"{letter}:{number}" for letter, number in zip(LETTERS, NUMBERS)][:n_pairs]
    random.seed(42)
    random.shuffle(pairs)
    counts = np.random.randint(1, 10, size=n_pairs)

    bars = plt.bar(pairs, counts)

    # Set label for each bar
    for bar, pair in zip(bars, pairs):
        bar.set_label(pair)

    plt.xlabel("Letter:Number Pairs")
    plt.ylabel("Counts")
    plt.title("Random Letter:Number Pairs Chart")

    return bars


import unittest
import matplotlib.pyplot as plt
from matplotlib.container import BarContainer
import random


class TestCases(unittest.TestCase):
    """Tests for the function f_900."""

    def test_return_type(self):
        """Verify the returned type of the function."""
        random.seed(0)
        ax = f_900(5)
        self.assertIsInstance(
            ax, BarContainer, "The returned object is not of the expected type."
        )

    def test_number_of_bars(self):
        """Verify the number of bars plotted for different `n_pairs` values."""
        random.seed(1)
        for i in [5, 10, 20]:
            ax = f_900(i)
            self.assertEqual(
                len(ax.patches),
                i,
                f"Expected {i} bars, but got {len(ax.patches)} bars.",
            )

    def test_labels_and_title(self):
        """Verify the labels and the title of the plotted bar chart."""
        random.seed(2)
        _ = f_900(15)
        fig = plt.gcf()
        axes = fig.gca()
        self.assertEqual(
            axes.get_xlabel(), "Letter:Number Pairs", "X label is incorrect."
        )
        self.assertEqual(axes.get_ylabel(), "Counts", "Y label is incorrect.")
        self.assertEqual(
            axes.get_title(), "Random Letter:Number Pairs Chart", "Title is incorrect."
        )

    def test_invalid_n_pairs(self):
        """Test the function with invalid `n_pairs` values."""
        random.seed(3)
        with self.assertRaises(ValueError):
            f_900(27)
        with self.assertRaises(ValueError):
            f_900(0)

    def test_valid_pairs(self):
        """Verify that the pairs generated are valid and correspond to the expected letter:number format."""
        random.seed(4)
        ax = f_900(5)
        expected_pairs = ["a:1", "b:2", "c:3", "d:4", "e:5"]

        generated_pairs = [bar.get_label() for bar in ax]

        for expected_pair in expected_pairs:
            self.assertIn(
                expected_pair,
                generated_pairs,
                f"Expected pair {expected_pair} not found in plotted pairs.",
            )


def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
