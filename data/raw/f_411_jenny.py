import pandas as pd
import matplotlib.pyplot as plt

def f_411(data):
    """
    Combine a list of dictionaries with the same keys into a single dictionary, turn it into a
    Pandas DataFrame and create a line plot of the data.

    Parameters:
    data (list): A list of dictionaries. The keys are labels and the values are data points.

    Returns:
    matplotlib.axes._subplots.AxesSubplot or None: Axes object of the plot showing 'Data over Time',
                                                   with 'Time' on the x-axis and 'Data Points' on the y-axis.
                                                   If data is empty, return None.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> ax = f_411([{'A': 10, 'B': 15, 'C': 12},\
                    {'A': 12, 'B': 20, 'C': 14},\
                    {'A': 15, 'B': 18, 'C': 15},\
                    {'A': 11, 'B': 17, 'C': 13}])
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_title()
    'Data over Time'
    >>> len(ax.lines)
    3
    """
    if not data:
        return None
    df = pd.DataFrame(data)
    plt.figure()
    for label in df.columns:
        plt.plot(df[label], label=label)
    plt.xlabel("Time")
    plt.ylabel("Data Points")
    plt.title("Data over Time")
    return plt.gca()


import unittest
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = [
            {"A": 10, "B": 15, "C": 12},
            {"A": 12, "B": 20, "C": 14},
            {"A": 15, "B": 18, "C": 15},
            {"A": 11, "B": 17, "C": 13},
        ]
        cls.data2 = [
            {"X": 5, "Y": 8},
            {"X": 6, "Y": 7},
            {"X": 7, "Y": 6},
            {"X": 8, "Y": 5},
        ]
        cls.data3 = [{"P": 3, "Q": 2, "R": 4, "S": 1}, {"P": 4, "Q": 3, "R": 2, "S": 3}]
        cls.data4 = [{"W": 7}, {"W": 8}, {"W": 9}, {"W": 6}]
        cls.data5 = [{"M": 1, "N": 3}, {"M": 3, "N": 1}]

    def test_case_1(self):
        # Test for correct Axes instance and labels for a typical data set
        ax = f_411(self.data1)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(ax.get_title(), "Data over Time")
        self.assertEqual(ax.get_xlabel(), "Time")
        self.assertEqual(ax.get_ylabel(), "Data Points")
        self.assertEqual(len(ax.lines), 3)

    def test_case_2(self):
        # Test for different keys across dictionaries in data list
        data = [{"A": 1, "B": 2}, {"B": 3, "C": 4}, {"A": 5, "C": 6}]
        ax = f_411(data)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertTrue(len(ax.lines) > 0)

    def test_case_3(self):
        # Test with empty data list
        self.assertIsNone(f_411([]))

    def test_case_4(self):
        # Test with data containing non-numeric values
        data = [{"A": "text", "B": "more text"}, {"A": 1, "B": 2}]
        with self.assertRaises(TypeError):
            f_411(data)

    def test_case_5(self):
        # Test with a single entry in the data list
        data = [{"A": 1, "B": 2}]
        ax = f_411(data)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
        self.assertEqual(len(ax.lines), 2)

    def test_case_6(self):
        # Test focusing on data processing correctness
        data = [
            {"A": 10, "B": 15, "C": 12},
            {"A": 12, "B": 20, "C": 14},
            {"A": 15, "B": 18, "C": 15},
            {"A": 11, "B": 17, "C": 13},
        ]
        ax = f_411(data)
        self.assertIsInstance(ax, matplotlib.axes.Axes)

        # Convert input data to DataFrame for easy comparison
        input_df = pd.DataFrame(data)

        # Iterate through each line in the plot and check against the input data
        for line in ax.lines:
            label = line.get_label()
            _, y_data = line.get_data()
            expected_y_data = input_df[label].values

            # Use numpy to compare the y_data from plot and expected data from input
            np.testing.assert_array_equal(
                y_data, expected_y_data, err_msg=f"Data mismatch for label {label}"
            )

    def tearDown(self):
        plt.close("all")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
