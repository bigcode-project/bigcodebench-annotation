import pandas as pd
from sklearn.preprocessing import StandardScaler

def f_647(df, age, weight):
    """
    Filters and standardizes a given DataFrame based on specified age and weight criteria.

    This function first filters the rows in the input DataFrame where 'Age' is less than the 
    specified 'age' and 'Weight' is greater than the specified 'weight'. It then standardizes 
    the numerical values in the filtered DataFrame using the StandardScaler from sklearn.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing at least the columns 'Age' and 'Weight'.
    age (numeric): The age threshold for filtering rows. Rows with 'Age' less than this value 
                   are selected.
    weight (numeric): The weight threshold for filtering rows. Rows with 'Weight' greater than 
                      this value are selected.

    Returns:
    pd.DataFrame: A DataFrame containing the filtered and standardized data. If the filtering 
                  results in an empty DataFrame, an empty DataFrame is returned.
    
    Raises:
    KeyError: If the input DataFrame does not contain the required columns 'Age' and 'Weight'.
    """
    selected_df = df[(df['Age'] < age) & (df['Weight'] > weight)]
    
    # Check if the selected DataFrame is empty
    if selected_df.empty:
        return selected_df

    # Standardizing the selected data
    scaler = StandardScaler()
    selected_df = pd.DataFrame(scaler.fit_transform(selected_df), columns=selected_df.columns)

    return selected_df


import unittest
import pandas as pd

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def setUp(self):
        # This method will run before each test
        self.data = {
            "Age": [25, 35, 45, 20, 55, 30],
            "Weight": [60, 80, 75, 85, 65, 90],
            "Other_Column": [1, 2, 3, 4, 5, 6]  # Some additional data
        }
        self.df = pd.DataFrame(self.data)

    def test_standard_usage(self):
        result_df = f_647(self.df, 70, 1)
        self.assertFalse(result_df.empty)
        self.assertEqual(result_df.shape[1], self.df.shape[1])
        self.assertTrue((result_df.columns == self.df.columns).all())
        expected = pd.DataFrame(
            {'Age': {0: -0.8401680504168059, 1: 0.0, 2: 0.8401680504168059, 3: -1.260252075625209, 4: 1.6803361008336117, 5: -0.42008402520840293}, 'Weight': {0: -1.497409771854291, 1: 0.3940552031195508, 2: -0.07881104062390962, 3: 0.8669214468630112, 4: -1.0245435281108304, 5: 1.3397876906064716}, 'Other_Column': {0: -1.4638501094227998, 1: -0.8783100656536799, 2: -0.29277002188455997, 3: 0.29277002188455997, 4: 0.8783100656536799, 5: 1.4638501094227998}}
        )
        pd.testing.assert_frame_equal(result_df, expected, atol=1e-2)

    def test_empty_dataframe(self):
        empty_df = pd.DataFrame()
        self.assertRaises(Exception, f_647, empty_df, 30, 70)

    def test_no_rows_meet_criteria(self):
        result_df = f_647(self.df, 15, 95)
        self.assertTrue(result_df.empty)

    def test_missing_columns(self):
        with self.assertRaises(KeyError):
            incomplete_df = self.df.drop(columns=["Age"])
            f_647(incomplete_df, 30, 70)

    def test_non_numeric_values(self):
        self.df['Age'] = self.df['Age'].astype(str)  # Converting Age to string
        with self.assertRaises(Exception):  # Assuming ValueError is raised for non-numeric inputs
            f_647(self.df, 30, 70)
            
if __name__ == "__main__":
    run_tests()