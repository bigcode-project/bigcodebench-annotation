import string
import random
import re


def f_296(elements, pattern, seed=100):
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
    >>> replaced_elements, result = f_296(ELEMENTS, pattern, 234)
    >>> print(replaced_elements)
    ['%vqd%', '%LAG%']
    """
    # Set the seed for reproducibility
    random.seed(seed)
    replaced_elements = []
    
    for element in elements:
        replaced = ''.join([random.choice(string.ascii_letters) for _ in element])
        formatted = '%{}%'.format(replaced)
        replaced_elements.append(formatted)
        
    # Concatenate all the formatted elements into a single string
    concatenated_elements = ''.join(replaced_elements)
    # Search for the regex pattern in the concatenated string
    search_result = re.search(pattern, concatenated_elements)
    # Return the search result
    return replaced_elements, bool(search_result)


import unittest
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Basic test with a given list of elements
        elements = ["abc", "def"]
        replaced_elements, res = f_296(elements, ".*", 234)
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
        replaced_elements, res = f_296(elements, pattern, 104)
        self.assertEqual(len(replaced_elements), len(elements))
        for element in replaced_elements:
            self.assertTrue(element.startswith("%"))
            self.assertTrue(element.endswith("%"))
        # Test the search result
        self.assertFalse(res)

    def test_case_3(self):
        # Test with a longer list of elements
        elements = ["abcdefgh", "ijklmnop", "qrstuvwxyz"]
        replaced_elements, res = f_296(elements, "%+", 101)
        self.assertEqual(len(replaced_elements), len(elements))
        for element in replaced_elements:
            self.assertTrue(element.startswith("%"))
            self.assertTrue(element.endswith("%"))
        # Test the search result
        self.assertTrue(res)

    def test_case_4(self):
        # Test with an empty list of elements
        elements = []
        replaced_elements, _ = f_296(elements, ".*", 123)
        self.assertEqual(len(replaced_elements), len(elements))

    def test_case_5(self):
        # Test with a list containing mixed-case elements
        elements = ["AbC", "dEfG", "HijKL"]
        replaced_elements, _ = f_296(elements, ".*", 456)
        self.assertEqual(len(replaced_elements), len(elements))
        for element in replaced_elements:
            self.assertTrue(element.startswith("%"))
            self.assertTrue(element.endswith("%"))


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    doctest.testmod()
    run_tests()
