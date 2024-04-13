import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def f_179(
        students=['John', 'Alice', 'Bob', 'Cindy', 'David'],
        subjects=['Math', 'English', 'Science', 'History', 'Geography']
    ):
    """
    Generate a report on students' grades for different subjects.
    
    The function generates random grades (between 1 and 100 both included) for each student and for each subject and returns a pandas DataFrame containing the grades. The function also returns a bar plot showing the average grades for each student.
    If there is no grade to display, return None instead of an empty plot.
        - The title of the plot should be 'Average Grades for Each Student'.
        - The x-label should be set to 'Student Name'.
        - The y-label should be set to 'Average Grade'.

    Parameters:
    - students (list): List of student names. Default is ['John', 'Alice', 'Bob', 'Cindy', 'David'].
    - subjects (list): List of subjects. Default is ['Math', 'English', 'Science', 'History', 'Geography'].

    Returns:
    tuple: A tuple containing:
        - pandas.DataFrame: A pandas DataFrame with student grades.
        - matplotlib.axes._axes.Axes: A matplotlib Axes object showing the average grades for each student (None if no data to plot).

    Requirements:
    - pandas
    - matplotlib.pyplot
    - random

    Example:
    >>> report, ax = f_179()
    >>> print(report)
    >>> if ax:
    >>>     plt.show()  # To display the plot
    """
    grade_data = []

    for student in students:
        grades = [randint(1, 100) for _ in subjects]
        grade_data.append(grades)

    grade_df = pd.DataFrame(grade_data, columns=subjects, index=students)
    
    if grade_df.empty:
        return grade_df, None
    
    ax = grade_df.mean(axis=1).plot(kind='bar', title="Average Grades for Each Student")
    ax.set_ylabel('Average Grade')
    ax.set_xlabel('Student Name')
    plt.show()
    return grade_df, ax

import unittest
import numpy as np

class TestCases(unittest.TestCase):
    """Test cases for the f_179 function."""
    def test_case_1(self):
        students = ['John', 'Alice', 'Bob']
        subjects = ['Math', 'English', 'Science']
        report, ax = f_179(students, subjects)
        
        # Check if the report contains the correct students and subjects
        self.assertListEqual(report.index.tolist(), students)
        self.assertListEqual(report.columns.tolist(), subjects)
        
        # Check if grades are between 1 and 100
        self.assertTrue((report >= 1).all().all())
        self.assertTrue((report <= 100).all().all())
        
        # Check the plot title
        self.assertEqual(ax.get_title(), "Average Grades for Each Student")

    def test_case_2(self):
        # Using default students and subjects
        report, ax = f_179()
        
        # Check the plot type
        extracted_values = [bar.get_height() for bar in ax.patches] # extract bar height
        extracted_categories = [tick.get_text() for tick in ax.get_xticklabels()] # extract category label

        self.assertTrue(np.allclose(np.array(extracted_values), report.mean(axis=1).values))
        self.assertListEqual(extracted_categories, ['John', 'Alice', 'Bob', 'Cindy', 'David'])

        # Check if grades are between 1 and 100
        self.assertTrue((report >= 1).all().all())
        self.assertTrue((report <= 100).all().all())
        
        # Check the plot title
        self.assertEqual(ax.get_title(), "Average Grades for Each Student")

    def test_case_3(self):
        students = ['Eve', 'Frank']
        subjects = ['Physics', 'Chemistry']
        report, ax = f_179(students, subjects)
        
        # Check if the report contains the correct students and subjects
        self.assertListEqual(report.index.tolist(), students)
        self.assertListEqual(report.columns.tolist(), subjects)
        
        # Check if grades are between 1 and 100
        self.assertTrue((report >= 1).all().all())
        self.assertTrue((report <= 100).all().all())
        
        # Check the plot title
        self.assertEqual(ax.get_title(), "Average Grades for Each Student")
        
    def test_case_4(self):
        # Testing with no students and subjects
        students = []
        subjects = []
        report, ax = f_179(students, subjects)
        
        # Check if the report is empty
        self.assertTrue(report.empty)
        
        # Check the plot doesn't exist
        self.assertIsNone(ax)
        
    def test_case_5(self):
        # Testing with a larger number of students and subjects
        students = ['John', 'Alice', 'Bob', 'Cindy', 'David', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy']
        subjects = ['Math', 'English', 'Science', 'History', 'Geography', 'Physics', 'Chemistry', 'Biology', 'Arts', 'Music']
        report, ax = f_179(students, subjects)
        
        # Check if the report contains the correct students and subjects
        self.assertListEqual(report.index.tolist(), students)
        self.assertListEqual(report.columns.tolist(), subjects)
        
        # Check if grades are between 1 and 100
        self.assertTrue((report >= 1).all().all())
        self.assertTrue((report <= 100).all().all())
        
        # Check the plot title
        self.assertEqual(ax.get_title(), "Average Grades for Each Student")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__" :
    run_tests()