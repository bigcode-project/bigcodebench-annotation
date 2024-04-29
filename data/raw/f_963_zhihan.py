from collections import Counter
from operator import itemgetter
import itertools


def f_963(word_dict):
    """
    Given a dictionary of words as keys and letters as values, count the frequency of each letter in the words.
    
    Parameters:
    word_dict (dict): The dictionary with words as keys and their letters as values.
    
    Returns:
    dict: A dictionary with letters as keys and their frequencies as values.
    
    Requirements:
    - collections.Counter
    - operator.itemgetter
    - itertools
    
    Example:
    >>> word_dict = {'apple': 'a', 'banana': 'b', 'cherry': 'c', 'date': 'd', 'elderberry': 'e', 'fig': 'f', 'grape': 'g', 'honeydew': 'h'}
    >>> counts = f_963(word_dict)
    >>> print(counts)
    {'e': 10, 'a': 8, 'r': 4, 'p': 3, 'b': 2, 'n': 2, 'c': 2, 'd': 2, 'y': 2, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'l': 1, 'o': 1, 't': 1, 'u': 1, 'w': 1}
    """
    letters = list(itertools.chain.from_iterable(word_dict.keys()))
    count_dict = dict(Counter(letters))
    
    sorted_dict = dict(sorted(count_dict.items(), key=itemgetter(1), reverse=True))
    
    return sorted_dict

import unittest
from collections import Counter

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_dict = {'apple': 'a', 'banana': 'b', 'cherry': 'c', 'date': 'd'}
        expected_output = dict(Counter('apple' + 'banana' + 'cherry' + 'date'))
        result = f_963(input_dict)
        self.assertDictEqual(result, expected_output)
        
    def test_case_2(self):
        input_dict = {'fig': 'f', 'grape': 'g', 'honeydew': 'h'}
        expected_output = dict(Counter('fig' + 'grape' + 'honeydew'))
        result = f_963(input_dict)
        self.assertDictEqual(result, expected_output)
    
    def test_case_3(self):
        input_dict = {'apple': 'a', 'elderberry': 'e', 'grape': 'g'}
        expected_output = dict(Counter('apple' + 'elderberry' + 'grape'))
        result = f_963(input_dict)
        self.assertDictEqual(result, expected_output)
    
    def test_case_4(self):
        input_dict = {'date': 'd', 'fig': 'f'}
        expected_output = dict(Counter('date' + 'fig'))
        result = f_963(input_dict)
        self.assertDictEqual(result, expected_output)
        
    def test_case_5(self):
        input_dict = {'apple': 'a', 'banana': 'b', 'cherry': 'c', 'date': 'd', 'elderberry': 'e', 'fig': 'f', 'grape': 'g', 'honeydew': 'h'}
        expected_output = dict(Counter('apple' + 'banana' + 'cherry' + 'date' + 'elderberry' + 'fig' + 'grape' + 'honeydew'))
        result = f_963(input_dict)
        self.assertDictEqual(result, expected_output)

# Running the tests to ensure they pass
run_tests()
if __name__ == "__main__":
    run_tests()