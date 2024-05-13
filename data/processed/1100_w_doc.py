import re
from sklearn.feature_extraction.text import TfidfVectorizer


def task_func(texts):
    """
    Processes a collection of text documents to compute the TF-IDF (Term Frequency-Inverse Document Frequency) scores
    for each word, excluding any URLs present in the texts. The TF-IDF scores help to identify the importance of a word
    within a document relative to a collection of documents.

    Parameters:
    texts (list of str): A list containing the text documents to be analyzed.

    Returns:
    tuple of (list of tuples, list of str):
        - The first element is a list of tuples, each tuple representing a document with its words' TF-IDF scores in a
          dense matrix format. Each score in the tuple corresponds to a word's TF-IDF score in the document.
        - The second element is a list of strings, representing the unique words (features) across all documents for
          which TF-IDF scores have been calculated. The order of words in this list matches the order of scores in the
          tuples of the first element.

    Requirements:
    - re
    - sklearn.feature_extraction.text.TfidfVectorizer

    Example:
    >>> task_func(['Visit https://www.python.org for more info.', 'Python is great.', 'I love Python.'])
    ([(0.5, 0.0, 0.5, 0.0, 0.0, 0.5, 0.0, 0.5), (0.0, 0.62276601, 0.0, 0.62276601, 0.0, 0.0, 0.4736296, 0.0), (0.0, 0.0, 0.0, 0.0, 0.79596054, 0.0, 0.60534851, 0.0)], ['for', 'great', 'info', 'is', 'love', 'more', 'python', 'visit'])

    Notes:
    - URLs in the text documents are removed before calculating TF-IDF scores to ensure they do not affect the analysis.
    - The TF-IDF scores are rounded to 8 decimal places for precision.
    """

    if all(text.strip() == "" for text in texts):
        return [], []
    cleaned_texts = [re.sub('http[s]?://\S+', '', text) for text in texts]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(cleaned_texts)
    dense_matrix = [tuple(round(val, 8) for val in row) for row in tfidf_matrix.toarray().tolist()]
    return dense_matrix, list(vectorizer.get_feature_names_out())

import unittest
class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_texts = ['Visit https://www.python.org for more info.', 'Python is great.', 'I love Python.']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_2(self):
        input_texts = ['Hello world!', 'Python programming is fun.', 'Data science with Python.']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_3(self):
        input_texts = ['I love coding.', 'You love coding too.', 'We all love coding.']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_4(self):
        input_texts = ['Check out this amazing article at https://www.example.com/article']
        output = task_func(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)
    def test_case_5(self):
        input_texts = ['', '', '']
        expected_output = ([], [])
        self.assertEqual(task_func(input_texts), expected_output)
