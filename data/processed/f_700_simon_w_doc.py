import random
import string

def f_826(max_length, n_samples, seed=None):
    """Generate a list containing random strings of lowercase letters. Each string's length varies from 1 to `max_length`.
    An optional seed can be set for the random number generator for reproducible results.

    Note:
    The function utilizes the `random.choices` function to generate random strings and combines them into a list.

    Parameters:
    max_length (int): The maximum length of the strings.
    n_samples (int): The number of strings to return.
    seed (int, optional): A seed for the random number generator. If None, the generator is initialized without a seed.

    Returns:
    list: A list containing random strings. Each string is a random combination of lowercase letters, 
    and their lengths will vary from 1 to `max_length`.

    Requirements:
    - random
    - string

    Raises:
    ValueError: If max_length is smaller than 1.

    Example:
    >>> f_826(3, 12, seed=12)
    ['gn', 'da', 'mq', 'rp', 'aqz', 'ex', 'o', 'b', 'vru', 'a', 'v', 'ncz']
    >>> f_826(5, n_samples=8, seed=1)
    ['ou', 'g', 'tmjf', 'avlt', 's', 'sfy', 'aao', 'rzsn']

    """
    if max_length < 1:
        raise ValueError("max_length must be larger than or equal to 1.")
    LETTERS = string.ascii_lowercase
    if seed is not None:
        random.seed(seed)
    all_combinations = []
    for i in range(n_samples):
        random_length = random.randint(1, max_length)
        combination = ''.join(random.choices(LETTERS, k=random_length))
        all_combinations.append(combination)
    return all_combinations

"""
This script contains tests for the function f_826.
Each test checks a specific aspect of the function's behavior.
"""
import unittest
import random
class TestCases(unittest.TestCase):
    def test_length_and_content(self):
        """Test the length of the output and whether it contains valid strings."""
        seed = 1  # for reproducibility
        max_length = 5
        result = f_826(max_length, n_samples=10, seed=seed)
        
        # All outputs should be strings
        self.assertTrue(all(isinstance(item, str) for item in result))
        # All strings should be of length <= max_length and > 0
        self.assertTrue(all(1 <= len(item) <= max_length for item in result))
        expected = ['ou', 'g', 'tmjf', 'avlt', 's', 'sfy', 'aao', 'rzsn', 'yoir', 'yykx']
        self.assertCountEqual(result, expected)
    def test_randomness(self):
        """Test that setting a seed produces reproducible results."""
        seed = 2
        result1 = f_826(3, seed=seed, n_samples=100)
        result2 = f_826(3, seed=seed, n_samples=100)
        self.assertEqual(result1, result2)  # results should be same with same seed
    def test_varying_length(self):
        """Test with varying n to check the function's robustness with different input sizes."""
        seed = 3
        for n in range(1, 15):  # testing multiple sizes
            result = f_826(n, seed=seed, n_samples=10)
            self.assertTrue(all(1 <= len(item) <= n for item in result))
    def test_negative_input(self):
        """Test how the function handles negative input. It should handle it gracefully."""
        with self.assertRaises(ValueError):
            f_826(-1, n_samples=22)  # negative numbers shouldn't be allowed
    def test_zero_length(self):
        """Test how the function handles zero input. It should handle it gracefully or according to its specification."""
        self.assertRaises(ValueError, f_826, 0, n_samples=5)
