import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def f_174(data):
    """
    Pre-processes the given product data by normalizing the 'Sales' and 'Profit' columns and visualizes the normalized data using a bar chart.
    
    Parameters:
    data (dict): A dictionary containing product data. The dictionary should have the following format:
                 {
                     'Name': [list of product names],
                     'Sales': [list of sales figures],
                     'Profit': [list of profit figures]
                 }
    
    Returns:
    tuple: A tuple containing:
        - DataFrame: The preprocessed dataframe with normalized 'Sales' and 'Profit' columns.
        - Axes: The matplotlib Axes object for the bar chart.

    Requirements:
    - pandas
    - sklearn.preprocessing
    - matplotlib

    Example:
    >>> data = {
    ...     'Name': ['Product A', 'Product B'],
    ...     'Sales': [1000, 2000],
    ...     'Profit': [200, 500]
    ... }
    >>> df, ax = f_174(data)
    >>> df
           Name     Sales    Profit
    0  Product A  0.0      0.0
    1  Product B  1.0      1.0
    """
    df = pd.DataFrame(data)
    
    scaler = MinMaxScaler()
    df[['Sales', 'Profit']] = scaler.fit_transform(df[['Sales', 'Profit']])
    
    ax = df.plot(x='Name', y=['Sales', 'Profit'], kind='bar', legend=True, figsize=(10, 6))
    ax.set_ylabel("Normalized Values")
    ax.set_title("Normalized Sales and Profit Data")
    
    return df, ax

import unittest
import numpy as np

class TestCases(unittest.TestCase):
    """Test cases for the f_174 function."""
    def test_case_1(self):
        test_data = {
            "Name" : ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
            "Sales" : [100, 200, 300, 400, 500],
            "Profit" : [20, 10, 0, 10, 20]
        }
        df, ax = f_174(test_data)
        self.assertEqual(df.shape, (5, 3))
        self.assertListEqual(list(df.columns), ['Name', 'Sales', 'Profit'])
        self.assertTrue(df['Sales'].max() <= 1)
        self.assertTrue(df['Sales'].min() >= 0)
        self.assertTrue(df['Profit'].max() <= 1)
        self.assertTrue(df['Profit'].min() >= 0)
        self.assertEqual(ax.get_title(), "Normalized Sales and Profit Data")
        
        self.assertTrue(np.allclose(np.array([0.00, 0.25, 0.50, 0.75, 1.00]), df['Sales'].values))
        self.assertTrue(np.allclose(np.array([1.0, 0.5, 0.0, 0.5, 1.0]), df['Profit'].values))
    
    def test_case_2(self):
        test_data = {
            'Name': ['Product A', 'Product B'],
            'Sales': [1000, 2000],
            'Profit': [200, 500]
        }
        df, ax = f_174(test_data)
        self.assertEqual(df.shape, (2, 3))
        self.assertTrue(df['Sales'].max() <= 1)
        self.assertTrue(df['Sales'].min() >= 0)
        self.assertTrue(df['Profit'].max() <= 1)
        self.assertTrue(df['Profit'].min() >= 0)
        
    def test_case_3(self):
        test_data = {
            'Name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G'],
            'Sales': [1000, 2000, 3000, 4000, 5000, 6000, 7000],
            'Profit': [200, 500, 800, 1000, 1200, 1500, 1800]
        }
        df, ax = f_174(test_data)
        self.assertEqual(df.shape, (7, 3))
        self.assertTrue(df['Sales'].max() <= 1)
        self.assertTrue(df['Sales'].min() >= 0)
        self.assertTrue(df['Profit'].max() <= 1)
        self.assertTrue(df['Profit'].min() >= 0)
        
    def test_case_4(self):
        test_data = {
            'Name': ['Product A', 'Product B', 'Product C'],
            'Sales': [2000, 2000, 2000],
            'Profit': [500, 500, 500]
        }
        df, ax = f_174(test_data)
        self.assertEqual(df.shape, (3, 3))
        self.assertTrue(df['Sales'].max() <= 1)
        self.assertTrue(df['Sales'].min() >= 0)
        self.assertTrue(df['Profit'].max() <= 1)
        self.assertTrue(df['Profit'].min() >= 0)
        
    def test_case_5(self):
        test_data = {
            'Name': ['Product A', 'Product B', 'Product C'],
            'Sales': [1000, 2000, 3000],
            'Profit': [-200, 0, 800]
        }
        df, ax = f_174(test_data)
        self.assertEqual(df.shape, (3, 3))
        self.assertTrue(df['Sales'].max() <= 1)
        self.assertTrue(df['Sales'].min() >= 0)
        self.assertTrue(df['Profit'].max() <= 1)
        self.assertTrue(df['Profit'].min() >= 0)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__" :
    run_tests()