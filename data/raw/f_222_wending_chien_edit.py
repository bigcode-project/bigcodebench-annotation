import pandas as pd
import re
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer


def f_222(df):
    """
    Analyzes articles by their titles for specific keywords ("how" or "what"), vectorizes the content using
    CountVectorizer, and groups them into clusters using KMeans clustering. This function is intended for basic
    content analysis and clustering to understand common themes or topics among articles asking questions starting
    with "how" or "what".

    Parameters:
    df (pd.DataFrame): DataFrame containing article data with columns 'Title' for the article titles and 'Content' for
    the article text.

    Returns:
    list: List of cluster labels for the filtered articles, indicating the cluster to which each article belongs.

    Requirements:
    pandas, re, sklearn.cluster, sklearn.feature_extraction.text

    Example:
    >>> df_sample = pd.DataFrame({
    ...    'Title': ['How to code?', 'What is Python?', 'The art of programming', 'How to cook?', 'What is life?'],
    ...    'Content': ['This is a tutorial about coding...', 'Python is a programming language...',
    ...                'Programming is an art...', 'This is a cooking tutorial...', 'Life is complicated...']
    ... })
    >>> f_222(df_sample)
    [0, 1, 0, 1]
    """
    pattern = re.compile(r'(how|what)', re.IGNORECASE)
    interesting_articles = df[df['Title'].apply(lambda x: bool(pattern.search(x)))]
    if interesting_articles.empty:
        return []

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(interesting_articles['Content'])

    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    kmeans.fit(X)

    return list(kmeans.labels_)


import unittest
import pandas as pd
import os


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


class TestCases(unittest.TestCase):
    def setUp(self):
        """Prepare environment and variables for tests."""
        self.df_sample = pd.DataFrame({
            'Title': ['How to code?', 'What is Python?', 'The art of programming', 'How to cook?', 'What is life?'],
            'Content': ['This is a tutorial about coding...', 'Python is a programming language...',
                        'Programming is an art...', 'This is a cooking tutorial...', 'Life is complicated...']
        })
        os.environ['OMP_NUM_THREADS'] = '1'  # Setup environment variable for deterministic parallel processing

    def tearDown(self):
        """Clean up after tests."""
        os.environ.pop('OMP_NUM_THREADS', None)

    def test_vectorizer_and_clustering(self):
        """Test if the vectorization and clustering are setting up as expected, without mocking."""
        cluster_labels = f_222(self.df_sample)
        self.assertIn(set(cluster_labels), [{0, 1}])  # We expect two clusters
        self.assertEqual(len(cluster_labels), 4, "Expected 4 cluster labels.")

    def test_no_matching_articles(self):
        """Test the function with a DataFrame that has no titles containing 'how' or 'what'."""
        df_no_matches = pd.DataFrame({
            'Title': ['Understanding AI', 'Introduction to Machine Learning'],
            'Content': ['AI is a broad field.', 'Machine learning is a subset of AI.']
        })
        cluster_labels = f_222(df_no_matches)
        self.assertEqual(len(cluster_labels), 0, "Expected no cluster labels for DataFrame without matching titles.")

    def test_empty_dataframe(self):
        """Test the function with an empty DataFrame."""
        df_empty = pd.DataFrame(columns=['Title', 'Content'])
        cluster_labels = f_222(df_empty)
        self.assertEqual(len(cluster_labels), 0, "Expected no cluster labels for an empty DataFrame.")

    def test_invalid_dataframe_structure(self):
        """Test the function with a DataFrame missing required columns."""
        df_invalid = pd.DataFrame({
            'Headline': ['How to learn Python?'],  # Wrong column name
            'Body': ['Content about Python.']  # Wrong column name
        })
        with self.assertRaises(KeyError):
            f_222(df_invalid)

    def test_function_exception_handling(self):
        """Test to ensure that function handles incorrect input types gracefully."""
        with self.assertRaises(TypeError):
            f_222(None)  # Passing None to simulate bad input


if __name__ == "__main__":
    unittest.main()
