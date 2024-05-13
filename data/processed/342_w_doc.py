import string
import random
import re


def task_func(elements, pattern, seed=100):
    """
    Replace each character in each element of the Elements list with a random 
    character and format the element into a pattern "%{0}%", where {0} is the
    replaced element. Finally, concatenate all the formatted elements into a 
    single string and search for the regex pattern specified in the parameter 
    pattern. Return the true or false value based on the search result.
        
    Parameters:
        elements (List[str]): The list of elements.
        pattern (str): The pattern to format the elements.
        seed (int, Optional): The seed for the random number generator. Defaults to 100.
    
    Returns:    
        List[str]: The list of formatted elements with replaced characters.
        bool: The search result based on the regex pattern.
        
    Requirements:
        - re
        - string
        - random
        
    Example:
    >>> ELEMENTS = ["abc", "def"]
    >>> pattern = ".*"
    >>> replaced_elements, result = task_func(ELEMENTS, pattern, 234)
    >>> print(replaced_elements)
    ['%vqd%', '%LAG%']
    """

    random.seed(seed)
    replaced_elements = []
    for element in elements:
        replaced = ''.join([random.choice(string.ascii_letters) for _ in element])
        formatted = '%{}%'.format(replaced)
        replaced_elements.append(formatted)
    concatenated_elements = ''.join(replaced_elements)
    search_result = re.search(pattern, concatenated_elements)
    return replaced_elements, bool(search_result)

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Basic test with a given list of elements
        elements = ["abc", "def"]
        replaced_elements, res = task_func(elements, ".*", 234)
        self.assertEqual(len(replaced_elements), len(elements))
        for element in replaced_elements:
            self.assertTrue(element.startswith("%"))
            self.assertTrue(element.endswith("%"))
        # Test the search result
        self.assertTrue(res)
    def test_case_2(self):
        # Test with a single-character list of elements
        elements = ["a"]
        # Test with a complex pattern
        pattern = ".*[a-z]{3}.*"
        replaced_elements, res = task_func(elements, pattern, 104)
        self.assertEqual(len(replaced_elements), len(elements))
        for element in replaced_elements:
            self.assertTrue(element.startswith("%"))
            self.assertTrue(element.endswith("%"))
        # Test the search result
        self.assertFalse(res)
    def test_case_3(self):
        # Test with a longer list of elements
        elements = ["abcdefgh", "ijklmnop", "qrstuvwxyz"]
        replaced_elements, res = task_func(elements, "%+", 101)
        self.assertEqual(len(replaced_elements), len(elements))
        for element in replaced_elements:
            self.assertTrue(element.startswith("%"))
            self.assertTrue(element.endswith("%"))
        # Test the search result
        self.assertTrue(res)
    def test_case_4(self):
        # Test with an empty list of elements
        elements = []
        replaced_elements, _ = task_func(elements, ".*", 123)
        self.assertEqual(len(replaced_elements), len(elements))
    def test_case_5(self):
        # Test with a list containing mixed-case elements
        elements = ["AbC", "dEfG", "HijKL"]
        replaced_elements, _ = task_func(elements, ".*", 456)
        self.assertEqual(len(replaced_elements), len(elements))
        for element in replaced_elements:
            self.assertTrue(element.startswith("%"))
            self.assertTrue(element.endswith("%"))
