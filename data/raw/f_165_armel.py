import re
import urllib.parse
import requests
from xml.etree import ElementTree as ET

# Constants

def f_165(myString):
    """
    Extract all URLs from a string called "myString," analyze each URL to extract the domain, and make a GET request to the sitemap.xml of each domain to extract all sitemap URLs.
    
    Parameters:
    - myString (str): The string to extract URLs from.
    
    Returns:
    - dict: A dictionary with domains as keys and sitemap URLs as values.

    Requirements:
    - re
    - urllib.parse
    - requests
    - xml.etree.ElementTree
    
    Example:
    >>> f_165("Check these links: http://www.google.com, https://www.python.org")
    {'www.google.com': ['https://www.google.com/sitemap_1.xml', 'https://www.google.com/sitemap_2.xml'], 'www.python.org': ['https://www.python.org/sitemap_1.xml', 'https://www.python.org/sitemap_2.xml']}
    """
    urls = re.findall('(https?://[^\\s]+)', myString)
    sitemap_urls = {}

    for url in urls:
        # Extract domain from URL
        domain = urllib.parse.urlparse(url).hostname
        
        if domain:
            # Make a GET request to the sitemap.xml
            sitemap_url = f"https://{domain}/sitemap.xml"
            response = requests.get(sitemap_url)
            
            if response.status_code == 200:
                # Parse the XML content of the sitemap
                root = ET.fromstring(response.content)
                # Extract all sitemap URLs
                sitemap_urls[domain] = [sitemap.text for sitemap in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}sitemaploc')]
                print(sitemap_urls[domain])
    
    return sitemap_urls

import unittest
from unittest.mock import patch

def mock_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code
            self.content = text.encode("utf-8")
    
    if args[0] == "https://www.example.com/sitemap.xml":
        return MockResponse(
            '<urlset><url><loc>https://www.example.com/page1</loc></url></urlset>',
            200
        )
    elif args[0] == "https://www.test.com/sitemap.xml":
        return MockResponse(
            '<urlset><url><loc>https://www.test.com/pageA</loc></url><url><loc>https://www.test.com/pageB</loc></url></urlset>',
            200
        )
    else:
        return MockResponse('', 404)

class TestCases(unittest.TestCase):
    """Test cases for the f_165 function."""   
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_1(self, *args, **kwargs):
        input_str = "Visit https://www.example.com and https://www.invalid.com"
        expected_output = {'www.example.com': ['https://www.example.com/page1']}
        result = f_165(input_str)
        print(f"yo1 {result}")
        self.assertEqual(result, expected_output)
        
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_2(self,*args, **kwargs):
        input_str = "Check https://www.example.com and https://www.test.com"
        expected_output = {
            'www.example.com': ['https://www.example.com/page1'],
            'www.test.com': ['https://www.test.com/pageA', 'https://www.test.com/pageB']
        }
        result = f_165(input_str)
        self.assertEqual(result, expected_output)
    
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_3(self, *args, **kwargs):
        input_str = "This string has no URLs."
        expected_output = {}
        result = f_165(input_str)
        self.assertEqual(result, expected_output)
    
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_4(self, *args, **kwargs):
        input_str = "Visit https://www.example.com, https://www.example.com and https://www.example.com"
        expected_output = {'www.example.com': ['https://www.example.com/page1']}
        result = f_165(input_str)
        self.assertEqual(result, expected_output)
    
    @patch('requests.get', side_effect=mock_requests_get)
    def test_case_5(self, *args, **kwargs):
        input_str = "Check out https://www.invalid.com"
        expected_output = {}
        result = f_165(input_str)
        self.assertEqual(result, expected_output)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__" :
    run_tests()    