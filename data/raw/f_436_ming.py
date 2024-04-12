import collections
import itertools
import matplotlib.pyplot as plt

# Constants
ITEMS = ['apple', 'banana', 'cherry', 'date', 'elderberry']

def f_436(a, b):
    """
    Combine two lists and record the frequency of predefined items in the combined list.
    
    Parameters:
    a (list): A list of items.
    b (list): Another list of items.

    Returns:
    matplotlib.axes.Axes: A bar chart showing the frequency of predefined items 
                          ['apple', 'banana', 'cherry', 'date', 'elderberry'] in the combined list.

    Requirements:
    - collections
    - itertools
    - matplotlib

    Example:
    >>> f_436(['apple', 'banana', 'cherry'], ['date', 'elderberry', 'apple', 'banana', 'cherry'])
    <matplotlib.axes._subplots.AxesSubplot object at 0x...>
    """
    combined = list(itertools.chain(a, b))
    counter = collections.Counter(combined)
    item_counts = [counter.get(item, 0) for item in ITEMS]
    
    ax = plt.bar(ITEMS, item_counts)
    return ax

import unittest
import matplotlib.container

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        a = ['apple', 'banana', 'cherry']
        b = ['date', 'elderberry', 'apple', 'banana', 'cherry']
        result = f_436(a, b)
        # Checking the type of returned object
        self.assertIsInstance(result, matplotlib.container.BarContainer)
        # Checking the height of the bars (frequencies)
        heights = [rect.get_height() for rect in result]
        expected_heights = [2, 2, 2, 1, 1]
        self.assertEqual(heights, expected_heights)
        
    def test_case_2(self):
        a = []
        b = ['apple', 'apple', 'apple']
        result = f_436(a, b)
        heights = [rect.get_height() for rect in result]
        expected_heights = [3, 0, 0, 0, 0]
        self.assertEqual(heights, expected_heights)

    def test_case_3(self):
        a = ['banana', 'cherry', 'date']
        b = ['banana', 'cherry', 'date']
        result = f_436(a, b)
        heights = [rect.get_height() for rect in result]
        expected_heights = [0, 2, 2, 2, 0]
        self.assertEqual(heights, expected_heights)

    def test_case_4(self):
        a = ['elderberry', 'elderberry']
        b = ['elderberry']
        result = f_436(a, b)
        heights = [rect.get_height() for rect in result]
        expected_heights = [0, 0, 0, 0, 3]
        self.assertEqual(heights, expected_heights)

    def test_case_5(self):
        a = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        b = []
        result = f_436(a, b)
        heights = [rect.get_height() for rect in result]
        expected_heights = [1, 1, 1, 1, 1]
        self.assertEqual(heights, expected_heights)

if __name__ == "__main__":
    run_tests()