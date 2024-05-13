import json
import math


def task_func(decimal_value, precision=2):
    """
    Calculate the square root of the given decimal value to a certain precision and then encode the result as a JSON string.
    
    Parameters:
    utc_datetime (datetime): The datetime in UTC.
    precision (int, Optional): The number of decimal places to round the square root to. Defaults to 2.
    
    Returns:
    str: The square root of the decimal value encoded as a JSON string.
    
    Requirements:
    - json
    - math
    
    Example:
    >>> from decimal import Decimal
    >>> decimal_value = Decimal('3.9')
    >>> json_str = task_func(decimal_value, decimal_value)
    >>> print(json_str)
    "1.97"
    """

    square_root = round(math.sqrt(decimal_value), 2)
    json_str = json.dumps(str(square_root))
    return json_str

import unittest
import doctest
from decimal import Decimal
class TestCases(unittest.TestCase):
    def test_case_1(self):
        decimal_value = Decimal('4.0')
        json_str = task_func(decimal_value)
        self.assertEqual(json.loads(json_str), "2.0")
    def test_case_2(self):
        decimal_value = Decimal('0.0')
        json_str = task_func(decimal_value)
        self.assertEqual(json.loads(json_str), "0.0")
    def test_case_3(self):
        decimal_value = Decimal('0.0001')
        json_str = task_func(decimal_value)
        self.assertEqual(json.loads(json_str), "0.01")
    def test_case_4(self):
        decimal_value = Decimal('1000000.0')
        json_str = task_func(decimal_value)
        self.assertEqual(json.loads(json_str), "1000.0")
    def test_case_5(self):
        decimal_value = Decimal('-1.0')
        with self.assertRaises(ValueError):
            task_func(decimal_value)
