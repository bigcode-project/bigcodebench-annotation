import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def f_184(list_of_pairs):
    """
    Create a Pandas DataFrame from a list of pairs and normalize the data using MinMaxScaler.
    
    Parameters:
    list_of_pairs (list): A list of tuples, where the first element is the category and 
                          the second element is the value.
    
    Returns:
    DataFrame:  A pandas DataFrame containing the columns 'Category' and 'Value'.
                Category contains the the first elements of each tuple.
                Value contains the normalized values of each tuple.

    Raises:
        Exception: If the input array is empty.
        ValueError: If Values are not numeric.
    
    Requirements:
    - pandas
    - sklearn.preprocessing.MinMaxScaler
    
    Example:
    >>> list_of_pairs = [('Fruits', 5), ('Vegetables', 9), ('Dairy', -1), ('Bakery', -2), ('Meat', 4)]
    >>> df = f_184(list_of_pairs)
    >>> print(df)
         Category     Value
    0      Fruits  0.636364
    1  Vegetables  1.000000
    2       Dairy  0.090909
    3      Bakery  0.000000
    4        Meat  0.545455
    >>> list_of_pairs = [('car', 3.2), ('bike', 0), ('train', -1), ('plane', -6.2), ('ship', 1234)]
    >>> df = f_184(list_of_pairs)
    >>> print(df)
      Category     Value
    0      car  0.007579
    1     bike  0.004999
    2    train  0.004193
    3    plane  0.000000
    4     ship  1.000000
    """

    if len(list_of_pairs) == 0:
        raise Exception('The input array should not be empty.')

    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])

    if pd.api.types.is_numeric_dtype(df.Value) is not True:
        raise ValueError('The values have to be numeric.')

    scaler = MinMaxScaler()
    df['Value'] = scaler.fit_transform(df[['Value']])

    return df

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        '''test with normal input data'''
        input_data = [('traditional', -4), ('we', 7), ('because', 3), ('ability', 10), ('exactly', -7)]
        result = f_184(input_data)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue('Value' in result.columns)
        self.assertAlmostEqual(result[result['Category'] == 'traditional']['Value'].item(), 0.176471, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'we']['Value'].item(), 0.823529, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'because']['Value'].item(), 0.588235, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'ability']['Value'].item(), 1.000000, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'exactly']['Value'].item(), 0.000000, places=6)
    def test_case_2(self):
        '''test empty input'''
        input_data = []
        self.assertRaises(Exception, f_184, input_data)
    def test_case_3(self):
        '''non numeric values'''
        input_data = [('fast', 'test'), ('ago', -8), ('player', 7), ('standard', 2), ('specific', 0)]
        self.assertRaises(Exception, f_184, input_data)
    def test_case_4(self):
        '''Floating point values'''
        input_data = [('real', 4.453), ('others', -1.12), ('professor', -2.2), ('other', -5), ('task', -7.933)]
        result = f_184(input_data)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue('Value' in result.columns)
        self.assertAlmostEqual(result[result['Category'] == 'real']['Value'].item(), 1.000000, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'others']['Value'].item(), 0.550057, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'professor']['Value'].item(), 0.462861, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'other']['Value'].item(), 0.236800, places=6)
        self.assertAlmostEqual(result[result['Category'] == 'task']['Value'].item(), 0.000000, places=6)
    def test_case_5(self):
        '''test for basic output structure'''
        input_data = [('visit', 4), ('brother', -2), ('experience', -10), ('whether', 8), ('hand', 3)]
        result = f_184(input_data)
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue('Value' in result.columns)
        self.assertTrue('Category' in result.columns)
        self.assertTrue(0 <= result['Value'].min() <= 1)
        self.assertTrue(0 <= result['Value'].max() <= 1)
