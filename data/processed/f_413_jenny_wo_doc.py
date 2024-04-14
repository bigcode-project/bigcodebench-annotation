import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt


def f_413(input_file):
    """
    Reads a JSON file containing a list of dictionaries. For each key across all dictionaries,
    calculates the mean and median of its values using numpy. Visualizes the mean and median
    using bar charts. Returns the results and plots.

    Parameters:
        - input_file (str): Path to the input JSON file containing a list of dictionaries.

    Returns:
        - result (dict): each key corresponds to those in the input dictionaries, and the corresponding
          value is another dict with keys 'mean' and 'median', representing the calculated statistics.
        - plots  (list[matplotlib.axes._subplots.AxesSubplot]): A list of bar charts, one for
          each key in the dictionaries, visualizing the mean and median values.

    Requirements:
        - json
        - numpy
        - collections.defaultdict
        - matplotlib.pyplot

    Example:
    >>> results, plots = f_413("sample_data.json")
    >>> type(plots[0])
    <class 'matplotlib.axes._subplots.Axes'>
    >>> results
    {'a': {'mean': 3.0, 'median': 3.0}, 'b': {'mean': 6.0, 'median': 6.0}}
    """
    with open(input_file, "r") as f:
        data = json.load(f)

    stats = defaultdict(list)
    for d in data:
        for key, value in d.items():
            stats[key].append(value)

    result = {k: {"mean": np.mean(v), "median": np.median(v)} for k, v in stats.items()}

    plots = []
    for key, values in result.items():
        _, ax = plt.subplots()
        ax.bar(["mean", "median"], [values["mean"], values["median"]])
        ax.set_title(f"Statistics of {key}")
        plots.append(ax)
    return result, plots

import matplotlib
import unittest
import tempfile
import os
class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.test_data = {
            "test_1.json": [{"a": 2, "b": 4}, {"a": 4, "b": 8}],
            "test_2.json": [{"x": 1}, {"y": 2}, {"z": 6}],
            "invalid.json": {"not": "valid"},
            "empty.json": [],
        }
        # Generate test files
        for filename, content in cls.test_data.items():
            with open(os.path.join(cls.temp_dir.name, filename), "w") as f:
                json.dump(content, f)
    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()
        plt.close("all")
    def test_case_1(self):
        # Check plot generation
        expected_titles = ["a", "b"]
        _, plots = f_413(os.path.join(self.temp_dir.name, "test_1.json"))
        self.assertEqual(len(plots), len(expected_titles))
        for plot, title in zip(plots, expected_titles):
            assert isinstance(plot, matplotlib.axes._axes.Axes)
            self.assertTrue(plot.get_title(), f"Statistics of {title}")
    def test_case_2(self):
        # Check result correctness
        results, _ = f_413(os.path.join(self.temp_dir.name, "test_1.json"))
        self.assertIn("a", results)
        self.assertIn("b", results)
        self.assertEqual(results["a"]["mean"], 3.0)
        self.assertEqual(results["a"]["median"], 3.0)
        self.assertEqual(results["b"]["mean"], 6.0)
        self.assertEqual(results["b"]["median"], 6.0)
    def test_case_3(self):
        # Test with invalid data structure (not a list of dicts)
        with self.assertRaises(AttributeError):
            f_413(os.path.join(self.temp_dir.name, "invalid.json"))
    def test_case_4(self):
        # Test with empty data
        results, plots = f_413(os.path.join(self.temp_dir.name, "empty.json"))
        self.assertEqual(results, {})
        self.assertEqual(len(plots), 0)
    def test_case_5(self):
        # Test handling nested dicts with one key each
        results, _ = f_413(os.path.join(self.temp_dir.name, "test_2.json"))
        self.assertIn("x", results)
        self.assertIn("y", results)
        self.assertIn("z", results)
        self.assertEqual(results["x"]["mean"], 1.0)
        self.assertEqual(results["x"]["median"], 1.0)
        self.assertEqual(results["y"]["mean"], 2.0)
        self.assertEqual(results["y"]["median"], 2.0)
        self.assertEqual(results["z"]["mean"], 6.0)
        self.assertEqual(results["z"]["median"], 6.0)
    def test_case_6(self):
        # Test with nonexistent filename
        with self.assertRaises(FileNotFoundError):
            f_413(os.path.join(self.temp_dir.name, "NOTEXISTS.json"))
