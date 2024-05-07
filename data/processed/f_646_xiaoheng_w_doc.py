import re
import math

def f_424(s):
    '''
    Count the number of integers and floating-point numbers in a comma-separated string and calculate the sum of their square roots.

    Parameters:
    - s (str): The comma-separated string.

    Returns:
    - count (int): The number of integers and floats in the string.
    - sqrt_sum (float): The sum of the square roots of the integers and floats.
    
    Requirements:
    - re
    - math
    
    Example:
    >>> count, sqrt_sum = f_424('1,2,3.5,abc,4,5.6')
    >>> print(count)  # Ensure this matches exactly with expected output
    5
    >>> print("{:.2f}".format(sqrt_sum))  # Ensure this matches exactly with expected output
    8.65
    '''
    numbers = re.findall(r'\b\d+(?:\.\d+)?\b', s)  # Use non-capturing group for decimals
    count = len(numbers)
    sqrt_sum = sum(math.sqrt(float(num)) for num in numbers if num)  # Ensure conversion to float
    return count, sqrt_sum

import unittest
class TestCases(unittest.TestCase):
    def test_1(self):
        count, sqrt_sum = f_424('1,2,3.5,abc,4,5.6')
        self.assertEqual(count, 5)
        self.assertAlmostEqual(sqrt_sum, sum(math.sqrt(x) for x in [1, 2, 3.5, 4, 5.6]))
    def test_2(self):
        count, sqrt_sum = f_424('a,b,c,10,20.5')
        self.assertEqual(count, 2)
        self.assertAlmostEqual(sqrt_sum, sum(math.sqrt(x) for x in [10, 20.5]))
    def test_3(self):
        count, sqrt_sum = f_424('1.1,2.2,3.3')
        self.assertEqual(count, 3)
        self.assertAlmostEqual(sqrt_sum, sum(math.sqrt(x) for x in [1.1, 2.2, 3.3]))
    def test_4(self):
        count, sqrt_sum = f_424('')
        self.assertEqual(count, 0)
        self.assertEqual(sqrt_sum, 0.0)
    def test_5(self):
        count, sqrt_sum = f_424('apple,banana,3.14,15,grape,1001')
        self.assertEqual(count, 3)
        self.assertAlmostEqual(sqrt_sum, sum(math.sqrt(x) for x in [3.14, 15, 1001]))
