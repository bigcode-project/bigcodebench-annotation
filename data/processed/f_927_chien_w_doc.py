import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt


def f_730(data):
    """
    Processes a dataset containing salary information and experience, then plots normalized salary against experience.
    The function executes the following steps:
    1. Input Validation: Checks if the input data dictionary contains the required keys ('Salary_String' and 'Experience').
       Raises a ValueError if the necessary keys are missing.
    2. DataFrame Conversion: Converts the input data into a pandas DataFrame for easier manipulation.
    3. Empty Data Handling: Checks if the DataFrame is empty. If so, it returns a default Axes instance with
       labeled axes but no data plotted. This handles cases where there is no data to plot.
    4. Salary Conversion: Converts 'Salary_String' values from comma-separated strings to floats.
       It handles potential conversion errors by catching ValueErrors and re-raising them with a custom message.
    5. Salary Normalization: Applies Min-Max scaling to normalize the salary values. This step transforms
       the salary data into a range between 0 and 1, allowing for easier comparison and visualization.
    6. Data Plotting: Creates a scatter plot of the normalized salary against experience using matplotlib.
       The plot's axes are labeled accordingly.

    Parameters:
    - data (dict): A dictionary with two keys: 'Salary_String' and 'Experience'.
                   'Salary_String' should contain salary values as comma-separated strings.
                   'Experience' should contain corresponding experience values as integers.

    Returns:
    - matplotlib.axes.Axes: An Axes instance with the plotted scatter plot.

    Raises:
    - ValueError: If the input dictionary does not contain the required keys or if data conversion from string to float fails.

    Requirements:
    - pandas
    - sklearn
    - matplotlib

    Example:
    >>> ax = f_730({'Salary_String': ['1,000', '2,000', '3,000'], 'Experience': [1, 2, 3]})
    >>> print(ax.get_title())
    Normalized Salary vs Experience
    """
    if not all(key in data for key in ["Salary_String", "Experience"]):
        raise ValueError(
            "Input data must contain 'Salary_String' and 'Experience' keys."
        )
    df = pd.DataFrame(data)
    if df.empty:
        _, ax = plt.subplots()
        ax.set_title("Normalized Salary vs Experience")
        ax.set_xlabel("Experience")
        ax.set_ylabel("Normalized Salary")
        return ax
    try:
        df["Salary_Float"] = df["Salary_String"].str.replace(",", "").astype(float)
    except ValueError:
        raise ValueError("Error converting Salary_String to float.")
    scaler = MinMaxScaler()
    df["Normalized_Salary"] = scaler.fit_transform(df[["Salary_Float"]])
    _, ax = plt.subplots()
    ax.scatter(df["Experience"], df["Normalized_Salary"])
    ax.set_title("Normalized Salary vs Experience")
    ax.set_xlabel("Experience")
    ax.set_ylabel("Normalized Salary")
    return ax

import unittest
import pandas as pd
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for f_730."""
    def test_valid_data(self):
        """Test with valid data."""
        data = {"Salary_String": ["1,000", "2,000", "3,000"], "Experience": [1, 2, 3]}
        result = f_730(data)
        self.assertIsInstance(result, Axes)
    def test_missing_key(self):
        """Test with missing key in input dictionary."""
        data = {"Salary_String": ["1,000", "2,000", "3,000"]}
        with self.assertRaises(ValueError):
            f_730(data)
    def test_empty_data(self):
        """Test with empty data."""
        data = {"Salary_String": [], "Experience": []}
        result = f_730(data)
        self.assertIsInstance(result, Axes)
    def test_invalid_salary_format(self):
        """Test with invalid salary format."""
        data = {
            "Salary_String": ["1.000", "2,000", "Three Thousand"],
            "Experience": [1, 2, 3],
        }
        with self.assertRaises(ValueError):
            f_730(data)
    def test_mismatched_lengths(self):
        """Test with mismatched lengths of salary and experience arrays."""
        data = {"Salary_String": ["1,000", "2,000"], "Experience": [1, 2, 3]}
        with self.assertRaises(ValueError):
            f_730(data)
    def tearDown(self):
        plt.close("all")
