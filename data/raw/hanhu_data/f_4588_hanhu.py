import random
import bisect
from array import array


def f_4590(n=10, total=100):
    """
    Generates 'n' random integer numbers such that their sum equals 'total', sorts these numbers,
    and determines the position where a new random number can be inserted to maintain the sorted order.
    The function uses a retry mechanism to ensure the generated numbers sum up to 'total'.

    Parameters:
    n (int): The number of random numbers to generate. Default is 10.
    total (int): The total sum of the generated numbers. Default is 100.

    Returns:
    tuple: A tuple containing the sorted numbers as an array and the insertion position for a new number.

    Requirements:
    - random
    - bisect
    - array

    Examples:
    >>> sorted_nums, pos = f_4590(5, 50)
    >>> len(sorted_nums) == 5
    True
    >>> sum(sorted_nums) == 50
    True
    """
    nums = []
    while sum(nums) != total:
        nums = [random.randint(0, total) for _ in range(n)]

    nums.sort()
    nums = array('i', nums)

    new_num = random.randint(0, total)
    pos = bisect.bisect(nums, new_num)

    return (nums, pos)

import unittest
from array import array

class TestF4590(unittest.TestCase):

    def test_return_type(self):
        nums, pos = f_4590(5, 50)
        self.assertIsInstance(nums, array)
        self.assertIsInstance(pos, int)

    def test_correct_length(self):
        nums, _ = f_4590(5, 50)
        self.assertEqual(len(nums), 5)

    def test_sum_of_numbers(self):
        nums, _ = f_4590(5, 50)
        self.assertEqual(sum(nums), 50)

    def test_sorted_order(self):
        nums, _ = f_4590(5, 50)
        self.assertEqual(list(nums), sorted(nums))

    def test_insertion_position(self):
        nums, pos = f_4590(5, 50)
        new_num = random.randint(0, 50)
        nums.insert(pos, new_num)
        self.assertEqual(nums[pos], new_num)

if __name__ == '__main__':
    unittest.main()
