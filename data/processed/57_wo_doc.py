import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(csv_file_path: str, title: str):
    """
    Create a heatmap of the correlation matrix of a DataFrame built from a CSV file. Round each correlation to 2 decimals.

    Parameters:
    csv_file_path (str): The path to the CSV file containing the input data.
    title (str): The title of the heatmap.

    Returns:
    DataFrame: correlation dataframe where each row and each column correspond to a specific column.
    matplotlib.axes.Axes: The Axes object of the plotted data.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - seaborn

    Example:
    >>> data = "data/task_func/csv_1.csv"
    >>> c, ax = task_func(data, 'Correlation Heatmap')
    """
    data = pd.read_csv(csv_file_path)
    corr = data.corr().round(2)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', cbar=True)
    plt.title(title)
    return corr, plt.gca()

import unittest
import os
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self) -> None:
        self.test_dir = "data/task_func"
        os.makedirs(self.test_dir, exist_ok=True)
        data = pd.DataFrame({'A': range(10), 'B': range(10), 'C': range(10)})
        data.to_csv(os.path.join(self.test_dir, "csv_1.csv"), index=False)
        data = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [5, 4, 3, 2, 1], 'Z': [2, 3, 4, 5, 6]})
        data.to_csv(os.path.join(self.test_dir, "csv_2.csv"), index=False)
        data = pd.DataFrame({'M': [10, 20, 30], 'N': [30, 20, 10], 'O': [15, 25, 35]})
        data.to_csv(os.path.join(self.test_dir, "csv_3.csv"), index=False)
        data = pd.DataFrame({'P': [10, 43], 'Q': [32, 19], 'R': [22, 16]})
        data.to_csv(os.path.join(self.test_dir, "csv_4.csv"), index=False)
        data = pd.DataFrame({'S': [1, 7, 3], 'T': [9, 9, 5], 'U': [5, 8, 2]})
        data.to_csv(os.path.join(self.test_dir, "csv_5.csv"), index=False)
    
    def tearDown(self) -> None:
        import shutil
        try:
            shutil.rmtree(self.test_dir)
        except:
            pass
    def test_case_1(self):
        title = 'Test Case 1'
        expected_c = pd.DataFrame(
            {
                "A" : [1.0, 1.0, 1.0],
                "B" : [1.0, 1.0, 1.0],
                "C" : [1.0, 1.0, 1.0]
            },
            index = ["A", "B", "C"]
        )
        c, ax = task_func(os.path.join(self.test_dir, "csv_1.csv"), title)
        self.assertEqual(ax.get_title(), title)
        pd.testing.assert_frame_equal(c, expected_c)
    def test_case_2(self):
        title = 'Test Case 2'
        expected_c = pd.DataFrame(
            {
                "X" : [1.0, -1.0, 1.0],
                "Y" : [-1.0, 1.0, -1.0],
                "Z" : [1.0, -1.0, 1.0]
            },
            index = ["X", "Y", "Z"]
        )
        c, ax = task_func(os.path.join(self.test_dir, "csv_2.csv"), title)
        self.assertEqual(ax.get_title(), title)
        pd.testing.assert_frame_equal(c, expected_c)
    def test_case_3(self):        
        title = 'Test Case 3'
        _, ax = task_func(os.path.join(self.test_dir, "csv_3.csv"), title)
        self.assertEqual(ax.get_title(), title)
    
    def test_case_4(self):     
        title = 'Test Case 4'
        _, ax = task_func(os.path.join(self.test_dir, "csv_4.csv"), title)
        self.assertEqual(ax.get_title(), title)
    def test_case_5(self):
        title = 'Test Case 5'
        expected_c = pd.DataFrame(
            {
                "S" : [1.0, 0.19, 0.65],
                "T" : [0.19, 1.0, 0.87],
                "U" : [0.65, 0.87, 1.0]
            },
            index = ["S", "T", "U"]
        )
        c, ax = task_func(os.path.join(self.test_dir, "csv_5.csv"), title)
        self.assertEqual(ax.get_title(), title)
        pd.testing.assert_frame_equal(c, expected_c)
