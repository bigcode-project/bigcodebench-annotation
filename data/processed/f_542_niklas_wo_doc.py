import pandas as pd
import json


def f_544(file_path, key):
    """
    Load a JSON file into a Pandas DataFrame, remove a specific key from each object and write the processed DataFrame back into a JSON file oriented by records.
    
    Parameters:
    - file_path (str): The path to the JSON file.
    - key (str): The key to remove from each object.
    
    Returns:
    - df (DataFrame): A pandas DataFrame representation of the processed JSON data.

    Requirements:
    - pandas
    - json
    
    Example:
    >>> df = f_544('data.json', 'ele')
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    df.drop(key, axis=1, inplace=True)
    with open(file_path, 'w') as file:
        file.write(df.to_json(orient='records'))
    return df

import unittest
import os
class TestCases(unittest.TestCase):
    def base(self, json_path, key, contents):
        # Create JSON file
        with open(json_path, 'w') as file:
            json.dump(contents, file)
        # Run function
        df = f_544(json_path, key)
        # Check key is removed
        self.assertFalse(key in df.columns)
        # Check JSON file is updated
        with open(json_path, 'r') as file:
            data = json.load(file)
        self.assertFalse(key in data[0])
        # Remove JSON file
        os.remove(json_path)
    def test_case_1(self):
        self.base('data.json', 'ele', [{'ele': 1, 'a': 2}, {'ele': 3, 'a': 4}])
    def test_case_2(self):
        self.base('data.json', 'ele', [{'ele': 1, 'a': 2}, {'ele': 3, 'a': 4}, {'ele': 5, 'a': 6}])
    def test_case_3(self):
        self.base('x.json', 'zzz', [{'zzz': 1, 'a': 2}, {'zzz': 3, 'a': 4}])
    def test_case_4(self):
        self.base('g.json', 'ele', [{'ele': 1, 'a': 2}, {'ele': 3, 'a': 4}])
    def test_case_5(self):
        self.base('data.json', 'ele', [{'ele': 1, 'a': 2}, {'ele': 3, 'a': 4}])
