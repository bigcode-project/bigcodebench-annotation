import csv
import os
from collections import Counter

# Constants
CSV_FILE_PATH = 'match_data.csv'

def f_673(goals, penalties):
    """
    Count the total number of goals and penalties from a CSV file and update it with the given goals and penalties.

    Parameters:
    - goals (dict): A dictionary where keys are team names and values are numbers of goals scored.
    - penalties (dict): A dictionary where keys are team names and values are numbers of penalties incurred.

    Returns:
    - count (Counter.collections): A Counter object with total counts of goals and penalties.

    Requirements:
    - csv
    - os
    - collections.Counter

    Example:
    >>> goals = {'Team A': 3, 'Team B': 2, 'Team C': 1, 'Team D': 0, 'Team E': 2}
    >>> penalties = {'Team A': 1, 'Team B': 0, 'Team C': 2, 'Team D': 3, 'Team E': 1}
    >>> counts = f_673(goals, penalties)
    >>> print(counts)
    Counter({'goals': 8, 'penalties': 7})
    """
    counts = Counter()

    if os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                counts['goals'] += int(row['goals'])
                counts['penalties'] += int(row['penalties'])

    for team, team_goals in goals.items():
        counts['goals'] += team_goals

    for team, team_penalties in penalties.items():
        counts['penalties'] += team_penalties

    return counts

import unittest
from collections import Counter
import os
import csv

def test_case_1(self):
    """
    Test Case 1:
    Test with no existing CSV file and empty dictionaries.
    Expected result: {'goals': 0, 'penalties': 0}
    """
    goals = {}
    penalties = {}
    result = f_673(goals, penalties, csv_file_path='non_existent_file.csv')
    expected_result = {'goals': 0, 'penalties': 0}
    self.assertEqual(result, expected_result, "Test Case 1 Failed")

def test_case_2(self):
    """
    Test Case 2:
    Test with existing CSV file and non-empty dictionaries.
    Expected result: {'goals': 11, 'penalties': 6}
    """
    goals = {'Team A': 3, 'Team B': 2}
    penalties = {'Team A': 1, 'Team C': 2}
    # Creating a sample CSV file for this test case
    csv_content = "team,goals,penalties\nTeam A,2,1\nTeam B,1,2\nTeam C,3,0\n"
    with open('test_data/test_case_2.csv', 'w') as f:
        f.write(csv_content)
    result = f_673(goals, penalties, csv_file_path='test_data/test_case_2.csv')
    expected_result = {'goals': 11, 'penalties': 6}
    self.assertEqual(result, expected_result, "Test Case 2 Failed")

def test_case_3(self):
    """
    Test Case 3:
    Test with existing CSV file and empty dictionaries.
    Expected result: {'goals': 8, 'penalties': 3}
    """
    goals = {}
    penalties = {}
    # Creating a sample CSV file for this test case
    csv_content = "team,goals,penalties\nTeam A,5,2\nTeam B,3,1\n"
    with open('test_data/test_case_3.csv', 'w') as f:
        f.write(csv_content)
    result = f_673(goals, penalties, csv_file_path='test_data/test_case_3.csv')
    expected_result = {'goals': 8, 'penalties': 3}
    self.assertEqual(result, expected_result, "Test Case 3 Failed")

def test_case_4(self):
    """
    Test Case 4:
    Test with no existing CSV file and non-empty dictionaries.
    Expected result: {'goals': 5, 'penalties': 3}
    """
    goals = {'Team A': 2, 'Team B': 3}
    penalties = {'Team A': 1, 'Team C': 2}
    result = f_673(goals, penalties, csv_file_path='non_existent_file.csv')
    expected_result = {'goals': 5, 'penalties': 3}
    self.assertEqual(result, expected_result, "Test Case 4 Failed")

def test_case_5(self):
    """
    Test Case 5:
    Test with existing CSV file, non-empty dictionaries, and negative values.
    Expected result: {'goals': 7, 'penalties': 2}
    """
    goals = {'Team A': -2, 'Team B': 3}
    penalties = {'Team A': 1, 'Team C': -2}
    # Creating a sample CSV file for this test case
    csv_content = "team,goals,penalties\nTeam A,2,1\nTeam B,1,2\nTeam C,3,0\n"
    with open('test_data/test_case_5.csv', 'w') as f:
        f.write(csv_content)
    result = f_673(goals, penalties, csv_file_path='test_data/test_case_5.csv')
    expected_result = {'goals': 7, 'penalties': 2}
    self.assertEqual(result, expected_result, "Test Case 5 Failed")

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()