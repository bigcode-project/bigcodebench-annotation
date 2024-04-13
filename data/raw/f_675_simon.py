import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def f_675(file_name: str) -> pd.DataFrame:
    """Normalize data in a csv file using MinMaxScaler from sklearn.
    Only numeric columns are normalized. Columns with other dtypes are left as
    they are.
    
    Parameters:
    file_name (str): The name of the csv file.
    
    Returns:
    DataFrame: A pandas DataFrame with normalized data.

    Raises:
    ValueError: If input does not have numeric columns.

    Requirements:
    - pandas
    - sklearn.preprocessing.MinMaxScaler
    
    Example:
    >>> normalized_data = f_675("sample.csv")
    >>> print(normalized_data.head())

    Name	Age	Salary
    0	Alex Anderson	0.304651	0.122298
    1	Mr. Leslie Casey	0.28140	0.598905
    2	Anthony George	0.996744	0.216552
    3	Brian Washington	0.126279	0.459948
    4	Elias Lawrence	0.337239	0.124185

    >>> normalized_data = f_675("test.csv")
    >>> print(normalized_data.head())

    Fruit	Weight	Amount
    0	Aplple	1	0.5
    1	Mr. Leslie Casey	0.32140	0.998905
    2	Anthony George	0.8998888	0.123784
    3	Brian Washington	0.121222	0.445321
    4	Elias Lawrence	0.345223	0

    """
    df = pd.read_csv(file_name)
    if df.select_dtypes(include='number').empty:
        raise ValueError("Input must at least have one numeric column.")
     
    scaler = MinMaxScaler()
    numeric_columns = df.select_dtypes(include='number').columns
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    return df

import unittest
import pandas as pd
import os


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):

    def test_case_0(self):
        # input without numeric columns\
        csv_path = os.path.join("f_675_data_simon", "test_non_numeric.csv")
        self.assertRaises(Exception, f_675, csv_path)
        csv_path = os.path.join("f_675_data_simon", "test_empty.csv")
        self.assertRaises(Exception, f_675, csv_path)

    def test_single_row(self):
        # input only one row
        csv_path = os.path.join("f_675_data_simon", "test_single.csv")
        df = f_675(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())

        expected = pd.DataFrame({
            'Name': ['Olivia Anderson'],
            'Age': [0.0],
            'Salary': [0.0]
        })

        pd.testing.assert_frame_equal(df, expected)

    def test_case_1(self):
        csv_path = os.path.join("f_675_data_simon", "test_data_0.csv")
        df = f_675(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())

        expected_path = os.path.join("f_675_data_simon", "test_res_0.csv")
        expected = pd.read_csv(expected_path, index_col=0)

        pd.testing.assert_frame_equal(df, expected)

    def test_case_2(self):
        csv_path = os.path.join("f_675_data_simon", "test_data_1.csv")
        df = f_675(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())

        expected_path = os.path.join("f_675_data_simon", "test_res_1.csv")
        expected = pd.read_csv(expected_path, index_col=0)

        pd.testing.assert_frame_equal(df, expected)

    def test_case_3(self):
        csv_path = os.path.join("f_675_data_simon", "test_data_2.csv")
        df = f_675(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())

        expected_path = os.path.join("f_675_data_simon", "test_res_2.csv")
        expected = pd.read_csv(expected_path, index_col=0)

        pd.testing.assert_frame_equal(df, expected)

    def test_case_4(self):
        csv_path = os.path.join("f_675_data_simon", "test_data_3.csv")
        df = f_675(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())

        expected_path = os.path.join("f_675_data_simon", "test_res_3.csv")
        expected = pd.read_csv(expected_path, index_col=0)

        pd.testing.assert_frame_equal(df, expected)

    def test_case_5(self):
        csv_path = os.path.join("f_675_data_simon", "test_data_4.csv")
        df = f_675(csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue((df['Age'] >= 0).all() and (df['Age'] <= 1).all())
        self.assertTrue((df['Salary'] >= 0).all() and (df['Salary'] <= 1).all())

        expected_path = os.path.join("f_675_data_simon", "test_res_4.csv")
        expected = pd.read_csv(expected_path, index_col=0)

        pd.testing.assert_frame_equal(df, expected)


if __name__ == "__main__":
    run_tests()