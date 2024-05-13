from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd


def task_func(documents):
    """
    Calculate the TF-IDF score of the words in a list of documents.
    
    Parameters:
    - documents (list of str): A list of text documents.
    
    Returns:
    pandas.DataFrame: A DataFrame with words as columns and documents as rows, containing the TF-IDF scores.
    
    Requirements:
    - nltk.tokenize.word_tokenize
    - sklearn.feature_extraction.text.TfidfVectorizer
    - pandas
    
    Example:
    >>> docs = ['This is the first document.', 'This document is the second document.', 'And this is the third one.', 'Is this the first document?']
    >>> tfidf = task_func(docs)
    >>> print(tfidf.shape)
    (4, 11)
    """

    vectorizer = TfidfVectorizer(tokenizer=word_tokenize)
    tfidf_matrix = vectorizer.fit_transform(documents)
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    return tfidf_df

import unittest
import doctest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        docs = ['This is the first document.', 'This document is the second document.']
        tfidf = task_func(docs)
        self.assertTrue(isinstance(tfidf, pd.DataFrame))
        self.assertEqual(tfidf.shape[0], 2)
        self.assertIn('first', tfidf.columns)
        self.assertIn('second', tfidf.columns)
        self.assertNotIn('third', tfidf.columns)
    def test_case_2(self):
        docs = ['And this is the third one.', 'Is this the first document?']
        tfidf = task_func(docs)
        self.assertTrue(isinstance(tfidf, pd.DataFrame))
        self.assertEqual(tfidf.shape[0], 2)
        self.assertIn('first', tfidf.columns)
        self.assertNotIn('second', tfidf.columns)
        self.assertIn('third', tfidf.columns)
    def test_case_3(self):
        docs = ['Hello world!', 'Machine learning is fun.']
        tfidf = task_func(docs)
        self.assertTrue(isinstance(tfidf, pd.DataFrame))
        self.assertEqual(tfidf.shape[0], 2)
        self.assertIn('hello', tfidf.columns)
        self.assertIn('world', tfidf.columns)
        self.assertIn('machine', tfidf.columns)
    def test_case_4(self):
        docs = ['Natural Language Processing.', 'Deep learning and neural networks.']
        tfidf = task_func(docs)
        self.assertTrue(isinstance(tfidf, pd.DataFrame))
        self.assertEqual(tfidf.shape[0], 2)
        self.assertIn('natural', tfidf.columns)
        self.assertIn('processing', tfidf.columns)
        self.assertIn('deep', tfidf.columns)
    def test_case_5(self):
        docs = ['Data science is a field.', 'It involves statistics and algorithms.']
        tfidf = task_func(docs)
        self.assertTrue(isinstance(tfidf, pd.DataFrame))
        self.assertEqual(tfidf.shape[0], 2)
        self.assertIn('data', tfidf.columns)
        self.assertIn('science', tfidf.columns)
        self.assertIn('statistics', tfidf.columns)
