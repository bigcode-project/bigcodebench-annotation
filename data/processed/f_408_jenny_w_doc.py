import collections
import matplotlib.pyplot as plt


def f_58(data):
    """
    Combine a list of dictionaries with the same keys (fruit names) into a single dictionary,
    calculate the total turnover for each fruit, and return a bar chart's axes with colors representing
    different fruits. The colors are selected from: 'red', 'yellow', 'green', 'blue', 'purple'. The function
    ensures that sales quantity must not be negative, throwing a ValueError if encountered.

    Parameters:
    data (list): A list of dictionaries. The keys are fruit names and the values are sales quantities.
                 Sales quantity must not be negative.

    Returns:
    total_sales (dict): A dictionary containing the total sales for each fruit.
    ax (matplotlib.container.BarContainer): A bar chart of total fruit sales, or None if data is empty

    Requirements:
    - collections
    - matplotlib.pyplot

    Example:
    >>> sales, plot = f_58([{'apple': 10, 'banana': 15, 'cherry': 12},\
                             {'apple': 12, 'banana': 20, 'cherry': 14},\
                             {'apple': 15, 'banana': 18, 'cherry': 15},\
                             {'apple': 11, 'banana': 17, 'cherry': 13}])
    >>> sales
    {'apple': 48, 'banana': 70, 'cherry': 54}
    >>> type(plot)
    <class 'matplotlib.container.BarContainer'>
    """
    if not data:
        return dict(), None
    all_keys = set().union(*data)
    for d in data:
        for k, v in d.items():
            if v < 0:
                raise ValueError("Sales quantity must not be negative.")
    combined_dict = dict((k, [d.get(k, 0) for d in data]) for k in all_keys)
    total_sales = {k: sum(v) for k, v in combined_dict.items()}
    total_sales = dict(collections.OrderedDict(sorted(total_sales.items())))
    labels, values = zip(*total_sales.items())
    colors = ["red", "yellow", "green", "blue", "purple"] * (len(labels) // 5 + 1)
    ax = plt.bar(labels, values, color=colors[: len(labels)])
    plt.xlabel("Fruit")
    plt.ylabel("Total Sales")
    plt.title("Total Fruit Sales")
    return total_sales, ax

import unittest
import collections
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case with one fruit
        data = [{"apple": 5}, {"apple": 7}, {"apple": 3}]
        sales, _ = f_58(data)
        expected_sales = {"apple": 15}
        self.assertDictEqual(sales, expected_sales)
    def test_case_2(self):
        # Test basic case with multiple fruits
        data = [
            {"apple": 10, "banana": 15, "cherry": 12, "date": 10},
            {"apple": 12, "banana": 20, "cherry": 14, "date": 9},
            {"apple": 15, "banana": 18, "cherry": 15, "date": 8},
            {"apple": 11, "banana": 17, "cherry": 13, "date": 7},
        ]
        sales, _ = f_58(data)
        expected_sales = {"apple": 48, "banana": 70, "cherry": 54, "date": 34}
        self.assertDictEqual(sales, expected_sales)
    def test_case_3(self):
        # Test basic case with one entry per fruit
        data = [{"apple": 1}, {"banana": 2}, {"cherry": 3}]
        sales, _ = f_58(data)
        expected_sales = {"apple": 1, "banana": 2, "cherry": 3}
        self.assertDictEqual(sales, expected_sales)
    def test_case_4(self):
        # Test zero quantities
        data = [
            {"apple": 0, "banana": 0},
            {"apple": 0, "banana": 0},
            {"apple": 0, "banana": 0},
        ]
        sales, _ = f_58(data)
        expected_sales = {"apple": 0, "banana": 0}
        self.assertDictEqual(sales, expected_sales)
    def test_case_5(self):
        # Test empty data
        data = []
        sales, _ = f_58(data)
        expected_sales = {}
        self.assertDictEqual(sales, expected_sales)
    def test_case_6(self):
        # Test missing fruit
        data = [{"apple": 10, "banana": 5}, {"banana": 15, "cherry": 7}, {"cherry": 3}]
        sales, _ = f_58(data)
        expected_sales = {"apple": 10, "banana": 20, "cherry": 10}
        self.assertDictEqual(sales, expected_sales)
    def test_case_7(self):
        # Test negative sales
        data = [{"apple": -10, "banana": 15}, {"apple": 12, "banana": -20}]
        with self.assertRaises(ValueError):
            f_58(data)
    def test_case_8(self):
        # Test large values
        data = [
            {"apple": 1000000, "banana": 500000},
            {"apple": 2000000, "banana": 1500000},
        ]
        sales, _ = f_58(data)
        expected_sales = {"apple": 3000000, "banana": 2000000}
        self.assertDictEqual(sales, expected_sales)
    def test_case_9(self):
        # Test visualization
        data = [{"apple": 10, "banana": 15}, {"banana": 5, "apple": 10}]
        _, plot = f_58(data)
        self.assertEqual(
            len(plot.patches), 2
        )  # Checking if the number of bars in the plot is correct
    def test_case_10(self):
        # Test non-string keys
        data = [{5: 10, "banana": 15}, {"banana": 5, 5: 10}]
        with self.assertRaises(TypeError):
            f_58(data)
    def test_case_11(self):
        # Test mixed types in sales
        data = [{"apple": 10.5, "banana": 15}, {"apple": 12, "banana": 20.5}]
        sales, _ = f_58(data)
        expected_sales = {"apple": 22.5, "banana": 35.5}
        self.assertDictEqual(sales, expected_sales)
    def tearDown(self):
        plt.close("all")
