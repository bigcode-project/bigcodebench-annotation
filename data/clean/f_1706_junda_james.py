import pandas as pd
import numpy as np
import itertools
from datetime import datetime, timedelta
import seaborn as sns

def f_1706(df, fruits=None, days=None, seed=None, sales_lower_bound=1, sales_upper_bound=50):
    """
    Appends randomly generated sales data for specified fruits over a given range of days to a DataFrame, 
    and returns a seaborn boxplot of the sales.

    Parameters:
    - df (pd.DataFrame): Initial Empty DataFrame to append sales data to. Must be empty. 
    - fruits (List[str], optional): List of fruits for sales data. Defaults to ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry'].
    - days (List[datetime], optional): List of days for sales data. Defaults to the range from January 1, 2024, to January 7, 2024.
    - seed (int, optional): Seed for the random number generator. Defaults to None.
    - sales_lower_bound (int, optional): Lower bound for random sales values. Defaults to 1.
    - sales_upper_bound (int, optional): Upper bound for random sales values. Defaults to 50.

    Returns:
    Tuple[pd.DataFrame, sns.axisgrid.FacetGrid]: Updated DataFrame with sales data and a seaborn boxplot of the sales.

    Raises:
    TypeError: If 'df' is not a pandas DataFrame.
    ValueError: If 'df' is not empty or  If 'sales_lower_bound' is not less than 'sales_upper_bound'.

    Requirements:
    - pandas 
    - numpy
    - itertools
    - datetime
    - seaborn

    Example:
    >>> initial_df = pd.DataFrame()
    >>> report_df, plot = f_1706(initial_df, seed=42)
    >>> print(report_df.head())
       Fruit        Day  Sales
    0  Apple 2024-01-01     39
    1  Apple 2024-01-02     29
    2  Apple 2024-01-03     15
    3  Apple 2024-01-04     43
    4  Apple 2024-01-05      8
    >>> plot.figure.show()

    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    if not df.empty:
        raise ValueError("Input DataFrame must be empty")
    if sales_lower_bound >= sales_upper_bound:
        raise ValueError("sales_lower_bound must be less than sales_upper_bound")

    if fruits is None:
        fruits = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    if days is None:
        # Set days to range from January 1, 2024, to January 7, 2024
        days = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(7)]

    if seed is not None:
        np.random.seed(seed)

    data = list(itertools.product(fruits, days))
    sales_data = pd.DataFrame(data, columns=['Fruit', 'Day'])
    sales_data['Sales'] = np.random.randint(sales_lower_bound, sales_upper_bound, size=len(data))

    result_df = pd.concat([df, sales_data])
    plot = sns.boxplot(x='Fruit', y='Sales', data=result_df)

    return result_df, plot

import unittest
import pandas as pd
import numpy as np
from datetime import datetime

class TestCases(unittest.TestCase):
    def setUp(self):
        # Define the default date range for comparison in tests
        self.default_days = [datetime(2024, 1, 1) + timedelta(days=x) for x in range(7)]

    def test_default_days_range(self):
        """Test the default days range is correctly applied."""
        initial_df = pd.DataFrame()
        report_df, _ = f_1706(initial_df, seed=42)
        unique_days = sorted(report_df['Day'].dt.date.unique())
        expected_days = [day.date() for day in self.default_days]
        self.assertEqual(len(unique_days), len(expected_days), "The number of unique days should match the default range.")
        for day in unique_days:
            self.assertIn(day, expected_days, "Each unique day should be within the default range.")

    def test_custom_days_range(self):
        """Test functionality with a custom days range."""
        initial_df = pd.DataFrame()
        custom_days = [datetime(2024, 1, 10), datetime(2024, 1, 11)]
        report_df, _ = f_1706(initial_df, days=custom_days, seed=42)
        unique_days = sorted(report_df['Day'].dt.date.unique())
        expected_custom_days = [day.date() for day in custom_days]
        self.assertEqual(len(unique_days), len(expected_custom_days), "The number of unique days should match the custom range.")
        for day in unique_days:
            self.assertIn(day, expected_custom_days, "Each unique day should be within the custom range.")


    def test_sales_bounds(self):
        """Test custom sales bounds are respected."""
        initial_df = pd.DataFrame()
        report_df, _ = f_1706(initial_df, seed=42, sales_lower_bound=20, sales_upper_bound=30)
        sales_values = report_df['Sales'].unique()
        self.assertTrue(all(20 <= val < 30 for val in sales_values), "All sales values should be within the specified bounds.")

    def test_invalid_sales_bounds(self):
        """Test error handling for invalid sales bounds."""
        with self.assertRaises(ValueError):
            f_1706(pd.DataFrame(), sales_lower_bound=50, sales_upper_bound=10)

    def test_with_non_dataframe_input(self):
        """Test that providing a non-DataFrame input raises a TypeError."""
        with self.assertRaises(TypeError):
            f_1706("not_a_dataframe")

    def test_reproducibility_with_seed(self):
        """Test reproducibility of sales data generation with a fixed seed."""
        initial_df = pd.DataFrame()
        df1, _ = f_1706(initial_df, seed=42)
        df2, _ = f_1706(initial_df, seed=42)
        pd.testing.assert_frame_equal(df1, df2, "DataFrames generated with the same seed should be identical.")
        
    def test_with_custom_fruits_and_days(self):
        fruits = ['Mango', 'Pineapple']
        days = [pd.Timestamp('2023-01-01'), pd.Timestamp('2023-01-02')]
        initial_df = pd.DataFrame()
        report_df, plot = f_1706(initial_df, fruits=fruits, days=days, sales_lower_bound=1, sales_upper_bound=50, seed=42)

        self.assertEqual(len(report_df['Fruit'].unique()), len(fruits), "Number of unique fruits should match the input")
        self.assertEqual(len(report_df['Day'].unique()), len(days), "Number of unique days should match the input")
        self.assertTrue(hasattr(plot, 'figure'), "Plot object should have a 'figure' attribute")

        # Convert DataFrame to a list of strings for each row
        df_list = report_df.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()

        # Check if the converted list matches the expected output 
        expect_output = ['Mango,2023-01-01 00:00:00,39', 'Mango,2023-01-02 00:00:00,29', 'Pineapple,2023-01-01 00:00:00,15', 'Pineapple,2023-01-02 00:00:00,43']
        self.assertAlmostEqual(df_list, expect_output, "DataFrame contents should match the expected output")
    
    def test_error_on_non_empty_dataframe(self):
        """Test that a ValueError is raised if the input DataFrame is not empty."""
        # Create a non-empty DataFrame
        non_empty_df = pd.DataFrame({'A': [1, 2, 3]})
        
        # Attempt to call f_1706 with a non-empty DataFrame and check for ValueError
        with self.assertRaises(ValueError) as context:
            f_1706(non_empty_df, seed=42)
        
        # Optionally, check the error message to ensure it's for the non-empty DataFrame condition
        self.assertTrue("Input DataFrame must be empty" in str(context.exception), "Function should raise ValueError for non-empty DataFrame input.")

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
