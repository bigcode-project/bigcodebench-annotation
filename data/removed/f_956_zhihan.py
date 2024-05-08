from collections import Counter
import os
import nltk
from nltk.corpus import stopwords
import string

def f_956(directory):
    """
    Analyze a directory of text files and return the most common word and its number, excluding stopwords and punctuation.

    Parameters:
    directory (str): Path to the directory containing text files.

    Returns:
    tuple: The most common word and its count.

    Requirements:
    - collections
    - os
    - nltk.corpus.stopwords
    - string

    Example:
    >>> f_956('./text_files')
    ('example', 10) # This is just a mock output; real output will depend on text files' content.
    """

    # Constants
    STOPWORDS = set(stopwords.words('english'))

    word_counter = Counter()
    
    for file in os.listdir(directory):
        if file.endswith('.txt'):
            with open(os.path.join(directory, file), 'r') as f:
                words = nltk.word_tokenize(f.read().lower())
                words = [word for word in words if word not in STOPWORDS and word not in string.punctuation]
                word_counter.update(words)
    
    common_word, count = word_counter.most_common(1)[0]
    return common_word, count

import os
import unittest

def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)

test_directory = "test_data/"


class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Testing with the sample directory containing text files
        result = f_956(test_directory)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], str)
        self.assertIsInstance(result[1], int)

    def test_case_2(self):
        # Testing with an empty directory
        empty_dir = "/mnt/data/empty_dir"
        os.makedirs(empty_dir, exist_ok=True)
        result = f_956(empty_dir)
        self.assertIsNone(result)

    def test_case_3(self):
        # Testing with a directory containing non-text files
        non_text_dir = "/mnt/data/non_text_dir"
        os.makedirs(non_text_dir, exist_ok=True)
        with open(os.path.join(non_text_dir, "image.jpg"), "wb") as f:
            f.write(b"fake_image_data")
        result = f_956(non_text_dir)
        self.assertIsNone(result)

    def test_case_4(self):
        # Testing with a directory containing only stopwords and punctuation
        stopwords_dir = "/mnt/data/stopwords_dir"
        os.makedirs(stopwords_dir, exist_ok=True)
        with open(os.path.join(stopwords_dir, "stopwords.txt"), "w") as f:
            f.write("and or but, if!")
        result = f_956(stopwords_dir)
        self.assertIsNone(result)

    def test_case_5(self):
        # Testing with a non-existent directory
        with self.assertRaises(FileNotFoundError):
            f_956("/mnt/data/non_existent_dir")
if __name__ == "__main__":
    run_tests()