import os
import json
from collections import Counter


def f_269(json_files_path='./json_files/', key='name'):
    """
    Count the occurrence of a particular key in all json files in a specified directory 
    and return a dictionary with the values of the specified key and their counts.
    
    Parameters:
    - json_files_path (str): The path to the directory containing the JSON files. Default is './json_files/'.
    - key (str): The key in the JSON files whose values need to be counted. Default is 'name'.
    
    Returns:
    dict: A dictionary with values of the key as keys and their counts as values.
    
    Requirements:
    - os
    - json
    - collections.Counter
    
    Example:
    >>> import tempfile
    >>> import json
    >>> directory = tempfile.mkdtemp()
    >>> data = [{'product': 'apple', 'quantity': 5}, {'product': 'banana', 'quantity': 3}]
    >>> for i, d in enumerate(data):
    ...     with open(f"{directory}/{i}.json", 'w') as file:
    ...         json.dump(d, file)

    >>> f_269(json_files_path=directory, key='product')
    {'apple': 1, 'banana': 1}
    """
    key_values = []

    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_files_path, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                if key in data:
                    key_values.append(data[key])

    return dict(Counter(key_values))


import unittest
import doctest
import tempfile


class TestCases(unittest.TestCase):

    def setUp(self):
        self.mock_data_directory = tempfile.mkdtemp()
        
        # Create mock data
        mock_data = [
            {'name': 'John', 'city': 'New York'},
            {'name': 'Jane', 'city': 'Los Angeles'},
            {'name': 'John', 'city': 'New York'},
            {'name': 'Alice', 'city': 'Chicago'},
            {'name': 'Bob', 'city': 'New York'},
            {'name': 'Alice', 'city': 'Chicago'},
            {'name': 'Alice', 'city': 'Chicago'},
            {'city': 'Los Angeles'},
            {'city': 'Chicago'},
            {'city': 'New York'},
            {'city': 'New York'},
            {'city': 'New York'},
        ]
        
        for i, data in enumerate(mock_data):
            with open(f"{self.mock_data_directory}/{i}.json", 'w') as file:
                json.dump(data, file)
    
    def test_case_1(self):
        # Test with mock data directory and 'name' key
        result = f_269(self.mock_data_directory, 'name')
        
        # To verify the result, we need to read all JSON files and count the occurrences of the 'name' key values
        expected_counts = []
        for filename in os.listdir(self.mock_data_directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.mock_data_directory, filename), 'r') as file:
                    data = json.load(file)
                    if 'name' in data:
                        expected_counts.append(data['name'])
                        
        expected_result = dict(Counter(expected_counts))
        
        self.assertDictEqual(result, expected_result)

    def test_case_2(self):
        # Test with a non-existent key
        result = f_269(self.mock_data_directory, 'non_existent_key')
        self.assertDictEqual(result, {})

    def test_case_3(self):
        # Test with another key present in our mock data ('city' in this case)
        result = f_269(self.mock_data_directory, 'city')
        
        # To verify the result, we need to read all JSON files and count the occurrences of the 'city' key values
        expected_counts = []
        for filename in os.listdir(self.mock_data_directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.mock_data_directory, filename), 'r') as file:
                    data = json.load(file)
                    if 'city' in data:
                        expected_counts.append(data['city'])
                        
        expected_result = dict(Counter(expected_counts))
        
        self.assertDictEqual(result, expected_result)

    def test_case_4(self):
        # Test with a directory that doesn't contain any JSON files
        empty_directory = f"{self.mock_data_directory}/empty_directory/"
        os.makedirs(empty_directory, exist_ok=True)
        
        result = f_269(empty_directory, 'name')
        self.assertDictEqual(result, {})

    def test_case_5(self):
        # Test with a directory that doesn't exist
        non_existent_directory = f"{self.mock_data_directory}/non_existent_directory/"
        
        with self.assertRaises(FileNotFoundError):
            f_269(non_existent_directory, 'name')


# Blackbox testing function
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
