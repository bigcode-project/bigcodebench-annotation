import json
import pandas as pd
import numpy as np
from collections import defaultdict


def f_389(input_file="data.json"):
    """
    Read a list of dictionaries from a JSON file, calculate the mean and median for each key
    (ignoring non-numeric or missing values), and convert the results into a Pandas DataFrame.

    Parameters:
    - input_file (str, optional): The input JSON file name. Defaults to 'data.json'.
                                  The file should contain a list of dictionaries. If a key is
                                  missing in a dictionary, it is treated as NaN for that record.
                                  Non-numeric values are ignored for the calculation of mean
                                  and median. If all values for a key are non-numeric or missing,
                                  the statistics for that key will be NaN.

    Returns:
    - df (pd.DataFrame): A DataFrame indexed and sorted by the variable names (keys) from the
                         input data, containing columns 'mean' and 'median'.

    Requirements:
    - numpy
    - collections
    - json
    - pandas

    Example:
    >>> df = f_389('data_1.json')
    a        mean  median
    b        mean  median
    c        mean  median
    """
    with open(input_file, "r") as f:
        data = json.load(f)
    all_keys = set().union(*(d.keys() for d in data))
    stats = defaultdict(list)
    for d in data:
        for key in all_keys:
            value = d.get(key, np.nan)
            if isinstance(value, (int, float)):
                stats[key].append(value)
            else:
                stats[key].append(np.nan)
    result = {
        k: {"mean": np.nanmean(v), "median": np.nanmedian(v)} for k, v in stats.items()
    }
    df = pd.DataFrame(result).transpose().sort_index()
    return df

import unittest
import numpy as np
import tempfile
import json
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_data_paths = []
        test_data = [
            [{"a": 2, "b": 3, "c": 4}],  # Test data for test_case_1
            [{"a": 1}],  # Test data for test_case_2
            [{"a": 1.5}, {"b": None}],  # Test data for test_case_3
            [],  # Test data for test_case_4
            [{"a": 1.5, "c": 4}, {"b": None}],  # Test data for test_case_5
        ]
        for idx, data in enumerate(test_data, start=1):
            path = self.temp_dir.name + f"/test_data_{idx}.json"
            with open(path, "w") as f:
                json.dump(data, f)
            self.test_data_paths.append(path)
    def test_case_1(self):
        # Basic test
        df = f_389(self.test_data_paths[0])
        self.assertListEqual(df.index.tolist(), ["a", "b", "c"])
        self.assertAlmostEqual(df.loc["a", "mean"], 2.0)
        self.assertAlmostEqual(df.loc["a", "median"], 2.0)
    def test_case_2(self):
        # Test with a single key
        df = f_389(self.test_data_paths[1])
        self.assertListEqual(df.index.tolist(), ["a"])
        self.assertAlmostEqual(df.loc["a", "mean"], 1.0)
        self.assertAlmostEqual(df.loc["a", "median"], 1.0)
    def test_case_3(self):
        # Test with missing values to ensure handling of NaN
        df = f_389(self.test_data_paths[2])
        self.assertListEqual(df.index.tolist(), ["a", "b"])
        self.assertAlmostEqual(df.loc["a", "mean"], 1.5)
        self.assertAlmostEqual(df.loc["a", "median"], 1.5)
        self.assertTrue(np.isnan(df.loc["b", "mean"]))
        self.assertTrue(np.isnan(df.loc["b", "median"]))
    def test_case_4(self):
        # Test empty dataframe creation from an empty input file
        df = f_389(self.test_data_paths[3])
        self.assertEqual(df.shape[0], 0)
    def test_case_5(self):
        # Test handling of mixed data, including valid values and NaN
        df = f_389(self.test_data_paths[4])
        self.assertListEqual(df.index.tolist(), ["a", "b", "c"])
        self.assertAlmostEqual(df.loc["a", "mean"], 1.5)
        self.assertAlmostEqual(df.loc["a", "median"], 1.5)
        self.assertTrue(np.isnan(df.loc["b", "mean"]))
        self.assertTrue(np.isnan(df.loc["b", "median"]))
        self.assertAlmostEqual(df.loc["c", "mean"], 4.0)
        self.assertAlmostEqual(df.loc["c", "median"], 4.0)
    def test_case_6(self):
        # Test with mixed types in values
        data = [{"a": 5, "b": "text", "c": 7}, {"a": "more text", "b": 4, "c": None}]
        path = self.temp_dir.name + "/test_data_6.json"
        with open(path, "w") as f:
            json.dump(data, f)
        df = f_389(path)
        self.assertListEqual(df.index.tolist(), ["a", "b", "c"])
        self.assertAlmostEqual(df.loc["a", "mean"], 5.0)
        self.assertAlmostEqual(df.loc["c", "mean"], 7.0)
        self.assertAlmostEqual(df.loc["b", "mean"], 4.0)
    def test_case_7(self):
        # Test a larger dataset with missing values
        data = [{"a": i, "b": i * 2 if i % 2 == 0 else None} for i in range(1, 101)]
        path = self.temp_dir.name + "/test_data_7.json"
        with open(path, "w") as f:
            json.dump(data, f)
        df = f_389(path)
        self.assertAlmostEqual(df.loc["a", "mean"], 50.5)
        self.assertAlmostEqual(
            df.loc["b", "mean"], np.mean([2 * i for i in range(2, 101, 2)])
        )
    def test_case_8(self):
        # Test with all non-numeric values for a key
        data = [
            {"a": "text", "b": "more text"},
            {"a": "even more text", "b": "still more text"},
        ]
        path = self.temp_dir.name + "/test_data_8.json"
        with open(path, "w") as f:
            json.dump(data, f)
        df = f_389(path)
        self.assertTrue(np.isnan(df.loc["a", "mean"]))
        self.assertTrue(np.isnan(df.loc["b", "mean"]))
    def test_case_9(self):
        # Test varying numbers of missing and non-numeric values
        data = [
            {"a": 10, "b": 20, "c": "ignore"},
            {"a": None, "b": 25, "c": 30},
            {"a": 5, "b": "ignore", "c": "ignore"},
        ]
        path = self.temp_dir.name + "/test_data_9.json"
        with open(path, "w") as f:
            json.dump(data, f)
        df = f_389(path)
        self.assertAlmostEqual(df.loc["a", "mean"], 7.5)
        self.assertAlmostEqual(df.loc["b", "mean"], 22.5)
        self.assertAlmostEqual(df.loc["c", "mean"], 30.0)
    def tearDown(self):
        self.temp_dir.cleanup()
