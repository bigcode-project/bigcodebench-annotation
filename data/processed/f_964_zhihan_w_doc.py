from collections import Counter
from operator import itemgetter
import itertools

#CONSTANT
ANIMAL = ['cat', 'camel', 'cow', 'dog', 'elephant', 'fox', 'giraffe', 'hippo', 'iguana', 'jaguar']

def f_777(animal_dict):
    """
    Given a dictionary of animals as keys and letters as values, count the frequency of each letter in the animals.
    
    Note:
    - Remove key in the dictionary if it is not an animal from ANIMAL constant

    Parameters:
    animal_dict (dict): The dictionary with animals as keys and their letters as values.
    
    Returns:
    dict: A dictionary with letters as keys and their frequencies as values, sorted in descending order by frequency. Format: {letter: frequency}.
    
    Requirements:
    - collections.Counter
    - operator.itemgetter
    - itertools
    
    Example:
    >>> animal_dict = {'cat': 'c', 'dog': 'd', 'elephant': 'e', 'fox': 'f', 'giraffe': 'g', 'hippo': 'h', 'iguana': 'i', 'jaguar': 'j'}
    >>> counts = f_777(animal_dict)
    >>> print(counts)
    {'a': 7, 'g': 4, 'o': 3, 'e': 3, 'p': 3, 'f': 3, 'i': 3, 't': 2, 'h': 2, 'n': 2, 'r': 2, 'u': 2, 'c': 1, 'd': 1, 'l': 1, 'x': 1, 'j': 1}
    """
    animal_dict_copy = {}
    for i in animal_dict:
        if i in ANIMAL:
            animal_dict_copy[i] = animal_dict[i]
    letters = list(itertools.chain.from_iterable(animal_dict_copy.keys()))
    count_dict = dict(Counter(letters))
    sorted_dict = dict(sorted(count_dict.items(), key=itemgetter(1), reverse=True))
    return sorted_dict

import unittest
from collections import Counter
class TestCases(unittest.TestCase):
    def test_case_1(self):
        # Input: A dictionary with multiple animal names and their initial letters.
        animal_dict = {'cat': 'c', 'dog': 'd', 'elephant': 'e', 'fox': 'f'}
        expected_output = dict(Counter('catdogelephantfox'))
        self.assertDictEqual(f_777(animal_dict), expected_output)
    def test_case_2(self):
        # Input: An empty dictionary.
        animal_dict = {}
        expected_output = {}
        self.assertDictEqual(f_777(animal_dict), expected_output)
    def test_case_3(self):
        # Input: A dictionary with one animal name and its initial letter.
        animal_dict = {'cat': 'c'}
        expected_output = {'c': 1, 'a': 1, 't': 1}
        self.assertDictEqual(f_777(animal_dict), expected_output)
    def test_case_4(self):
        # Input: A dictionary with animal names having repetitive initial letters.
        animal_dict = {'cat': 'c', 'camel': 'c', 'cow': 'c'}
        expected_output = dict(Counter('catcamelcow'))
        self.assertDictEqual(f_777(animal_dict), expected_output)
    def test_case_5(self):
        # Input: A dictionary with non-animal words and their initial letters.
        animal_dict = {'hello': 'h', 'world': 'w'}
        expected_output = {}
        self.assertDictEqual(f_777(animal_dict), expected_output)
