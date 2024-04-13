import collections
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Constants
PRODUCTS = ['apple', 'orange', 'banana', 'grape', 'pear']

def f_194(sales_data):
    """
    Analyze a list of sales data, return summary statistics, and a histogram of sales by product. 

    Parameters:
    sales_data (list): A list of dictionaries where each dictionary represents sales data for a product,
                       e.g., [{'product': 'apple', 'sales': 60}, {'product': 'orange', 'sales': 65}]

    Returns:
    - dict: A dictionary with summary statistics (mean, median, mode) for the sales data. Each key of the dictionary represents a product and the associated value is a dictionary with the keys 'mean', 'median' and 'mode'.
    - matplotlib.figure.Figure: A histogram of sales by product. If there is not product, return None.

    Requirements:
    - collections
    - numpy
    - pandas
    - matplotlib.pyplot

    Example:
    >>> sales_data = [{'product': 'apple', 'sales': 60}, {'product': 'orange', 'sales': 65}]
    >>> stats, fig = f_194(sales_data)
    >>> print(stats)
    >>> fig.show()
    The function uses a predefined list of products:
    PRODUCTS = ['apple', 'orange', 'banana', 'grape', 'pear']

    """
    sales = collections.defaultdict(list)
    for data in sales_data:
        sales[data['product']].append(data['sales'])

    if not sales :
        return {}, None
    summary_stats = {}
    for product in sales:
        sales_array = np.array(sales[product])
        summary_stats[product] = {
            'mean': np.mean(sales_array),
            'median': np.median(sales_array),
            'mode': collections.Counter(sales_array).most_common(1)[0][0]
        }

    product_sales_df = pd.DataFrame([])
    for k in sales :
        additional_rows = pd.DataFrame(
            {k : sales[k]}
        )
        product_sales_df = pd.concat([product_sales_df, additional_rows], axis=0)
    ax = product_sales_df.hist(bins=10)
    fig = ax[0][0].get_figure()
    fig.suptitle('Sales by Product')
    fig.supxlabel('Product')
    fig.supylabel('Sales')
    return summary_stats, fig

import unittest
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    """Test cases for the f_194 function."""   
    def test_case_1(self):
        # Given sales data for two products
        sales_data = [{'product': 'apple', 'sales': 60}, {'product': 'orange', 'sales': 65}]
        stats, fig = f_194(sales_data)
        
        # Asserting the summary statistics
        self.assertEqual(stats['apple']['mean'], 60)
        self.assertEqual(stats['apple']['median'], 60)
        self.assertEqual(stats['apple']['mode'], 60)
        
        self.assertEqual(stats['orange']['mean'], 65)
        self.assertEqual(stats['orange']['median'], 65)
        self.assertEqual(stats['orange']['mode'], 65)
        
        # Asserting properties of the histogram
        self.assertEqual(fig.get_suptitle(), 'Sales by Product')
        self.assertEqual(fig.get_supxlabel(), 'Product')
        self.assertEqual(fig.get_supylabel(), 'Sales')

    def test_case_2(self):
        # Given sales data with multiple entries for a product
        sales_data = [{'product': 'apple', 'sales': 60}, {'product': 'apple', 'sales': 70}, {'product': 'banana', 'sales': 40}]
        stats, fig = f_194(sales_data)
        
        # Asserting the summary statistics
        self.assertEqual(stats['apple']['mean'], 65)
        self.assertEqual(stats['apple']['median'], 65)
        self.assertEqual(stats['apple']['mode'], 60) # Mode is the most frequent value
        
        self.assertEqual(stats['banana']['mean'], 40)
        self.assertEqual(stats['banana']['median'], 40)
        self.assertEqual(stats['banana']['mode'], 40)
        
        # Asserting properties of the histogram
        self.assertEqual(fig.get_suptitle(), 'Sales by Product')
        self.assertEqual(fig.get_supxlabel(), 'Product')
        self.assertEqual(fig.get_supylabel(), 'Sales')
        
    

    def test_case_3(self):
        # Given sales data for all products
        sales_data = [
            {'product': 'apple', 'sales': 60}, {'product': 'orange', 'sales': 55}, 
            {'product': 'banana', 'sales': 40}, {'product': 'grape', 'sales': 70}, 
            {'product': 'pear', 'sales': 50}
        ]
        stats, fig = f_194(sales_data)
        
        # Asserting the summary statistics
        self.assertEqual(stats['apple']['mean'], 60)
        self.assertEqual(stats['orange']['mean'], 55)
        self.assertEqual(stats['banana']['mean'], 40)
        self.assertEqual(stats['grape']['mean'], 70)
        self.assertEqual(stats['pear']['mean'], 50)
        
    def test_case_4(self):
        # Given sales data with zero sales for a product
        sales_data = [{'product': 'apple', 'sales': 0}]
        stats, fig = f_194(sales_data)
        
        # Asserting the summary statistics
        self.assertEqual(stats['apple']['mean'], 0)
        self.assertEqual(stats['apple']['median'], 0)
        self.assertEqual(stats['apple']['mode'], 0)
        
    def test_case_5(self):
        # Given sales data with missing products
        sales_data = [{'product': 'apple', 'sales': 60}, {'product': 'banana', 'sales': 40}]
        stats, fig = f_194(sales_data)
        
        # Asserting the summary statistics
        self.assertEqual(stats['apple']['mean'], 60)
        self.assertEqual(stats['banana']['mean'], 40)
        
    def test_case_6(self):
        # Given empty sales data
        sales_data = []
        stats, fig = f_194(sales_data)
        
        # Asserting the summary statistics
        self.assertDictEqual(stats, {})
        self.assertIsNone(fig)
        
    def test_case_7(self):
        # Given sales data with negative sales values
        sales_data = [{'product': 'apple', 'sales': -10}]
        stats, fig = f_194(sales_data)
        
        # Asserting the summary statistics
        self.assertEqual(stats['apple']['mean'], -10)
        self.assertEqual(stats['apple']['median'], -10)
        self.assertEqual(stats['apple']['mode'], -10)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__" :
    run_tests()
