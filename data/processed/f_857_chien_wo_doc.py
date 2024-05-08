import requests
import pandas as pd


def f_878(api_url):
    """
    Fetches data from a specified API, processes the JSON response, converts it into a pandas DataFrame,
    and plots the data using matplotlib.
    If the data is empty, no plot is generated. If the API request fails, it raises an HTTPError.
    The function also checks if the provided API URL is a string.

    Parameters:
    - api_url (str): The URL of the API to fetch data from.

    Returns:
    - DataFrame: A pandas DataFrame with the parsed data from the API.
    - Axes or None: A matplotlib Axes object representing the plot of the data, or None if the data is empty.

    Raises:
    - HTTPError: If the API request fails due to issues like network problems, invalid response, etc.
    - TypeError: If the `api_url` is not a string.

    Requirements:
    - requests
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df, plot = f_878("https://api.example.com/data")
    >>> df.head()
    >>> if plot:
    >>>     plot.show()
    """
    if not isinstance(api_url, str):
        raise TypeError("api_url must be a string")
    response = requests.get(api_url, timeout=5)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)
    plot = df.plot() if not df.empty else None
    return df, plot

import unittest
from unittest.mock import patch, Mock
import pandas as pd
import matplotlib.pyplot as plt
API_URL = "https://api.example.com/data"
class TestCases(unittest.TestCase):
    """Test cases for the function."""
    @patch("requests.get")
    def test_successful_api_call_with_data(self, mock_get):
        """Test the function with a successful API call returning non-empty data."""
        mock_get.return_value = Mock(status_code=200, json=lambda: [{"a": 1, "b": 2}])
        df, plot = f_878("http://example.com/api")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIsInstance(plot, plt.Axes)
    @patch("requests.get")
    def test_successful_api_call_with_empty_data(self, mock_get):
        """Test the function with a successful API call returning empty data."""
        mock_get.return_value = Mock(status_code=200, json=lambda: [])
        df, plot = f_878("http://example.com/api")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.empty)
        self.assertIsNone(plot)
    @patch("requests.get")
    def test_api_call_with_invalid_json(self, mock_get):
        """Test the function with an API call returning invalid JSON."""
        mock_get.return_value = Mock(
            status_code=200, json=lambda: Exception("Invalid JSON")
        )
        with self.assertRaises(Exception):
            f_878("http://example.com/api")
    @patch("requests.get")
    def test_api_call_with_http_error(self, mock_get):
        """Test the function with an API call that raises an HTTP error."""
        mock_get.side_effect = requests.HTTPError()
        with self.assertRaises(requests.HTTPError):
            f_878("http://example.com/api")
    def test_incorrect_url_type(self):
        """Test the function with an incorrect type for the URL."""
        with self.assertRaises(TypeError):
            f_878(123)
    def tearDown(self):
        plt.close()
