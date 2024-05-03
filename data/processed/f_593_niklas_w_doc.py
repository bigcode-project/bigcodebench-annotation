import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def f_721(data, columns, target_column):
    """
    Perform a logistic regression on a DataFrame to predict a specific target column.
    
    Parameters:
    - data (numpy.array): The input data as a NumPy array.
    - columns (list): The list of column names.
    - target_column (str): The target column name.

    Returns:
    - accuracy (float): The accuracy of the logistic regression model.

    Requirements:
    - pandas
    - sklearn
    
    Example:
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> data = np.random.randint(0, 100, size=(100, 4))  # Using np to generate random data
    >>> columns = ['A', 'B', 'C', 'target']
    >>> f_721(data, columns, 'target')
    0.0
    """
    df = pd.DataFrame(data, columns=columns)
    if target_column not in df.columns:
        raise ValueError('Target column does not exist in DataFrame')

    X = df.drop(columns=target_column)  # Operate directly on the DataFrame
    y = df[target_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy

import unittest
import numpy as np
class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data = np.array([[1, 4, 0], [2, 5, 1], [3, 6, 0]])
        columns = ['A', 'B', 'C']
        self.assertEqual(f_721(data, columns, 'C'), 0.0)
    def test_case_2(self):
        data = np.array([[1, 2, 3, -10], [4, 5, 6, -10], [1, 1, 1, 0]])
        columns = ['A', 'B', 'C', 'D']
        self.assertEqual(f_721(data, columns, 'C'), 0.0)
    def test_case_3(self):
        data = np.array([
            [60, 45, 1],
            [40, 55, 1],
            [30, 71, 1],
            [20, 82, 1],
            [10, 95, 1],
            [59, 40, 0],
            [39, 60, 1],
            [29, 70, 1],
            [19, 80, 1],
            [9,  89, 1]
        ])
        columns = ['A', 'B', 'C']
        self.assertEqual(f_721(data, columns, 'C'), 1.0)
    def test_case_4(self):
        data = np.array([
            [-10, 2, 3, -10],
            [-10, 5, 6, 10],
            [-10, -2, -1, -10],
            [-10, 1, 0, -10],
            [-10, 8, 9, 10],
            [-10, -5, -4, -10]
        ])
        columns = ['A', 'B', 'C', 'D']
        self.assertEqual(f_721(data, columns, 'D'), 1.0)
    def test_case_5(self):
        data = np.array([
            [-10, 2, 3, -10, 1],
            [-10, 5, 6, 10, 1],
            [-10, -2, -1, -10, 1],
            [-10, 1, 0, -10, 1],
            [-10, 8, 9, 10, 1],
            [-10, -5, -4, -10, 1]
        ])
        columns = ['A', 'B', 'C', 'D', 'E']
        self.assertEqual(f_721(data, columns, 'D'), 1.0)
