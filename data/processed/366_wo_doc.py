import subprocess
import pandas as pd

def task_func(script_path, output_file_path):
    """
    Executes a script to produce a CSV, reads the CSV, and plots a bar graph from the data.

    This function runs the provided script, which should generate a CSV file at the specified output path.
    The CSV must have exactly two columns. It then reads this CSV into a DataFrame and plots a bar graph,
    setting the first column as the x-axis labels and the second column as the bar heights.
    It will raise ValueError if the script fails to execute, or if the produced CSV is not valid.

    Parameters:
    - script_path (str): Path to the script to be executed.
    - output_file_path (str): Path where the script outputs the CSV.

    Returns:
    - df (pd.DataFrame): DataFrame containing the data from the CSV.
    - ax (matplotlib.axes._axes.Axes): Axes object of the plotted bar graph.

    Raises:
    - ValueError: If the script fails to execute, the CSV is invalid, or the CSV does not contain exactly 2 columns.
    
    Requirements:
    - pandas
    - subprocess

    Examples:
    >>> df, ax = task_func("generate_data.sh", "data.csv")
    >>> type(df)
    <class 'pandas.core.frame.DataFrame'>
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """
    try:
        subprocess.run([script_path], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise ValueError(
            "Error occurred while executing the script or script not found"
        )
    df = pd.read_csv(output_file_path)
    if len(df.columns) != 2:
        raise ValueError("CSV file must contain exactly 2 columns")
    ax = df.plot(kind="bar", x=df.columns[0], legend=False)
    ax.set_xlabel(df.columns[0])
    return df, ax

import unittest
import os
import tempfile
# import matplotlib
# Force matplotlib to not use any Xwindows backend.
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.script_path = os.path.join(self.temp_dir.name, "script.sh")
        self.output_path = os.path.join(self.temp_dir.name, "output.csv")
        self.valid_csv_content = [
            f'echo "Name,Value" > {self.output_path}\n',
            f'echo "A,1" >> {self.output_path}\n',
            f'echo "B,2" >> {self.output_path}\n',
            f'echo "C,3" >> {self.output_path}\n',
        ]
    def tearDown(self):
        self.temp_dir.cleanup()
        plt.close("all")
    def _create_script(self, lines):
        with open(self.script_path, "w") as file:
            file.write("#!/bin/bash\n")
            file.writelines(lines)
        os.chmod(self.script_path, 0o755)
    def _validate_y_tick_labels(self, ax, df):
        plt.gcf().canvas.draw()  # In older versions, need to force matplotlib to render
        y_tick_labels = [
            float(label.get_text())
            for label in ax.get_yticklabels()
            if label.get_text()
        ]
        self.assertTrue(
            all(
                y_tick_labels[i] <= y_tick_labels[i + 1]
                for i in range(len(y_tick_labels) - 1)
            ),
            "Y-tick labels are not in increasing order",
        )
        self.assertTrue(
            min(y_tick_labels) <= df[df.columns[1]].min() <= max(y_tick_labels)
            and min(y_tick_labels) <= df[df.columns[1]].max() <= max(y_tick_labels),
            "Y-tick labels do not cover the range of the data",
        )
    def test_case_1(self):
        # Test plot generation
        self._create_script(self.valid_csv_content)
        df, ax = task_func(self.script_path, self.output_path)
        expected_labels = df.iloc[:, 0].tolist()
        x_tick_labels = [tick.get_text() for tick in ax.get_xticklabels()]
        # Expected return object type
        self.assertIsInstance(ax, plt.Axes)
        # Expected number of bars
        self.assertEqual(len(ax.patches), df.shape[0])
        # x-tick labels match the first column of the DataFrame
        self.assertListEqual(x_tick_labels, expected_labels)
        self._validate_y_tick_labels(ax, df)
    def test_case_2(self):
        # Test basic csv
        expected_columns = ["Name", "Value"]
        expected_data = {"Name": ["A", "B", "C"], "Value": [1, 2, 3]}
        self._create_script(self.valid_csv_content)
        df, ax = task_func(self.script_path, self.output_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (3, 2))
        self._validate_y_tick_labels(ax, df)
        self.assertListEqual(df.columns.tolist(), expected_columns)
        for column, expected_values in expected_data.items():
            self.assertTrue(all(df[column] == expected_values))
    def test_case_3(self):
        # Test handling of script execution failure
        self._create_script(["exit 1\n"])
        with self.assertRaises(ValueError):
            task_func(self.script_path, self.output_path)
    def test_case_4(self):
        # Test handling of files with too many columns
        content = [
            f'echo "Name,Value,Extra" > {self.output_path}\n',
            f'echo "A,1,Ignore" >> {self.output_path}\n',
            f'echo "B,2,Ignore" >> {self.output_path}\n',
        ]
        self._create_script(content)
        with self.assertRaises(ValueError):
            task_func(self.script_path, self.output_path)
    def test_case_5(self):
        # Test handling of files with too few columns
        content = [
            f'echo "Name" > {self.output_path}\n',
            f'echo "A" >> {self.output_path}\n',
            f'echo "B" >> {self.output_path}\n',
        ]
        self._create_script(content)
        with self.assertRaises(ValueError):
            task_func(self.script_path, self.output_path)
    def test_case_6(self):
        # Test handling of empty file
        content = [f"> {self.output_path}\n"]
        self._create_script(content)
        with self.assertRaises(ValueError):
            task_func(self.script_path, self.output_path)
    def test_case_7(self):
        # Test handling non-numeric values
        content = [
            f'echo "Name,Value" > {self.output_path}\n',
            f'echo "A,NonNumeric" >> {self.output_path}\n',
            f'echo "B,2" >> {self.output_path}\n',
        ]
        self._create_script(content)
        with self.assertRaises(TypeError):
            task_func(self.script_path, self.output_path)
    def test_case_8(self):
        # Test handling missing values
        content = [
            f'echo "Name,Value" > {self.output_path}\n',
            f'echo "A," >> {self.output_path}\n',
            f'echo "B,2" >> {self.output_path}\n',
        ]
        self._create_script(content)
        df, _ = task_func(self.script_path, self.output_path)
        self.assertTrue(df.isnull().values.any())
        self.assertEqual(df.shape, (2, 2))
    def test_case_9(self):
        # Handle handling of non-exitent script
        with self.assertRaises(ValueError):
            task_func(
                os.path.join(self.temp_dir.name, "invalid_script_nonexist.sh"),
                self.output_path,
            )
