import sys
import json
from datetime import datetime

# Constants
PATH_TO_APPEND = '/path/to/whatever'
JSON_FILE = '/path/to/json_file.json'

def task_func(path_to_append=PATH_TO_APPEND, json_file=JSON_FILE):
    """
    Add a specific path to sys.path and update a JSON file with the current date and time.
    This function appends a given path to Python's sys.path and updates a JSON file with the current date and time under the key 'last_updated'.
    
    Parameters:
    - path_to_append (str): The path to append to sys.path. Default is '/path/to/whatever'.
    - json_file (str): The path to the JSON file to update. Default is '/path/to/json_file.json'. The file should exist before running the function.

    Returns:
    - json_data (dict): The updated JSON data. The dictionary will contain a 'last_updated' key with the current datetime as its value.

    Requirements:
    - sys
    - json
    - datetime.datetime

    Example:
    >>> task_func('/path/to/new_directory', '/path/to/new_json_file.json')
    {'last_updated': '2023-08-28 12:34:56'}
    """

    sys.path.append(path_to_append)
    with open(json_file, 'r+') as file:
        json_data = json.load(file)
        json_data['last_updated'] = str(datetime.now())
        file.seek(0)
        json.dump(json_data, file, indent=4)
        file.truncate()
    return json_data

import unittest
import json
import os
import tempfile
import sys
from datetime import datetime
# Update this path if needed to point to an actual temporary directory
class TestCases(unittest.TestCase):
    
    def setUp(self):
        # Create temporary JSON files for testing in text mode
        self.test_json_file_1 = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.test_json_file_2 = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        json.dump({'key': 'value'}, self.test_json_file_1)
        json.dump({'key': 'value'}, self.test_json_file_2)
        self.test_json_file_1.close()
        self.test_json_file_2.close()
        self.tmp_file = tempfile.mktemp(suffix='.json')
        with open(self.tmp_file, 'w') as f:
            json.dump({'initial_key': 'initial_value'}, f)
    def tearDown(self):
        # Remove temporary JSON files after testing
        os.unlink(self.test_json_file_1.name)
        os.unlink(self.test_json_file_2.name)
        os.remove(self.tmp_file)
        
    def test_path_append(self):
        # Test if the path is correctly appended to sys.path
        new_path = '/new/test/path'
        task_func(path_to_append=new_path, json_file=self.test_json_file_1.name)
        self.assertIn(new_path, sys.path)
    def test_json_update_1(self):
        # Test if the JSON file is correctly updated (test_json_file_1)
        output = task_func(json_file=self.test_json_file_1.name)
        self.assertIn('last_updated', output)
        self.assertIsInstance(datetime.strptime(output['last_updated'], '%Y-%m-%d %H:%M:%S.%f'), datetime)
    def test_json_update_2(self):
        # Test if the JSON file is correctly updated (test_json_file_2)
        output = task_func(json_file=self.test_json_file_2.name)
        self.assertIn('last_updated', output)
        self.assertIsInstance(datetime.strptime(output['last_updated'], '%Y-%m-%d %H:%M:%S.%f'), datetime)
    def test_default_path(self):
        # Test if the default path is correctly appended when no argument is passed
        task_func(json_file=self.test_json_file_1.name)
        self.assertIn('/path/to/whatever', sys.path)
    def test_default_json(self):
        # Test if the default JSON file is correctly updated when no argument is passed
        output = task_func(json_file=self.tmp_file)
        self.assertIn('last_updated', output)
        self.assertIsInstance(datetime.strptime(output['last_updated'], '%Y-%m-%d %H:%M:%S.%f'), datetime)
