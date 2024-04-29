import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

def f_999(data):
    ''' 
    Train a simple linear regression model based on the given data and evaluate the model by calculating the mean square error.

    Parameters:
    data (dict): The hours of study and scores.

    Returns:
    float: The mean squared error.

    Requirements:
    - pandas
    - sklearn.model_selection
    - sklearn.linear_model
    - numpy

    Example:
    >>> f_938(DATA)
    6.182284986260905
    '''
    df = pd.DataFrame(data)
    
    X = df[['Hours']]
    y = df['Scores']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    mse = np.mean((y_test - predictions) ** 2)
    
    return mse
    

import unittest
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        data = {
            'Hours': [2.5, 5.1, 3.2, 8.5, 3.5],
            'Scores': [21, 47, 27, 75, 30],
        }
        mse = f_999(data)
        self.assertIsInstance(mse, float)

    def test_case_2(self):
        data = {
            'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2],
            'Scores': [21, 47, 27, 75, 30, 20, 88],
        }
        mse = f_999(data)
        self.assertIsInstance(mse, float)
        
    def test_case_3(self):
        data = {
            'Hours': [2.5, 3.5, 1.5],
            'Scores': [21, 30, 20],
        }
        mse = f_999(data)
        self.assertIsInstance(mse, float)

    def test_case_4(self):
        data = {
            'Hours': [5.5, 8.3, 2.7],
            'Scores': [60, 81, 25],
        }
        mse = f_999(data)
        self.assertIsInstance(mse, float)

    def test_case_5(self):
        data = {
            'Hours': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7],
            'Scores': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25],
        }
        mse = f_999(data)
        self.assertAlmostEqual(mse, 6.182284986260905, places=5)
if __name__ == "__main__":
    run_tests()