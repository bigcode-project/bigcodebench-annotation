import pandas as pd
from random import randint
from statistics import mean

def f_488(products_list):
    """
    Generate a DataFrame of sales data for a list of products.
    
    Functionality:
    This function takes in a list of product names and generates random sales data for each product over a period of 12 months.
    It then calculates the average sales for each product and returns the results as a pandas DataFrame.
    
    Parameters:
    products_list (list): A list of product names.
    
    Returns:
    DataFrame: A pandas DataFrame with columns: 'Product', 'Month 1', 'Month 2', ..., 'Month 12', 'Average Sales'.
    
    Requirements:
    - pandas
    - random
    - statistics
    
    Example:
    >>> products = ['Apples', 'Bananas', 'Grapes', 'Oranges', 'Pineapples']
    >>> sales_data = f_488(products)
    >>> print(sales_data)
    """
    sales_data = []

    for product in products_list:
        sales = [randint(100, 500) for _ in range(12)]
        avg_sales = mean(sales)
        sales.append(avg_sales)
        sales_data.append([product] + sales)

    sales_df = pd.DataFrame(sales_data, columns=['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales'])

    return sales_df

import unittest
import pandas as pd

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a single product
        products = ["Apples"]
        sales_data = f_488(products)
        
        # Checking if returned DataFrame has the correct structure
        expected_columns = ['Product'] + [f'Month {i+1}' for i in range(12)] + ['Average Sales']
        self.assertEqual(list(sales_data.columns), expected_columns)
        
        # Checking the correctness of average sales
        avg_sales = sales_data['Average Sales'].iloc[0]
        self.assertAlmostEqual(avg_sales, sales_data.iloc[0, 1:13].mean(), places=2)
        
        # Checking if sales values are within the expected range
        self.assertTrue((sales_data.iloc[0, 1:13] >= 100).all() and (sales_data.iloc[0, 1:13] <= 500).all())

    def test_case_2(self):
        # Test with multiple products
        products = ["Apples", "Bananas", "Grapes"]
        sales_data = f_488(products)
        self.assertEqual(len(sales_data), 3)

    def test_case_3(self):
        # Test with no products
        products = []
        sales_data = f_488(products)
        self.assertEqual(len(sales_data), 0)

    def test_case_4(self):
        # Test with a long product name
        products = ["A" * 100]
        sales_data = f_488(products)
        self.assertEqual(sales_data['Product'].iloc[0], "A" * 100)

    def test_case_5(self):
        # Test with products having special characters
        products = ["@pples", "!Bananas", "#Grapes"]
        sales_data = f_488(products)
        self.assertTrue(all(item in sales_data['Product'].tolist() for item in products))


if __name__ == "__main__":
    run_tests()