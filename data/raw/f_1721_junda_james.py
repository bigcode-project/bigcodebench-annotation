import pandas as pd
from random import choices, seed

def f_1721(products, ratings, weights, random_seed=42):
    """
    Generates a DataFrame containing ratings for a given list of products. Ratings are generated randomly based on the provided weights. 
    The DataFrame is sorted by ratings in descending order.

    Parameters:
    products (list): List of product names.
    ratings (list): List of possible ratings.
    weights (list): List of weights corresponding to each rating for weighted random selection.
    random_seed (int, optional): Seed for random number generation for reproducibility. Defaults to 42.

    Returns:
    pandas.DataFrame: A DataFrame with two columns: 'Product' and 'Rating', sorted by 'Rating' in descending order.

    Requirements:
    - pandas
    - random

    Example:
    >>> products = ["iPhone", "iPad", "Macbook", "Airpods", "Apple Watch"]
    >>> ratings = [1, 2, 3, 4, 5]
    >>> weights = [0.05, 0.1, 0.2, 0.3, 0.35]
    >>> df = f_1721(products, ratings, weights, 42)
    >>> print(df.head()) # Expected output is a DataFrame sorted by 'Rating', which may vary due to randomness.
           Product  Rating
    4  Apple Watch       5
    0       iPhone       4
    2      Macbook       3
    3      Airpods       3
    1         iPad       1
    """

    seed(random_seed)  # Setting the seed for reproducibility
    product_ratings = []

    for product in products:
        rating = choices(ratings, weights, k=1)[0]
        product_ratings.append([product, rating])

    df = pd.DataFrame(product_ratings, columns=["Product", "Rating"])
    df.sort_values("Rating", ascending=False, inplace=True)

    return df

import unittest
import pandas as pd

class TestCases(unittest.TestCase):
    def setUp(self):
        self.products = ["iPhone", "iPad", "Macbook", "Airpods", "Apple Watch"]
        self.ratings = [1, 2, 3, 4, 5]
        self.weights = [0.05, 0.1, 0.2, 0.3, 0.35]

    def test_random_reproducibility(self):
        df1 = f_1721(self.products, self.ratings, self.weights, 42)
        df2 = f_1721(self.products, self.ratings, self.weights, 42)
        pd.testing.assert_frame_equal(df1, df2)

    def test_dataframe_structure(self):
        df = f_1721(self.products, self.ratings, self.weights)
        self.assertEqual(list(df.columns), ['Product', 'Rating'])
        self.assertEqual(len(df), len(self.products))

    def test_rating_range(self):
        df = f_1721(self.products, self.ratings, self.weights)
        self.assertTrue(df['Rating'].isin(self.ratings).all())

    def test_sort_order(self):
        df = f_1721(self.products, self.ratings, self.weights)
        sorted_df = df.sort_values('Rating', ascending=False)
        pd.testing.assert_frame_equal(df, sorted_df)

    def test_different_seeds(self):
        df1 = f_1721(self.products, self.ratings, self.weights, 42)
        df2 = f_1721(self.products, self.ratings, self.weights, 24)
        with self.assertRaises(AssertionError):
            pd.testing.assert_frame_equal(df1, df2)

    
    def test_values(self):
        df1 = f_1721(self.products, self.ratings, self.weights, 42)
        df_list = df1.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        expect = ['Apple Watch,5', 'iPhone,4', 'Macbook,3', 'Airpods,3', 'iPad,1']
   
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")

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