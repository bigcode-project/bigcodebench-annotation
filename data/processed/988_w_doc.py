import pandas as pd
import seaborn as sns


def task_func(data=None):
    """
    Converts string-formatted weights to floats and plots a scatter plot of weight against height.

    This function takes a dictionary with two keys: 'Weight_String' and 'Height'. The 'Weight_String' key should 
    contain a list of weight values in string format, while the 'Height' key should have a list of corresponding 
    height values in numerical format. If the input dictionary is not provided, the function uses a default dataset.
    The function then converts the string-formatted weights into float, and plots a scatter plot to visualize 
    the relationship between weight and height.
       
    Parameters:
    - data (dict, optional): A dictionary with keys 'Weight_String' and 'Height'. 'Weight_String' is expected to be 
                           a list of weight values in string format (e.g., ['60.5', '65.7']), and 'Height' is expected 
                           to be a list of corresponding numerical height values (e.g., [160, 165]). If no dictionary 
                           is provided, a default dataset with predetermined values is used.
                           Default dictionary:
                           {
                               'Weight_String': ['60.5', '65.7', '70.2', '75.9', '80.1'],
                               'Height': [160, 165, 170, 175, 180]
                           }

    Returns:
    - ax (matplotlib.axes._axes.Axes): A scatter plot with weight on the x-axis and height on the y-axis, titled "Weight vs Height".

    Raises:
    - ValueError: If any of the values in the 'Weight_String' key are not formatted as strings. This validation ensures 
                that the weight data is in the expected format for conversion to float.

    Requirements:
    - pandas
    - seaborn

    Example:
    >>> ax = task_func()
    >>> print(ax.get_title())
    Weight vs Height
    """
    if data is None:
        data = {
            "Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"],
            "Height": [160, 165, 170, 175, 180],
        }
    df = pd.DataFrame(data)
    if not all(isinstance(weight, str) for weight in df["Weight_String"]):
        raise ValueError("Weights must be provided as strings.")
    df["Weight_Float"] = df["Weight_String"].astype(float)
    ax = sns.scatterplot(data=df, x="Weight_Float", y="Height")
    ax.set_title("Weight vs Height")
    return ax

import unittest
import pandas as pd
from matplotlib.axes import Axes
class TestCases(unittest.TestCase):
    """Test cases for task_func"""
    def test_default_data(self):
        """Test task_func with its default data."""
        result = task_func()
        self.assertIsInstance(result, Axes)
    def test_custom_data(self):
        """Test task_func with custom data."""
        custom_data = {
            "Weight_String": ["50.5", "55.7", "60.2"],
            "Height": [150, 155, 160],
        }
        result = task_func(custom_data)
        self.assertIsInstance(result, Axes)
    def test_incorrect_data_type(self):
        """Test task_func with incorrect data types in Weight_String."""
        incorrect_data = {
            "Weight_String": [
                60.5,
                65.7,
                70.2,
            ],  # Intentionally using floats instead of strings
            "Height": [160, 165, 170],
        }
        with self.assertRaises(ValueError):
            task_func(incorrect_data)
    def test_empty_data(self):
        """Test task_func with empty data."""
        empty_data = {"Weight_String": [], "Height": []}
        result = task_func(empty_data)
        self.assertIsInstance(result, Axes)
    def test_mismatched_data_length(self):
        """Test task_func with mismatched lengths of Weight_String and Height."""
        mismatched_data = {
            "Weight_String": ["60.5", "65.7"],  # Less weights than heights
            "Height": [160, 165, 170],
        }
        with self.assertRaises(ValueError):
            task_func(mismatched_data)
