import random
import math


def f_689(range_start=1, range_end=100, pairs_count=10, random_seed=None):
    """
    Create a generator object that generates a sequence of tuples.
    Each tuple contains two random numbers and the square root of their
    absolute difference.

    A random seed is used to have reproducability in the outputs.

    Parameters:
    - range_start (int): The start of the range for random numbers. Default is 1.
    - range_end (int): The end of the range for random numbers. Default is 100.
    - pairs_count (int): The number of pairs to generate. Default is 10.
    - random_seed (int): Seed used for rng. Default is None.
    
    Returns:
    generator: A generator object that produces tuples in the format
               (num1, num2, square root of absolute difference).

    Requirements:
    - random
    - math

    Example:
    >>> pairs = f_689()
    >>> print(next(pairs))
    (23, 89, 66)

    >>> pairs = f_689(1, 3, pairs_count=25, random_seed=14)
    >>> print(next(pairs))
    (1, 3, 1.4142135623730951)
    """
    random.seed(random_seed)
    pairs = [(random.randint(range_start, range_end), random.randint(range_start, range_end)) for _ in range(pairs_count)]
    return ((x, y, math.sqrt(abs(x - y))) for x, y in pairs)

import unittest
from faker import Faker
import math


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    faker = Faker()

    def test_rng(self):
        pairs1 = f_689(random_seed=42)
        pairs2 = f_689(random_seed=42)
        for _ in range(10):
            self.assertEqual(next(pairs1), next(pairs2))

    def test_case_1(self):
        pairs = f_689(random_seed=1)
        self.assertIsInstance(pairs, type((x for x in range(1))))
        expected = [
            (18, 73, 7.416198487095663),
            (98, 9, 9.433981132056603),
            (33, 16, 4.123105625617661),
            (64, 98, 5.830951894845301),
            (58, 61, 1.7320508075688772),
            (84, 49, 5.916079783099616),
            (27, 13, 3.7416573867739413),
            (63, 4, 7.681145747868608),
            (50, 56, 2.449489742783178),
            (78, 98, 4.47213595499958)
        ]
        for _ in range(10):
            x, y, diff = next(pairs)
            self.assertEqual(diff, math.sqrt(abs(x - y)))
            self.assertEqual((x, y, diff), expected[_])

    def test_case_2(self):
        pairs = f_689(50, 150, random_seed=12)
        self.assertIsInstance(pairs, type((x for x in range(1))))
        expected = [
            (110, 84, 5.0990195135927845),
            (134, 117, 4.123105625617661),
            (135, 94, 6.4031242374328485),
            (68, 98, 5.477225575051661),
            (51, 97, 6.782329983125268),
            (111, 85, 5.0990195135927845),
            (132, 108, 4.898979485566356),
            (138, 126, 3.4641016151377544),
            (79, 121, 6.48074069840786),
            (50, 134, 9.16515138991168)
        ]
        for _ in range(10):
            x, y, diff = next(pairs)
            self.assertTrue(50 <= x <= 150)
            self.assertTrue(50 <= y <= 150)
            self.assertEqual(diff, math.sqrt(abs(x - y)))
            self.assertEqual((x, y, diff), expected[_])

    def test_case_3(self):
        pairs_count = 25
        pairs = f_689(pairs_count=pairs_count, random_seed=14)
        self.assertIsInstance(pairs, type((x for x in range(1))))
        expected = [
            (14, 79, 8.06225774829855),
            (90, 97, 2.6457513110645907),
            (84, 68, 4.0),
            (32, 35, 1.7320508075688772),
            (95, 33, 7.874007874011811),
            (38, 94, 7.483314773547883),
            (10, 85, 8.660254037844387),
            (58, 39, 4.358898943540674),
            (60, 88, 5.291502622129181),
            (51, 51, 0.0),
            (100, 16, 9.16515138991168),
            (34, 29, 2.23606797749979),
            (41, 46, 2.23606797749979),
            (34, 47, 3.605551275463989),
            (81, 81, 0.0),
            (67, 20, 6.855654600401044),
            (21, 71, 7.0710678118654755),
            (86, 85, 1.0),
            (36, 22, 3.7416573867739413),
            (2, 84, 9.055385138137417),
            (9, 16, 2.6457513110645907),
            (77, 44, 5.744562646538029),
            (4, 11, 2.6457513110645907),
            (36, 27, 3.0),
            (49, 52, 1.7320508075688772)
        ]
        for _ in range(pairs_count):
            x, y, diff = next(pairs)
            self.assertEqual(diff, math.sqrt(abs(x - y)))
            self.assertEqual((x, y, diff), expected[_])

    def test_case_4(self):
        pairs = f_689(pairs_count=0)
        self.assertIsInstance(pairs, type((x for x in range(1))))
        self.assertEqual(sum(1 for _ in pairs), 0)


if __name__ == "__main__":
    run_tests()