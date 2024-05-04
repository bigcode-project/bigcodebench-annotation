import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Constants
COLUMNS = ['Name', 'Age', 'Country', 'Score']

def f_55(df):
    """
    Generates a histogram of scores and a boxplot of scores by country from a pandas DataFrame. 
    It considers only unique names for both plots.

    Parameters:
    df (DataFrame): A pandas DataFrame containing the columns 'Name', 'Age', 'Country', and 'Score'.

    Returns:
    matplotlib.figure.Figure: A matplotlib figure containing the histogram and boxplot.

    Requirements:
    - matplotlib.pyplot
    - seaborn
    - pandas

    Note:
    - The function would return "Invalid input" string if the input is invalid (e.g., does not contain the required 'Name' key).
    - The histogram of scores has a title "Histogram of Scores".
    - The boxplot of scores has a title "Boxplot of Scores by Country".

    Example:
    >>> data = pd.DataFrame([{'Name': 'James', 'Age': 30, 'Country': 'USA', 'Score': 85}, {'Name': 'Nick', 'Age': 50, 'Country': 'Australia', 'Score': 80}])
    >>> fig = f_55(data)
    >>> axes = fig.get_axes()
    >>> print(axes[0].get_title())
    Histogram of Scores

    >>> print(f_55("not a dataframe"))
    Invalid input
    """
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"
    try:
        df = df.drop_duplicates(subset='Name')
        fig = plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        sns.histplot(df['Score'], bins=10)
        plt.title('Histogram of Scores')
        plt.subplot(1, 2, 2)
        sns.boxplot(x='Country', y='Score', data=df)
        plt.title('Boxplot of Scores by Country')
        plt.tight_layout()
        return fig
    except Exception as e:
        return "Invalid input"

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def test_valid_dataframe(self):
        # Test with a valid DataFrame with unique and duplicate 'Name' entries
        data = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Country': 'USA', 'Score': 85},
            {'Name': 'James', 'Age': 35, 'Country': 'USA', 'Score': 90},
            {'Name': 'Lily', 'Age': 28, 'Country': 'Canada', 'Score': 92},
            {'Name': 'Sam', 'Age': 40, 'Country': 'UK', 'Score': 88},
            {'Name': 'Nick', 'Age': 50, 'Country': 'Australia', 'Score': 80}
        ])
        fig = f_55(data)
        # Retrieve axes from the figure
        axes = fig.get_axes()
        # Assert titles
        self.assertEqual(axes[0].get_title(), 'Histogram of Scores')
        self.assertEqual(axes[1].get_title(), 'Boxplot of Scores by Country')
        
        # Assert data points in the boxplot
        for idx, country in enumerate(data['Country']):
            # Filter collection corresponding to the country
            for collection in axes[1].collections:
                if collection.get_label() == country:
                    self.assertIn(data['Score'][idx], collection.get_offsets()[:, 1])
                    break  # Exit inner loop once found
    def test_empty_dataframe(self):
        # Test with an empty DataFrame
        data = pd.DataFrame([])
        result = f_55(data)
        self.assertEqual(result, "Invalid input")
    def test_missing_columns(self):
        # Test with a DataFrame missing required columns
        data = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Score': 85},
            {'Name': 'Lily', 'Age': 28, 'Score': 92}
        ])
        result = f_55(data)
        self.assertEqual(result, "Invalid input")
    def test_non_dataframe_input(self):
        # Test with a non-DataFrame input
        data = "not a dataframe"
        result = f_55(data)
        self.assertEqual(result, "Invalid input")
    def test_plot_attributes(self):
        # Test if the plot contains the correct title, x-axis, y-axis, and data points
        data = pd.DataFrame([
            {'Name': 'James', 'Age': 30, 'Country': 'USA', 'Score': 85},
            {'Name': 'Nick', 'Age': 50, 'Country': 'Australia', 'Score': 80}
        ])
        fig = f_55(data)
        # Retrieve axes from the figure
        axes = fig.get_axes()
        # Assert titles
        self.assertEqual(axes[0].get_title(), 'Histogram of Scores')
        self.assertEqual(axes[1].get_title(), 'Boxplot of Scores by Country')
        
        # Assert data points in the boxplot
        for idx, country in enumerate(data['Country']):
            # Filter collection corresponding to the country
            for collection in axes[1].collections:
                if collection.get_label() == country:
                    self.assertIn(data['Score'][idx], collection.get_offsets()[:, 1])
                    break  # Exit inner loop once found
