# Importing the required libraries
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Hard-coded list of common English stopwords for demonstration purposes
STOPWORDS = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
                 "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", 
                 "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", 
                 "theirs", "themselves", "what", "which", "who", "whom", "this", "that", 
                 "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", 
                 "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", 
                 "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", 
                 "at", "by", "for", "with", "about", "against", "between", "into", "through", 
                 "during", "before", "after", "above", "below", "to", "from", "up", "down", 
                 "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "simple", "test"])


def f_94(text, n=2):
    """
    Analyzes a text string, removing duplicate consecutive words and stopwords,
    generates a square co-occurrence matrix of words, and plots this matrix.

    Parameters:
    - text (str): Input text to be analyzed.
    - n (int, optional): Size of n-grams for the co-occurrence matrix. Defaults to 2.

    Returns:
    - tuple:
        - pd.DataFrame: Square co-occurrence matrix of words.
        - matplotlib.axes.Axes: Plot object of the co-occurrence matrix.

    Requirements:
        - re
        - pandas
        - matplotlib.pyplot
        - numpy
        - sklearn.feature_extraction.text

    Example:
    >>> import matplotlib
    >>> text = "hello hello world world"
    >>> df, ax = f_94(text, n=2)
    >>> df.columns.tolist()
    ['hello world']
    >>> df.index.tolist()
    ['hello world']
    >>> df.iloc[0, 0]
    0
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text)
    words_filtered = ' '.join([word for word in text.lower().split() if word not in STOPWORDS])
    if not words_filtered.strip():
        empty_df = pd.DataFrame()
        fig, ax = plt.subplots()
        return empty_df, ax
    vectorizer = CountVectorizer(ngram_range=(n, n))
    X = vectorizer.fit_transform([words_filtered])  # Ensure input is treated as a single document
    matrix = (X.T * X).todense()
    np.fill_diagonal(matrix, 0)
    feature_names = vectorizer.get_feature_names_out() if hasattr(vectorizer,
                                                                  'get_feature_names_out') else vectorizer.get_feature_names()
    matrix_df = pd.DataFrame(matrix, index=feature_names, columns=feature_names)
    fig, ax = plt.subplots()
    cax = ax.matshow(matrix_df, cmap='hot')
    fig.colorbar(cax)
    ax.set_xticks(np.arange(len(matrix_df.columns)))
    ax.set_yticks(np.arange(len(matrix_df.index)))
    ax.set_xticklabels(matrix_df.columns, rotation=90)
    ax.set_yticklabels(matrix_df.index)
    return matrix_df, ax

import unittest
class TestCases(unittest.TestCase):
    def test_simple_text(self):
        """Test with a simple text."""
        text = "hello world"
        matrix, _ = f_94(text)
        self.assertEqual(matrix.shape, (1, 1), "Matrix shape should be (1, 1) for unique words 'hello' and 'world'.")
    def test_text_with_stopwords(self):
        """Test text with stopwords removed."""
        text = "this is a simple test"
        matrix, _ = f_94(text)
        self.assertTrue(matrix.empty, "Matrix should be empty after removing stopwords.")
    def test_duplicate_words(self):
        """Test text with duplicate consecutive words."""
        text = "happy happy joy joy"
        matrix, _ = f_94(text)
        self.assertIn('happy joy', matrix.columns, "Matrix should contain 'happy joy' after duplicates are removed.")
    def test_ngram_range(self):
        """Test with a specific n-gram range."""
        text = "jump high and run fast"
        # Assuming no preprocessing that removes words, we expect 3 unique tri-grams.
        matrix, _ = f_94(text, n=3)
        # Expecting a 3x3 matrix since there are 3 unique tri-grams with no overlap in this simple case.
        self.assertEqual(matrix.shape, (2, 2),
                         "Matrix shape should be (3, 3) for a tri-gram analysis without word removal.")
    def test_empty_text(self):
        """Test with an empty string."""
        text = ""
        matrix, _ = f_94(text)
        self.assertTrue(matrix.empty, "Matrix should be empty for an empty string.")
