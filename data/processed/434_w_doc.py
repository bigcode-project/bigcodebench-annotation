import pandas as pd
import re
import random


def task_func(s: str, seed: int = 0) -> pd.DataFrame:
    """
    Generate a Pandas DataFrame of products with their ID, quantity, code, price, product, and description
    based on a specified string of product data.

    The input string is expected to be divided into segments by newlines. Each segment is expected to
    be further split into parts by whitespace: ID, quantity, code, price, and a product description.
    The function will remove trailing whitespaces in each field and assign a product name per unique code.
    Product name is randomly sampled from: ['Apple', 'Banana', 'Orange', 'Pear', 'Grape'].
    The same product name will be assigned to each code for each input s, however different codes can be
    mapped to the same name.

    Parameters:
    - s    (str): Product data string split by newline, then whitespace.
                  Expected format per segment: '<ID> <Quantity> <Code> <Price> <Description>'
                  If incomplete, this function raises ValueError.
    - seed (int): Random seed for reproducibility. Defaults to 0.

    Returns:
    - data_df (pd.DataFrame): DataFrame with columns: ['ID', 'Quantity', 'Code', 'Price', 'Product', 'Description'].
                              Quantity and Price are expected to be integers.

    Requirements:
    - pandas
    - re
    - random

    Examples:
    >>> s = '1 10 A10B 100 This is a description with spaces'
    >>> df = task_func(s)
    >>> df
      ID  Quantity  Code  Price Product                        Description
    0  1        10  A10B    100    Pear  This is a description with spaces

    >>> s = '1 10 A10B 100 This is a description with spaces\\n2 20 B20C 200 Another description example'
    >>> df = task_func(s)
    >>> df
      ID  Quantity  Code  Price Product                        Description
    0  1        10  A10B    100    Pear  This is a description with spaces
    1  2        20  B20C    200    Pear        Another description example
    """
    if not s:
        raise ValueError("Incomplete data provided.")
    random.seed(seed)
    products = ["Apple", "Banana", "Orange", "Pear", "Grape"]
    code_to_product = dict()
    data_list = []
    segments = [segment.strip() for segment in s.split("\n")]
    for segment in segments:
        if segment:
            elements = re.split(r"\s+", segment.strip(), 4)
            if len(elements) < 5:
                raise ValueError("Incomplete data provided.")
            id, quantity, code, price, description = elements
            product = code_to_product.get(code, random.choice(products))
            data_list.append([id, quantity, code, price, product, description])
    df = pd.DataFrame(
        data_list, columns=["ID", "Quantity", "Code", "Price", "Product", "Description"]
    )
    df["Quantity"] = df["Quantity"].astype(int)
    df["Price"] = df["Price"].astype(int)
    return df

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        self.df1 = pd.DataFrame(
            {
                "ID": ["1"],
                "Quantity": ["10"],
                "Code": ["A10B"],
                "Price": ["100"],
                "Description": ["This is a description with spaces"],
            }
        )
        self.df2 = pd.DataFrame(
            {
                "ID": ["2"],
                "Quantity": ["15"],
                "Code": ["B20C"],
                "Price": ["200"],
                "Description": ["Another description with spaces"],
            }
        )
        self.df_multiple = pd.concat([self.df1, self.df2]).reset_index(drop=True)
        for col in ["Quantity", "Price"]:
            self.df1[col] = self.df1[col].astype(int)
            self.df2[col] = self.df2[col].astype(int)
            self.df_multiple[col] = self.df_multiple[col].astype(int)
    def _test_most_columns(self, df1, df2):
        columns_to_test = ["ID", "Quantity", "Code", "Price", "Description"]
        for col in columns_to_test:
            pd.testing.assert_series_equal(df1[col], df2[col])
    def test_case_1(self):
        # Test basic structure and data correctness
        input_str = "1 10 A10B 100 This is a description with spaces"
        result = task_func(input_str)
        self.assertIsInstance(result, pd.DataFrame)
        self._test_most_columns(result, self.df1)
    def test_case_2(self):
        # Test multiline basic structure and correctness
        input_str = "\n".join(
            [
                "1 10 A10B 100 This is a description with spaces",
                "2 15 B20C 200 Another description with spaces",
            ]
        )
        result = task_func(input_str)
        self._test_most_columns(result, self.df_multiple)
    def test_case_3(self):
        # Test multiline with trailing whitespaces
        input_str = "\n".join(
            [
                "1 10 A10B 100 This is a description with spaces         ",
                "2 15 B20C 200 Another description with spaces     ",
            ]
        )
        result = task_func(input_str)
        self._test_most_columns(result, self.df_multiple)
    def test_case_4(self):
        # Test behavior with extra spaces in the input string
        input_str = "\n".join(
            [
                "1   10 A10B 100       This is a description with spaces",
                "2  15   B20C   200 Another description with spaces     ",
            ]
        )
        result = task_func(input_str)
        self._test_most_columns(result, self.df_multiple)
    def test_case_5(self):
        # Test code to product mapping when there are duplicates
        input_str = "\n".join(
            [
                "1 10 A10B 100 This is a description with spaces",
                "2 15 A10B 200 Another description with spaces",
            ]
        )
        result = task_func(input_str)
        product_names = result["Product"]
        self.assertEqual(product_names.iloc[0], product_names.iloc[1])
    def test_case_6(self):
        # Test behavior with empty input string
        input_str = ""
        with self.assertRaises(ValueError):
            task_func(input_str)
    def test_case_7(self):
        # Test behavior with incomplete input string
        input_str = "1 10"
        with self.assertRaises(ValueError):
            task_func(input_str)
