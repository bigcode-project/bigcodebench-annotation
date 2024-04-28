from collections import Counter
import pandas as pd


def f_478(list_of_menuitems):
    """
    Given a nested list of menu items, this function flattens the list and returns a Pandas DataFrame
    detailing the count of each individual menu item.

    Parameters:
        list_of_menuitems (list): A nested list of menu items.

    Returns:
        DataFrame: A pandas DataFrame with menu items as indices and a 'Count' column showing the count of each menu item.

    Requirements:
        - collections
        - pandas

    Example:
        >>> result = f_478([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
        >>> result.loc['Pizza', 'Count']
        2
        >>> result.loc['Coke', 'Count']
        2
    """
    # Flattening the list using list comprehension
    flat_list = [item for sublist in list_of_menuitems for item in sublist]
    counter = Counter(flat_list)

    # Creating the DataFrame
    df = pd.DataFrame.from_dict(counter, orient='index', columns=['Count'])
    df.index.name = 'MenuItem'

    return df

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_478([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
        expected_result = pd.DataFrame({'Count': [2, 1, 2, 1]},
                                       index=pd.Index(['Pizza', 'Burger', 'Coke', 'Pasta'], name='MenuItem'))
        pd.testing.assert_frame_equal(result, expected_result)
    def test_case_2(self):
        result = f_478([['Bread', 'Butter'], ['Bread', 'Jam'], ['Bread', 'Jam'], ['Butter', 'Jam']])
        expected_result = pd.DataFrame({'Count': [3, 2, 3]},
                                       index=pd.Index(['Bread', 'Butter', 'Jam'], name='MenuItem'))
        pd.testing.assert_frame_equal(result, expected_result)
    def test_case_3(self):
        result = f_478([['Tea', 'Coffee'], ['Tea', 'Milk'], ['Coffee', 'Milk']])
        expected_result = pd.DataFrame({'Count': [2, 2, 2]}, index=pd.Index(['Tea', 'Coffee', 'Milk'], name='MenuItem'))
        pd.testing.assert_frame_equal(result, expected_result)
    def test_case_4(self):
        result = f_478([['Sandwich'], ['Sandwich', 'Juice'], ['Coffee']])
        expected_result = pd.DataFrame({'Count': [2, 1, 1]},
                                       index=pd.Index(['Sandwich', 'Juice', 'Coffee'], name='MenuItem'))
        pd.testing.assert_frame_equal(result, expected_result)
    def test_case_5(self):
        result = f_478([[], [], []])
        self.assertTrue(result.empty)
