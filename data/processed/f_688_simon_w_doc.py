import pandas as pd
from statistics import mean


def f_512(df: pd.DataFrame) -> dict:
    """
    Convert a Pandas DataFrame into a dictionary of generator objects in which 
    each generator generates a sequence of tuples that contain a unique name 
    and the corresponding average score for that name.

    Parameters:
    df (DataFrame): The DataFrame containing 'Name' (string) and 'Score' (number) columns to analyze.

    Returns:
    dict: A dictionary of generator objects. Each generator generates a tuple 
          containing a unique name and the corresponding average score for that name.

    Raises:
    ValueError: If the DataFrame does not have the 'Name' and 'Score' columns.

    Requirements:
    - pandas
    - statistics

    Example:
    >>> df_sample = pd.DataFrame({
    ...     'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
    ...     'Score': [85, 79, 90, 88, 82]
    ... })
    >>> gen_dict = f_512(df_sample)
    >>> {key: next(value) for key, value in gen_dict.items()}
    {'John': ('John', 86), 'Nick': ('Nick', 79), 'Tom': ('Tom', 86.5)}

    >>> df_sample = pd.DataFrame({
    ...     'Name': ['Micky', 'Donald', 'Girl'],
    ...     'Score': [25.2, 9, -1]
    ... })
    >>> gen_dict = f_512(df_sample)
    >>> {key: next(value) for key, value in gen_dict.items()}
    {'Donald': ('Donald', 9.0), 'Girl': ('Girl', -1.0), 'Micky': ('Micky', 25.2)}
    """

    if 'Name' not in df.columns or 'Score' not in df.columns:
        raise ValueError('The DataFram should have the columns "Name" and "Score".')

    grouped = df.groupby('Name')
    result_dict = {}
    for name, group in grouped:
        avg_score = mean(group['Score'])
        result_dict[name] = iter([(name, avg_score)])

    return result_dict

import unittest
import pandas as pd
from statistics import mean
from faker import Faker
fake = Faker()
class TestCases(unittest.TestCase):
    def test_case_wrong_columns(self):
        df_sample1 = pd.DataFrame({
            'A': ['Tom', 'Nick', 'John', 'Tom', 'John'],
            'Score': [85, 79, 90, 88, 82]
        })
        self.assertRaises(Exception, f_512, df_sample1)
    
    def test_case_1(self):
        df_test = pd.DataFrame({
            'Name': ['Tom', 'Nick', 'John'],
            'Score': [85, 79, 90]
        })
        gen_dict = f_512(df_test)
        expected_result = {
            'John': ('John', 90),
            'Nick': ('Nick', 79),
            'Tom': ('Tom', 85)
        }
        self.assertDictEqual({key: next(value) for key, value in gen_dict.items()}, expected_result)
    
    def test_case_2(self):
        df_test = pd.DataFrame({
            'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
            'Score': [85, 79, 90, 88, 82]
        })
        gen_dict = f_512(df_test)
        expected_result = {
            'John': ('John', 86),
            'Nick': ('Nick', 79),
            'Tom': ('Tom', 86.5)
        }
        self.assertDictEqual({key: next(value) for key, value in gen_dict.items()}, expected_result)
    
    def test_case_3(self):
        df_test = pd.DataFrame({
            'Name': ['Tom', 'Nick', 'John', 'Anna', 'Elsa'],
            'Score': [85, 79, 90, 88, 82]
        })
        gen_dict = f_512(df_test)
        expected_result = {
            'Anna': ('Anna', 88),
            'Elsa': ('Elsa', 82),
            'John': ('John', 90),
            'Nick': ('Nick', 79),
            'Tom': ('Tom', 85)
        }
        self.assertDictEqual({key: next(value) for key, value in gen_dict.items()}, expected_result)
    
    def test_case_4(self):
        names = [fake.first_name() for _ in range(10)]
        scores = [fake.random_int(min=50, max=100) for _ in range(10)]
        df_test = pd.DataFrame({
            'Name': names,
            'Score': scores
        })
        gen_dict = f_512(df_test)
        grouped = df_test.groupby('Name')
        expected_result = {name: (name, mean(group['Score'])) for name, group in grouped}
        self.assertDictEqual({key: next(value) for key, value in gen_dict.items()}, expected_result)
    
    def test_case_5(self):
        df_test = pd.DataFrame({
            'Name': [],
            'Score': []
        })
        gen_dict = f_512(df_test)
        self.assertDictEqual(gen_dict, {})
