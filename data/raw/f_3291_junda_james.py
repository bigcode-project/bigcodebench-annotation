import os
import pandas as pd
from datetime import datetime

def f_3291(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Filters data in a specific date range from a column in an Excel file and returns a Pandas DataFrame of the filtered data.

    Parameters:
    excel_directory (str): The directory of the Excel file.
    file_name (str): The name of the Excel file.
    column_name (str): The name of the date column to filter.
    start_date (str): The start date in 'yyyy-mm-dd' format.
    end_date (str): The end date in 'yyyy-mm-dd' format.

    Returns:
    pd.DataFrame: A pandas DataFrame with the filtered data.

    Raises:
    FileNotFoundError: If the specified Excel file does not exist.
    ValueError: If start_date or end_date are in an incorrect format, or if column_name does not exist in the DataFrame.

    Example:
    >>> data_dir, file_name = './excel_files/', 'excel_file1.xls'
    >>> test_file = create_dummy_file(data_dir, file_name)
    >>> filtered_df = f_3291(data_dir, file_name, 'Date', '2020-01-01', '2020-12-31')
    >>> os.remove(test_file)
    >>> os.rmdir(data_dir)
    >>> print(filtered_df.head())
       Unnamed: 0       Date     Value
    0           0 2020-01-01  0.823110
    1           1 2020-01-02  0.026118
    2           2 2020-01-03  0.210771
    3           3 2020-01-04  0.618422
    4           4 2020-01-05  0.098284
    
    Requirements:
    - os
    - pandas
    - datetime
    - numpy
    """
    excel_file = os.path.join(excel_directory, file_name)
    if not os.path.exists(excel_file):
        raise FileNotFoundError(f"The file {excel_file} does not exist.")

    df = pd.read_excel(excel_file)

    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} does not exist in the DataFrame.")

    try:
        df[column_name] = pd.to_datetime(df[column_name])
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Date format is incorrect. Please use 'yyyy-mm-dd' format.") from e

    filtered_df = df[(df[column_name] >= start_date) & (df[column_name] <= end_date)]

    return filtered_df

import unittest
import pandas as pd
import numpy as np
import os
from datetime import datetime

def create_dummy_file(data_dir, file_name):
    os.makedirs(data_dir, exist_ok=True)
    np.random.seed(52)
    test_data = pd.DataFrame({
        'Date': pd.date_range(start='2020-01-01', periods=100, freq='D'),
        'Value': np.random.rand(100)
    })
    test_file = os.path.join(data_dir, file_name)
    test_data.to_excel(test_file)
    return test_file

class TestCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create dummy Excel file for testing
        cls.test_dir = 'test_excel_files'
        os.makedirs(cls.test_dir, exist_ok=True)
        np.random.seed(52)
        test_data = pd.DataFrame({
            'Date': pd.date_range(start='2020-01-01', periods=100, freq='D'),
            'Value': np.random.rand(100)
        })
        cls.test_file = os.path.join(cls.test_dir, 'test_file.xls')
        test_data.to_excel(cls.test_file)

    @classmethod
    def tearDownClass(cls):
        # Cleanup test directory
        os.remove(cls.test_file)
        os.rmdir(cls.test_dir)

    def test_valid_input(self):
        filtered_df = f_3291(self.test_dir, 'test_file.xls', 'Date', '2020-01-01', '2020-04-10')
        self.assertTrue(len(filtered_df) > 0)
        self.assertTrue((filtered_df['Date'] >= datetime(2020, 1, 1)).all())
        self.assertTrue((filtered_df['Date'] <= datetime(2020, 4, 10)).all())
        
        df_list = filtered_df.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        # with open('df_contents.txt', 'w') as file:
        #     file.write(str(df_list))
            
        expect = ['0,2020-01-01 00:00:00,0.8231103407097919', '1,2020-01-02 00:00:00,0.026117981569867332', '2,2020-01-03 00:00:00,0.21077063993129397', '3,2020-01-04 00:00:00,0.6184217693496102', '4,2020-01-05 00:00:00,0.09828446533689916', '5,2020-01-06 00:00:00,0.6201313098768588', '6,2020-01-07 00:00:00,0.053890219598443756', '7,2020-01-08 00:00:00,0.9606540578042385', '8,2020-01-09 00:00:00,0.9804293742150735', '9,2020-01-10 00:00:00,0.5211276502712239', '10,2020-01-11 00:00:00,0.6365533448355478', '11,2020-01-12 00:00:00,0.7647569482692499', '12,2020-01-13 00:00:00,0.7649552946168192', '13,2020-01-14 00:00:00,0.41768557955972274', '14,2020-01-15 00:00:00,0.7688053063237427', '15,2020-01-16 00:00:00,0.4232017504120317', '16,2020-01-17 00:00:00,0.9261035715268315', '17,2020-01-18 00:00:00,0.6819264848723984', '18,2020-01-19 00:00:00,0.3684555913246884', '19,2020-01-20 00:00:00,0.85890985535282', '20,2020-01-21 00:00:00,0.38049567998338985', '21,2020-01-22 00:00:00,0.09495426388360773', '22,2020-01-23 00:00:00,0.3248907136368232', '23,2020-01-24 00:00:00,0.41511218614249124', '24,2020-01-25 00:00:00,0.7422739488503802', '25,2020-01-26 00:00:00,0.6579088675866257', '26,2020-01-27 00:00:00,0.20131683134279676', '27,2020-01-28 00:00:00,0.808487913243346', '28,2020-01-29 00:00:00,0.7864024384097678', '29,2020-01-30 00:00:00,0.3949396379041129', '30,2020-01-31 00:00:00,0.5106162349890584', '31,2020-02-01 00:00:00,0.7961595415020245', '32,2020-02-02 00:00:00,0.4453774958910275', '33,2020-02-03 00:00:00,0.7430669105102151', '34,2020-02-04 00:00:00,0.07874907332177594', '35,2020-02-05 00:00:00,0.4876452580166796', '36,2020-02-06 00:00:00,0.4343886448729798', '37,2020-02-07 00:00:00,0.24605794567291628', '38,2020-02-08 00:00:00,0.8616407182731707', '39,2020-02-09 00:00:00,0.020022559117985117', '40,2020-02-10 00:00:00,0.45082670983145', '41,2020-02-11 00:00:00,0.04742287434525816', '42,2020-02-12 00:00:00,0.4977274961778495', '43,2020-02-13 00:00:00,0.8587740041280045', '44,2020-02-14 00:00:00,0.3348156564151846', '45,2020-02-15 00:00:00,0.9015900311504366', '46,2020-02-16 00:00:00,0.1228875539702794', '47,2020-02-17 00:00:00,0.15743374693326317', '48,2020-02-18 00:00:00,0.7873852916367928', '49,2020-02-19 00:00:00,0.6649390578290946', '50,2020-02-20 00:00:00,0.7202041723984404', '51,2020-02-21 00:00:00,0.5392553233782389', '52,2020-02-22 00:00:00,0.4719474542548665', '53,2020-02-23 00:00:00,0.9006875037302683', '54,2020-02-24 00:00:00,0.37451251076585956', '55,2020-02-25 00:00:00,0.5277864449097718', '56,2020-02-26 00:00:00,0.6944934244649952', '57,2020-02-27 00:00:00,0.425568262771457', '58,2020-02-28 00:00:00,0.6385766794385177', '59,2020-02-29 00:00:00,0.5943246846083065', '60,2020-03-01 00:00:00,0.4542809790228073', '61,2020-03-02 00:00:00,0.9157764166967288', '62,2020-03-03 00:00:00,0.7440674029374216', '63,2020-03-04 00:00:00,0.9294858018400058', '64,2020-03-05 00:00:00,0.8911779892563932', '65,2020-03-06 00:00:00,0.32033320619063854', '66,2020-03-07 00:00:00,0.6900263485800929', '67,2020-03-08 00:00:00,0.058868078357722564', '68,2020-03-09 00:00:00,0.20178386343344057', '69,2020-03-10 00:00:00,0.7230617666544835', '70,2020-03-11 00:00:00,0.7520099236736953', '71,2020-03-12 00:00:00,0.29538112744121003', '72,2020-03-13 00:00:00,0.958446920480605', '73,2020-03-14 00:00:00,0.004363273526967193', '74,2020-03-15 00:00:00,0.34974214023403494', '75,2020-03-16 00:00:00,0.19748236998530688', '76,2020-03-17 00:00:00,0.4375885112215021', '77,2020-03-18 00:00:00,0.9296156676737218', '78,2020-03-19 00:00:00,0.28024548115249903', '79,2020-03-20 00:00:00,0.42788389922088954', '80,2020-03-21 00:00:00,0.4651649617638387', '81,2020-03-22 00:00:00,0.8551238146044345', '82,2020-03-23 00:00:00,0.98438684194162', '83,2020-03-24 00:00:00,0.47772756497270474', '84,2020-03-25 00:00:00,0.536704363369267', '85,2020-03-26 00:00:00,0.782204582357083', '86,2020-03-27 00:00:00,0.814825266813197', '87,2020-03-28 00:00:00,0.1456551348709756', '88,2020-03-29 00:00:00,0.3432296625039042', '89,2020-03-30 00:00:00,0.6956199030600098', '90,2020-03-31 00:00:00,0.18821937901900487', '91,2020-04-01 00:00:00,0.4554246915674217', '92,2020-04-02 00:00:00,0.9704230791517012', '93,2020-04-03 00:00:00,0.9943457894909822', '94,2020-04-04 00:00:00,0.750508378633138', '95,2020-04-05 00:00:00,0.5122888937915386', '96,2020-04-06 00:00:00,0.5147723383402653', '97,2020-04-07 00:00:00,0.06917213261814714', '98,2020-04-08 00:00:00,0.9711823643126941', '99,2020-04-09 00:00:00,0.9548204075970019']
        
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")

    def test_invalid_file_path(self):
        with self.assertRaises(FileNotFoundError):
            f_3291('invalid_dir', 'test_file.xls', 'Date', '2020-01-01', '2020-12-31')

    def test_invalid_column_name(self):
        with self.assertRaises(ValueError):
            f_3291(self.test_dir, 'test_file.xls', 'NonexistentColumn', '2020-01-01', '2020-12-31')

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            f_3291(self.test_dir, 'test_file.xls', 'Date', '01-01-2020', '12-31-2020')

    def test_no_data_in_range(self):
        filtered_df = f_3291(self.test_dir, 'test_file.xls', 'Date', '2021-01-01', '2021-12-31')
        self.assertEqual(len(filtered_df), 0)

# Run the tests
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