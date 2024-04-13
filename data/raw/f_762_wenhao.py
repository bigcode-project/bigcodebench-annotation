import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def f_762(df):
    """
    Draw and return a correlation matrix heatmap for a DataFrame containing numerical columns.
    The title of the heatmap is set to 'Correlation Matrix'.
    
    Parameters:
    df (pandas.DataFrame): The DataFrame containing numerical columns to be used for correlation.

    Returns:
    matplotlib.axes._subplots.AxesSubplot: The matplotlib Axes object representing the heatmap.

    Requirements:
    - pandas
    - seaborn
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    >>> ax = f_762(df)
    >>> type(ax)
    <class 'matplotlib.axes._subplots.AxesSubplot'>

    """
    correlation_matrix = df.corr()
    ax = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    ax.set_title('Correlation Matrix')
    return ax

import unittest
import pandas as pd
import matplotlib.pyplot as plt

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
        ax = f_762(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_2(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [-4, -5, -6], 'c': [-7, -8, -9]})
        ax = f_762(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_3(self):
        df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [-7, -8, -9]})
        ax = f_762(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_4(self):
        df = pd.DataFrame({'a': [1, 1, 1], 'b': [2, 2, 2], 'c': [3, 3, 3]})
        ax = f_762(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
    def test_case_5(self):
        df = pd.DataFrame({'a': [1, 2, None], 'b': [4, None, 6], 'c': [None, 8, 9]})
        ax = f_762(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.title.get_text(), 'Correlation Matrix')
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()