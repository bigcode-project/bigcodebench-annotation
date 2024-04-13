import pandas as pd
import numpy as np


def f_681(test_scores, student):
    """
    Calculate the average test score for a particular student from a given DataFrame of test results.
    
    Parameters:
    test_scores (DataFrame): The DataFrame containing columns 'Student' and 'Score'.
        The Student columns is of dtype int and contains student IDs. The Score 
        column is of dtype float.
    student (int): The specific student ID for which the average score needs to be calculated.
    
    Returns:
    float: The average score for the student.
    
    Requirements:
    - pandas
    - numpy
    
    Example:
    >>> STUDENTS = range(1, 101)
    >>> scores = pd.DataFrame({'Student': list(np.random.choice(STUDENTS, 50, replace=True)), 
    ...                        'Score': np.random.randint(50, 101, size=50)})
    >>> f_681(scores, 10)
    75.0

    >>> scores = pd.DataFrame({'Student': [1, 2, 1, 1], 
                               'Score': [10, 1, 1, 1]})
    >>> f_681(1)
    4.0
    """
    if student not in test_scores['Student'].values:
        raise ValueError(f"The student with ID {student} is not present in the test scores DataFrame.")
        
    student_scores = test_scores[test_scores['Student'] == student]['Score']
    average_score = student_scores.mean()
    
    return average_score

import unittest
from faker import Faker
import numpy as np
import pandas as pd

fake = Faker()


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def setUp(self):
        self.student_ids = range(1, 6)
        self.students_sample = list(np.random.choice(self.student_ids, 50, replace=True))
        self.scores = pd.DataFrame({
            'Student': self.students_sample, 
            'Score': np.random.randint(50, 101, size=50)
        })

    def test_case_1(self):
        student_id = self.students_sample[0]
        expected_avg = self.scores[self.scores['Student'] == student_id]['Score'].mean()
        result = f_681(self.scores, student_id)
        self.assertAlmostEqual(expected_avg, result, places=2)

    def test_case_2(self):
        student_id = max(self.student_ids) + 1
        with self.assertRaises(ValueError):
            f_681(self.scores, student_id)

    def test_case_3(self):
        empty_df = pd.DataFrame(columns=['Student', 'Score'])
        student_id = fake.random_int(min=1, max=100)
        with self.assertRaises(ValueError):
            f_681(empty_df, student_id)

    def test_case_4(self):
        scores = pd.DataFrame({
            'Student': list(self.student_ids), 
            'Score': [100] * len(self.student_ids)
        })
        student_id = self.student_ids[3]
        result = f_681(scores, student_id)
        self.assertEqual(result, 100.0)

    def test_case_5(self):
        scores = pd.DataFrame({
            'Student': list(self.student_ids) * 10, 
            'Score': list(np.random.randint(50, 101, size=len(self.student_ids)*10))
        })
        student_id = self.student_ids[4]
        expected_avg = scores[scores['Student'] == student_id]['Score'].mean()
        result = f_681(scores, student_id)
        self.assertAlmostEqual(expected_avg, result, places=2)


if __name__ == "__main__":
    run_tests()