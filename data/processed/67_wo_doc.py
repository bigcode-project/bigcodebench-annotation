import pandas as pd
import re
import os

def task_func(dir_path: str, pattern: str = '^EMP'):
    """
    Look for all ascendingly sorted files in a directory that start with a given pattern, and return the number of files against their size. You should return a pandas DataFrame with 2 columns 'File' and 'Size' with correspond to the file name and the size respectively.

    Parameters:
    - dir_path (str): The path to the directory.
    - pattern (str): The pattern to match. Default is '^EMP' (files starting with 'EMP').

    Returns:
    - pandas.DataFrame: A pandas DataFrame with file names and their sizes.

    Requirements:
    - pandas
    - re
    - os

    Example:
    >>> report = task_func('/path/to/directory')
    >>> print(report)
    """
    file_sizes = []
    for file in sorted(os.listdir(dir_path)):
        if re.match(pattern, file):
            file_sizes.append((file, os.path.getsize(os.path.join(dir_path, file))))
    df = pd.DataFrame(file_sizes, columns=['File', 'Size'])
    return df

import unittest
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        self.test_dir = "data/task_func"
        os.makedirs(self.test_dir, exist_ok=True)
        self.f_1 = os.path.join(self.test_dir, "EMP001.doc")
        self.f_2 = os.path.join(self.test_dir, "EMP002.doc")
        self.f_3 = os.path.join(self.test_dir, "EMP003.doc")
        self.f_4 = os.path.join(self.test_dir, "NOTEMP1.txt")
        self.f_5 = os.path.join(self.test_dir, "NOTEMP2.txt")
        self.f_6 = os.path.join(self.test_dir, "A1.txt")
        self.f_7 = os.path.join(self.test_dir, "A2.txt")
        self.f_8 = os.path.join(self.test_dir, "A3.txt")
        self.f_9 = os.path.join(self.test_dir, "B1.py")
        self.f_10 = os.path.join(self.test_dir, "B2.py")
        for i, element in enumerate([self.f_1, self.f_2, self.f_3, self.f_4, self.f_5, self.f_6, self.f_7, self.f_8, self.f_9, self.f_10]) :
            with open(element, "w") as f :
                f.write(f"Test content {i+1}")
    def tearDown(self):
        for filename in [
            self.f_1, self.f_2, self.f_3, self.f_4, self.f_5,
            self.f_6, self.f_7, self.f_8, self.f_9, self.f_10
        ]:
            os.remove(filename)
        os.rmdir(self.test_dir)
    def test_case_1(self):
        report = task_func(self.test_dir)
        self.assertEqual(len(report), 3)
        for i, row in report.iterrows():
            self.assertEqual(row['Size'], os.path.getsize(os.path.join(self.test_dir, f"EMP00{i+1}.doc")))
    def test_case_2(self):
        report = task_func(self.test_dir, pattern="^NOTEMP")
        self.assertEqual(len(report), 2)
        for i, row in report.iterrows():
            self.assertEqual(row['Size'], os.path.getsize(os.path.join(self.test_dir, f"NOTEMP{i+1}.txt")))
    def test_case_3(self):
        report = task_func(self.test_dir, pattern="NOTFOUND")
        expected_df = pd.DataFrame(
            {
                "File" : [],
                "Size" : []
            }
        ).astype({"File" : "object", "Size" : "object"})
        self.assertTrue(
            report.empty
        )
        self.assertTrue(report.shape == expected_df.shape)
    def test_case_4(self):
        report = task_func(self.test_dir, pattern="^A")
        self.assertEqual(len(report), 3)
        for i, row in report.iterrows():
            self.assertEqual(row['Size'], os.path.getsize(os.path.join(self.test_dir, f"A{i+1}.txt")))
    def test_case_5(self):
        report = task_func(self.test_dir, pattern="^B")
        self.assertEqual(len(report), 2)
        for i, row in report.iterrows():
            self.assertEqual(row['Size'], os.path.getsize(os.path.join(self.test_dir, f"B{i+1}.py")))
