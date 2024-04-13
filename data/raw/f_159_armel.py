import re
import pandas as pd
import matplotlib.pyplot as plt

# Constants
PATTERNS_TO_PLOT = ['nnn', 'aaa', 'sss', 'ddd', 'fff']

def f_159(df):
    """
    Given a pandas DataFrame with a column named 'strings' and the list of patterns PATTERNS_TO_PLOT, count the number of occurrences of each pattern in
    the column 'strings' of each row of the dataframe.
    - For each of the pattern, plot a line plot representing the number of occurrences of this pattern per row of the dataframe.
    - Each plot should be labeled with the name of the corresponding pattern.

    Parameters:
    df (pandas.DataFrame): The input DataFrame with a column named 'strings'.
    
    Returns:
    matplotlib.axes.Axes: The Axes object of the plotted data.
    
    Requirements:
    - re
    - pandas
    - matplotlib.pyplot
    
    Example:
    >>> df = pd.DataFrame({'strings': ['nnnaaaasssddd', 'aaasssdddnnn', 'sssdddnnnaaa', 'dddnnnaaasss', 'nnnaaasssddd']})
    >>> ax = f_159(df)
    >>> type(ax)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    """
    counts = {pattern: [] for pattern in PATTERNS_TO_PLOT}
    
    for _, row in df.iterrows():
        for pattern in PATTERNS_TO_PLOT:
            counts[pattern].append(len(re.findall(pattern, row['strings'])))
    
    fig, ax = plt.subplots()
    for pattern, values in counts.items():
        ax.plot(values, label=pattern)
    
    ax.legend()
    
    return ax

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_159 function."""
    def test_case_1(self):
        df = pd.DataFrame(
            {
                "strings" : ['nnnnnnnnn', 'aaannn', 'sssaaasssaaaddd', 'fffdddnnn']
            }
        )
        ax = f_159(df)
        
        # Check the type of the returned object
        self.assertIsInstance(ax, plt.Axes)
        
        # Check if the plot has the correct legend labels
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertListEqual(legend_labels, PATTERNS_TO_PLOT)

    def test_case_2(self):
        df = pd.DataFrame(
            {
                "strings" : ['nnnaaasssfffddd']
            }
        )
        ax = f_159(df)
        
        self.assertIsInstance(ax, plt.Axes)
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertListEqual(legend_labels, PATTERNS_TO_PLOT)

    def test_case_3(self):
        df = pd.DataFrame(
            {
                "strings" : ['no pattern']
            }
        )
        ax = f_159(df)
        
        self.assertIsInstance(ax, plt.Axes)
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertListEqual(legend_labels, PATTERNS_TO_PLOT)

    def test_case_4(self):
        df = pd.DataFrame(
            {
                "strings" : ['fffffffff', 'dddddd', 'aaaddd']
            }
        )
        ax = f_159(df)
        
        self.assertIsInstance(ax, plt.Axes)
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertListEqual(legend_labels, PATTERNS_TO_PLOT)

    def test_case_5(self):
        df = pd.DataFrame(
            {
                "strings" : ['dddddddddaaafffsssaaannn']
            }
        )
        ax = f_159(df)
        
        self.assertIsInstance(ax, plt.Axes)
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        self.assertListEqual(legend_labels, PATTERNS_TO_PLOT)
    
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()    