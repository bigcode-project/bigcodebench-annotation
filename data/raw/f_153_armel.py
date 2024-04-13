import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.python.org/downloads/'

def f_153(html_file_path=None):
    """
    Scrape the Python.org download page (or a provided local HTML file) and return a DataFrame with Python version and release date.

    Parameters:
    - html_file_path (str, optional): Path to a local HTML file to be parsed. If not provided, the function scrapes the Python.org download page.

    Returns:
    DataFrame: A pandas DataFrame with two columns: 'Version' and 'Release Date'. Each row represents
               a version of Python and its corresponding release date.
    
    Requirements:
    - requests
    - bs4 (BeautifulSoup)
    - pandas

    Example:
    >>> versions = f_153()
    >>> print(versions.head())
    >>> versions_local = f_153(html_file_path="path_to_local_html_file")
    >>> print(versions_local.head())
    """
    if html_file_path:
        with open(html_file_path, "r") as f:
            content = f.read()
    else:
        response = requests.get(URL)
        content = response.text
        
    soup = BeautifulSoup(content, 'html.parser')
    version_elements = soup.select('.download-list-widget .list-row-container li')
    version_data = []

    for version_element in version_elements:
        version = version_element.find('span', class_='release-number').text.split(' ')[1]
        date = version_element.find('span', class_='release-date').text
        version_data.append([version, date])

    version_df = pd.DataFrame(version_data, columns=['Version', 'Release Date'])
    return version_df

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_153 function."""
    def setUp(self):
        self.test_dir = "data/f_153"
        os.makedirs(self.test_dir, exist_ok=True)
        self.html_1 = os.path.join(self.test_dir, "html_1.html")
        html_1="""
        <html>
        <head>
        <title>
        </title>
        </head>
        <body>
        <div class="row download-list-widget">

            <h2 class="widget-title">Looking for a specific release?</h2>
            <p class="success-quote">Python releases by version number:</p>

            <div class="list-row-headings">
                <span class="release-number">Release version</span>
                <span class="release-date">Release date</span>
                <span class="release-download">&nbsp;</span>
                <span class="release-enhancements">Click for more</span>
            </div>
            <ol class="list-row-container menu">
                
                <li>
                    <span class="release-number"><a href="/downloads/release/python-3119/">Python 3.11.9</a></span>
                    <span class="release-date">April 2, 2024</span>
                    <span class="release-download"><a href="/downloads/release/python-3119/"><span aria-hidden="true" class="icon-download"></span> Download</a></span>
                    <span class="release-enhancements"><a href="https://docs.python.org/release/3.11.9/whatsnew/changelog.html#python-3-11-9">Release Notes</a></span>
                </li>
                
                <li>
                    <span class="release-number"><a href="/downloads/release/python-31014/">Python 3.10.14</a></span>
                    <span class="release-date">March 19, 2024</span>
                    <span class="release-download"><a href="/downloads/release/python-31014/"><span aria-hidden="true" class="icon-download"></span> Download</a></span>
                    <span class="release-enhancements"><a href="https://docs.python.org/release/3.10.14/whatsnew/changelog.html">Release Notes</a></span>
                </li>
                
                <li>
                    <span class="release-number"><a href="/downloads/release/python-3919/">Python 3.9.19</a></span>
                    <span class="release-date">March 19, 2024</span>
                    <span class="release-download"><a href="/downloads/release/python-3919/"><span aria-hidden="true" class="icon-download"></span> Download</a></span>
                    <span class="release-enhancements"><a href="https://docs.python.org/release/3.9.19/whatsnew/changelog.html">Release Notes</a></span>
                </li>
            </ol>
            <p><a href="/download/releases/">View older releases</a><!-- removed by Frank until content available <small><em>Older releases: <a href="#">Source releases, <a href="#">binaries-1.1</a>, <a href="#">binaries-1.2</a>, <a href="#">binaries-1.3</a>, <a href="#">binaries-1.4</a>, <a href="#">binaries-1.5</a></em></small> --></p>
        </div>
        </body>
        </html>
        """
        with open(self.html_1, "w") as f :
            f.write(html_1)
        self.html_2 = os.path.join(self.test_dir, "html_2.html")
        html_2="""
        <html>
        <head>
        <title>
        </title>
        </head>
        <body>
        <div class="row download-list-widget">

            <h2 class="widget-title">Looking for a specific release?</h2>
            <p class="success-quote">Python releases by version number:</p>

            <div class="list-row-headings">
                <span class="release-number">Release version</span>
                <span class="release-date">Release date</span>
                <span class="release-download">&nbsp;</span>
                <span class="release-enhancements">Click for more</span>
            </div>
            <ol class="list-row-container menu">
                
                <li>
                    <span class="release-number"><a href="/downloads/release/python-3119/">Python 3.11.9</a></span>
                    <span class="release-date">April 2, 2024</span>
                    <span class="release-download"><a href="/downloads/release/python-3119/"><span aria-hidden="true" class="icon-download"></span> Download</a></span>
                    <span class="release-enhancements"><a href="https://docs.python.org/release/3.11.9/whatsnew/changelog.html#python-3-11-9">Release Notes</a></span>
                </li>
            </ol>
            <p><a href="/download/releases/">View older releases</a><!-- removed by Frank until content available <small><em>Older releases: <a href="#">Source releases, <a href="#">binaries-1.1</a>, <a href="#">binaries-1.2</a>, <a href="#">binaries-1.3</a>, <a href="#">binaries-1.4</a>, <a href="#">binaries-1.5</a></em></small> --></p>   
        </div>
        </body>
        </html>
        """
        with open(self.html_2, "w") as f :
            f.write(html_2)
        self.html_3 = os.path.join(self.test_dir, "html_3.html")
        html_3="""
        <html>
        <head><title></title></head>
        <body></body>
        </html>
        """
        with open(self.html_3, "w") as f :
            f.write(html_3)
        self.html_4 = os.path.join(self.test_dir, "html_4.html")
        html_4="""
        <html>
        <head>
        <title>
        </title>
        </head>
        <body>
        <div class="row download-list-widget">

            <h2 class="widget-title">Looking for a specific release?</h2>
            <p class="success-quote">Python releases by version number:</p>

            <div class="list-row-headings">
                <span class="release-number">Release version</span>
                <span class="release-date">Release date</span>
                <span class="release-download">&nbsp;</span>
                <span class="release-enhancements">Click for more</span>
            </div>
            <ol class="list-row-container menu">
                
                <li>
                    <span class="release-number"><a href="/downloads/release/python-234/">Python 2.3.4</a></span>
                    <span class="release-date">May 27, 2004</span>
                    <span class="release-download"><a href="/downloads/release/python-234/"><span aria-hidden="true" class="icon-download"></span> Download</a></span>
                    <span class="release-enhancements"><a href="http://hg.python.org/cpython/raw-file/v2.3.4/Misc/NEWS">Release Notes</a></span>
                </li>
            </ol>
            <p><a href="/download/releases/">View older releases</a><!-- removed by Frank until content available <small><em>Older releases: <a href="#">Source releases, <a href="#">binaries-1.1</a>, <a href="#">binaries-1.2</a>, <a href="#">binaries-1.3</a>, <a href="#">binaries-1.4</a>, <a href="#">binaries-1.5</a></em></small> --></p>   
        </div>
        </body>
        </html>
        """
        with open(self.html_4, "w") as f :
            f.write(html_4)
    
    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.test_dir)  
    
    def test_case_1(self):
        versions = f_153(html_file_path=self.html_1)
        self.assertIsInstance(versions, pd.DataFrame)
        self.assertEqual(list(versions.columns), ['Version', 'Release Date'])
        self.assertFalse(versions.empty)
        df = pd.DataFrame(
            {
                "Version": ["3.11.9", "3.10.14", "3.9.19"],
                "Release Date": ["April 2, 2024", "March 19, 2024", "March 19, 2024"]
            }
        )
        pd.testing.assert_frame_equal(versions, df)
    def test_case_2(self):
        versions = f_153(html_file_path=self.html_2)
        self.assertIsInstance(versions, pd.DataFrame)
        self.assertEqual(list(versions.columns), ['Version', 'Release Date'])
        self.assertFalse(versions.empty)
        df = pd.DataFrame(
            {
                "Version": ["3.11.9"],
                "Release Date": ["April 2, 2024"]
            }
        )
        pd.testing.assert_frame_equal(versions, df)

    def test_case_3(self):
        versions = f_153(html_file_path=self.html_3)
        self.assertIsInstance(versions, pd.DataFrame)
        self.assertEqual(list(versions.columns), ['Version', 'Release Date'])
        self.assertTrue(versions.empty)

    def test_case_4(self):
        versions = f_153(html_file_path=self.html_4)
        self.assertIsInstance(versions, pd.DataFrame)
        self.assertEqual(list(versions.columns), ['Version', 'Release Date'])
        self.assertFalse(versions.empty)
        df = pd.DataFrame(
            {
                "Version": ["2.3.4"],
                "Release Date": ["May 27, 2004"]
            }
        )
        pd.testing.assert_frame_equal(versions, df)

    def test_case_5(self):
        versions = f_153(html_file_path=None)
        self.assertIsInstance(versions, pd.DataFrame)
        self.assertEqual(list(versions.columns), ['Version', 'Release Date'])
        self.assertFalse(versions.empty)
        self.assertTrue(versions.shape[0] >= 20)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests() 