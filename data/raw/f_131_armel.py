import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def f_131(page_title):
    """
    Create a word cloud from the text of a Wikipedia page.

    Parameters:
    page_title (str): The title of the Wikipedia page.

    Returns:
    matplotlib.axes.Axes: The Axes object of the plotted data. Is None if there is no wikipedia page with the title given as input.

    Requirements:
    - wikipedia
    - wordcloud.WordCloud
    - matplotlib.pyplot

    Example:
    >>> ax = f_131('Python (programming language)')
    """
    try:
        text = wikipedia.page(page_title).content
    except Exception as e:
        print(f"An error occured: {e}")
        return None
    wordcloud = WordCloud().generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    ax = plt.gca()
    return ax

import unittest
from unittest.mock import patch

class A :
    def __init__(self, content) -> None:
        self.content = content
        self.text = content

class TestCases(unittest.TestCase):
    """Test cases for the f_131 function."""
    @patch('wikipedia.page')
    def test_case_1(self, mock_function):
        # Mocking the function to prevent actual execution
        mock_function.return_value = A("I want to sleep")
        # Running the function
        _ = f_131('Python (programming language)')

    @patch('wikipedia.page')
    def test_case_2(self, mock_function):
        # Mocking the function to prevent actual execution
        mock_function.return_value = A("I want to sleep because it is important to sleep.")
        # Running the function
        _ = f_131('Python (programming language)')

    @patch('wikipedia.page')
    def test_case_3(self, mock_function):
        # Mocking the function to prevent actual execution
        mock_function.return_value = A("I want to sleep")
        # Running the function
        _ = f_131('Python (programming language)')

    @patch('wikipedia.page')
    def test_case_4(self, mock_function):
        # Mocking the function to prevent actual execution
        mock_function.return_value =A("I want to eat")
        # Running the function
        _ = f_131('Python (programming language)')

    @patch('wikipedia.page')
    def test_case_5(self, mock_function):
        # Mocking the function to prevent actual execution
        mock_function.return_value = A("I want to help you to get your business to work.")
        # Running the function
        _ = f_131('Python (programming language)')

    def test_case_6(self):
        ax = f_131("Invalid Page Title")
        self.assertIsNone(ax)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
