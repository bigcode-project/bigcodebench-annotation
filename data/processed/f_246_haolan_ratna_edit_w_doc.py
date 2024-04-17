import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def f_246(df):
    """
    Perform a linear regression between "age" and "score" in the DataFrame, excluding rows with duplicate names.
    Plot the regression line and the scatter plot of the data.

    Parameters:
    df (DataFrame): The pandas DataFrame containing the data.

    Returns:
    tuple: A tuple containing the matplotlib.pyplot object and the axes object.

    Note:
    - The function use "Linear Regression" for the plot title.
    - The function use "Age" and "Score" as the xlabel and ylabel respectively.

    Requirements:
    - pandas
    - numpy
    - scipy.stats
    - matplotlib.pyplot

    Example:
    >>> data = pd.DataFrame([
                                {'Name': 'Alice', 'Age': 20, 'Score': 70},
                                {'Name': 'Bob', 'Age': 25, 'Score': 75},
                                {'Name': 'Eve', 'Age': 30, 'Score': 80}
                            ])
    >>> plt, ax = f_246(data)
    >>> ax.lines[0].get_xdata()
    20
    """

    df = df.drop_duplicates(subset='Name')

    slope, intercept, r_value, _, _ = stats.linregress(df['Age'], df['Score'])

    df['Age_up'] = intercept + slope * df['Age']
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    plt.scatter(df['Age'], df['Score'], label='Data')
    plt.plot(df['Age'].values, df['Age_up'].values, 'r', label='Fitted line')
    plt.xlabel('Age')
    plt.ylabel('Score')
    plt.title('Linear Regression')
    plt.legend()
    return plt, ax

import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestF1545(unittest.TestCase):
    def test_correct_data_handling(self):
        data = pd.DataFrame([
            {'Name': 'Alice', 'Age': 25, 'Score': 80},
            {'Name': 'Bob', 'Age': 30, 'Score': 85},
            {'Name': 'Alice', 'Age': 25, 'Score': 80},
            {'Name': 'Eve', 'Age': 35, 'Score': 90}
        ])
        plt, ax = f_246(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 1)  # Only one line for the regression
        self.assertEqual(len(ax.collections), 1)  # Only one collection for scatter plot
    def test_linear_regression(self):
        data = pd.DataFrame([
            {'Name': 'Alice', 'Age': 20, 'Score': 70},
            {'Name': 'Bob', 'Age': 25, 'Score': 75},
            {'Name': 'Eve', 'Age': 30, 'Score': 80}
        ])
        plt, ax = f_246(data)
        line = ax.lines[0]
        x_data, y_data = line.get_xdata(), line.get_ydata()
        self.assertTrue((y_data[1] - y_data[0]) / (x_data[1] - x_data[0]) > 0)  # Positive slope
    def test_plotting_elements(self):
        data = pd.DataFrame([
            {'Name': 'Alice', 'Age': 20, 'Score': 70},
            {'Name': 'Bob', 'Age': 25, 'Score': 75}
        ])
        plt, ax= f_246(data)
        self.assertEqual(ax.get_xlabel(), 'Age')
        self.assertEqual(ax.get_ylabel(), 'Score')
        self.assertEqual(ax.get_title(), 'Linear Regression')
    def test_empty_dataframe(self):
        data = pd.DataFrame([
            {'Name': 'Alice', 'Age': 20, 'Score': 70},
            {'Name': 'Bob', 'Age': 25, 'Score': 75}
        ])
        plt, ax = f_246(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 1)  # No line for regression
        self.assertEqual(len(ax.collections), 1)  # No scatter plot
    def test_missing_columns(self):
        data = pd.DataFrame([
            {'Name': 'Alice', 'Age': 20},
            {'Name': 'Bob', 'Age': 25}
        ])
        with self.assertRaises(KeyError):
            f_246(data)
