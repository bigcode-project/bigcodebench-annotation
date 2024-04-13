import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['email', 'list']

def f_151(api_url):
    """
    Download email data from a RESTful API, convert it into a Pandas DataFrame, 
    calculate the sum, mean, and standard deviation of a numeric list associated with each email, 
    and then draw a histogram (with 10 bins) of the standard deviations.

    The expected format of the email data is a list of dictionaries, where each dictionary has:
    - 'email': an email address (string)
    - 'list': a list of numeric values (list of numbers)

    The dataframe columns should include 'sum', 'mean' and 'std' which represent each opearation applied to the numeric list associated to each email.
    
    Parameters:
    api_url (str): The URL of the RESTful API.

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame with email data and calculated metrics, or None if there's an error.
        - Axes: A matplotlib axes containing the histogram of standard deviations, or None if there's no data or an error.

    Requirements:
    - pandas
    - requests
    - numpy
    - matplotlib.pyplot

    Example:
    >>> df, ax = f_151('https://api.example.com/email_data')
    >>> print(df)
    >>> plt.show()
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        email_data = response.json()

        df = pd.DataFrame(email_data, columns=COLUMNS)
        if df.empty:
            return df, None

        df['sum'] = df['list'].apply(np.sum)
        df['mean'] = df['list'].apply(np.mean)
        df['std'] = df['list'].apply(np.std)

        ax = df['std'].hist(bins=10)  # Adjusting bin count for better representation
    
        return df, ax

    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None, None

import unittest
from unittest.mock import patch

class A :
    def __init__(self, data, status_code=200) -> None:
        self.data = data
        self.status_code = status_code
    
    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.RequestException("An error occured")
    
    def json(self):
        return self.data

class TestCases(unittest.TestCase):
    """Test cases for the f_151 function."""
    @patch('requests.get')
    def test_case_1(self, mock_get):
        data = {
            "email" : ["first@example.com", "second@example.com"],
            "list" : [
                [1, 2],
                [3, 4]
            ]
        }
        mock_get.return_value = A(data)
        df, ax = f_151('https://api.example.com/email_data')
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass  
        self.assertTrue(len(df) == 2)
        self.assertTrue(len(ax.patches) == 10)

    @patch('requests.get')
    def test_case_2(self, mock_get):
        mock_get.return_value = A({}, status_code=404)
        df, ax = f_151('https://api.invalid.com/data')
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass 
        self.assertIsNone(df)
        self.assertIsNone(ax)

    @patch('requests.get')
    def test_case_3(self, mock_get):
        data = {
            "email" : [],
            "list" : []
        }
        mock_get.return_value = A(data)
        df, ax = f_151('https://api.example.com/empty_data')
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass 
        self.assertTrue(len(df) == 0)
        self.assertIsNone(ax)
        
    @patch('requests.get')
    def test_case_4(self, mock_get):
        data = {
            "email" : ["third@example.com", "fourth@example.com", "fifth@example.com"],
            "list" : [
                [5, 6, 7],
                [8, 9, 10],
                [11, 12, 13]
            ]
        }
        mock_get.return_value = A(data)
        df, ax = f_151('https://api.different.com/data')
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass 
        self.assertTrue(len(df) == 3)
        self.assertTrue(len(ax.patches) > 0)
        
    @patch('requests.get')
    def test_case_5(self, mock_get):
        data = {
            "email" : ["seventh@example.com", "eighth@example.com", "ninth@example.com", "tenth@example.com"],
            "list" : [
                [14],
                [15, 16],
                [17, 18, 19],
                [20, 21, 22, 23]
            ]
        }
        mock_get.return_value = A(data)
        df, ax = f_151('https://api.another.com/data')
        try:
            fig = ax.get_figure()
            plt.close(fig)
        except:
            pass 
        self.assertTrue(len(df) == 4)
        self.assertTrue(len(ax.patches) > 0)
        self.assertEqual(df.loc[0, 'mean'], 14.0)
        self.assertEqual(df.loc[1, 'mean'], 15.5)
        self.assertEqual(df.loc[2, 'mean'], 18.0)
        self.assertEqual(df.loc[3, 'mean'], 21.5)
        self.assertEqual(df.loc[0, 'sum'], 14)
        self.assertEqual(df.loc[1, 'sum'], 31)
        self.assertEqual(df.loc[2, 'sum'], 54)
        self.assertEqual(df.loc[3, 'sum'], 86)
        self.assertEqual(df.loc[1, 'std'], 0.5)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests() 