import bisect
import random

def task_func(num, list_length = 5, min_value = 0, max_value = 0):
    """
    Insert a number into a randomly generated sorted list and return the new sorted list.

    Parameters:
    num (int): The integer number to insert.
    list_length (int): The length of the randomly generated list of integers.
    min_value (int): The minimum value for randomly generated integers.
    max_value (int): The maximum value for randomly generated integers.

    Returns:
    tuple: A tuple containing two lists: 
        list[int]: The randomly generated list of integers with the specified length.
        list[int]: A new sorted list containing the original elements and the inserted number.
    
    Requirements:
    - bisect
    - random

    Example:
    >>> random.seed(0)
    >>> task_func(4, 5, 100, 100)
    ([100, 100, 100, 100, 100], [4, 100, 100, 100, 100, 100])
    >>> task_func(15, 0, 10, 20)
    ([], [15])
    """

    numbers = [random.randint(min_value, max_value) for _ in range(list_length)]
    sorted_list = numbers.copy()
    bisect.insort(sorted_list, num)
    return numbers, sorted_list

import unittest
from unittest.mock import patch
import random
class TestCases(unittest.TestCase):
    @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_insert_into_empty_list(self, mock_randint):
        random.seed(0)
        result = task_func(15, 0, 5, 60)
        self.assertEqual(result, ([], [15]))
    @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_insert_into_existing_list(self, mock_randint):
        random.seed(0)
        result = task_func(15, 5, 10, 60)
        self.assertEqual(result, ([12, 23, 34, 45, 56], [12, 15, 23, 34, 45, 56]))
    @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_insert_at_beginning(self, mock_randint):
        random.seed(0)
        result = task_func(4, 4, 10, 60)
        self.assertEqual(result, ([12, 23, 34, 45], [4, 12, 23, 34, 45]))
    # @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_insert_at_end(self):
        random.seed(0)
        result = task_func(15, 4, 10, 10)
        self.assertEqual(result, ([10, 10, 10, 10], [10, 10, 10, 10, 15]))
    @patch('random.randint', side_effect=[12, 34, 56])
    def test_insert_in_middle(self, mock_randint):
        random.seed(0)
        result = task_func(15, 3, 10, 60)
        self.assertEqual(result, ([12, 34, 56], [12, 15, 34, 56]))
    @patch('random.randint', side_effect=[12, 23, 34, 45, 56])
    def test_random_list_length(self, mock_randint):
        random.seed(0)
        result = task_func(15, 5, 10, 20)
        self.assertEqual(len(result[0]), 5)
        self.assertIn(15, result[1])
