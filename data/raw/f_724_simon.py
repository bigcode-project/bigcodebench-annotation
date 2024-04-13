import sqlite3
import pandas as pd
import os


def f_724(db_file, table_name, column_name, pattern='\d+[xX]'):
    """
    Find all matches with a regex pattern in a list of strings in an SQL database.
    
    The function loads an sql database and selects all entries from the specified
    table. All entries of the specified column are matched against a regex pattern.
    Matches are returned in a DataFrame.

    Parameters:
    db_file (str): The SQLite database file.
    table_name (str): The name of the table to search.
    column_name (str): The name of the column to search.
    pattern (str, optional): The regex pattern to search for. Defaults to '\d+[xX]'.

    Returns:
    DataFrame: A pandas DataFrame with the matches.
        
    Raises:
    ValueError: If db_file does not exist.

    Requirements:
    - sqlite3
    - pandas
    - os
        
    Example:
    >>> result = f_724('f_724_data_simon/sample.db', 'test_table', 'test_column')
    >>> print(result.head(10))
        id              test_column
    0    1                  4x4 car
    1    2           New 3x3 puzzle
    3    4  Product with 5X feature
    55  56                   1xsafe
    56  57                 3xmother
    57  58                  5xenjoy
    58  59                   2xhome
    59  60                 3xanswer
    60  61                   5xgirl
    61  62                   5xkind

    >>> result = f_724('f_724_data_simon/sample.db', 'test_table', 'test_column', pattern='kind')
    >>> print(result)
        id                                        test_column
    20  21  To between successful ever ago PM toward today...
    42  43  Entire manage wife management perform size def...
    61  62                                             5xkind
    """

    if not os.path.isfile(db_file):
        raise ValueError('db_file does not exist.')
    
    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    
    if df[column_name].dtype == 'object':  # Check if the column data type is a string
        matches = df[df[column_name].str.contains(pattern)]
    else:
        matches = pd.DataFrame(columns=df.columns)  # Return an empty DataFrame
    
    return matches

import unittest
import pandas as pd
import os
import os

class TestCases(unittest.TestCase):

    def setUp(self) -> None:
        self.db_path = os.path.join('f_724_data_simon', 'sample.db')
        self.empty_path = os.path.join('f_724_data_simon', 'empty.db')

    def test_case_1(self):
        # Input: Database with known data, table name, and column name
        result = f_724(self.db_path, 'test_table', 'test_column')
        excpected = pd.DataFrame(
           {'id': {0: 1,
                1: 2,
                3: 4,
                55: 56,
                56: 57,
                57: 58,
                58: 59,
                59: 60,
                60: 61,
                61: 62,
                62: 63,
                63: 64,
                64: 65,
                65: 66,
                66: 67,
                67: 68,
                68: 69,
                69: 70,
                70: 71,
                71: 72,
                72: 73,
                73: 74,
                74: 75,
                75: 76,
                76: 77,
                77: 78,
                78: 79,
                79: 80,
                80: 81,
                81: 82,
                82: 83,
                83: 84,
                84: 85,
                85: 86,
                86: 87,
                87: 88,
                88: 89,
                89: 90,
                90: 91,
                91: 92,
                92: 93,
                93: 94,
                94: 95,
                95: 96,
                96: 97,
                97: 98,
                98: 99,
                99: 100,
                100: 101,
                101: 102,
                102: 103,
                103: 104,
                104: 105},
                'test_column': {0: '4x4 car',
                1: 'New 3x3 puzzle',
                3: 'Product with 5X feature',
                55: '1xsafe',
                56: '3xmother',
                57: '5xenjoy',
                58: '2xhome',
                59: '3xanswer',
                60: '5xgirl',
                61: '5xkind',
                62: '4xsituation',
                63: '2xsimilar',
                64: '1xloss',
                65: '4xdifficult',
                66: '7xsea',
                67: '1xpeace',
                68: '1xyourself',
                69: '3xoccur',
                70: '2xbill',
                71: '7xmore',
                72: '4xeye',
                73: '4xgoal',
                74: '7xwhite',
                75: '7xsix',
                76: '9xcourt',
                77: '2xhave',
                78: '2xremain',
                79: '2xbehind',
                80: '5xdeep',
                81: '7xold',
                82: '7xstatement',
                83: '1xok',
                84: '4xsport',
                85: '2xtraining',
                86: '3xclearly',
                87: '3xsupport',
                88: '8xrecord',
                89: '7xpretty',
                90: '7xlawyer',
                91: '5ximage',
                92: '3xperformance',
                93: '1xyet',
                94: '4xproduce',
                95: '2xpolitics',
                96: '8xback',
                97: '1xpartner',
                98: '5xduring',
                99: '5xcoach',
                100: '1xproject',
                101: '6xgirl',
                102: '1xmember',
                103: '6xkitchen',
                104: '9xarm'}}
        )

        # Check if the result is a DataFrame
        self.assertIsInstance(result, pd.DataFrame)
        
        # Check if the returned DataFrame has more matches than the initially inserted ones
        # Since we added 50 more entries that match the regex pattern
        self.assertEqual(len(result), 53)
        pd.testing.assert_frame_equal(result, excpected)

    def test_case_2(self):
        # Test with a column that has no matches
        result = f_724(self.db_path, 'test_table', 'id')
        self.assertEqual(len(result), 0)

    def test_case_3(self):
        # Test with a non-existent table
        with self.assertRaises(Exception):
            f_724(self.db_path, 'non_existent_table', 'test_column')

    def test_case_4(self):
        # Test with a non-existent column
        with self.assertRaises(Exception):
            f_724(self.db_path, 'test_table', 'non_existent_column')
            
    def test_case_5(self):
        # Test with a database that has no tables (we'll create an empty db for this)
        empty_db_path = os.path.join("f_724_data_simon", "empty.db")
        
        with self.assertRaises(Exception):
            f_724(self.empty_path, 'test_table', 'test_column')
            
    def test_case_6(self):
        # Test with a non-existent database file
        db_path = os.path.join("f_724_data_simon", "non_existent.db")

        with self.assertRaises(Exception):
            f_724(db_path, 'test_table', 'test_column')
    
    def test_case_7(self):
        # Test with a different regex pattern
        # Here, we are trying to match any word characters (alphanumeric characters plus underscore)
        result = f_724(self.db_path, 'test_table', 'test_column', pattern='ab')
        expected = pd.DataFrame(
            {'id': {14: 15, 15: 16, 21: 22, 30: 31},
 'test_column': {14: 'Hand soon trip sing. Plan cost tell spend that quality. After listen help summer likely able.',
  15: 'War not century support. That send other president everybody yourself necessary.\nLess rather recent study dream buy Democrat. Environmental game thus first about air reality left.',
  21: 'Feel establish would our each. Even cup college decide alone free dark product. Full great during avoid approach.',
  30: 'Store foot near interest husband. View several position write keep guy wrong. Degree either blue plan up table beat.\nFire while less section. My save cost nation paper affect between.'}}
        )
        # Check if the result is a DataFrame
        self.assertIsInstance(result, pd.DataFrame)
        
        # Check if the returned DataFrame has matches
        self.assertEqual(len(result), 4)
        pd.testing.assert_frame_equal(result, expected)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()