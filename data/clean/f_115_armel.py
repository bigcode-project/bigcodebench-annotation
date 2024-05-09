import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def f_115(df: pd.DataFrame):
    """
    Perform PCA on a DataFrame (excluding non-numeric columns) and draw a scatter plot of the first two main components. The principal columns should be name 'Component 1' and 'Component 2'.
    Missing values are replaced by column's average.

    Parameters:
    df (DataFrame): The pandas DataFrame.

    Returns:
    DataFrame: A pandas DataFrame with the first two principal components. The columns should be 'principal component 1' and 'principal component 2'.
    Axes: A matplotlib Axes object representing the scatter plot. The xlabel should be 'principal component' and the ylabel 'principal component 2'.

    Requirements:
    - pandas
    - numpy
    - sklearn.decomposition.PCA
    - seaborn
    - matplotlib

    Example:
    >>> df = pd.DataFrame([[1,2,3],[4,5,6],[7.0,np.nan,9.0]], columns=["c1","c2","c3"])
    >>> principalDf, ax = f_115(df)
    >>> print(principalDf)
       Component 1  Component 2
    0     4.450915    -0.662840
    1    -0.286236     1.472436
    2    -4.164679    -0.809596
    """
    # Select only numeric columns
    df_numeric = df.select_dtypes(include=[np.number])
    # Replace missing values
    df_numeric = df_numeric.fillna(df_numeric.mean(axis=0))
    # Perform PCA
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(df_numeric)
    principalDf = pd.DataFrame(
        data=principalComponents,
        columns=["Component 1", "Component 2"],
    )

    # Plot scatter plot
    ax = sns.scatterplot(data=principalDf, x="Component 1", y="Component 2")
    plt.show()
    return principalDf, ax


import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_115 function."""

    def test_case_1(self):
        df = pd.DataFrame(
            [[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["c1", "c2", "c3"]
        )
        principalDf, ax = f_115(df)
        self.assertTrue("Component 1" in principalDf.columns)
        self.assertTrue("Component 2" in principalDf.columns)
        self.assertEqual(principalDf.shape, (3, 2))
        self.assertEqual(ax.get_xlabel(), "Component 1")
        self.assertEqual(ax.get_ylabel(), "Component 2")

    def test_case_2(self):
        df = pd.DataFrame(
            {
                "A": [1, 2.5, 3, 4.5, 5],
                "B": [5, 4.5, np.nan, 2, 1.5],
                "C": [2.5, 3, 4, 5.5, 6],
                "categoral_1": ["A", "B", "B", "B", "A"],
                "categoral_2": ["0", "1", "1", "0", "1"],
            }
        )
        principalDf, ax = f_115(df)
        self.assertTrue("Component 1" in principalDf.columns)
        self.assertTrue("Component 2" in principalDf.columns)
        self.assertEqual(principalDf.shape, (5, 2))
        self.assertEqual(ax.get_xlabel(), "Component 1")
        self.assertEqual(ax.get_ylabel(), "Component 2")

    def test_case_3(self):
        df = pd.DataFrame(
            {
                "col1": [None, 17, 11, None],
                "col2": [0, 4, 15, 27],
                "col3": [7, 9, 3, 8],
            }
        )
        principalDf, ax = f_115(df)
        self.assertTrue("Component 1" in principalDf.columns)
        self.assertTrue("Component 2" in principalDf.columns)
        self.assertEqual(principalDf.shape, (4, 2))
        self.assertEqual(ax.get_xlabel(), "Component 1")
        self.assertEqual(ax.get_ylabel(), "Component 2")

    def test_case_4(self):
        df = pd.DataFrame(
            {
                "c1": [np.nan] * 9 + [10],
                "c2": [np.nan] * 8 + [20, 30],
                "c3": [np.nan] * 7 + [40, 50, 60],
            }
        )
        principalDf, ax = f_115(df)
        self.assertTrue("Component 1" in principalDf.columns)
        self.assertTrue("Component 2" in principalDf.columns)
        self.assertEqual(principalDf.shape, (10, 2))
        self.assertEqual(ax.get_xlabel(), "Component 1")
        self.assertEqual(ax.get_ylabel(), "Component 2")

    def test_case_5(self):
        df = pd.DataFrame({"c1": [1] * 10, "c2": [2] * 10, "c3": [3] * 10})
        principalDf, ax = f_115(df)
        self.assertTrue("Component 1" in principalDf.columns)
        self.assertTrue("Component 2" in principalDf.columns)
        self.assertEqual(principalDf.shape, (10, 2))
        self.assertEqual(ax.get_xlabel(), "Component 1")
        self.assertEqual(ax.get_ylabel(), "Component 2")


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
