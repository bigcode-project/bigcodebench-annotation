import random
from collections import Counter
from statistics import mode


def f_690(list_length=1000, range_start=1, range_end=10, random_seed=None):
    """
    Generate a random list of integers within a specified range. Convert this
    list to a generator object that yields tuples. Each tuple contains a number
    from the list and its frequency. Additionally, find and return the mode of 
    the list.

    Parameters:
    - list_length (int): The length of the random list to be generated. Default is 1000.
    - range_start (int): The start of the range for random numbers. Default is 1.
    - range_end (int): The end of the range for random numbers. Default is 10.
    - random_seed (int): Seed for the rng. Default is None.

    Returns:
    tuple: A tuple containing:
    - int: The mode of the generated list.
    - generator: A generator object yielding tuples with each number from the list and its frequency.

    Requirements:
    - random
    - collections
    - statistics

    Example:
    >>> mode, numbers = f_690(100, 1, 5)
    >>> print(mode)  # prints the mode e.g. 3
    >>> print(next(numbers))  # prints a tuple like (1, 25)
    2
    (2, 26)

    >>> mode, numbers = f_690(20, -12, 334, random_seed=23)
    >>> print(mode)
    >>> print([_ for _ in numbers])
    136
    [(136, 1), (30, 1), (-4, 1), (291, 1), (145, 1), (204, 1), (182, 1), (259, 1), (171, 1), (54, 1), (86, 1), (124, 1), (215, 1), (-5, 1), (101, 1), (305, 1), (220, 1), (0, 1), (42, 1), (31, 1)]

    """
    random.seed(random_seed)
    random_list = [random.randint(range_start, range_end) for _ in range(list_length)]
    counter = Counter(random_list)
    numbers = ((number, count) for number, count in counter.items())
    return mode(random_list), numbers

import unittest

 
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_rng(self):
        mode1, numbers1 = f_690(random_seed=2)
        mode2, numbers2 = f_690(random_seed=2)
        self.assertEqual(mode1, mode2)
        self.assertCountEqual([_ for _ in numbers1], [_ for _ in numbers2])

    def test_case_1(self):
        mode, numbers = f_690(100, 1, 5, random_seed=1)
        self.assertEqual(mode, 4)
        expected = [(2, 18), (5, 22), (1, 20), (3, 14), (4, 26)]
        self.assertCountEqual([_ for _ in numbers], expected)
        
    def test_case_2(self):
        mode, numbers = f_690(50, 3, 7, random_seed=12)
        self.assertEqual(mode, 7)
        expected = [(6, 9), (5, 8), (7, 12), (4, 10), (3, 11)]
        self.assertCountEqual([_ for _ in numbers], expected)
        
    def test_case_3(self):
        mode, numbers = f_690(200, 10, 20, random_seed=222)
        self.assertEqual(mode, 18)
        expected = [
            (11, 20),
            (13, 21),
            (14, 17),
            (10, 20),
            (17, 20),
            (16, 16),
            (20, 13),
            (18, 29),
            (15, 16),
            (12, 15),
            (19, 13)
        ]
        self.assertCountEqual([_ for _ in numbers], expected)
        
    def test_case_4(self):
        mode, numbers = f_690(1000, 0, 1, random_seed=42)
        self.assertEqual(mode, 1)
        expected = [(0, 486), (1, 514)]
        self.assertCountEqual([_ for _ in numbers], expected)

    def test_case_5(self):
        mode, numbers = f_690(10, 5, 5, random_seed=1)
        self.assertEqual(mode, 5)
        expected = [(5, 10)]
        self.assertCountEqual([_ for _ in numbers], expected)
    
    def test_case_6(self):
        _, numbers = f_690()
        self.assertIsInstance(numbers, type((x for x in range(1))))  # Checking if it's a generator


if __name__ == "__main__":
    run_tests()