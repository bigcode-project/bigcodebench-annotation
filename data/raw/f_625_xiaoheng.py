import urllib.request
from bs4 import BeautifulSoup
import csv
import os

# Constants
CSV_FILE_PATH = 'scraped_data.csv'

def f_625(url):
    """
    Scrape data from a given URL and save the scraped data to a CSV file.

    Parameters:
    - url (str): The URL to scrape data from.

    Returns:
    - CSV_FILE_PATH (str): The path of the CSV file where the scraped data is saved.

    Requirements:
    - urllib
    - bs4
    - csv
    - os

    Example:
    >>> f_625('http://www.example.com/')
    'scraped_data.csv'
    """
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    data = []
    table = soup.find('table', attrs={'class':'data-table'})
    table_rows = table.find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        data.append(row)
    
    if os.path.exists(CSV_FILE_PATH):
        os.remove(CSV_FILE_PATH)

    with open(CSV_FILE_PATH, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    return CSV_FILE_PATH

import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestCases(unittest.TestCase):
    
    def test_correct_scraping(self):
        # Testing if the function scrapes the correct data from the sample HTML page
        output_csv_path = f_625('file:///mnt/data/f_625_data_xiaoheng/sample_page.html')
        with open(output_csv_path, "r") as file:
            content = file.read()
        expected_content = 'Header 1,Header 2\nData 1,Data 2\nData 3,Data 4\n'
        self.assertEqual(content, expected_content)

    def test_invalid_url(self):
        # Testing with an invalid URL should raise an exception
        with self.assertRaises(Exception):
            f_625("invalid_url")
    
    def test_no_table(self):
        # Testing with an HTML content that has no table
        with self.assertRaises(Exception):
            f_625('file:///mnt/data/f_625_data_xiaoheng/no_table_page.html')

    def test_empty_table(self):
        # Testing with an HTML content that has an empty table
        output_csv_path = f_625('file:///mnt/data/f_625_data_xiaoheng/empty_table_page.html')
        with open(output_csv_path, "r") as file:
            content = file.read()
        self.assertEqual(content, "")  # Expecting an empty CSV content

    def test_overwrite_existing_csv(self):
        # Testing if the function overwrites an existing CSV file
        with open(CSV_FILE_PATH, "w") as file:
            file.write("Old Content")
        
        output_csv_path = f_625('file:///mnt/data/f_625_data_xiaoheng/sample_page.html')
        with open(output_csv_path, "r") as file:
            content = file.read()
        self.assertNotEqual(content, "Old Content")
        
if __name__ == "__main__":
    run_tests()