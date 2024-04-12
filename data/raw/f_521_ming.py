import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def f_521(x, y, labels):
    """
    Scale the "x" and "y" arrays using the standard scaler of sklearn and plot them with given labels.
    Each pair of x and y arrays are scaled independently and plotted as a separate series with a label.

    Parameters:
    - x (list of np.ndarray): List of numpy arrays representing the x-values of the data points.
    - y (list of np.ndarray): List of numpy arrays representing the y-values of the data points.
    - labels (list of str): List of strings representing the labels for each data series.

    Returns:
    - matplotlib.figure.Figure: The figure object containing the plot.

    Requirements:
    - numpy for numerical operations.
    - matplotlib.pyplot for plotting.
    - sklearn.preprocessing for data scaling.

    Example:
    >>> x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
    >>> y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
    >>> labels = ['A', 'B', 'C']
    >>> fig = f_521(x, y, labels)
    >>> plt.show()
    """
    scaler = StandardScaler()

    fig, ax = plt.subplots()

    # Iterate over the datasets, scale each, and plot
    for i in range(len(x)):
        # Combine x and y values and scale them
        xy = np.vstack((x[i], y[i])).T  # Transpose to get correct shape for scaling
        xy_scaled = scaler.fit_transform(xy)  # Scale data

        # Plot scaled data
        ax.plot(xy_scaled[:, 0], xy_scaled[:, 1], label=labels[i])

    ax.legend()  # Add a legend to the plot

    return fig  # Return the figure object containing the plot


import unittest
import numpy.testing as npt


class TestF521(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.x = [np.array([1,2,3]), np.array([4,5,6])]
        self.y = [np.array([4,5,6]), np.array([7,8,9])]
        self.labels = ['Group 1', 'Group 2']

    def test_figure_type(self):
        """Test that the function returns a matplotlib figure."""
        fig = f_521(self.x, self.y, self.labels)
        self.assertTrue(str(type(fig)).endswith("matplotlib.figure.Figure'>"))

    def test_plot_labels(self):
        """Test that the correct number of labels are in the legend."""
        fig = f_521(self.x, self.y, self.labels)
        ax = fig.axes[0]
        self.assertEqual(len(ax.get_legend_handles_labels()[1]), len(self.labels))

    def test_non_empty_plot(self):
        """Test that the plot is not empty."""
        fig = f_521(self.x, self.y, self.labels)
        ax = fig.axes[0]
        self.assertTrue(len(ax.lines) > 0)

    def test_scaled_values_range(self):
        """Test that the scaled values have a mean close to 0 and a standard deviation close to 1."""
        scaler = StandardScaler()
        for xy in zip(self.x, self.y):
            xy_scaled = scaler.fit_transform(np.vstack(xy).T)
            self.assertTrue(np.allclose(np.mean(xy_scaled, axis=0), 0, atol=1e-7))
            self.assertTrue(np.allclose(np.std(xy_scaled, axis=0), 1, atol=1e-7))

    def test_input_unchanged(self):
        """Test that the original input arrays are unchanged after scaling."""
        x_original = [arr.copy() for arr in self.x]
        y_original = [arr.copy() for arr in self.y]
        f_521(self.x, self.y, self.labels)
        for orig, after in zip(x_original, self.x):
            npt.assert_array_equal(orig, after)
        for orig, after in zip(y_original, self.y):
            npt.assert_array_equal(orig, after)


if __name__ == "__main__":
    unittest.main()
