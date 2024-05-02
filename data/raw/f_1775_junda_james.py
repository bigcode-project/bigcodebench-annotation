import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt

def f_1775(df):
    """
    Impute missing values in the last column of the dataframe using mean imputation, then create a box plot to visualize the distribution of data in the last column.

    Parameters:
    df (DataFrame): The input dataframe.
    
    Returns:
    DataFrame: A pandas DataFrame with the imputed last column.
    Axes: A matplotlib Axes object with the boxplot of the last column of the dataframe.

    Raises:
    ValueError: If the input is not a DataFrame or has no columns.

    Requirements:
    - numpy
    - pandas
    - sklearn
    - seaborn
    - matplotlib.pyplot
    
    Example:
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
    >>> df.iloc[::3, -1] = np.nan  # Insert some NaN values
    >>> imputed_df, ax = f_1775(df)
    >>> ax.get_title()  # 'Boxplot of Last Column'
    'Boxplot of Last Column'
    >>> ax.get_xlabel() # 'D'
    'D'
    """
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty pandas DataFrame.")

    last_col = df.columns[-1]
    imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
    df[last_col] = imp_mean.fit_transform(df[last_col].values.reshape(-1, 1))

    fig, ax = plt.subplots()
    sns.boxplot(x=df[last_col], ax=ax)
    ax.set_title('Boxplot of Last Column')
    ax.set_xlabel(last_col)
    return df, ax

import unittest
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class TestCases(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
        self.df.iloc[::3, -1] = np.nan  # Insert some NaN values

    def test_return_types(self):
        imputed_df, ax = f_1775(self.df)
        self.assertIsInstance(imputed_df, pd.DataFrame)
        self.assertIsInstance(ax, plt.Axes)
        df_list = imputed_df.apply(lambda row: ','.join(row.values.astype(str)), axis=1).tolist()

        expect = ['51.0,92.0,14.0,55.666666666666664', '60.0,20.0,82.0,86.0', '74.0,74.0,87.0,99.0', '23.0,2.0,21.0,55.666666666666664', '1.0,87.0,29.0,37.0', '1.0,63.0,59.0,20.0', '32.0,75.0,57.0,55.666666666666664', '88.0,48.0,90.0,58.0', '41.0,91.0,59.0,79.0', '14.0,61.0,61.0,55.666666666666664', '61.0,50.0,54.0,63.0', '2.0,50.0,6.0,20.0', '72.0,38.0,17.0,55.666666666666664', '88.0,59.0,13.0,8.0', '89.0,52.0,1.0,83.0', '91.0,59.0,70.0,55.666666666666664', '7.0,46.0,34.0,77.0', '80.0,35.0,49.0,3.0', '1.0,5.0,53.0,55.666666666666664', '53.0,92.0,62.0,17.0', '89.0,43.0,33.0,73.0', '61.0,99.0,13.0,55.666666666666664', '47.0,14.0,71.0,77.0', '86.0,61.0,39.0,84.0', '79.0,81.0,52.0,55.666666666666664', '25.0,88.0,59.0,40.0', '28.0,14.0,44.0,64.0', '88.0,70.0,8.0,55.666666666666664', '0.0,7.0,87.0,62.0', '10.0,80.0,7.0,34.0', '34.0,32.0,4.0,55.666666666666664', '27.0,6.0,72.0,71.0', '11.0,33.0,32.0,47.0', '22.0,61.0,87.0,55.666666666666664', '98.0,43.0,85.0,90.0', '34.0,64.0,98.0,46.0', '77.0,2.0,0.0,55.666666666666664', '89.0,13.0,26.0,8.0', '78.0,14.0,89.0,41.0', '76.0,50.0,62.0,55.666666666666664', '51.0,95.0,3.0,93.0', '22.0,14.0,42.0,28.0', '35.0,12.0,31.0,55.666666666666664', '58.0,85.0,27.0,65.0', '41.0,44.0,61.0,56.0', '5.0,27.0,27.0,55.666666666666664', '83.0,29.0,61.0,74.0', '91.0,88.0,61.0,96.0', '0.0,26.0,61.0,55.666666666666664', '2.0,69.0,71.0,26.0', '8.0,61.0,36.0,96.0', '50.0,43.0,23.0,55.666666666666664', '58.0,31.0,95.0,87.0', '51.0,61.0,57.0,51.0', '11.0,38.0,1.0,55.666666666666664', '55.0,80.0,58.0,1.0', '1.0,91.0,53.0,86.0', '95.0,96.0,0.0,55.666666666666664', '1.0,52.0,43.0,89.0', '31.0,69.0,31.0,67.0', '54.0,74.0,55.0,55.666666666666664', '37.0,23.0,68.0,97.0', '69.0,85.0,10.0,15.0', '96.0,72.0,58.0,55.666666666666664', '79.0,92.0,2.0,19.0', '58.0,35.0,18.0,89.0', '66.0,18.0,19.0,55.666666666666664', '70.0,51.0,32.0,39.0', '38.0,81.0,0.0,10.0', '91.0,56.0,88.0,55.666666666666664', '22.0,30.0,93.0,41.0', '98.0,6.0,15.0,89.0', '59.0,1.0,0.0,55.666666666666664', '11.0,68.0,36.0,31.0', '8.0,98.0,18.0,47.0', '79.0,2.0,19.0,55.666666666666664', '53.0,32.0,23.0,74.0', '71.0,35.0,37.0,83.0', '98.0,88.0,98.0,55.666666666666664', '92.0,17.0,81.0,65.0', '53.0,34.0,79.0,60.0', '40.0,99.0,32.0,55.666666666666664', '32.0,13.0,20.0,47.0', '19.0,7.0,6.0,66.0', '16.0,32.0,47.0,55.666666666666664', '58.0,85.0,21.0,29.0', '37.0,50.0,53.0,7.0', '26.0,26.0,97.0,55.666666666666664', '29.0,96.0,27.0,63.0', '96.0,68.0,60.0,47.0', '18.0,3.0,34.0,55.666666666666664', '48.0,16.0,43.0,91.0', '29.0,92.0,45.0,5.0', '98.0,36.0,23.0,55.666666666666664', '45.0,52.0,94.0,98.0', '59.0,96.0,62.0,84.0', '31.0,86.0,32.0,55.666666666666664', '17.0,24.0,94.0,53.0', '57.0,66.0,45.0,23.0', '31.0,46.0,85.0,55.666666666666664']
        self.assertEqual(df_list, expect, "DataFrame contents should match the expected output")

    def test_imputation(self):
        imputed_df, _ = f_1775(self.df)
        self.assertFalse(imputed_df.isna().any().any())

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            f_1775("not a dataframe")

    def test_empty_dataframe(self):
        with self.assertRaises(ValueError):
            f_1775(pd.DataFrame())

    def test_plot_title_and_labels(self):
        _, ax = f_1775(self.df)
        self.assertEqual(ax.get_title(), 'Boxplot of Last Column')
        self.assertEqual(ax.get_xlabel(), 'D')

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