import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

PRODUCTS = ['Product' + str(i) for i in range(1, 6)]
MONTHS = ['Month' + str(i) for i in range(1, 13)]


def f_501():
    """
    Generate a DataFrame representing monthly sales of products and visualize the total sales.

    The function creates a DataFrame where each row represents a month, each column represents a product,
    and cell values represent sales figures. It then plots the total sales per product across all months
    using both a line plot and a heatmap for visualization.

    Returns:
    - pd.DataFrame: A DataFrame with randomly generated sales figures for each product over 12 months.

    The function also displays:
    - A line plot showing the total sales per product.
    - A heatmap visualizing sales figures across products and months.

    Requirements:
    - pandas for data manipulation.
    - numpy for random data generation.
    - matplotlib.pyplot and seaborn for plotting.
    """
    sales = np.random.randint(100, 1001, size=(len(MONTHS), len(PRODUCTS)))
    df = pd.DataFrame(sales, index=MONTHS, columns=PRODUCTS)

    # Visualizations
    total_sales = df.sum()
    plt.figure(figsize=(10, 5))
    total_sales.plot(kind='line', title='Total Sales per Product')
    plt.ylabel('Total Sales')
    plt.show()

    plt.figure(figsize=(10, 8))
    sns.heatmap(df, annot=True, fmt="d", cmap='viridis')
    plt.title('Monthly Sales per Product')
    plt.show()

    return df


import unittest

class TestF501(unittest.TestCase):
    def test_dataframe_shape(self):
        """Test if the DataFrame has the correct shape."""
        df = f_501()
        self.assertEqual(df.shape, (12, 5))  # 12 months and 5 products

    def test_dataframe_columns(self):
        """Test if the DataFrame has the correct column names."""
        df = f_501()
        expected_columns = PRODUCTS
        self.assertListEqual(list(df.columns), expected_columns)

    def test_dataframe_index(self):
        """Test if the DataFrame has the correct index."""
        df = f_501()
        expected_index = MONTHS
        self.assertListEqual(list(df.index), expected_index)

    def test_sales_range(self):
        """Test if sales figures are within the expected range."""
        df = f_501()
        self.assertTrue((df >= 100).all().all() and (df <= 1000).all().all())

    def test_returns_dataframe(self):
        """Test if the function returns a pandas DataFrame."""
        df = f_501()
        self.assertIsInstance(df, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()

