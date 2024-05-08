import pandas as pd
import numpy as np


def f_331(file_path="data.csv", columns=["A", "B", "C"]):
    """
    Read a CSV file into a Pandas DataFrame, convert numeric values into floats,and draw a line chart of data in the specified columns.
    In addition, compute the cube-root of the data.
    
    Parameters:
    - file_path (str): Path to the CSV file. Default is 'data.csv'.
    - columns (list of str): List of column names from the data to plot.
                             Default is ['A', 'B', 'C'].

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame of the data in the CSV file.
        - Axes: A matplotlib Axes object showing the plotted data.
        - Series: A pandas Series containing the cube-root of the data.
        
    Requirements:
    - pandas
    - numpy

    Example:
    >>> df, ax, croot = f_331('path_to_csv.csv', ['Column1', 'Column2', 'Column3'])
    >>> df
       Column1  Column2  Column3
    0      1.0      2.0      3.0
    1      4.0      5.0      6.0
    >>> ax
    <matplotlib.axes._axes.Axes object at 0x7f24b00f4a90>
    >>> croot
    0    1.0    
    """
    df = pd.read_csv(file_path, dtype=float)
    ax = df[columns].plot()
    croot = np.cbrt(df[columns])
    return df, ax, croot

import unittest
import tempfile
import pandas as pd
import matplotlib.pyplot as plt
import os
class TestCases(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_files = {}
        # Data setups for different scenarios
        self.data_sets = {
            "int": pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}),
            "varied": pd.DataFrame(
                {
                    "IntColumn": [1, 2, 3],
                    "FloatColumn": [1.1, 2.2, 3.3],
                    "StringColumn": ["4", "5", "6"],
                }
            ),
            "varied_invalid": pd.DataFrame(
                {
                    "IntColumn": [1, 2, 3],
                    "FloatColumn": [1.1, 2.2, 3.3],
                    "StringColumn": ["a", "b", "c"],
                }
            ),
        }
        # Write data sets to temporary files
        for key, df in self.data_sets.items():
            temp_file_path = os.path.join(self.test_dir.name, f"{key}.csv")
            df.to_csv(temp_file_path, index=False, header=True)
            self.temp_files[key] = temp_file_path
    def tearDown(self):
        self.test_dir.cleanup()
        plt.close("all")
    def test_case_1(self):
        file_path = self.temp_files["int"]
        df, ax, croot = f_331(file_path=file_path, columns=["A", "B", "C"])
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(df.columns.tolist(), ["A", "B", "C"])
        self.assertTrue((df["A"].tolist() == [1, 2, 3]))
        self.assertTrue((df["B"].tolist() == [4, 5, 6]))
        self.assertTrue((df["C"].tolist() == [7, 8, 9]))
        self.assertEqual(croot.to_dict(), {'A': {0: 1.0, 1: 1.2599210498948734, 2: 1.4422495703074083}, 'B': {0: 1.5874010519681996, 1: 1.7099759466766968, 2: 1.8171205928321394}, 'C': {0: 1.9129311827723894, 1: 2.0, 2: 2.080083823051904}})
        
    def test_case_2(self):
        file_path = self.temp_files["int"]
        with self.assertRaises(KeyError):
            f_331(file_path=file_path, columns=["A", "B", "Nonexistent"])
    def test_case_3(self):
        file_path = self.temp_files["varied"]
        df, ax, croot = f_331(
            file_path=file_path, columns=["IntColumn", "FloatColumn", "StringColumn"]
        )
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(df["IntColumn"].equals(pd.Series([1.0, 2.0, 3.0])))
        self.assertTrue(df["FloatColumn"].equals(pd.Series([1.1, 2.2, 3.3])))
        self.assertTrue(df["StringColumn"].equals(pd.Series([4.0, 5.0, 6.0])))
        self.assertEqual(croot.to_dict(), {'IntColumn': {0: 1.0, 1: 1.2599210498948734, 2: 1.4422495703074083}, 'FloatColumn': {0: 1.0322801154563672, 1: 1.300591446851387, 2: 1.4888055529538275}, 'StringColumn': {0: 1.5874010519681996, 1: 1.7099759466766968, 2: 1.8171205928321394}})
        
    def test_case_4(self):
        file_path = self.temp_files["varied_invalid"]
        with self.assertRaises(Exception):
            f_331(file_path=file_path, columns=["StringColumn"])
    def test_case_5(self):
        with self.assertRaises(FileNotFoundError):
            f_331(file_path="nonexistent_file.csv")
