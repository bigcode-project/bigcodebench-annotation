import re
from nltk.corpus import stopwords


def f_494(text: str) -> dict:
    """
    Analyzes a given text string by removing duplicate words and stopwords, 
    and then returns a frequency distribution of the remaining words.

    Parameters:
    - text (str): The text string to analyze.

    Returns:
    - dict: The frequency distribution of the words in the text after filtering.

    Requirements:
    - re
    - nltk.corpus

    Note:
    - A manually defined set of common English stopwords is used for filtering.

    Examples:
    >>> f_494("The quick brown fox jumps over the lazy dog and the dog was not that quick to respond.")
    {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'lazy': 1, 'dog': 1, 'respond': 1}

    >>> f_494("hello hello world")
    {'hello': 1, 'world': 1}
    """
    # Remove duplicate words
    stop_words = set(stopwords.words('english'))
    text = ' '.join(sorted(set(text.split()), key=text.index))
    # Tokenize and remove stopwords
    words = [word for word in re.findall(r'\b\w+\b', text.lower()) if word not in stop_words]
    
    # Create frequency distribution
    freq_dist = {}
    for word in words:
        freq_dist[word] = freq_dist.get(word, 0) + 1
    
    return freq_dist

import unittest

class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_text = "The quick brown fox jumps over the lazy dog and the dog was not that quick to respond."
        output = f_494(input_text)
        expected_output = {'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'lazy': 1, 'dog': 1, 'respond': 1}
        self.assertEqual(output, expected_output)

    def test_case_2(self):
        input_text = "hello hello world"
        output = f_494(input_text)
        expected_output = {'hello': 1, 'world': 1}
        self.assertEqual(output, expected_output)

    def test_case_3(self):
        input_text = "the and is"
        output = f_494(input_text)
        expected_output = {}
        self.assertEqual(output, expected_output)

    def test_case_4(self):
        input_text = ""
        output = f_494(input_text)
        expected_output = {}
        self.assertEqual(output, expected_output)

    def test_case_5(self):
        input_text = "hello1 hello2 hello1"
        output = f_494(input_text)
        expected_output = {'hello1': 1, 'hello2': 1}
        self.assertEqual(output, expected_output)

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()