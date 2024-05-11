import pandas as pd
import numpy as np
from random import randint

# Constants
STUDENTS = ['Joe', 'Amy', 'Mark', 'Sara', 'John', 'Emily', 'Zoe', 'Matt']
COURSES = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History', 'Geography', 'Computer Science']


def task_func():
    """
    Generates a DataFrame containing random grades for a predefined list of students across a set of courses.
    Each student will have one grade per course and an average grade calculated across all courses.

    Returns:
    DataFrame: A pandas DataFrame with columns for each student's name, their grades for each course,
               and their average grade across all courses.

    Requirements:
    - pandas
    - numpy
    - random

    Note:
    The grades are randomly generated for each course using a uniform distribution between 0 and 100.

    Example:
    >>> random.seed(0)
    >>> grades = task_func()
    >>> print(grades[['Name', 'Average Grade']].to_string(index=False))
     Name  Average Grade
      Joe         51.875
      Amy         53.250
     Mark         53.750
     Sara         47.125
     John         55.250
    Emily         48.625
      Zoe         63.750
     Matt         54.750
    """
    students_data = []
    for student in STUDENTS:
        grades = [randint(0, 100) for _ in COURSES]
        average_grade = np.mean(grades)
        students_data.append([student] + grades + [average_grade])
    columns = ['Name'] + COURSES + ['Average Grade']
    grades_df = pd.DataFrame(students_data, columns=columns)
    return grades_df

import unittest
from unittest.mock import patch
import random
class TestCases(unittest.TestCase):
    def setUp(self):
        random.seed(0)
        # Correctly set up the mock within the test execution context
        self.patcher = patch('random.randint', side_effect=[i % 100 for i in range(800)])  # Assuming 8 students and 100 course entries
        self.mock_randint = self.patcher.start()
        self.grades_df = task_func()
        self.patcher.stop()
    def test_dataframe_columns(self):
        # Ensure the DataFrame contains the correct columns
        expected_columns = ['Name'] + COURSES + ['Average Grade']
        self.assertListEqual(list(self.grades_df.columns), expected_columns, "DataFrame should have specific columns")
    def test_grade_range(self):
        # Check that all grades are within the valid range (0 to 100)
        course_columns = self.grades_df.columns[1:-1]  # Exclude 'Name' and 'Average Grade'
        for course in course_columns:
            self.assertTrue(self.grades_df[course].between(0, 100).all(),
                            f"All grades in {course} should be between 0 and 100")
    def test_average_grade_calculation(self):
        # Verify that the average grade is correctly calculated
        course_columns = self.grades_df.columns[1:-1]  # Exclude 'Name' and 'Average Grade'
        calculated_avg = self.grades_df[course_columns].mean(axis=1)
        np.testing.assert_array_almost_equal(self.grades_df['Average Grade'], calculated_avg, decimal=1,
                                             err_msg="Average grades should be correctly calculated")
    def test_all_students_included(self):
        # Ensure that all predefined students are included in the DataFrame
        self.assertTrue(set(STUDENTS).issubset(set(self.grades_df['Name'])),
                        "All predefined students should be included in the DataFrame")
    def test_deterministic_grades(self):
        # Verify the grades are deterministic under mocked conditions
        random.seed(0)
        expected_first_row_grades = [randint(0, 100) for _ in COURSES]
        actual_first_row_grades = self.grades_df.iloc[0, 1:-1].tolist()
        self.assertListEqual(actual_first_row_grades, expected_first_row_grades,
                             "The first row grades should be deterministic and match the expected pattern")
