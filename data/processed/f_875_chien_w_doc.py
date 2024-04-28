import matplotlib.pyplot as plt
import random
import string
import pandas as pd
import seaborn as sns

# Constants
LETTERS = list(string.ascii_lowercase)


def f_47(rows=1000, string_length=3):
    """
    Generate a dataframe of random strings and create a heatmap showing the correlation
    in the frequency of each letter in these strings.

    This function generates a specified number of random strings, each of a given length,
    and calculates the frequency of each letter in these strings. A heatmap of the 
    correlation matrix is then displayed, showing the co-occurrence frequencies of different 
    letters within these strings.

    If the number of rows specified is zero, the function will print a message indicating
    that no data is available to generate the heatmap and will return None. Otherwise, 
    it processes the DataFrame to convert the generated strings into a one-hot encoded format
    and then sums up these encodings to calculate the frequency of each letter.

    Parameters:
    - rows (int, optional): Number of random strings to generate. Must be non-negative. 
      Default is 1000. If set to 0, the function returns None after printing a message.
    - string_length (int, optional): Length of each random string. Must be non-negative. 
      Default is 3. A value of 0 results in the generation of empty strings.

    Returns:
    - matplotlib.axes._axes.Axes or None: A seaborn heatmap plot object if 
      data is generated; otherwise, None.

    Requirements:
    - random
    - string
    - pandas
    - seaborn
    - matplotlib

    Note
    - If no strings are generated (e.g., rows = 0), the 
       DataFrame will be empty. In this case, the function prints a message "No data to generate heatmap." and returns None.
    - If the DataFrame is not empty, each string is split into its 
       constituent letters, converted into one-hot encoded format, and then the frequency 
       of each letter is calculated by summing these encodings.
       
    Example:
    >>> ax = f_47(1000, 3)
    >>> ax.get_xlim()
    (0.0, 26.0)
    """

    # Generate random strings
    data = ["".join(random.choices(LETTERS, k=string_length)) for _ in range(rows)]

    # Create a DataFrame and compute letter frequency
    df = pd.DataFrame({"String": data})

    # Check if the DataFrame is empty
    if df.empty:
        print("No data to generate heatmap.")
        return None

    df = pd.get_dummies(df["String"].apply(list).explode()).groupby(level=0).sum()

    # Calculate the correlation matrix
    corr = df.corr()

    # Create and return the heatmap
    ax = sns.heatmap(corr, annot=True, fmt=".2f")
    plt.close()  # Close the plot to prevent it from showing during function call
    return ax

import unittest
import matplotlib.pyplot as plt
import random
class TestCases(unittest.TestCase):
    """Tests for f_47."""
    def test_default_parameters(self):
        """
        Test f_47 with default parameters (rows=1000, string_length=3).
        Verifies if the function returns a matplotlib Axes object.
        """
        random.seed(0)
        result = f_47()
        self.assertIsInstance(result, plt.Axes)
    def test_custom_rows(self):
        """
        Test f_47 with a custom number of rows.
        Verifies if the function still returns a matplotlib Axes object.
        """
        random.seed(1)
        result = f_47(rows=500)
        self.assertIsInstance(result, plt.Axes)
    def test_custom_string_length(self):
        """
        Test f_47 with a custom string length.
        Verifies if the function still returns a matplotlib Axes object.
        """
        random.seed(2)
        result = f_47(string_length=5)
        self.assertIsInstance(result, plt.Axes)
    def test_large_dataset(self):
        """
        Test f_47 with a large dataset.
        Verifies if the function can handle a large number of rows without errors.
        """
        random.seed(3)
        result = f_47(rows=10000, string_length=3)
        self.assertIsInstance(result, plt.Axes)
    def test_zero_rows(self):
        """
        Test f_47 with zero rows.
        Verifies if the function handles edge case of zero rows by returning None.
        """
        random.seed(4)
        result = f_47(rows=0)
        self.assertIsNone(result, "Function should return None for zero rows.")
    def tearDown(self):
        plt.close()
