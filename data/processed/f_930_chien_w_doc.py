import string
import random
import pandas as pd
import numpy as np

# Constants
NUM_SAMPLES = 1000  # Number of samples


def f_950():
    """
    Generates a DataFrame with two columns: a string field and a float field.
    The string field contains randomly generated strings of 10 ASCII letters.
    The float field contains randomly generated numbers between 0 and 10000,
    formatted with two decimal places and a comma as the thousands separator.

    Parameters:
    - None

    Returns:
        DataFrame: A pandas DataFrame with NUM_SAMPLES rows. Each row contains a
        random string in the 'String Field' column and a formatted float in the
        'Float Field' column.

    Requirements:
    - string
    - random
    - pandas
    - numpy

    Example:
    >>> random.seed(0)
    >>> np.random.seed(0)
    >>> dataset = f_950()
    >>> print(dataset.head(1))
      String Field Float Field
    0   RNvnAvOpyE    5,488.14

    Note: The exact values in the dataset will vary as they are randomly generated.
    """
    data = {
        "String Field": [
            "".join(random.choices(string.ascii_letters, k=10))
            for _ in range(NUM_SAMPLES)
        ],
        "Float Field": [f"{x:,.2f}" for x in np.random.uniform(0, 10000, NUM_SAMPLES)],
    }
    df = pd.DataFrame(data)
    return df

import unittest
import pandas as pd
import random
class TestCases(unittest.TestCase):
    """Test cases for f_950."""
    def test_dataframe_creation(self):
        """
        Test if the function returns a pandas DataFrame.
        """
        random.seed(1)
        result = f_950()
        self.assertIsInstance(result, pd.DataFrame)
    def test_row_count(self):
        """
        Test if the DataFrame contains the correct number of rows.
        """
        random.seed(2)
        result = f_950()
        self.assertEqual(len(result), NUM_SAMPLES)
    def test_column_count(self):
        """
        Test if the DataFrame contains exactly two columns.
        """
        random.seed(3)
        result = f_950()
        self.assertEqual(len(result.columns), 2)
    def test_string_field_format(self):
        """
        Test if the 'String Field' contains strings of 10 ASCII letters.
        """
        random.seed(4)
        result = f_950()
        all_strings = all(result["String Field"].str.match("^[A-Za-z]{10}$"))
        self.assertTrue(all_strings)
    def test_float_field_format(self):
        """
        Test if the 'Float Field' contains formatted float strings.
        """
        random.seed(5)
        result = f_950()
        all_floats = all(
            isinstance(float(val.replace(",", "")), float)
            for val in result["Float Field"]
        )
        self.assertTrue(all_floats)
