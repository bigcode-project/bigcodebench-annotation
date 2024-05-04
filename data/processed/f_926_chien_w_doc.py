import pandas as pd
from scipy.stats import pearsonr


def f_414(data):
    """
    Calculates the Pearson correlation coefficient between numerical scores and categorical grades.

    This function performs three main tasks:
    1. Converts scores from string format to floats.
    2. Encodes categorical grades into numerical values based on their rank order.
    3. Computes the Pearson correlation coefficient between the numerical scores and the encoded grades.

    Parameters:
    - data (dict): A dictionary containing two keys:
                 - 'Score_String': A list of scores in string format.
                 - 'Grade': A list of corresponding grades in string format.
                 Each list under these keys must have the same length.

    Returns:
    - correlation (float): The Pearson correlation coefficient between the converted numerical scores and encoded grades.
           Returns NaN if the input data frame has less than 2 rows, as the correlation coefficient cannot be calculated in this case.

    Requirements:
    - pandas
    - scipy

    Example:
    >>> round(f_414({'Score_String': ['80.5', '85.7', '90.2'], 'Grade': ['B', 'B+', 'A-']}),2)
    -0.46
    """
    df = pd.DataFrame(data)
    if len(df) < 2:  # Check if the data frame has less than 2 rows
        return float("nan")  # or return None
    df["Score_Float"] = df["Score_String"].astype(float)
    df["Grade_Encoded"] = df["Grade"].astype("category").cat.codes
    correlation = pearsonr(df["Score_Float"], df["Grade_Encoded"])[0]
    return correlation

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    """Test cases for f_414"""
    def test_normal_operation(self):
        """
        Test normal operation with valid input.
        """
        data = {"Score_String": ["80.5", "85.7", "90.2"], "Grade": ["B", "B+", "A-"]}
        result = f_414(data)
        self.assertIsInstance(result, float)
    def test_empty_input(self):
        """
        Test the function with empty input.
        """
        data = {"Score_String": [], "Grade": []}
        result = f_414(data)
        self.assertTrue(pd.isna(result))
    def test_invalid_score_format(self):
        """
        Test the function with invalid score format.
        """
        data = {"Score_String": ["eighty", "85.7", "90.2"], "Grade": ["B", "B+", "A-"]}
        with self.assertRaises(ValueError):
            f_414(data)
    def test_mismatched_lengths(self):
        """
        Test the function with mismatched lengths of scores and grades.
        """
        data = {"Score_String": ["80.5", "85.7"], "Grade": ["B", "B+", "A-"]}
        with self.assertRaises(ValueError):
            f_414(data)
    def test_non_ordinal_grades(self):
        """
        Test the function with non-ordinal grade inputs.
        """
        data = {
            "Score_String": ["80.5", "85.7", "90.2"],
            "Grade": ["Pass", "Fail", "Pass"],
        }
        result = f_414(data)
        self.assertIsInstance(result, float)
