import pandas as pd
import matplotlib.pyplot as plt

def f_2258(df, category_col, sales_col):
    """
    Generates a bar chart for sales data from a given DataFrame, with a title 'Sales Report by Category',
    and raises an exception if there are duplicate category entries.

    Parameters:
    - df (pandas.DataFrame): DataFrame containing the sales data. It must not be empty, should contain
                             at least one row with numeric sales data, and must not have duplicate 
                             entries in the category column.
    - category_col (str): Column name for the product categories. This column should not contain duplicates.
    - sales_col (str): Column name for the sales figures.

    Returns:
    - matplotlib.axes.Axes: Axes object of the generated bar chart if df is not empty; None otherwise.

    Raises:
    - ValueError: If the DataFrame is empty, lacks numeric sales data, or contains duplicate entries in the category column.

    Requirements:
    - pandas
    - matplotlib

    Example usage:
    >>> df = pd.DataFrame({'Category': ['Electronics', 'Clothing', 'Home', 'Books', 'Sports'], 'Sales': [1000, 1500, 1200, 800, 1100]})
    >>> ax = f_2258(df, 'Category', 'Sales')
    """
    if df.empty or not df[sales_col].dtype.kind in 'biufc':
        raise ValueError("DataFrame is empty, lacks sales data, or sales data is not numeric.")
    
    if df[category_col].duplicated().any():
        raise ValueError("DataFrame contains duplicate entries in the category column.")

    ax = df.set_index(category_col)[sales_col].plot(kind='bar', title="Sales Report by Category")
    plt.ylabel('Sales')
    plt.show()
    return ax


import unittest
import pandas as pd

class TestCases(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            'Category': ['Electronics', 'Clothing', 'Home', 'Books', 'Sports'],
            'Sales': [1000, 1500, 1200, 800, 1100]
        })

    def test_sales_data_input(self):
        ax = f_2258(self.df, 'Category', 'Sales')
        self.assertEqual(len(ax.patches), 5)  # 5 bars for 5 categories

    def test_single_category_input(self):
        df_single = self.df.head(1)  # Only one category
        ax = f_2258(df_single, 'Category', 'Sales')
        self.assertEqual(len(ax.patches), 1)  # 1 bar for 1 category

    def test_no_data(self):
        df_empty = pd.DataFrame(columns=['Category', 'Sales'])  # Empty DataFrame
        with self.assertRaises(ValueError):
            ax = f_2258(df_empty, 'Category', 'Sales')

    def test_invalid_columns(self):
        with self.assertRaises(KeyError):
            f_2258(self.df, 'NonexistentCategory', 'Sales')

    def test_duplicate_category_input(self):
        df_duplicate = pd.concat([self.df, self.df]).reset_index(drop=True)
        with self.assertRaises(ValueError):
            f_2258(df_duplicate, 'Category', 'Sales')

def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()