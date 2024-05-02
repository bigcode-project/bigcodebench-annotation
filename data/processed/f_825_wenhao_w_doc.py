import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def f_302(df, column, bins=30, density=True, alpha=0.6, color="g", seed=None):
    """
    Plots a histogram for a specified column of a pandas DataFrame and overlays
    it with a fitted normal distribution curve.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame.
    - column (str): The column name for which the histogram is plotted.
    - bins (int, optional): Number of bins for the histogram. Defaults to 30.
    - density (bool, optional): If True, the histogram is normalized to form a
                                probability density. Defaults to True.
    - alpha (float, optional): Transparency level for the histogram bars.
                               Defaults to 0.6.
    - color (str, optional): Color of the histogram bars. Defaults to 'g'.
    - seed (int, optional): Seed for the random number generator.
                            Defaults to None (not set).

    Returns:
    - matplotlib.axes._axes.Axes: The matplotlib Axes object with the plot.

    Requirements:
    - numpy
    - matplotlib
    - scipy

    Example:
    >>> np.random.seed(0)
    >>> df = pd.DataFrame({'A': np.random.normal(0, 1, 1000)})
    >>> ax = f_302(df, 'A')
    >>> ax.get_title()
    "Normal Fit for 'A'"
    """
    if seed is not None:
        np.random.seed(seed)

    data = df[column]
    mu, std = norm.fit(data)

    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, density=density, alpha=alpha, color=color)

    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    ax.plot(x, p, "k", linewidth=2)

    title = f"Normal Fit for '{column}'"
    ax.set_title(title)
    ax.set_ylabel("Density")
    ax.set_xlabel(column)

    return ax

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
class TestCases(unittest.TestCase):
    @classmethod
    def setUp(self):
        np.random.seed(42)
    def test_data_correctness(self):
        """Tests if the normal distribution parameters accurately represent the data's distribution."""
        mean, std_dev = 0, 1
        df = pd.DataFrame({"F": np.random.normal(mean, std_dev, 5000)})
        ax = f_302(df, "F")
        line = ax.lines[
            0
        ]  # Assu the normal distribution line is the first line object in the plot
        x_data = line.get_xdata()
        y_data = line.get_ydata()
        # The peak of the normal distribution curve should be at the mean
        estimated_mean = x_data[np.argmax(y_data)]
        self.assertAlmostEqual(
            estimated_mean,
            mean,
            places=1,
            msg="The calculated mean does not match the expected mean.",
        )
    def test_bins_parameter(self):
        """Verifies that changing the number of bins affects the plot."""
        df = pd.DataFrame({"B": np.random.normal(0, 1, 100)})
        ax_default_bins = f_302(df, "B")
        ax_more_bins = f_302(df, "B", bins=50)
        self.assertNotEqual(
            ax_default_bins.patches,
            ax_more_bins.patches,
            "Different 'bins' parameters should result in different histograms.",
        )
    def test_alpha_parameter(self):
        """Checks if the alpha parameter correctly sets the transparency."""
        df = pd.DataFrame({"C": np.random.normal(0, 1, 100)})
        ax = f_302(df, "C", alpha=0.1)
        self.assertLess(
            ax.patches[0].get_alpha(),
            0.5,
            "The alpha parameter should control the transparency of histogram bars.",
        )
    def test_density_parameter(self):
        """Ensures the density parameter properly normalizes the histogram."""
        df = pd.DataFrame({"D": np.random.normal(0, 1, 100)})
        ax = f_302(df, "D", density=False)
        total_bar_area = sum((p.get_width() * p.get_height() for p in ax.patches))
        self.assertNotEqual(
            total_bar_area,
            1,
            "With 'density=False', the histogram should not be normalized to form a probability density.",
        )
    def test_color_parameter(self):
        """Validates that the histogram bars use the specified color."""
        df = pd.DataFrame({"E": np.random.normal(0, 1, 100)})
        ax = f_302(
            df, "E", color="blue", alpha=0.6
        )  # Match alpha value with the function's default or specified value
        for patch in ax.patches:
            self.assertEqual(
                patch.get_facecolor(),
                colors.to_rgba("blue", alpha=0.6),
                "The bars should match the specified color.",
            )
    def tearDown(self):
        plt.close("all")
