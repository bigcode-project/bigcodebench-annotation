import collections
import random
import json

# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

def f_974(department_data):
    """
    Generate a JSON object from employee data based on given department codes and their employee counts.

    Note:
    - The keys are department codes (from the list: ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']) and the values are lists of 
    employee levels ('Junior', 'Mid', 'Senior') in that department.

    Parameters:
    department_data (dict): A dictionary with department codes as keys and number of employees as values.

    Returns:
    str: A JSON object representing employee levels for each department.

    Requirements:
    - collections
    - random
    - json

    Example:
    >>> random.seed(0)
    >>> department_info = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 8, 'HR$$': 7}
    >>> level_data_json = f_974(department_info)
    >>> print(level_data_json)
    {"EMP$$": ["Mid", "Mid", "Junior", "Mid", "Senior", "Mid", "Mid", "Mid", "Mid", "Mid"], "MAN$$": ["Senior", "Junior", "Senior", "Junior", "Mid"], "DEV$$": ["Junior", "Junior", "Senior", "Mid", "Senior", "Senior", "Senior", "Junior"], "HR$$": ["Mid", "Junior", "Senior", "Junior", "Senior", "Mid", "Mid"]}
    """
    level_data = collections.defaultdict(list)
    
    for prefix, num_employees in department_data.items():
        if prefix not in PREFICES:
            continue

        for _ in range(num_employees):
            level = random.choice(LEVELS)
            level_data[prefix].append(level)

    return json.dumps(level_data)

import unittest
import collections
import random
import json

# Constants
PREFICES = ['EMP$$', 'MAN$$', 'DEV$$', 'HR$$']
LEVELS = ['Junior', 'Mid', 'Senior']

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(EmployeeLevelDataTests))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class EmployeeLevelDataTests(unittest.TestCase):
    
    def test_case_1(self):
        random.seed(0)
        input_data = {'EMP$$': 5, 'MAN$$': 3, 'DEV$$': 4, 'HR$$': 2}
        output_data = f_974(input_data)
        parsed_output = json.loads(output_data)
        
        for key, value in input_data.items():
            self.assertIn(key, parsed_output)
            self.assertEqual(len(parsed_output[key]), value)
            for level in parsed_output[key]:
                self.assertIn(level, LEVELS)
    
    def test_case_2(self):
        random.seed(0)
        input_data = {'EMP$$': 10}
        output_data = f_974(input_data)
        parsed_output = json.loads(output_data)
        
        self.assertEqual(len(parsed_output), 1)
        self.assertEqual(len(parsed_output['EMP$$']), 10)
        for level in parsed_output['EMP$$']:
            self.assertIn(level, LEVELS)
    
    def test_case_3(self):
        random.seed(0)
        input_data = {'MAN$$': 6, 'DEV$$': 7}
        output_data = f_974(input_data)
        parsed_output = json.loads(output_data)
        
        self.assertEqual(len(parsed_output), 2)
        self.assertEqual(len(parsed_output['MAN$$']), 6)
        self.assertEqual(len(parsed_output['DEV$$']), 7)
        for level in parsed_output['MAN$$']:
            self.assertIn(level, LEVELS)
        for level in parsed_output['DEV$$']:
            self.assertIn(level, LEVELS)
    
    def test_case_4(self):
        random.seed(0)
        input_data = {'HR$$': 3}
        output_data = f_974(input_data)
        parsed_output = json.loads(output_data)
        
        self.assertEqual(len(parsed_output), 1)
        self.assertEqual(len(parsed_output['HR$$']), 3)
        for level in parsed_output['HR$$']:
            self.assertIn(level, LEVELS)
    
    def test_case_5(self):
        random.seed(0)
        input_data = {}
        output_data = f_974(input_data)
        parsed_output = json.loads(output_data)
        self.assertEqual(len(parsed_output), 0)


if __name__ == "__main__":
    run_tests()