import json
import os
import re

# Constants
VALID_JSON_STRUCTURE = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "email": {"type": "string"}
    },
    "required": ["name", "age", "email"]
}

EMAIL_REGEX = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

def f_1029(file_path, attribute):
    """
    Validate the structure and contents of a JSON file against predefined schema rules and retrieve a specified attribute from the JSON object. Ensures that all required fields exist, match their defined types, and checks the validity of the email format using a regular expression.
    
    Parameters:
    file_path (str): The path to the JSON file.
    attribute (str): The attribute to retrieve from the JSON object.

    Returns:
    Any: The value of the specified attribute, consistent with the type defined in the JSON schema.

    Requirements:
    - json
    - os
    - re

    Errors:
    - Raises ValueError if the file does not exist, required attributes are missing, types do not match, or the email format is invalid.

    Example:
    >>> f_1029('/path/to/file.json', 'email')
    'john.doe@example.com'
    """
    if not os.path.isfile(file_path):
        raise ValueError(f'{file_path} does not exist.')

    with open(file_path, 'r') as f:
        data = json.load(f)

    for key in VALID_JSON_STRUCTURE['required']:
        if key not in data:
            raise ValueError(f'{key} is missing from the JSON object.')
        if not isinstance(data[key], VALID_JSON_STRUCTURE['properties'][key]['type']):
            raise ValueError(f'{key} is not of type {VALID_JSON_STRUCTURE["properties"][key]["type"]}.')

    if 'email' in data and not re.fullmatch(EMAIL_REGEX, data['email']):
        raise ValueError('Email is not valid.')

    return data[attribute]

import unittest
import json
import os
import re
from typing import Union

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_valid_json(self):
        # Test with valid JSON data
        result = f_1029('/mnt/data/valid.json', 'name')
        self.assertEqual(result, "John Doe")
    
    def test_case_invalid_missing_attr(self):
        # Test with JSON missing required attribute
        with self.assertRaises(ValueError):
            f_1029('/mnt/data/invalid_missing_attr.json', 'name')
    
    def test_case_invalid_email_format(self):
        # Test with JSON having incorrect email format
        with self.assertRaises(ValueError):
            f_1029('/mnt/data/invalid_email_format.json', 'email')
    
    def test_case_non_existent_file(self):
        # Test with non-existent file path
        with self.assertRaises(ValueError):
            f_1029('/mnt/data/non_existent.json', 'name')
    
    def test_case_retrieve_age(self):
        # Test retrieving age from valid JSON
        result = f_1029('/mnt/data/valid.json', 'age')
        self.assertEqual(result, 30)

if __name__ == "__main__":
    run_tests()