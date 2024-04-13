import pandas as pd

def f_137(country_dict):
    """
    Create a DataFrame from a dictionary of countries as keys and their populations as values.
    
    Parameters:
    country_dict (dict): The dictionary with countries as keys and their populations as values.
    
    Returns:
    DataFrame: A pandas DataFrame with countries and their populations.
    
    Requirements:
    - pandas
    
    Example:
    >>> country_dict = {'China': 1444216107, 'India': 1393409038, 'USA': 332915073, 'Indonesia': 276361783, 'Pakistan': 225199937}
    >>> df = f_137(country_dict)
    >>> print(df)
               Country  Population
    0            China  1444216107
    1            India  1393409038
    2              USA   332915073
    3        Indonesia   276361783
    4         Pakistan   225199937
    """
    country_data = list(country_dict.items())
    df = pd.DataFrame(country_data, columns=['Country', 'Population'])
    return df

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_137 function."""
    def test_case_1(self):
        # Testing the function with the given example
        country_dict = {'China': 1444216107, 'India': 1393409038, 'USA': 332915073, 'Indonesia': 276361783, 'Pakistan': 225199937}
        df = f_137(country_dict)
        
        # Asserting the shape and values of the DataFrame
        self.assertEqual(df.shape, (5, 2))
        self.assertEqual(df['Country'].tolist(), ['China', 'India', 'USA', 'Indonesia', 'Pakistan'])
        self.assertEqual(df['Population'].tolist(), [1444216107, 1393409038, 332915073, 276361783, 225199937])
    
    def test_case_2(self):
        # Testing the function with an empty dictionary
        country_dict = {}
        df = f_137(country_dict)
        
        # Asserting the shape and values of the DataFrame
        self.assertEqual(df.shape, (0, 2))
        self.assertEqual(df['Country'].tolist(), [])
        self.assertEqual(df['Population'].tolist(), [])

    def test_case_3(self):
        # Testing the function with a dictionary having only one country
        country_dict = {'Australia': 25649909}
        df = f_137(country_dict)
        
        # Asserting the shape and values of the DataFrame
        self.assertEqual(df.shape, (1, 2))
        self.assertEqual(df['Country'].tolist(), ['Australia'])
        self.assertEqual(df['Population'].tolist(), [25649909])

    def test_case_4(self):
        # Testing the function with a dictionary having only one country
        country_dict = {'Australia': 25649909}
        df = f_137(country_dict)
        
        # Asserting the shape and values of the DataFrame
        self.assertEqual(df.shape, (1, 2))
        self.assertEqual(df['Country'].tolist(), ['Australia'])
        self.assertEqual(df['Population'].tolist(), [25649909])

    def test_case_5(self):
        # Testing the function with a dictionary having only one country
        country_dict = {'Australia': 25649909}
        df = f_137(country_dict)
        
        # Asserting the shape and values of the DataFrame
        self.assertEqual(df.shape, (1, 2))
        self.assertEqual(df['Country'].tolist(), ['Australia'])
        self.assertEqual(df['Population'].tolist(), [25649909])

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests() 