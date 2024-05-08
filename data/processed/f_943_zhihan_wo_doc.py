import re
from collections import Counter

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

def f_764(text):
    """
    Count the stopwords found in the text after you have removed URLs.

    Parameters:
    text (str): The text to summarize.

    Returns:
    list: A list of tuples where each tuple contains a word and its frequency.

    Requirements:
    - re
    - collection.Counter

    Example:
    >>> f_764('Visit https://www.python.org for more info. Python is great, we love Python.')
    [('for', 1), ('more', 1), ('is', 1), ('we', 1)]
    >>> f_764('Visit https://www.python.org for more info. Python is great, we love Python, and we also love Rust.')
    [('for', 1), ('more', 1), ('is', 1), ('we', 2), ('and', 1)]

    Note:
    - Valid url is start with http or https
    - The capitilization need to macth the stopwords
    """
    text = re.sub('http[s]?://\S+', '', text)
    words = re.findall(r'\b\w+\b', text)
    word_freq = Counter(words)
    result = Counter(words)
    for i in word_freq:
        if i not in PREDEFINED_STOPWORDS:
            del result[i]
    return list(result.items())

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Test with a URL
        input_text = 'Visit https://www.python.org for more info. Python is great.'
        expected_output = [('for', 1), ('more', 1), ('is', 1)]
        self.assertEqual(f_764(input_text), expected_output)
    def test_case_2(self):
        # Test without a URL
        input_text = 'Python is an amazing programming language.'
        expected_output = [('is', 1), ('an', 1)]
        self.assertEqual(f_764(input_text), expected_output)
    def test_case_3(self):
        # Test with long text
        input_text = "Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
        expected_output = [('is', 1), ('an', 1), ('and', 4), ('by', 1), ('in', 1), ('with', 1), ('its', 1), ('of', 1), ('to', 1), ('for', 1)]
        print(f_764(input_text))
        self.assertEqual(f_764(input_text), expected_output)
    def test_case_4(self):
        # Test with multiple URLs
        input_text = 'Check out https://www.python.org and https://www.djangoproject.com. Both are amazing.'
        expected_output = [('out', 1), ('and', 1), ('are', 1)]
        self.assertEqual(f_764(input_text), expected_output)
    def test_case_5(self):
        # Test with short text
        input_text = 'I love Python.'
        expected_output = []
        self.assertEqual(f_764(input_text), expected_output)
