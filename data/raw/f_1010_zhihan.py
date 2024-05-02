import numpy as np
import itertools
import statistics

# Constant seed for deterministic randomness
SEED = 42


def f_1010(T1, range_=100):
    """
    Convert elements in 'T1' to integers and create a list of random integers with fixed randomness.
    The size of the list is the sum of the integers in `T1`. Calculate and return the mean, median, and mode of the list.

    Parameters:
    T1 (tuple): A tuple of tuples, each containing string representations of integers.
    range_ (int, optional): The upper limit (exclusive) for generating random integers. Default is 100.

    Returns:
    tuple: A tuple containing the mean, median, and mode of the list of random integers.
           The mean and median are floats, and the mode is an integer.

    Requirements:
    - numpy for random number generation, calculating mean, and median
    - itertools for flattening the list
    - statistics for calculating the mode

    Example:
    >>> T1 = (('13', '17', '18', '21', '32'), ('07', '11', '13', '14', '28'), ('01', '05', '06', '08', '15', '16'))
    >>> stats = f_1010(T1)
    >>> print(stats)
    (50.2, 48.0, 27)

    >>> stats = f_1010(T1, range_=50)
    >>> print(stats)
    (24.5, 25.0, 17)
    """
    # Convert strings to integers and flatten the list
    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_nums = sum(flattened_list)

    # Initialize numpy random state with the global SEED
    random_state = np.random.RandomState(SEED)

    # Generate random numbers within the specified range using the seeded random state
    random_nums = random_state.randint(0, range_, total_nums)

    # Calculate mean, median, and mode
    mean = np.mean(random_nums)
    median = np.median(random_nums)
    mode = statistics.mode(random_nums)

    return mean, median, mode


import unittest
import numpy as np
import statistics


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        T1 = (('1', '2'), ('2', '3'), ('3', '4'))
        mean, median, mode = f_1010(T1)
        self.assertIsInstance(mean, float)
        self.assertIsInstance(median, float)
        self.assertTrue(0 <= mean <= 100)
        self.assertTrue(0 <= median <= 100)
        self.assertTrue(0 <= mode <= 100)

    def test_case_2(self):
        T1 = (('1', '2', '3'), ('4', '5'), ('6', '7', '8', '9'))
        mean, median, mode = f_1010(T1)
        self.assertIsInstance(mean, float)
        self.assertIsInstance(median, float)
        self.assertTrue(0 <= mean <= 100)
        self.assertTrue(0 <= median <= 100)
        self.assertTrue(0 <= mode <= 100)

    def test_basic_functionality(self):
        T1 = (('10', '20', '30'), ('40', '50', '60'))
        mean, median, mode = f_1010(T1)
        expected_mean, expected_median, expected_mode = (48.98095238095238, 50.0, 61)
        np.testing.assert_allclose(mean, expected_mean, rtol=1e-5)
        np.testing.assert_allclose(median, expected_median, rtol=1e-5)
        self.assertEqual(mode, expected_mode)

    def test_single_element(self):
        T1 = (('1',),)
        mean, median, mode = f_1010(T1)
        expected_mean, expected_median, expected_mode = (51.0, 51.0, 51)
        np.testing.assert_allclose(mean, expected_mean, rtol=1e-5)
        np.testing.assert_allclose(median, expected_median, rtol=1e-5)
        self.assertEqual(mode, expected_mode)

    def test_large_numbers(self):
        T1 = (('1000', '2000'), ('3000', '4000', '5000'))
        mean, median, mode = f_1010(T1)
        expected_mean, expected_median, expected_mode = (49.525933333333334, 50.0, 16)
        np.testing.assert_allclose(mean, expected_mean, rtol=1e-5)
        np.testing.assert_allclose(median, expected_median, rtol=1e-5)
        self.assertEqual(mode, expected_mode)


if __name__ == "__main__":
    run_tests()
