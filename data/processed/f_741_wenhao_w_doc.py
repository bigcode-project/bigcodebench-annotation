import numpy as np
import random

def f_264(length=10000, seed=0):
    """
    Generates a random walk of a specified length. A random walk is a path that consists of a series of random steps
    on some mathematical space. In this case, the steps are either +1 or -1, chosen with equal probability.

    Parameters:
    - length (int): The number of steps in the random walk. Must be a non-negative integer. Default is 10000.
    - seed (int, optional): An optional seed value to initialize the random number generator. Use this for reproducible results.
    
    Requirements:
    - numpy
    - random
    
    Returns:
    - np.array: A numpy array representing the positions of the walk at each step. Starts at 0.

    Raises:
    - ValueError: If `length` is negative.
    
    Example:
    >>> random.seed(0)     # For reproducibility in doctest
    >>> walk = f_264(5)
    >>> walk.tolist()
    [0, 1, 2, 1, 0, 1]
    """
    if length < 0:
        raise ValueError("length must be a non-negative integer")
    random.seed(seed)
    steps = [1 if random.random() > 0.5 else -1 for _ in range(length)]
    walk = np.cumsum([0] + steps)  # Starts at 0
    return walk

import unittest
class TestCases(unittest.TestCase):
    def setUp(self):
        random.seed(42)  # Setting seed for reproducibility
    def test_default_length(self):
        walk = f_264(seed=42)
        self.assertEqual(len(walk), 10001)  # Includes starting point
    def test_custom_length(self):
        walk = f_264(5000, seed=42)
        self.assertEqual(len(walk), 5001)  # Includes starting point
    def test_first_step_zero(self):
        walk = f_264(1, seed=42)
        self.assertEqual(walk[0], 0)  # First position should be 0
    def test_negative_length(self):
        with self.assertRaises(ValueError):
            f_264(-1)
    def test_output_type(self):
        walk = f_264(5, seed=42)
        self.assertEqual(walk.tolist(), [0, 1, 0, -1, -2, -1])
