import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def f_157(sample_size=100, slope=3, intercept=0):
    """
    Generate a sample dataset using the given slope and intercept, fit it with a linear regression model, and plot the data points and regression line.
    Here is a step by step guide.
    0. Create the inputs of the data by sampling sample_size values from a uniform distribution over [0, 1)
    1. Create the outputs by multiplying the inputs by the slope and adding the intercept and a standard gaussian noise
    2. Create a linear regression model and fit it to the data.
    3. Add a scatter plot of the inputs and outputs.
    4. Plot a lineplot showing the inputs and their predictions.
    5. the xlabel should be 'X', the ylabel 'y' and the title 'Data points and Regression Line'.
    
    Parameters:
    - sample_size (int): The number of sample data points. Default is 100.
    - slope (float): The slope for the data generation. Default is 3.
    - intercept (float): The intercept for the data generation. Default is 0.

    Returns:
    - model (LinearRegression): The fitted linear regression model.
    - plot (matplotlib.pyplot): The scatter plot of data points and regression line.

    Requirements:
    - numpy
    - sklearn.linear_model.LinearRegression
    - matplotlib.pyplot

    Example:
    >>> model, plot = f_157(sample_size=50, slope=2, intercept=1)
    """
    X = np.random.rand(sample_size, 1)
    y = slope * X + intercept + np.random.randn(sample_size, 1)

    model = LinearRegression()
    model.fit(X, y)

    plt.scatter(X, y)
    plt.plot(X, model.predict(X), color='red')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Data points and Regression Line')

    return model, plt

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_157 function."""
    def test_case_1(self):
        # Test with default parameters
        model, plot = f_157()
        
        # Check if the model's coefficients are close to the expected slope
        self.assertAlmostEqual(model.coef_[0][0], 3, delta=1.0)

        # Check if the intercept of the model is close to the expected intercept
        self.assertAlmostEqual(model.intercept_[0], 0, delta=0.5)
        
        # Check the attributes of the plot
        self.assertEqual(plot.gca().get_xlabel(), 'X')
        self.assertEqual(plot.gca().get_ylabel(), 'y')
        self.assertEqual(plot.gca().get_title(), 'Data points and Regression Line')
    
    def test_case_2(self):
        # Test with smaller sample size and different slope and intercept
        model, plot = f_157(sample_size=500, slope=2, intercept=1)
        
        # Check if the model's coefficients are close to the expected slope
        self.assertAlmostEqual(model.coef_[0][0], 2, delta=1.0)

        # Check if the intercept of the model is close to the expected intercept
        self.assertAlmostEqual(model.intercept_[0], 1, delta=0.5)

    def test_case_3(self):
        # Test with larger sample size and negative slope
        model, plot = f_157(sample_size=200, slope=-5, intercept=3)
        
        # Check if the model's coefficients are close to the expected slope
        self.assertAlmostEqual(model.coef_[0][0], -5, delta=0.5)

        # Check if the intercept of the model is close to the expected intercept
        self.assertAlmostEqual(model.intercept_[0], 3, delta=0.5)
    
    def test_case_4(self):
        # Test with zero slope and intercept
        model, plot = f_157(sample_size=1500, slope=0, intercept=0)
        
        # Check if the model's coefficients are close to the expected slope
        self.assertAlmostEqual(model.coef_[0][0], 0, delta=0.1)

        # Check if the intercept of the model is close to the expected intercept
        self.assertAlmostEqual(model.intercept_[0], 0, delta=0.1)

    def test_case_5(self):
        # Test with random slope and intercept
        random_slope = 3
        random_intercept = 4
        model, plot = f_157(sample_size=100, slope=random_slope, intercept=random_intercept)
        
        # Check if the model's coefficients are close to the expected slope
        self.assertAlmostEqual(model.coef_[0][0], random_slope, delta=1)

        # Check if the intercept of the model is close to the expected intercept
        self.assertAlmostEqual(model.intercept_[0], random_intercept, delta=1)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()  