import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def f_103(text):
    """
    Create a word cloud from text after removing URLs and plot it.

    Parameters:
    - text (str): The text to analyze.

    Returns:
    WordCloud object: The generated word cloud.
    Raises:
    ValueError("No words available to generate a word cloud after removing URLs."): If there are no words available to generate a word cloud after removing URLs.

    Requirements:
    - re
    - wordcloud.WordCloud
    - matplotlib.pyplot

    Example:
    >>> print(f_103('Visit https://www.python.org for more info. Python is great. I love Python.').words_)
    {'Python': 1.0, 'Visit': 0.5, 'info': 0.5, 'great': 0.5, 'love': 0.5}
    >>> print(f_103('Check out this link: http://www.example.com. Machine learning is fascinating.').words_)
    {'Check': 1.0, 'link': 1.0, 'Machine': 1.0, 'learning': 1.0, 'fascinating': 1.0}
    """
    # Remove URLs
    text = re.sub(r"http[s]?://\S+", "", text)
    if not text.strip():  # Check if text is not empty after URL removal
        raise ValueError(
            "No words available to generate a word cloud after removing URLs."
        )
    # Generate word cloud
    wordcloud = WordCloud().generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud)
    plt.axis("off")  # Do not show axis to make it visually appealing
    return wordcloud


import unittest


class TestCases(unittest.TestCase):
    """Test cases for the f_103 function."""

    def test_case_1(self):
        text = (
            f"Visit https://www.example1.com for more info. This is the first sentence."
        )
        result = f_103(text)
        self.assertIsInstance(result, WordCloud)
        self.assertNotIn("https://www.example1.com", result.words_)

    def test_case_2(self):
        text = f"Check out this link: https://www.example2.com. This is the second sentence."
        result = f_103(text)
        self.assertIsInstance(result, WordCloud)
        self.assertNotIn("https://www.example2.com", result.words_)

    def test_case_3(self):
        text = "There is no url in this sentence."
        result = f_103(text)
        self.assertIsInstance(result, WordCloud)

    def test_case_4(self):
        text = "https://www.example4.com"
        with self.assertRaises(ValueError) as context:
            f_103(text)
        self.assertEqual(
            str(context.exception),
            "No words available to generate a word cloud after removing URLs.",
        )

    def test_case_5(self):
        text = f"Check https://www.example51.com and also visit https://www.example52.com for more details. This is the fifth sentence."
        result = f_103(text)
        self.assertIsInstance(result, WordCloud)
        self.assertNotIn("https://www.example51.com", result.words_)


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
