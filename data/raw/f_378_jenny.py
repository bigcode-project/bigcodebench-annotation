import re
import random
import pandas as pd


def f_378(data_list, seed=None):
    """
    Shuffle the substrings within each string in a given list.

    This function takes a list of comma-separated strings and splits each into substrings.
    It extracts substrings based on commas, removing leading and trailing whitespaces
    from each. Then, it shuffles these processed substrings within each string, and
    returns a pandas DataFrame with two columns: "Original String" and "Shuffled String".

    Parameters:
    data_list (list): The list of comma-separated strings.
    seed (int, optional): Seed for the random number generator. Default is None.

    Returns:
    DataFrame: A pandas DataFrame with columns 'Original String' and 'Shuffled String'.

    Requirements:
    - pandas
    - random
    - re

    Example:
    >>> f_378(['lamp, bag, mirror', 'table, chair'], seed=42)
         Original String    Shuffled String
    0  lamp, bag, mirror  bag, lamp, mirror
    1       table, chair       chair, table
    """
    if seed is not None:
        random.seed(seed)

    df = pd.DataFrame(data_list, columns=["Original String"])

    shuffled_strings = []
    for s in data_list:
        substrings = re.split("\s*,\s*", s)
        random.shuffle(substrings)
        shuffled_s = ", ".join(substrings)
        shuffled_strings.append(shuffled_s)

    df["Shuffled String"] = shuffled_strings

    return df


import unittest


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test basic case
        input_data = ["lamp, bag, mirror", "table, chair"]
        output_df = f_378(input_data)
        self.assertEqual(output_df["Original String"].iloc[0], "lamp, bag, mirror")
        self.assertEqual(output_df["Original String"].iloc[1], "table, chair")
        self.assertEqual(len(output_df["Shuffled String"].iloc[0].split(", ")), 3)
        self.assertEqual(len(output_df["Shuffled String"].iloc[1].split(", ")), 2)

    def test_case_2(self):
        # Test single character substrings
        input_data = ["A, B, C, D", "E, F, G"]
        output_df = f_378(input_data)
        self.assertEqual(output_df["Original String"].iloc[0], "A, B, C, D")
        self.assertEqual(output_df["Original String"].iloc[1], "E, F, G")
        self.assertEqual(len(output_df["Shuffled String"].iloc[0].split(", ")), 4)
        self.assertEqual(len(output_df["Shuffled String"].iloc[1].split(", ")), 3)

    def test_case_3(self):
        # Test single-item list
        input_data = ["word1, word2"]
        output_df = f_378(input_data)
        self.assertEqual(output_df["Original String"].iloc[0], "word1, word2")
        self.assertEqual(len(output_df["Shuffled String"].iloc[0].split(", ")), 2)

    def test_case_4(self):
        # Tests shuffling with an empty string
        input_data = [""]
        output_df = f_378(input_data)
        self.assertEqual(output_df["Original String"].iloc[0], "")
        self.assertEqual(output_df["Shuffled String"].iloc[0], "")

    def test_case_5(self):
        # Test shuffling single substring (no shuffling)
        input_data = ["single"]
        output_df = f_378(input_data)
        self.assertEqual(output_df["Original String"].iloc[0], "single")
        self.assertEqual(output_df["Shuffled String"].iloc[0], "single")

    def test_case_6(self):
        # Testing the effect of a specific random seed to ensure reproducibility
        input_data = ["a, b, c, d"]
        output_df1 = f_378(input_data, seed=42)
        output_df2 = f_378(input_data, seed=42)
        self.assertEqual(
            output_df1["Shuffled String"].iloc[0], output_df2["Shuffled String"].iloc[0]
        )

    def test_case_7(self):
        # Tests shuffling with varying spaces around commas
        input_data = ["one,two, three"]
        corrected_expected_shuffled = "two, one, three"
        output_df = f_378(input_data, seed=42)
        self.assertEqual(output_df["Original String"].iloc[0], "one,two, three")
        self.assertEqual(
            output_df["Shuffled String"].iloc[0], corrected_expected_shuffled
        )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
