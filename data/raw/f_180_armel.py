import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def f_180(db_path: str) -> pd.DataFrame:
    '''
    Fetch and plot the monthly sales from an SQLite database. The name of the table of interest is 'sales' and it has two columns 'sale_date' and 'amount'.

    Args:
    - db_path (str): Path to the SQLite database file.

    Returns:
    pd.DataFrame: A pandas DataFrame with the monthly sales data.

    Requirements:
    - sqlite3
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df = f_180('sales.db')
    >>> print(df)
    >>> df.plot(kind='bar', x='month', y='total_sales', title='Monthly Sales')

    Note:
    Ensure the database table structure contains 'sale_date' and 'amount' columns for correct functionality.
    '''
    conn = sqlite3.connect(db_path)
    query = "SELECT strftime('%Y-%m', sale_date) as month, SUM(amount) as total_sales FROM sales GROUP BY month"
    df = pd.read_sql_query(query, conn)
    print(f"yo = {df}")
    conn.close()
    
    # Plotting the sales data
    df.plot(kind='bar', x='month', y='total_sales', title='Monthly Sales', figsize=(10, 6))
    plt.ylabel('Total Sales')
    plt.xlabel('Month')
    plt.show()
    
    return df

from pathlib import Path
import unittest
import os

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
class TestCases(unittest.TestCase):
    """Test cases for the f_180 function."""
    def setUp(self):
        self.test_dir = "data/f_180"
        os.makedirs(self.test_dir, exist_ok=True)

        self.db_1 = os.path.join(self.test_dir, "db_1.db")
        if not os.path.exists(self.db_1) :
            Path(self.db_1).touch()
            conn = sqlite3.connect(self.db_1)
            c = conn.cursor()
            c.execute('''CREATE TABLE sales (sale_date date, amount float)''')
            df = pd.DataFrame(
                {
                    "sale_date" : ["2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01"],
                    "amount" : [301.0, 400.0, 400.5, 360.5]
                }
            )
            df.to_sql('sales', conn, if_exists='append', index = False)

        self.db_2 = os.path.join(self.test_dir, "db_2.db")
        if not os.path.exists(self.db_2) :
            Path(self.db_2).touch()
            conn = sqlite3.connect(self.db_2)
            c = conn.cursor()
            c.execute('''CREATE TABLE sales (sale_date date, amount float)''')
            df = pd.DataFrame(
                {
                    "sale_date" : ["2024-01-01", "2024-02-01", "2024-01-02", "2024-03-01", "2024-02-02"],
                    "amount" : [13, 11, 117, 56, 29]
                }
            )
            df.to_sql('sales', conn, if_exists='append', index = False)
    
    def test_case_1(self):
        df = f_180(self.db_1)

        # Check the DataFrame structure
        self.assertTrue('month' in df.columns)
        self.assertTrue('total_sales' in df.columns)
        
        # Check the monthly sales data
        expected_data = {
            "2023-01": 301.0,
            "2023-02": 400.0,
            "2023-03": 400.5,
            "2023-04": 360.5
        }
        for month, total_sales in expected_data.items():
            self.assertAlmostEqual(df[df['month'] == month]['total_sales'].values[0], total_sales, delta=0.01)
    
    def test_case_2(self):
        df = f_180(self.db_2)

        # Check the DataFrame structure
        self.assertTrue('month' in df.columns)
        self.assertTrue('total_sales' in df.columns)
        
        # Check the monthly sales data
        expected_data = {
            "2024-01": 130.0,
            "2024-02": 40.0,
            "2024-03": 56.0
        }
        for month, total_sales in expected_data.items():
            self.assertAlmostEqual(df[df['month'] == month]['total_sales'].values[0], total_sales, delta=0.01)

if __name__ == "__main__" :
    run_tests()