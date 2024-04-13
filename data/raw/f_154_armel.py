import math
import random
import matplotlib.pyplot as plt
import numpy as np

RADIUS = 1
NUM_POINTS = 1000

def f_154(num_points=NUM_POINTS, radius=RADIUS):
    """
    Estimate the value of Pi using the Monte Carlo Method and visualize the points used in the estimate.
    - Use a scatter plot for the visualization
    - The samples that fall inside the circle should be plotted in blue and labeled as 'Inside Circle'.
    - The samples that fall outside the circle should be plotted in red and labeled as 'Inside Circle'.

    Parameters:
    - num_points (int): Number of random points to generate for the estimation. Default is 1000.
    - radius (float): Radius of the circle for the estimation. Default is 1.

    Returns:
    tuple:
    - float: The estimated value of pi. The value should be between 2.5 and 3.5.
    - matplotlib.axes.Axes: Axes object with the visualization of the points. The visualization will display points 
      inside the circle in blue and points outside in red.

    Requirements:
    - math: Used for mathematical calculations.
    - random: Used for generating random points.
    - matplotlib.pyplot: Used for visualizing the generated points.
    - numpy: Not directly used in this function but can be utilized for additional enhancements.

    Example:
    >>> pi_estimate, ax = f_154(1000, 1)
    >>> print(pi_estimate)
    >>> plt.show()
    """
    import math
    import random
    import matplotlib.pyplot as plt
    
    inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(num_points):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        distance = math.sqrt(x**2 + y**2)
        if distance <= radius:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    fig, ax = plt.subplots()
    ax.scatter(x_inside, y_inside, color='b', label='Inside Circle')
    ax.scatter(x_outside, y_outside, color='r', label='Outside Circle')
    ax.set_aspect('equal', adjustable='box')
    ax.legend()

    pi_estimate = 4 * inside_circle / num_points

    return pi_estimate, ax

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_154 function."""
    def test_case_1(self):
        pi_estimate, ax = f_154(1000, 1)
        self.assertIsInstance(pi_estimate, float)
        self.assertGreaterEqual(pi_estimate, 2.5)
        self.assertLessEqual(pi_estimate, 3.5)
        self.assertIsInstance(ax, type(plt.gca()))
        
    def test_case_2(self):
        pi_estimate, ax = f_154(5000, 2)
        self.assertIsInstance(pi_estimate, float)
        self.assertGreaterEqual(pi_estimate, 2.5)
        self.assertLessEqual(pi_estimate, 3.5)
        self.assertIsInstance(ax, type(plt.gca()))
        
    def test_case_3(self):
        pi_estimate, ax = f_154(100, 0.5)
        self.assertIsInstance(pi_estimate, float)
        self.assertGreaterEqual(pi_estimate, 2.5)
        self.assertLessEqual(pi_estimate, 3.5)
        self.assertIsInstance(ax, type(plt.gca()))
        
    def test_case_4(self):
        num_points = 100
        radius = 3
        pi_estimate, ax = f_154(num_points, radius)
        self.assertIsInstance(pi_estimate, float)
        self.assertGreaterEqual(pi_estimate, 2.5)
        self.assertLessEqual(pi_estimate, 3.5)
        self.assertIsInstance(ax, type(plt.gca()))

    def test_case_5(self):
        num_points = 1000
        radius = 0.1
        pi_estimate, ax = f_154(num_points, radius)
        self.assertIsInstance(pi_estimate, float)
        self.assertGreaterEqual(pi_estimate, 2.5)
        self.assertLessEqual(pi_estimate, 3.5)
        self.assertIsInstance(ax, type(plt.gca()))

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests() 