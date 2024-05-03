import random
import statistics

# Constants
AGE_RANGE = (22, 60)

def f_973(dict1):
    """
    Calculate the mean, the median, and the mode(s) of the age of the employees in the department "EMP$$." 
    Generate random ages for each employee within the range [22, 60].

    Parameters:
    dict1 (dict): A dictionary with department codes as keys and number of employees 
                  as values.

    Returns:
    tuple: A tuple of mean, median, and a list of mode(s) of employee ages.

    Requirements:
    - random
    - statistics

    Example:
    >>> d = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 8, 'HR$$': 7}
    >>> stats = f_973(d)
    >>> print(stats)
    (Mean of ages, Median of ages, [List of modes])
    """
    emp_ages = []
    
    for prefix, num_employees in dict1.items():
        if not prefix.startswith('EMP$$'):
            continue

        for _ in range(num_employees):
            age = random.randint(*AGE_RANGE)
            emp_ages.append(age)

    # If no employees in EMP$$ department
    if not emp_ages:
        return 0, 0, []
    
    mean_age = statistics.mean(emp_ages)
    median_age = statistics.median(emp_ages)
    mode_age = statistics.multimode(emp_ages)

    return mean_age, median_age, mode_age

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        # Input: 10 employees in "EMP$$" department
        d = {'EMP$$': 10}
        mean_age, median_age, mode_age = f_973(d)
        
        # Checks
        self.assertTrue(22 <= mean_age <= 60)
        self.assertTrue(22 <= median_age <= 60)
        self.assertTrue(all(22 <= age <= 60 for age in mode_age))
    
    def test_case_2(self):
        # Input: Different number of employees in multiple departments
        d = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 8, 'HR$$': 7}
        mean_age, median_age, mode_age = f_973(d)
        
        # Checks
        self.assertTrue(22 <= mean_age <= 60)
        self.assertTrue(22 <= median_age <= 60)
        self.assertTrue(all(22 <= age <= 60 for age in mode_age))
    
    def test_case_3(self):
        # Input: No employees in "EMP$$" department
        d = {'MAN$$': 5, 'DEV$$': 8, 'HR$$': 7}
        mean_age, median_age, mode_age = f_973(d)
        
        # Checks
        self.assertEqual(mean_age, 0)
        self.assertEqual(median_age, 0)
        self.assertEqual(mode_age, [])
    
    def test_case_4(self):
        # Input: Large number of employees in "EMP$$" department to increase likelihood of multiple modes
        d = {'EMP$$': 1000}
        mean_age, median_age, mode_age = f_973(d)
        
        # Checks
        self.assertTrue(22 <= mean_age <= 60)
        self.assertTrue(22 <= median_age <= 60)
        self.assertTrue(all(22 <= age <= 60 for age in mode_age))
    
    def test_case_5(self):
        # Input: Only one employee in "EMP$$" department
        d = {'EMP$$': 1}
        mean_age, median_age, mode_age = f_973(d)
        
        # Checks
        self.assertTrue(22 <= mean_age <= 60)
        self.assertEqual(mean_age, median_age)
        self.assertEqual([mean_age], mode_age)

# Run the tests
run_tests()
if __name__ == "__main__":
    run_tests()