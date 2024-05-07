import numpy as np
import matplotlib.pyplot as plt
import itertools

def f_191(n_walks, n_steps, seed=None):
    """
    Create and plot `n_walks` number of random walks, each with `n_steps` steps.

    The function checks for valid n_walks and n_steps, then generates walks via numpy.
    Each walk is plotted in a different color cycling through a predefined set of colors:
    ['b', 'g', 'r', 'c', 'm', 'y', 'k'].

    Parameters:
    - n_walks (int): The number of random walks to be generated and plotted.
    - n_steps (int): The number of steps in each random walk.
    - seed (int, optional): Seed for random number generation. Default is None.

    Returns:
    - ax (plt.Axes): A Matplotlib Axes containing the plotted random walks.

    Requirements:
    - numpy
    - matplotlib
    - itertools

    Example:
    >>> ax = f_191(5, 100, seed=42)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(-20.0, 0, '−20'), Text(0.0, 0, '0'), Text(20.0, 0, '20'), Text(40.0, 0, '40'), Text(60.0, 0, '60'), Text(80.0, 0, '80'), Text(100.0, 0, '100'), Text(120.0, 0, '120')]
    """
    if n_walks < 0 or n_steps < 0:
        raise ValueError("Walks and steps cannot be negative.")
    np.random.seed(seed)
    COLORS = ["b", "g", "r", "c", "m", "y", "k"]
    color_cycle = itertools.cycle(COLORS)
    fig, ax = plt.subplots()
    for _ in range(n_walks):
        walk = np.random.choice([-1, 1], size=n_steps)
        walk = np.cumsum(walk)
        ax.plot(walk, next(color_cycle))
    return ax

import unittest
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic setup
        ax = f_191(5, 100, seed=42)
        self.assertIsInstance(ax, plt.Axes)
    def test_case_2(self):
        # Test number of walks
        for n_walk in [0, 1, 2, 10, 50]:
            ax = f_191(n_walk, 10, seed=42)
            lines = ax.get_lines()
            self.assertEqual(len(lines), n_walk)
    def test_case_3(self):
        # Test number of steps
        for n_steps in [0, 1, 10, 100, 500]:
            ax = f_191(2, n_steps, seed=42)
            lines = ax.get_lines()
            self.assertEqual(len(lines[0].get_ydata()), n_steps)
    def test_case_4(self):
        # Test random seed
        ax1 = f_191(5, 100, seed=42)
        ax2 = f_191(5, 100, seed=42)
        ax3 = f_191(5, 100, seed=0)
        lines1 = ax1.get_lines()
        lines2 = ax2.get_lines()
        lines3 = ax3.get_lines()
        self.assertTrue(
            all(
                np.array_equal(line1.get_ydata(), line2.get_ydata())
                for line1, line2 in zip(lines1, lines2)
            )
        )
        self.assertFalse(
            all(
                np.array_equal(line1.get_ydata(), line3.get_ydata())
                for line1, line3 in zip(lines1, lines3)
            ),
            "Random walks are not reproducible using the same seed.",
        )
    def test_case_5(self):
        # Test invalid n_walks
        with self.assertRaises(ValueError):
            f_191(-1, 100, seed=42)
    def test_case_6(self):
        # Test negative n_steps
        with self.assertRaises(ValueError):
            f_191(1, -100, seed=42)
    def tearDown(self):
        plt.close("all")
