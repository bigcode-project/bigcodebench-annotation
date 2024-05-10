import numpy as np
from sympy import symbols, solve


def f_266(precision=2, seed=0):
    """
    Solve a quadratic equation in the form of ax ^ 2 + bx + c = 0, where a, b, and c randomly generated numbers are between -10 and 10. The solutions are complex numbers rounded to the specified accuracy.

    Parameters:
    precision (int): The number of decimal places to which to round the solutions.
    seed (int, Optional): The seed for the random number generator.

    Returns:
    tuple: A tuple of two solutions formatted as complex numbers (rounded to the specified precision).

    Requirements:
    - numpy
    - math
    - sympy

    Example:
    >>> result = f_266()
    >>> len(result)
    2
    >>> result
    ((-3.86+0j), (-0.54+0j))
    """
    np.random.seed(seed)
    a = np.random.uniform(-10, 10)
    b = np.random.uniform(-10, 10)
    c = np.random.uniform(-10, 10)

    x = symbols('x')
    equation = a * x**2 + b * x + c

    solutions = solve(equation, x)
    solutions = [complex(round(complex(solution).real, precision), round(complex(solution).imag, precision)) for solution in solutions]

    return tuple(solutions)


import unittest
import doctest


class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_266(seed=1789)
        self.assertIsInstance(result, tuple, "The result should be a tuple.")
        self.assertEqual(len(result), 2, "The tuple should have two values.")
        for value in result:
            self.assertEqual(value.real, round(value.real, 2), "The value should be rounded to 2 decimal places.")
            self.assertEqual(value.imag, round(value.imag, 2), "The value should be rounded to 2 decimal places.")
        # Test the output
        self.assertEqual(result, ((-5.15+0j), (0.41+0j)))
        

    def test_case_2(self):
        result = f_266(precision=3)
        for value in result:
            self.assertEqual(value.real, round(value.real, 3), "The value should be rounded to 3 decimal places.")
            self.assertEqual(value.imag, round(value.imag, 3), "The value should be rounded to 3 decimal places.")

    def test_case_3(self):
        result = f_266(precision=0)
        for value in result:
            self.assertEqual(value.real, round(value.real), "The value should be an integer.")
            self.assertEqual(value.imag, round(value.imag), "The value should be an integer.")

    def test_case_4(self):
        result = f_266(precision=4)
        for value in result:
            self.assertEqual(value.real, round(value.real, 4), "The value should be rounded to 4 decimal places.")
            self.assertEqual(value.imag, round(value.imag, 4), "The value should be rounded to 4 decimal places.")

    def test_case_5(self):
        result = f_266(precision=5, seed=1234)
        for value in result:
            self.assertEqual(value.real, round(value.real, 5), "The value should be rounded to 5 decimal places.")
            self.assertEqual(value.imag, round(value.imag, 5), "The value should be rounded to 5 decimal places.")
        # Test the output
        self.assertEqual(result, ((0.19792-0.40336j), (0.19792+0.40336j)))


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
