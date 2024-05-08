import numpy as np
import matplotlib.pyplot as plt

def f_1784():
    """
    Generate diagrams for the sine and cosine functions over the interval [0, 2π].

    This function plots the sine and cosine functions, setting appropriate titles and axis labels.

    Returns:
        Figure: A Matplotlib Figure object containing the plots.
        ndarray: An array of Matplotlib Axes objects for the subplots, where:
                 - The first Axes object contains the sine function plot.
                 - The second Axes object contains the cosine function plot.

    The sine function plot is labeled 'Sine function', with x-axis labeled 'x' and y-axis labeled 'sin(x)'.
    The cosine function plot is labeled 'Cosine function', with x-axis labeled 'x' and y-axis labeled 'cos(x)'.

    Requirements:
        - numpy
        - matplotlib.pyplot

    Example:
        >>> fig, axs = f_1784()
        >>> plt.show()
    """
    x_values = np.linspace(0, 2 * np.pi, 400)
    fig, axs = plt.subplots(2)
    
    axs[0].plot(x_values, np.sin(x_values))
    axs[0].set_title('Sine function')
    axs[0].set_xlabel('x')
    axs[0].set_ylabel('sin(x)')
    
    axs[1].plot(x_values, np.cos(x_values))
    axs[1].set_title('Cosine function')
    axs[1].set_xlabel('x')
    axs[1].set_ylabel('cos(x)')
    
    plt.tight_layout()
    
    return fig, axs


import unittest
import numpy as np
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    def setUp(self):
        self.fig, self.axs = f_1784()

    def test_return_types(self):
        self.assertIsInstance(self.fig, plt.Figure)
        self.assertEqual(len(self.axs), 2)
        for ax in self.axs:
            self.assertIsInstance(ax, plt.Axes)

    def test_plot_titles(self):
        self.assertEqual(self.axs[0].get_title(), 'Sine function')
        self.assertEqual(self.axs[1].get_title(), 'Cosine function')

    def test_axes_labels(self):
        self.assertEqual(self.axs[0].get_xlabel(), 'x')
        self.assertEqual(self.axs[0].get_ylabel(), 'sin(x)')
        self.assertEqual(self.axs[1].get_xlabel(), 'x')
        self.assertEqual(self.axs[1].get_ylabel(), 'cos(x)')

    def test_plot_contents(self):
        sine_line = self.axs[0].lines[0]
        cosine_line = self.axs[1].lines[0]
        np.testing.assert_array_almost_equal(sine_line.get_ydata(), np.sin(sine_line.get_xdata()), decimal=5)
        np.testing.assert_array_almost_equal(cosine_line.get_ydata(), np.cos(cosine_line.get_xdata()), decimal=5)

    def test_x_values_range(self):
        for ax in self.axs:
            line = ax.lines[0]
            self.assertTrue(np.all(line.get_xdata() >= 0) and np.all(line.get_xdata() <= 2 * np.pi))

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
