import json
import pandas as pd


def task_func(result, csv_file_path="test.csv", json_file_path="test.json"):
    """
    Save the list of dictionaries provided in the 'result' parameter to a CSV file (without index) and a JSON file.

    Parameters:
    - result (list): A list of dictionaries.
    - csv_file_path (str): A path to a CSV file.
    - json_file_path (str): A path to a JSON file.

    Returns:
    None

    Requirements:
    - pandas
    - json

    Example:
    >>> result = [{"hi": 7, "bye": 4, "from_user": 0}, {1: 2, 3: 4, 5: 6}]
    >>> task_func(result, 'test.csv', 'test.json')
    """
    df = pd.DataFrame(result)
    df.to_csv(csv_file_path, index=False)
    with open(json_file_path, 'w') as f:
        json.dump(result, f, indent=4)
    return None

import unittest
import os
class TestCases(unittest.TestCase):
    """Test cases for the task_func function."""
    def setUp(self):
        self.test_dir = "data/task_func"
        os.makedirs(self.test_dir, exist_ok=True)
        self.f_1 = os.path.join(self.test_dir, "csv_1.csv")
        self.f_2 = os.path.join(self.test_dir, "csv_2.csv")
        self.f_3 = os.path.join(self.test_dir, "csv_3.csv")
        self.f_4 = os.path.join(self.test_dir, "csv_4.csv")
        self.f_5 = os.path.join(self.test_dir, "csv_5.csv")
        self.j_1 = os.path.join(self.test_dir, "json_1.json")
        self.j_2 = os.path.join(self.test_dir, "json_2.json")
        self.j_3 = os.path.join(self.test_dir, "json_3.json")
        self.j_4 = os.path.join(self.test_dir, "json_4.json")
        self.j_5 = os.path.join(self.test_dir, "json_5.json")
    def tearDown(self):
        import shutil
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    def test_case_1(self):
        # Test with a list of dictionaries with string keys and integer values
        result = [
            {"hi": 7, "bye": 4, "from_user": 0}
        ]
        task_func(result, self.f_1, self.j_1)
        self.assertTrue(os.path.exists(self.f_1))
        self.assertTrue(os.path.exists(self.j_1))
        with open(self.j_1, 'r') as f:
            loaded_json = json.load(f)
        # Adjusting the expected result for JSON's string keys
        expected_result = [{"hi": 7, "bye": 4, "from_user": 0}]
        self.assertEqual(loaded_json, expected_result)
    def test_case_2(self):
        # Test with a list of dictionaries with integer keys and values
        result = [{1: 2, 3: 4, 5: 6}]
        task_func(result, self.f_2, self.j_2)
        self.assertTrue(os.path.exists(self.f_2))
        self.assertTrue(os.path.exists(self.j_2))
        with open(self.j_2, 'r') as f:
            loaded_json = json.load(f)
        # Adjusting the expected result for JSON's string keys
        expected_result = [{"1": 2, "3": 4, "5": 6}]
        self.assertEqual(loaded_json, expected_result)
    def test_case_3(self):
        # Test with an empty list
        result = []
        task_func(result, self.f_3, self.j_3)
        self.assertTrue(os.path.exists(self.f_3))
        self.assertTrue(os.path.exists(self.j_3))
        with open(self.j_3, 'r') as f:
            loaded_json = json.load(f)
        # Adjusting the expected result for JSON's string keys
        expected_result = []
        self.assertEqual(loaded_json, expected_result)
    def test_case_4(self):
        # Test with a list of dictionaries with string keys and integer values
        result = [
            {"hi": 7, "bye": 4, "from_user": 3}
        ]
        task_func(result, self.f_4, self.j_4)
        self.assertTrue(os.path.exists(self.f_4))
        self.assertTrue(os.path.exists(self.j_4))
        with open(self.j_4, 'r') as f:
            loaded_json = json.load(f)
        # Adjusting the expected result for JSON's string keys
        expected_result = [{"hi": 7, "bye": 4, "from_user": 3}]
        self.assertEqual(loaded_json, expected_result)
    def test_case_5(self):
        # Test with a list of dictionaries with string keys and integer values
        result = [
            {"hi": 7, "bye": 4, "from_user": 11}
        ]
        task_func(result, self.f_5, self.j_5)
        self.assertTrue(os.path.exists(self.f_5))
        df = pd.read_csv(self.f_5)
        self.assertEqual(df.loc[0, "hi"], 7)
        self.assertEqual(df.loc[0, "bye"], 4)
        self.assertEqual(df.loc[0, "from_user"], 11)
        self.assertTrue(os.path.exists(self.j_5))
        with open(self.j_5, 'r') as f:
            loaded_json = json.load(f)
        # Adjusting the expected result for JSON's string keys
        expected_result = [{"hi": 7, "bye": 4, "from_user": 11}]
        self.assertEqual(loaded_json, expected_result)
