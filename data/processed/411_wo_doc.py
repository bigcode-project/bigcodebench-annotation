import pandas as pd
import json


def task_func(data: dict, output_path: str = "./default_data_output.json") -> str:
    """
    Converts the given DataFrame to a dictionary, dropping the column named 'c'
    if it exists, and then saves it as a JSON file.

    Parameters:
    - data (dict): The input data dictionary.
    - output_path (str, optional): The path where the JSON file should be saved. Default is './default_data_output.json'.

    Returns:
    - str: Path where the JSON file was saved.

    Requirements:
    - pandas
    - json

    Example:
    >>> task_func({'a': [1,2], 'b': [3,4], 'c': [5,6]})
    './default_data_output.json'
    >>> print(json.load(open(task_func({'a': [1,2], 'b': [3,4], 'c': [5,6]})))
    {'a': {'0': 1, '1': 2}, 'b': {'0': 3, '1': 4}}
    >>> task_func({'a': [1,2], 'b': [3,4], 'c': [5,6]}, 'custom/path/results.json')
    'custom/path/results.json'
    >>> print(json.load(open(task_func({'a': [1,2], 'b': [3,4], 'c': [5,6]}, 'custom/path/results.json')))
    {'a': {'0': 1, '1': 2}, 'b': {'0': 3, '1': 4}}
    """
    df = pd.DataFrame(data)
    df = df.drop(columns="c", errors="ignore")
    data_dict = df.to_dict(orient="dict")
    with open(output_path, "w") as file:
        json.dump(data_dict, file)
    return output_path

import unittest
import pandas as pd
import json
import os
class TestCases(unittest.TestCase):
    def read_json_file(self, path):
        # Helper function to read content from a JSON file
        with open(path, "r") as f:
            return json.load(f)
    def tearDown(self):
        # Cleanup procedure after each test to remove generated files
        files_to_remove = [
            "./default_data_output.json",
            "./custom_data_output_2.json",
            "./custom_data_output_3.json",
            "./custom_data_output_4.json",
            "./custom_data_output_5.json",
        ]
        for file in files_to_remove:
            if os.path.exists(file):
                os.remove(file)
    def convert_keys_to_str(self, dictionary):
        # Convert dictionary keys to strings recursively
        if not isinstance(dictionary, dict):
            return dictionary
        return {str(k): self.convert_keys_to_str(v) for k, v in dictionary.items()}
    def test_case_1(self):
        # Test basic DataFrame with column "c"
        data = {"a": [1, 2], "b": [3, 4], "c": [5, 6]}
        df = pd.DataFrame(data)
        output_path = task_func(data)
        self.assertTrue(os.path.exists(output_path))
        expected_data = self.convert_keys_to_str(
            df.drop(columns="c").to_dict(orient="dict")
        )
        self.assertEqual(self.read_json_file(output_path), expected_data)
    def test_case_2(self):
        # Test DataFrame with non-numeric data and column "c"
        data = {"name": ["Alice", "Bob"], "country": ["USA", "Canada"], "c": ["x", "y"]}
        df = pd.DataFrame(data)
        custom_path = "./custom_data_output_2.json"
        output_path = task_func(data, custom_path)
        self.assertTrue(os.path.exists(output_path))
        expected_data = self.convert_keys_to_str(
            df.drop(columns="c").to_dict(orient="dict")
        )
        self.assertEqual(self.read_json_file(output_path), expected_data)
    def test_case_3(self):
        # Test DataFrame with multiple columns and no column "c"
        data = {"age": [25, 30], "height": [170, 175]}
        df = pd.DataFrame(data)
        custom_path = "./custom_data_output_3.json"
        output_path = task_func(data, custom_path)
        self.assertTrue(os.path.exists(output_path))
        expected_data = self.convert_keys_to_str(df.to_dict(orient="dict"))
        self.assertEqual(self.read_json_file(output_path), expected_data)
    def test_case_4(self):
        # Test DataFrame with mixed data types including column "c"
        data = {
                "id": [1, 2],
                "is_student": [True, False],
                "grades": ["A", "B"],
                "c": [0.5, 0.8],
            }
        df = pd.DataFrame(data)
        output_path = task_func(data)
        self.assertTrue(os.path.exists(output_path))
        expected_data = self.convert_keys_to_str(
            df.drop(columns="c").to_dict(orient="dict")
        )
        self.assertEqual(self.read_json_file(output_path), expected_data)
    def test_case_5(self):
        # Test an empty DataFrame
        data = {}
        df = pd.DataFrame(data)
        custom_path = "./custom_data_output_5.json"
        output_path = task_func(data, custom_path)
        self.assertTrue(os.path.exists(output_path))
        expected_data = self.convert_keys_to_str(df.to_dict(orient="dict"))
        self.assertEqual(self.read_json_file(output_path), expected_data)
