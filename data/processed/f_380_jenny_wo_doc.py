import pandas as pd
import random
import re


def f_323(data_list, seed=None):
    """
    Apply a random operation (remove, replace, shuffle, or randomize) to substrings in a list of strings.

    This function processes a list of comma-separated strings by applying one of four random operations to
    their substrings: remove, replace, shuffle, or randomize. Here, a substring refers to the individual
    items in the string that are separated by commas, sensitive to leading/trailing whitespace, i.e.
    'apple' != 'apple ', and sensitive to case, i.e. 'APPLE' != 'aPPLE'.

    The choice of operation and the substrings it affects are determined randomly. The operations are:
    - Remove: Randomly selects and removes a substring.
              If a string contains only one substring, no 'remove' operation is applied.
    - Replace: Randomly selects a substring and replaces it with 'random_string'.
    - Shuffle: Randomly shuffles the order of the substrings.
    - Randomize: Assigns a new, random order to the substrings.

    Finally, the function returns a DataFrame with column 'Original String' containing the input strings
    and the 'Modified String' column containing the strings after applying the random operation.

    Parameters:
    - data_list (list): The list of strings. If empty, function will return a DataFrame with the expected
                        columns that is otherwise empty.
    - seed (int, optional): A seed for the random operations to ensure reproducibility. Default is None.

    Returns:
    df (pd.DataFrame): DataFrame containing original and modified strings.

    Requirements:
    - pandas
    - random
    - re

    Example:
    >>> f_323(['lamp, bag, mirror', 'table, chair, bag, lamp'], seed=0)
               Original String          Modified String
    0        lamp, bag, mirror        bag, lamp, mirror
    1  table, chair, bag, lamp  lamp, chair, bag, table
    """
    random.seed(seed)
    df = pd.DataFrame(data_list, columns=["Original String"])
    modified_strings = []
    for s in data_list:
        substrings = re.split(", ", s)
        operation = random.choice(["remove", "replace", "shuffle", "randomize"])
        if operation == "remove":
            if len(substrings) > 1:
                random_substring = random.choice(substrings)
                substrings.remove(random_substring)
                modified_s = ", ".join(substrings)
            else:
                modified_s = s
        elif operation == "replace":
            random_substring_index = random.choice(range(len(substrings)))
            substrings[random_substring_index] = "random_string"
            modified_s = ", ".join(substrings)
        elif operation == "shuffle":
            random.shuffle(substrings)
            modified_s = ", ".join(substrings)
        elif operation == "randomize":
            random_positions = random.sample(range(len(substrings)), len(substrings))
            modified_s = ", ".join([substrings[i] for i in random_positions])
        modified_strings.append(modified_s)
    df["Modified String"] = modified_strings
    return df

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    default_seed = 42
    def test_case_1(self):
        # Test basic functionality
        data_list = ["lamp, bag, mirror", "table, chair, bag, lamp"]
        result = f_323(data_list, seed=self.default_seed)
        self.assertEqual(result["Original String"].tolist(), data_list)
        self.assertNotEqual(result["Original String"][0], result["Modified String"][0])
        self.assertNotEqual(result["Original String"][1], result["Modified String"][1])
    def test_case_2(self):
        # Test single string
        data_list = ["apple, orange, banana"]
        result = f_323(data_list, seed=self.default_seed)
        self.assertEqual(result["Original String"].tolist(), data_list)
        self.assertNotEqual(result["Original String"][0], result["Modified String"][0])
    def test_case_3(self):
        # Test single character
        data_list = ["a, b, c", "d, e, f", "g, h, i", "j, k, l", "m, n, o"]
        result = f_323(data_list, seed=self.default_seed)
        self.assertEqual(result["Original String"].tolist(), data_list)
        for idx in range(len(data_list)):
            self.assertNotEqual(
                result["Original String"][idx], result["Modified String"][idx]
            )
    def test_case_4(self):
        # Test whitespace sensitivity
        data_list = ["apple, apple, apple ", " apple,   apple ,   apple "]
        result = f_323(data_list, seed=self.default_seed)
        modified_strings = result["Modified String"].tolist()
        self.assertTrue(
            all(
                original != modified
                for original, modified in zip(data_list, modified_strings)
            ),
            "The function should treat substrings differently based on whitespace.",
        )
    def test_case_5(self):
        # Test case sensitivity
        data_list = ["apple, Apple", "APPLE, apple"]
        result = f_323(data_list, seed=self.default_seed)
        self.assertEqual(result["Original String"].tolist(), data_list)
        # Checking that modifications respect case sensitivity
        self.assertNotEqual(result["Modified String"][0], result["Modified String"][1])
    def test_case_6(self):
        # Test same random seed produces same results
        data_list = ["lamp, bag, mirror", "table, chair, bag, lamp"]
        result1 = f_323(data_list, seed=self.default_seed)
        result2 = f_323(data_list, seed=self.default_seed)
        pd.testing.assert_frame_equal(result1, result2)
    def test_case_7(self):
        # Test function integrity by calculating expected results with fixed random seed
        data_list = ["a, b, c", "d, e, f"]
        expected_modifications = ["b, c", "e, f, d"]
        result = f_323(data_list, seed=self.default_seed)
        self.assertEqual(
            result["Modified String"].tolist(),
            expected_modifications,
            "With a fixed seed, the modifications should be predictable and reproducible.",
        )
    def test_case_8(self):
        # Test invalid input handling
        for invalid_data_list in [
            [1, 2, 3],
            [None, "apple"],
            [None, None],
            [1, "orange", 3],
        ]:
            with self.assertRaises(TypeError):
                f_323(invalid_data_list, seed=self.default_seed)
    def test_case_9(self):
        # Test empty list input
        data_list = []
        result = f_323(data_list, seed=self.default_seed)
        self.assertTrue(
            result.empty,
            "The result should be an empty DataFrame for an empty input list.",
        )
    def test_case_10(self):
        # Test input list with an empty string
        data_list = [""]
        result = f_323(data_list, seed=self.default_seed)
        self.assertEqual(
            result["Modified String"].tolist(),
            [""],
            "An empty string should remain unchanged.",
        )
    def test_case_11(self):
        # Test input with a single substring (no commas)
        data_list = ["single"]
        result = f_323(data_list, seed=self.default_seed)
        self.assertEqual(
            result["Modified String"].tolist(),
            ["single"],
            "A single substring should remain unchanged.",
        )
