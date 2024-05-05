import pandas as pd
import regex as re
import seaborn as sns
import matplotlib.pyplot as plt

COLUMN_NAMES = ["Name", "Email", "Age", "Country"]


def f_125(text):
    """
    Extract data from a text and create a Pandas DataFrame.
    The text contains several lines, each formatted as 'Name: John Doe, Email: john.doe@example.com, Age: 30, Country: USA'.
    Plot the age distribution using seaborn.

    The data is extracted using the regular expression pattern:
    "Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)"
    and the resulting DataFrame has columns: ['Name', 'Email', 'Age', 'Country']

    Parameters:
    text (str): The text to analyze.

    Returns:
    DataFrame: A pandas DataFrame with extracted data.

    Requirements:
    - pandas
    - regex
    - seaborn
    - matplotlib.pyplot

    Example:
    >>> text = 'Name: John Doe, Email: john.doe@example.com, Age: 30, Country: USA\nName: Jane Doe, Email: jane.doe@example.com, Age: 25, Country: UK'
    >>> df = f_125(text)
    >>> print(df)
           Name                 Email  Age Country
    0  John Doe  john.doe@example.com   30     USA
    1  Jane Doe  jane.doe@example.com   25      UK
    """
    pattern = r"Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)"
    matches = re.findall(pattern, text)
    data = []
    for match in matches:
        data.append(match[:-1])
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    df["Age"] = df["Age"].astype(int)
    sns.histplot(data=df, x="Age")
    plt.show()
    return df


import unittest


class TestCases(unittest.TestCase):
    """Test cases for the f_125 function."""

    def test_case_1(self):
        input_text = "Name: John Doe, Email: john.doe@example.com, Age: 30, Country: USA\nName: Jane Doe, Email: jane.doe@example.com, Age: 25, Country: UK"
        df = f_125(input_text)
        self.assertEqual(df.shape, (2, 4))
        self.assertListEqual(list(df.columns), ["Name", "Email", "Age", "Country"])
        self.assertListEqual(
            df.iloc[0].tolist(), ["John Doe", "john.doe@example.com", 30, "USA"]
        )
        self.assertListEqual(
            df.iloc[1].tolist(), ["Jane Doe", "jane.doe@example.com", 25, "UK"]
        )

    def test_case_2(self):
        input_text = (
            "Name: Alex Smith, Email: alex.smith@example.com, Age: 35, Country: Canada"
        )
        df = f_125(input_text)
        self.assertEqual(df.shape, (1, 4))
        self.assertListEqual(
            df.iloc[0].tolist(), ["Alex Smith", "alex.smith@example.com", 35, "Canada"]
        )

    def test_case_3(self):
        input_text = ""
        df = f_125(input_text)
        self.assertTrue(df.empty)

    def test_case_4(self):
        input_text = (
            "Name: Alex Smith, Email: alex.smith@example.com, Age: 35, Country: Canada"
        )
        df = f_125(input_text)
        self.assertEqual(df.shape, (1, 4))
        self.assertListEqual(
            df.iloc[0].tolist(), ["Alex Smith", "alex.smith@example.com", 35, "Canada"]
        )

    def test_case_5(self):
        input_text = """Name: Alex Smith, Email: alex.smith@example.com, Age: 35, Country: Canada
        Name: Bob Miller, Email: bob.miller@example.com, Age: 25, Country: USA
        Name: Anna Karin, Email: anna.karin@example.com, Age: 47, Country: Finland
        """
        df = f_125(input_text)
        self.assertEqual(df.shape, (3, 4))
        self.assertListEqual(list(df.columns), ["Name", "Email", "Age", "Country"])
        self.assertListEqual(
            df.iloc[0].tolist(), ["Alex Smith", "alex.smith@example.com", 35, "Canada"]
        )
        self.assertListEqual(
            df.iloc[1].tolist(), ["Bob Miller", "bob.miller@example.com", 25, "USA"]
        )
        self.assertListEqual(
            df.iloc[2].tolist(), ["Anna Karin", "anna.karin@example.com", 47, "Finland"]
        )


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
