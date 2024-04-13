import pandas as pd
import random
import re

def f_765(person_names, email_domains, num_records=5):
    """
    Generate a DataFrame with a specified number of records containing personal names and emails. 
    The emails are cleaned by replacing all occurrences of "@" with "[at]".
    
    Parameters:
    - person_names (list of str): A list of person names to use in the records.
    - email_domains (list of str): A list of email domains to use in the records.
    - num_records (int, optional): The number of records to generate. Default is 5.
    
    Returns:
    - DataFrame: A pandas DataFrame with columns 'Name' and 'Email' containing the person names and cleaned emails.
    
    Requirements:
    - pandas for DataFrame manipulation
    - random for random selection
    - re for regular expression operations
    
    Raises:
    - ValueError: If the number of names provided is less than the number of records requested or if no email domains are provided.
    
    Example:
    >>> f_765(['John Doe', 'Jane Smith'], ['gmail.com', 'yahoo.com'], 2)
             Name              Email
    0    John Doe  john[at]yahoo.com
    1  Jane Smith  jane[at]gmail.com
    >>> f_765(['Alice'], ['outlook.com'], 1)
        Name                 Email
    0  Alice  alice[at]outlook.com
    """
    if len(person_names) < num_records or len(email_domains) == 0:
        raise ValueError("Insufficient number of names or domains provided.")
    
    data = []
    
    # Randomly select 'num_records' names from the provided list
    selected_names = random.sample(person_names, num_records)

    for name in selected_names:
        email = re.sub('@', '[at]', '{}@{}'.format(name.split()[0].lower(), random.choice(email_domains)))
        data.append([name, email])

    df = pd.DataFrame(data, columns=['Name', 'Email'])
    return df

import unittest
import pandas as pd

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_case_1(self):
        random.seed(0)  # Initialize random seed
        result_df = f_765(['John Doe', 'Jane Smith'], ['gmail.com', 'yahoo.com'], 2)
        self.assertTrue(isinstance(result_df, pd.DataFrame))
        self.assertEqual(len(result_df), 2)
        self.assertTrue(set(result_df.columns) == {'Name', 'Email'})
        self.assertTrue(all(result_df['Email'].str.contains('[at]')))
        
    def test_case_2(self):
        random.seed(0)  # Initialize random seed
        result_df = f_765(['Alice'], ['outlook.com'], 1)
        self.assertTrue(isinstance(result_df, pd.DataFrame))
        self.assertEqual(len(result_df), 1)
        self.assertTrue(set(result_df.columns) == {'Name', 'Email'})
        self.assertTrue(all(result_df['Email'].str.contains('[at]')))
        
    def test_case_3(self):
        random.seed(0)  # Initialize random seed
        with self.assertRaises(ValueError):
            f_765(['John Doe'], ['gmail.com'], 2)
            
    def test_case_4(self):
        random.seed(0)  # Initialize random seed
        with self.assertRaises(ValueError):
            f_765(['John Doe', 'Jane Smith'], [], 2)
            
    def test_case_5(self):
        random.seed(0)  # Initialize random seed
        result_df = f_765(['John Doe', 'Jane Smith', 'Bob'], ['gmail.com', 'yahoo.com'], 3)
        self.assertTrue(isinstance(result_df, pd.DataFrame))
        self.assertEqual(len(result_df), 3)
        self.assertTrue(set(result_df.columns) == {'Name', 'Email'})
        self.assertTrue(all(result_df['Email'].str.contains('[at]')))

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    run_tests()