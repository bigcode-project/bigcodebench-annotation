import pandas as pd
import numpy as np


CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]


def task_func(s1, s2):
    """
    Compares and visualizes the sales data of two stores for predefined categories.
    The function generates a bar plot for categories where both stores have sales exceeding a specified threshold.
    The Euclidean distance between the two series is also computed.
    
    Parameters:
    s1 (pd.Series): Sales data for store 1, indexed by categories.
    s2 (pd.Series): Sales data for store 2, indexed by categories.

    Returns:
    matplotlib.axes.Axes or None: A bar plot for categories where both stores' sales exceed the threshold of 200,
    or None if no such categories exist.
    float: The Euclidean distance between the two series or 0.0 if no categories meet the threshold.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> np.random.seed(seed=32)
    >>> s1 = pd.Series(np.random.randint(100, 500, size=5), index=CATEGORIES)
    >>> s2 = pd.Series(np.random.randint(150, 600, size=5), index=CATEGORIES)
    >>> ax, edit_distance = task_func(s1, s2)
    >>> ax.get_title()
    'Sales Comparison Above Threshold in Categories'
    >>> edit_distance
    387.5590277622236
    """
    high_sales_categories = s1.index[(s1 > 200) & (s2 > 200)]
    if high_sales_categories.empty:
        return None, 0.0
    df = pd.DataFrame(
        {"Store 1": s1[high_sales_categories], "Store 2": s2[high_sales_categories]}
    )
    edit_distance = np.linalg.norm(df["Store 1"] - df["Store 2"])
    ax = df.plot(kind="bar", title="Sales Comparison Above Threshold in Categories")
    return ax, edit_distance

import pandas as pd
import numpy as np
import unittest
import matplotlib.pyplot as plt
# Constants (should be kept consistent with function.py)
CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]
class TestCases(unittest.TestCase):
    """Tests for function task_func."""
    def test_sales_above_threshold(self):
        """Test that the function returns a plot when sales exceed the threshold"""
        np.random.seed(seed=32)
        s1 = pd.Series(np.random.randint(100, 500, size=5), index=CATEGORIES)
        np.random.seed(seed=32)
        s2 = pd.Series(np.random.randint(150, 600, size=5), index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        # Check the correct categories are plotted
        categories_plotted = [label.get_text() for label in ax.get_xticklabels()]
        self.assertListEqual(
            categories_plotted, ["Electronics", "Home Decor", "Automotive", "Books"]
        )
        # Check the title of the plot
        self.assertEqual(
            ax.get_title(), "Sales Comparison Above Threshold in Categories"
        )
        self.assertAlmostEqual(edit_distance, 100.0)
        
    def test_no_sales_above_threshold(self):
        """Test that no categories are plotted when no sales exceed the threshold"""
        np.random.seed(seed=32)
        s1 = pd.Series(np.random.randint(50, 150, size=5), index=CATEGORIES)
        np.random.seed(seed=32)
        s2 = pd.Series(np.random.randint(50, 150, size=5), index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        # Check that no categories are plotted
        self.assertIsNone(
            ax, "Expected None as no categories should meet the threshold"
        )
        self.assertAlmostEqual(edit_distance, 0.0)
    def test_all_sales_above_threshold(self):
        """Test that all categories are plotted when all sales exceed the threshold"""
        np.random.seed(seed=123)
        s1 = pd.Series(np.random.randint(200, 500, size=5), index=CATEGORIES)
        np.random.seed(seed=123)
        s2 = pd.Series(np.random.randint(250, 600, size=5), index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        # Check that all categories are plotted
        categories_plotted = [label.get_text() for label in ax.get_xticklabels()]
        self.assertListEqual(categories_plotted, CATEGORIES)
        self.assertAlmostEqual(edit_distance, 389.8127755730948)
        
    def test_some_sales_above_threshold(self):
        """Test that some categories are plotted when some sales exceed the threshold"""
        s1 = pd.Series([250, 180, 290, 200, 290], index=CATEGORIES)
        s2 = pd.Series([260, 290, 195, 299, 295], index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        # Check that only the correct categories are plotted
        categories_plotted = [label.get_text() for label in ax.get_xticklabels()]
        self.assertListEqual(categories_plotted, ["Electronics", "Books"])
        self.assertAlmostEqual(edit_distance, 11.180339887498949)
        
    def test_single_sales_above_threshold(self):
        """Test that only a single category is plotted when only a single category has sales exceeding the threshold"""
        s1 = pd.Series([150, 180, 290, 200, 190], index=CATEGORIES)
        s2 = pd.Series([160, 190, 295, 199, 195], index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        # Check that only a single category is plotted
        categories_plotted = [label.get_text() for label in ax.get_xticklabels()]
        self.assertListEqual(categories_plotted, ["Home Decor"])
        self.assertAlmostEqual(edit_distance, 5.0)
        
    def tearDown(self):
        plt.close()
