import json
import os
import glob


# Constants
KEY = 'mynewkey'
VALUE = 'mynewvalue'

def f_258(directory):
    """
    Add a new key-value pair to all JSON files in a specific directory and save the updated JSON files.
    
    Specifically, the function searches for all JSON files within the provided directory and 
    updates each JSON file by adding a new key-value pair ('mynewkey': 'mynewvalue') if the key 
    doesn't already exist. The function modifies the JSON files in place.

    Parameters:
    directory (str): The directory containing the JSON files.

    Returns:
    int: The number of JSON files updated.

    Requirements:
    - json
    - os
    - glob

    Example:
    >>> f_258('./json_files') # Random test case with no JSON files
    0
    """
    files = glob.glob(os.path.join(directory, '*.json'))
    updated_files = 0

    for file in files:
        with open(file, 'r+') as f:
            data = json.load(f)
            if KEY not in data:
                data[KEY] = VALUE
                f.seek(0)
                f.truncate()
                json.dump(data, f)
                updated_files += 1

    return updated_files


import unittest
import tempfile
import shutil
import doctest


class TestCases(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory after testing
        shutil.rmtree(self.test_dir)

    def test_case_1(self):
        # Create mock JSON files
        file_1 = os.path.join(self.test_dir, "file_1.json")
        file_2 = os.path.join(self.test_dir, "file_2.json")
        
        with open(file_1, 'w') as f:
            json.dump({"name": "Alice"}, f)
        with open(file_2, 'w') as f:
            json.dump({"name": "Bob", "mynewkey": "existingvalue"}, f)

        # Run the function
        updated_files = f_258(self.test_dir)

        # Assert number of updated files
        self.assertEqual(updated_files, 1)

        # Assert content of the updated file
        with open(file_1, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {"name": "Alice", "mynewkey": "mynewvalue"})

        with open(file_2, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {"name": "Bob", "mynewkey": "existingvalue"})

    def test_case_2(self):
        # Create mock JSON files
        file_1 = os.path.join(self.test_dir, "file_3.json")
        file_2 = os.path.join(self.test_dir, "file_4.json")
        
        with open(file_1, 'w') as f:
            json.dump({"id": 1}, f)
        with open(file_2, 'w') as f:
            json.dump({"id": 2}, f)

        # Run the function
        updated_files = f_258(self.test_dir)

        # Assert number of updated files
        self.assertEqual(updated_files, 2)

        # Assert content of the updated files
        with open(file_1, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {"id": 1, "mynewkey": "mynewvalue"})

        with open(file_2, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {"id": 2, "mynewkey": "mynewvalue"})

    def test_case_3(self):
        # No JSON files in the directory
        updated_files = f_258(self.test_dir)
        self.assertEqual(updated_files, 0)

    def test_case_4(self):
        # Create mock JSON files with nested structures
        file_1 = os.path.join(self.test_dir, "file_5.json")
        
        with open(file_1, 'w') as f:
            json.dump({"details": {"name": "Charlie", "age": 30}}, f)

        # Run the function
        updated_files = f_258(self.test_dir)

        # Assert number of updated files
        self.assertEqual(updated_files, 1)

        # Assert content of the updated files
        with open(file_1, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {"details": {"name": "Charlie", "age": 30}, "mynewkey": "mynewvalue"})

    def test_case_5(self):
        # Create mock JSON files with list structures
        file_1 = os.path.join(self.test_dir, "file_6.json")
        
        with open(file_1, 'w') as f:
            json.dump({"items": ["apple", "banana", "cherry"]}, f)

        # Run the function
        updated_files = f_258(self.test_dir)

        # Assert number of updated files
        self.assertEqual(updated_files, 1)

        # Assert content of the updated files
        with open(file_1, 'r') as f:
            data = json.load(f)
            self.assertEqual(data, {"items": ["apple", "banana", "cherry"], "mynewkey": "mynewvalue"})


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    doctest.testmod()
    run_tests()