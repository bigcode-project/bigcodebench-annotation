import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re


def f_284(example_str):
    """
    Extract all texts not enclosed in square brackets into a string and calculate the TF-IDF values
    which are returned as a dictionary.

    Parameters:
    example_str (str): The input string.

    Returns:
    dict: A dictionary with words as keys and TF-IDF scores as values.

    Requirements:
    - sklearn.feature_extraction.text.TfidfVectorizer
    - numpy
    - re

    Example:
    >>> tfidf_scores = f_284("Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003] Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]")
    >>> print(tfidf_scores)
    {'dog': 0.3779644730092272, 'josie': 0.3779644730092272, 'mugsy': 0.3779644730092272, 'smith': 0.7559289460184544}
    """
    pattern = r'\[.*?\]'
    text = re.sub(pattern, '', example_str)
    if not text.strip():
        return {}

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([text])
    feature_names = tfidf_vectorizer.get_feature_names_out()
    tfidf_scores = dict(zip(feature_names, np.squeeze(tfidf_matrix.toarray())))

    return tfidf_scores


import unittest
import doctest


class TestCases(unittest.TestCase):

    def test_case_1(self):
        input_str = "Adversarial ] input ][[][ i[s []] a [ problem ] in [ machine learning ]"
        output = f_284(input_str)
        expected_output = {
            'adversarial': 0.5773502691896258, 
            'in': 0.5773502691896258, 
            'input': 0.5773502691896258
        }
        self.assertDictEqual(output, expected_output)

    def test_case_2(self):
        input_str = "Alice [1234 Street, City, State] Bob Charlie [5678 Street, AnotherCity, State]"
        output = f_284(input_str)
        expected_output = {
            'alice': 0.5773502691896258, 
            'bob': 0.5773502691896258, 
            'charlie': 0.5773502691896258
        }
        self.assertDictEqual(output, expected_output)

    def test_case_3(self):
        input_str = "No brackets here at all"
        output = f_284(input_str)
        expected_output = {
            'all': 0.4472135954999579, 
            'at': 0.4472135954999579, 
            'brackets': 0.4472135954999579, 
            'here': 0.4472135954999579, 
            'no': 0.4472135954999579
        }
        self.assertDictEqual(output, expected_output)

    def test_case_4(self):
        input_str = "Mix [bracketed content] (and non-bracketed) content"
        output = f_284(input_str)
        expected_output = {
            'and': 0.4472135954999579, 
            'bracketed': 0.4472135954999579, 
            'content': 0.4472135954999579, 
            'mix': 0.4472135954999579, 
            'non': 0.4472135954999579
        }
        self.assertDictEqual(output, expected_output)

    def test_case_5(self):
        input_str = "[Only bracketed content]"
        output = f_284(input_str)
        expected_output = {}
        self.assertDictEqual(output, expected_output)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    doctest.testmod()
    run_tests()
