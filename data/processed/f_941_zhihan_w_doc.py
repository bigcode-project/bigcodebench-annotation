import re
from string import punctuation

# Predefined list of common stopwords
PREDEFINED_STOPWORDS = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", 
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", 
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", 
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", 
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", 
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "more"
}

def f_762(text):
    """
    Clean the specified text by removing URLs, stopwords, and punctuation.

    Parameters:
    text (str): The text to be cleaned.

    Returns:
    str: The cleaned text with URLs, predefined stopwords, and punctuation removed.

    Requirements:
    - re
    - string.punctuation

    Example:
    >>> f_762('Visit https://www.python.org for more info. I love to eat apples.')
    'Visit info love eat apples'
    """
    PUNCTUATION = set(punctuation)
    text = re.sub('http[s]?://\S+', '', text)
    text = re.sub('[{}]'.format(re.escape(''.join(PUNCTUATION))), '', text)
    words = text.split()
    cleaned_words = [word for word in words if word.lower() not in PREDEFINED_STOPWORDS]
    return ' '.join(cleaned_words)

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_text = 'Visit https://www.python.org for more info. I love to eat apples and oranges!'
        expected_output = 'Visit info love eat apples oranges'
        result = f_762(input_text)
        self.assertEqual(result, expected_output)
    def test_case_2(self):
        input_text = 'Check out https://www.google.com and also https://www.openai.com'
        expected_output = 'Check also'
        result = f_762(input_text)
        self.assertEqual(result, expected_output)
    def test_case_3(self):
        input_text = 'Hello, world! How are you today?'
        expected_output = 'Hello world How today'
        result = f_762(input_text)
        self.assertEqual(result, expected_output)
    def test_case_4(self):
        input_text = 'Machine learning AI'
        expected_output = 'Machine learning AI'
        result = f_762(input_text)
        self.assertEqual(result, expected_output)
    def test_case_5(self):
        input_text = ''
        expected_output = ''
        result = f_762(input_text)
        self.assertEqual(result, expected_output)
