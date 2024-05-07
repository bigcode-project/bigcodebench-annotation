import pandas as pd
import numpy as np


def f_853(product_dict, product_keys):
    """
    Create a profit report for a list of products based on a specific product dictionary that includes the quantity,
    price, and profit of each product. Additionally, calculate the average price and profit for all considered products,
    and plot a bar chart of the profit for each product.

    Parameters:
    - product_dict (dict): The dictionary containing product details with product name as key and a list
    [quantity, price] as value.
    - product_keys (list): The list of product keys to consider for the report.

    Returns: tuple: A tuple containing:
    - DataFrame: A pandas DataFrame with columns
    ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit'].
    - Axes: A matplotlib Axes object representing the plotted bar chart of profit for each product
    (None if no products).

    Requirements:
    - pandas
    - numpy

    Example:
    >>> product_dict = {'Apple': [100, 2.5], 'Orange': [80, 3.5], 'Banana': [120, 1.5]}
    >>> product_keys = ['Apple', 'Banana']
    >>> report, ax = f_853(product_dict, product_keys)
    >>> print(report)
      Product  Quantity  Price  Profit  Average Price  Average Profit
    0   Apple       100    2.5   250.0            2.0           215.0
    1  Banana       120    1.5   180.0            2.0           215.0

    """
    columns = ['Product', 'Quantity', 'Price', 'Profit']
    data = []
    for key in product_keys:
        quantity, price = product_dict[key]
        profit = quantity * price
        data.append([key, quantity, price, profit])
    df = pd.DataFrame(data, columns=columns)
    if not df.empty:
        avg_price = np.mean(df['Price'])
        avg_profit = np.mean(df['Profit'])
        df['Average Price'] = avg_price
        df['Average Profit'] = avg_profit
        ax = df.plot(x='Product', y='Profit', kind='bar', legend=False, title="Profit for each product")
        ax.set_ylabel("Profit")
    else:
        ax = None
    return df, ax

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        # Setup common to all tests: A product dictionary
        self.product_dict = {
            'Apple': [100, 2.5],
            'Orange': [80, 3.5],
            'Banana': [120, 1.5]
        }
    def test_case_1(self):
        # Test with a single product
        product_keys = ['Apple']
        report, ax = f_853(self.product_dict, product_keys)
        self.assertEqual(len(report), 1)  # Should return 1 row
        self.assertIn('Apple', report['Product'].values)
        self.assertAlmostEqual(report['Average Price'].iloc[0], 2.5)
        self.assertAlmostEqual(report['Average Profit'].iloc[0], 250.0)
    def test_case_2(self):
        # Test with multiple products
        product_keys = ['Apple', 'Orange']
        report, ax = f_853(self.product_dict, product_keys)
        self.assertEqual(len(report), 2)  # Should return 2 rows
        self.assertTrue(all(item in ['Apple', 'Orange'] for item in report['Product'].values))
        expected_avg_price = (2.5 + 3.5) / 2
        expected_avg_profit = (250.0 + 280.0) / 2
        self.assertTrue(all(report['Average Price'] == expected_avg_price))
        self.assertTrue(all(report['Average Profit'] == expected_avg_profit))
    def test_case_3(self):
        # Test with no products
        product_keys = []
        report, ax = f_853(self.product_dict, product_keys)
        self.assertTrue(report.empty)  # Should return an empty DataFrame
    def test_case_4(self):
        # Test with a product that doesn't exist in the dictionary
        product_keys = ['Mango']  # Mango is not in product_dict
        with self.assertRaises(KeyError):
            f_853(self.product_dict, product_keys)
    def test_case_5(self):
        # Test the DataFrame structure
        product_keys = ['Apple', 'Banana']
        report, ax = f_853(self.product_dict, product_keys)
        expected_columns = ['Product', 'Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']
        self.assertEqual(list(report.columns), expected_columns)
        for col in ['Quantity', 'Price', 'Profit', 'Average Price', 'Average Profit']:
            self.assertTrue(pd.api.types.is_numeric_dtype(report[col]), f"{col} should be numeric type")
