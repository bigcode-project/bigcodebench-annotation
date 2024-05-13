import numpy as np
import pandas as pd

def task_func(students=["Alice", "Bob", "Charlie", "David", "Eve"], seed=42):
    """
    Generate random scores for a given list of students, sort these scores in ascending order,
    and return both the scores and a bar plot of these scores.

    Parameters:
    students (list of str): List of student names.
    seed (int): Seed for the random number generator. Default is 42.

    Returns:
    DataFrame: A pandas DataFrame with columns 'Student' and 'Score', sorted by 'Score'.
    Axes: A matplotlib Axes object containing the bar plot of scores.

    use np.random.randint(0, 100) to generate the scores of the students

    Requirements:
    - numpy
    - pandas

    Example:
    >>> scores, plot = task_func()
    >>> print(scores)
       Student  Score
    2  Charlie     14
    0    Alice     51
    4      Eve     60
    3    David     71
    1      Bob     92
    """

    np.random.seed(seed)
    scores_data = [(student, np.random.randint(0, 100)) for student in students]
    df = pd.DataFrame(scores_data, columns=["Student", "Score"])
    df.sort_values("Score", inplace=True)
    ax = df.plot(x='Student', y='Score', kind='bar', legend=False)
    ax.set_ylabel("Score")
    return df, ax

import unittest
import pandas as pd
class TestCases(unittest.TestCase):
    def setUp(self):
        self.students = ["Alice", "Bob", "Charlie", "David", "Eve"]
    def test_random_reproducibility(self):
        df1, _ = task_func(self.students, 42)
        df2, _ = task_func(self.students, 42)
        pd.testing.assert_frame_equal(df1, df2)
    def test_dataframe_columns(self):
        df, _ = task_func(self.students)
        self.assertListEqual(list(df.columns), ["Student", "Score"])
    def test_scores_within_range(self):
        df, _ = task_func(self.students)
        self.assertTrue(df["Score"].between(0, 100).all())
    def test_plot_labels(self):
        _, ax = task_func(self.students)
        self.assertEqual(ax.get_ylabel(), "Score")
        self.assertEqual(ax.get_xlabel(), "Student")
    def test_different_seeds_produce_different_scores(self):
        df1, _ = task_func(self.students, 42)
        df2, _ = task_func(self.students, 43)
        self.assertFalse(df1.equals(df2))
    
    def test_dataframe_value(self):
        df, _ = task_func(self.students)                
        df_list = df.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        expect = ['Charlie,14', 'Alice,51', 'Eve,60', 'David,71', 'Bob,92']
        # with open('df_contents.txt', 'w') as file:
        #     file.write(str(df_list))
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")
