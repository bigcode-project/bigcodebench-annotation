import pandas as pd
import regex as re

def f_128(text):
   """
   Extract data from a text and create a Pandas DataFrame. The text contains several lines, each formatted as 'Score: 85, Category: Math'.

   Parameters:
   text (str): The text to analyze. 

   Returns:
   DataFrame: A pandas DataFrame with extracted data. Make sure to convert the scores in integer.

   Requirements:
   - pandas
   - regex

   Example:
   >>> text = "Score: 85, Category: Math\nScore: 90, Category: Science\nScore: 80, Category: Math"
   >>> df = f_128(text)
   >>> print(df)
      Score   Category
   0     85       Math
   1     90    Science
   2     80       Math
   """
   pattern = r"Score: (.*?), Category: (.*?)(\n|$)"
   matches = re.findall(pattern, text)
   data = [match[:2] for match in matches]  # Extracting only the score and category from each match
   df = pd.DataFrame(data, columns=['Score', 'Category'])
   df['Score'] = df['Score'].astype(int)
   return df

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_128 function."""
    def test_case_1(self):
        text = "Score: 85, Category: Math\nScore: 90, Category: Science\nScore: 80, Category: Math"
        df = f_128(text)
        self.assertEqual(len(df), 3)
        self.assertEqual(df["Score"].iloc[0], 85)
        self.assertEqual(df["Category"].iloc[0], "Math")
        self.assertEqual(df["Score"].iloc[1], 90)
        self.assertEqual(df["Category"].iloc[1], "Science")
        self.assertEqual(df["Score"].iloc[2], 80)
        self.assertEqual(df["Category"].iloc[2], "Math")

    def test_case_2(self):
        text = "Score: 70, Category: History"
        df = f_128(text)
        self.assertEqual(len(df), 1)
        self.assertEqual(df["Score"].iloc[0], 70)
        self.assertEqual(df["Category"].iloc[0], "History")

    def test_case_3(self):
        text = ""  # Empty string
        df = f_128(text)
        self.assertEqual(len(df), 0)  # Expecting an empty DataFrame

    def test_case_4(self):
        text = "Score: 70, Category: Chemistry"
        df = f_128(text)
        self.assertEqual(len(df), 1)
        self.assertEqual(df["Score"].iloc[0], 70)
        self.assertEqual(df["Category"].iloc[0], "Chemistry")

    def test_case_5(self):
        text = "Score: 70, Category: Literature\nScore: 37, Category: Mathematics\nScore: 90, Category: Japanese\nScore: 58, Category: Machine Learning"
        df = f_128(text)
        self.assertEqual(len(df), 4)
        self.assertEqual(df["Score"].iloc[0], 70)
        self.assertEqual(df["Category"].iloc[0], "Literature")
        self.assertEqual(df["Score"].iloc[1], 37)
        self.assertEqual(df["Category"].iloc[1], "Mathematics")
        self.assertEqual(df["Score"].iloc[2], 90)
        self.assertEqual(df["Category"].iloc[2], "Japanese")
        self.assertEqual(df["Score"].iloc[3], 58)
        self.assertEqual(df["Category"].iloc[3], "Machine Learning")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests() 