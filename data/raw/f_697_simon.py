import collections
import pandas as pd

def f_697(obj_list, attr):
    """
    Count the frequency of each value of the given attribute from a list of objects.
    
    This function returns a pandas Dataframe containing frequency count of the specified attribute from the objects in the list.
    The DataFrame consist of two columns ('attribute' and 'count'), which contain the attribute and its
    specific count respectively.
    
    If no attributes are found, an empty DataFrame is returned.

    Parameters:
    obj_list (list): The list of objects with attributes.
    attr (str): The attribute to count.

    Returns:
    collections.Counter: The frequency count of each value of the attribute.

    Requirements:
    - collections: Using the collections.Counter for calculating the frequencies
    - pandas: For creating the DataFrame
    
    Example:
    >>> class ExampleObject:
    ...     def __init__(self, color, shape):
    ...         self.color = color
    ...         self.shape = shape
    ...
    >>> obj_list = [ExampleObject('Red', 'Square'), ExampleObject('Green', 'Circle'), ExampleObject('Red', 'Rectangle')]
    >>> count = f_697(obj_list, 'color')
    >>> print(count)
        attribute  count
    0       Red      2
    1     Green      1

    >>> class ExampleObject:
    ...     def __init__(self, animal, shape):
    ...         self.animal = animal
    ...         self.shape = shape
    ...
    >>> obj_list = [ExampleObject('tiger', 'Square'), ExampleObject('leopard', 'Circle'), ExampleObject('cat', 'Rectangle'), ExampleObject('elephant', 'Rectangle')]
    >>> count = f_697(obj_list, 'shape')
    >>> print(count)
        attribute  count
    0     Square      1
    1     Circle      1
    2  Rectangle      2
    """
    attr_values = [getattr(obj, attr) for obj in obj_list]
    count = collections.Counter(attr_values)
    if len(count.keys()) == 0:
        return pd.DataFrame()

    df = pd.DataFrame.from_dict(count, orient='index').reset_index()
    df = df.rename(columns={'index':'attribute', 0:'count'})
    return df


import unittest
from collections import Counter

class TestCases(unittest.TestCase):
    class ExampleObject:
        def __init__(self, color, shape):
            self.color = color
            self.shape = shape

    def test_case_1(self):
        obj_list = [
            self.ExampleObject('Red', 'Square'),
            self.ExampleObject('Green', 'Circle'),
            self.ExampleObject('Red', 'Rectangle')
        ]
        result = f_697(obj_list, 'color')
        expected = pd.DataFrame({
            'attribute': ['Red', 'Green'],
            'count': [2, 1]

        })
        pd.testing.assert_frame_equal(result.sort_index(), expected)

    def test_case_2(self):
        obj_list = [
            self.ExampleObject('Red', 'Square'),
            self.ExampleObject('Green', 'Circle'),
            self.ExampleObject('Red', 'Square')
        ]
        result = f_697(obj_list, 'shape')
        expected = pd.DataFrame({
            'attribute': ['Square', 'Circle'],
            'count': [2, 1]

        })
        pd.testing.assert_frame_equal(result.sort_index(), expected)

    def test_case_3(self):
        obj_list = []
        result = f_697(obj_list, 'color')
        self.assertTrue(result.empty)

    def test_case_4(self):
        obj_list = [
            self.ExampleObject('Red', 'Square'),
            self.ExampleObject('Red', 'Square'),
            self.ExampleObject('Red', 'Square')
        ]
        result = f_697(obj_list, 'color')
        expected = pd.DataFrame({
            'attribute': ['Red'],
            'count': [3]

        })
        pd.testing.assert_frame_equal(result.sort_index(), expected)

    def test_case_5(self):
        obj_list = [
            self.ExampleObject('Red', 'Square'),
            self.ExampleObject('Green', 'Circle'),
            self.ExampleObject('Blue', 'Triangle')
        ]
        result = f_697(obj_list, 'shape')
        expected = pd.DataFrame({
            'attribute': ['Square', 'Circle', 'Triangle'],
            'count': [1, 1, 1]

        })
        pd.testing.assert_frame_equal(result.sort_index(), expected)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()