from collections import Counter
import pandas as pd


def f_630(list_of_menuitems):
    """
    Given a nested list of menu items, this function flattens the list and returns a Pandas DataFrame
    detailing the count of each individual menu item with index name 'MenuItem'.

    Parameters:
        list_of_menuitems (list): A nested list of menu items.

    Returns:
        DataFrame: A pandas DataFrame with menu items as indices and a 'Count' column showing the count of each menu item.

    Requirements:
        - collections
        - pandas

    Example:
        >>> result = f_630([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
        >>> result.loc['Pizza', 'Count']
        2
        >>> result.loc['Coke', 'Count']
        2
    """
    flat_list = [item for sublist in list_of_menuitems for item in sublist]
    counter = Counter(flat_list)
    df = pd.DataFrame.from_dict(counter, orient='index', columns=['Count'])
    df.index.name = 'MenuItem'
    return df

import unittest
class TestCases(unittest.TestCase):
    def test_normal_functionality(self):
        """Test the function with typical nested lists."""
        input_list = [['apple', 'banana'], ['apple'], ['banana', 'orange']]
        expected_df = pd.DataFrame({'Count': [2, 2, 1]}, index=['apple', 'banana', 'orange'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(f_630(input_list), expected_df)
    def test_empty_list(self):
        """Test the function with an empty list."""
        expected_df = pd.DataFrame(columns=['Count'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(f_630([]), expected_df)
    def test_single_level_list(self):
        """Test with a non-nested, single-level list."""
        input_list = [['apple', 'banana', 'apple']]
        expected_df = pd.DataFrame({'Count': [2, 1]}, index=['apple', 'banana'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(f_630(input_list), expected_df)
    def test_uniform_list(self):
        """Test with a list where all sublists contain the same item."""
        input_list = [['apple'], ['apple'], ['apple']]
        expected_df = pd.DataFrame({'Count': [3]}, index=['apple'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(f_630(input_list), expected_df)
    def test_duplicate_items_across_sublists(self):
        """Ensure items appearing in multiple sublists are counted correctly."""
        input_list = [['apple', 'banana'], ['banana', 'banana', 'apple']]
        expected_df = pd.DataFrame({'Count': [2, 3]}, index=['apple', 'banana'])
        expected_df.index.name = 'MenuItem'
        pd.testing.assert_frame_equal(f_630(input_list), expected_df)
