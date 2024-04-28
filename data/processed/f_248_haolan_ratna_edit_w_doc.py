import matplotlib
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def f_222(df):
    """
    Standardize 'Age' and 'Score' columns in a pandas DataFrame, remove duplicate entries based on 'Name', and plot a scatter plot of these standardized values.

    Parameters:
    df (pandas.DataFrame): DataFrame containing 'Name', 'Age', and 'Score' columns.

    Returns:
    pandas.DataFrame: DataFrame with standardized 'Age' and 'Score', duplicates removed.
    matplotlib.axes.Axes: Axes object of the scatter plot.

    Note:
    - The function use "Scatter Plot of Standardized Age and Score" for the plot title.
    - The function use "Age (standardized)" and "Score (standardized)" as the xlabel and ylabel respectively.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot
    - sklearn.preprocessing

    Example:
    >>> import pandas as pd
    >>> data = pd.DataFrame([{'Name': 'James', 'Age': 30, 'Score': 85},{'Name': 'James', 'Age': 35, 'Score': 90},{'Name': 'Lily', 'Age': 28, 'Score': 92},{'Name': 'Sam', 'Age': 40, 'Score': 88},{'Name': 'Nick', 'Age': 50, 'Score': 80}])
    >>> modified_df, plot_axes = f_222(data)
    >>> modified_df.head()
        Name       Age     Score
    0  James -0.797724 -0.285365
    2   Lily -1.025645  1.312679
    3    Sam  0.341882  0.399511
    4   Nick  1.481487 -1.426825
    """

    df = df.drop_duplicates(subset='Name')

    scaler = StandardScaler()

    df[['Age', 'Score']] = scaler.fit_transform(df[['Age', 'Score']])

    plt.figure(figsize=(8, 6))
    plt.scatter(df['Age'], df['Score'])
    plt.xlabel('Age (standardized)')
    plt.ylabel('Score (standardized)')
    plt.title('Scatter Plot of Standardized Age and Score')
    ax = plt.gca()  # Get current axes
    
    return df, ax

import unittest
import pandas as pd
from faker import Faker
import matplotlib
class TestCases(unittest.TestCase):
    def setUp(self):
        # Using Faker to create test data
        fake = Faker()
        self.test_data = pd.DataFrame([{'Name': fake.name(), 'Age': fake.random_int(min=18, max=100), 'Score': fake.random_int(min=0, max=100)} for _ in range(10)])
    def test_duplicate_removal(self):
        df, _ = f_222(self.test_data)
        self.assertEqual(df['Name'].nunique(), df.shape[0])
    def test_standardization(self):
        df, _ = f_222(self.test_data)
        self.assertAlmostEqual(df['Age'].mean(), 0, places=1)
        self.assertAlmostEqual(int(df['Age'].std()), 1, places=1)
        self.assertAlmostEqual(df['Score'].mean(), 0, places=1)
        self.assertAlmostEqual(int(df['Score'].std()), 1, places=1)
    def test_return_types(self):
        data = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Score': 85},
            {'Name': 'James', 'Age': 35, 'Score': 90},
            {'Name': 'Lily', 'Age': 28, 'Score': 92},
            {'Name': 'Sam', 'Age': 40, 'Score': 88},
            {'Name': 'Nick', 'Age': 50, 'Score': 80}
        ])
        df, ax = f_222(data)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(ax, matplotlib.axes.Axes)
    def test_plot_contents(self):
        _, ax = f_222(self.test_data)
        self.assertEqual(ax.get_title(), 'Scatter Plot of Standardized Age and Score')
        self.assertEqual(ax.get_xlabel(), 'Age (standardized)')
        self.assertEqual(ax.get_ylabel(), 'Score (standardized)')
    def test_plot_data_points(self):
        df, ax = f_222(self.test_data)
        scatter = [child for child in ax.get_children() if isinstance(child, matplotlib.collections.PathCollection)]
        self.assertEqual(len(scatter), 1)
        self.assertEqual(len(scatter[0].get_offsets()), len(df))
