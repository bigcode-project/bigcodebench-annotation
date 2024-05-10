import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft


def f_241(range_start=-10, range_end=10, step=0.1):
    """
    Create a generator object that generates a sequence of tuples. Each tuple contains x, sin(x), and cos(x) 
    values. The function then plots the sine and cosine functions using these values along with the absolute 
    difference between the two functions and returns the plot. Finally, it returns the magnitude of the mean 
    and median of the 1D fft of the absolute difference between the two functions.

    Parameters:
    - range_start: The starting value of the x range.
    - range_end: The ending value of the x range.
    - step: The step size for the x values.

    Returns:
    tuple: A tuple containing two items:
        - generator: A generator object producing tuples in the format (x, sin(x), cos(x), abs(sin(x) - cos(x)).
        - ax: An Axes object representing the plot.
        - float: The abs of the mean of the 1D fft of the absolute difference between sin(x) and cos(x).
        - float: The abs of the median of the 1D fft of the absolute difference between sin(x) and cos(x).

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.fft

    Example:
    >>> data, ax, fft_mean, fft_median = f_241()
    >>> print(next(data))
    (-10.0, 0.5440211108893698, -0.8390715290764524, 1.383092639965822)
    """
    if range_start>range_end:
        raise ValueError("range_start cannot be smaller than range_end.")

    x_values = np.arange(range_start, range_end, step)
    data = ((x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x))) for x in x_values)
    fft_values = fft([abs(np.sin(x) - np.cos(x)) for x in x_values])
    _, ax = plt.subplots()
    for x, sin_x, cos_x, abs_x in data:
        ax.scatter(x, sin_x, color='b')
        ax.scatter(x, cos_x, color='r')
        ax.scatter(x, abs_x, color='g')
    
    # We recreate the generator since it was exhausted in the for loop above
    data = ((x, np.sin(x), np.cos(x), abs(np.sin(x) - np.cos(x))) for x in x_values)
    return data, ax, abs(np.mean(fft_values)), abs(np.median(fft_values))


import unittest
import types
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        data, ax, _, _ = f_241()
        self.assertIsInstance(data, types.GeneratorType, "Returned data is not a generator")
        x, sin_x, cos_x, _ = next(data)
        self.assertAlmostEqual(x, -10.0, delta=0.01, msg="Unexpected x value in the first tuple")
        self.assertAlmostEqual(sin_x, np.sin(-10.0), delta=0.01, msg="Unexpected sin(x) value in the first tuple")
        self.assertAlmostEqual(cos_x, np.cos(-10.0), delta=0.01, msg="Unexpected cos(x) value in the first tuple")

    def test_case_2(self):
        data, ax, mean_fft, median_fft = f_241(23, 43, 0.4)
        points = list(data)
        self.assertEqual(len(points), 50, "Unexpected number of points generated")
        self.assertAlmostEqual(points[-1][0], 42.6, delta=0.01, msg="Unexpected last x value")
        self.assertAlmostEqual(round(mean_fft, 2), 0.31, delta=0.01, msg="Unexpected mean of the 1D fft")
        self.assertAlmostEqual(round(median_fft, 2), 0.57, delta=0.01, msg="Unexpected median of the 1D fft")

    def test_case_3(self):
        data, ax, _, _ = f_241()
        points = list(data)
        x_values = [point[0] for point in points]
        abs_diff_values = [point[3] for point in points]
        self.assertTrue(all(-10.0 <= x <= 10.0 for x in x_values), "x values are out of the expected range")
        self.assertTrue(all(0.0 <= x <= 1.42 for x in abs_diff_values), "abs(sin(x) - cos(x)) values are out of the expected range")
        # Check the plot data
        lines = ax.get_children()
        self.assertEqual(len(lines), 610, "Unexpected number of lines in the plot")

    def test_case_4(self):
        with self.assertRaises(ValueError):
            f_241(33, -11, 2)

    def test_case_5(self):
        data, _, mean_fft, median_fft = f_241()
        points = list(data)
        for x, sin_x, cos_x, _ in points:
            self.assertAlmostEqual(sin_x, np.sin(x), delta=0.01, msg=f"sin({x}) value is incorrect")
            self.assertAlmostEqual(cos_x, np.cos(x), delta=0.01, msg=f"cos({x}) value is incorrect")
        self.assertAlmostEqual(round(mean_fft, 2), 1.38, delta=0.01, msg="Unexpected mean of the 1D fft")
        self.assertAlmostEqual(round(median_fft, 2), 0.54, delta=0.01, msg="Unexpected median of the 1D fft")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
