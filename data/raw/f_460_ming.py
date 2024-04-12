import pandas as pd
import re

def f_460(df, letter):
    """
    The function filters rows in a DataFrame in which the values of the 'Word' column begin with a specified letter. 
    It then calculates the length of the words in the filtered column and returns a dictionary of word lengths 
    and their respective counts.

    Parameters:
    df (DataFrame): The input DataFrame. It should have a 'Word' column.
    letter (str): The letter to filter the 'Word' column by. 

    Returns:
    dict: A dictionary of word lengths and their counts.
    
    Requirements:
    - pandas
    - re

    Example:
    >>> df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi']})
    >>> f_460(df, 'a')
    {5: 2, 6: 1}
    """
    regex = '^' + letter
    filtered_df = df[df['Word'].str.contains(regex, regex=True)]
    word_lengths = filtered_df['Word'].str.len()
    count_dict = word_lengths.value_counts().to_dict()

    return count_dict

import unittest
import pandas as pd

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'date', 'elephant', 'fig', 'grape', 'kiwi']})
        result = f_460(df, 'a')
        expected_result = {5: 1}
        self.assertDictEqual(result, expected_result)

    def test_case_2(self):
        df = pd.DataFrame({'Word': ['cat', 'dog', 'elephant', 'fish', 'goose']})
        result = f_460(df, 'e')
        expected_result = {8: 1}
        self.assertDictEqual(result, expected_result)

    def test_case_3(self):
        df = pd.DataFrame({'Word': ['kiwi', 'lemon', 'mango', 'nectarine', 'orange']})
        result = f_460(df, 'm')
        expected_result = {5: 1}
        self.assertDictEqual(result, expected_result)

    def test_case_4(self):
        df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'date', 'elephant', 'fig', 'grape', 'kiwi']})
        result = f_460(df, 'z')
        expected_result = {}
        self.assertDictEqual(result, expected_result)

    def test_case_5(self):
        df = pd.DataFrame({'Word': ['zebra', 'zoo', 'zucchini']})
        result = f_460(df, 'z')
        expected_result = {5: 1, 3: 1, 8: 1}
        self.assertDictEqual(result, expected_result)


if __name__ == "__main__":
    run_tests()