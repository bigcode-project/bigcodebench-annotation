import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def f_142(data):
    """
    You are given a list of elements. Each element of the list is a list of 3 values. Use this list of elements to build a dataframe with 3 columns 'col1', 'col2' and 'col3' and create a distribution of chart of the different values of "col3" grouped by "col1" and "col2" using seaborn.
    
    The function's logic is as follows:
    1. Build a pandas DataFrame by using list of elements. Make sure to name the columns as 'col1', 'col2' and 'col3', the constant COLUMNS is provided for this purpose.
    2. Create a new dataframe by grouping the values in the column 'col3' by ['col1', 'col2'].
    3. Reset the index of the newly created dataframe. This dataframe is the first element of the output tuple.
    4. Create a distribution plot of the 'col3' column of the previous dataframe using seaborn. This plot is the second and last element of the output tuple.
        - The xlabel (label for the x-axis) is set to the 'col3'.

    Parameters:
    data (list): The DataFrame to be visualized.

    Returns:
    tuple:
        pandas.DataFrame: The DataFrame of the analyzed data.
        plt.Axes: The seaborn plot object.

    Requirements:
    - pandas
    - seaborn
    - matplotlib

    Example:
    >>> data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
    >>> 
    >>> analyzed_df, plot = f_142(data)
    >>> print(analyzed_df)
    """
    df = pd.DataFrame(data, columns=COLUMNS)
    analyzed_df = df.groupby(COLUMNS[:-1])[COLUMNS[-1]].nunique().reset_index()
    ax = sns.distplot(analyzed_df[COLUMNS[-1]])
    
    return analyzed_df, ax

import unittest
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    """Test cases for the f_142 function."""    
    def test_case_1(self):
        data = [[1, 1, 1], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 3], [1, 2, 3], [2, 1, 1], [2, 1, 2], [2, 1, 3], [2, 2, 3], [2, 2, 3], [2, 2, 3]]
        analyzed_df, plot = f_142(data)
        
        # Asserting the analyzed DataFrame
        expected_df = pd.DataFrame({
            'col1': [1, 1, 2, 2],
            'col2': [1, 2, 1, 2],
            'col3': [2, 1, 3, 1]
        })
        pd.testing.assert_frame_equal(analyzed_df, expected_df)
        
        # Asserting plot attributes (e.g., title, x-axis, y-axis)
        self.assertEqual(plot.get_xlabel(), 'col3')
        
    def test_case_2(self):
        # Testing with a different dataset
        data = [[1, 1, 1], [1, 1, 2], [1, 1, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]]
        analyzed_df, plot = f_142(data)
        
        # Asserting the analyzed DataFrame
        expected_df = pd.DataFrame({
            'col1': [1, 1],
            'col2': [1, 2],
            'col3': [3, 1]
        })
        pd.testing.assert_frame_equal(analyzed_df, expected_df)
        
        # Asserting plot attributes
        self.assertEqual(plot.get_xlabel(), 'col3')
    
    def test_case_3(self):
        data = [[1, 2, 3], [1, 2, 4], [1, 2, 5], [6, 7, 8]]
        analyzed_df, plot = f_142(data)
        
        # Asserting the analyzed DataFrame
        expected_df = pd.DataFrame({
            'col1': [1, 6],
            'col2': [2, 7],
            'col3': [3, 1]
        })
        pd.testing.assert_frame_equal(analyzed_df, expected_df)
        
        # Asserting plot attributes
        self.assertEqual(plot.get_xlabel(), 'col3')
    
    def test_case_4(self):
        data = [
            [0, 0, 1],
            [0, 0, 4],
            [0, 1, 1],
            [0, 1, 7],
            [1, 0, 0],
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
        analyzed_df, plot = f_142(data)
        expected_data = [
            [0, 0, 2],
            [0, 1, 2],
            [1, 0, 1],
            [1, 1, 1]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)
        pd.testing.assert_frame_equal(analyzed_df, expected_df)

        # Asserting plot attributes
        self.assertEqual(plot.get_xlabel(), 'col3')

    def test_case_5(self):
        data = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 0, 1],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
        analyzed_df, plot = f_142(data)
        expected_data = [
            [0, 0, 2],
            [0, 1, 2],
            [1, 0, 2],
            [1, 1, 2]
        ]
        expected_df = pd.DataFrame(expected_data, columns=COLUMNS)

        pd.testing.assert_frame_equal(analyzed_df, expected_df)

        # Asserting plot attributes
        self.assertEqual(plot.get_xlabel(), 'col3')

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests() 