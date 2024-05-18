from collections import Counter
import json
import random


# Constants
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def f_304(n, file_name, seed=77):
    """
    Create a json file with a number of n randomly selected words from a constant list named WORDS.
    
    Parameters:
    n (int): The number of words to select from the list.
    file_name (str): The name of the json file to be generated.
    seed (int, Optional): The seed for the random number generator. Defaults to 77.
    
    Returns:
    str: The name of the json file generated.

    Requirements:
    - collections
    - json
    - random

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()
    >>> file_name = temp_dir + "/word_counts.json"
    >>> f_304(5, file_name, 29).endswith('word_counts.json')
    True
    """
    random.seed(seed)
    if n < 1 or n > len(WORDS):
        raise ValueError('n must be greater than 0')
    random.shuffle(WORDS)
    selected_words = WORDS[:n]
    counts = Counter(selected_words)

    with open(file_name, 'w') as f:
        json.dump(dict(counts), f)

    return file_name


import unittest
import os
import doctest


class TestCases(unittest.TestCase):
    file_name = "word_counts.json"

    def tearDown(self) -> None:
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_case_1(self):
        # Test with n = 3
        self.file_name = f_304(3, self.file_name)
        self.assertTrue(os.path.exists(self.file_name))
        with open(self.file_name, 'r') as f:
            data = json.load(f)
        self.assertEqual(len(data), 3)
        
    def test_case_2(self):
        # Test with n = 5
        self.file_name = f_304(5, self.file_name, 29)
        self.assertTrue(os.path.exists(self.file_name))
        with open(self.file_name, 'r') as f:
            data = json.load(f)
        self.assertEqual(len(data), 5)
        # Test if the counts are correct
        self.assertEqual(data['honeydew'], 1)
        self.assertEqual(data['elderberry'], 1)
        self.assertEqual(data['grape'], 1)
        self.assertEqual(data['cherry'], 1)
        self.assertEqual(data['banana'], 1)
        
    def test_case_3(self):
        # Test with n less than 1
        with self.assertRaises(ValueError):
            f_304(0, self.file_name)
            
    def test_case_4(self):
        # Test with n greater than length of WORDS list
        with self.assertRaises(ValueError):
            f_304(100, self.file_name)
            
    def test_case_5(self):
        # Test with n equal to length of WORDS list
        self.file_name = f_304(
            len(
                ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
            ),
            self.file_name
        )
        self.assertTrue(os.path.exists(self.file_name))
        with open(self.file_name, 'r') as f:
            data = json.load(f)
        self.assertEqual(
            len(data), 
            len(
                ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
            )
        )


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    run_tests()
    doctest.testmod()
