import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def task_func(df):
    '''
    Processes a DataFrame containing dates and lists of numbers. It converts the lists into separate columns,
    performs Principal Component Analysis (PCA), and returns the explained variance ratio of the principal components
    along with a bar chart visualizing this ratio. Returns 0,0 if the input DataFrame is empty.

    Parameters:
    df (DataFrame): A pandas DataFrame with columns 'Date' and 'Value'. 'Date' is a date column, and 'Value' contains 
                    lists of numbers.

    Returns:
    tuple: (explained_variance_ratio, ax)
           explained_variance_ratio (ndarray): The explained variance ratio of the principal components.
           ax (Axes): The matplotlib Axes object for the variance ratio bar chart.

    Note:
    - The function use "Explained Variance Ratio of Principal Components" for the plot title.
    - The function use "Principal Component" and "Explained Variance Ratio" as the xlabel and ylabel respectively.
    
    Requirements:
    - pandas
    - sklearn.decomposition
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
    >>> explained_variance_ratio, ax = task_func(df)
    >>> print(len(explained_variance_ratio))
    2
    '''
    if df.empty:
        return 0,0
    df['Date'] = pd.to_datetime(df['Date'])
    df = pd.concat([df['Date'], df['Value'].apply(pd.Series)], axis=1)
    pca = PCA()
    pca.fit(df.iloc[:,1:])
    explained_variance_ratio = pca.explained_variance_ratio_
    fig, ax = plt.subplots()
    ax.bar(range(len(explained_variance_ratio)), explained_variance_ratio)
    ax.set_title('Explained Variance Ratio of Principal Components')
    ax.set_xlabel('Principal Component')
    ax.set_ylabel('Explained Variance Ratio')
    return explained_variance_ratio, ax

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class TestCases(unittest.TestCase):
    def test_return_types(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        variance_ratio, plot = task_func(df)
        self.assertIsInstance(variance_ratio, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
    def test_known_input_output(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        variance_ratio, plot = task_func(df)
        self.assertIsInstance(variance_ratio, np.ndarray)
        self.assertIsInstance(plot, plt.Axes)
    def test_empty_dataframe(self):
        empty_df = pd.DataFrame()
        variance_ratio, _ = task_func(empty_df)
        self.assertEqual(variance_ratio, 0)
    def test_single_row_dataframe(self):
        single_row_df = pd.DataFrame([['2021-01-01', [8, 10, 12]]], columns=['Date', 'Value'])
        variance_ratio, _ = task_func(single_row_df)
        self.assertEqual(len(variance_ratio), 1)
    def test_plot_attributes(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        _, ax = task_func(df)
        self.assertEqual(ax.get_title(), 'Explained Variance Ratio of Principal Components')
        self.assertEqual(ax.get_xlabel(), 'Principal Component')
        self.assertEqual(ax.get_ylabel(), 'Explained Variance Ratio')
    def test_plot_explained_variance_ratio(self):
        df = pd.DataFrame([['2021-01-01', [8, 10, 12]], ['2021-01-02', [7, 9, 11]]], columns=['Date', 'Value'])
        variance_ratio, ax = task_func(df)
        bar_heights = [rect.get_height() for rect in ax.patches]
        self.assertListEqual(bar_heights, list(variance_ratio))
