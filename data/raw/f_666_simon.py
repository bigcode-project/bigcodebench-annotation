import pandas as pd
import csv
import random

def f_666(
    n, 
    countries=['USA', 'UK', 'China', 'India', 'Germany'], 
    products=['Product A', 'Product B', 'Product C', 'Product D', 'Product E'], 
    output_path=None,
    random_seed=None):
    """
    Generate random sales data and return it as a pandas DataFrame.
    The sales data has the columns 'Country', 'Product' and 'Sales'.
    Country and Product get sampled from the provided lists / the default values.
    Sales is populated by generating random integers between 1 and 100.
    If an output_path is provided, the generated data is saved to a csv file.

    Parameters:
    n (int): The number of sales records to generate.
    countries (list, optional): List of countries for sales data generation. Defaults to ['USA', 'UK', 'China', 'India', 'Germany'].
    products (list, optional): List of products for sales data generation. Defaults to ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'].
    output_path (str, optional): Path to save the generated sales data as a CSV file. If not provided, the data will not be saved to a file.
    random_seed (int): Seed for rng. Used in generating the sales data. 

    Returns:
    DataFrame: A pandas DataFrame with the generated sales data.

    Requirements:
    - pandas
    - csv
    - random

    Example:
    >>> df = f_666(5)
    >>> print(df)
    Country    Product  Sales
    0   India  Product B     50
    1      UK  Product C     27
    2      UK  Product A      1
    3      UK  Product E     49
    4      UK  Product E      6

    >>> df = f_666(7, products=['tea', 'coffee'], countries=['Austria', 'Australia'])
    >>> print(df)
            Country Product  Sales
    0    Austria  coffee     88
    1    Austria  coffee     69
    2    Austria  coffee     30
    3  Australia  coffee     56
    4  Australia     tea      1
    5    Austria     tea     55
    6    Austria     tea     61
    """
    
    random.seed(random_seed)
    
    sales_data = []
    
    for _ in range(n):
        country = random.choice(countries)
        product = random.choice(products)
        sales = random.randint(1, 100)
        sales_data.append({'Country': country, 'Product': product, 'Sales': sales})

    # If an output path is provided, save the data to a CSV file
    if output_path:
        with open(output_path, 'w', newline='') as csvfile:
            fieldnames = ['Country', 'Product', 'Sales']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(sales_data)
        
    return pd.DataFrame(sales_data)

import unittest
from faker import Faker
import pandas as pd
import os

fake = Faker()

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def setUp(self):
        # Setting up a temporary directory to save CSV files during tests
        self.temp_dir = "temp_test_dir"
        os.makedirs(self.temp_dir, exist_ok=True)

    def test_rng(self):
        'rng reproducability'
        df1 = f_666(100, random_seed=1)
        df2 = f_666(100, random_seed=1)

        self.assertTrue(pd.testing.assert_frame_equal(df1, df2) is None)

    def test_case_1(self):
        'default values'
        df = f_666(100, random_seed=12)
        self.assertEqual(len(df), 100)
        self.assertTrue(set(df["Country"].unique()).issubset(set(['USA', 'UK', 'China', 'India', 'Germany'])))
        self.assertTrue(set(df["Product"].unique()).issubset(set(['Product A', 'Product B', 'Product C', 'Product D', 'Product E'])))
        self.assertTrue(df["Sales"].min() >= 1)
        self.assertTrue(df["Sales"].max() <= 100)

    def test_case_2(self):
        'test with random countries and products'
        countries = [fake.country() for _ in range(5)]
        products = [fake.unique.first_name() for _ in range(5)]
        df = f_666(200, countries=countries, products=products, random_seed=1)
        self.assertEqual(len(df), 200)
        self.assertTrue(set(df["Country"].unique()).issubset(set(countries)))
        self.assertTrue(set(df["Product"].unique()).issubset(set(products)))

    def test_case_3(self):
        'empty'
        df = f_666(0)
        self.assertEqual(len(df), 0)

    def test_case_4(self):
        'only one countrie and product'
        df = f_666(50, countries=['USA'], products=['Product A'])
        self.assertEqual(len(df), 50)
        self.assertTrue(set(df["Country"].unique()) == set(['USA']))
        self.assertTrue(set(df["Product"].unique()) == set(['Product A']))

    def test_case_5(self):
        'saving to csv'
        output_path = self.temp_dir
        df = f_666(100, output_path=os.path.join(output_path, 'test.csv'))
        self.assertEqual(len(df), 100)
        # Verify the file was saved correctly
        saved_df = pd.read_csv(os.path.join(output_path, 'test.csv'))
        pd.testing.assert_frame_equal(df, saved_df)

    def tearDown(self):
        # Cleanup temporary directory after tests
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)

if __name__ == "__main__":
    run_tests()