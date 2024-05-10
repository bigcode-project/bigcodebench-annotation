from collections import Counter
import random
import string

# Constants
LETTERS = string.ascii_letters

def task_func(list_of_lists):
    """
    If you have a nested list, replace each sublist with a random letter and return a count of each letter in the final list.

    Parameters:
    - list_of_lists (list): A nested list.

    Returns:
    - dict: A dictionary containing count of each letter in the list.

    Requirements:
    - collections
    - random
    - string

    Example:
    >>> random.seed(42)
    >>> task_func([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
    {'O': 1, 'h': 1, 'b': 1}
    """
    flat_list = [random.choice(LETTERS) for _ in list_of_lists]
    return dict(Counter(flat_list))

import unittest
class TestCases(unittest.TestCase):
    # Input 1: Standard nested list with string values
    def test_case_1(self):
        result = task_func([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
        assert isinstance(result, dict)
        assert sum(result.values()) == 3
    # Input 2: Nested list with numerical values
    def test_case_2(self):
        result = task_func([[1, 2], [3, 4], [5, 6]])
        assert isinstance(result, dict)
        assert sum(result.values()) == 3
    # Input 3: Nested list with mixed string and numerical values
    def test_case_3(self):
        result = task_func([['Pizza', 1], [2, 'Coke'], ['Pasta', 3]])
        assert isinstance(result, dict)
        assert sum(result.values()) == 3
    # Input 4: Empty list
    def test_case_4(self):
        result = task_func([])
        assert isinstance(result, dict)
        assert sum(result.values()) == 0
    # Input 5: Nested list with a single sublist
    def test_case_5(self):
        result = task_func([['Pizza']])
        assert isinstance(result, dict)
        assert sum(result.values()) == 1
