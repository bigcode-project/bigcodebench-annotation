import csv
import collections
import operator

def f_1007(csv_file_path):
    """
    Find the best-selling product from a given CSV file with sales data.

    This function assumes that the CSV file contains a header and two columns: 
    'product' and 'quantity', where 'product' is a string representing the product 
    name and 'quantity' is an integer representing the quantity sold.

    Args:
        csv_file_path (str): Path to the CSV file containing sales data.

    Returns:
        str: The name of the top-selling product based on the total quantity sold.

    Requirements:
    - csv
    - collections
    - operator

    Example:
    >>> f_1007("path/to/sales.csv")
    'Product ABC'
    """
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        sales_data = collections.defaultdict(int)
        for row in reader:
            product, quantity = row[0], int(row[1])
            sales_data[product] += quantity

    top_selling_product = max(sales_data.items(), key=operator.itemgetter(1))[0]

    return top_selling_product

import os
import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Given the sales1.csv data, the top selling product is "Product B" with 200 sales
        result = f_1007(os.path.join('test_data', "sales1.csv"))
        self.assertEqual(result, "Product B")

    def test_case_2(self):
        # Given the sales2.csv data, the top selling product is "Product Z" with 120 sales
        result = f_1007(os.path.join('test_data', "sales2.csv"))
        self.assertEqual(result, "Product Z")

    def test_case_3(self):
        # Given the sales3.csv data, the top selling product is "Product M" with 500 sales
        result = f_1007(os.path.join('test_data', "sales3.csv"))
        self.assertEqual(result, "Product M")

    def test_case_4(self):
        # Given the sales4.csv data, which has no products, the function should handle it gracefully
        with self.assertRaises(ValueError):
            f_1007(os.path.join('test_data', "sales4.csv"))

    def test_case_5(self):
        # Given the sales5.csv data, there's only one product "Single Product" with 999 sales
        result = f_1007(os.path.join('test_data', "sales5.csv"))
        self.assertEqual(result, "Single Product")
if __name__ == "__main__":
    run_tests()