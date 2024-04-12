import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
    
def f_443(data):
    """
    Draw a histogram of the data.

    Parameters:
    data (str): The data string in the format 'value-value-value-...'.

    Returns:
    ax (matplotlib.axes._subplots.AxesSubplot): The Axes object of the created histogram.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot

    Notes:
    - The histogram uses bins calculated as `np.arange(data.min(), data.max()+2) - 0.5`.

    Example:
    >>> data = '1-2-3-4-5-6-7-8-9-10'
    >>> ax = f_443(data)
    """
    data = data.split('-')
    data = [int(d) for d in data]
    df = pd.DataFrame(data, columns=['Values'])
    
    plt.figure(figsize=(10, 6))
    ax = plt.gca()  # Get current Axes
    ax.hist(df['Values'], bins=np.arange(df['Values'].min(), df['Values'].max()+2) - 0.5, edgecolor='black')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Values')
    ax.set_xticks(sorted(list(set(data))))  # Set x-ticks based on unique data values
    plt.show()
    
    return ax

import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):

    def test_case_1(self):
        data = '1-2-3-4-5'
        ax = f_443(data)
        self.assertEqual(ax.get_title(), 'Histogram of Values')
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')
        self.assertListEqual(list(ax.get_xticks()), [1, 2, 3, 4, 5])

    def test_case_2(self):
        data = '5-5-5-5-5'
        ax = f_443(data)
        self.assertEqual(ax.get_title(), 'Histogram of Values')
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')
        self.assertListEqual(list(ax.get_xticks()), [5])

    def test_case_3(self):
        data = '7'
        ax = f_443(data)
        self.assertEqual(ax.get_title(), 'Histogram of Values')
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')
        self.assertListEqual(list(ax.get_xticks()), [7])

    def test_case_4(self):
        data = '2-8-4-10-1'
        ax = f_443(data)
        self.assertEqual(ax.get_title(), 'Histogram of Values')
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')
        self.assertListEqual(sorted(list(ax.get_xticks())), [1, 2, 4, 8, 10])

    def test_case_5(self):
        data = '1-50-100-150'
        ax = f_443(data)
        self.assertEqual(ax.get_title(), 'Histogram of Values')
        self.assertEqual(ax.get_xlabel(), 'Value')
        self.assertEqual(ax.get_ylabel(), 'Frequency')
        self.assertListEqual(sorted(list(ax.get_xticks())), [1, 50, 100, 150])


if __name__ =='__main__':
    run_tests()