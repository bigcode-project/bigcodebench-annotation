import pandas as pd
import requests
from io import StringIO

def task_func(csv_url, sort_by_column="title"):
    """
    Fetches data from a given CSV URL and returns a pandas DataFrame sorted based on the specified column.

    Parameters:
    - csv_url (str): The URL to fetch the CSV data from.
    - sort_by_column (str): The column name based on which the data needs to be sorted. Default is "title".

    Returns:
    DataFrame: The pandas DataFrame that sorted based on the specified column.

    Requirements:
    - pandas
    - requests
    - io.StringIO

    Raises:
    Exception: If the response status code is not 200.

    Example:
    >>> task_func("http://example.com/data.csv", sort_by_column="title")
       id   title  price
    0   1   Apple    0.3
    1   2  Banana    0.5
    2   3  Cherry    0.2

    >>> task_func("http://example.com/data.csv", sort_by_column="price")
       id   title  price
    2   3  Cherry    0.2
    0   1   Apple    0.3
    1   2  Banana    0.5
    
    """

    response = requests.get(csv_url)
    response.raise_for_status()  # Raise an exception for invalid responses
    csv_data = response.text
    df = pd.read_csv(StringIO(csv_data))
    sorted_df = df.sort_values(by=sort_by_column)
    return sorted_df

import unittest
from unittest.mock import patch
from io import StringIO
import pandas as pd
import requests
class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_case_1(self, mock_get):
        mock_csv_content = "id,title,price\n2,Banana,0.5\n1,Apple,0.3\n3,Cherry,0.2\n"
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        
        result = task_func("http://example.com/data.csv", 'title')
        expected_titles = ["Apple", "Banana", "Cherry"]
        actual_titles = result['title'].tolist()
        self.assertEqual(actual_titles, expected_titles)
    @patch('requests.get')
    def test_case_2(self, mock_get):
        mock_csv_content = "id,title,price\n2,Banana,0.5\n1,Apple,0.3\n3,Cherry,0.2\n"
        
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        
        result = task_func("http://example.com/tst.csv", 'price')
        self.assertEqual(result.iloc[0]['price'], 0.2)
        self.assertEqual(result.iloc[1]['price'], 0.3)
        self.assertEqual(result.iloc[2]['price'], 0.5)
    @patch('requests.get')
    def test_case_3(self, mock_get):
        mock_csv_content = "id,title,price\n2,Banana,0.5\n1,Apple,0.3\n3,Cherry,0.2\n"
        
        
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        
        result = task_func("http://example.com/tst.csv")
        self.assertEqual(result.iloc[0]['title'], "Apple")
        self.assertEqual(result.iloc[1]['title'], "Banana")
        self.assertEqual(result.iloc[2]['title'], "Cherry")
    @patch('requests.get')
    def test_case_4(self, mock_get):
        mock_csv_content =  "id,title,price\n"
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        
        result = task_func("http://example.com/empty.csv")
        self.assertTrue(result.empty)
    @patch('requests.get')
    def test_case_5(self, mock_get):
        mock_csv_content = "id,name,age\n2,John,25\n1,Alice,30\n3,Bob,20\n"
        mock_response = requests.models.Response()
        mock_response.status_code = 200
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        
        result = task_func("http://example.com/test_2.csv", "age")
        self.assertEqual(result.iloc[0]['name'], "Bob")
        self.assertEqual(result.iloc[1]['name'], "John")
        self.assertEqual(result.iloc[2]['name'], "Alice")
    
    @patch('requests.get')
    def test_case_6(self, mock_get):
        mock_csv_content =  "id,title,price\n"
        mock_response = requests.models.Response()
        mock_response.status_code = 400
        mock_response.headers['content-type'] = 'text/csv'
        mock_response._content = mock_csv_content.encode('utf-8')
        mock_get.return_value = mock_response
        with self.assertRaises(Exception): 
            result = task_func("http://example.com/error.csv")
