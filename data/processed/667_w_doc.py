import json
import re
from collections import Counter

# Constants
REPLACE_NONE = "None"

def task_func(json_str):
    """
    Process a JSON string by:
    1. Removing None values.
    2. Counting the frequency of each unique value.
    3. Replacing all email addresses with the placeholder "None".
    
    Parameters:
    json_str (str): The JSON string to be processed.
    
    Returns:
    dict: A dictionary containing:
        - "data": Processed JSON data.
        - "value_counts": A Counter object with the frequency of each unique value.
    
    Requirements:
    - json
    - re
    - collections.Counter
    
    Example:
    >>> json_str = '{"name": "John", "age": null, "email": "john@example.com"}'
    >>> task_func(json_str)
    {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1, 'None': 1})}
    """
    data = json.loads(json_str)
    processed_data = {}
    for key, value in data.items():
        if value is None:
            continue
        if isinstance(value, str) and re.match(r"[^@]+@[^@]+\.[^@]+", value):
            value = REPLACE_NONE
        processed_data[key] = value
    value_counts = Counter(processed_data.values())
    return {"data": processed_data, "value_counts": value_counts}

import unittest
import json
from collections import Counter
class TestCases(unittest.TestCase):
    def test_basic(self):
        json_str = '{"name": "John", "age": null, "email": "john@example.com"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1, 'None': 1})}
        self.assertEqual(result, expected)
    def test_multiple_none(self):
        json_str = '{"name": "John", "age": null, "city": null, "email": "john@example.com"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1, 'None': 1})}
        self.assertEqual(result, expected)
    def test_multiple_emails(self):
        json_str = '{"name": "John", "email1": "john1@example.com", "email2": "john2@example.com"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'email1': 'None', 'email2': 'None'}, 'value_counts': Counter({'None': 2, 'John': 1})}
        self.assertEqual(result, expected)
    def test_no_emails(self):
        json_str = '{"name": "John", "age": 25, "city": "NY"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'age': 25, 'city': 'NY'}, 'value_counts': Counter({'John': 1, 25: 1, 'NY': 1})}
        self.assertEqual(result, expected)
    def test_different_values(self):
        json_str = '{"name": "John", "age": 25, "city": "NY", "friend": "John"}'
        result = task_func(json_str)
        expected = {'data': {'name': 'John', 'age': 25, 'city': 'NY', 'friend': 'John'}, 'value_counts': Counter({'John': 2, 25: 1, 'NY': 1})}
        self.assertEqual(result, expected)
