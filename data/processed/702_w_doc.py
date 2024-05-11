import pandas as pd
from sklearn.decomposition import PCA

def task_func(df):
    """
    Perform Principal Component Analysis (PCA) on the DataFrame and record the first two main components.
    
    Parameters:
    - df (DataFrame): The pandas DataFrame.
    
    Returns:
    - df_pca (DataFrame): The DataFrame with the first two principal components named 'PC1' and 'PC2' as columns.

    Requirements:
    - pandas
    - sklearn
    
    Example:
    >>> df = pd.DataFrame([[5.1, 3.5, 1.4], [4.9, 3.0, 1.4], [4.7, 3.2, 1.3]], columns = ['x', 'y', 'z'])
    >>> df_pca = task_func(df)
    >>> print(df_pca)
            PC1       PC2
    0  0.334781 -0.011992
    1 -0.187649 -0.142630
    2 -0.147132  0.154622
    """
    pca = PCA(n_components=2)
    df_pca = pca.fit_transform(df)
    df_pca = pd.DataFrame(df_pca, columns=['PC1', 'PC2'])
    return df_pca

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        df = pd.DataFrame([[0, 0], [0, 0]], columns = ['x', 'y'])
        df_pca = task_func(df)
        self.assertTrue('PC1' in df_pca.columns)
        self.assertTrue('PC2' in df_pca.columns)
        self.assertEqual(df_pca.shape, (2, 2))
        self.assertEqual(df_pca['PC1'].iloc[0], 0)
        self.assertEqual(df_pca['PC2'].iloc[0], 0)
        self.assertEqual(df_pca['PC1'].iloc[1], 0)
        self.assertEqual(df_pca['PC2'].iloc[1], 0)
    def test_case_2(self):
        df = pd.DataFrame([[1, 1], [1, 1]], columns = ['x', 'y'])
        df_pca = task_func(df)
        self.assertTrue('PC1' in df_pca.columns)
        self.assertTrue('PC2' in df_pca.columns)
        self.assertEqual(df_pca.shape, (2, 2))
        self.assertEqual(df_pca['PC1'].iloc[0], 0)
        self.assertEqual(df_pca['PC2'].iloc[0], 0)
        self.assertEqual(df_pca['PC1'].iloc[1], 0)
        self.assertEqual(df_pca['PC2'].iloc[1], 0)
    def test_case_3(self):
        df = pd.DataFrame([[1, 0], [0, 1]], columns = ['x', 'y'])
        df_pca = task_func(df)
        self.assertTrue('PC1' in df_pca.columns)
        self.assertTrue('PC2' in df_pca.columns)
        self.assertEqual(df_pca.shape, (2, 2))
        pca_new = PCA(n_components=2)
        df_pca_new = pca_new.fit_transform(df)
        self.assertEqual(df_pca['PC1'].iloc[0], df_pca_new[0, 0])
        self.assertEqual(df_pca['PC2'].iloc[0], df_pca_new[0, 1])
        self.assertEqual(df_pca['PC1'].iloc[1], df_pca_new[1, 0])
        self.assertEqual(df_pca['PC2'].iloc[1], df_pca_new[1, 1])
    def test_case_4(self):
        df = pd.DataFrame([[4, 3, 2, 1], [1, 2, 3, 4]], columns = ['x', 'y', 'z', 'w'])
        df_pca = task_func(df)
        self.assertTrue('PC1' in df_pca.columns)
        self.assertTrue('PC2' in df_pca.columns)
        self.assertEqual(df_pca.shape, (2, 2))
        pca_new = PCA(n_components=2)
        df_pca_new = pca_new.fit_transform(df)
        self.assertEqual(df_pca['PC1'].iloc[0], df_pca_new[0, 0])
    def test_case_5(self):
        df = pd.DataFrame([[1, 2, 3, 4], [4, 3, 2, 1]], columns = ['x', 'y', 'z', 'w'])
        df_pca = task_func(df)
        self.assertTrue('PC1' in df_pca.columns)
        self.assertTrue('PC2' in df_pca.columns)
        self.assertEqual(df_pca.shape, (2, 2))
        pca_new = PCA(n_components=2)
        df_pca_new = pca_new.fit_transform(df)
        self.assertEqual(df_pca['PC1'].iloc[0], df_pca_new[0, 0])
