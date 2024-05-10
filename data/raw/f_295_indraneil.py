import random
import string
from matplotlib import pyplot as plt


def f_295(elements, seed=100):
    """
    Format each string in the given list "elements" into a pattern "% {0}%", 
    where {0} is a randomly generated alphanumeric string of length 5. Additionally,
    return the plot axes of an histogram of the occurrence of each character across 
    all the strings and a dictionary containing the count of each character in all 
    the formatted strings.
    
    Parameters:
    elements (List[str]): A list of string elements to be formatted.
    seed (int, Optional): The seed for the random number generator. Defaults to 100.
    
    Returns:
    List[str]: A list of elements formatted with random patterns.
    plt.Axes: The axes object of the histogram plot.
    dict: A dictionary containing the count of each character in the formatted strings.
    
    Requirements:
    - random
    - string
    - matplotlib.pyplot
    
    Example:
    >>> patterns, ax, counts = f_295(['abc', 'def'])
    >>> patterns
    ['% jCVRT%', '% AXHeC%']
    >>> counts
    {'%': 4, ' ': 2, 'j': 1, 'C': 2, 'V': 1, 'R': 1, 'T': 1, 'A': 1, 'X': 1, 'H': 1, 'e': 1}
    """
    random.seed(seed)
    random_patterns = []

    for element in elements:
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        pattern = '% {}%'.format(random_str)
        random_patterns.append(pattern)

    # Histogram of character occurrences
    char_count = {}
    for pattern in random_patterns:
        for char in pattern:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            
    # Getting the axes object for the histogram plot
    _, ax = plt.subplots()
    ax.bar(char_count.keys(), char_count.values())

    return random_patterns, ax, char_count


import unittest
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a list containing two strings
        result, ax, data = f_295(['hello', 'world'], seed=39)
        self.assertEqual(len(result), 2)
        for pattern in result:
            self.assertTrue(pattern.startswith('%'))
            self.assertTrue(pattern.endswith('%'))
            self.assertEqual(len(pattern), 8) # 5 characters + 3 special characters
        
        # Test the histogram plot
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.patches), 12)

        # Test the character count dictionary
        self.assertEqual(data['%'], 4)

    def test_case_2(self):
        # Test with an empty list
        result, _, _ = f_295([])
        self.assertEqual(result, [])

    def test_case_3(self):
        # Test with a list containing multiple identical strings
        result, _, _ = f_295(['test', 'test', 'test'])
        self.assertEqual(len(result), 3)
        for pattern in result:
            self.assertTrue(pattern.startswith('%'))
            self.assertTrue(pattern.endswith('%'))
            self.assertEqual(len(pattern), 8)

    def test_case_4(self):
        # Test with a list containing single character strings
        result, ax, data = f_295(['a', 'b', 'c'])
        self.assertEqual(len(result), 3)
        for pattern in result:
            self.assertTrue(pattern.startswith('%'))
            self.assertTrue(pattern.endswith('%'))
            self.assertEqual(len(pattern), 8)

        # Test the character count dictionary
        self.assertEqual(data['C'], 2)
        self.assertEqual(data['%'], 6)
        self.assertEqual(data['V'], 1)
    
    def test_case_5(self):
        # Test with a list containing strings of varying lengths
        result, _, _ = f_295(['short', 'mediumlength', 'averyverylongstring'])
        self.assertEqual(len(result), 3)
        for pattern in result:
            self.assertTrue(pattern.startswith('%'))
            self.assertTrue(pattern.endswith('%'))
            self.assertEqual(len(pattern), 8)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
