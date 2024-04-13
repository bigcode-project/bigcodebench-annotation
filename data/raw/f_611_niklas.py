import json
import csv

def f_611(json_file, csv_file):
    """
    Convert a JSON file to CSV.
    
    Parameters:
    - json_file (str): The path to the JSON file.
    - csv_file (str): The path to the CSV file.

    Returns:
    - csv_file: The function returns the path to the CSV file that was written.

    Requirements:
    - json
    - csv
        
    Example:
    >>> f_611('path_to_json_file.json', 'path_to_csv_file.csv')
    """
    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data.keys())
        writer.writerow(data.values())
    
    return csv_file

import unittest
import os

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Create json file
        json_file = './test.json'
        with open(json_file, 'w') as f:
            json.dump({'a': 1, 'b': 2, 'c': 3}, f)
        # Run function
        csv_file = f_611(json_file, './test.csv')
        # Check file
        self.assertTrue(os.path.exists(csv_file))
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        self.assertEqual(csv_data, [['a', 'b', 'c'], ['1', '2', '3']])
        # Remove file
        os.remove(json_file)
        os.remove(csv_file)

    def test_case_2(self):
        # Create json file
        json_file = './test.json'
        with open(json_file, 'w') as f:
            json.dump({'z': 1, 'y': 2, 'x': 3}, f)
        # Run function
        csv_file = f_611(json_file, './test.csv')
        # Check file
        self.assertTrue(os.path.exists(csv_file))
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        self.assertEqual(csv_data, [['z', 'y', 'x'], ['1', '2', '3']])
        # Remove file
        os.remove(json_file)
        os.remove(csv_file)

    def test_case_3(self):
        # Create json file
        json_file = './testx.json'
        with open(json_file, 'w') as f:
            json.dump({'xxx': 99}, f)
        # Run function
        csv_file = f_611(json_file, './testx.csv')
        # Check file
        self.assertTrue(os.path.exists(csv_file))
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        self.assertEqual(csv_data, [['xxx'], ['99']])
        # Remove file
        os.remove(json_file)
        os.remove(csv_file)

    def test_case_4(self):
        # Create json file
        json_file = './testy.json'
        with open(json_file, 'w') as f:
            json.dump({'yyy': 99}, f)
        # Run function
        csv_file = f_611(json_file, './testy.csv')
        # Check file
        self.assertTrue(os.path.exists(csv_file))
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        self.assertEqual(csv_data, [['yyy'], ['99']])
        # Remove file
        os.remove(json_file)
        os.remove(csv_file)

    def test_case_5(self):
        # Create json file
        json_file = './testz.json'
        with open(json_file, 'w') as f:
            json.dump({'zzz': 99}, f)
        # Run function
        csv_file = f_611(json_file, './testz.csv')
        # Check file
        self.assertTrue(os.path.exists(csv_file))
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            csv_data = list(reader)
        self.assertEqual(csv_data, [['zzz'], ['99']])
        # Remove file
        os.remove(json_file)
        os.remove(csv_file)


run_tests()
if __name__ == "__main__":
    run_tests()