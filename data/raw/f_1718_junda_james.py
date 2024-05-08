import numpy as np
import pandas as pd

def f_1718(products, n_samples=100, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42):
    """
    Generate a sales report with randomly simulated sales and profit data for a given list of products.
    The data is aggregated by product and sorted by total profit in descending order. 
    
    Parameters:
    - products (list of str): List of product names.
    - n_samples (int): The number of data points to generate for the report. Default is 100.
    - sales_lower (int): The minimum sales value for the random generation. Default is 50.
    - sales_upper (int): The maximum sales value for the random generation. Default is 200.
    - profit_margin_min (float): The minimum profit margin as a fraction of sales. Default is 0.1.
    - profit_margin_max (float): The maximum profit margin as a fraction of sales. Default is 0.5.
    - random_seed (int): Seed for the random number generator to ensure reproducibility. Default is 42.

    Returns:
    pd.DataFrame: A DataFrame containing aggregated sales and profit data for each product, sorted by profit.

    Raises:
    ValueError: If n_samples is not a positive integer, or if sales_lower is greater than sales_upper.
    TypeError: If products is not a list of strings, or if sales_lower, sales_upper, profit_margin_min, or profit_margin_max are not numeric.

    Requirements:
    - numpy
    - pandas

    Example:
    >>> products = ["iPhone", "iPad", "Macbook", "Airpods", "Apple Watch"]
    >>> report = f_1718(products, n_samples=50, sales_lower=100, sales_upper=150, profit_margin_min=0.2, profit_margin_max=0.4, random_seed=42)
    >>> print(report)
           Product  Sales      Profit
    2      Macbook   1561  444.826709
    3         iPad   1383  401.925334
    0      Airpods   1297  381.482713
    1  Apple Watch   1123  308.078536
    4       iPhone    921  294.013887
    """
    np.random.seed(random_seed)
    
    if not products:
        return pd.DataFrame(columns=["Product", "Sales", "Profit"])

    if not isinstance(products, list) or not all(isinstance(product, str) for product in products):
        raise TypeError("products must be a list of strings.")
    if not isinstance(n_samples, int) or n_samples <= 0:
        raise ValueError("n_samples must be a positive integer.")
    if not (isinstance(sales_lower, int) and isinstance(sales_upper, int)) or sales_lower >= sales_upper:
        raise ValueError("sales_lower must be less than sales_upper and both must be integers.")
    if not all(isinstance(x, (int, float)) for x in [profit_margin_min, profit_margin_max]) or profit_margin_min >= profit_margin_max:
        raise ValueError("profit_margin_min must be less than profit_margin_max and both must be numeric.")

    data = []
    for _ in range(n_samples):
        product = np.random.choice(products)
        sales = np.random.randint(sales_lower, sales_upper + 1)
        profit = sales * np.random.uniform(profit_margin_min, profit_margin_max)
        data.append([product, sales, profit])

    df = pd.DataFrame(data, columns=["Product", "Sales", "Profit"])
    df = df.groupby("Product", as_index=False).sum()
    df.sort_values("Profit", ascending=False, inplace=True)

    return df

import pandas as pd
import unittest

class TestCases(unittest.TestCase):

    def test_random_reproducibility(self):
        report1 = f_1718(["iPhone", "iPad"], n_samples=50, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42)
        report2 = f_1718(["iPhone", "iPad"], n_samples=50, sales_lower=50, sales_upper=200, profit_margin_min=0.1, profit_margin_max=0.5, random_seed=42)
        pd.testing.assert_frame_equal(report1, report2)

    def test_number_of_rows(self):
        report = f_1718(["iPhone", "iPad"], n_samples=50, sales_lower=50, sales_upper=200)
        self.assertEqual(len(report), len(set(["iPhone", "iPad"])))

    def test_sorting_by_profit(self):
        report = f_1718(["iPhone", "iPad"], sales_lower=50, sales_upper=200)
        self.assertTrue(report["Profit"].is_monotonic_decreasing)

    def test_custom_parameters(self):
        report = f_1718(["iPhone", "iPad", "Macbook", "Airpods", "Apple Watch"], n_samples=50, sales_lower=100, sales_upper=150, profit_margin_min=0.2, profit_margin_max=0.4, random_seed=42)
        # This test needs to be adjusted based on the expected outcome of the custom parameters.
        # Specific checks on DataFrame contents should account for the randomness and reproducibility aspects.
        self.assertTrue(len(report) > 0, "The report should contain aggregated sales and profit data.")
        
    def test_new_custom_parameters(self):
        report1 = f_1718(["iPhone", "iPad", "Macbook", "Airpods", "Apple Watch"], n_samples=50, sales_lower=100, sales_upper=150, profit_margin_min=0.2, profit_margin_max=0.4, random_seed=42)
        df_list = report1.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        expect = ['Macbook,1561,444.82670855378143', 'iPad,1383,401.9253335536443', 'Airpods,1297,381.4827132170069', 'Apple Watch,1123,308.07853599252707', 'iPhone,921,294.0138866107959']

        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")
    
    def test_sales_bounds_validation(self):
        """Test that an error is raised if sales_lower is greater than sales_upper."""
        with self.assertRaises(ValueError):
            f_1718(["Product1"], sales_lower=250, sales_upper=100)

    def test_profit_margin_validation(self):
        """Test that an error is raised if profit_margin_min is greater than or equal to profit_margin_max."""
        with self.assertRaises(ValueError):
            f_1718(["Product1"], profit_margin_min=0.6, profit_margin_max=0.5)

    def test_product_list_validation(self):
        """Test that an error is raised if the products list is not a list of strings."""
        with self.assertRaises(TypeError):
            f_1718([123, 456], n_samples=10)

    def test_n_samples_validation(self):
        """Test that an error is raised if n_samples is not a positive integer."""
        with self.assertRaises(ValueError):
            f_1718(["Product1"], n_samples=-10)

    def test_empty_product_list(self):
        """Test that the function can handle an empty product list."""
        report = f_1718([], n_samples=10)
        self.assertTrue(report.empty, "The report should be empty if no products are provided.")

    def test_zero_samples(self):
        """Test handling of zero samples."""
        with self.assertRaises(ValueError):
            f_1718(["Product1"], n_samples=-10)

    def test_single_product_reproducibility(self):
        """Test that the function generates consistent results for a single product across multiple runs."""
        report1 = f_1718(["Product1"], n_samples=10, random_seed=42)
        report2 = f_1718(["Product1"], n_samples=10, random_seed=42)
        pd.testing.assert_frame_equal(report1, report2)


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
