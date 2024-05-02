from collections import Counter
import itertools
import numpy as np

# Fixed seed for reproducibility
SEED = 42


def f_1009(T1, range_=100):
    """
    Convert elements in 'T1' to integers and create a list of random integers with fixed randomness.
    The size of the list is the sum of the integers in `T1`. Count the occurrences of each number in the list
    using a Counter. The random integers are generated between 0 (inclusive) and `range_` (exclusive),
    with randomness fixed by a seed.

    Parameters:
    T1 (tuple): A tuple of tuples, each containing string representations of integers.
    range_ (int, optional): The upper limit (exclusive) for generating random integers. Default is 100.

    Returns:
    Counter: A Counter object with the count of each number in the list of random integers.

    Requirements:
    - collections.Counter
    - itertools.chain
    - numpy for random number generation

    Example:
    >>> T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
    >>> f_1009(T1)
    Counter({51: 4,
         92: 2,
         14: 6,
         71: 4,
         60: 1,
         20: 3,
         82: 1,
         86: 2,
         ...
         })
    >>> f_1009(T1, range_=50)
    Counter({38: 10,
         28: 4,
         14: 8,
         42: 2,
         7: 7,
         20: 4,
         18: 2,
         22: 5,
         10: 4,
         ...
         })
    """
    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_nums = sum(flattened_list)

    # Initialize numpy random state with the fixed seed
    rng = np.random.RandomState(SEED)

    # Generate random numbers within the specified range using the seeded random state
    random_nums = rng.randint(0, range_, total_nums)
    counts = Counter(random_nums)

    return counts


import unittest
from collections import Counter


class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Input 1: Single tuple with small integers as strings
        T1 = (('1', '2', '3'),)
        result = f_1009(T1)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 6)  # Sum of the integers in T1 is 6

    def test_case_2(self):
        # Input 2: Multiple tuples with small integers as strings
        T1 = (('1', '2'), ('3', '4'))
        result = f_1009(T1)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 10)  # Sum of the integers in T1 is 10

    def test_case_3(self):
        # Input 3: Single tuple with larger integers as strings
        T1 = (('10', '20', '30'),)
        result = f_1009(T1)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 60)  # Sum of the integers in T1 is 60

    def test_case_4(self):
        # Input 4: Multiple tuples with mixed small and large integers as strings
        T1 = (('1', '10'), ('100', '1000'))
        result = f_1009(T1)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 1111)  # Sum of the integers in T1 is 1111

    def test_case_5(self):
        # Input 5: Single tuple with repeating integers as strings
        T1 = (('1', '1', '1'),)
        result = f_1009(T1)
        self.assertIsInstance(result, Counter)
        self.assertEqual(sum(result.values()), 3)  # Sum of the integers in T1 is 3


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
