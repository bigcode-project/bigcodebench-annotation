import pandas as pd
import matplotlib.pyplot as plt


def f_198(data):
    """
    Combine a list of dictionaries with the same keys (fruit names) into a single pandas dataframe
    where NA/NaN values are filled with 0, then generate a line chart of sales.
    The chart should have title 'Fruit Sales over Time', x-axis 'Time', and y-axis 'Sales Quantity'.

    Parameters:
    - data (list): A list of dictionaries. Each element correspond to sales quantities at a point in time,
                   where keys are fruit names (str) and values are sales quantities (int). If values
                   are not the expected type, this function raises TypeError.

    Returns:
    - matplotlib.axes._axes.Axes: The generated plot's Axes object.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> f_198([{'apple': 10, 'banana': 15, 'cherry': 12, 'durian': 0}])
    <Axes: title={'center': 'Fruit Sales over Time'}, xlabel='Time', ylabel='Sales Quantity'>
    >>> f_198([{'apple': 10, 'banana': 15, 'cherry': 12}, {'apple': 12, 'banana': 20, 'cherry': 14}])
    <Axes: title={'center': 'Fruit Sales over Time'}, xlabel='Time', ylabel='Sales Quantity'>
    """
    df = pd.DataFrame(data)
    df.fillna(0, inplace=True)
    for fruit in df.columns:
        plt.plot(df[fruit], label=fruit)
    plt.xlabel("Time")
    plt.ylabel("Sales Quantity")
    plt.title("Fruit Sales over Time")
    plt.legend()
    return plt.gca()

import unittest
import matplotlib
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        data = [{"apple": 10}, {"banana": 15, "cherry": 12}]
        ax = f_198(data)
        # Test default plot values
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertTrue(isinstance(ax.lines[0], matplotlib.lines.Line2D))
        self.assertEqual(ax.get_title(), "Fruit Sales over Time")
        self.assertEqual(ax.get_xlabel(), "Time")
        self.assertEqual(ax.get_ylabel(), "Sales Quantity")
    def test_case_2(self):
        # Test flat input
        data = [{"apple": 11, "banana": 15, "cherry": 12, "durian": 10}]
        ax = f_198(data)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(len(ax.lines), len(data[0]))
        for i, (fruit_name, fruit_quantity) in enumerate(data[0].items()):
            self.assertEqual(ax.lines[i]._label, fruit_name)
            self.assertEqual(ax.lines[i]._y, fruit_quantity)
            self.assertIsInstance(ax.lines[i], matplotlib.lines.Line2D)
    def test_case_3(self):
        data = [
            {"apple": 15},
            {"apple": 2, "banana": 11, "cherry": 8},
        ]
        ax = f_198(data)
        # Test data correctness
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(len(ax.lines), 3)
        self.assertEqual(ax.lines[0]._label, "apple")
        self.assertEqual(ax.lines[0]._y.tolist(), [15, 2])
        self.assertEqual(ax.lines[1]._label, "banana")
        self.assertEqual(ax.lines[1]._y.tolist(), [0, 11])
        self.assertEqual(ax.lines[2]._label, "cherry")
        self.assertEqual(ax.lines[2]._y.tolist(), [0, 8])
    def test_case_4(self):
        # Test one fruit only
        data = [{"apple": 10}, {"apple": 12}, {"apple": 15}]
        ax = f_198(data)
        self.assertTrue(isinstance(ax, plt.Axes))
        self.assertEqual(len(ax.lines), 1)
        self.assertEqual(ax.lines[0]._label, "apple")
        self.assertEqual(ax.lines[0]._y.tolist(), [10, 12, 15])
    def test_case_5(self):
        # Test that function fails with unexpected data values
        with self.assertRaises(ValueError):
            f_198("")
        with self.assertRaises(ValueError):
            f_198(1)
        # Test that function fails with unexpected data types
        with self.assertRaises(TypeError):
            f_198(["apple", 10, "banana", 10])
        with self.assertRaises(TypeError):
            f_198([{"apple": "10"}, {"cherry": 10}])
    def tearDown(self):
        plt.close("all")
