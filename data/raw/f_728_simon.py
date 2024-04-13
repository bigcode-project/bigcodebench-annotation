import pandas as pd
from collections import Counter


def f_728(data):
    '''
    Analyze a dictionary of student data to return a dataframe sorted by name and age in ascending order, 
    the average score per student as a pandas Series, and the most common age as an integer.
    
    Parameters:
    data (dict): A dictionary containing student data with three keys:
        - 'Name': List of student names.
        - 'Age': List of student ages.
        - 'Score': List of student scores.

    Returns:
    pd.DataFrame, pd.Series, int or None: 
        - A dataframe sorted by 'Name' and 'Age' in ascending order.
        - A series representing average scores indexed by student names.
        - An integer representing the most common age or None if no data is available.

    Raises:
    ValueError: If the dictionary does not have the required keys.

    Requirements:
    - pandas
    - collections

    Example:
    >>> data = {
    ...     'Name': ['Tom', 'Nick', 'John', 'Tom', 'John', 'John', 'Nick', 'Tom', 'John', 'Tom'],
    ...     'Age': [20, 21, 19, 20, 19, 19, 21, 20, 19, 20],
    ...     'Score': [85, 79, 92, 88, 90, 92, 81, 86, 90, 85]
    ... }
    >>> df, avg_scores, common_age = f_728(data)
    >>> print(df)
         Name  Age  Score
    2    John   19     92
    4    John   19     90
    5    John   19     92
    8    John   19     90
    1    Nick   21     79
    6    Nick   21     81
    0     Tom   20     85
    3     Tom   20     88
    7     Tom   20     86
    9     Tom   20     85
    >>> print(avg_scores)
    Name
    John    91.00
    Nick    80.00
    Tom     86.25
    Name: Score, dtype: float64
    >>> print(common_age)
    19

    >>> data = {
    ...     'Name': ['Simon', 'Alex', 'Tanja', 'Amanda', 'Tanja'],
    ...     'Age': [21, 42, 54, 20, 54],
    ...     'Score': [1, 1, 2, 3, 5]
    ... }
    >>> df, avg_scores, common_age = f_728(data)
    >>> rint(df)
        Name  Age  Score
    1    Alex   42      1
    3  Amanda   20      3
    0   Simon   21      1
    2   Tanja   54      2
    4   Tanja   54      5
    >>> print(avg_scores)
    Name
    Alex      1.0
    Amanda    3.0
    Simon     1.0
    Tanja     3.5
    Name: Score, dtype: float64
    >>> print(common_age)
    54
    '''

    if not all(key in data for key in ['Name', 'Age', 'Score']):
        raise ValueError("The dictionary must have the keys 'Name', 'Age', 'Score'")


    # Creating a dataframe and sorting it
    df = pd.DataFrame(data).sort_values(['Name', 'Age'])
    
    # Calculating average scores
    avg_scores = df.groupby('Name')['Score'].mean()
    
    # Getting the most common age
    age_counts = Counter(df['Age'])
    most_common_age = age_counts.most_common(1)[0][0] if age_counts else None
    
    return df, avg_scores, most_common_age
    

import unittest
import pandas as pd
import os

class TestCases(unittest.TestCase):

    def setUp(self):
        self.data_small_path = os.path.join('f_728_data_simon', 'data_small.csv') 
        self.data_medium_path = os.path.join('f_728_data_simon', 'data_medium.csv') 
        self.data_large_path = os.path.join('f_728_data_simon', 'data_large.csv') 


    def test_wrong_keys(self):
        data = {
        'a': ['Tom', 'Nick', 'John', 'Tom', 'John', 'John', 'Nick', 'Tom', 'John', 'Tom'],
        'Age': [20, 21, 19, 20, 19, 19, 21, 20, 19, 20],
        'Score': [85, 79, 92, 88, 90, 92, 81, 86, 90, 85]
        }
        self.assertRaises(Exception, f_728, data)
        

    def test_case_1(self):
        data_small = pd.read_csv(self.data_small_path).to_dict(orient='list')
        df, avg_scores, common_age = f_728(data_small)
        df_exp = pd.DataFrame(
            {'Name': {2: 'Brent',
            9: 'Brianna',
            6: 'Justin',
            4: 'Karen',
            0: 'Lisa',
            7: 'Russell',
            8: 'Ryan',
            3: 'Sheri',
            1: 'Stephen',
            5: 'Vincent'},
            'Age': {2: 23, 9: 21, 6: 21, 4: 22, 0: 23, 7: 20, 8: 18, 3: 22, 1: 18, 5: 22},
            'Score': {2: 66,
            9: 98,
            6: 80,
            4: 51,
            0: 87,
            7: 97,
            8: 83,
            3: 75,
            1: 78,
            5: 70}}
        )
        avg_exp = pd.Series({'Brent': 66.0,
            'Brianna': 98.0,
            'Justin': 80.0,
            'Karen': 51.0,
            'Lisa': 87.0,
            'Russell': 97.0,
            'Ryan': 83.0,
            'Sheri': 75.0,
            'Stephen': 78.0,
            'Vincent': 70.0})
        pd.testing.assert_frame_equal(df, df_exp)
        pd.testing.assert_series_equal(avg_scores, avg_exp, check_index=False, check_names=False)
        self.assertEqual(common_age, 22)

    def test_case_2(self):
        data_medium = pd.read_csv(self.data_medium_path).to_dict(orient='list')
        df, avg_scores, common_age = f_728(data_medium)
        df_exp = pd.read_csv(os.path.join('f_728_data_simon', 'medium_res.csv'), index_col=0)
        avg_exp = pd.read_csv(os.path.join('f_728_data_simon', 'medium_series.csv'), index_col=0, header=0).squeeze("columns")

        pd.testing.assert_frame_equal(df, df_exp)
        pd.testing.assert_series_equal(avg_scores, avg_exp)
        self.assertEqual(common_age, 23)

    def test_case_3(self):
        data_large = pd.read_csv(self.data_large_path).to_dict(orient='list')
        df, avg_scores, common_age = f_728(data_large)
        df_exp = pd.read_csv(os.path.join('f_728_data_simon', 'large_res.csv'), index_col=0)
        avg_exp = pd.read_csv(os.path.join('f_728_data_simon', 'large_series.csv'), index_col=0, header=0).squeeze("columns")
        pd.testing.assert_frame_equal(df, df_exp)
        pd.testing.assert_series_equal(avg_scores, avg_exp)

        self.assertEqual(common_age, 30)

    def test_case_4(self):
        data = {
            'Name': ['M', 'M', 'M'],
            'Age': [40, 40, 40],
            'Score': [70, 70, 70]
        }
        df, avg_scores, common_age = f_728(data)
        self.assertEqual(df.shape, (3, 3))
        self.assertAlmostEqual(avg_scores['M'], 70.0)
        self.assertEqual(common_age, 40)

    def test_case_5(self):
        data = {
            'Name': [],
            'Age': [],
            'Score': []
        }
        df, avg_scores, common_age = f_728(data)
        self.assertEqual(df.shape, (0, 3))
        self.assertTrue(avg_scores.empty)
        self.assertIsNone(common_age)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()