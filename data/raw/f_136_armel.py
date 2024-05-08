import pandas as pd

def f_136(state_dict: dict) -> pd.DataFrame:
    """
    Create a pandas DataFrame from a given dictionary of states and their populations. Filter out the states that lie within one standard deviation of the mean population.

    Parameters:
    - state_dict (dict): Dictionary with states as keys and their populations as values.

    Returns:
    - DataFrame: A pandas DataFrame with two columns: 'State' and 'Population'.

    Requirements:
    - pandas

    Example:
    >>> state_dict = {'California': 39538223, 'Texas': 29145505, 'New York': 20201249, 'Florida': 21538187, 'Illinois': 12812508}
    >>> df = f_136(state_dict)
    >>> print(df)
           State  Population
    0  California    39538223
    1       Texas    29145505
    2    New York    20201249
    3     Florida    21538187
    4    Illinois    12812508
    """
    state_data = list(state_dict.items())
    df = pd.DataFrame(state_data, columns=['State', 'Population'])
    return df

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_136 function."""
    def test_case_1(self):
        state_dict = {
            'California': 39538223,
            'Texas': 29145505,
            'New York': 20201249,
            'Florida': 21538187,
            'Illinois': 12812508
        }
        df = f_136(state_dict)
        expected_output = pd.DataFrame({
            'State': ['California', 'Texas', 'New York', 'Florida', 'Illinois'],
            'Population': [39538223, 29145505, 20201249, 21538187, 12812508]
        })
        pd.testing.assert_frame_equal(df, expected_output)

    def test_case_2(self):
        state_dict = {'California': 39538223}
        df = f_136(state_dict)
        expected_output = pd.DataFrame({
            'State': ['California'],
            'Population': [39538223]
        })
        pd.testing.assert_frame_equal(df, expected_output)

    def test_case_3(self):
        state_dict = {}
        df = f_136(state_dict)
        expected_output = pd.DataFrame({
            'State': pd.Series([], dtype='object'),
            'Population': pd.Series([], dtype='object')
        }, index=pd.Index([], dtype='object'))
        pd.testing.assert_frame_equal(df, expected_output)

    def test_case_4(self):
        state_dict = {'California': 39538223}
        df = f_136(state_dict)
        expected_output = pd.DataFrame({
            'State': ['California'],
            'Population': [39538223]
        })
        pd.testing.assert_frame_equal(df, expected_output)

    def test_case_5(self):
        state_dict = {'California': 39538223}
        df = f_136(state_dict)
        expected_output = pd.DataFrame({
            'State': ['California'],
            'Population': [39538223]
        })
        pd.testing.assert_frame_equal(df, expected_output)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()