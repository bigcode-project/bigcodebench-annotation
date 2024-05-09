from itertools import cycle
from random import choice, seed


def f_710(n_colors, colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple'], rng_seed=None):
    """
    Generates a list representing a color pattern. The pattern consists of 'n_colors' elements 
    and alternates between a cyclic sequence of colors as defined in the parameter 'colors',
    and random colors from the same list.
    Optionally, a seed for the random number generator can be provided for repeatable randomness.

    If n_colors is smaller than or equal to zero an empty list is returned.

    Parameters:
    n_colors (int): The number of colors to include in the pattern. This number indicates the total 
                    elements in the returned list, alternating between cyclic and random colors.
    colors (list of str, optional): The list of colors to generate from. 
                Defaults to  ['Red', 'Green', 'Blue', 'Yellow', 'Purple'].
    rng_seed (int, optional): A seed for the random number generator to ensure repeatability of the color selection. 
                              If 'None', the randomness is based on system time or other sources of entropy.

    Returns:
    list: A list representing the color pattern. Each element of the list is a string indicating 
          the color. For example, with n_colors=4 and a specific seed, the result could be consistent 
          across calls with the same seed.

    Requirements:
    - itertools
    - random

    Examples:
    >>> color_pattern = f_710(4, rng_seed=123)
    >>> print(color_pattern)
    ['Red', 'Red', 'Green', 'Blue']

    >>> colors = ['Brown', 'Green', 'Black']
    >>> color_pattern = f_710(12, colors=colors, rng_seed=42)
    >>> print(color_pattern)
    ['Brown', 'Black', 'Green', 'Brown', 'Black', 'Brown', 'Brown', 'Black', 'Green', 'Green', 'Black', 'Brown']
    """

    # Setting the seed for the random number generator
    if rng_seed is not None:
        seed(rng_seed)

    color_cycle = cycle(colors)
    color_pattern = []

    for _ in range(n_colors):
        color = next(color_cycle) if _ % 2 == 0 else choice(colors)
        color_pattern.append(color)

    return color_pattern


import unittest


class TestCases(unittest.TestCase):
    def test_small_number_of_colors(self):
        # Testing with a small number of colors and a fixed seed for repeatability
        color_pattern = f_710(4, rng_seed=123)
        expected_pattern = ['Red', 'Red', 'Green', 'Blue']  # This pattern is based on the seed value
        self.assertEqual(color_pattern, expected_pattern)

    def test_large_number_of_colors(self):
        # Testing with a large number of colors to check the function's behavior with more extensive patterns
        # Here, we're not checking for exact match due to randomness, but rather size and content
        color_pattern = f_710(100, rng_seed=123)
        self.assertEqual(len(color_pattern), 100)
        self.assertTrue(all(color in ['Red', 'Green', 'Blue', 'Yellow', 'Purple'] for color in color_pattern))

    def test_zero_colors(self):
        # Testing with zero colors, which should return an empty list
        color_pattern = f_710(0, rng_seed=123)
        self.assertEqual(color_pattern, [])

    def test_negative_number_of_colors(self):
        # Testing with a negative number, which should not break the function and return an empty list
        color_pattern = f_710(-4, rng_seed=123)
        self.assertEqual(color_pattern, [])

    def test_repeatability_with_same_seed(self):
        # Testing the function with the same seed value should produce the same results
        color_pattern1 = f_710(10, rng_seed=123)
        color_pattern2 = f_710(10, rng_seed=123)
        self.assertEqual(color_pattern1, color_pattern2)

    def test_randomness_with_different_seeds(self):
        # Testing the function with different seeds should produce different results
        color_pattern1 = f_710(10, rng_seed=123)
        color_pattern2 = f_710(10, rng_seed=456)
        self.assertNotEqual(color_pattern1, color_pattern2)

    def test_no_seed_provided(self):
        # Testing the function without a seed should still produce valid results (though they can't be predetermined)
        color_pattern = f_710(10)  # No seed provided
        self.assertEqual(len(color_pattern), 10)
        self.assertTrue(all(color in ['Red', 'Green', 'Blue', 'Yellow', 'Purple'] for color in color_pattern))

    def test_custom_colors(self):
        colors = ['Brown', 'White', 'Black', "Orange"]
        color_pattern = f_710(10, colors=colors, rng_seed=12)  # No seed provided
        self.assertTrue(all(color in colors for color in color_pattern))
        expected = ['Brown',
                    'Orange',
                    'White',
                    'Black',
                    'Black',
                    'Black',
                    'Orange',
                    'White',
                    'Brown',
                    'Orange']
        self.assertEqual(color_pattern, expected)

    def test_cyclicity(self):
        color_pattern = f_710(1000, rng_seed=1234)  # No seed provided
        colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple']
        color_cycle = cycle(colors)
        for i in range(500):
            self.assertEqual(color_pattern[2*i], next(color_cycle))


def run_tests():
    # Function to execute the unittests
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


# This is to ensure the tests run when this script is executed
if __name__ == "__main__":
    run_tests()