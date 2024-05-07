import re
import string
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
# Constants
ALPHANUMERIC = re.compile('[\W_]+')
PUNCTUATIONS = string.punctuation


def f_542(text: str, sia: SentimentIntensityAnalyzer) -> dict:
    """Analyze the sentiment of a text using the provided SentimentIntensityAnalyzer.
    The text is first cleaned by:
    - Removing all non-alphanumeric characters except spaces.
    - Converting to lowercase.
    - Removing punctuation.
    
    Parameters:
    text (str): The string to analyze.
    sia (SentimentIntensityAnalyzer): An instance of the SentimentIntensityAnalyzer for sentiment analysis.
    
    Returns:
    dict: A dictionary with sentiment scores. The dictionary contains four scores:
          - 'compound': The overall sentiment score.
          - 'neg': Negative sentiment score.
          - 'neu': Neutral sentiment score.
          - 'pos': Positive sentiment score.
    
    Requirements:
    - re
    - string
    - nltk
    - nltk.sentiment.vader
    
    Example:
    >>> from nltk.sentiment import SentimentIntensityAnalyzer
    >>> sia = SentimentIntensityAnalyzer()
    >>> f_542("I love Python!", sia)
    {'neg': 0.0, 'neu': 0.192, 'pos': 0.808, 'compound': 0.6369}
    """
    text = ALPHANUMERIC.sub(' ', text).lower()
    text = text.translate(str.maketrans('', '', PUNCTUATIONS))
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

import unittest
# Mock the SentimentIntensityAnalyzer for our tests
class MockedSentimentIntensityAnalyzer:
    def polarity_scores(self, text):
        return {'compound': 0.5, 'neg': 0.25, 'neu': 0.25, 'pos': 0.5}
class TestCases(unittest.TestCase):
    def test_case_1(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = f_542("I love Python!", sia)
        expected = {'compound': 0.5, 'neg': 0.25, 'neu': 0.25, 'pos': 0.5}
        self.assertEqual(result, expected)
    
    def test_case_2(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = f_542("I hate rainy days.", sia)
        self.assertEqual(result['neg'], 0.25)
    
    def test_case_3(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = f_542("The weather is neutral today.", sia)
        self.assertEqual(result['neu'], 0.25)
    
    def test_case_4(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = f_542("Absolutely fantastic!", sia)
        self.assertEqual(result['pos'], 0.5)
    
    def test_case_5(self):
        sia = MockedSentimentIntensityAnalyzer()
        result = f_542("This is a bad idea!", sia)
        self.assertEqual(result['neg'], 0.25)
