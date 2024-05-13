import pandas as pd
import seaborn as sns

def task_func(data):
    """
    Draw and return a correlation matrix heatmap for a DataFrame containing numerical columns.
    The title of the heatmap is set to 'Correlation Matrix'.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing numerical columns to be used for correlation.

    Returns:
    matplotlib.axes._axes.Axes: The matplotlib Axes object representing the heatmap.

    Requirements:
    - pandas
    - seaborn

    Example:
    >>> data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    >>> ax = task_func(data)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>

    """

    df = pd.DataFrame(data)
    correlation_matrix = df.corr()
    ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    ax.set_title('Correlation Matrix')
    return ax

import unittest
import pandas as pd
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_2(self):
        data = {'a': [1, 2, 3], 'b': [-4, -5, -6], 'c': [-7, -8, -9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_3(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [-7, -8, -9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_4(self):
        data = {'a': [1, 1, 1], 'b': [2, 2, 2], 'c': [3, 3, 3]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_5(self):
        data = {'a': [1, 2, None], 'b': [4, None, 6], 'c': [None, 8, 9]}
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
