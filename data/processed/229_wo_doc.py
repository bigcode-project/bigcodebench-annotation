import json
import random
from datetime import datetime, timedelta


# Constants
USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

def task_func(file_path, num_entries, seed=None):
    """
    Create a JSON file on a specific file path with random user activity data.
    The number of entries in the JSON file is determined by num_entries. The written JSON file contains a list of dictionaries, with each dictionary representing a log entry with the following keys: 'user', 'action', and 'timestamp'.

    Parameters:
    file_path (str): The file path where the JSON file should be created.
    num_entries (int): The number of entries of random data to generate.
    seed (int, optional): The seed for random data generation. Default is None.

    Returns:
    str: The file path of the generated JSON file.

    Requirements:
    - os
    - json
    - random
    - datetime

    Example:
    >>> task_func('/tmp/log.json', 100)
    '/tmp/log.json'
    """
    if seed is not None:
        random.seed(seed)
    log_entries = []
    current_time = datetime.now()
    for _ in range(num_entries):
        user = random.choice(USERS)
        action = random.choice(['login', 'logout', 'view_page', 'edit_profile', 'post_message'])
        timestamp = current_time.strftime('%Y-%m-%dT%H:%M:%S')
        log_entries.append({'user': user, 'action': action, 'timestamp': timestamp})
        current_time -= timedelta(minutes=random.randint(1, 60))
    with open(file_path, 'w') as json_file:
        json.dump(log_entries, json_file, indent=4)
    return file_path

import unittest
import os
import doctest
import tempfile
class TestCases(unittest.TestCase):
    def setUp(self):
        # Set up the test file path
        self.temp_dir = tempfile.gettempdir()
        self.test_file_path = f"{self.temp_dir}/test_log.json"
    
    def tearDown(self):
        # Clean up the generated test file after each test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
    
    def test_case_1(self):
        # Test basic functionality with a small number of entries
        result_path = task_func(self.test_file_path, 5, seed=42)
        self.assertEqual(result_path, self.test_file_path)
        self.assertTrue(os.path.exists(result_path))
        with open(result_path, 'r') as json_file:
            data = json.load(json_file)
            self.assertEqual(len(data), 5)
    
    def test_case_2(self):
        # Test with a larger number of entries
        result_path = task_func(self.test_file_path, 100, seed=42)
        self.assertEqual(result_path, self.test_file_path)
        self.assertTrue(os.path.exists(result_path))
        with open(result_path, 'r') as json_file:
            data = json.load(json_file)
            self.assertEqual(len(data), 100)
    
    def test_case_3(self):
        # Test the randomness of the entries (should be consistent with the seed)
        result_path = task_func(self.test_file_path, 10, seed=42)
        with open(result_path, 'r') as json_file:
            data1 = json.load(json_file)
        
        os.remove(result_path)
        
        result_path = task_func(self.test_file_path, 10, seed=42)
        with open(result_path, 'r') as json_file:
            data2 = json.load(json_file)
        
        self.assertEqual(data1, data2)
    
    def test_case_4(self):
        # Test the randomness of the entries without a seed (should differ between runs)
        result_path = task_func(self.test_file_path, 10)
        with open(result_path, 'r') as json_file:
            data1 = json.load(json_file)
        
        os.remove(result_path)
        
        result_path = task_func(self.test_file_path, 10)
        with open(result_path, 'r') as json_file:
            data2 = json.load(json_file)
        
        self.assertNotEqual(data1, data2)
    
    def test_case_5(self):
        # Test the attributes in the entries
        result_path = task_func(self.test_file_path, 5, seed=42)
        with open(result_path, 'r') as json_file:
            data = json.load(json_file)
            for entry in data:
                self.assertIn('user', entry)
                self.assertIn('action', entry)
                self.assertIn('timestamp', entry)
                self.assertIn(entry['user'], USERS)
                self.assertIn(entry['action'], ['login', 'logout', 'view_page', 'edit_profile', 'post_message'])
