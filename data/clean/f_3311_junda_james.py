import pandas as pd
import codecs

def f_3311(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Decodes all Unicode escape strings in a particular column ("UnicodeString") in a given Pandas DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The pandas DataFrame which must contain the column "UnicodeString".

    Returns:
    pd.DataFrame: The DataFrame with decoded strings in the "UnicodeString" column.

    Raises:
    KeyError: If the column "UnicodeString" does not exist in the DataFrame.
    TypeError: If the input is not a Pandas DataFrame.

    Example:
    >>> df = pd.DataFrame({
    ...     'Name': ['John', 'Anna', 'Peter'],
    ...     'Age': [27, 23, 29],
    ...     'Salary': [50000, 60000, 70000],
    ...     'UnicodeString': ['\u004A\u006F\u0068\u006E', '\u0041\u006E\u006E\u0061', '\u0050\u0065\u0074\u0065\u0072']
    ... })
    >>> f_3311(df)
        Name  Age  Salary UnicodeString
    0   John   27   50000          John
    1   Anna   23   60000          Anna
    2  Peter   29   70000         Peter

    Requirements:
    - pandas
    - codecs
    """
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("The input must be a pandas DataFrame.")

    if 'UnicodeString' not in dataframe.columns:
        raise KeyError("'UnicodeString' column not found in the DataFrame.")

    dataframe['UnicodeString'] = dataframe['UnicodeString'].apply(lambda x: codecs.decode(x, 'unicode_escape'))

    return dataframe

import unittest
import pandas as pd

class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.test_data = pd.DataFrame({
            'Name': ['John', 'Anna', 'Peter'],
            'Age': [27, 23, 29],
            'Salary': [50000, 60000, 70000],
            'UnicodeString': ['\u004A\u006F\u0068\u006E', '\u0041\u006E\u006E\u0061', '\u0050\u0065\u0074\u0065\u0072']
        })

    def test_unicode_decoding(self):
        decoded_df = f_3311(self.test_data)
        expected_strings = ['John', 'Anna', 'Peter']
        self.assertListEqual(list(decoded_df['UnicodeString']), expected_strings)

    def test_missing_column(self):
        with self.assertRaises(KeyError):
            f_3311(pd.DataFrame({'Name': ['John']}))

    def test_non_dataframe_input(self):
        with self.assertRaises(TypeError):
            f_3311("Not a DataFrame")

    def test_empty_dataframe(self):
        empty_df = pd.DataFrame({'UnicodeString': []})
        result_df = f_3311(empty_df)
        self.assertTrue(result_df['UnicodeString'].empty)

    def test_non_string_unicode_values(self):
        df_with_non_string = pd.DataFrame({'UnicodeString': [123, 456]})
        with self.assertRaises(Exception):
            f_3311(df_with_non_string)

# Run the tests
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