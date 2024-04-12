import random
import re

# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def f_695(n_sentences):
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
    >>> result = f_695(2)
    >>> print(result)
    sample sample including contains text text text including sample including. words sample words several sample sample sample text text words
    
    Note: 
    - The actual output will vary due to the randomness of sentence generation.
    """
    sentences = []
    for _ in range(n_sentences):
        sentence_len = random.randint(5, 10)
        # Ensuring that each sentence has only one period at the end
        sentence = " ".join(random.choice(WORD_LIST) for _ in range(sentence_len)).rstrip('.') + "."
        sentences.append(sentence)

    text = " ".join(sentences)
    # Removing all non-alphanumeric characters except spaces and periods
    text = re.sub('[^\s\w.]', '', text).lower().strip()
    # Ensuring that each sentence ends with a period by stripping any extra spaces and splitting correctly
    text = '. '.join([sentence.strip() for sentence in text.split('.') if sentence])

    return text

import unittest

class TestCases(unittest.TestCase):
    # Test case 1: Validate that a single sentence is generated correctly
    def test_single_sentence(self):
        result = f_695(1)
        self.assertIsInstance(result, str, "The output should be a string.")
        self.assertEqual(result.count('.'), 1, "There should be exactly one period in a single sentence.")
        self.assertTrue(result.endswith('.'), "The sentence should end with a period.")
        self.assertTrue(result.islower(), "The sentence should be in lowercase.")
        self.assertTrue(all(c.isalnum() or c.isspace() or c == '.' for c in result), "The sentence should only contain alphanumeric characters, spaces, and periods.")

    # Test case 2: Validate that multiple sentences are generated correctly
    def test_multiple_sentences(self):
        result = f_695(5)
        self.assertEqual(result.count('.'), 5, "There should be exactly five periods for five sentences.")
        self.assertTrue(all(sentence.strip().endswith('.') for sentence in result.split('  ')), "Each sentence should end with a period.")

    # Test case 3: Validate that no sentence is generated when zero is specified
    def test_no_sentences(self):
        result = f_695(0)
        self.assertEqual(result, '', "The output should be an empty string when no sentences are requested.")

    # Test case 4: Validate the randomness of generated sentences
    def test_randomness(self):
        result1 = f_695(2)
        result2 = f_695(2)
        self.assertNotEqual(result1, result2, "The sentences should be randomly generated and thus not equal.")

    # Test case 5: Validate that the length of a sentence is within the expected range
    def test_sentence_length(self):
        result = f_695(1)
        words = result[:-1].split()  # Remove period and split by spaces
        self.assertTrue(5 <= len(words) <= 10, "The sentence should have 5 to 10 words.")
    
def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)
if __name__ == "__main__":
    run_tests()