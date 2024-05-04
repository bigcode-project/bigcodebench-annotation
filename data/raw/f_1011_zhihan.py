import numpy as np
import itertools
from random import randint


def f_1011(T1, max_value=100):
    """
    Converts elements in 'T1', a tuple of tuples containing string representations 
    of integers, to integers and creates a list of random integers. The size of the 
    list equals the sum of these integers. Returns the 25th, 50th, and 75th percentiles 
    of this list.

    Parameters:
    T1 (tuple of tuple of str): A tuple of tuples, each containing string representations of integers.
    max_value (int): The upper bound for random number generation, exclusive. Default is 100.
    
    Returns:
    tuple: A tuple (p25, p50, p75) representing the 25th, 50th, and 75th percentiles of the list.

    Requirements:
    - numpy
    - itertools
    - random.randint
    
    Example:
    >>> import random
    >>> random.seed(42)
    >>> T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
    >>> percentiles = f_1011(T1)
    >>> print(percentiles)
    (24.0, 48.0, 77.0)
    """
    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_nums = sum(flattened_list)

    random_nums = [randint(0, max_value) for _ in range(total_nums)]

    p25 = np.percentile(random_nums, 25)
    p50 = np.percentile(random_nums, 50)
    p75 = np.percentile(random_nums, 75)

    return p25, p50, p75

import unittest

class TestCases(unittest.TestCase):

    def test_case_1(self):
        T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
        p25, p50, p75 = f_1011(T1)
        self.assertTrue(0 <= p25 <= 100)
        self.assertTrue(0 <= p50 <= 100)
        self.assertTrue(0 <= p75 <= 100)
        self.assertTrue(p25 <= p50 <= p75)

    def test_case_2(self):
        T1 = (('10',), ('10', '10', '10'))
        p25, p50, p75 = f_1011(T1)
        self.assertTrue(0 <= p25 <= 100)
        self.assertTrue(0 <= p50 <= 100)
        self.assertTrue(0 <= p75 <= 100)
        self.assertTrue(p25 <= p50 <= p75)

    def test_case_3(self):
        T1 = (('5', '5', '5', '5'), ('10', '15'), ('1', '2', '3', '4', '5'))
        p25, p50, p75 = f_1011(T1)
        self.assertTrue(0 <= p25 <= 100)
        self.assertTrue(0 <= p50 <= 100)
        self.assertTrue(0 <= p75 <= 100)
        self.assertTrue(p25 <= p50 <= p75)

    def test_case_4(self):
        T1 = (('50',), ('25', '25'))
        p25, p50, p75 = f_1011(T1)
        self.assertTrue(0 <= p25 <= 100)
        self.assertTrue(0 <= p50 <= 100)
        self.assertTrue(0 <= p75 <= 100)
        self.assertTrue(p25 <= p50 <= p75)

    def test_case_5(self):
        T1 = (('1', '1', '1', '1', '1', '1', '1', '1', '1', '1'), ('10', '10'))
        p25, p50, p75 = f_1011(T1)
        self.assertTrue(0 <= p25 <= 100)
        self.assertTrue(0 <= p50 <= 100)
        self.assertTrue(0 <= p75 <= 100)
        self.assertTrue(p25 <= p50 <= p75)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()