import numpy as np
import itertools
import json


def task_func(data_list, json_file_name="mean_values.json"):
    """
    Calculate the mean of the numeric values for each position in the provided data list 
    and return the results. Optionally, the results can be exported to a specified JSON file.
    
    Parameters:
    - data_list (list of tuples): List of data tuples where each tuple contains a string followed by numeric values.
    - json_file_name (str, optional): Name of the JSON file to export the results. Defaults to 'mean_values.json'.

    Requirements:
    - numpy
    - itertools
    - json

    Returns:
    - dict: A dictionary with keys in the format 'Position {i}' and values being the mean of the numeric values 
            at position i in the provided data list.

    Example:
    >>> import tempfile
    >>> json_file = tempfile.NamedTemporaryFile(delete=False)
    >>> task_func([('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)], json_file.name)
    {'Position 1': 3.0, 'Position 2': 4.0}
    """
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = [np.nanmean(column) for column in unzipped_data[1:]]
    results = {'Position {}'.format(i+1): mean_value for i, mean_value in enumerate(mean_values)}
    with open(json_file_name, 'w') as f:
        json.dump(results, f)
    return results

import unittest
import doctest
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        self.json_file = tempfile.NamedTemporaryFile(delete=False)
    def tearDown(self):
        self.json_file.close()
    def test_case_1(self):
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4), ('d', 4, 5), ('e', 5, 6)]
        expected_output = {'Position 1': 3.0, 'Position 2': 4.0}
        self.assertEqual(task_func(data_list, self.json_file.name), expected_output)
    def test_case_2(self):
        data_list = [('a', 10, 20), ('b', 20, 30), ('c', 30, 40)]
        expected_output = {'Position 1': 20.0, 'Position 2': 30.0}
        self.assertEqual(task_func(data_list, self.json_file.name), expected_output)
    def test_case_3(self):
        data_list = [('a', 5), ('b', 10), ('c', 15)]
        expected_output = {'Position 1': 10.0}
        self.assertEqual(task_func(data_list, self.json_file.name), expected_output)
    def test_case_4(self):
        data_list = [('a', 1, 2, 3), ('b', 4, 5, 6), ('c', 7, 8, 9)]
        expected_output = {'Position 1': 4.0, 'Position 2': 5.0, 'Position 3': 6.0}
        self.assertEqual(task_func(data_list, self.json_file.name), expected_output)
        
    def test_case_5(self):
        # Test with JSON file export
        data_list = [('a', 1, 2), ('b', 2, 3), ('c', 3, 4)]
        expected_output = {'Position 1': 2.0, 'Position 2': 3.0}
        result = task_func(data_list, json_file_name=self.json_file.name)
        self.assertEqual(result, expected_output)
        with open(self.json_file.name, "r") as f:
            json_output = json.load(f)
        self.assertEqual(json_output, expected_output)
