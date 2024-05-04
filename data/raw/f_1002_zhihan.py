import random
import statistics

# Constants
# LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def f_1002(LETTERS):
    """
    Create a dictionary in which keys are random letters and values are lists of random integers.
    The dictionary is then sorted by the mean of the values in descending order, demonstrating the use of the statistics library.
    
    Parameters:
        LETTERS (list of str): A list of characters used as keys for the dictionary.
    
    Returns:
    dict: The sorted dictionary with letters as keys and lists of integers as values, sorted by their mean values.
    
    Requirements:
    - random
    - statistics
    
    Example:
    >>> import random
    >>> random.seed(42)
    >>> sorted_dict = f_1002(['a', 'b', 'c'])
    >>> list(sorted_dict.keys())
    ['a', 'b', 'c']
    >>> isinstance(sorted_dict['a'], list)
    True
    >>> type(sorted_dict['a'])  # Check type of values
    <class 'list'>
    """
    random_dict = {k: [random.randint(0, 100) for _ in range(random.randint(1, 10))] for k in LETTERS}
    sorted_dict = dict(sorted(random_dict.items(), key=lambda item: statistics.mean(item[1]), reverse=True))
    return sorted_dict

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        sorted_dict = f_1002()
        self.assertIsInstance(sorted_dict, dict, "The function should return a dictionary.")

    def test_case_2(self):
        sorted_dict = f_1002()
        all_letters = all([key in LETTERS for key in sorted_dict.keys()])
        self.assertTrue(all_letters, "All keys of the dictionary should be letters.")
        
    def test_case_3(self):
        sorted_dict = f_1002()
        all_lists = all([isinstance(val, list) and all(isinstance(i, int) for i in val) for val in sorted_dict.values()])
        self.assertTrue(all_lists, "All values of the dictionary should be lists of integers.")
        
    def test_case_4(self):
        sorted_dict = f_1002()
        sums = [sum(val) for val in sorted_dict.values()]
        self.assertTrue(all(sums[i] >= sums[i + 1] for i in range(len(sums) - 1)), "The dictionary should be sorted in descending order based on the sum of its values.")
    
    def test_case_5(self):
        sorted_dict = f_1002()
        self.assertEqual(set(sorted_dict.keys()), set(LETTERS), "The dictionary should have all letters as keys.")
if __name__ == "__main__":
    run_tests()