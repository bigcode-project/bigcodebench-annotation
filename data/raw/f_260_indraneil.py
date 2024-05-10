import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def f_260(dictionary, key, value, n=100, bins=30, seed=0):
    """
    Updates the provided dictionary with a specified key-value pair and generates a random dataset of size 'n' 
    following a normal distribution. The mean and standard deviation of the distribution are set to the value 
    associated with the given key. Additionally, it returns a histogram of the generated dataset.
    
    Parameters:
    - dictionary (dict): The dictionary to be updated.
    - key (str): The key to be added to the dictionary.
    - value (str): The value to be associated with the provided key.
    - n (int, optional): The size of the random dataset to be generated. Default is 100.
    - bins (int, optional): The number of bins for the histogram. Default is 30.
    - seed (int, optional): The seed for the random number generator. Default is 0.
    
    Returns:
    - tuple: Updated dictionary and the generated dataset as a pandas Series along with the histogram plot.
    
    Requirements:
    - numpy
    - matplotlib
    - pandas

    Raises:
    - ValueError: If the provided value is not a number.
    
    Example:
    >>> d, data, ax = f_260({'key1': 10, 'key2': 20}, 'newkey', '25', n=500)
    >>> d
    {'key1': 10, 'key2': 20, 'newkey': '25'}
    >>> len(data)
    500
    """
    np.random.seed(seed)
    # Test that value is a number
    try:
        float(value)
    except ValueError:
        raise ValueError("Value must be a number.")
    # Update the dictionary
    dictionary[key] = value
    
    # Generate the dataset
    data = np.random.normal(loc=float(value), scale=float(value), size=n)
    
    # Plot the histogram of the generated data and get the axes object
    _, ax = plt.subplots()
    ax.hist(data, bins=bins, density=True)
    data = pd.Series(data)
    return dictionary, data, ax


import unittest
import doctest


class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        d, data, _ = f_260({'key1': 10, 'key2': 20}, 'newkey', '25', n=500)
        self.assertIn('newkey', d)
        self.assertEqual(d['newkey'], '25')
        self.assertEqual(len(data), 500)
        
    def test_case_2(self):
        d, data, _ = f_260({}, 'firstkey', '15', n=300)
        self.assertIn('firstkey', d)
        self.assertEqual(d['firstkey'], '15')
        self.assertEqual(len(data), 300)
        
    def test_case_3(self):
        d, data, ax = f_260({'a': 5}, 'b', '10', n=1000)
        self.assertIn('b', d)
        self.assertEqual(d['b'], '10')
        self.assertEqual(len(data), 1000)
        # Test the histogram plot
        self.assertEqual(len(ax.patches), 30)
        # Test the axes data
        self.assertAlmostEqual(ax.get_xlim()[1], 40.5, places=1)
        self.assertAlmostEqual(ax.get_ylim()[1], 0.05, places=1)
        
    def test_case_4(self):
        d, data, _ = f_260({'x': 50}, 'y', '75', n=10, seed=77)
        self.assertIn('y', d)
        self.assertEqual(d['y'], '75')
        self.assertEqual(len(data), 10)
        # Test the generated data
        self.assertTrue(np.allclose(data, np.array(
            [ 91.83, 124.61, 31.51, 105.58, 109.98, -73.1,  95.66, -43.18, 192.62,  20.64]
        ), atol=0.01))
        
    def test_case_5(self):
        d, data, _ = f_260({'1': 100}, '2', '200', n=700)
        self.assertIn('2', d)
        self.assertEqual(d['2'], '200')
        self.assertEqual(len(data), 700)
        

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
