import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

def f_3122(file_path='arena.csv', target_column='Index', seed=42):
    """
    Trains a random forest model on data from a CSV file, using one column as the target variable (y) 
    and the rest as features (X), and visualizes the feature importances in a bar plot. This function 
    also handles missing values by dropping rows with any NaN values.

    Parameters:
    - file_path (str): Path to the CSV file containing the dataset. Defaults to 'arena.csv'.
    - target_column (str): Name of the column to be used as the target variable (y). Defaults to 'Index'.
    - seed (int): Seed for the random state of the RandomForestClassifier to ensure reproducibility. Defaults to 42.

    Returns:
    - matplotlib.axes.Axes: Axes object displaying the bar plot of feature importances.
    - numpy.ndarray: Array containing the feature importances derived from the random forest model.

    Raises:
    - FileNotFoundError: Raised if the specified file_path does not lead to a valid file.
    - ValueError: Raised if the specified target_column is not found in the CSV file's columns, or if the input data contains NaN, infinity or a value too large for dtype('float32').

    Requirements:
    - pandas: For loading and manipulating the CSV file.
    - sklearn.ensemble.RandomForestClassifier: For training the random forest model.
    - seaborn and matplotlib for plotting the feature importances.
    - numpy 
    - os 

    Example:
    The CSV file format:
        Index,Score1,Score2,Score3
        1,10,20,30
        2,15,25,35
        3,20,30,40
    
    >>> file_path = 'arena.csv'
    >>> create_dummy_file(file_path)
    >>> ax, importances = f_3122(file_path, 'Index') # This will train a random forest model predicting 'Index' from 'Score1', 'Score2', and 'Score3', then plot and return the importances of 'Score1', 'Score2', and 'Score3' as features (X).
    >>> os.remove(file_path)
    """
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    
    df = pd.read_csv(file_path)
    
    if target_column not in df.columns:
        raise ValueError(f"The specified target column '{target_column}' does not exist in the CSV file.")
    
    # Drop rows with any NaN values
    df_cleaned = df.dropna()

    X = df_cleaned.drop(target_column, axis=1)
    y = df_cleaned[target_column]
    
    # Option to scale features if needed
    # scaler = StandardScaler()
    # X_scaled = scaler.fit_transform(X)
    
    clf = RandomForestClassifier(random_state=seed)
    clf.fit(X, y)
    importances = clf.feature_importances_
    
    fig, ax = plt.subplots()
    sns.barplot(x=X.columns, y=importances, ax=ax)
    ax.set_title('Feature Importances')
    
    return ax, importances


import unittest
import pandas as pd
import os
import numpy as np
from numpy.testing import assert_array_almost_equal

def create_dummy_file(file_path):
    data = {
        'Index': [1, 2, 3],
        'Score1': [10, 15, 20],
        'Score2': [20, 25, 30],
        'Score3': [30, 35, 40]
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)


class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a dummy CSV for testing
        data = {
            'Index': [1, 2, 3],
            'Score1': [10, 15, 20],
            'Score2': [20, 25, 30],
            'Score3': [30, 35, 40]
        }
        df = pd.DataFrame(data)
        df.to_csv('dummy_arena.csv', index=False)
        
        # Create a more complex dummy CSV for advanced testing
        np.random.seed(42)  # For reproducibility
        complex_data = {
            'Index': np.arange(1, 11),
            'Feature1': np.random.randint(-10, 50, 10),
            'Feature2': np.random.normal(0, 5, 10),
            'Feature3': np.random.uniform(25, 75, 10),
            'Feature4': np.random.lognormal(0, 1, 10),
            'Feature5': np.linspace(10, 100, 10),
            'Outcome': np.random.choice([0, 1], 10)  # Binary outcome for classification
        }
        complex_df = pd.DataFrame(complex_data)
        # Introduce some missing values
        complex_df.loc[4:6, 'Feature2'] = np.nan
        complex_df.loc[2:3, 'Feature4'] = np.nan
        complex_df.to_csv('complex_dummy_arena.csv', index=False)

    @classmethod
    def tearDownClass(cls):
        os.remove('dummy_arena.csv')
        os.remove('complex_dummy_arena.csv')

    def test_feature_importances(self):
        # Test the function for normal functionality
        ax, importances = f_3122('dummy_arena.csv', 'Index')
        self.assertEqual(len(importances), 3)  # Expecting 3 features
        self.assertTrue(np.all(importances >= 0))  # Importances should be non-negative
        expect = np.array([0.35294118, 0.36470588, 0.28235294])
        assert_array_almost_equal(importances, expect, decimal=6)
        
    def test_file_not_found(self):
        # Test FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            f_3122('nonexistent.csv', 'Index')

    def test_invalid_target_column(self):
        # Test ValueError for invalid target column
        with self.assertRaises(ValueError):
            f_3122('dummy_arena.csv', 'NonexistentColumn')
            
    
    def test_feature_importances1(self):
        # Test the function for normal functionality
        ax, importances = f_3122('complex_dummy_arena.csv', 'Index')
        print(importances)
        expect = np.array([0.16335979, 0.22973545, 0.15900794, 0.18597884, 0.19796296, 0.06395503])
        assert_array_almost_equal(importances, expect, decimal=6)

def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()
