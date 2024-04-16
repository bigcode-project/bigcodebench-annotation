import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

# Constants
PATTERN = r"([a-fA-F\d]{32})"

def f_299(df, column):
    """
    Find all matches of the regex pattern '([a-fA-F\ d] {32})' in a Pandas DataFrame column and count the occurrence of any unique match in the data.

    Parameters:
    df (DataFrame): The pandas DataFrame.
    column (str): The column in which to find the pattern.

    Returns:
    Series: A pandas Series with counts of each unique match.

    Requirements:
    - pandas
    - re
    - numpy
    - matplotlib.pyplot

    Example:
    >>> data = pd.DataFrame({"text": ["6f96cfdfe5ccc627cadf24b41725caa4 gorilla", 
    ...                               "6f96cfdfe5ccc627cadf24b41725caa4 banana",
    ...                               "1234567890abcdef1234567890abcdef apple"]})
    >>> counts = f_299(data, "text")
    >>> print(counts.index[0])
    6f96cfdfe5ccc627cadf24b41725caa4
    """

    matches = df[column].apply(lambda x: re.findall(PATTERN, x))
    flattened_matches = np.concatenate(matches.values)
    counts = pd.Series(flattened_matches).value_counts()
    
    return counts

import unittest
import pandas as pd
import re
from faker import Faker

# Constants for the test cases
PATTERN = r"([a-fA-F\d]{32})"

def generate_mock_dataframe(num_rows, include_hex=True):
    fake = Faker()
    data = []

    for _ in range(num_rows):
        if include_hex:
            sentence = fake.sentence() + " " + fake.hexify(text='^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', upper=False)
        else:
            sentence = fake.sentence()
        data.append(sentence)

    return pd.DataFrame({"text": data})

class TestCases(unittest.TestCase):
    def test_typical_use_case(self):
        df = generate_mock_dataframe(10, include_hex=True)
        result = f_299(df, "text")
        self.assertIsInstance(result, pd.Series)
        for hex_pattern in result.index:
            self.assertRegex(hex_pattern, PATTERN)

    def test_default(self):
        df = pd.DataFrame({"text": ["6f96cfdfe5ccc627cadf24b41725caa4 gorilla", 
                            "6f96cfdfe5ccc627cadf24b41725caa4 banana",
                            "1234567890abcdef1234567890abcdef apple"]})
        result = f_299(df, "text")
        self.assertIsInstance(result, pd.Series)
        for hex_pattern in result.index:
            self.assertRegex(hex_pattern, PATTERN)

    def test_no_matches(self):
        df = generate_mock_dataframe(10, include_hex=False)
        result = f_299(df, "text")
        self.assertTrue(result.empty)

    def test_mixed_data(self):
        df = generate_mock_dataframe(10, include_hex=True)
        df.loc[0, "text"] += " some-non-hex-string"
        result = f_299(df, "text")
        self.assertIsInstance(result, pd.Series)
        for hex_pattern in result.index:
            self.assertRegex(hex_pattern, PATTERN)


    def test_incorrect_column(self):
        df = generate_mock_dataframe(10, include_hex=True)
        with self.assertRaises(KeyError):
            f_299(df, "nonexistent_column")

    def test_large_dataset(self):
        df = generate_mock_dataframe(1000, include_hex=True)
        result = f_299(df, "text")
        self.assertIsInstance(result, pd.Series)

    
    
    

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()