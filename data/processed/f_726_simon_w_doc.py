import pandas as pd
from scipy.stats import chi2_contingency

def f_748(df, columns=['A', 'B', 'C'], larger=50, equal=900):
    """
    Filters a pandas DataFrame based on the values of specific rows, and performs
    a chi-square independence test on the first two columns.

    The function filters rows based on the following criteria:
        Keep only rows where:
            The value of the second column: df['second'] > larger
            and
            The value of the third column: df['third'] == equal
    
    After filtering a conigency table of the first two columns is computed,
    which is then used in the chi2 independence test. The p_value of the test
    is returned.        

    Parameters:
    df (pd.DataFrame): A DataFrame containing at least the columns specified in the 'columns' parameter.
    columns (list): A list of column names to consider for the operation, defaulting to ['A', 'B', 'C'].
                    The first column should contain categorical data, the second numerical data (used for filtering with values > 'larger'),
                    and the third numerical data (used for filtering with a fixed value of 'equal').
    larger (float, optional): Used for filtering rows against the second column where values > 'larger'.
                              Defaults to 50.
    equal (float, optional): Used for filtering rows against the third column where values == equal.
                             Defaults to 900.

    Returns:
    float: The p-value from the chi-square independence test, indicating the statistical significance.
           
    Raises:
    ValueError: If there's insufficient data for the test (no rows meeting the criteria).
    ValueError: If the number of specified columns is not 3.
    ValueError: If the specified columns are not contained in df.
    

    Requirements:
    - pandas
    - scipy.stats

    Example:
    >>> df = pd.DataFrame({
    ...     'A': ['Yes', 'No', 'Yes', 'No'],
    ...     'B': [55, 70, 40, 85],
    ...     'C': [900, 900, 800, 900]
    ... })
    >>> f_748(df)
    0.22313016014842973

    >>> df = pd.DataFrame({
    ...     'test': ['A', 'b', 'b', 'a', 'c', 'd'],
    ...     'hi': [45, 2, 2, 3, 4, 4],
    ...     'column3': [50, 50, 50, 50, 50, 50, ]
    ... })
    >>> f_748(df, ['test', 'hi', 'column3'], larger=2, equal=50)
    0.23810330555354436
    """
    if len(columns) != 3:
        raise ValueError("Exactly three columns should be specified.")
    for column in columns:
        if column not in df.columns:
            raise ValueError('The specified columns should exist in the DataFrame.')
    col_categorical, col_numerical, col_filter = columns
    selected = df[(df[col_numerical] > larger) & (df[col_filter] == equal)][[col_categorical, col_numerical]]
    contingency_table = pd.crosstab(selected[col_categorical], selected[col_numerical])
    if contingency_table.size == 0:
        raise ValueError("Insufficient data - no matching data for the applied conditions.")
    _, p_value, _, _ = chi2_contingency(contingency_table)
    return p_value

import unittest
import pandas as pd
import faker
class TestCases(unittest.TestCase):
    def test_column_not_in_df(self):
        fake = faker.Faker()
        fake.seed_instance(42)
        rows = 10
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [81 for i in range(rows)],
                'D': [900 for i in range(rows)] 
            }
        )
        self.assertRaises(Exception, f_748, data)
    def test_column_number(self):
        fake = faker.Faker()
        fake.seed_instance(42)
        rows = 10
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [81 for i in range(rows)],
                'C': [900 for i in range(rows)] 
            }
        )
        self.assertRaises(Exception, f_748, data, ['A'])
        self.assertRaises(Exception, f_748, data, ['A', 'B', 'C', 'D'])
    def test_no_data_after_filer(self):
        fake = faker.Faker()
        fake.seed_instance(42)
        rows = 10
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [20 for i in range(rows)],
                'C': [901 for i in range(rows)] 
            }
        )
        self.assertRaises(Exception, f_748, data)
    def test_medium_dataframe(self):
        # Test with a medium-sized dataframe (50 rows)
        fake = faker.Faker()
        fake.seed_instance(12)
        rows = 50
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [fake.random_int(0, 100) for i in range(rows)],
                'C': [fake.random_int(899, 901) for i in range(rows)] 
            }
        )        
        p_value = f_748(data)
        self.assertAlmostEqual(p_value, 0.23, places=1)
    def test_large_dataframe(self):
        # Test with a large dataframe (1000 rows)
        fake = faker.Faker()
        fake.seed_instance(21)
        rows = 1000
        data = pd.DataFrame(
            {
                'A': [fake.name() for i in range(rows)],
                'B': [fake.random_int(0, 100) for i in range(rows)],
                'C': [fake.random_int(800, 950) for i in range(rows)] 
            }
        )        
        p_value = f_748(data)
        self.assertAlmostEqual(p_value, 0.22, places=1)
    def test_very_large_dataframe(self):
        data = pd.DataFrame(
            {
                'A': ['a', 'a', 'a', 'a', 'a'],
                'B': [70, 70, 70, 70, 70],
                'C': [900, 900, 900, 900, 900] 
            }
        )
        p_value = f_748(data)
        self.assertAlmostEqual(p_value, 1.0, places=1)
    def test_huge_dataframe(self):
        # different column names
        fake = faker.Faker()
        fake.seed_instance(21)
        rows = 1000
        data = pd.DataFrame(
            {
                'test': [fake.name() for i in range(rows)],
                'five': [fake.random_int(21, 150) for i in range(rows)],
                '1': [fake.random_int(821, 950) for i in range(rows)] 
            }
        )        
        p_value = f_748(data, columns=['test', 'five', '1'])
        self.assertAlmostEqual(p_value, 0.22, places=1)
    def test_diff_filter(self):
        # different filter values
        fake = faker.Faker()
        fake.seed_instance(21)
        rows = 1000
        data = pd.DataFrame(
            {
                'test': [fake.name() for i in range(rows)],
                'five': [fake.random_int(21, 150) for i in range(rows)],
                '1': [fake.random_int(19, 21) for i in range(rows)] 
            }
        )        
        p_value = f_748(data, columns=['test', 'five', '1'], larger=100, equal=20)
        self.assertAlmostEqual(p_value, 0.35, places=1)
