from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def f_386(start_time, end_time, step, amplitude, period, seed=0):
    """
    Generate a time series with a given seasonality from the start time to the end time
    with a given step, and plot the time series with the seasonality.

    Parameters:
    - start_time (int): The start epoch time in milliseconds.
    = end_time (int): The end epoch time in milliseconds.
    - step (int): The step in milliseconds between each data point. Must be at least 1.
    - amplitude (float): The amplitude of the seasonality.
    - period (int): The period of the seasonality in milliseconds. Must be at least 0.
    - seed (int): Random seed for reproducibility. Defaults to 0.

    Returns:
    plt.Axes: A plot of the generated 'Time Series with Seasonality',
              with 'Timestamp' on x-axis and 'Value' on y-axis.

    Requirements:
    - datetime.datetime
    - pandas
    - numpy

    Example:
    >>> ax = f_386(0, 10000, 100, 1, 1000)
    >>> type(ax)
    <matplotlib.axes._axes.Axes>
    >>> ax.get_xticklabels()
    [Text(-20.0, 0, '1970-01-01 01:00:08.000000'), ... ]
    """
    np.random.seed(seed)

    if period <= 0 or step < 1:
        raise ValueError("Invalid input values")

    COLUMNS = ["Timestamp", "Value"]

    timestamps = np.arange(start_time, end_time, step)
    df = pd.DataFrame(columns=COLUMNS)

    if amplitude == 0:
        values = [0] * len(timestamps)
    else:
        values = np.random.normal(size=len(timestamps))

    data = []
    for i, ts in enumerate(timestamps):
        dt = datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d %H:%M:%S.%f")
        value = values[i] + amplitude * np.sin(2 * np.pi * ts / period)
        data.append([dt, value])

    df = pd.DataFrame(data, columns=COLUMNS)

    ax = df.plot(x="Timestamp", y="Value", title="Time Series with Seasonality")
    ax.set_ylabel("Value")
    return ax


import unittest
import matplotlib.pyplot as plt


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic properties
        test_cases = [
            (0, 10000, 100, 1, 1000),
            (0, 100000, 1000, 2, 5000),
            (0, 10000, 100, 0.5, 1000),
            (0, 10000, 100, 1, 500),
            (0, 10000, 500, 1, 1000),
        ]
        for start_time, end_time, step, amplitude, period in test_cases:
            with self.subTest(
                start_time=start_time,
                end_time=end_time,
                step=step,
                amplitude=amplitude,
                period=period,
            ):
                ax = f_386(start_time, end_time, step, amplitude, period)
                self.assertIsInstance(ax, plt.Axes)
                self.assertEqual(ax.get_title(), "Time Series with Seasonality")
                self.assertEqual(ax.get_xlabel(), "Timestamp")
                self.assertEqual(ax.get_ylabel(), "Value")

    def test_case_2(self):
        # Test large step
        # Plot should still behave as expected even when step > (end_time - start_time)
        ax = f_386(0, 10000, 200000, 1, 1000)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_title(), "Time Series with Seasonality")
        self.assertEqual(ax.get_xlabel(), "Timestamp")
        self.assertEqual(ax.get_ylabel(), "Value")

    def test_case_3(self):
        # Test handling invalid input types - period
        with self.assertRaises(ValueError):
            f_386(0, 10000, 100, 1, 0)
        with self.assertRaises(ValueError):
            f_386(0, 10000, 100, 1, -1)

    def test_case_4(self):
        # Test handling invalid input types - step
        with self.assertRaises(ValueError):
            f_386(0, 10000, -100, 1, 1000)
        with self.assertRaises(ValueError):
            f_386(0, 10000, 0, 1, 1000)

    def test_case_5(self):
        # Test plot data integrity
        ax = f_386(0, 10000, 100, 1, 1000)
        xy_data = ax.get_lines()[0].get_xydata()
        expected_length = (10000 - 0) // 100
        self.assertEqual(len(xy_data), expected_length)

    def test_case_6(self):
        # Test random seed
        ax1 = f_386(0, 10000, 100, 1, 1000, seed=42)
        xy_data1 = ax1.get_lines()[0].get_xydata()

        ax2 = f_386(0, 10000, 100, 1, 1000, seed=42)
        xy_data2 = ax2.get_lines()[0].get_xydata()

        ax3 = f_386(0, 10000, 100, 1, 1000, seed=43)
        xy_data3 = ax3.get_lines()[0].get_xydata()

        self.assertTrue(
            np.array_equal(xy_data1, xy_data2),
            "Results should be the same with the same seed",
        )

        self.assertFalse(
            np.array_equal(xy_data1, xy_data3),
            "Results should be different with different seeds",
        )

    def tearDown(self):
        plt.close("all")


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    run_tests()
