from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import itertools

def f_426(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    """
    Given a nested list of menu items, flatten the list using itertool chain, count the occurrences of each item, then
    plot a histogram with an alphabetically sorted x-axis labeled as "Menu Items" and y-axis as "Frequency".

    Parameters:
    - list_of_menuitems (list): A non-empty nested list of menu items. Each element is a list of menu item strings.
    - title (str, optional): The title of the histogram plot. Default is "Menu Distribution".
    - color (str, optional): The color of the bars in the histogram. Default is "blue".
    - width (float, optional): The width of the bars in the histogram. Default is 1.0.

    Returns:
    - ax (object): An Axes object representing the histogram plot.

    Requirements:
    - collections.Counter
    - numpy
    - matplotlib.pyplot
    - itertools

    Example:
    >>> f_426([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
    <Axes: title={'center': 'Menu Distribution'}, xlabel='Menu Items', ylabel='Frequency'>
    >>> f_426(['Burger'], title='A Title', color='red', width=5.0)
    <Axes: title={'center': 'A Title'}, xlabel='Menu Items', ylabel='Frequency'>
    """
    # Flatten the list
    flat_list = list(itertools.chain(*list_of_menuitems))

    # Count the occurrences of each menu item
    counter = Counter(flat_list)
    labels, values = zip(*sorted(counter.items(), key=lambda x: x[0]))
    indexes = np.arange(len(labels))

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(indexes, values, width, color=color)
    ax.set_xticklabels(labels)
    ax.set_xlabel("Menu Items")
    ax.set_ylabel("Frequency")
    ax.set_title(title)

    return ax

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_data = [["Pizza", "Burger"], ["Pizza", "Coke"], ["Pasta", "Coke"]]
        ax = f_426(input_data)
        # Test default plot properties
        self.assertEqual(ax.get_title(), "Menu Distribution")
        self.assertEqual(ax.get_xlabel(), "Menu Items")
        self.assertEqual(ax.get_ylabel(), "Frequency")
        for p in ax.patches:
            # RGBA color
            self.assertEqual(p.get_facecolor(), (0.0, 0.0, 1.0, 1.0))
            # bar width
            self.assertEqual(p.get_width(), 1.0)
    def test_case_2(self):
        input_data = [["Pizza", "Burger"], ["Pizza", "Coke"], ["Pasta", "Coke"]]
        ax = f_426(input_data, title="Custom Title", color="red", width=0.8)
        # Test custom plot properties
        self.assertEqual(ax.get_title(), "Custom Title")
        self.assertEqual(ax.get_xlabel(), "Menu Items")
        self.assertEqual(ax.get_ylabel(), "Frequency")
        for p in ax.patches:
            # RGBA color
            self.assertEqual(p.get_facecolor(), (1.0, 0.0, 0.0, 1.0))
            # bar width
            self.assertEqual(p.get_width(), 0.8)
    def test_case_3(self):
        input_data = [["Burger"], ["Pizza"], ["Pasta"]]
        ax = f_426(input_data)
        # Test count
        bars = [p.get_height() for p in ax.patches]
        self.assertEqual(bars, [1, 1, 1])
    def test_case_4(self):
        input_data = [["Carrot", "Apple"], ["Apple", "Banana"], ["Banana"]]
        ax = f_426(input_data)
        # Test x-axis order
        self.assertEqual(
            [_._text for _ in ax.get_xticklabels() if _._text],
            ["Apple", "Banana", "Carrot"],
        )
    def test_case_5(self):
        # Test input edge case: some empty elements
        ax = f_426([[], ["Apple"]])
        self.assertEqual(len(ax.patches), 1)
        for p in ax.patches:
            # bar width
            self.assertEqual(p.get_width(), 1.0)
            self.assertEqual(p.get_height(), 1)
    def test_case_6(self):
        with self.assertRaises(ValueError):
            f_426([])
        with self.assertRaises(ValueError):
            f_426([[]])
        with self.assertRaises(ValueError):
            f_426("")
        with self.assertRaises(TypeError):
            f_426(None)
        with self.assertRaises(TypeError):
            f_426(1)
        with self.assertRaises(TypeError):
            f_426([1])
    def tearDown(self):
        plt.close("all")
