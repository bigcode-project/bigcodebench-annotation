import json
import re
from collections import Counter

# Constants
REPLACE_NONE = "None"

def f_653(json_str):
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
    >>> json_str = '{"name": "John", "age": None, "email": "john@example.com"}'
    >>> f_653(json_str)
    {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1})}
    """
    data = json.loads(json_str)
    data = {k: v for k, v in data.items() if v is not None}

    value_counts = Counter(data.values())
    data = {k: REPLACE_NONE if isinstance(v, str) and re.match(r"[^@]+@[^@]+\.[^@]+", v) else v for k, v in data.items()}

    return {"data": data, "value_counts": value_counts}

import unittest
import json
from collections import Counter

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_basic(self):
        json_str = '{"name": "John", "age": null, "email": "john@example.com"}'
        result = f_653(json_str)
        expected = {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1})}
        self.assertEqual(result, expected)

    def test_multiple_none(self):
        json_str = '{"name": "John", "age": null, "city": null, "email": "john@example.com"}'
        result = f_653(json_str)
        expected = {'data': {'name': 'John', 'email': 'None'}, 'value_counts': Counter({'John': 1})}
        self.assertEqual(result, expected)

    def test_multiple_emails(self):
        json_str = '{"name": "John", "email1": "john1@example.com", "email2": "john2@example.com"}'
        result = f_653(json_str)
        expected = {'data': {'name': 'John', 'email1': 'None', 'email2': 'None'}, 'value_counts': Counter({'John': 1})}
        self.assertEqual(result, expected)

    def test_no_emails(self):
        json_str = '{"name": "John", "age": 25, "city": "NY"}'
        result = f_653(json_str)
        expected = {'data': {'name': 'John', 'age': 25, 'city': 'NY'}, 'value_counts': Counter({'John': 1, 25: 1, 'NY': 1})}
        self.assertEqual(result, expected)

    def test_different_values(self):
        json_str = '{"name": "John", "age": 25, "city": "NY", "friend": "John"}'
        result = f_653(json_str)
        expected = {'data': {'name': 'John', 'age': 25, 'city': 'NY', 'friend': 'John'}, 'value_counts': Counter({'John': 2, 25: 1, 'NY': 1})}
        self.assertEqual(result, expected)
if __name__ == "__main__":
    run_tests()