import json
import os
import re

def f_1029(
    file_path,
    attribute,
    INPUT_JSON={
        "type": "object",
        "properties": {
            "name": {"type": str},  
            "age": {"type": int},   
            "email": {"type": str}  
        },
        "required": ["name", "age", "email"]
    },
    EMAIL_REGEX=r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"):
    """
    Validate the structure and contents of a JSON file against predefined schema rules and retrieve a specified attribute from the JSON object. Ensures that all required fields exist, match their defined types, and checks the validity of the email format using a regular expression.
    
    Parameters:
    file_path (str): The path to the JSON file.
    attribute (str): The attribute to retrieve from the JSON object.
    INPUT_JSON (dict): The input json to validate.
    EMAIL_REGEX (str): The regex used to check the email validity.

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

    for key in INPUT_JSON['required']:
        if key not in data:
            raise ValueError(f'{key} is missing from the JSON object.')
        if not isinstance(data[key], INPUT_JSON['properties'][key]['type']):
            raise ValueError(f'{key} is not of type {INPUT_JSON["properties"][key]["type"]}.')

    if 'email' in data and not re.fullmatch(EMAIL_REGEX, data['email']):
        raise ValueError('Email is not valid.')

    return data[attribute]

import unittest
import json
import os
import re

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        # Creating a dummy JSON file
        self.filepath = '/tmp/test_data.json'
        self.valid_data = {
            "name": "John Doe",
            "age": 30,
            "email": "john.doe@example.com"
        }
        self.invalid_email_data = {
            "name": "John Doe",
            "age": 30,
            "email": "johndoe@example"
        }
        with open(self.filepath, 'w') as file:
            json.dump(self.valid_data, file)
    
    def tearDown(self):
        # Remove the dummy JSON file after the test
        os.remove(self.filepath)

    def test_case_valid_json(self):
        # Test with valid JSON data
        result = f_1029(self.filepath, 'name')
        self.assertEqual(result, "John Doe")
    
    def test_case_invalid_email_format(self):
        # Overwrite with invalid email format data and test
        with open(self.filepath, 'w') as file:
            json.dump(self.invalid_email_data, file)
        with self.assertRaises(ValueError):
            f_1029(self.filepath, 'email')
    
    def test_case_missing_attribute(self):
        # Test with JSON missing a required attribute by removing 'age'
        modified_data = self.valid_data.copy()
        del modified_data['age']
        with open(self.filepath, 'w') as file:
            json.dump(modified_data, file)
        with self.assertRaises(ValueError):
            f_1029(self.filepath, 'age')
    
    def test_case_retrieve_age(self):
        # Test retrieving age from valid JSON
        result = f_1029(self.filepath, 'age')
        self.assertEqual(result, 30)

    def test_case_non_existent_file(self):
        # Test with non-existent file path
        with self.assertRaises(ValueError):
            f_1029('/tmp/non_existent.json', 'name')

if __name__ == "__main__":
    run_tests()