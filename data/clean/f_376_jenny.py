import pandas as pd
import re
import random


def f_376(data_list, seed=None):
    """
    Removes a random comma-separated value (treated as a "substring") from each string
    in a list and returns a pandas DataFrame containing the original and modified strings.

    Parameters:
    - data_list (list of str): A list of comma-separated strings. The function will remove
                               leading and trailing whitespaces first before processing.
    - seed (int, optional): Seed for the random number generator for reproducibility.
      Default is None, which uses system time.

    Returns:
    - DataFrame: A pandas DataFrame with columns 'Original String' and 'Modified String'.

    Requirements:
    - pandas
    - re
    - random

    Example:
    >>> f_376(['lamp, bag, mirror', 'table, chair, bag, lamp'], seed=42)
               Original String   Modified String
    0        lamp, bag, mirror         lamp, bag
    1  table, chair, bag, lamp  chair, bag, lamp
    """
    if seed is not None:
        random.seed(seed)

    df = pd.DataFrame([s.strip() for s in data_list], columns=["Original String"])

    modified_strings = []
    for s in data_list:
        substrings = re.split(", ", s)
        random_substring = random.choice(substrings)
        modified_s = (
            s.replace(", " + random_substring, "")
            if ", " + random_substring in s
            else s.replace(random_substring + ", ", "")
        )
        modified_strings.append(modified_s)

    df["Modified String"] = modified_strings

    return df


import unittest
import pandas as pd


class TestCases(unittest.TestCase):
    def setUp(self):
        self.columns = ["Original String", "Modified String"]

    def test_case_1(self):
        # Test basic case
        input_data = ["apple, orange, banana", "car, bike, plane"]
        result = f_376(input_data, seed=42)
        self._test_dataframe(result, input_data)

    def test_case_2(self):
        # Test single character
        input_data = ["a, b, c, d, e", "f, g, h, i, j"]
        result = f_376(input_data, seed=42)
        self._test_dataframe(result, input_data)

    def test_case_3(self):
        # Test single numeric characters
        input_data = ["1, 2, 3", "4, 5, 6, 7"]
        result = f_376(input_data, seed=42)
        self._test_dataframe(result, input_data)

    def test_case_4(self):
        # Test with an empty list
        input_data = []
        result = f_376(input_data, seed=42)
        self.assertTrue(result.empty)

    def test_case_5(self):
        # Test with strings without commas
        input_data = ["apple", "car"]
        result = f_376(input_data, seed=42)
        # Ensure dataframe has correct columns
        self.assertListEqual(list(result.columns), self.columns)
        # Ensure 'Modified String' is the same as 'Original String' for single values
        for orig, mod in zip(result["Original String"], result["Modified String"]):
            self.assertEqual(orig.strip(), mod)

    def test_case_6(self):
        # Test strings with leading and trailing spaces
        input_data = [" apple, orange, banana ", " car, bike, plane"]
        expected_data = ["apple, orange, banana", "car, bike, plane"]
        result = f_376(input_data, seed=42)
        self._test_dataframe(result, expected_data)

    def test_case_7(self):
        # Test strings where the same value appears multiple times
        input_data = ["apple, apple, banana", "car, car, bike, plane"]
        result = f_376(input_data, seed=42)
        # Special case where substrings might be duplicated
        for orig, mod in zip(result["Original String"], result["Modified String"]):
            diff = len(orig.split(", ")) - len(mod.split(", "))
            self.assertTrue(diff in [0, 1])  # Either no change or one substring removed

    def test_case_8(self):
        # Test reproducibility with the same seed
        input_data = ["apple, orange, banana", "car, bike, plane"]
        result1 = f_376(input_data, seed=42)
        result2 = f_376(input_data, seed=42)
        pd.testing.assert_frame_equal(result1, result2)

    def test_case_9(self):
        # Test difference with different seeds
        input_data = ["apple, orange, banana", "car, bike, plane"]
        result1 = f_376(input_data, seed=42)
        result2 = f_376(input_data, seed=43)
        self.assertFalse(result1.equals(result2))

    def _test_dataframe(self, df, input_data):
        # Ensure dataframe has correct columns
        self.assertListEqual(list(df.columns), self.columns)

        # Ensure 'Modified String' has one less substring than 'Original String'
        for orig, mod in zip(df["Original String"], df["Modified String"]):
            self.assertTrue(orig in input_data)  # Ensure original string is from input
            self.assertEqual(len(orig.split(", ")) - 1, len(mod.split(", ")))


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
