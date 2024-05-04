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
    
    def setUp(self):
        # Setting up a common letters array and sorted dictionary for use in all tests
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.sorted_dict = f_1002(self.letters)

    def test_case_1(self):
        # Check if the function returns a dictionary
        self.assertIsInstance(self.sorted_dict, dict, "The function should return a dictionary.")

    def test_case_2(self):
        # Ensure all keys in the sorted dictionary are within the provided letters
        all_letters = all([key in self.letters for key in self.sorted_dict.keys()])
        self.assertTrue(all_letters, "All keys of the dictionary should be letters.")
        
    def test_case_3(self):
        # Ensure all values are lists of integers
        all_lists = all([isinstance(val, list) and all(isinstance(i, int) for i in val) for val in self.sorted_dict.values()])
        self.assertTrue(all_lists, "All values of the dictionary should be lists of integers.")
        
    def test_case_4(self):
        # Check if the dictionary is sorted by the mean values in descending order
        means = [statistics.mean(val) for val in self.sorted_dict.values()]
        self.assertTrue(all(means[i] >= means[i + 1] for i in range(len(means) - 1)), "The dictionary should be sorted in descending order based on the mean of its values.")
    
    def test_case_5(self):
        # Check if the dictionary includes all provided letters as keys
        self.assertEqual(set(self.sorted_dict.keys()), set(self.letters), "The dictionary should have all provided letters as keys.")
        
if __name__ == "__main__":
    run_tests()