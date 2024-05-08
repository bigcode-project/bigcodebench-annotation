import random
import re

# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def f_707(n_sentences):
    """
    Generate a string of random sentences using a predefined word list. 
    Each sentence is guaranteed to have one period at the end, and no period within the sentence.
    The generated sentences will be concatenated into a single string, 
    with all letters in lowercase and all non-alphanumeric characters except spaces removed.

    Parameters:
    - n_sentences (int): The number of sentences to generate.

    Returns:
    - str: A string containing the generated sentences in lowercase 
         with non-alphanumeric characters removed (except for single periods ending sentences).
    
    Requirements:
    - random
    - re
    
    Example:
    >>> random.seed(42)
    >>> result = f_707(2)
    >>> print(result)
    sample sample including contains text text text including sample including. words sample words several sample sample sample text text words.
    
    Note: 
    - The actual output will vary due to the randomness of sentence generation.
    """
    sentences = []
    for _ in range(n_sentences):
        sentence_len = random.randint(5, 10)
        sentence = " ".join(random.choice(WORD_LIST) for _ in range(sentence_len)) + "."
        sentences.append(sentence)
    text = " ".join(sentences)
    text = re.sub(r'[^\w\s.]', '', text).lower()
    text = re.sub(r'\s+\.', '.', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

import unittest
import re
class TestCases(unittest.TestCase):
    def test_single_sentence(self):
        result = f_707(1)
        self.assertIsInstance(result, str)
        self.assertEqual(result.count('.'), 1)
        self.assertTrue(result.endswith('.'))
        self.assertTrue(all(c.isalnum() or c.isspace() or c == '.' for c in result))
    def test_multiple_sentences(self):
        result = f_707(3)
        # Ensure the text ends with a period for accurate splitting
        self.assertTrue(result.endswith('.'), "The generated text should end with a period.")
        # Split the sentences properly by using regex that keeps the period with each sentence
        sentences = re.split(r'(?<=\.)\s+', result.strip())
        self.assertEqual(len(sentences), 3, "There should be exactly three sentences.")
        # Check that each sentence (excluding the last split empty due to trailing period) ends with a period
        self.assertTrue(all(sentence.endswith('.') for sentence in sentences), "Each sentence should end with a period.")
    def test_no_sentences(self):
        result = f_707(0)
        self.assertEqual(result, '')
    def test_randomness(self):
        random.seed(42)  # Set seed for reproducibility in testing
        result1 = f_707(2)
        random.seed(42)
        result2 = f_707(2)
        self.assertEqual(result1, result2)
    def test_sentence_length(self):
        result = f_707(1)
        words = result[:-1].split()  # Remove period and split by spaces
        self.assertTrue(5 <= len(words) <= 10)
