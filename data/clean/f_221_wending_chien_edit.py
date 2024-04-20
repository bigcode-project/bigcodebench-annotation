import pandas as pd
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


def f_221(df):
    """
    Analyzes a given DataFrame containing article titles and content to identify articles with titles that include
    the words "how" or "what". It calculates the TF-IDF scores for the words in the content of these articles and
    visualizes these scores in a bar plot.

    Parameters:
    df (DataFrame): A DataFrame containing at least two columns: 'Title' and 'Content'.

    Returns:
    Axes: A matplotlib Axes object displaying a bar plot of the TF-IDF scores.

    Note:
    - If the DataFrame does not contain 'Title' and 'Content' columns, the function returns an empty plot.
    - If no articles have titles containing "how" or "what," the function also returns an empty plot.

    Requirements:
    pandas, re, matplotlib.pyplot, sklearn.feature_extraction.text, numpy

    Example:
    >>> data = {'Title': ['How to make pancakes', 'News update'], 'Content': ['Pancakes are easy to make.', 'Today’s news is about politics.']}
    >>> df = pd.DataFrame(data)
    >>> ax = f_221(df)
    >>> type(ax)
    <class 'matplotlib.axes._subplots.AxesSubplot'>
    """
    pattern = re.compile(r'(how|what)', re.IGNORECASE)

    # Check if the DataFrame has the required columns
    if not set(['Title', 'Content']).issubset(df.columns):
        fig, ax = plt.subplots()
        return ax

    interesting_articles = df[df['Title'].apply(lambda x: bool(pattern.search(x)))]

    fig, ax = plt.subplots()

    # If there are no interesting articles, return an empty plot
    if interesting_articles.empty:
        return ax

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(interesting_articles['Content'])
    tfidf_scores = np.array(X.sum(axis=0))[0]

    ax.bar(vectorizer.get_feature_names_out(), tfidf_scores)
    ax.set_ylabel('TF-IDF Score')
    plt.xticks(rotation='vertical')

    return ax


import unittest
import pandas as pd


class TestCases(unittest.TestCase):

    def setUp(self):
        # Sample data for testing
        self.DATA = {
            'Title': ['How to code?', 'What is Python?', 'The art of programming', 'How to cook?', 'What is life?'],
            'Content': ['This is a tutorial about coding...', 'Python is a programming language...',
                        'Programming is an art...', 'This is a cooking tutorial...', 'Life is complicated...']
        }
        self.df_sample = pd.DataFrame(self.DATA)

    def test_case_1(self):
        # Test with original data
        ax = f_221(self.df_sample)
        self.assertEqual(len(ax.patches), 11)  # Adjusting based on actual data
        self.assertEqual(ax.get_ylabel(), "TF-IDF Score")

    def test_case_2(self):
        # Test with no interesting articles
        df_no_interesting = self.df_sample.copy()
        df_no_interesting['Title'] = ['Coding 101', 'Python tutorial', 'Programming basics', 'Cooking basics',
                                      'Life basics']
        ax = f_221(df_no_interesting)
        self.assertEqual(len(ax.patches), 0)  # No bars in the plot as no interesting articles

    def test_case_3(self):
        # Test with only one interesting article
        df_one_interesting = self.df_sample.copy()
        df_one_interesting['Title'] = ['How to play guitar?', 'Python tutorial', 'Programming basics', 'Cooking basics',
                                       'Life basics']
        ax = f_221(df_one_interesting)
        self.assertEqual(len(ax.patches), 5)  # 5 unique words in the interesting article

    def test_case_4(self):
        # Test with data not containing columns 'Title' and 'Content'
        df_empty = pd.DataFrame(columns=['Title', 'Description'])
        ax = f_221(df_empty)
        self.assertEqual(len(ax.patches), 0)  # No bars in the plot as dataframe is empty

    def test_case_5(self):
        # Test with empty dataframe
        df_empty = pd.DataFrame(columns=['Title', 'Content'])
        ax = f_221(df_empty)
        self.assertEqual(len(ax.patches), 0)  # No bars in the plot as dataframe is empty


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
