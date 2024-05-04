import numpy as np
import itertools
from random import randint
import statistics

def f_1010(T1, RANGE=100):
    """
    Convert elements in 'T1' to integers and create a list of random integers.
    The size of the list is the sum of the integers in `T1`. Calculate and 
    return the mean, median, and mode of the list.
    
    Parameters:
    T1 (tuple of tuples): Each tuple contains string representations of integers which are converted to integers.
    RANGE (int, optional): The upper limit for generating random integers. Default is 100.
    
    Returns:
    tuple: A tuple containing the mean, median, and mode of the generated list of random integers.
           The mean and median are floats, and the mode is an integer. The calculations use the generated
           list whose size is determined by the sum of converted integers from `T1`.
    
    Requirements:
    - numpy
    - itertools
    - random.randint
    - statistics
    
    Example:
    >>> import random
    >>> random.seed(42)
    >>> T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
    >>> stats = f_1010(T1)
    >>> print(stats)
    (49.88, 48.0, 20)
    >>> stats = f_1010(T1, RANGE=50)
    >>> print(stats)
    (23.773333333333333, 25.0, 15)
    """
    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_nums = sum(flattened_list)
    random_nums = [randint(0, RANGE) for _ in range(total_nums)]
    mean = np.mean(random_nums)
    median = np.median(random_nums)
    mode = statistics.mode(random_nums)
    return mean, median, mode

import unittest
import numpy as np
import statistics

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        T1 = (('1', '2'), ('2', '3'), ('3', '4'))
        mean, median, mode = f_1010(T1)
        self.assertIsInstance(mean, float)
        self.assertIsInstance(median, float)
        self.assertIsInstance(mode, int)
        self.assertTrue(0 <= mean <= 100)
        self.assertTrue(0 <= median <= 100)
        self.assertTrue(0 <= mode <= 100)

    def test_case_2(self):
        T1 = (('1', '2', '3'), ('4', '5'), ('6', '7', '8', '9'))
        mean, median, mode = f_1010(T1)
        self.assertIsInstance(mean, float)
        self.assertIsInstance(median, float)
        self.assertIsInstance(mode, int)
        self.assertTrue(0 <= mean <= 100)
        self.assertTrue(0 <= median <= 100)
        self.assertTrue(0 <= mode <= 100)
        
    def test_case_3(self):
        T1 = (('1', '2', '3'), ('4', '5'), ('6', '7', '8', '9'))
        mean, median, mode = f_1010(T1, RANGE=50)
        self.assertIsInstance(mean, float)
        self.assertIsInstance(median, float)
        self.assertIsInstance(mode, int)
        self.assertTrue(0 <= mean <= 50)
        self.assertTrue(0 <= median <= 50)
        self.assertTrue(0 <= mode <= 50)
        
    def test_case_4(self):
        T1 = (('1',), ('2',), ('3',))
        mean, median, mode = f_1010(T1)
        self.assertIsInstance(mean, float)
        self.assertIsInstance(median, float)
        self.assertIsInstance(mode, int)
        self.assertTrue(0 <= mean <= 100)
        self.assertTrue(0 <= median <= 100)
        self.assertTrue(0 <= mode <= 100)
        
    def test_case_5(self):
        T1 = (('10', '20', '30'), ('40', '50'), ('60', '70', '80', '90'))
        mean, median, mode = f_1010(T1)
        self.assertIsInstance(mean, float)
        self.assertIsInstance(median, float)
        self.assertIsInstance(mode, int)
        self.assertTrue(0 <= mean <= 100)
        self.assertTrue(0 <= median <= 100)
        self.assertTrue(0 <= mode <= 100)

if __name__ == "__main__":
    run_tests()