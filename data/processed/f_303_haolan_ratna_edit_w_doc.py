import itertools
import json


def f_59(json_list, r):
    """
    Generate all possible combinations of r elements from a given number list taken from JSON string input.
    
    Parameters:
    json_list (str): JSON string containing the number list.
    r (int): The number of elements in each combination.

    Returns:
    list: A list of tuples, each tuple representing a combination.

    Note:
    - The datetime to be extracted is located in the 'number_list' key in the JSON data.

    Raises:
    - Raise an Exception if the json_list is an invalid JSON, empty, or does not have 'number_list' key.
    
    Requirements:
    - itertools
    - json
    
    Example:
    >>> combinations = f_59('{"number_list": [1, 2, 3, 4, 5]}', 3)
    >>> print(combinations)
    [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
    """
    try:
        # Convert JSON string to Python dictionary
        data = json.loads(json_list)

        # Extract number_list from dictionary
        number_list = data['number_list']
        return list(itertools.combinations(number_list, r))
    except Exception as e:
        raise e

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_59('{"number_list": [1, 2, 3, 4, 5]}', 3)
        expected = [(1, 2, 3), (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 4), (2, 3, 5), (2, 4, 5), (3, 4, 5)]
        self.assertEqual(result, expected)
    def test_case_2(self):
        result = f_59('{"number_list": ["a", "b", "c"]}', 2)
        expected = [('a', 'b'), ('a', 'c'), ('b', 'c')]
        self.assertEqual(result, expected)
    def test_case_3(self):
        result = f_59('{"number_list": [1, 2, 3]}', 1)
        expected = [(1,), (2,), (3,)]
        self.assertEqual(result, expected)
    def test_case_4(self):
        with self.assertRaises(Exception):
            result = f_59('[]', 1)
    def test_case_5(self):
        result = f_59('{"number_list": [1, 2]}', 3)
        expected = []
        self.assertEqual(result, expected)
