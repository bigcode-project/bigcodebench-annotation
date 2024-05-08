import pandas as pd
import collections

def f_172(df):
    """
    Generate a sales report from a DataFrame, excluding duplicate customer names. 
    The report includes total sales and the most popular sales category.

    Parameters:
    df (DataFrame): A pandas DataFrame with columns 'Customer', 'Category', and 'Sales'.

    Returns:
    dict: A dictionary with keys 'Total Sales' (sum of sales) and 'Most Popular Category' (most frequent category).

    Requirements:
    - pandas
    - collections

    Raises:
    - The function will raise a ValueError is input df is not a DataFrame.

    Note:
    - The function would return the first category in alphabetical order for "Most Popular Category' in the case of tie

    Example:
    >>> data = pd.DataFrame([{'Customer': 'John', 'Category': 'Electronics', 'Sales': 500}, {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300}])
    >>> report = f_172(data)
    >>> print(report)
    {'Total Sales': 800, 'Most Popular Category': 'Electronics'}
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame")
    df = df.drop_duplicates(subset='Customer')
    total_sales = df['Sales'].sum()
    popular_category = collections.Counter(df['Category']).most_common(1)[0][0]
    return {'Total Sales': total_sales, 'Most Popular Category': popular_category}

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_regular(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300},
            {'Customer': 'Peter', 'Category': 'Beauty', 'Sales': 400},
            {'Customer': 'Nick', 'Category': 'Sports', 'Sales': 600}
        ])
        expected_output = {'Total Sales': 1800, 'Most Popular Category': 'Electronics'}
        self.assertEqual(f_172(data), expected_output)
    def test_case_with_duplicates(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'John', 'Category': 'Fashion', 'Sales': 200},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300},
            {'Customer': 'Peter', 'Category': 'Beauty', 'Sales': 400}
        ])
        expected_output = {'Total Sales': 1200, 'Most Popular Category': 'Electronics'}
        self.assertEqual(f_172(data), expected_output)
    def test_case_empty(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300}
        ])
        expected_output = {'Total Sales': 800, 'Most Popular Category': 'Electronics'}
        self.assertEqual(f_172(data), expected_output)
    def test_case_unique_customers(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300}
        ])
        expected_output = {'Total Sales': 800, 'Most Popular Category': 'Electronics'}
        self.assertEqual(f_172(data), expected_output)
    def test_case_tie_categories(self):
        data = pd.DataFrame([
            {'Customer': 'John', 'Category': 'Electronics', 'Sales': 500},
            {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300},
            {'Customer': 'Nick', 'Category': 'Home', 'Sales': 200},
            {'Customer': 'Alice', 'Category': 'Electronics', 'Sales': 300}
        ])
        # In case of a tie, the first category in alphabetical order will be chosen
        expected_output = {'Total Sales': 1300, 'Most Popular Category': 'Electronics'}
        self.assertEqual(f_172(data), expected_output)
    def test_case_6(self):
        with self.assertRaises(ValueError):
            f_172("non_df")
