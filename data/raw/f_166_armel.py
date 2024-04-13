import os
import re
from urllib.parse import urlparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def f_166(myString: str, save_dir: str = None) -> str:
    """
    Extract the first URL from a string and take a screenshot of the web page at that URL.
    - The picture should be saved as the domain name with a png extension.
    - The path to the directory where to save the picture is given as an argument.

    Parameters:
    - myString (str): The string from which to extract the URL.
    - save_dir (str): The path to the directory where to save the picture. If None, consider the current directory.

    Returns:
    - str: The filename of the screenshot, named after the domain of the URL (e.g., 'www.google.com.png').

    Requirements:
    - os
    - re
    - urllib.parse
    - selenium.webdriver
    - webdriver_manager.chrome

    Example:
    >>> f_166('See this: https://www.google.com')
    'www.google.com.png'
    """
    # Extract the first URL from the string
    url = re.search(r'(https?://\S+)', myString).group()
    domain = urlparse(url).netloc
    
    # Use webdriver in headless mode to capture screenshot
    options = webdriver.ChromeOptions()
    options.headless = True
    #driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver = webdriver.Chrome()
    driver.get(url)
    screenshot_filename = domain + '.png'
    driver.save_screenshot(os.path.join(save_dir, screenshot_filename) if save_dir else screenshot_filename)
    driver.quit()

    return screenshot_filename

import unittest

class TestCases(unittest.TestCase):
    """Test cases for the f_166 function."""
    def setUp(self) -> None:
        self.test_dir = "data/f_166"
        os.makedirs(self.test_dir, exist_ok=True)
    
    def tearDown(self) -> None:
        import shutil
        shutil.rmtree(self.test_dir)

    def test_case_1(self):
        # A valid URL in the string
        input_string = 'Visit this website: https://www.example.com'
        result = f_166(input_string, self.test_dir)
        self.assertEqual(result, 'www.example.com.png')
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "www.example.com.png")))

    def test_case_2(self):
        # A string without a URL
        input_string = 'This is just a regular string without any URL.'
        with self.assertRaises(Exception):
            f_166(input_string)

    def test_case_3(self):
        # A string with multiple URLs
        input_string = 'Visit these websites: https://www.google.com and https://huggingface.co'
        result = f_166(input_string)
        self.assertEqual(result, 'www.google.com.png')

    def test_case_4(self):
        # A non-HTTP/HTTPS URL
        input_string = 'Check this ftp link: ftp://files.example.com'
        with self.assertRaises(Exception):
            f_166(input_string)

    def test_case_5(self):
        # A string with an invalid URL format
        input_string = 'Visit this site: www.example without protocol.'
        with self.assertRaises(Exception):
            f_166(input_string)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
