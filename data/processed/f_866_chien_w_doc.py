import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def f_866(dataframe):
    """
    Calculate the correlation matrix of a DataFrame and plot a scatter plot for the pair of columns with the highest absolute correlation.

    Parameters:
    - dataframe (pd.DataFrame): The DataFrame containing numeric columns for correlation calculation.

    Returns:
    - ax (plt.Axes): The scatter plot of the pair of columns with the highest absolute correlation.

    Requirements:
    - pandas
    - numpy
    - matplotlib

    Exception Handling:
    - Raises ValueError if the input DataFrame is empty.
    - Raises TypeError if any column in the DataFrame is non-numeric.
    - Raises ValueError if the DataFrame has fewer than two columns.

    Example:
    >>> df = pd.DataFrame({
    ...     'A': np.random.rand(100),
    ...     'B': np.random.rand(100),
    ...     'C': np.random.rand(100)
    ... })
    >>> ax = f_866(df)
    >>> print(ax)
    Axes(0.125,0.11;0.775x0.77)
    """

    if dataframe.empty:
        raise ValueError("DataFrame is empty.")
        
    if not all(dataframe.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise TypeError("All columns must be numeric for correlation calculation.")

    if dataframe.shape[1] < 2:
        raise ValueError("DataFrame must have at least two columns for correlation calculation.")

    # Explicit use of pd.DataFrame.corr() to calculate the correlation matrix
    corr_matrix = pd.DataFrame.corr(dataframe)
    abs_corr_matrix = corr_matrix.abs()

    # Finding the pair of columns with the highest absolute correlation
    highest_corr_value = abs_corr_matrix.unstack().dropna().nlargest(2).iloc[-1]
    max_corr_pair = np.where(abs_corr_matrix == highest_corr_value)

    # Extracting column names for the highest correlation
    column_x = dataframe.columns[max_corr_pair[0][0]]
    column_y = dataframe.columns[max_corr_pair[1][0]]

    # Using plt to plot the scatter plot
    plt.figure(figsize=(10, 6))  # Creating a figure
    plt.scatter(dataframe[column_x], dataframe[column_y])  # Plotting the scatter plot
    plt.title(f"Scatter plot between {column_x} and {column_y}")  # Setting the title
    plt.xlabel(column_x)  # Setting the x-axis label
    plt.ylabel(column_y)  # Setting the y-axis label
    plt.show()  # Displaying the figure

    return plt.gca()  # Returning the current Axes object for further use

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    """Test cases for the function f_866."""
    def test_high_correlation(self):
        """
        Test if the function correctly identifies and plots the pair of columns with the highest positive correlation.
        """
        np.random.seed(0)  # Set a fixed seed for reproducibility
        df = pd.DataFrame(
            {"A": np.arange(100), "B": np.arange(100) * 2, "C": np.random.rand(100)}
        )
        ax = f_866(df)
        corr = df.corr()
        abs_corr = corr.abs()
        max_corr = abs_corr.unstack().dropna().nlargest(3).iloc[-1]
        expected_pair = np.where(abs_corr == max_corr)
        expected_labels = (
            df.columns[expected_pair[0][0]],
            df.columns[expected_pair[1][0]],
        )
        self.assertEqual((ax.get_xlabel(), ax.get_ylabel()), expected_labels)
    def test_no_correlation(self):
        """
        Test if the function handles a case where there is no significant correlation between columns.
        """
        np.random.seed(1)
        df = pd.DataFrame(
            {
                "A": np.random.rand(100),
                "B": np.random.rand(100),
                "C": np.random.rand(100),
            }
        )
        ax = f_866(df)
        self.assertIsInstance(ax, plt.Axes)
    def test_negative_correlation(self):
        """
        Test if the function correctly identifies and plots the pair of columns with the highest absolute correlation,
        including negative correlations.
        """
        np.random.seed(2)
        df = pd.DataFrame(
            {"A": np.arange(100), "B": np.random.rand(100), "C": -np.arange(100) + 50}
        )
        ax = f_866(df)
        corr = df.corr()
        # Get the pair with the highest absolute correlation excluding self-correlations
        abs_corr = corr.abs()
        max_corr = abs_corr.unstack().dropna().nlargest(3).iloc[-1]
        expected_pair = np.where(abs_corr == max_corr)
        expected_labels = (
            df.columns[expected_pair[0][0]],
            df.columns[expected_pair[1][0]],
        )
        self.assertEqual((ax.get_xlabel(), ax.get_ylabel()), expected_labels)
    def test_single_column(self):
        """
        Test if the function raises a ValueError when provided with a DataFrame containing only one column.
        """
        np.random.seed(3)
        df = pd.DataFrame({"A": np.random.rand(100)})
        with self.assertRaises(ValueError):
            f_866(df)
    def test_non_numeric_columns(self):
        """
        Test if the function raises a TypeError when provided with a DataFrame containing non-numeric columns.
        """
        np.random.seed(4)
        df = pd.DataFrame(
            {"A": np.random.rand(100), "B": ["text"] * 100, "C": np.random.rand(100)}
        )
        with self.assertRaises(TypeError):
            f_866(df)
    def test_empty_dataframe(self):
        """
        Test if the function raises a ValueError when provided with an empty DataFrame.
        """
        df = pd.DataFrame()  # Create an empty DataFrame
        with self.assertRaises(ValueError):
            f_866(df)
