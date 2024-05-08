import csv
import collections
import operator

def f_7(csv_file_path):
    """
    Find the best-selling product from a given CSV file with sales data.

    This function parses a CSV file assumed to have a header followed by rows containing
    two columns: 'product' and 'quantity'. It computes the total sales per product and
    determines the product with the highest cumulative sales. The CSV file must include
    at least these two columns, where 'product' is the name of the product as a string
    and 'quantity' is the number of units sold as an integer.

    Args:
        csv_file_path (str): The file path to the CSV file containing sales data.

    Returns:
        str: The name of the top-selling product based on the total quantity sold.

    Requirements:
    - csv
    - collections
    - operator

    Example:
    >>> f_7("path/to/sales.csv")
    'Product ABC'
    """
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        sales_data = collections.defaultdict(int)
        for row in reader:
            product, quantity = row[0], int(row[1])
            sales_data[product] += quantity
    top_selling_product = max(sales_data.items(), key=operator.itemgetter(1))[0]
    return top_selling_product

import os
import unittest
import csv
class TestCases(unittest.TestCase):
    def setUp(self):
        # Create a directory for test files if it does not exist
        self.test_dir = os.path.join(os.getcwd(), 'test_data')
        os.makedirs(self.test_dir, exist_ok=True)
    def tearDown(self):
        # Remove all files created in the test directory
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    def test_case_1(self):
        # Correct data, expected top-seller is determined correctly
        self.create_csv('sales1.csv', [['product', 'quantity'], ['Product B', '200'], ['Product A', '100']])
        result = f_7(os.path.join(self.test_dir, "sales1.csv"))
        self.assertEqual(result, "Product B")
    def test_case_2(self):
        # Correct data, expected top-seller is determined correctly
        self.create_csv('sales2.csv', [['product', 'quantity'], ['Product Z', '120'], ['Product Y', '80']])
        result = f_7(os.path.join(self.test_dir, "sales2.csv"))
        self.assertEqual(result, "Product Z")
    def test_case_3(self):
        # Correct data, expected top-seller is determined correctly
        self.create_csv('sales3.csv', [['product', 'quantity'], ['Product M', '500'], ['Product N', '400']])
        result = f_7(os.path.join(self.test_dir, "sales3.csv"))
        self.assertEqual(result, "Product M")
    def test_case_4(self):
        # Empty file with header, expect a ValueError or a graceful handle
        self.create_csv('sales4.csv', [['product', 'quantity']])
        with self.assertRaises(ValueError):
            f_7(os.path.join(self.test_dir, "sales4.csv"))
    def test_case_5(self):
        # Single product data, correct determination
        self.create_csv('sales5.csv', [['product', 'quantity'], ['Single Product', '999']])
        result = f_7(os.path.join(self.test_dir, "sales5.csv"))
        self.assertEqual(result, "Single Product")
    def test_case_6(self):
        # File does not exist, expect FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            f_7(os.path.join(self.test_dir, "nonexistent.csv"))
    def test_case_7(self):
        # Incorrect data types, expect ValueError or graceful handling of conversion failure
        self.create_csv('sales6.csv', [['product', 'quantity'], ['Product A', 'one hundred']])
        with self.assertRaises(ValueError):
            f_7(os.path.join(self.test_dir, "sales6.csv"))
    def create_csv(self, filename, rows):
        # Helper function to create CSV files with given rows
        path = os.path.join(self.test_dir, filename)
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
