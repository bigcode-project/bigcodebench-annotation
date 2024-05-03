import re
from sklearn.feature_extraction.text import TfidfVectorizer


def f_944(texts):
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
    >>> f_944(['Visit https://www.python.org for more info.', 'Python is great.', 'I love Python.'])
    ([(0.70710678, 0.70710678, 0.        , 0.        , 0.        , 0.        ),
      (0.        , 0.        , 0.6316672 , 0.6316672 , 0.44943642, 0.        ),
      (0.        , 0.        , 0.        , 0.        , 0.44943642, 0.6316672 )],
     ['for', 'info', 'great', 'is', 'python', 'love'])

    Notes:
    - URLs in the text documents are removed before calculating TF-IDF scores to ensure they do not affect the analysis.
    - The TF-IDF scores are rounded to 8 decimal places for precision.
    """

    # Handle empty input
    if all(text.strip() == "" for text in texts):
        return [], []

    # Remove URLs
    cleaned_texts = [re.sub('http[s]?://\S+', '', text) for text in texts]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(cleaned_texts)

    # Convert the sparse matrix to a dense format, round the values, convert to tuples and return along with feature names
    dense_matrix = [tuple(round(val, 8) for val in row) for row in tfidf_matrix.toarray().tolist()]
    return dense_matrix, list(vectorizer.get_feature_names_out())


import unittest


def run_tests():
    """Execute the test cases for the function f_944."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner(verbosity=2)
    results = runner.run(suite)
    return results


class TestCases(unittest.TestCase):
    def test_case_1(self):
        input_texts = ['Visit https://www.python.org for more info.', 'Python is great.', 'I love Python.']
        output = f_944(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)

    def test_case_2(self):
        input_texts = ['Hello world!', 'Python programming is fun.', 'Data science with Python.']
        output = f_944(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)

    def test_case_3(self):
        input_texts = ['I love coding.', 'You love coding too.', 'We all love coding.']
        output = f_944(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)

    def test_case_4(self):
        input_texts = ['Check out this amazing article at https://www.example.com/article']
        output = f_944(input_texts)
        sorted_indices = sorted(range(len(output[1])), key=lambda k: output[1][k])
        expected_output = (
            [tuple(row[i] for i in sorted_indices) for row in output[0]],
            sorted(output[1])
        )
        self.assertEqual(output, expected_output)

    def test_case_5(self):
        input_texts = ['', '', '']
        expected_output = ([], [])
        self.assertEqual(f_944(input_texts), expected_output)


if __name__ == '__main__':
    run_tests()
