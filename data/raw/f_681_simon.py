import pandas as pd
import numpy as np


def f_681(test_scores, student):
    """
    Calculate the average test score and the standard deviation for a particular student from a given DataFrame of test results.
    
    Parameters:
    test_scores (DataFrame): The DataFrame containing columns 'Student' and 'Score'.
        The Student columns is of dtype int and contains student IDs. The Score 
        column is of dtype float.
    student (int): The specific student ID for which the average score needs to be calculated.
    
    Returns:
    np.array([float, float]): A numpy array containing the average score and the standard deviation for the student.
    
    Raises:
    ValueError: student is not present in the test_scores dataframe
                
    Requirements:
    - pandas
    - numpy
    
    Example:
    >>> STUDENTS = range(1, 101)
    >>> np.random.seed(10)
    >>> scores = pd.DataFrame({'Student': list(np.random.choice(STUDENTS, 50, replace=True)), 
    ...                        'Score': np.random.randint(50, 101, size=50)})
    >>> f_681(scores, 10)
    array([70.        ,  7.07106781])

    >>> scores = pd.DataFrame({'Student': [1, 2, 1, 1], 'Score': [10, 1, 1, 1]})
    >>> f_681(scores, 1)
    array([4.        , 5.19615242])
    """
    if student not in test_scores['Student'].values:
        raise ValueError(f"The student with ID {student} is not present in the test scores DataFrame.")
        
    student_scores = test_scores[test_scores['Student'] == student]['Score']
    average_score = student_scores.mean()
    std = student_scores.std()
    
    return np.array([average_score, std])

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
        expected_std = self.scores[self.scores['Student'] == student_id]['Score'].std()

        res = f_681(self.scores, student_id)
        avg, std = res
        self.assertIsInstance(res, np.ndarray)
        self.assertAlmostEqual(expected_avg, avg, places=2)
        self.assertAlmostEqual(expected_std, std, places=2)


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
        res = f_681(scores, student_id)
        avg, std = res
        self.assertIsInstance(res, np.ndarray)
        self.assertEqual(avg, 100.0)
        self.assertTrue(np.isnan(std))

    def test_case_5(self):
        scores = pd.DataFrame({
            'Student': list(self.student_ids) * 10, 
            'Score': list(np.random.randint(50, 101, size=len(self.student_ids)*10))
        })
        student_id = self.student_ids[4]
        expected_avg = scores[scores['Student'] == student_id]['Score'].mean()
        expected_std = scores[scores['Student'] == student_id]['Score'].std()

        avg, std = f_681(scores, student_id)
        self.assertAlmostEqual(expected_avg, avg, places=2)
        self.assertAlmostEqual(expected_std, std, places=2)



if __name__ == "__main__":
    run_tests()