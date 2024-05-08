import re
import random
import string

def f_724(n, pattern, seed=None):
    """
    Generate a random string of length 'n' and find all non-overlapping matches
    of the regex 'pattern'.

    The function generates a random string of ASCII Letters and Digits using 
    the random module. By providing a seed the results are reproducable.
    Non overlapping matches of the provided pattern are then found using the re
    module.
    
    Parameters:
    n (int): The length of the random string to be generated.
    pattern (str): The regex pattern to search for in the random string.
    seed (int, optional): A seed parameter for the random number generator for reproducible results. Defaults to None.

    Returns:
    list: A list of all non-overlapping matches of the regex pattern in the generated string.

    Requirements:
    - re
    - random
    - string

    Example:
    >>> f_724(100, r'[A-Za-z]{5}', seed=12345)
    ['mrKBk', 'BqJOl', 'NJlwV', 'UfHVA', 'LGkjn', 'vubDv', 'GSVAa', 'kXLls', 'RKlVy', 'vZcoh', 'FnVZW', 'JQlqL']

    >>> f_724(1000, r'[1-9]{2}', seed=1)
    ['51', '84', '16', '79', '16', '28', '63', '82', '94', '18', '68', '42', '95', '33', '64', '38', '69', '56', '32', '16', '18', '19', '27']
     """
    if seed is not None:
        random.seed(seed)
    rand_str = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    matches = re.findall(pattern, rand_str)
    return matches

import unittest
class TestCases(unittest.TestCase):
    
    def test_valid_pattern_matching(self):
        test_length = 100
        test_pattern = r'[A-Za-z]{5}'
        test_seed = 12345  # using a seed for consistency
        expected_matches = [
            'mrKBk',
            'BqJOl',
            'NJlwV',
            'UfHVA',
            'LGkjn',
            'vubDv',
            'GSVAa',
            'kXLls',
            'RKlVy',
            'vZcoh',
            'FnVZW',
            'JQlqL'
        ]
        actual_matches = f_724(test_length, test_pattern, seed=test_seed)
        self.assertEqual(actual_matches, expected_matches)
    def test_no_matches_found(self):
        test_length = 100
        test_pattern = r'XYZ'
        test_seed = 12345
        expected_matches = []
        actual_matches = f_724(test_length, test_pattern, seed=test_seed)
        self.assertEqual(actual_matches, expected_matches)
    def test_zero_length_string(self):
        test_length = 0
        test_pattern = r'[A-Za-z0-9]{5}'
        expected_matches = []
        actual_matches = f_724(test_length, test_pattern, seed=None)
        self.assertEqual(actual_matches, expected_matches)
    def test_unusual_pattern(self):
        test_length = 100
        test_pattern = r'[^A-Za-z0-9]+'
        test_seed = 67890
        expected_matches = []
        actual_matches = f_724(test_length, test_pattern, seed=test_seed)
        self.assertEqual(actual_matches, expected_matches)
    def test_extreme_input_values(self):
        test_length = 10000  # Reduced size for the environment's stability
        test_pattern = r'[A-Za-z]{5}'
        actual_matches = f_724(test_length, test_pattern, seed=None)
        self.assertIsInstance(actual_matches, list)
