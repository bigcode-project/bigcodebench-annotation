import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def f_287(data):
    """
    Processes a dictionary containing product names and their corresponding prices in string format. 
    The function converts these string prices (which may include commas as thousand separators) into float values. 
    It then calculates statistical measures (mean, median, and standard deviation) of these prices and 
    generates a histogram to visually represent the distribution of the prices.

    Parameters:
    - data (dict): A dictionary with two keys: 'Product' and 'Price_String'. 
        'Product' is a list of product names, each name corresponding to a product.
        'Price_String' is a list of prices in string format, associated with these products. 
        The price strings can contain commas for thousand separators and a period for the decimal point (e.g., "1,234.56").

    Returns:
    - dict: Contains the calculated mean, median, and standard deviation (sample) of the prices. 
        The keys are 'mean', 'median', and 'std_dev'.
    - matplotlib.axes._axes.Axes: A subplot object that represents the histogram plot of the product prices. 
        The histogram displays the frequency distribution of the prices.

    Note:
    - A histogram plot is generated using these prices, with automatic bin sizing ('auto'), a blue color, 
      70% opacity (alpha=0.7), and a relative width (rwidth) of 0.85 for the bars. 
    - The histogram's title is set to 'Histogram of Product Prices', and the x and y-axis are labeled 'Price' and 'Frequency', respectively.

    Requirements:
    - pandas
    - numpy
    - matplotlib

    Example:
    >>> results = f_287({'Product': ['Apple', 'Banana'], 'Price_String': ['1,234.00', '567.89']})
    >>> print(results)
    ({'mean': 900.9449999999999, 'median': 900.9449999999999, 'std_dev': 471.0108980161712}, (array([1., 1.]), array([ 567.89 ,  900.945, 1234.   ]), <BarContainer object of 2 artists>))

    Note:
    - The function assumes that each product name in the 'Product' list has a corresponding price in the 'Price_String' list.
    - The histogram plot's appearance (like color, alpha, and rwidth) is pre-set but can be customized further if needed.
    """
    df = pd.DataFrame(data)
    df["Price_Float"] = df["Price_String"].apply(lambda x: float(x.replace(",", "")))
    mean_price = np.mean(df["Price_Float"])
    median_price = np.median(df["Price_Float"])
    std_dev_price = np.std(df["Price_Float"], ddof=1)
    ax = plt.hist(df["Price_Float"], bins="auto", color="blue", alpha=0.7, rwidth=0.85)
    plt.title("Histogram of Product Prices")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    return {"mean": mean_price, "median": median_price, "std_dev": std_dev_price}, ax

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    """Test cases for f_287"""
    def test_basic_functionality(self):
        """Test basic functionality."""
        sample_data = {
            "Product": ["James", "Olivia", "Jamie", "Angela", "Jennifer"],
            "Price_String": ["2,213.00", "6,083.00", "5,461.00", "884.00", "2,783.00"],
        }
        float_prices = [
            float(price.replace(",", "")) for price in sample_data["Price_String"]
        ]
        expected_mean = np.mean(float_prices)
        expected_median = np.median(float_prices)
        expected_std_dev = np.std(float_prices, ddof=1)
        result, _ = f_287(sample_data)
        self.assertAlmostEqual(result["mean"], expected_mean)
        self.assertAlmostEqual(result["median"], expected_median)
        self.assertAlmostEqual(result["std_dev"], expected_std_dev)
    def test_large_sample_size(self):
        """Test large sample size."""
        sample_data = {
            "Product": [
                "Adam",
                "Lisa",
                "Scott",
                "Bianca",
                "Ashlee",
                "Shannon",
                "Michelle",
                "Robert",
                "Joseph",
                "Joshua",
                "Traci",
                "Jacob",
                "Daniel",
                "Timothy",
                "Paul",
            ],
            "Price_String": [
                "1,691.00",
                "967.00",
                "5,789.00",
                "6,806.00",
                "3,301.00",
                "5,319.00",
                "7,619.00",
                "134.00",
                "7,883.00",
                "5,028.00",
                "3,330.00",
                "5,253.00",
                "8,551.00",
                "1,631.00",
                "7,637.00",
            ],
        }
        float_prices = [
            float(price.replace(",", "")) for price in sample_data["Price_String"]
        ]
        expected_mean = np.mean(float_prices)
        expected_median = np.median(float_prices)
        expected_std_dev = np.std(float_prices, ddof=1)
        result, _ = f_287(sample_data)
        self.assertAlmostEqual(result["mean"], expected_mean)
        self.assertAlmostEqual(result["median"], expected_median)
        self.assertAlmostEqual(result["std_dev"], expected_std_dev)
    def test_invalid_input(self):
        """Test invalid input."""
        with self.assertRaises(Exception):
            f_287({})
        with self.assertRaises(Exception):
            f_287({"Product": ["Apple"], "Price_WrongKey": ["1,234.00"]})
    def test_all_zero_prices(self):
        """Test all zero prices."""
        sample_data = {
            "Product": ["Apple", "Banana", "Cherry"],
            "Price_String": ["0.00", "0.00", "0.00"],
        }
        result, _ = f_287(sample_data)
        self.assertEqual(result["mean"], 0)
        self.assertEqual(result["median"], 0)
        self.assertEqual(result["std_dev"], 0)
    def test_non_uniform_distribution(self):
        """Test non-uniform distribution."""
        sample_data = {
            "Product": ["Apple", "Banana", "Cherry", "Date", "Fig"],
            "Price_String": ["1,000.00", "500.00", "1,500.00", "2,000.00", "2,500.00"],
        }
        float_prices = [
            float(price.replace(",", "")) for price in sample_data["Price_String"]
        ]
        expected_mean = np.mean(float_prices)
        expected_median = np.median(float_prices)
        expected_std_dev = np.std(float_prices, ddof=1)
        result, _ = f_287(sample_data)
        self.assertAlmostEqual(result["mean"], expected_mean)
        self.assertAlmostEqual(result["median"], expected_median)
        self.assertAlmostEqual(result["std_dev"], expected_std_dev)
    def tearDown(self):
        plt.close()
