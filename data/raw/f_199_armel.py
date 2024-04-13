import pandas as pd
import matplotlib.pyplot as plt
from random import randint

def f_199(list_of_pairs):
    """
    Create a Pandas DataFrame from a list of pairs and visualize the data using a bar chart.
    
    Parameters:
    list_of_pairs (list): A list of pairs, where the first element is the category and 
                          the second element is the value.
    
    Returns:
    - pandas.DataFrame : A pandas dataframe containing the following columns :
        - Category (str): The first value of the tuples in the list of pairs.
        - Value (int): The second value of the tuples in the list of pairs. Replace negative values by a random integer between 0 and 10 both included.
    - matplotlib.axes._axes.Axes : A barplot representing each category and the corresponding value. 
                                   The x-axis should be labeled 'Category', the y-axis 'Value', and the 
                                   title of the plot should be 'Category vs Value'.
    
    Requirements:
    - pandas
    - matplotlib.pyplot
    - random
    
    Notes:
    - Negative values in the list are replaced with random values between 0 and 10.
    
    Example:
    >>> list_of_pairs = [('Fruits', 5), ('Vegetables', 9), ('Dairy', -1), ('Bakery', -2), ('Meat', 4)]
    >>> df, ax = f_199(list_of_pairs)
    >>> print(df)
    >>> plt.show()  # To display the plot
    """
    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])
    df['Value'] = df['Value'].apply(lambda x: x if x > 0 else randint(0, 10))
    ax = df.plot(kind='bar', x='Category', y='Value', legend=False)
    ax.set_title('Category vs Value')
    ax.set_xlabel('Category')
    ax.set_ylabel('Value')
    return df, ax

import unittest
from faker import Faker
fake = Faker()
Faker.seed(0)
class TestCases(unittest.TestCase):
    """Test cases for the f_199 function."""
    def test_case_1(self):
        """
        Test normal operation with valid input
        """
        data = [('Fruits', 5), ('Vegetables', 9), ('Dairy', 7), ('Bakery', 3), ('Meat', 4)]
        df, ax = f_199(data)
        values = df.values
        self.assertEqual(df.shape[-1], 2)
        self.assertDictEqual(
            {
                df.columns[0] : [t[0] for t in values],
                df.columns[1] : [t[1] for t in values],
            },
            {
                "Category" : ["Fruits", "Vegetables", "Dairy", "Bakery", "Meat"],
                "Value" : [5, 9, 7, 3, 4]
            }
        )
        self.assertEqual(len(df), 5)
        self.assertTrue(all(df['Value'] >= 0))
        self.assertEqual(ax.get_xlabel(), 'Category')
        self.assertEqual(ax.get_ylabel(), 'Value')
        self.assertEqual(ax.get_title(), 'Category vs Value')

    def test_case_2(self):
        """
        Test right length and non negative Value
        """
        data = [(fake.unique.first_name(), fake.random_int(min=-10, max=-1)) for _ in range(5)]
        df, ax = f_199(data)
        self.assertTrue(all(df['Value'] >= 0))
        self.assertEqual(ax.get_title(), 'Category vs Value')

    def test_case_3(self):
        """
        Test non negative and maximum <= 10
        """
        data = [(fake.unique.first_name(), fake.random_int(min=-100, max=-10)) for _ in range(5)]
        df, ax = f_199(data)
        self.assertTrue(all(df['Value'] >= 0))
        self.assertTrue(all(df['Value'] <= 10))
        self.assertEqual(ax.get_title(), 'Category vs Value')

    def test_case_4(self):
        """
        Test right length and non negative Value
        """
        data = [(fake.unique.first_name(), fake.random_int(min=-10, max=10)) for _ in range(10)]
        df, ax = f_199(data)
        self.assertEqual(len(df), 10)
        self.assertTrue(all(df['Value'] >= 0))
        self.assertEqual(ax.get_title(), 'Category vs Value')

    def test_case_5(self):
        """
        Test right length and non negative Value
        """
        data = [(fake.first_name(), fake.random_int(min=-10, max=10)) for _ in range(5)]
        data.extend(data)
        df, ax = f_199(data)
        self.assertEqual(len(df), 10)
        self.assertTrue(all(df['Value'] >= 0))
        self.assertEqual(ax.get_title(), 'Category vs Value')

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()