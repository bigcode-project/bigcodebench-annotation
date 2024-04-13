import pandas as pd

def f_176(sales_data_dict):
    """
    Generate a sales report from the specified dictionary.
    
    Parameters:
    sales_data_dict (dict): A dictionary where keys are categories and values are sales.

    Returns:
    DataFrame: A pandas DataFrame with sales data. It should have 2 columns : 'Category' and 'Sales'.
    
    Requirements:
    - pandas
    
    Example:
    >>> sales_data = {'Electronics': 5000, 'Clothing': 4000, 'Groceries': 3000, 'Books': 2000, 'Sports': 1000}
    >>> report = f_176(sales_data)
    >>> print(report)
              Category  Sales
    0     Electronics   5000
    1        Clothing   4000
    2       Groceries   3000
    3           Books   2000
    4          Sports   1000
    """
    report_df = pd.DataFrame(list(sales_data_dict.items()), columns=['Category', 'Sales'])
    return report_df

import unittest
import pandas as pd

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    """Test cases for the f_176 function."""
    def test_case_1(self):
        sales_data = {'Electronics': 5000, 'Clothing': 4000, 'Groceries': 3000, 'Books': 2000, 'Sports': 1000}
        expected_df = pd.DataFrame(
            {
                'Category': ['Electronics', 'Clothing', 'Groceries', 'Books', 'Sports'], 
                'Sales': [5000, 4000, 3000, 2000, 1000]
            }
        )
        result_df = f_176(sales_data)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_case_2(self):
        sales_data = {'Books': 500, 'Sports': 600}
        expected_df = pd.DataFrame({'Category': ['Books', 'Sports'], 'Sales': [500, 600]})
        result_df = f_176(sales_data)
        pd.testing.assert_frame_equal(result_df, expected_df)
        
    def test_case_3(self):
        sales_data = {'Electronics': 15000}
        expected_df = pd.DataFrame({'Category': ['Electronics'], 'Sales': [15000]})
        result_df = f_176(sales_data)
        pd.testing.assert_frame_equal(result_df, expected_df)
        
    def test_case_4(self):
        sales_data = {}
        expected_df = pd.DataFrame(
            {
                'Category': pd.Series([], dtype='object'), 
                'Sales': pd.Series([], dtype='object')
            },
        )
        result_df = f_176(sales_data)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_case_5(self):
        sales_data = {'Clothing': 9000, 'Groceries': 5000, 'Sports': 100}
        expected_df = pd.DataFrame({'Category': ['Clothing', 'Groceries', 'Sports'], 'Sales': [9000, 5000, 100]})
        result_df = f_176(sales_data)
        pd.testing.assert_frame_equal(result_df, expected_df)

if __name__ == "__main__" :
    run_tests()