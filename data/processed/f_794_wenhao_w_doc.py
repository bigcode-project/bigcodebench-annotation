import pandas as pd
import numpy as np
import random
from random import randint, seed

# Constants
CATEGORIES = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Toys & Games']

def f_125(mystrings, n_products, seed=0):
    """
    Create a product catalog DataFrame where each row represents a product with the following columns:
    - 'Product Name': The name of the product with spaces replaced by underscores.
    - 'Category': The category to which the product belongs.
    - 'Price': The price of the product, generated randomly based on a normal distribution with a mean of 50 and a standard deviation of 10.
    
    Parameters:
    mystrings (list of str): List of product names.
    n_products (int): Number of products to generate in the catalog.

    Returns:
    pd.DataFrame: A pandas DataFrame containing the product catalog information.

    Requirements:
    - pandas
    - numpy
    - random.randint
    - random.seed

    Constants:
    - CATEGORIES: A list of categories used to randomly assign a category to each product.

    Examples:
    >>> f_125(['Mobile Phone', 'T Shirt', 'Coffee Maker', 'Python Book', 'Toy Car'], 2)
       Product Name        Category  Price
    0   Python_Book           Books  67.64
    1  Mobile_Phone  Home & Kitchen  54.00
    >>> f_125(['Laptop', 'Sweater'], 1)
      Product Name Category  Price
    0      Sweater    Books  67.64
    """
    catalogue_data = []
    random.seed(seed)
    np.random.seed(seed)
    for _ in range(n_products):
        product_name = mystrings[randint(0, len(mystrings) - 1)].replace(' ', '_')
        category = CATEGORIES[randint(0, len(CATEGORIES) - 1)]
        price = round(np.random.normal(50, 10), 2)
        catalogue_data.append([product_name, category, price])
    catalogue_df = pd.DataFrame(catalogue_data, columns=['Product Name', 'Category', 'Price'])
    return catalogue_df

import unittest
from pandas.testing import assert_frame_equal
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        
        result = f_125(['Mobile Phone', 'T Shirt', 'Coffee Maker', 'Python Book', 'Toy Car'], 2, 42)
        # assert the value of the DataFrame
        self.assertEqual(result['Product Name'].tolist(), ['Mobile_Phone', 'Coffee_Maker'])
        self.assertEqual(result['Category'].tolist(), ['Electronics', 'Clothing'])
        self.assertEqual(result['Price'].tolist(), [54.97, 48.62])
        
    def test_case_2(self):
        result = f_125(['Laptop', 'Sweater'], 1)
        self.assertEqual(result['Product Name'].tolist(), ['Sweater'])
        self.assertEqual(result['Category'].tolist(), ['Books'])
        self.assertEqual(result['Price'].tolist(), [67.64])
        
    def test_case_3(self):
        result = f_125(['Book', 'Pen', 'Bag'], 3)
        self.assertEqual(result['Product Name'].tolist(), ['Pen', 'Book', 'Bag'])
        self.assertEqual(result['Category'].tolist(), ['Books', 'Home & Kitchen', 'Books'])
        self.assertEqual(result['Price'].tolist(), [67.64, 54.00, 59.79])
        
    def test_case_4(self):
        result = f_125(['Watch'], 2)
        self.assertEqual(result['Product Name'].tolist(), ['Watch', 'Watch'])
        self.assertEqual(result['Category'].tolist(), ['Books', 'Home & Kitchen'])
        self.assertEqual(result['Price'].tolist(), [67.64, 54.00])
    def test_case_5(self):
        result = f_125(['TV', 'Fridge', 'Sofa', 'Table'], 0)
        self.assertEqual(result.empty, True)
