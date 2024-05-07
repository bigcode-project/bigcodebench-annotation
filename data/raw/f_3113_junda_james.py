import pandas as pd
from texttable import Texttable
import os
import glob

def f_3113(data_dir='./data/'):
    """
    Generates a summary table of all CSV files in a specified directory using Texttable. 
    If an empty CSV file is encountered, a pandas.errors.EmptyDataError is raised.

    Parameters:
    - data_dir (str): The directory to search for CSV files. Default is './data/'.

    Returns:
    - str: A string representation of the table summarizing the CSV files. Each row contains the file name, number of rows, and number of columns.

    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    - ValueError: If there are no CSV files in the specified directory.
    - pandas.errors.EmptyDataError: If an empty CSV file is encountered.

    Requirements:
    - pandas
    - texttable
    - os
    - glob

    Example:
    >>> data_dir = './data/'
    >>> dummy_files = create_dummy_files(data_dir)
    >>> print(f_3113(data_dir))
    +-----------+------+---------+
    |   File    | Rows | Columns |
    +===========+======+=========+
    | test2.csv | 10   | 4       |
    +-----------+------+---------+
    | test2.csv | 10   | 4       |
    +-----------+------+---------+
    | test1.csv | 5    | 2       |
    +-----------+------+---------+
    | test1.csv | 5    | 2       |
    +-----------+------+---------+
    >>> tear_down_dummy_files(data_dir, dummy_files)
    """
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"The directory '{data_dir}' does not exist.")

    data_files = glob.glob(os.path.join(data_dir, '*.csv'))
    if not data_files:
        raise ValueError(f"No CSV files found in the directory '{data_dir}'.")

    summary_data = []
    for file in data_files:
        try:
            data = pd.read_csv(file)
            summary_data.append([os.path.basename(file), data.shape[0], data.shape[1]])
        except pd.errors.EmptyDataError:
            # Handle empty CSV file
            raise pd.errors.EmptyDataError(f"Error when reading file '{file}'.")
        data = pd.read_csv(file)
        summary_data.append([os.path.basename(file), data.shape[0], data.shape[1]])

    table = Texttable()
    table.add_rows([['File', 'Rows', 'Columns']] + summary_data)

    return table.draw()

import unittest
import pandas as pd
import os

def create_dummy_files(data_dir):
    os.makedirs(data_dir, exist_ok=True)

    # Creating dummy CSV files with more diverse data
    dummy_files = ['test1.csv', 'test2.csv']

    # Create a DataFrame with a range of integers
    pd.DataFrame({'col1': range(5), 'col2': range(5, 10)}).to_csv(data_dir + dummy_files[0], index=False)

    # Create a DataFrame with mixed data types and missing values
    mixed_data = pd.DataFrame({
        'a': range(10),
        'b': [float(x) for x in range(10)],
        'c': list('abcdefghij'),
        'd': [None if x % 2 == 0 else x for x in range(10)]
    })
    mixed_data.to_csv(data_dir + dummy_files[1], index=False)
    return dummy_files

def tear_down_dummy_files(data_dir, dummy_files):
    # Cleaning up the dummy data directory
    for file in dummy_files:
        os.remove(data_dir + file)
    os.rmdir(data_dir)

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Setting up a dummy data directory
        cls.test_data_dir = './test_data/'
        os.makedirs(cls.test_data_dir, exist_ok=True)

        # Creating dummy CSV files with more diverse data
        cls.dummy_files = ['test1.csv', 'test2.csv', 'empty.csv']

        # Create a DataFrame with a range of integers
        pd.DataFrame({'col1': range(5), 'col2': range(5, 10)}).to_csv(cls.test_data_dir + cls.dummy_files[0], index=False)

        # Create a DataFrame with mixed data types and missing values
        mixed_data = pd.DataFrame({
            'a': range(10),
            'b': [float(x) for x in range(10)],
            'c': list('abcdefghij'),
            'd': [None if x % 2 == 0 else x for x in range(10)]
        })
        mixed_data.to_csv(cls.test_data_dir + cls.dummy_files[1], index=False)

        # Empty DataFrame for the third file
        pd.DataFrame().to_csv(cls.test_data_dir + cls.dummy_files[2], index=False)


    @classmethod
    def tearDownClass(cls):
        # Cleaning up the dummy data directory
        for file in cls.dummy_files:
            os.remove(cls.test_data_dir + file)
        os.rmdir(cls.test_data_dir)
        os.rmdir('./empty_test_data/')

    def test_normal_functionality(self):
        os.remove(self.test_data_dir + 'empty.csv')
        table_str = f_3113(self.test_data_dir)
        with open('df_contents.txt', 'w') as file:
            file.write(str(table_str))
            
        expect_str = '''+-----------+------+---------+
|   File    | Rows | Columns |
+===========+======+=========+
| test2.csv | 10   | 4       |
+-----------+------+---------+
| test2.csv | 10   | 4       |
+-----------+------+---------+
| test1.csv | 5    | 2       |
+-----------+------+---------+
| test1.csv | 5    | 2       |
+-----------+------+---------+'''

        self.assertEqual(expect_str, table_str)
        pd.DataFrame().to_csv(self.test_data_dir + 'empty.csv', index=False)
        
    def test_directory_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            f_3113('./nonexistent_directory/')

    def test_no_csv_files(self):
        with self.assertRaises(ValueError):
            empty_dir = './empty_test_data/'
            os.makedirs(empty_dir, exist_ok=True)
            f_3113(empty_dir)
            os.rmdir(empty_dir)

    def test_empty_csv_file(self):
        with self.assertRaises(pd.errors.EmptyDataError):
            f_3113(self.test_data_dir)

    def test_file_path_in_output(self):
        # Temporarily remove the empty CSV file
        os.remove(self.test_data_dir + 'empty.csv')
        table_str = f_3113(self.test_data_dir)
        for file in self.dummy_files:
            if file != 'empty.csv':  # Skip the empty file
                self.assertIn(file, table_str)
        # Restore the empty CSV file
        pd.DataFrame().to_csv(self.test_data_dir + 'empty.csv', index=False)

def run_tests():
    """Run all tests for this function."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCases)
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    run_tests()