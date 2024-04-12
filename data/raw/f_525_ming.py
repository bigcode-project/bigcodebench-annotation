import unittest

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics


def f_525(sales_data):
    """
    Plot sales trends for five products over a year, highlighting variability with standard deviation shading.

    Parameters:
    - sales_data (pd.DataFrame): DataFrame with sales data, expected columns: 'Month', 'Product A' to 'Product E'.

    Returns:
    - ax (matplotlib.axes.Axes): Axes object with the sales trends plot.

    Requirements:
    - pandas for data manipulation.
    - matplotlib.pyplot for plotting.
    - numpy for numerical operations.
    - statistics for standard deviation calculation.

    Example usage:
    >>> sales_data = pd.DataFrame({
    ...     'Month': range(1, 13),
    ...     'Product A': np.random.randint(100, 200, size=12),
    ...     'Product B': np.random.randint(150, 250, size=12),
    ...     'Product C': np.random.randint(120, 220, size=12),
    ...     'Product D': np.random.randint(130, 230, size=12),
    ...     'Product E': np.random.randint(140, 240, size=12)
    ... })
    >>> ax = f_525(sales_data)
    >>> plt.show()  # Displays the plot
    """
    fig, ax = plt.subplots()
    for label in sales_data.columns[1:]:  # Skipping 'Month' column
        monthly_sales = sales_data[label]
        std_dev = statistics.stdev(monthly_sales)

        ax.plot(sales_data['Month'], monthly_sales, label=label)
        ax.fill_between(sales_data['Month'],
                        monthly_sales - std_dev,
                        monthly_sales + std_dev,
                        alpha=0.2)

    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.set_title('Monthly Sales Trends with Standard Deviation')
    ax.legend()

    # Set x-ticks to be explicit months from the DataFrame
    ax.set_xticks(sales_data['Month'])

    return ax


class TestF525(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Generating a sample sales DataFrame
        cls.sales_data = pd.DataFrame({
            'Month': range(1, 13),
            'Product A': np.random.randint(100, 200, size=12),
            'Product B': np.random.randint(150, 250, size=12),
            'Product C': np.random.randint(120, 220, size=12),
            'Product D': np.random.randint(130, 230, size=12),
            'Product E': np.random.randint(140, 240, size=12)
        })

    def test_plot_labels(self):
        """Ensure all product labels are present in the plot legend."""
        ax = f_525(self.sales_data)
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertEqual(set(legend_labels), set(self.sales_data.columns[1:]),
                         "Not all product labels are present in the plot legend.")

    def test_plot_lines(self):
        """Check if the plot contains lines for each product."""
        ax = f_525(self.sales_data)
        self.assertEqual(len(ax.lines), len(self.sales_data.columns) - 1,
                         "Plot does not contain the correct number of lines.")

    def test_monthly_ticks(self):
        """Verify that all months are correctly plotted as x-ticks."""
        ax = f_525(self.sales_data)
        # Convert x-ticks to integers for comparison
        x_ticks = [int(tick) for tick in ax.get_xticks() if tick.is_integer()]
        expected_ticks = self.sales_data['Month'].tolist()
        self.assertListEqual(x_ticks, expected_ticks, "Not all months are correctly plotted as x-ticks.")

    def test_positive_sales(self):
        """Ensure all plotted sales values are positive."""
        ax = f_525(self.sales_data)
        for line in ax.lines:
            self.assertTrue(all(y >= 0 for y in line.get_ydata()),
                            "Plotted sales values should be positive.")

    def test_std_dev_shading(self):
        """Check for standard deviation shading around each product line."""
        ax = f_525(self.sales_data)
        self.assertGreaterEqual(len(ax.collections), len(self.sales_data.columns) - 1,
                                "Missing standard deviation shading for one or more products.")


if __name__ == "__main__":
    unittest.main()