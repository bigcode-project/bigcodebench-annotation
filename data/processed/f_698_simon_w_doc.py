import heapq
import random

def f_338(obj_list, attr, top_n=5, seed=None):
    """
Find the top N values of the specified attribute in a list of objects.
Return the top N values as well a a randomly sampled value of all attributes.

Parameters:
obj_list (list): The list of objects.
attr (str): The attribute to find the top N values.
top_n (int, optional): The number of top values to retrieve. Defaults to 5.
seed (float, optional): The seed used for randomly choosing an attribute.

Returns:
list[int]: The top N values as a list of integers. Empty list if there are no attributes.
float: A randomly chosen value of all attributes, None if there are no attributes.

Requirements:
- heapq
- random
    
Example:
    >>> # Sample data class used in the example
    >>> class Object:
    ...     def __init__(self, value):
    ...         self.value = value
    ...
    >>> random.seed(1)
    >>> obj_list = [Object(random.randint(1, 100)) for _ in range(33)]
    >>> top_values, random_value = f_338(obj_list, 'value', 5, seed=1)
    >>> print(top_values)
    [99, 98, 98, 98, 93]
    >>> print(random_value)
    58

    >>> class Object:
    ...     def __init__(self, value):
    ...         self.test = value
    ...
    >>> random.seed(2)
    >>> obj_list = [Object(random.randint(1, 12)) for _ in range(13)]
    >>> top_values, random_value = f_338(obj_list, 'test', 2, 12)
    >>> print(top_values)
    [12, 11]
    >>> print(random_value)
    5
"""
    random.seed(seed)
    attr_values = [getattr(obj, attr) for obj in obj_list]
    if len(attr_values) == 0:
        return [], None
    top_values = heapq.nlargest(top_n, attr_values)
    random_value = random.choice(attr_values)
    return top_values, random_value

import unittest
from faker import Faker
# Test cases with random data
class TestCases(unittest.TestCase):
    faker = Faker()
    faker.seed_instance(42)
    
    def generate_objects(self, count):
        class TestObject:
            def __init__(self, value):
                self.value = value
        
        return [TestObject(self.faker.random_int(min=1, max=100)) for _ in range(count)]
    
    def test_case_1(self):
        obj_list = self.generate_objects(10)
        result, rand = f_338(obj_list, 'value', 5, seed=12)
        self.assertEqual(result, [95, 95, 82, 36, 32])
        self.assertEqual(rand, 18)
    def test_case_2(self):
        obj_list = self.generate_objects(50)
        result, rand = f_338(obj_list, 'value', 7, seed=1)
        self.assertEqual(result, [98, 98, 95, 94, 92, 90, 90])
        self.assertEqual(rand, 12)
        
    def test_case_3(self):
        obj_list = []
        result, rand = f_338(obj_list, 'value', 5, seed=2)
        self.assertEqual(result, [])
        self.assertEqual(rand, None)
        
    def test_case_4(self):
        obj_list = self.generate_objects(5)
        result, rand = f_338(obj_list, 'value', 10, seed=3)
        self.assertEqual(result, [81, 80, 71, 38, 11])
        self.assertEqual(rand, 71)
        
    def test_case_5(self):
        obj_list = self.generate_objects(100)
        result, rand = f_338(obj_list, 'value', 3, seed=4)
        self.assertEqual(result, [100, 99, 99])
        self.assertEqual(rand, 22)
    def test_case_rng(self):
        obj_list = self.generate_objects(100)
        result, rand = f_338(obj_list, 'value', 3, seed=123)
        result2, rand2 = f_338(obj_list, 'value', 3, seed=43)
        self.assertEqual(result, result2)
        self.assertNotEqual(rand, rand2)
        result, rand3 = f_338(obj_list, 'value', 3, seed=123)
        self.assertEqual(rand, rand3)
