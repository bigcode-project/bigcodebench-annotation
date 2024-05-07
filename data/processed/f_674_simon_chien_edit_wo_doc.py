import collections
import numpy as np


def f_173(file_name):
    """
    Find the most common value in each column of a csv file with column names.

    If some values occur the same number of times, the values are sorted
    alphabetically and the first is considered most common.

    If an empty csv is passed, an empty dictionary is returned. 
    
    Parameters:
    file_name (str): The name of the csv file.
    
    Returns:
    dict: A dictionary with column names as keys and most common values as values.

    Requirements:
    - collections
    - numpy
    
    Example:
    >>> common_values = f_173('sample.csv')
    >>> print(common_values)
    {'Name': 'Simon Velasquez',
    'Age': 21,
    'Fruit': 'Apple',
    'Genre': 'HipHop',
    'Height': 172}
    """
    data = np.genfromtxt(file_name, delimiter=',', names=True,
                         dtype=None, encoding=None)
    common_values = {}
    if len(np.atleast_1d(data)) == 0:
        return {}
    if len(np.atleast_1d(data)) == 1:
        for col in data.dtype.names:
            common_values[col] = data[col].item()
    else:
        for col in data.dtype.names:
            counter = collections.Counter(data[col])
            if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                common_values[col] = sorted(counter.items())[0][0]
            else:
                common_values[col] = counter.most_common(1)[0][0]
    return common_values

import unittest
import os
import shutil
import tempfile
import csv
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory to house the CSV files
        self.test_dir = tempfile.mkdtemp()
    def tearDown(self):
        # Remove the temporary directory after the test
        shutil.rmtree(self.test_dir)
    def create_csv(self, file_name, headers, data):
        # Helper function to create a CSV file
        path = os.path.join(self.test_dir, file_name)
        with open(path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        return path
    def test_empty_csv(self):
        # Test for an empty CSV file
        file_path = self.create_csv('empty.csv', ['Name', 'Age'], [])
        result = f_173(file_path)
        self.assertEqual(result, {})
    def test_single_entry(self):
        # Test for a CSV file with a single entry
        file_path = self.create_csv('single.csv', ['Name', 'Age'], [{'Name': 'John', 'Age': '30'}])
        result = f_173(file_path)
        self.assertEqual(result, {'Name': 'John', 'Age': 30})
    def test_common_values_sorted(self):
        # Test for common values, ensuring alphabetical sorting
        file_path = self.create_csv('common_values.csv', ['Fruit'], [{'Fruit': 'Apple'}, {'Fruit': 'Banana'}, {'Fruit': 'Apple'}, {'Fruit': 'Banana'}, {'Fruit': 'Cherry'}])
        result = f_173(file_path)
        self.assertEqual(result, {'Fruit': 'Apple'})
    def test_multiple_columns(self):
        # Test for multiple columns and entries
        data = [{'Name': 'Alice', 'Age': '25', 'Country': 'USA'},
                {'Name': 'Bob', 'Age': '30', 'Country': 'USA'},
                {'Name': 'Alice', 'Age': '25', 'Country': 'Canada'}]
        file_path = self.create_csv('multi_columns.csv', ['Name', 'Age', 'Country'], data)
        result = f_173(file_path)
        expected = {'Name': 'Alice', 'Age': 25, 'Country': 'USA'}
        self.assertEqual(result, expected)
    def test_tie_breaking(self):
        # Test for tie-breaking in value counts
        data = [{'Name': 'Alice'}, {'Name': 'Bob'}, {'Name': 'Alice'}, {'Name': 'Bob'}]
        file_path = self.create_csv('tie.csv', ['Name'], data)
        result = f_173(file_path)
        self.assertEqual(result, {'Name': 'Alice'})
