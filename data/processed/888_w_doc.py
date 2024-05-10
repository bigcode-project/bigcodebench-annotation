import pandas as pd
from collections import Counter


def task_func(data):
    """
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
    >>> df, avg_scores, common_age = task_func(data)
    >>> print(df)
       Name  Age  Score
    2  John   19     92
    4  John   19     90
    5  John   19     92
    8  John   19     90
    1  Nick   21     79
    6  Nick   21     81
    0   Tom   20     85
    3   Tom   20     88
    7   Tom   20     86
    9   Tom   20     85
    """
    if not all(key in data for key in ['Name', 'Age', 'Score']):
        raise ValueError("The dictionary must have the keys 'Name', 'Age', 'Score'")
    df = pd.DataFrame(data).sort_values(['Name', 'Age'])
    avg_scores = df.groupby('Name')['Score'].mean()
    age_counts = Counter(df['Age'])
    most_common_age = age_counts.most_common(1)[0][0] if age_counts else None
    return df, avg_scores, most_common_age

import unittest
import pandas as pd
import os
class TestCases(unittest.TestCase):
    def test_wrong_keys(self):
        # Testing with incorrect dictionary keys
        data = {
            'Names': ['Tom', 'Nick'],
            'Ages': [20, 21],
            'Scores': [85, 79]
        }
        with self.assertRaises(ValueError):
            task_func(data)
    def test_correct_processing(self):
        # Testing with correctly formatted data
        data = {
            'Name': ['Tom', 'Nick', 'Tom', 'John'],
            'Age': [20, 21, 20, 19],
            'Score': [85, 79, 88, 92]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(df.iloc[0]['Name'], 'John')
        self.assertAlmostEqual(avg_scores['Tom'], 86.5)
        self.assertEqual(common_age, 20)
    def test_empty_data(self):
        # Testing with empty lists
        data = {'Name': [], 'Age': [], 'Score': []}
        df, avg_scores, common_age = task_func(data)
        self.assertTrue(df.empty)
        self.assertTrue(avg_scores.empty)
        self.assertIsNone(common_age)
    def test_all_same_age(self):
        # Testing with all students having the same age
        data = {
            'Name': ['Alice', 'Bob', 'Cindy'],
            'Age': [25, 25, 25],
            'Score': [88, 92, 85]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(common_age, 25)
    def test_no_common_age(self):
        # Testing with no common age, each student has a unique age
        data = {
            'Name': ['Alice', 'Bob', 'Cindy'],
            'Age': [24, 25, 26],
            'Score': [88, 92, 85]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(common_age, 24)  # Assuming the first element is taken if all are equally common
    def test_duplicate_names_different_ages(self):
        # Testing with duplicate names but different ages
        data = {
            'Name': ['Tom', 'Tom', 'Nick'],
            'Age': [20, 21, 21],
            'Score': [85, 88, 79]
        }
        df, avg_scores, common_age = task_func(data)
        self.assertEqual(len(df[df['Name'] == 'Tom']), 2)
        self.assertNotEqual(df.iloc[0]['Age'], df.iloc[1]['Age'])
        self.assertTrue(df[df['Name'] == 'Tom'].Age.isin([20, 21]).all())
