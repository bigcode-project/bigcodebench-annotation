import requests
from bs4 import BeautifulSoup


def f_1030(url, selector):
    """
    Scrape a web page for elements matching a specified CSS selector and return the text of the first matching element.

    Parameters:
    url (str): The URL of the website to scrape.
    selector (str): A CSS selector to locate the element(s). This can target HTML tags, classes, IDs, or attributes.

    Returns:
    str: The text content of the first element that matches the CSS selector if found; otherwise, returns a message indicating the selector did not match any elements.

    Requirements:
    - requests
    - bs4

    Example:
    >>> f_1030("https://www.python.org/", "title")
    'Welcome to Python.org'
    >>> f_1030("https://www.python.org/", ".introduction .shrubbery")
    'Some introduction text here...'
    >>> f_1030("https://www.python.org/", "meta[name='description']")
    'The official home of the Python Programming Language'
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Use .select() to find elements matching the CSS selector; it returns a list of matching elements
    matched_elements = soup.select(selector)

    # If there's at least one match, return the text of the first matched element
    if matched_elements:
        # Extract text in a way that handles both regular elements and special cases like <meta> tags
        first_matched_element = matched_elements[0]
        if first_matched_element.name == 'meta' and 'content' in first_matched_element.attrs:
            return first_matched_element['content']
        else:
            return first_matched_element.get_text(strip=True)
    else:
        return f"No elements matching the selector '{selector}' were found on the provided website."


import unittest
from unittest.mock import patch, MagicMock


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    @patch('requests.get')
    def test_f_1030_attribute_found(self, mock_get):
        # Mock the response from requests.get
        mock_get.return_value = MagicMock()
        # Example HTML content
        example_html = '<html><head><title>Test Title</title></head><body></body></html>'
        mock_get.return_value.text = example_html

        # Call the function with the mocked requests.get
        result = f_1030("https://example.com/", "title")

        # Verify the result
        self.assertEqual(result, "Test Title")

    @patch('requests.get')
    def test_f_1030_attribute_not_found(self, mock_get):
        # Mock the response from requests.get
        mock_get.return_value = MagicMock()
        # Example HTML content without the target attribute
        example_html = '<html><head></head><body></body></html>'
        mock_get.return_value.text = example_html

        # Call the function with the mocked requests.get
        result = f_1030("https://example.com/", "title")

        # Verify the result indicates the attribute was not found
        self.assertEqual(result, "The attribute 'title' was not found on the provided website.")

    @patch('requests.get')
    def test_f_1030_title_attribute_found(self, mock_get):
        # Testing for a standard attribute (title) that exists
        mock_get.return_value = MagicMock()
        example_html = '<html><head><title>Test Title</title></head><body></body></html>'
        mock_get.return_value.text = example_html
        result = f_1030("https://example.com/", "title")
        self.assertEqual(result, "Test Title")

    @patch('requests.get')
    def test_f_1030_non_standard_attribute(self, mock_get):
        # Testing with a non-standard attribute
        mock_get.return_value = MagicMock()
        example_html = '<html><body><div data-custom="value">Content</div></body></html>'
        mock_get.return_value.text = example_html
        result = f_1030("https://example.com/", "div[data-custom]")
        self.assertEqual(result, "Content")

    @patch('requests.get')
    def test_f_1030_invalid_html(self, mock_get):
        # Testing with invalid HTML content
        mock_get.return_value = MagicMock()
        example_html = '<html><div><span>Unclosed div'
        mock_get.return_value.text = example_html
        result = f_1030("https://example.com/", "span")
        self.assertEqual(result, "Unclosed div")  # Check if the function can handle and parse invalid HTML

    @patch('requests.get')
    def test_f_1030_attribute_not_found(self, mock_get):
        # Testing for a missing attribute
        mock_get.return_value = MagicMock()
        example_html = '<html><head></head><body></body></html>'
        mock_get.return_value.text = example_html
        result = f_1030("https://example.com/", "title")
        self.assertEqual(result, "No elements matching the selector 'title' were found on the provided website.")

    @patch('requests.get')
    def test_f_1030_meta_description(self, mock_get):
        # Mock the response from requests.get to return a specific HTML structure
        mock_get.return_value.ok = True
        mock_get.return_value.text = """
           <html>
               <head>
                   <meta name="description" content="The official home of the Python Programming Language">
               </head>
               <body>
                   <p>Python is a programming language that lets you work quickly and integrate systems more effectively.</p>
               </body>
           </html>
           """

        # Call the function with the mocked requests.get
        result = f_1030("https://www.python.org/", "meta[name='description']")

        # Verify that the result matches the expected description content
        self.assertEqual(result, "The official home of the Python Programming Language")


if __name__ == '__main__':
    unittest.main()
