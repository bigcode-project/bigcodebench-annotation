import collections
import numpy as np


def f_674(file_name):
    """
    Find the most common value in each column of a csv file with column names.

    If some values occur the same number of times, the values are sorted
    alphabetically and the first is considered most common.

    If an empty csv is passed, an empty dictionary is returned. 
    
    Parameters:
    file_name (str): The name of the csv file.
    
    Returns:
    dict: A dictionary with column names as keys and most common values as values.

    Requirements:
    - collections
    - numpy
    
    Example:
    >>> common_values = f_674('sample.csv')
    >>> print(common_values)
    {'Name': 'Simon Velasquez',
    'Age': 21,
    'Fruit': 'Apple',
    'Genre': 'HipHop',
    'Height': 172}

    >>> common_values = f_674('test.csv')
    >>> print(common_values)
    {'Object': 'Chair',
    'Weight': '211kg',
    'Dancing Style': 'Waltz',}
    """
    data = np.genfromtxt(file_name, delimiter=',', names=True,
                         dtype=None, encoding=None)
    common_values = {}

    if len(np.atleast_1d(data)) == 0:
        return {}

    if len(np.atleast_1d(data)) == 1:
        for col in data.dtype.names:
            common_values[col] = data[col].item()

    else:
        for col in data.dtype.names:
            counter = collections.Counter(data[col])
            if counter.most_common(2)[0][1] == counter.most_common(2)[1][1]:
                common_values[col] = sorted(counter.items())[0][0]
            else:
                common_values[col] = counter.most_common(1)[0][0]

    return common_values

import unittest
import os


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_empty(self):
        result = f_674(os.path.join('f_674_data_simon', 'test_data_empty.csv'))
        self.assertEqual(result, {})

    def test_1_entry(self):
        result = f_674(os.path.join('f_674_data_simon', 'test_data_1column.csv'))
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 4)

        self.assertCountEqual(result.keys(), ['Name', 'Age', 'Genre', 'Height'])
        self.assertEqual(result['Name'], 'Christopher Martinez')
        self.assertEqual(result['Age'], 21)
        self.assertEqual(result['Genre'], 'Rock')
        self.assertEqual(result['Height'], 180)    

    def test_case_1(self):
        result = f_674(os.path.join('f_674_data_simon', 'test_data_0.csv'))
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 4)

        self.assertCountEqual(result.keys(), ['Name', 'Age', 'Country', 'Gender'])
        self.assertEqual(result['Name'], 'Adam King')
        self.assertEqual(result['Age'], 21)
        self.assertEqual(result['Country'], 'Korea')
        self.assertEqual(result['Gender'], 'Male')    

    def test_case_2(self):
        result = f_674(os.path.join('f_674_data_simon', 'test_data_1.csv'))
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 4)

        self.assertCountEqual(result.keys(), ['Name', 'Age', 'Country', 'Gender'])
        self.assertEqual(result['Name'], 'Aaron Joyce')
        self.assertEqual(result['Age'], 20)
        self.assertEqual(result['Country'], 'Tuvalu')
        self.assertEqual(result['Gender'], 'Female')  
    
    def test_case_3(self):
        result = f_674(os.path.join('f_674_data_simon', 'test_data_2.csv'))
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 4)

        self.assertCountEqual(result.keys(), ['Name', 'Age', 'Country', 'Gender'])
        self.assertEqual(result['Name'], 'Aaron Velasquez')
        self.assertEqual(result['Age'], 21)
        self.assertEqual(result['Country'], 'Afghanistan')
        self.assertEqual(result['Gender'], 'Female')  
    
    def test_case_4(self):
        result = f_674(os.path.join('f_674_data_simon', 'test_data_3.csv'))
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 4)

        self.assertCountEqual(result.keys(), ['Name', 'Age', 'Country', 'Gender'])
        self.assertEqual(result['Name'], 'Alex Wright')
        self.assertEqual(result['Age'], 62)
        self.assertEqual(result['Country'], 'Albania')
        self.assertEqual(result['Gender'], 'Male')  
    
    def test_case_5(self):
        result = f_674(os.path.join('f_674_data_simon', 'test_data_4.csv'))
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result), 4)

        self.assertCountEqual(result.keys(), ['Name', 'Age', 'Country', 'Gender'])
        self.assertEqual(result['Name'], 'Albert Gordon')
        self.assertEqual(result['Age'], 26)
        self.assertEqual(result['Country'], 'Comoros')
        self.assertEqual(result['Gender'], 'Female')  
        
if __name__ == "__main__":
    run_tests()