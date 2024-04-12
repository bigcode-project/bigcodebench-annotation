import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from random import sample
from typing import Tuple

# Constants
STUDENTS = ['Student' + str(i) for i in range(1, 101)]
COURSES = ['Course' + str(i) for i in range(1, 6)]


def f_498(num_students: int) -> Tuple[pd.DataFrame, plt.Axes]:
    """
    Generate a Pandas DataFrame that displays the grades of a randomly selected group of students in multiple courses.
    Calculate the average grade in each course, the number of students with a passing grade (>= 60), 
    and visualize this information using a bar plot.

    Parameters:
    num_students (int): The number of students in the sample.

    Returns:
    Tuple[pd.DataFrame, plt.Axes]: A tuple containing the generated DataFrame and the bar plot's Axes object.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot
    - random

    Example:
    >>> df, ax = f_498(50)
    >>> print(df.head())
       Course1  Course2  Course3  Course4  Course5
    Student1      67       76       89       54       92
    Student2      43       56       75       48       92
    ...
    >>> ax.get_title()
    'Course-wise Average and Passing Grade Counts'
    """
    # Generate sample students and grades
    students_sample = sample(STUDENTS, num_students)
    grades = np.random.randint(40, 101, size=(num_students, len(COURSES)))

    # Create DataFrame
    df = pd.DataFrame(grades, index=students_sample, columns=COURSES)

    # Create plot
    fig, ax = plt.subplots()
    df.mean().plot(kind='bar', ax=ax, position=1, width=0.4, color='b', label='Average Grade')
    df[df >= 60].count().plot(kind='bar', ax=ax, position=0, width=0.4, color='g', label='Passing Grade Counts')
    ax.set_title('Course-wise Average and Passing Grade Counts')
    ax.legend()

    return df, ax

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Test with 10 students
        df, ax = f_498(10)
        
        # Check DataFrame dimensions
        self.assertEqual(df.shape, (10, 5))
        
        # Check plot title
        self.assertEqual(ax.get_title(), 'Course-wise Average and Passing Grade Counts')
    
    def test_case_2(self):
        # Test with 50 students
        df, ax = f_498(50)
        
        # Check DataFrame dimensions
        self.assertEqual(df.shape, (50, 5))
        
        # Check plot title
        self.assertEqual(ax.get_title(), 'Course-wise Average and Passing Grade Counts')
        
    def test_case_3(self):
        # Test with 100 students
        df, ax = f_498(100)
        
        # Check DataFrame dimensions
        self.assertEqual(df.shape, (100, 5))
        
        # Check plot title
        self.assertEqual(ax.get_title(), 'Course-wise Average and Passing Grade Counts')
    
    def test_case_4(self):
        # Test with 1 student
        df, ax = f_498(1)
        
        # Check DataFrame dimensions
        self.assertEqual(df.shape, (1, 5))
        
        # Check plot title
        self.assertEqual(ax.get_title(), 'Course-wise Average and Passing Grade Counts')
        
    def test_case_5(self):
        # Test with 5 students
        df, ax = f_498(5)
        
        # Check DataFrame dimensions
        self.assertEqual(df.shape, (5, 5))
        
        # Check plot title
        self.assertEqual(ax.get_title(), 'Course-wise Average and Passing Grade Counts')


if __name__ == "__main__":
    run_tests()