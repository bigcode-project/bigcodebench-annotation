import numpy as np
import matplotlib.pyplot as plt


def f_1757():
    """
    Creates and displays a diagram of a parabola represented by the equation y = x^2.
    The function plots the parabola using matplotlib, sets the title as 'y = x^2', labels the axes as 'x' and 'y',
    and enables the grid. It uses a fixed range for x values from -10 to 10 with 400 points.
    This function is used for demonstrating basic plotting capabilities and visualizing
    quadratic functions. The function does not take any parameters and does not return any value.

    Requirements:
    - numpy
    - matplotlib.pyplot

    Parameters:
    None
    
    Returns:
    None
    
    Examples:
    >>> f_1757() # This will display the plot of the parabola y = x^2
    >>> type(f_1757())
    <class 'NoneType'>
    """
    X = np.linspace(-10, 10, 400)
    Y = X**2

    plt.figure()
    plt.plot(X, Y)
    plt.title('y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

import unittest
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch, ANY

class TestCases(unittest.TestCase):
    def test_no_error(self):
        """Test that the function runs without error."""
        try:
            f_1757()
        except Exception as e:
            self.fail(f"Function f_1757 raised an exception: {e}")

    def test_plot_elements(self):
        """Test that the plot contains correct elements like title and labels."""
        with patch('matplotlib.pyplot.show'):
            f_1757()
            fig = plt.gcf()
            self.assertEqual(fig.axes[0].get_title(), 'y = x^2')
            self.assertEqual(fig.axes[0].get_xlabel(), 'x')
            self.assertEqual(fig.axes[0].get_ylabel(), 'y')

    @patch('numpy.linspace')
    @patch('matplotlib.pyplot.plot')
    def test_plot_data(self, mock_plot, mock_linspace):
        """Test if the plot contains the correct data."""
        # Set up the mock for linspace to return a specific range
        mock_linspace.return_value = np.linspace(-10, 10, 400)
        expected_X = np.linspace(-10, 10, 400)
        expected_Y = expected_X ** 2

        # Execute the function under test
        with patch('matplotlib.pyplot.show'):
            f_1757()

            # Assert the plot was called correctly, allow additional arguments like labels
            mock_plot.assert_called_with(expected_X, expected_Y, label=ANY)

    def test_grid_enabled(self):
        """Test if the grid is enabled in the plot."""
        with patch('matplotlib.pyplot.show'):
            f_1757()
            fig = plt.gcf()
            self.assertTrue(fig.axes[0].get_xgridlines()[0].get_visible())
            self.assertTrue(fig.axes[0].get_ygridlines()[0].get_visible())

    @patch('matplotlib.pyplot.show')
    def test_show_called(self, mock_show):
        """Test that plt.show() is called to display the plot."""
        f_1757()
        mock_show.assert_called_once()


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
