import pandas as pd
from itertools import cycle
from random import randint, seed


def task_func(
    n_grades,
    students=['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    grade_range=range(1, 11),
    rng_seed=None
):
    """
    Generates a grade report for a specified number of grades.
    The function cycles through the given list of students, assigning each a
    random grade from a predefined range, and compiles this information into
    a pandas DataFrame.
    The random grades can be made reproducable by providing a seed in 'rng_seed'.

    Parameters:
    n_grades (int): The number of grades to include in the report.
    students (list of str): The students to include in the report. Defaults to ['Alice', 'Bob', 'Charlie', 'David', 'Eve'].
    grade_range (range): The range of grades that can be assigned. Defaults to range(1, 11).
    rng_seed (int, optional): Seed used in the generation of random integers.
    
    Returns:
    DataFrame: A pandas DataFrame with two columns: 'Student' and 'Grade'. Each row represents a student's grade.

    Raises:
    ValueError: If list of students is empty.

    Requirements:
    - pandas
    - itertools
    - random

    Example:
    >>> grade_report = task_func(3, ['Alice', 'Bob'], range(1, 3), rng_seed=1)
    >>> print(grade_report)
      Student  Grade
    0   Alice      1
    1     Bob      1
    2   Alice      2

    >>> grade_report = task_func(5, rng_seed=12)
    >>> print(grade_report)
       Student  Grade
    0    Alice      8
    1      Bob      5
    2  Charlie      9
    3    David      6
    4      Eve      3
    """
    if len(students) == 0:
        raise ValueError("The students list should contain at least one student.")
    seed(rng_seed)
    student_cycle = cycle(students)
    grade_data = []
    for _ in range(n_grades):
        student = next(student_cycle)
        grade = randint(min(grade_range), max(grade_range))
        grade_data.append([student, grade])
    grade_df = pd.DataFrame(grade_data, columns=['Student', 'Grade'])
    return grade_df

import unittest
from unittest.mock import patch
import pandas as pd
class TestCases(unittest.TestCase):
    # Helper function to compare DataFrames
    def are_dataframes_equal(self, df1, df2):
        if df1.equals(df2):
            return True
        else:
            # Check if the two dataframes have the same columns and values
            return df1.shape == df2.shape and (df1.columns == df2.columns).all() and (df1.values == df2.values).all()
    def test_case_1(self):
        # Simple case with minimum input
        result = task_func(1, ['Alice'], range(1, 2), rng_seed=32)
        expected = pd.DataFrame({'Student': ['Alice'], 'Grade': [1]})
        self.assertTrue(self.are_dataframes_equal(result, expected))
    def test_case_2(self):
        # Testing with multiple grades and checking the cycling feature of students
        result = task_func(5, ['Alice', 'Bob'], range(1, 3), rng_seed=1233)
        # Since grades are random, we check for correct students and valid grades only
        expected_students = ['Alice', 'Bob', 'Alice', 'Bob', 'Alice']
        self.assertEqual(list(result['Student']), expected_students)
        self.assertTrue(all(grade in [1, 2] for grade in result['Grade']))
    def test_case_3(self):
        # Testing with different grade range
        result = task_func(200, ['Alice'], range(100, 102), rng_seed=12)
        # Check if the grades are within the specified range
        self.assertTrue(all(100 <= grade <= 101 for grade in result['Grade']))
    def test_case_4(self):
        # Testing with a larger number of grades
        number_of_grades = 1000
        result = task_func(number_of_grades, ['Alice', 'Bob'], range(1, 5), rng_seed=42)
        self.assertEqual(len(result), number_of_grades)
        self.assertTrue(all(1 <= grade <= 4 for grade in result['Grade']))
    def test_case_5(self):
        # Testing with an empty list of students, which should handle the error gracefully
        with self.assertRaises(Exception):
            task_func(3, [], range(1, 3))
    def test_default(self):
        result = task_func(10, rng_seed=12)
        expected = pd.DataFrame({
            'Student': {0: 'Alice',
            1: 'Bob',
            2: 'Charlie',
            3: 'David',
            4: 'Eve',
            5: 'Alice',
            6: 'Bob',
            7: 'Charlie',
            8: 'David',
            9: 'Eve'},
            'Grade': {0: 8, 1: 5, 2: 9, 3: 6, 4: 3, 5: 7, 6: 1, 7: 6, 8: 8, 9: 5}
        })
        pd.testing.assert_frame_equal(result, expected, check_dtype=False)
