import numpy as np
import matplotlib.pyplot as plt

def f_1786():
    """
    Draws the linear equation y = 2x + 1 on a 2D plot for x values ranging from -10 to 10, and marks the solution for x = 2 with a green 'o' (circle) marker.

    The plot includes:
    - A red line representing the equation y = 2x + 1, labeled as 'y=2x+1', for x in [-10, 10].
    - A green circle marker indicating the solution at x = 2, y = 5.
    - Title: 'Solution of the equation y=2x+1 at x=2'
    - X-axis labeled as 'x', with a range from -10 to 10.
    - Y-axis labeled as 'y', with a range automatically adjusted based on the equation.
    - A legend indicating labels for the equation and the solution point.

    Returns:
        matplotlib.axes.Axes: An object representing the plot with specified features and ranges.

    Requirements:
        - numpy
        - matplotlib.pyplot
    """
    X = np.linspace(-10, 10, 400)  # X range specified
    y = 2 * X + 1

    fig, ax = plt.subplots()
    ax.plot(X, y, '-r', label='y=2x+1')
    
    solution_y = 2 * 2 + 1  # y value at x = 2
    ax.plot(2, solution_y, 'go', label='Solution at x=2')
    
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim([-10, 10])  # Explicitly setting the x-axis range
    # ax.set_ylim is optional and can be set if a specific y-range is desired
    ax.legend(loc='best')
    ax.grid()

    return ax

import unittest
import matplotlib.pyplot as plt
import matplotlib

class TestCases(unittest.TestCase):
    def test_return_type(self):
        ax = f_1786()
        self.assertIsInstance(ax, plt.Axes)

    def test_line_plot(self):
        ax = f_1786()
        line = ax.lines[0]
        self.assertEqual(line.get_label(), 'y=2x+1')

    def test_solution_plot(self):
        ax = f_1786()
        # Find the solution point among line plots
        # Assuming the last added line plot is the solution point
        solution_point = ax.lines[-1]  # Get the last line plot, which should be the solution
        self.assertTrue(solution_point.get_marker() == 'o')  # Check marker shape
        color = solution_point.get_color()
        expected_green = matplotlib.colors.to_rgba('green')

        # We convert both the actual color and the expected 'green' color to RGBA format for a proper comparison
        actual_color_rgba = matplotlib.colors.to_rgba(color)
        self.assertTrue(np.allclose(actual_color_rgba, expected_green, atol=0.01), f"Actual color {actual_color_rgba} not close to expected green {expected_green}")

    def test_plot_title_and_labels(self):
        ax = f_1786()
        self.assertEqual(ax.get_title(), 'Solution of the equation y=2x+1 at x=2')
        self.assertEqual(ax.get_xlabel(), 'x')
        self.assertEqual(ax.get_ylabel(), 'y')

    def test_solution_accuracy(self):
        ax = f_1786()
        solution_point = ax.lines[-1]  # Get the last line plot, which should be the solution
        x_data, y_data = solution_point.get_data()
        self.assertAlmostEqual(x_data[0], 2)  # x coordinate of the solution
        self.assertAlmostEqual(y_data[0], 5)  # y coordinate of the solution

    def test_x_range(self):
        ax = f_1786()
        self.assertEqual(ax.get_xlim(), (-10, 10))  # Check if the x-axis range is set as expected

def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()