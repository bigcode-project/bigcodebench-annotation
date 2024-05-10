import collections
import random
import itertools


ANIMALS = ['Cat', 'Dog', 'Elephant', 'Lion', 'Tiger', 'Bear', 'Giraffe', 'Horse', 'Rabbit', 'Snake', 'Zebra']

def f_313(animal_dict, max_count=10, seed=0):
    """
    Given a constant list of animals in ANIMALS, and a dictionary 'animal_dict' with keys as people's names and values
    as their favorite animal names, reverse the keys and values in a given dictionary and count the occurrences of each
    predefined animal name with a random count. Return the reversed dictionary and the counter with animal name
    occurrences.

    This function performs two tasks:
    1. It reverses the given dictionary (animal_dict) such that the original values become keys and the original 
    keys become lists of values.
    2. It counts the occurrences of each animal name in a predefined list (ANIMALS). The count of each animal name
    is a random integer between 1 and max_count (inclusive).

    Parameters:
    animal_dict (dict): A dictionary with keys as names and values as animal names.
    max_count (int, Optional): A positive integer denoting the maximum count of each animal. Default is 10.
    Must be greater than 0.
    seed (int, Optional): An integer to seed the random number generator. Default is 0.

    Returns:
    tuple: A tuple where the first element is a reversed dictionary and the second element is a counter with animal 
           name occurrences (with randomness in count).

    Requirements:
    - collections
    - random
    - itertools

    Example:
    >>> animal_dict = {'John': 'Cat', 'Alice': 'Dog', 'Bob': 'Elephant', 'Charlie': 'Lion', 'David': 'Tiger', 'Sue': 'Pangolin'}
    >>> reversed_dict, animal_counter = f_313(animal_dict, 15, 77)
    >>> reversed_dict
    {'Cat': ['John'], 'Dog': ['Alice'], 'Elephant': ['Bob'], 'Lion': ['Charlie'], 'Tiger': ['David']}
    >>> dict(animal_counter.most_common(5))
    {'Giraffe': 14, 'Cat': 13, 'Zebra': 9, 'Snake': 8, 'Elephant': 6}
    """
    if max_count < 1:
        raise ValueError("max_count must be a positive integer")

    random.seed(seed)

    reversed_dict = {v: [] for v in animal_dict.values() if isinstance(v, str) and v in ANIMALS}
    for k, v in animal_dict.items():
        if isinstance(v, str) and v in ANIMALS:
            reversed_dict[v].append(k)

    animal_counter = collections.Counter(itertools.chain.from_iterable([[v] * random.randint(1, max_count) for v in ANIMALS]))
    return reversed_dict, animal_counter


import unittest
import doctest


class TestCases(unittest.TestCase):

    def test_case_1(self):
        # Testing if the dictionary is correctly reversed
        input_dict = {'John': 'Cat', 'Alice': 'Dog', 'Bob': 'Elephant'}
        expected_output = {'Cat': ['John'], 'Dog': ['Alice'], 'Elephant': ['Bob']}
        reversed_dict, animal_counter = f_313(input_dict)
        self.assertEqual(reversed_dict, expected_output)
        self.assertEqual(set(animal_counter.keys()), set(ANIMALS))

    def test_case_2(self):
        # Testing if the animal counts are within the range of 1 to 10
        _, animal_counter = f_313({})
        for animal in ANIMALS:
            self.assertIn(animal, animal_counter)
            self.assertTrue(1 <= animal_counter[animal] <= 10)

    def test_case_3(self):
        # Testing if all predefined animals are counted
        _, animal_counter = f_313({}, 17, 42)
        target = {'Rabbit': 14, 'Elephant': 9, 'Lion': 8, 'Tiger': 8, 'Bear': 5, 'Cat': 4, 
                  'Giraffe': 4, 'Horse': 3, 'Snake': 2, 'Dog': 1, 'Zebra': 1}
        self.assertEqual(animal_counter, target)

    def test_case_4(self):
        # Testing function behavior with an empty dictionary
        expected_reversed_dict = {}
        reversed_dict, animal_counter = f_313(expected_reversed_dict)
        self.assertEqual(reversed_dict, expected_reversed_dict)
        self.assertEqual(set(animal_counter.keys()), set(ANIMALS))
        with self.assertRaises(ValueError):
            f_313(expected_reversed_dict, -1)

    def test_case_5(self):
        # Testing function behavior with a non-empty dictionary
        input_dict = {'John': 'Lion', 'Alice': 'Tiger'}
        expected_reversed_dict = {'Lion': ['John'], 'Tiger': ['Alice']}
        reversed_dict, animal_counter = f_313(input_dict)
        self.assertEqual(reversed_dict, expected_reversed_dict)
        self.assertEqual(set(animal_counter.keys()), set(ANIMALS))


def run_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCases))
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    doctest.testmod()
    run_tests()
