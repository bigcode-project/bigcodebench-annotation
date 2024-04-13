import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def f_161(df, patterns=None):
    """
    Given a pandas DataFrame with a column named 'strings' and the list of patterns, count the number of occurrences of each pattern in
    the 'strings' column of each row of the dataframe.
    - Store the results in a dataframe whose columns are the patterns.
    - Create a heatmap of the obtained dataset
    
    Parameters:
    - df (DataFrame): The input DataFrame.
    - patterns (list of str, optional): List of string patterns to be searched in the DataFrame. 
        Defaults to ['nnn', 'aaa', 'sss', 'ddd', 'fff'] if not provided.
    
    Returns:
    tuple: A tuple containing:
        - pd.DataFrame: DataFrame containing counts of each pattern.
        - matplotlib.axes.Axes: The heatmap axes.
    
    Requirements:
    - re
    - pandas
    - seaborn
    - matplotlib.pyplot
    
    Example:
    >>> df = pd.DataFrame({'strings': ['nnnaaaasssddd', 'aaasssdddnnn', 'sssdddnnnaaa', 'dddnnnaaasss', 'nnnaaasssddd']})
    >>> patterns = ['nnn', 'aaa', 'sss']
    >>> counts_df, heatmap_axes = f_161(df, patterns)
    """
    if patterns is None:
        patterns = ['nnn', 'aaa', 'sss', 'ddd', 'fff']
    
    counts = pd.DataFrame(columns=patterns)
    
    for _, row in df.iterrows():
        row_counts = {pattern: len(re.findall(pattern, row['strings'])) for pattern in patterns}
        counts = counts.append(row_counts, ignore_index=True)
    counts = counts.astype("int64")
    # Fill NaN values with zeros
    counts.fillna(0, inplace=True)
    
    heatmap_axes = sns.heatmap(counts.values, annot=True, cmap='viridis')
    return counts, heatmap_axes

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_161 function."""
    def test_case_1(self):
        # Test with default patterns
        df = pd.DataFrame(
            {
                "strings": ['nnnaaaannnfffddd', 'ddddddd', 'fffaaasss', 'ssssssnnnnfff', 'dddfffsss']
            }
        )
        counts_df, heatmap_axes = f_161(df)
        try:
            fig = heatmap_axes.get_figure()
            plt.close(fig)
        except:
            pass
        # Assertions
        self.assertTrue(set(['nnn', 'aaa', 'sss', 'ddd', 'fff']).issubset(set(counts_df.columns)))

        self.assertListEqual(counts_df.loc[:, "nnn"].values.tolist(), [2, 0, 0, 1, 0])
        self.assertListEqual(counts_df.loc[:, "aaa"].values.tolist(), [1, 0, 1, 0, 0])
        self.assertListEqual(counts_df.loc[:, "fff"].values.tolist(), [1, 0, 1, 1, 1])

        self.assertEqual(heatmap_axes.get_title(), '')

    def test_case_2(self):
        # Test with a subset of patterns
        df = pd.DataFrame(
            {
                "strings": ['nnnaaaannnfffddd', 'ddddddd', 'fffaaasss', 'ssssssnnnnfff', 'dddfffsss']
            }
        )
        patterns = ['nnn', 'aaa', 'sss']
        counts_df, heatmap_axes = f_161(df, patterns)
        try:
            fig = heatmap_axes.get_figure()
            plt.close(fig)
        except:
            pass
        # Assertions
        self.assertTrue(set(patterns).issubset(set(counts_df.columns)))
        self.assertEqual(heatmap_axes.get_title(), '')

    def test_case_3(self):
        # Test with entirely different patterns
        df = pd.DataFrame(
            {
                "strings": ['dfsnsadfnsafsnsasd', 'nsansansa', 'asddfsasd', 'nsansansadfs', 'dfs']
            }
        )
        patterns = ['nsa', 'asd', 'dfs']
        counts_df, heatmap_axes = f_161(df, patterns)
        try:
            fig = heatmap_axes.get_figure()
            plt.close(fig)
        except:
            pass
        # Assertions
        self.assertTrue(set(patterns).issubset(set(counts_df.columns)))
        self.assertEqual(heatmap_axes.get_title(), '')

    def test_case_4(self):
        # Test with a larger dataset
        df = pd.DataFrame(
            {
                "strings": ['nnn', 'nnn', 'nnn', 'aaa', 'aaa', 'aaa', 'sss', 'sss', 'sss', 'ddd', 'ddd', 'ddd', 'fff', 'fff', 'fff', 'sss']
            }
        )
        counts_df, heatmap_axes = f_161(df)
        try:
            fig = heatmap_axes.get_figure()
            plt.close(fig)
        except:
            pass
        # Assertions
        self.assertTrue(set(['nnn', 'aaa', 'sss', 'ddd', 'fff']).issubset(set(counts_df.columns)))
        self.assertListEqual(
            counts_df.loc[:, "fff"].values.tolist(),
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]
        )
        self.assertEqual(heatmap_axes.get_title(), '')

    def test_case_5(self):
        # Test with a pattern that is unlikely to occur
        df = pd.DataFrame(
            {
                "strings": ['it', 'is', 'not', 'supposed', 'to', 'occur']
            }
        )
        patterns = ['naaaas', 'ssddnn']
        counts_df, heatmap_axes = f_161(df, patterns)
        try:
            fig = heatmap_axes.get_figure()
            plt.close(fig)
        except:
            pass
        # Assertions
        self.assertTrue(set(patterns).issubset(set(counts_df.columns)))
        self.assertEqual(heatmap_axes.get_title(), '')

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()