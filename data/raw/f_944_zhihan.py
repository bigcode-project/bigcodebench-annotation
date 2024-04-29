import re
from sklearn.feature_extraction.text import TfidfVectorizer

def f_944(texts):
    """
    Calculate the TF-IDF score for each word in a text collection after removing URLs.

    Parameters:
    texts (list of str): The texts to analyze.

    Returns:
    tuple: A tuple containing:
        - list of tuples: A dense matrix of TF-IDF scores.
        - list of str: The feature names (words) corresponding to the scores.

    Requirements:
    - re
    - sklearn.feature_extraction.text.TfidfVectorizer

    Example:
    >>> f_944(['Visit https://www.python.org for more info.', 'Python is great.', 'I love Python.'])
    ([(0.70710678, 0.70710678, 0.        , 0.        , 0.        , 0.        ),
      (0.        , 0.        , 0.6316672 , 0.6316672 , 0.44943642, 0.        ),
      (0.        , 0.        , 0.        , 0.        , 0.44943642, 0.6316672 )],
     ['for', 'info', 'great', 'is', 'python', 'love'])
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
if __name__ == "__main__":
    run_tests()