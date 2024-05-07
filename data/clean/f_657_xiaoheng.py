from collections import Counter
import itertools
import operator

def f_657(list_of_menuitems):
    """
    Faced with a nested list of menu items, flatten the list and return the most common menu item.

    Parameters:
    - list_of_menuitems (list): A nested list of menu items.

    Returns:
    - str: The most common menu item.

    Requirements:
    - collections
    - itertools
    - operator

    Example:
    >>> f_657([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
    'Pizza'
    """
    flat_list = list(itertools.chain(*list_of_menuitems))

    counter = Counter(flat_list)

    return max(counter.items(), key=operator.itemgetter(1))[0]

import unittest

class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Description: Testing with a list where 'Pizza' appears more frequently than other items.
        input_data = [['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']]
        output = f_657(input_data)
        self.assertEqual(output, 'Pizza')
    
    def test_case_2(self):
        # Description: Testing with a list where 'Burger' appears more frequently than other items.
        input_data = [['Burger', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']]
        output = f_657(input_data)
        self.assertEqual(output, 'Burger')
    
    def test_case_3(self):
        # Description: Testing with a list where 'Pasta' appears more frequently than other items.
        input_data = [['Pasta', 'Pasta'], ['Pasta', 'Coke'], ['Pizza', 'Coke']]
        output = f_657(input_data)
        self.assertEqual(output, 'Pasta')
    
    def test_case_4(self):
        # Description: Testing with a list where 'Sushi' appears more frequently than other items.
        input_data = [['Sushi'], ['Sushi', 'Coke'], ['Pizza', 'Coke']]
        output = f_657(input_data)
        self.assertEqual(output, 'Sushi')
    
    def test_case_5(self):
        # Description: Testing with a list where 'Salad' appears more frequently than other items.
        input_data = [['Salad'], ['Salad', 'Coke'], ['Pizza', 'Coke'], ['Salad', 'Burger']]
        output = f_657(input_data)
        self.assertEqual(output, 'Salad')

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()