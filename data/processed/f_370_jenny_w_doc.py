from collections import Counter
import pandas as pd


def f_370(myList):
    """
    Count the frequency of each word in a list and return a DataFrame of words and their number.

    Parameters:
    myList (list): List of strings. Each string is considered a word regardless of its content,
                                    however the function is case insensitive, and it removes
                                    leading and trailing whitespaces. If empty, function returns
                                    a DataFrame with a Count column that is otherwise empty.

    Returns:
    DataFrame: A pandas DataFrame with words and their counts.

    Requirements:
    - collections.Counter
    - pandas

    Example:
    >>> myList = ['apple', 'banana', 'apple', 'cherry', 'banana', 'banana']
    >>> f_370(myList)
            Count
    apple       2
    banana      3
    cherry      1
    """
    words = [w.lower().strip() for w in myList]
    word_counts = dict(Counter(words))
    report_df = pd.DataFrame.from_dict(word_counts, orient="index", columns=["Count"])

    return report_df

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        input_data = ["apple", "banana", "apple", "cherry", "banana", "banana"]
        expected_output = pd.DataFrame(
            {"Count": [2, 3, 1]}, index=["apple", "banana", "cherry"]
        )
        pd.testing.assert_frame_equal(f_370(input_data), expected_output)
    def test_case_2(self):
        # Test repeated value
        input_data = ["apple", "apple", "apple"]
        expected_output = pd.DataFrame({"Count": [3]}, index=["apple"])
        pd.testing.assert_frame_equal(f_370(input_data), expected_output)
    def test_case_3(self):
        # Test empty list
        input_data = []
        expected_output = pd.DataFrame(columns=["Count"])
        pd.testing.assert_frame_equal(f_370(input_data), expected_output)
    def test_case_4(self):
        # Test single entry
        input_data = ["kiwi"]
        expected_output = pd.DataFrame({"Count": [1]}, index=["kiwi"])
        pd.testing.assert_frame_equal(f_370(input_data), expected_output)
    def test_case_5(self):
        # Tests the function's ability to handle mixed case words correctly.
        input_data = ["Apple", "apple", "APPLE"]
        expected_output = pd.DataFrame({"Count": [3]}, index=["apple"])
        pd.testing.assert_frame_equal(f_370(input_data), expected_output)
    def test_case_6(self):
        # Tests the function's ability to handle words with leading/trailing spaces.
        input_data = ["banana ", " banana", "  banana"]
        expected_output = pd.DataFrame({"Count": [3]}, index=["banana"])
        pd.testing.assert_frame_equal(f_370(input_data), expected_output)
    def test_case_7(self):
        # Tests the function's ability to handle words with special characters.
        input_data = ["kiwi!", "!kiwi", "kiwi"]
        expected_output = pd.DataFrame(
            {"Count": [1, 1, 1]}, index=["kiwi!", "!kiwi", "kiwi"]
        )
        pd.testing.assert_frame_equal(f_370(input_data), expected_output)
    def test_case_8(self):
        # Tests the function's handling of numeric strings as words.
        input_data = ["123", "456", "123", "456", "789"]
        expected_output = pd.DataFrame(
            {"Count": [2, 2, 1]}, index=["123", "456", "789"]
        )
        pd.testing.assert_frame_equal(f_370(input_data), expected_output)
    def test_case_9(self):
        # Tests the function's handling of empty strings and strings with only spaces.
        input_data = [" ", "  ", "", "apple", "apple "]
        expected_output = pd.DataFrame({"Count": [3, 2]}, index=["", "apple"])
        pd.testing.assert_frame_equal(f_370(input_data), expected_output)
    def test_case_10(self):
        # Tests handling of strings that become duplicates after strip() is applied.
        input_data = ["banana", "banana ", " banana", "banana"]
        expected_output = pd.DataFrame({"Count": [4]}, index=["banana"])
        pd.testing.assert_frame_equal(f_370(input_data), expected_output)
