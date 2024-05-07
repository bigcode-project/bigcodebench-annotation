import pandas as pd
from sklearn.preprocessing import StandardScaler


def f_61(data):
    """Scales numeric columns of a data dictionary using the StandardScaler.

    This function scales the numeric columns of a dataframe using the StandardScaler from scikit-learn.
    Non-numeric columns remain unchanged. If a column contains mixed data types, it tries to convert the entire column
    to float. If any value in the column cannot be converted to float, the entire column is left unchanged.

    Requirements:
    - pandas
    - sklearn.preprocessing.StandardScaler
    
    Parameters:
    - data (dict): Input data.

    Returns:
    - pd.DataFrame: Dataframe with scaled numeric columns.

    Example:
    >>> result = f_61({'x': [10, 20, 30, 40]})
    >>> result
              x
    0 -1.341641
    1 -0.447214
    2  0.447214
    3  1.341641
    >>> result2 = f_61({'a': [10.5, 23.4, 15.6, 78.9],'b': [45.6, 67.8, 89.0, 12.3],'c': ['apple', 'banana', 'cherry', 'date']})
    >>> result2
              a         b       c
    0 -0.788098 -0.284409   apple
    1 -0.317428  0.497496  banana
    2 -0.602019  1.244180  cherry
    3  1.707546 -1.457267    date
    """
    dataframe = pd.DataFrame(data)
    scaler = StandardScaler()
    for column in dataframe.columns:
        if dataframe[column].dtype in ["float64", "int64"]:
            dataframe[column] = scaler.fit_transform(
                dataframe[column].values.reshape(-1, 1)
            )
        else:
            converted_column = dataframe[column].apply(pd.to_numeric, errors="coerce")
            if (
                not converted_column.isna().all()
            ):  # If all values are convertible to float
                dataframe[column] = scaler.fit_transform(
                    converted_column.values.reshape(-1, 1)
                )
    return dataframe

import unittest
import numpy as np
import pandas as pd
class TestCases(unittest.TestCase):
    def test_case_1(self):
        """Test the correctness of the scaling applied by the function."""
        # Creating a sample dataframe with three numeric columns
        data = {
                "a": [10.5, 23.4, 15.6, 78.9],
                "b": [45.6, 67.8, 89.0, 12.3],
                "c": [12.3, 45.6, 78.9, 0.1],
            }
        df = pd.DataFrame(
            data
        )
        result = f_61(data)
        # Checking if the mean of scaled columns is approximately 0 and standard deviation is approximately 1
        self.assertTrue(np.isclose(result["a"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(result["b"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(np.std(result["a"]), 1, atol=1e-2))
        self.assertTrue(np.isclose(np.std(result["b"]), 1, atol=1e-2))
    def test_case_2(self):
        """Test with an empty DataFrame."""
        # Creating an empty dataframe
        data = {}
        df = pd.DataFrame(data)
        result = f_61(data)
        # Ensuring the result is also an empty dataframe
        self.assertTrue(result.empty)
    def test_case_3(self):
        """Test with a DataFrame that doesn't have any columns to scale."""
        # Creating a dataframe with a single non-numeric column
        data = {"c": ["foo", "bar"]}
        df = pd.DataFrame(data)
        result = f_61(data)
        # Ensuring the output dataframe is unchanged
        pd.testing.assert_frame_equal(result, df, check_dtype=False)
    def test_case_4(self):
        """Test with a DataFrame where all columns are to be scaled."""
        # Creating a dataframe with two numeric columns
        data = {"a": [10.5, 23.4, 15.6, 78.9], "b": [45.6, 67.8, 89.0, 12.3]}
        df = pd.DataFrame(
            data
        )
        result = f_61(data)
        # Checking if the mean of scaled columns is approximately 0 and standard deviation is approximately 1
        self.assertTrue(np.isclose(result["a"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(result["b"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(np.std(result["a"]), 1, atol=1e-2))
        self.assertTrue(np.isclose(np.std(result["b"]), 1, atol=1e-2))
    def test_case_5(self):
        """Test with a DataFrame with single rows."""
        # Creating a dataframe with a single row and three columns
        data = {"a": [5.5], "b": [8.6], "c": [7.7]}
        df = pd.DataFrame(data)
        result = f_61(data)
        self.assertDictEqual(result.to_dict(), {'a': {0: 0.0}, 'b': {0: 0.0}, 'c': {0: 0.0}})
    def test_case_6(self):
        """Test with a DataFrame with mixed datatypes."""
        # Creating a dataframe with mixed data types (both floats and strings) in columns
        data = {
                "a": [10.5, 23.4, 15.6, "78.9"],
                "b": [45.6, "67.8", 89.0, 12.3],
                "c": [12.3, 45.6, 78.9, "0.1"],
            }
        df = pd.DataFrame(
            data
        )
        result = f_61(data)
        # Checking if the mean of scaled columns is approximately 0 and standard deviation is approximately 1
        self.assertTrue(np.isclose(result["a"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(result["b"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(np.std(result["a"]), 1, atol=1e-2))
        self.assertTrue(np.isclose(np.std(result["b"]), 1, atol=1e-2))
    def test_case_7(self):
        """Test with a DataFrame with negative values."""
        # Creating a dataframe with negative values in columns
        data = {"a": [-1, -2, -3, -4], "b": [-4, -5, -6, -7], "c": [-7, -8, -9, -10]}
        df = pd.DataFrame(
            data
        )
        result = f_61(data)
        # Checking if the mean of scaled columns is approximately 0 and standard deviation is approximately 1
        self.assertTrue(np.isclose(result["a"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(result["b"].mean(), 0, atol=1e-7))
        self.assertTrue(np.isclose(np.std(result["a"]), 1, atol=1e-2))
        self.assertTrue(np.isclose(np.std(result["b"]), 1, atol=1e-2))
