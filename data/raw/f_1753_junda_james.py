import pandas as pd
import numpy as np
from random import choice, seed as set_seed

def f_1753(num_of_students, seed=42, name_list=None, gender_list=None, age_range=(15, 20), score_range=(50, 100)):
    """
    Generate a Pandas DataFrame with randomized student data. This function allows for specifying 
    the total number of students and the randomness seed for reproducible outcomes. Data attributes 
    include student names, ages, genders, and scores, each derived from provided parameters or defaults.

    Parameters:
    - num_of_students (int): The number of student records to generate. Must be a positive integer.
    - seed (int, optional): Seed for the random number generator to ensure reproducible data. Defaults to 42.
    - name_list (list of str, optional): A list of names from which student names are randomly selected. 
      If not provided, defaults to ['John', 'Mike', 'Sara', 'Emma', 'Nick'].
    - gender_list (list of str, optional): A list of genders from which student genders are randomly selected. 
      If not provided, defaults to ['Male', 'Female'].
    - age_range (tuple of int, optional): A tuple specifying the inclusive range of student ages. Defaults to (15, 20).
    - score_range (tuple of int, optional): A tuple specifying the inclusive range of student scores. Defaults to (50, 100).

    Returns:
    - pandas.DataFrame: A DataFrame object with columns ['Name', 'Age', 'Gender', 'Score'], containing 
      randomly generated data for the specified number of students. Names and genders are randomly selected 
      from the provided lists (or defaults). Ages and scores are randomly generated within the specified ranges.

    Raises:
    - ValueError: If num_of_students is non-positive.

    Notes:
    - The 'Name' column values are selected randomly from the 'name_list'.
    - The 'Age' column values are integers randomly generated within the 'age_range', inclusive.
    - The 'Gender' column values are selected randomly from the 'gender_list'.
    - The 'Score' column values are integers randomly generated within the 'score_range', inclusive.
    - Setting the same seed value ensures the reproducibility of the dataset across different function calls.

    Requirements:
    - pandas
    - numpy
    - random

    Example:
    >>> student_data = f_1753(5, seed=123)
    >>> print(student_data.head())
       Name  Age  Gender  Score
    0  John   20  Female     52
    1  John   19  Female     84
    2  Sara   16    Male     69
    3  John   17  Female     72
    4  Nick   16  Female     82
    """
    if num_of_students <= 0:
        raise ValueError("num_of_students must be positive.")

    set_seed(seed)
    np.random.seed(seed)

    name_list = name_list or ['John', 'Mike', 'Sara', 'Emma', 'Nick']
    gender_list = gender_list or ['Male', 'Female']

    data = []
    for _ in range(num_of_students):
        name = choice(name_list)
        age = np.random.randint(age_range[0], age_range[1] + 1)
        gender = choice(gender_list)
        score = np.random.randint(score_range[0], score_range[1] + 1)
        data.append([name, age, gender, score])

    columns = ['Name', 'Age', 'Gender', 'Score']
    df = pd.DataFrame(data, columns=columns)
    return df

import unittest
import pandas as pd
import numpy as np

class TestCases(unittest.TestCase):
    def test_with_seed(self):
        df1 = f_1753(5, seed=42)        
        df_list = df1.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()

        expect = ['John,18,Male,78', 'Sara,17,Male,57', 'Mike,19,Male,70', 'John,16,Male,68', 'Nick,17,Female,60']
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")
        
    def test_reproducibility_with_seed(self):
        df1 = f_1753(3, seed=123)
        df2 = f_1753(3, seed=123)
        pd.testing.assert_frame_equal(df1, df2)

    def test_positive_num_students(self):
        df = f_1753(5)
        self.assertEqual(len(df), 5)

    def test_invalid_num_students(self):
        with self.assertRaises(ValueError):
            f_1753(-1)

    def test_column_names(self):
        df = f_1753(1)
        self.assertListEqual(list(df.columns), ['Name', 'Age', 'Gender', 'Score'])

    def test_age_range(self):
        df = f_1753(10, age_range=(18, 22))
        self.assertTrue(all(18 <= age <= 22 for age in df['Age']))

    def test_custom_name_and_gender_list(self):
        custom_names = ['Alex', 'Bob']
        custom_genders = ['Non-Binary']
        df = f_1753(2, name_list=custom_names, gender_list=custom_genders)
        self.assertIn(df.iloc[0]['Name'], custom_names)
        self.assertIn(df.iloc[0]['Gender'], custom_genders)

    def test_score_range(self):
        df = f_1753(10, score_range=(60, 70))
        self.assertTrue(all(60 <= score <= 70 for score in df['Score']))

def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()