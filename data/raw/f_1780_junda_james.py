import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def f_1780(df, cols):
    """
    Standardize specified numeric columns in a dataframe.

    Parameters:
    df (DataFrame): The dataframe.
    cols (list): The columns to standardize.

    Returns:
    DataFrame: The dataframe with standardized columns.

    Raises:
    ValueError: If 'df' is not a DataFrame, 'cols' is not a list, or columns in 'cols' don't exist in 'df'.

    Requirements:
    - pandas
    - numpy
    - sklearn.preprocessing.StandardScaler

    Example:
    >>> np.random.seed(0)
    >>> df = pd.DataFrame({'A': np.random.normal(0, 1, 1000), 'B': np.random.exponential(1, 1000)})
    >>> df = f_1780(df, ['A', 'B'])
    >>> print(df.describe())
                      A             B
    count  1.000000e+03  1.000000e+03
    mean  -1.243450e-17 -1.865175e-16
    std    1.000500e+00  1.000500e+00
    min   -3.040310e+00 -1.024196e+00
    25%   -6.617441e-01 -7.183075e-01
    50%   -1.293911e-02 -2.894497e-01
    75%    6.607755e-01  4.095312e-01
    max    2.841457e+00  5.353738e+00
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df must be a pandas DataFrame.")
    if not isinstance(cols, list) or not all(isinstance(col, str) for col in cols):
        raise ValueError("cols must be a list of column names.")
    if not all(col in df.columns for col in cols):
        raise ValueError("All columns in cols must exist in the dataframe.")

    scaler = StandardScaler()
    df[cols] = scaler.fit_transform(df[cols])

    return df

import unittest
import numpy as np
import pandas as pd 

class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(0)
        self.df = pd.DataFrame({
            'A': np.random.normal(0, 1, 1000), 
            'B': np.random.exponential(1, 1000), 
            'C': np.random.randint(0, 100, 1000)
        })

    def test_standardized_columns(self):
        standardized_df = f_1780(self.df, ['A', 'B'])
        self.assertAlmostEqual(standardized_df['A'].mean(), 0, places=1)
        self.assertAlmostEqual(standardized_df['A'].std(), 1, places=1)
        self.assertAlmostEqual(standardized_df['B'].mean(), 0, places=1)
        self.assertAlmostEqual(standardized_df['B'].std(), 1, places=1)
        df_list = standardized_df.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()
        with open('df_contents.txt', 'w') as file:
            file.write(str(df_list))

    def test_invalid_input_dataframe(self):
        with self.assertRaises(ValueError):
            f_1780("not a dataframe", ['A', 'B'])

    def test_invalid_input_cols(self):
        with self.assertRaises(ValueError):
            f_1780(self.df, 'A')

    def test_nonexistent_column(self):
        with self.assertRaises(ValueError):
            f_1780(self.df, ['A', 'NonexistentColumn'])

    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_1780(pd.DataFrame(), ['A', 'B'])

    # Additional test cases as needed...
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