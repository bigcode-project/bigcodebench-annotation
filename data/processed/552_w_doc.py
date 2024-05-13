import collections
import itertools
import matplotlib.pyplot as plt

# Constants
ITEMS = ['apple', 'banana']


def task_func(a, b, items=ITEMS):
    """
    Combine two lists and record the frequency of predefined items in the combined list.

    Parameters:
    a (list): A list of items.
    b (list): Another list of items.
    items (list, optional): a list of predefined items

    Returns:
    matplotlib.axes.Axes: A bar chart showing the frequency of predefined items in the combined list.

    Requirements:
    - collections
    - itertools
    - matplotlib.pyplot

    Example:
    >>> ax = task_func(['apple', 'banana', 'cherry'], ['date', 'elderberry', 'apple', 'banana', 'cherry'])
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """

    combined = list(itertools.chain(a, b))
    counter = collections.Counter(combined)
    item_counts = [counter.get(item, 0) for item in items]
    fig, ax = plt.subplots()
    ax.bar(items, item_counts, color='skyblue')
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Item Frequency in Combined List')
    plt.xticks(rotation=45)
    plt.tight_layout()  # Adjust layout to make room for item labels
    return ax

import unittest
import matplotlib
class TestCases(unittest.TestCase):
    def test_standard_functionality(self):
        """Test with typical list inputs."""
        a = ['apple', 'banana', 'cherry']
        b = ['banana', 'apple', 'apple', 'dragonfruit']
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
    def test_empty_lists(self):
        """Test with both lists empty."""
        a = []
        b = []
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
    def test_one_empty_list(self):
        """Test with one list empty."""
        a = ['apple', 'apple']
        b = []
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
    def test_non_predefined_items_only(self):
        """Test with lists containing non-predefined items."""
        a = ['cherry', 'dragonfruit']
        b = ['cherry', 'mango']
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
    def test_all_predefined_items(self):
        """Test with lists containing only predefined items."""
        a = ['apple', 'apple']
        b = ['banana']
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
    def test_duplicate_items(self):
        """Test with lists containing duplicate items."""
        a = ['apple', 'apple']
        b = ['apple', 'banana', 'banana']
        ax = task_func(a, b)
        self.assertIsInstance(ax, plt.Axes)
