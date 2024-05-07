import random
import pandas as pd
import collections

# Constants
VEGETABLES = ['Carrot', 'Potato', 'Tomato', 'Cabbage', 'Spinach']


def f_741(vegetable_dict, seed=0):
    """
    Calculate statistics for the vegetables preferred by people listed in the input dictionary.
    The function reverses the dictionary to map vegetables to people and assigns random counts to these vegetables.
    It then calculates the occurrences of each vegetable as a percentage of the total counts.

    A dictionary is created to map each vegetable to a person from the input where vegetables are values.
    Random counts between 1 and 10 are assigned to simulate varying popularity or availability of each vegetable.

    Parameters:
    vegetable_dict (dict): A dictionary mapping people's names to their preferred vegetables.
    seed (int): An integer value to seed the random number generator. Defaults to 0.
    
    Returns:
    DataFrame: Returns a DataFrame with columns for vegetable names, their random counts,
    and their percentage occurrence within the total counts.

    Requirements:
    - random
    - pandas
    - collections

    Example:
    >>> vegetable_dict = {'John': 'Carrot', 'Alice': 'Potato', 'Bob': 'Tomato'}
    >>> print(f_741(vegetable_dict))
            Count  Percentage
    Carrot      7   46.666667
    Potato      7   46.666667
    Tomato      1    6.666667
    """
    random.seed(seed)
    reversed_dict = {v: k for k, v in vegetable_dict.items()}
    vegetable_counter = collections.Counter({vegetable: random.randint(1, 10) for vegetable in reversed_dict.keys()})
    statistics_df = pd.DataFrame.from_dict(vegetable_counter, orient='index', columns=['Count'])
    statistics_df['Percentage'] = statistics_df['Count'] / statistics_df['Count'].sum() * 100
    return statistics_df

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        vegetable_dict = {'John': 'Carrot', 'Alice': 'Potato', 'Bob': 'Tomato'}
        result = f_741(vegetable_dict)
        self.assertIn('Carrot', result.index)
        self.assertIn('Potato', result.index)
        self.assertIn('Tomato', result.index)
        self.assertTrue(all(result['Percentage'] <= 100))
        self.assertTrue(all(result['Percentage'] >= 0))
    def test_case_2(self):
        vegetable_dict = {'Charlie': 'Cabbage', 'David': 'Spinach'}
        result = f_741(vegetable_dict)
        self.assertIn('Cabbage', result.index)
        self.assertIn('Spinach', result.index)
        self.assertTrue(all(result['Percentage'] <= 100))
        self.assertTrue(all(result['Percentage'] >= 0))
    def test_case_3(self):
        vegetable_dict = {}
        result = f_741(vegetable_dict)
        self.assertTrue(all(result['Percentage'] <= 100))
        self.assertTrue(all(result['Percentage'] >= 0))
    def test_case_4(self):
        vegetable_dict = {'Eva': 'Carrot', 'Frank': 'Carrot', 'Grace': 'Tomato'}
        result = f_741(vegetable_dict)
        self.assertIn('Carrot', result.index)
        self.assertIn('Tomato', result.index)
        self.assertTrue(all(result['Percentage'] <= 100))
        self.assertTrue(all(result['Percentage'] >= 0))
    def test_case_5(self):
        vegetable_dict = {'Hannah': 'Spinach', 'Ian': 'Potato', 'Jack': 'Cabbage', 'Katie': 'Tomato'}
        result = f_741(vegetable_dict)
        self.assertIn('Spinach', result.index)
        self.assertIn('Potato', result.index)
        self.assertIn('Cabbage', result.index)
        self.assertIn('Tomato', result.index)
        self.assertTrue(all(result['Percentage'] <= 100))
        self.assertTrue(all(result['Percentage'] >= 0))
