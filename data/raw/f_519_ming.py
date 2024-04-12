import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Make sure to download NLTK stopwords
nltk.download('stopwords')

# Define a regex pattern for matching all non-alphanumeric characters
ALPHANUMERIC = re.compile('[\W_]+')

# Load NLTK's list of English stop words
STOPWORDS = nltk.corpus.stopwords.words('english')


def f_519(texts):
    """
    Creates a document-term matrix (DTM) from a list of text documents using CountVectorizer from Scikit-learn.
    Texts are preprocessed by removing non-alphanumeric characters (excluding spaces),
    converting to lowercase, and excluding English stop words defined in NLTK.

    Parameters:
    - texts (list of str): The list of text documents to convert into a DTM.

    Returns:
    - pd.DataFrame: A DataFrame where rows represent documents and columns represent unique terms;
                    cell values indicate the frequency of a term in a document.

    Requirements:
    - Python packages: re, nltk, pandas, scikit-learn

    Example:
    >>> texts = ["Hello, world!", "Machine learning is great.", "Python is my favorite programming language."]
    >>> dtm = f_519(texts)
    >>> print(dtm)
    """
    cleaned_texts = [ALPHANUMERIC.sub(' ', text).lower() for text in texts]
    tokenized_texts = [' '.join(word for word in text.split() if word not in STOPWORDS) for text in cleaned_texts]

    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(tokenized_texts)
    dtm_df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())

    return dtm_df


import unittest

class TestF519(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.texts = [
            "Hello, world!",
            "Data science is about the extraction of knowledge from data.",
            "Machine learning is a fascinating field.",
            "Python is a versatile programming language.",
            "Stop words are filtered out in text preprocessing."
        ]

    def test_dtm_shape(self):
        """Ensure the DTM has the correct shape."""
        dtm = f_519(self.texts)
        self.assertEqual(dtm.shape[0], len(self.texts), "DTM should have one row per document.")

    def test_dtm_non_negative(self):
        """Ensure all values in the DTM are non-negative."""
        dtm = f_519(self.texts)
        self.assertTrue((dtm >= 0).all().all(), "All DTM values should be non-negative.")

    def test_stopwords_removal(self):
        """Check if common stopwords are removed."""
        dtm = f_519(["This is a test.", "Another test here."])
        self.assertNotIn("is", dtm.columns, "Stopwords should be removed from DTM columns.")

    def test_alphanumeric_filtering(self):
        """Verify that non-alphanumeric characters are filtered out."""
        dtm = f_519(["Example: test!", "#Another$% test."])
        self.assertFalse(any(char in dtm.columns for char in ":!#$%"), "Non-alphanumeric characters should be filtered out.")

    def test_lowercase_conversion(self):
        """Test if all text is converted to lowercase."""
        dtm = f_519(["LoWeR and UPPER"])
        self.assertIn("lower", dtm.columns, "All text should be converted to lowercase.")
        self.assertIn("upper", dtm.columns, "All text should be converted to lowercase.")


if __name__ == '__main__':
    unittest.main()
