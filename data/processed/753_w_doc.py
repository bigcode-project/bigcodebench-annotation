import math
import random
import statistics

# Constants
RADIUS = 5

def task_func(n):
    """
    Generate n random points within a circle of radius RADIUS (default value is 5) and return their average distance from the center.

    Parameters:
    - n (int): The number of points to be generated.

    Returns:
    - float: The average distance from the center of the circle.

    Requirements:
    - math
    - random
    - statistics

    Example:
    >>> random.seed(42)
    >>> task_func(100)
    3.2406
    >>> task_func(50)
    3.4443
    """
    distances = []
    for _ in range(n):
        theta = 2 * math.pi * random.random()
        r = RADIUS * math.sqrt(random.random())
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        distance = math.sqrt(x**2 + y**2)
        distances.append(distance)
    return round(statistics.mean(distances), 4)

import unittest
class TestCases(unittest.TestCase):
    def test_1(self):
        avg_distance = task_func(1000)
        self.assertTrue(3.1 <= avg_distance <= 3.5, f"Expected average distance to be between 3.1 and 3.5, got {avg_distance}")
    def test_2(self):
        avg_distance = task_func(500)
        self.assertTrue(3.2 <= avg_distance <= 3.5, f"Expected average distance to be between 3.2 and 3.5, got {avg_distance}")
    def test_3(self):
        avg_distance = task_func(100)
        self.assertTrue(2.8 <= avg_distance <= 3.7, f"Expected average distance to be between 2.8 and 3.7, got {avg_distance}")
    def test_4(self):
        avg_distance = task_func(50)
        # Allowing a wider range due to higher variance with fewer points
        self.assertTrue(2.4 <= avg_distance <= 4.1, f"Expected average distance to be between 2.4 and 4.1, got {avg_distance}")
    def test_5(self):
        avg_distance = task_func(10)
        # Even wider range for very few points
        self.assertTrue(1.4 <= avg_distance <= 4.6, f"Expected average distance to be between 1.4 and 4.6, got {avg_distance}")
