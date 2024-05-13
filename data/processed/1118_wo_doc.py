import json
import csv
import requests
from io import StringIO

# Constants
CSV_URL = 'https://example.com/data.csv'
JSON_FILE = 'data.json'

def task_func(csv_url=CSV_URL, json_file_path=JSON_FILE):
    """
    Downloads a CSV file from a specified URL, converts it to JSON format, and saves it to a specified file path.
    
    Parameters:
    - csv_url (str): The URL from which the CSV data should be downloaded. Defaults to a constant CSV_URL.
    - json_file_path (str): The file path where the JSON data should be saved. Defaults to a constant JSON_FILE.

    Returns:
    str: The path to the saved JSON file.

    Requirements:
    - json
    - csv
    - requests
    - io.StringIO

    Example:
    >>> task_func("https://example.com/sample.csv", "sample.json")
    "sample.json"
    """

    response = requests.get(csv_url)
    csv_data = csv.reader(StringIO(response.text))
    headers = next(csv_data)
    json_data = [dict(zip(headers, row)) for row in csv_data]
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file)
    return json_file_path

import unittest
from unittest.mock import patch, Mock
import json
import csv
import requests
from io import StringIO
# Mocking the CSV data
mock_csv_data = """header1,header2,header3
value1a,value2a,value3a
value1b,value2b,value3b
"""
# Creating the mocked response object for the requests.get call
mock_response = Mock()
mock_response.text = mock_csv_data
# Blackbox test cases
class TestCases(unittest.TestCase):
    
    @patch("requests.get", return_value=mock_response)
    def test_case_1(self, mock_get):
        # Testing with default parameters
        output_file = task_func()
        with open(output_file, 'r') as file:
            data = json.load(file)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['header1'], 'value1a')
        
    @patch("requests.get", return_value=mock_response)
    def test_case_2(self, mock_get):
        # Testing with custom parameters
        output_file = task_func("https://example.com/mock.csv", "mock_output.json")
        with open(output_file, 'r') as file:
            data = json.load(file)
        self.assertEqual(data[1]['header2'], 'value2b')
        
    @patch("requests.get", return_value=mock_response)
    def test_case_3(self, mock_get):
        # Testing JSON structure
        output_file = task_func()
        with open(output_file, 'r') as file:
            data = json.load(file)
        self.assertIn('header3', data[0])
        
    @patch("requests.get", return_value=mock_response)
    def test_case_4(self, mock_get):
        # Testing CSV with only headers (no data)
        mock_get.return_value.text = "header1,header2,header3\n"
        output_file = task_func()
        with open(output_file, 'r') as file:
            data = json.load(file)
        self.assertEqual(len(data), 0)
        
    @patch("requests.get", return_value=mock_response)
    def test_case_5(self, mock_get):
        # Testing CSV with multiple data rows
        mock_get.return_value.text = mock_csv_data
        output_file = task_func()
        with open(output_file, 'r') as file:
            data = json.load(file)
        self.assertEqual(len(data), 2)
