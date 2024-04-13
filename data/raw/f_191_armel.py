import os
import pandas as pd
import matplotlib.pyplot as plt

def f_191(data_path, filename, column_name):
    """
    Draws a histogram of a specific column in a CSV file and returns the plot.

    Parameters:
    - filename (str): The name of the csv file.
    - data_path (str) : The path to the directory where the csv file is stored.
    - column_name (str): The name of the column to plot.

    Returns:
    - matplotlib.axes.Axes: The Axes object representing the histogram. The plot title should be the column name.

    Requirements:
    - os
    - pandas
    - matplotlib.pyplot

    Example:
    >>> ax = f_191('./data/f_191/', 'csv_1.csv', 'Age')
    """
    df = pd.read_csv(os.path.join(data_path, filename))
    ax = df[column_name].hist()
    ax.set_title(column_name)
    return ax
    
import unittest
import pandas as pd

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    """Test cases for the f_191 function.""" 
    def setUp(self) -> None:
        self.test_dir = "data/f_191"
        os.makedirs(self.test_dir, exist_ok=True)
        with open(os.path.join(self.test_dir, "csv_1.csv"), "w") as f :
           f.write("Age\n10\n11\n45\n77\n32\n22\89\n13\n7\n6\n19\n37\n20\n56")
        with open(os.path.join(self.test_dir, "csv_2.csv"), "w") as f :
           f.write("Salary\n40000\n37000\n120000\n140000\n90000\n33000\n54000\n70000\n60000\n24000")
        with open(os.path.join(self.test_dir, "csv_3.csv"), "w") as f :
           f.write("Height\n180\n181\n170\n163\n140\n145\n190\n189\n177")
        with open(os.path.join(self.test_dir, "csv_3.csv"), "w") as f :
           f.write("Minutes\n1\n2\n3\n4\n5\n6\n7\n8\n9")
        with open(os.path.join(self.test_dir, "csv_3.csv"), "w") as f :
           f.write("")
    
    def test_case_1(self):
        ax = f_191(self.test_dir, 'csv_1.csv', 'Age')
        self.assertEqual(ax.get_title(), 'Age')

    def test_case_2(self):
        ax = f_191(self.test_dir, 'csv_2.csv', 'Salary')
        self.assertEqual(ax.get_title(), 'Salary')

    def test_case_3(self):
        with self.assertRaises(FileNotFoundError):
            f_191(self.test_dir, "csv.csv", 'age')

    def test_case_4(self):
        with self.assertRaises(KeyError):
            f_191(self.test_dir, 'csv_4.csv', 'nonexistent_column')

    def test_case_5(self):
        with self.assertRaises(pd.errors.EmptyDataError):
            f_191(self.test_dir, 'csv_5.csv', 'Age')


if __name__ == "__main__":
    run_tests()