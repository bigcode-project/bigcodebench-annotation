import pandas as pd
import random

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def f_14(value_range=(0, 100)):
    """
    Generate a category distribution within a specified range and return as a DataFrame.

    Parameters:
    value_range (tuple): A tuple specifying the range (min, max) for generating random values for categories.
    
    Returns:
    DataFrame: A pandas DataFrame that has two columns: 'Category' (category names) and 'Count' (count of each category). 

    Requirements:
    - pandas
    - random

    Example:
    >>> random.seed(0)
    >>> df = f_14()
    >>> df['Count'][0] >= 0
    True
    """
    distribution = {category: random.randint(*value_range) for category in CATEGORIES}
    df = pd.DataFrame(list(distribution.items()), columns=['Category', 'Count'])
    return df

import unittest
import pandas as pd
import random
class TestCases(unittest.TestCase):
    def test_return_type(self):
        """Test if the function returns a DataFrame."""
        random.seed(0)
        result = f_14()
        self.assertIsInstance(result, pd.DataFrame)
    def test_columns(self):
        """Test if the DataFrame has the correct columns."""
        random.seed(0)
        result = f_14()
        self.assertListEqual(list(result.columns), ['Category', 'Count'])
    def test_value_range_default(self):
        """Test if the 'Count' values are within the default range."""
        random.seed(0)
        result = f_14()
        for count in result['Count']:
            self.assertTrue(0 <= count <= 100)
    def test_value_range_custom(self):
        """Test if the 'Count' values are within a custom range."""
        random.seed(0)
        test_range = (10, 50)
        result = f_14(value_range=test_range)
        for count in result['Count']:
            self.assertTrue(test_range[0] <= count <= test_range[1])
    def test_number_of_rows(self):
        """Test if the DataFrame contains the expected number of rows."""
        random.seed(0)
        result = f_14()
        self.assertEqual(len(result), len(CATEGORIES))
