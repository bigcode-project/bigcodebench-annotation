import csv
import json
import os


def f_231(file_name):
    """
    Convert a csv file to a json file.
    
    Parameters:
    file_name (str): The name of the csv file.
    
    Returns:
    str: The file name of the created json file.

    Requirements:
    - csv
    - json
    - os

    Raises:
    FileNotFoundError: If the file does not exist.
    
    Example:
    >>> import tempfile
    >>> FILE_NAME = tempfile.NamedTemporaryFile(prefix='report_', suffix='.csv', dir='/tmp').name
    >>> with open(FILE_NAME, 'w', newline='') as csvfile:
    ...     fieldnames = ['id', 'name', 'age']
    ...     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    ...     _ = writer.writeheader()
    ...     _ = writer.writerow({'id': '1', 'name': 'John', 'age': '25'})
    ...     _ = writer.writerow({'id': '2', 'name': 'Doe', 'age': '30'})
    >>> json_file = f_231(FILE_NAME)
    >>> print(json_file.startswith('/tmp/report_') and json_file.endswith('.json'))
    True
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError("File does not exist.")

    data = []

    with open(file_name, 'r') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            data.append(row)

    json_file_name = file_name.split('.')[0] + '.json'

    with open(json_file_name, 'w') as f:
        json.dump(data, f)

    return json_file_name


import unittest
import doctest


class TestCases(unittest.TestCase):
    def setUp(self):
        # Creating sample CSV files for testing
        self.csv_file_1 = "sample_1.csv"
        with open(self.csv_file_1, 'w', newline='') as csvfile:
            fieldnames = ['id', 'name', 'age']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'id': '1', 'name': 'John', 'age': '25'})
            writer.writerow({'id': '2', 'name': 'Doe', 'age': '30'})
            
        self.csv_file_2 = "sample_2.csv"
        with open(self.csv_file_2, 'w', newline='') as csvfile:
            fieldnames = ['product', 'price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'product': 'apple', 'price': '0.5'})
            writer.writerow({'product': 'banana', 'price': '0.3'})

    def tearDown(self):
        # Cleaning up the created files after testing
        os.remove(self.csv_file_1)
        if os.path.exists(self.csv_file_1.split('.')[0] + '.json'):
            os.remove(self.csv_file_1.split('.')[0] + '.json')
        
        os.remove(self.csv_file_2)
        if os.path.exists(self.csv_file_2.split('.')[0] + '.json'):
            os.remove(self.csv_file_2.split('.')[0] + '.json')

    def test_case_1(self):
        # Testing with the first sample CSV
        json_file = f_231(self.csv_file_1)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]['id'], '1')
            self.assertEqual(data[0]['name'], 'John')
            self.assertEqual(data[0]['age'], '25')

    def test_case_2(self):
        # Testing with the second sample CSV
        json_file = f_231(self.csv_file_2)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[0]['product'], 'apple')
            self.assertEqual(data[0]['price'], '0.5')

    def test_case_3(self):
        # Testing with a non-existing file
        with self.assertRaises(FileNotFoundError):
            f_231("non_existing.csv")

    def test_case_4(self):
        # Testing with an empty CSV file
        empty_csv = "empty.csv"
        with open(empty_csv, 'w', newline='') as csvfile:
            pass
        json_file = f_231(empty_csv)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 0)
        os.remove(empty_csv)
        os.remove(empty_csv.split('.')[0] + '.json')

    def test_case_5(self):
        # Testing with a CSV file having only headers
        headers_csv = "headers_only.csv"
        with open(headers_csv, 'w', newline='') as csvfile:
            fieldnames = ['field1', 'field2']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        json_file = f_231(headers_csv)
        self.assertTrue(os.path.exists(json_file))
        with open(json_file, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data), 0)
        os.remove(headers_csv)
        os.remove(headers_csv.split('.')[0] + '.json')


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    doctest.testmod()
    run_tests()
