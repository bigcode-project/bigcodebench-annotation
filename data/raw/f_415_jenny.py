import json
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict


def f_415(input_file: str) -> plt.Axes:
    """
    Read a list of dictionaries from a JSON file, calculate the results (mean and median for each key)
    via numpy, convert the input data into a pandas DataFrame with the keys as "X" and values as "Y"
    for visualization with a seaborn box plot, then return the results and box plot.

    Parameters:
    - input_file (str): The input JSON file name with absolute path.

    Returns:
    - results (dict): Dictionary where each key is a unique key from the original input, and each
                      value is a corresponding dict, with keys 'mean' and 'median' and the statistics
                      as values.
    - ax (plt.Axes): The box plot of aggregated 'Values for Each Key' in the input data.

    Requirements:
    - json
    - seaborn
    - matplotlib.pyplot
    - pandas
    - numpy
    - collections.defaultdict

    Example:
    >>> results, ax = f_415("/path/to/data.json")
    >>> ax
    <class 'matplotlib.axes._axes.Axes'>
    >>> results
    {'a': {'mean': 3.0, 'median': 3.0}, 'b': {'mean': 2.0, 'median': 3.0}}
    """
    with open(input_file, "r") as f:
        data = json.load(f)

    stats = defaultdict(list)
    for d in data:
        for key, value in d.items():
            stats[key].append(value)

    results = {
        k: {"mean": np.mean(v), "median": np.median(v)} for k, v in stats.items()
    }

    data = pd.DataFrame(data).melt(var_name="X", value_name="Y")
    ax = sns.boxplot(data=data, x="X", y="Y")
    ax.set_title("Boxplot of Values for Each Key")
    return results, ax


import unittest
import os
import tempfile
import matplotlib.pyplot as plt
import json


class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup a temporary directory and write sample JSON data to a temp file
        self.temp_dir = tempfile.TemporaryDirectory()
        self.sample_data_file = os.path.join(self.temp_dir.name, "sample_data.json")
        self.sample_data = [
            {"A": 10, "B": 20, "C": 30},
            {"A": 15, "B": 25, "C": 35},
            {"A": 20, "B": 30, "C": 40},
        ]
        with open(self.sample_data_file, "w") as f:
            json.dump(self.sample_data, f)

        # Create an invalid JSON file for testing
        self.invalid_json_file = os.path.join(self.temp_dir.name, "invalid.json")
        with open(self.invalid_json_file, "w") as f:
            f.write("invalid content")

    def tearDown(self):
        self.temp_dir.cleanup()
        plt.close("all")

    def test_case_1(self):
        # Test if the function can read the JSON data file and return a plot
        _, ax = f_415(self.sample_data_file)
        self.assertIsInstance(ax, plt.Axes, "The function should return a plot (Axes).")
        self.assertTrue(len(ax.get_xticks()) > 0, "The plot should have x-axis ticks.")
        self.assertTrue(len(ax.get_yticks()) > 0, "The plot should have y-axis ticks.")
        self.assertTrue(ax.get_title(), "Boxplot of Values for Each Key")

    def test_case_2(self):
        # Check result correctness
        results, _ = f_415(self.sample_data_file)
        self.assertIn("A", results)
        self.assertIn("B", results)
        self.assertIn("C", results)
        self.assertEqual(results["A"]["mean"], 15.0)
        self.assertEqual(results["A"]["median"], 15.0)
        self.assertEqual(results["B"]["mean"], 25.0)
        self.assertEqual(results["B"]["median"], 25.0)
        self.assertEqual(results["C"]["mean"], 35.0)
        self.assertEqual(results["C"]["median"], 35.0)

    def test_case_3(self):
        # Test the correctness of the x-axis labels
        _, ax = f_415(self.sample_data_file)
        x_labels = [label.get_text() for label in ax.get_xticklabels()]
        expected_x_labels = ["A", "B", "C"]
        self.assertListEqual(
            x_labels, expected_x_labels, "The x-axis labels are not as expected."
        )

    def test_case_4(self):
        # Test the correctness of the y-axis data points
        _, ax = f_415(self.sample_data_file)
        # Correctly extract the height of the boxes in the box plot
        boxes = [
            box.get_height() for box in ax.containers if hasattr(box, "get_height")
        ]
        self.assertTrue(
            all(height > 0 for height in boxes),
            "Each box plot should have y-data points.",
        )

    def test_case_5(self):
        # Test if the function raises an error for non-existent file
        with self.assertRaises(FileNotFoundError):
            f_415(os.path.join(self.temp_dir.name, "non_existent.json"))

    def test_case_6(self):
        # Test if the function raises an error for invalid JSON format
        with self.assertRaises(json.JSONDecodeError):
            f_415(os.path.join(self.temp_dir.name, "invalid.json"))


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
