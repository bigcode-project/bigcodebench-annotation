import numpy as np
import matplotlib.pyplot as plt
import cmath

def f_446(x, y):
    """
    Draw the phase of a complex function over a range of x and y and return the matplotlib axes object
    along with the 2D array of calculated phase values.

    Parameters:
    x (numpy.ndarray): The range of x values.
    y (numpy.ndarray): The range of y values.

    Returns:
    tuple: containing
        - matplotlib.axes.Axes: The axes object with the phase plot.
        - numpy.ndarray: The 2D array of calculated phase values.
    
    Raises:
    TypeError: If either `x` or `y` is not a numpy.ndarray.
    ValueError: If `x` and `y` do not have the same length.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    - cmath

    Examples:
    >>> ax, Z = f_446(np.array([1, 2, 3]), np.array([1, 2, 3]))
    >>> isinstance(ax, plt.Axes), isinstance(Z, np.ndarray)
    (True, True)
    >>> ax, Z = f_446(np.array([0]), np.array([0]))  # Test with single point
    >>> isinstance(ax, plt.Axes), isinstance(Z, np.ndarray)
    (True, True)
    """
    # Type check for x and y
    if not isinstance(x, np.ndarray) or not isinstance(y, np.ndarray):
        raise TypeError("x and y must be numpy.ndarray")

    # Handle empty arrays
    if x.size == 0 or y.size == 0:
        print("Empty x or y array provided.")
        return None, np.array([])  # Adjusted to return a tuple

    # Check for mismatched array sizes
    if len(x) != len(y):
        raise ValueError("Mismatched array sizes: x and y must have the same length")

    Z = np.zeros((len(y), len(x)), dtype=float)
    for i in range(len(y)):
        for j in range(len(x)):
            z = complex(x[j], y[i])
            Z[i, j] = cmath.phase(z**2 - 1)

    fig, ax = plt.subplots()
    c = ax.imshow(Z, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)), origin='lower', cmap='hsv')
    fig.colorbar(c, ax=ax, label="Phase (radians)")
    ax.grid()

    return ax, Z

import unittest
import numpy as np
import matplotlib.pyplot as plt
import cmath
class TestCases(unittest.TestCase):
    def test_input_types(self):
        """Test the function with non-numpy array inputs."""
        with self.assertRaises(TypeError):
            f_446([1, 2, 3], np.array([1, 2, 3]))
    def test_empty_arrays(self):
        """Test function with empty numpy arrays."""
        _, Z = f_446(np.array([]), np.array([]))
        self.assertEqual(Z.size, 0)
    def test_single_point(self):
        """Test the function with single-point arrays."""
        ax, Z = f_446(np.array([0]), np.array([0]))
        self.assertIsInstance(ax, plt.Axes)
        self.assertIsInstance(Z, np.ndarray)
    def test_phase_calculation(self):
        """Test phase calculation for known values."""
        x = np.array([1, -1])
        y = np.array([0, 0])
        _, Z = f_446(x, y)
        expected_phases = np.array([cmath.phase((1 + 0j)**2 - 1), cmath.phase((-1 + 0j)**2 - 1)])
        np.testing.assert_array_almost_equal(Z[0], expected_phases)
    def test_mismatched_array_sizes(self):
        """Test function with arrays of different lengths."""
        with self.assertRaises(ValueError):
            f_446(np.array([0]), np.array([0, 1]))
