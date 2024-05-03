import re
import urllib.parse
import requests
import json

# Constants


def f_981(myString, API_KEY):
    """
    Extract all URLs from a myString string, analyze each URL to extract the domain, and use the IP API to get the geolocation data for each domain.
    
    
    Parameters:
    myString (str): The string to extract URLs from.
    API_KEY (str): The API key used to access the IP API service.

    
    Returns:
    dict: A dictionary with domains as keys and geolocation data as values.

    Requirements:
    - re
    - urllib.parse
    - requests
    - json
    
    Example:
    >>> f_981("Check these links: http://www.google.com, https://www.python.org")
    {'www.google.com': {'status': 'success', 'country': 'United States', 'countryCode': 'US', 'region': 'CA', 'regionName': 'California', 'city': 'Mountain View', 'zip': '94043', 'lat': '37.4192', 'lon': '-122.0574', 'timezone': 'America/Los_Angeles', 'isp': 'Google LLC', 'org': 'Google LLC', 'as': 'AS15169 Google LLC', 'query': '172.217.12.142'}, 'www.python.org': {'status': 'success', 'country': 'United States', 'countryCode': 'US', 'region': 'OR', 'regionName': 'Oregon', 'city': 'Boardman', 'zip': '97818', 'lat': '45.8696', 'lon': '-119.688', 'timezone': 'America/Los_Angeles', 'isp': 'Amazon.com, Inc.', 'org': 'Amazon Data Services NoVa', 'as': 'AS16509 Amazon.com, Inc.', 'query': '151.101.193.223'}}
    """
    urls = re.findall('(https?://[^\s,]+)', myString)
    geo_data = {}

    for url in urls:
        domain = urllib.parse.urlparse(url).netloc
        response = requests.get(f"http://ip-api.com/json/{domain}?access_key={API_KEY}")
        geo_data[domain] = json.loads(response.text)

    return geo_data

import unittest
from unittest.mock import patch
import requests
import json

class MockResponse:
    def __init__(self):
        self.text = json.dumps({
            'status': 'success',
            'country': 'United States',
            'countryCode': 'US',
            'region': 'CA',
            'regionName': 'California',
            'city': 'Mountain View',
            'zip': '94043',
            'lat': '37.4192',
            'lon': '-122.0574',
            'timezone': 'America/Los_Angeles',
            'isp': 'Google LLC',
            'org': 'Google LLC',
            'as': 'AS15169 Google LLC',
            'query': '172.217.12.142'
        })

    def json(self):
        return json.loads(self.text)

@patch('requests.get', return_value=MockResponse())
def run_tests(mock_get):

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    def test_case_1(self):
        result = f_981("http://www.google.com", "TEST_API_KEY")
        self.assertIn('www.google.com', result)
        self.assertEqual(result['www.google.com']['city'], 'Mountain View')

    def test_case_2(self):
        result = f_981("http://www.google.com, https://www.python.org", "TEST_API_KEY")
        self.assertIn('www.google.com', result)
        self.assertIn('www.python.org', result)

    def test_case_3(self):
        result = f_981("This is a test without URLs.", "TEST_API_KEY")
        self.assertEqual(result, {})

    def test_case_4(self):
        result = f_981("This is not a link: abc://test.link", "TEST_API_KEY")
        self.assertEqual(result, {})

    def test_case_5(self):
        result = f_981("http://www.google.com, http://www.google.com/about", "TEST_API_KEY")
        self.assertIn('www.google.com', result)
        self.assertNotIn('www.google.com/about', result)

if __name__ == "__main__":
    run_tests()