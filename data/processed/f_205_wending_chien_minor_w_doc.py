import pandas as pd
from sklearn.preprocessing import LabelEncoder


def f_393(data):
    """
    Transforms categorical data into a numerical format suitable for machine learning algorithms using sklearn's
    LabelEncoder. This function generates a DataFrame that pairs original categorical values with their numerical
    encodings.

    Parameters:
    data (list): List of categorical data to be encoded.

    Returns:
    DataFrame: A DataFrame with columns 'Category' and 'Encoded', where 'Category' is the original data and 'Encoded'
    is the numerical representation.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> df = f_393(['A', 'B', 'C', 'A', 'D', 'E', 'B', 'C'])
    >>> print(df.to_string(index=False))
    Category  Encoded
           A        0
           B        1
           C        2
           A        0
           D        3
           E        4
           B        1
           C        2
    """
    le = LabelEncoder()
    encoded = le.fit_transform(data)
    df = pd.DataFrame({'Category': data, 'Encoded': encoded})
    return df

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing basic functionality
        result = f_393(['A', 'B', 'C', 'A', 'D', 'E', 'B', 'C'])
        expected = pd.DataFrame({'Category': ['A', 'B', 'C', 'A', 'D', 'E', 'B', 'C'],
                                 'Encoded': [0, 1, 2, 0, 3, 4, 1, 2]})
        pd.testing.assert_frame_equal(result, expected)
    def test_case_2(self):
        # Testing with a single unique category
        result = f_393(['A', 'A', 'A'])
        expected = pd.DataFrame({'Category': ['A', 'A', 'A'],
                                 'Encoded': [0, 0, 0]})
        pd.testing.assert_frame_equal(result, expected)
    def test_case_3(self):
        # Testing with an empty list
        result = f_393([])
        expected = pd.DataFrame({'Category': [],
                                 'Encoded': []})
        pd.testing.assert_frame_equal(result, expected, check_dtype=False)
    def test_case_4(self):
        # Testing with multiple unique categories but in a different order
        result = f_393(['E', 'D', 'C', 'B', 'A'])
        expected = pd.DataFrame({'Category': ['E', 'D', 'C', 'B', 'A'],
                                 'Encoded': [4, 3, 2, 1, 0]})
        pd.testing.assert_frame_equal(result, expected)
    def test_case_5(self):
        # Testing with a list containing a single different category
        result = f_393(['Z'])
        expected = pd.DataFrame({'Category': ['Z'],
                                 'Encoded': [0]})
        pd.testing.assert_frame_equal(result, expected)
