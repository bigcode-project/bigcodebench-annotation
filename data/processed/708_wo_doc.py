import json
import csv
import os
import base64

def task_func(raw_string, filename, output_dir):
    """
    Processes a base64-encoded JSON string, stores the data in a CSV file, and returns the path of the file.

    Parameters:
    - raw_string (str): The base64 encoded JSON string.
    - filename (str): The name of the file to which the data should be saved (without extension).
    - output_dir (str): The path of the directory in which the file should be saved.

    Returns:
    - file_path (str): The path of the file.

    Requirements:
    - json
    - csv
    - os
    - base64

    Example:
    >>> task_func('eyJrZXkiOiAiVmFsdWUifQ==', 'data', './output')
    './output/data.csv'
    """

    decoded_string = base64.b64decode(raw_string).decode('utf-8')
    data = json.loads(decoded_string)
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f'{filename}.csv')
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for key, value in data.items():
            writer.writerow([key, value])
    return file_path

import unittest
import shutil
class TestCases(unittest.TestCase):
    def tearDown(self):
        if os.path.exists('./output'):
            shutil.rmtree('./output')
    
    def test_case_1(self):
        raw_string = 'eyJrZXkiOiAiVmFsdWUifQ=='
        filename = 'data'
        output_dir = './output'
        expected = './output/data.csv'
        self.assertEqual(task_func(raw_string, filename, output_dir), expected)
        with open(expected, 'r') as f:
            self.assertEqual(f.read(), 'key,Value\n')
        os.remove(expected)
    
    def test_case_2(self):
        string_before = """{"key": "hello"}"""
        raw_string = base64.b64encode(string_before.encode('utf-8')).decode('utf-8')
        filename = 'data'
        output_dir = './output'
        expected = './output/data.csv'
        self.assertEqual(task_func(raw_string, filename, output_dir), expected)
        with open(expected, 'r') as f:
            self.assertEqual(f.read(), 'key,hello\n')
        os.remove(expected)
    def test_case_3(self):
        string_before = """{"key": "hello", "key2": "world"}"""
        raw_string = base64.b64encode(string_before.encode('utf-8')).decode('utf-8')
        filename = 'data'
        output_dir = './output'
        expected = './output/data.csv'
        self.assertEqual(task_func(raw_string, filename, output_dir), expected)
        with open(expected, 'r') as f:
            self.assertEqual(f.read(), 'key,hello\nkey2,world\n')
        os.remove(expected)
    def test_case_4(self):
        string_before = """{"key": "hello", "key2": "world", "key3": "!"}"""
        raw_string = base64.b64encode(string_before.encode('utf-8')).decode('utf-8')
        filename = 'data'
        output_dir = './output'
        expected = './output/data.csv'
        self.assertEqual(task_func(raw_string, filename, output_dir), expected)
        with open(expected, 'r') as f:
            self.assertEqual(f.read(), 'key,hello\nkey2,world\nkey3,!\n')
        os.remove(expected)
    def test_case_5(self):
        string_before = """{"key": "hello", "key2": "world", "key3": "!", "key4": "test"}"""
        raw_string = base64.b64encode(string_before.encode('utf-8')).decode('utf-8')
        filename = 'data'
        output_dir = './output'
        expected = './output/data.csv'
        self.assertEqual(task_func(raw_string, filename, output_dir), expected)
        with open(expected, 'r') as f:
            self.assertEqual(f.read(), 'key,hello\nkey2,world\nkey3,!\nkey4,test\n')
        os.remove(expected)
