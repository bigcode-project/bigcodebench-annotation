import numpy as np
from scipy.stats import norm


def f_677(data: np.ndarray, threshold: float = 2.0) -> list:
    """
    Determine the outlier indices in a 1D numpy array based on the Z score.

    First a normal distribution is fitted to the data, the mean and standard
    deviation is used to calculate the z scores of each datapoint. 
    If the absolute z score of a datapoint is larger than threshold it is
    considered an outlier and its index is recorded.

    If the standard deviation is 0, an empty list is returned as outliers. 
    
    Parameters:
    data (numpy.ndarray): The 1D numpy array to check for outliers.
    threshold (float): The outlier threshold. Defaults to 2.

    Returns:
    list: The indices of outliers in the data where Z score > threshold. Empty if standard deviation is 0
    float: The mean of the fitted normal distribution.
    float: The variance of the fitted normal distribution.

    Requirements:
    - numpy for getting the indices of the outliers
    - scipy.stats.norm for fitting a normal distribution to the data

    Example:
    >>> data = np.array([1, 2, 3, 4, 5, 6, 100])
    >>> f_677(data)
    ([0, 1, 2, 3, 4, 6], 17.285714285714285, 33.804962804358794)

    >>> data = np.array([-10, 3, 5, 5, 5, 5, 5, 7, 20])
    >>> outliers, mean, var = f_677(data, threshold=4)
    >>> print(outliers)
    >>> print(mean)
    >>> print(var)
    [0, 8]
    5.0
    7.133644853010899 
    """
    # Calculate the z-scores
    mean, var = norm.fit(data)
    std_dev = np.sqrt(var)
    if std_dev == 0:
        return [], mean, var
    z_scores = (data - mean) / std_dev
    outliers = np.where(np.abs(z_scores) > threshold)

    return list(outliers[0]), mean, var


import unittest
import numpy as np


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_case_1(self):
        data = np.array([1, 2, 3, 4, 5, 6, 100])
        result, mean, var = f_677(data)
        self.assertEqual(result, [0, 1, 2, 3, 4, 6])
        self.assertAlmostEqual(mean, 17.2, delta=0.1)
        self.assertAlmostEqual(var, 33.8, delta=0.1)

    def test_case_2(self):
        data = np.array([1, 2, 3, 4, 5, 6, 7])
        result, mean, var = f_677(data)
        self.assertEqual(result, [0, 6])
        self.assertAlmostEqual(mean, 4, delta=0.1)
        self.assertAlmostEqual(var, 2, delta=0.1)

    def test_case_3(self):
        data = np.array([5, 5, 5, 5, 5])
        result, mean, var = f_677(data)
        self.assertEqual(result, [])
        self.assertAlmostEqual(mean, 5, delta=0.1)
        self.assertAlmostEqual(var, 0, delta=0.1)

    def test_case_4(self):
        from faker import Faker
        fake = Faker()
        fake.seed_instance(12)
        data = np.array([fake.random_int(min=0, max=100) for _ in range(10000)])
        result, mean, var = f_677(data)
        self.assertEqual(len(result), 7871)
        self.assertAlmostEqual(mean, 50.28, delta=0.1)
        self.assertAlmostEqual(var, 29.03, delta=0.1)

    def test_case_5(self):
        data = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 50])
        result, mean, var = f_677(data, threshold=0.5)
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 11])
        self.assertAlmostEqual(mean, 4.17, delta=0.1)
        self.assertAlmostEqual(var, 14.14, delta=0.1)



if __name__ == "__main__":
    run_tests()
