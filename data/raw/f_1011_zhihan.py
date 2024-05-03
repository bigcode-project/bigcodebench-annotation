import numpy as np
import itertools
from random import randint

SEED = 42


def f_1011(T1, range_=100):
    """
    Converts string representations of integers in a nested tuple structure to integers,
    generates a list of random integers with a length equal to the sum of these integers,
    and calculates specific percentiles of the random integers list.

    Parameters:
    - T1 (tuple of tuples): Each inner tuple contains string representations of integers.
    - range_ (int, optional): The upper bound (exclusive) for the random integers generation. Defaults to 100.

    Returns:
    - tuple: A tuple containing the 25th, 50th, and 75th percentiles (p25, p50, p75) of the generated list of random integers.

    Requirements:
    - numpy
    - itertools
    - random

    Example:
    >>> T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
    >>> f_1011(T1)
    (23.0, 51.0, 74.0)
    >>> T1 = (('1', '2', '3'),)
    >>> f_1011(T1)
    (27.75, 55.5, 68.25)
    """

    # Convert strings to integers and flatten the list
    flattened_list = [int(number) for sublist in T1 for number in sublist]
    total_nums = sum(flattened_list)

    # Initialize numpy random state with the provided seed
    random_state = np.random.RandomState(SEED)

    # Generate random numbers within the specified range using the seeded random state
    random_nums = random_state.randint(0, range_, total_nums)

    # Calculate percentiles
    p25 = np.percentile(random_nums, 25)
    p50 = np.percentile(random_nums, 50)
    p75 = np.percentile(random_nums, 75)

    return p25, p50, p75


import unittest


class TestCases(unittest.TestCase):

    def test_single_tuple(self):
        T1 = (('1', '2', '3'),)
        result = f_1011(T1)
        expected = (27.75, 55.5, 68.25)
        np.testing.assert_allclose(result, expected, rtol=1e-5, atol=1e-8)

    def test_large_range(self):
        T1 = (('10', '20', '30'),)
        result = f_1011(T1, range_=1000)
        expected = (235.75, 470.0, 699.25)
        np.testing.assert_allclose(result, expected, rtol=1e-5, atol=1e-8)

    def test_multiple_tuples(self):
        T1 = (('1', '2'), ('3', '4'), ('5',))
        result = f_1011(T1)
        expected = (22.0, 71.0, 84.0)
        np.testing.assert_allclose(result, expected, rtol=1e-5, atol=1e-8)

    def test_identical_numbers(self):
        T1 = (('5', '5'), ('5', '5'))
        result = f_1011(T1)
        expected = (22.5, 56.0, 83.0)
        np.testing.assert_allclose(result, expected, rtol=1e-5, atol=1e-8)

    def test_single_large_tuple(self):
        T1 = (('1',) * 1000,)  # Tuple with 1000 '1's
        result = f_1011(T1)
        expected = (23.0, 50.0, 74.0)
        np.testing.assert_allclose(result, expected, rtol=1e-5, atol=1e-8)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
